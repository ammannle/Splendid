#!/usr/bin/env python3
"""Erzeugt Ms Sprachaufnahmen für das Missionsbriefing (Piper, neuronale Stimmen) und bettet sie in die Seite ein.

Aufruf:  python3 tools/tts.py <Ordner mit Piper-Stimmen>
Benötigt: pip install piper-tts, ffmpeg, Stimmen de_DE-kerstin-low und de_DE-thorsten-high
(https://huggingface.co/rhasspy/piper-voices). Nach jeder Änderung an den Szenentexten erneut ausführen.
"""
import base64, json, os, re, subprocess, sys, tempfile, wave

HTML = os.path.join(os.path.dirname(__file__), '..', 'operation-splendide.html')
VOICES = {  # Kennung: (Modell, Sprechtempo, Bitrate)
    'm': ('de_DE-kerstin-low', 1.08, '32k'),
    's': ('de_DE-thorsten-high', 1.04, '40k'),
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

def main(vdir):
    src = open(HTML, encoding='utf-8').read()
    caps = captions(src)
    data = {}
    with tempfile.TemporaryDirectory() as tmp:
        for vk, (model, ls, br) in VOICES.items():
            data[vk] = {}
            for i, c in enumerate(caps):
                w, mp = os.path.join(tmp, 'a.wav'), os.path.join(tmp, 'a.mp3')
                subprocess.run([sys.executable, '-m', 'piper', '-m', os.path.join(vdir, model + '.onnx'), '-f', w,
                                '--length-scale', str(ls), '--sentence-silence', '0.32', '--noise-scale', '0.6'],
                               input=norm(c).encode(), check=True, capture_output=True)
                # Klang: Brummen weg, etwas Wärme, sanfte Kompression, kurzer Raum (Lagebesprechung)
                af = ('highpass=f=75,equalizer=f=180:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1.2:g=2,'
                      'acompressor=threshold=-20dB:ratio=3:attack=8:release=120,'
                      'aecho=0.85:0.5:38|61:0.16|0.09,loudnorm=I=-17:TP=-1.5,apad=pad_dur=0.15')
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', w, '-af', af, '-ac', '1', '-b:a', br, mp], check=True)
                data[vk][key(c)] = base64.b64encode(open(mp, 'rb').read()).decode()
                print(vk, i, round(os.path.getsize(mp) / 1024), 'KB', norm(c)[:60])
    blob = json.dumps(data, separators=(',', ':'))
    tag = f'<script type="application/json" id="vxData">{blob}</script>'
    src = re.sub(r'<script type="application/json" id="vxData">.*?</script>', lambda m: tag, src, flags=re.S) \
        if 'id="vxData"' in src else src.replace('</body>', tag + '\n</body>')
    open(HTML, 'w', encoding='utf-8').write(src)
    print('eingebettet:', round(len(blob) / 1024), 'KB')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
