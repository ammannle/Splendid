#!/usr/bin/env python3
"""Filmmusik für das Briefing einbetten.

Die Stücke wurden mit MusicGen (Meta, facebook/musicgen-small, Lizenz CC BY-NC 4.0, private Nutzung) erzeugt,
siehe Prompts in MUSIC unten. Aufruf: python3 tools/music.py <Ordner mit brief.wav, title.wav, drive.wav, casino.wav, final.wav>
Klang: Lautheit angleichen, Ein-/Ausblendung, Mono-MP3, eingebettet als <script type="application/json" id="muData">.
"""
import base64, json, os, re, subprocess, sys, tempfile

HTML = os.path.join(os.path.dirname(__file__), '..', 'operation-splendide.html')
MUSIC = {  # Schlüssel: (Prompt, Länge s, Schleife)
    'brief': ('dark suspenseful cinematic underscore, low cello drone, sparse piano notes, ticking clock percussion, slow building tension, espionage thriller film score, orchestral, no vocals', 30, True),
    'title': ('powerful cinematic spy thriller main title, bold brass stabs, driving staccato strings, timpani hits, minor key, heroic and dangerous, orchestral film score, no vocals', 22, False),
    'drive': ('driving espionage chase underscore, pulsing staccato strings ostinato, steady percussion, low brass, propulsive, minor key, cinematic orchestral, no vocals', 30, True),
    'casino': ('tense high stakes poker scene underscore, slow heartbeat bass drum, tremolo strings, dissonant piano, suspense, cinematic orchestral thriller, no vocals', 30, True),
    'final': ('cinematic spy thriller finale, resolving orchestral swell, noble brass theme, strings, timpani roll, confident ending, film score, no vocals', 22, False),
}

def main(d):
    data = {}
    with tempfile.TemporaryDirectory() as tmp:
        for k, (_, _, loop) in MUSIC.items():
            src = os.path.join(d, k + '.wav')
            if not os.path.exists(src): print('fehlt', k); continue
            out = os.path.join(tmp, k + '.mp3')
            dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout)
            af = f'highpass=f=35,loudnorm=I=-19:TP=-2,afade=t=in:d={0.05 if not loop else 0.3},afade=t=out:st={dur - (2.5 if not loop else 0.2):.2f}:d={2.5 if not loop else 0.2}'
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-af', af, '-ac', '1', '-ar', '32000', '-b:a', '56k', out], check=True)
            data[k] = base64.b64encode(open(out, 'rb').read()).decode()
            print(k, round(os.path.getsize(out) / 1024), 'KB')
    src = open(HTML, encoding='utf-8').read()
    tag = '<script type="application/json" id="muData">' + json.dumps(data, separators=(',', ':')) + '</script>'
    src = re.sub(r'<script type="application/json" id="muData">.*?</script>', lambda m: tag, src, flags=re.S) if 'id="muData"' in src else src.replace('</body>', tag + '\n</body>')
    open(HTML, 'w', encoding='utf-8').write(src)

if __name__ == '__main__':
    main(sys.argv[1])
