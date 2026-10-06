#!/usr/bin/env python3
"""Ms Stimme für das Briefing, robust erzeugt (Chatterbox Multilingual + Kontrolle per Spracherkennung).

Aufruf (Umgebung mit torch, chatterbox-tts, faster-whisper):
  python tools/tts_robust.py <Referenz.wav> <Ausgabeordner> [Indizes, z. B. 3,7]
Danach: python3 tools/tts.py --wavdir <Ausgabeordner>

Ablauf je Szenentext:
  1. Text aufbereiten (Zahlen, Abkürzungen, Namen phonetisch für eine deutsche Stimme).
  2. Ganzen Text am Stück erzeugen (natürlicher Fluss), bis zu 4 Versuche.
  3. Jeden Versuch per Spracherkennung (faster-whisper, Wort-Zeitmarken) gegen den Soll-Text prüfen:
     fehlende oder zusätzliche Wörter senken die Wertung; Eigennamen zählen nicht (die Erkennung kennt sie nicht).
  4. Alles nach dem letzten Soll-Wort wird abgeschnitten (erfundene Silben, Atemgeräusche am Ende).
  5. Klappt es am Stück nicht, Satz für Satz mit je bis zu 5 Versuchen.
Referenzstimme: synthetische Studiostimme (XTTS-v2-Sprecherin), keine echte Person.
"""
import os, re, sys, difflib
import torch, torchaudio as ta
sys.path.insert(0, os.path.dirname(__file__))
import tts
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from faster_whisper import WhisperModel

NUM = {1:'eins',2:'zwei',3:'drei',4:'vier',5:'fünf',6:'sechs',7:'sieben',8:'acht',9:'neun',10:'zehn',11:'elf',12:'zwölf',13:'dreizehn',
       14:'vierzehn',15:'fünfzehn',16:'sechzehn',17:'siebzehn',18:'achtzehn',19:'neunzehn',20:'zwanzig',21:'einundzwanzig',22:'zweiundzwanzig',30:'dreißig',45:'fünfundvierzig'}
# Aussprache: Namen so geschrieben, wie eine deutsche Stimme sie richtig spricht
SAY = [(r'\bMr\. ', 'Mister '), ('00-Einheit', 'Doppelnull-Einheit'), ('Doppelnull-Einheit. Hier spricht M.', 'Doppel-Null-Einheit. Hier spricht Emm.'),
       ('Kennwort: VESPER', 'Kennwort: Wesper'), (r'\bVESPER\b', 'Wesper'), (r'\bVesper\b', 'Wesper'), ('SPECTRE', 'Spekter'),
       (r'\b2006\b', 'zweitausendsechs'), ('Le Chiffre', 'Lö Schiffre'), ('Cheb', 'Chepp'), ('Tržiště', 'Trschischtje'),
       ('Vítkov', 'Wiitkoff'), ('Planá', 'Plahna'), ('Strahov', 'Strachoff'), ('Karlín', 'Karliin'), ('Barrandov', 'Barrandoff'),
       ('Danube House', 'Dänjub Haus'), ('Splendide', 'Splondiehd'), ('Straight Flush', 'Streht Flasch'), ('Casino Royale', 'Kasino Roajal'),
       (r'\bBond\b', 'Bond'), ('Quantum', 'Kwantum'), ('Pupp', 'Pupp')]
NAMES = {'chepp','trschischtje','wiitkoff','plahna','strachoff','karliin','barrandoff','dänjub','splondiehd','streht','flasch','lö','schiffre',
         'kwantum','spekter','wesper','loket','pupp','kasino','roajal','emm','m'}

def norm(t):
    t = re.sub(r'^M:\s*', '', t)
    t = re.sub(r'\b(\d{1,2}):(\d{2})\b', lambda m: f"{NUM.get(int(m[1]), m[1])} Uhr" + ('' if m[2] == '00' else f" {NUM.get(int(m[2]), m[2])}"), t)
    t = t.replace('Mio. $', 'Millionen Dollar')
    t = re.sub(r'[„“"]', '', t).replace(' · ', ', ')
    for a, b in SAY: t = re.sub(a, b, t)
    return t

