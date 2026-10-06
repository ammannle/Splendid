#!/usr/bin/env python3
"""Realistische Stimmen für das Briefing mit Chatterbox Multilingual (Resemble AI, MIT-Lizenz), läuft auf CPU.

Aufruf (in einer Umgebung mit torch + chatterbox-tts):
  python tools/tts_chatterbox.py <Ausgabeordner> <Referenz-M.wav> <Referenz-Erzähler.wav>
Als Referenz dienen synthetische Piper-Stimmen (keine echten Personen). Danach:
  python3 tools/tts.py --wavdir <Ausgabeordner>
Erzeugt je Szene und Stimme <vk>_<key>.wav, Satz für Satz (stabiler), mit kurzen Pausen dazwischen.
"""
import os, re, sys
import torch, torchaudio as ta
sys.path.insert(0, os.path.dirname(__file__))
import tts
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

# Nur Zahlen, Abkürzungen und Zeichen ausschreiben; Namen bleiben im Original (das Modell spricht sie selbst)
LIGHT = [(r'\bMr\. ', 'Mister '), (r'\bD6\b', 'D sechs'), (r'\bDBS\b', 'D B S'), (r'\bQ\b', 'Kju'), ('Modul 07', 'Modul null sieben'),
         (r'\bTag 1\b', 'Tag eins'), (r'\bTag 2\b', 'Tag zwei'), (r'\bTag 3\b', 'Tag drei'), (r'\bTerminal 1\b', 'Terminal eins')]
NUM = {1:'eins',2:'zwei',3:'drei',4:'vier',5:'fünf',6:'sechs',7:'sieben',8:'acht',9:'neun',10:'zehn',11:'elf',12:'zwölf',13:'dreizehn',14:'vierzehn',
       15:'fünfzehn',16:'sechzehn',17:'siebzehn',18:'achtzehn',19:'neunzehn',20:'zwanzig',21:'einundzwanzig',22:'zweiundzwanzig',30:'dreißig',45:'fünfundvierzig'}

def norm(t):
    t = re.sub(r'^M:\s*', '', t)
    t = re.sub(r'\b(\d{1,2}):(\d{2})\b', lambda m: f"{NUM.get(int(m[1]), m[1])} Uhr" + ('' if m[2] == '00' else f" {NUM.get(int(m[2]), m[2])}"), t)
    t = t.replace('00-Einheit', 'Doppelnull-Einheit').replace('Mio. $', 'Millionen Dollar')
    t = re.sub(r'\b007\b', 'Null Null Sieben', t); t = re.sub(r'\bkm\b', 'Kilometer', t)
    t = re.sub(r'[„“"]', '', t).replace(' · ', ', ')
    for a, b in LIGHT: t = re.sub(a, b, t)
    return t

def sentences(t):
    parts = re.split(r'(?<=[.!?])\s+', t.strip())
    out = []
    for p in parts:  # sehr kurze Sätze an den vorigen hängen
        if out and len(p) < 18: out[-1] += ' ' + p
        else: out.append(p)
    return out

VOICE = {'m': dict(exaggeration=0.62, cfg_weight=0.45, temperature=0.7), 's': dict(exaggeration=0.55, cfg_weight=0.45, temperature=0.7)}

def main(outdir, ref_m, ref_s, only=None):
    os.makedirs(outdir, exist_ok=True)
    caps = tts.captions(open(tts.HTML, encoding='utf-8').read())
    model = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
    for vk, ref in (('m', ref_m), ('s', ref_s)):
        if only and vk != only: continue
        for i, c in enumerate(caps):
            if not c: continue
            f = os.path.join(outdir, f'{vk}_{tts.key(c)}.wav')
            if os.path.exists(f): continue
            torch.manual_seed(7 + i)
            pieces = []
            for snt in sentences(norm(c)):
                w = model.generate(snt, language_id='de', audio_prompt_path=ref, **VOICE[vk])
                pieces += [w, torch.zeros(1, int(model.sr * 0.2))]
            ta.save(f, torch.cat(pieces[:-1], dim=1), model.sr)
            print(vk, i, norm(c)[:70], flush=True)

if __name__ == '__main__':
    main(*sys.argv[1:4], *(sys.argv[4:5] or [None]))
