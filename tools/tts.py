#!/usr/bin/env python3
"""Erzeugt Ms Sprachaufnahmen für das Missionsbriefing (Piper, neuronale Stimmen) und bettet sie in die Seite ein.

Aufruf:  python3 tools/tts.py <Ordner mit Piper-Stimmen>
         python3 tools/tts.py --wavdir <Ordner>   (fertige Aufnahmen aus tools/tts_chatterbox.py verwenden, nur Klang + Einbetten)
Benötigt: pip install piper-tts, ffmpeg, Stimmen de_DE-kerstin-low und de_DE-thorsten-high
(https://huggingface.co/rhasspy/piper-voices). Nach jeder Änderung an den Szenentexten erneut ausführen.
"""
import base64, json, os, re, subprocess, sys, tempfile, wave

HTML = os.path.join(os.path.dirname(__file__), '..', 'operation-splendide.html')
VOICES = {  # Kennung: (Modell, Sprechtempo, Bitrate)
    'm': ('de_DE-kerstin-low', 0.96, '40k'),
    's': ('de_DE-thorsten-high', 0.93, '40k'),
}
# Aussprache: englische und tschechische Namen für eine deutsche Stimme umschreiben
SAY = [
    (r"\bMr\. ", 'Mister '), (r"\bMiss ", 'Miss '), ('Le Chiffre', 'Lö Schiffre'), ('Tržiště', 'Trschischtje'),
    ('Vítkov', 'Wiitkoff'), ("Becher's", 'Bechers'), ("Gordon's", 'Gordens'), ('Kina Lillet', 'Kina Lilleh'),
    ('Body-Worlds', 'Bodie-Wörlds'), ('Danube House', 'Dänjub Haus'), ('Rebuy', 'Ri-Bai'), ('Straight Flush', 'Streht Flasch'),
    ('Skyfleet', 'Skaiflieht'), ('Broadchest', 'Brohdtschest'), ('Arlington Beech', 'Arlington Biehtsch'),
    ('D6', 'D sechs'), ('E-Vignette', 'E-Winjette'), ('Range Rover', 'Rehndsch Rower'), ('Dryden', 'Draiden'),
    (r'\bWhite\b', 'Wait'), ('Splendide', 'Splondiehd'), ('Vesper', 'Wesper'), ('Mathis', 'Matiess'),
    ('Miami', 'Maiämi'), ('Planá', 'Plahna'), ('Strahov', 'Strachoff'), ('Teplá', 'Teplah'), ('Karlín', 'Karlien'),
    ('Barrandov', 'Barrandoff'), (r'\bDBS\b', 'D B S'), (r'\bQ\b', 'Kju'), ('Cheb', 'Chepp'), ('Pupp', 'Pupp'),
    ('Gettler', 'Gettler'), ('Doppelnull', 'Doppel-Null'), ('Modul 07', 'Modul null sieben'), ('Check-in', 'Tschekinn'),
    ('checken', 'tschecken'), ('Royale', 'Roajal'), ('Chips', 'Tschips'),
]

def captions(src):
    blk = src[src.index('const SC=['):]
    blk = blk[:blk.index('\n];')]
    out = []
    for line in blk.split('\n')[1:]:
        m = re.findall(r"(?<![A-Za-z])c:'((?:[^'\\]|\\.)*)'", line)
        if m: out.append(m[-1].replace("\\'", "'"))
    return out

def key(t):  # gleiche Prüfsumme wie vxKey() in der Seite
    h = 5381
    for ch in t: h = ((h * 33) ^ ord(ch)) & 0xFFFFFFFF
    return format(h, 'x')

def norm(t):
    t = re.sub(r'^M:\s*', '', t)
    t = re.sub(r'\b(\d{1,2}):(\d{2})\b', lambda m: f"{int(m[1])} Uhr" + ('' if m[2] == '00' else f" {int(m[2])}"), t)
    t = t.replace('00-Einheit', 'Doppelnull-Einheit').replace('Mio. $', 'Millionen Dollar')
    t = re.sub(r'\b007\b', 'null null sieben', t); t = re.sub(r'\bkm\b', 'Kilometer', t)
    t = re.sub(r'[„“"]', '', t).replace(' · ', ', ')
    for a, b in SAY: t = re.sub(a, b, t)
    return t