def words(t):
    return re.sub(r'[^a-zäöüß ]', ' ', t.lower().replace('-', ' ')).split()

def sentences(t):
    out = []
    for p in re.split(r'(?<=[.!?])\s+', t.strip()):
        if out and (len(p) < 18 or len(out[-1]) < 25): out[-1] += ' ' + p
        else: out.append(p)
    return out

def judge(asr, ref_text, wav, sr):
    """Wertung 0..1 und gekürzter Clip (bis zum letzten Soll-Wort)."""
    seg, _ = asr.transcribe(wav, language='de', beam_size=5, word_timestamps=True)
    hw = [w for s in seg for w in s.words]
    hyp = [re.sub(r'[^a-zäöüß]', '', w.word.lower()) for w in hw]
    ref = [w for w in words(ref_text)]
    keep = lambda ws: [w for w in ws if w and w not in NAMES and not w.isdigit()]
    r2, h2 = keep(ref), keep(hyp)
    sm = difflib.SequenceMatcher(None, r2, h2)
    extra = sum((j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op in ('insert', 'replace') and (j2 - j1) > (i2 - i1))
    score = sm.ratio() - 0.12 * extra
    # Ende: letztes Erkennungswort, das zu den letzten Soll-Wörtern passt
    end = None
    tail = set(ref[-3:])
    for k in range(len(hw) - 1, -1, -1):
        if hyp[k] in tail or difflib.SequenceMatcher(None, hyp[k], ref[-1]).ratio() > .6:
            end = hw[k].end; break
    if end is None and hw: end = hw[-1].end
    a, s0 = ta.load(wav)
    if end is not None:
        cut = min(a.shape[-1], int((end + 0.12) * s0))
        a = a[:, :cut]
        fade = min(int(0.04 * s0), a.shape[-1])
        a[:, -fade:] *= torch.linspace(1, 0, fade)
    return score, a, ' '.join(w.word for w in hw)

def main(ref, outdir, only=None):
    os.makedirs(outdir, exist_ok=True)
    caps = [c for c in tts.captions(open(tts.HTML, encoding='utf-8').read()) if c]
    m = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
    asr = WhisperModel('medium', device='cpu', compute_type='int8')
    V = dict(exaggeration=0.5, cfg_weight=0.5, temperature=0.65)
    tmp = os.path.join(outdir, '_tmp.wav')
    def best_of(text, n, seed):
        best = None
        for k in range(n):
            torch.manual_seed(seed + k * 101)
            w = m.generate(text, language_id='de', audio_prompt_path=ref, **V)
            ta.save(tmp, w, m.sr)
            sc, a, hyp = judge(asr, text, tmp, m.sr)
            if best is None or sc > best[0]: best = (sc, a, hyp)
            if sc >= .97: break
        return best
    for i, c in enumerate(caps):
        if only and i not in only: continue
        f = os.path.join(outdir, f'm_{tts.key(c)}.wav')
        if os.path.exists(f) and not only: continue
        text = norm(c)
        sc, a, hyp = best_of(text, 6, 7 + i * 13)
        if sc < .95 and len(sentences(text)) > 1:
            parts = []
            for j, snt in enumerate(sentences(text)):
                s2, a2, h2 = best_of(snt, 6, 900 + i * 31 + j * 7)
                parts += [a2, torch.zeros(1, int(m.sr * 0.18))]
            a = torch.cat(parts[:-1], 1); sc = -1; hyp = '(satzweise)'
        ta.save(f, a, m.sr)
        print(i, round(sc, 2), text[:60], '=>', hyp[:90], flush=True)
    if os.path.exists(tmp): os.remove(tmp)

if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], a[1], set(int(x) for x in a[2].split(',')) if len(a) > 2 else None)