def radio(w, mp, br, light=False):
    """light: realistische Stimme, nur sanft gefärbt (Chatterbox). Sonst Klang einer abhörsicheren Funkverbindung: Stimme etwas tiefer (Formanten bleiben), Funkband, leichte Sättigung,
    harte Kompression, Rauschteppich, Kanal öffnet mit Rauschstoß und Piepton, endet mit Quittungston."""
    sr = 'aformat=sample_rates=22050:channel_layouts=mono'
    voice = (
        (f'[0:a]{sr},highpass=f=120,lowpass=f=7000,equalizer=f=2500:t=q:w=1:g=2.5,'  # realistisch: nur sanft gefärbt
         'acompressor=threshold=-22dB:ratio=3:attack=5:release=100:makeup=2,'
         'aecho=0.9:0.35:11|23:0.08|0.05,loudnorm=I=-16:TP=-1.5,apad=pad_dur=0.12[v];' if light else
         f'[0:a]{sr},rubberband=pitch=0.94:formant=preserved,highpass=f=260,lowpass=f=3900,'
         'equalizer=f=1700:t=q:w=1:g=4,equalizer=f=500:t=q:w=1:g=-2,'
         'acompressor=threshold=-24dB:ratio=6:attack=3:release=80:makeup=4,asoftclip=type=tanh,'
         'aecho=0.9:0.4:9|17:0.12|0.07,loudnorm=I=-16:TP=-1.5,apad=pad_dur=0.12[v];'))
    fc = voice + (
        f'anoisesrc=color=white:amplitude=0.5:duration=0.09,{sr},bandpass=f=1800:width_type=h:w=2400,afade=t=out:st=0.02:d=0.07[sq];'
        f'sine=f=1450:duration=0.07,{sr},volume=0.22,afade=t=out:st=0.05:d=0.02,apad=pad_dur=0.12[b1];'
        f'sine=f=1250:duration=0.05,{sr},volume=0.2,apad=pad_dur=0.02[r1];'
        f'sine=f=880:duration=0.08,{sr},volume=0.2,afade=t=out:st=0.05:d=0.03[r2];'
        f'anoisesrc=color=white:amplitude=0.3:duration=0.1,{sr},bandpass=f=1800:width_type=h:w=2400,afade=t=out:st=0:d=0.1[sq2];'
        '[sq][b1][v][r1][r2][sq2]concat=n=6:v=0:a=1[c];'
        f'anoisesrc=color=pink:amplitude={0.006 if light else 0.012}:duration=60,{sr},highpass=f=300,lowpass=f=3500[bed];'
        '[c][bed]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.9[o]')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', w, '-filter_complex', fc, '-map', '[o]',
                    '-ac', '1', '-ar', '22050', '-b:a', br, mp], check=True)

def main(vdir, wavdir=None):
    src = open(HTML, encoding='utf-8').read()
    caps = [c for c in captions(src) if c]
    data = {}
    with tempfile.TemporaryDirectory() as tmp:
        for vk, (model, ls, br) in VOICES.items():
            data[vk] = {}
            for i, c in enumerate(caps):
                w, mp = os.path.join(tmp, 'a.wav'), os.path.join(tmp, 'a.mp3')
                if wavdir:
                    w = os.path.join(wavdir, f'{vk}_{key(c)}.wav')
                    if not os.path.exists(w): print('fehlt', vk, i, c[:40]); continue
                    radio(w, mp, br, light=True)
                    data[vk][key(c)] = base64.b64encode(open(mp, 'rb').read()).decode()
                    print(vk, i, round(os.path.getsize(mp) / 1024), 'KB'); continue
                subprocess.run([sys.executable, '-m', 'piper', '-m', os.path.join(vdir, model + '.onnx'), '-f', w,
                                '--length-scale', str(ls), '--sentence-silence', '0.22', '--noise-scale', '0.6'],
                               input=norm(c).encode(), check=True, capture_output=True)
                radio(w, mp, br)
                data[vk][key(c)] = base64.b64encode(open(mp, 'rb').read()).decode()
                print(vk, i, round(os.path.getsize(mp) / 1024), 'KB', norm(c)[:60])
    blob = json.dumps(data, separators=(',', ':'))
    tag = f'<script type="application/json" id="vxData">{blob}</script>'
    src = re.sub(r'<script type="application/json" id="vxData">.*?</script>', lambda m: tag, src, flags=re.S) \
        if 'id="vxData"' in src else src.replace('</body>', tag + '\n</body>')
    open(HTML, 'w', encoding='utf-8').write(src)
    print('eingebettet:', round(len(blob) / 1024), 'KB')

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--wavdir']: main(None, a[1])
    else: main(a[0] if a else '.')
