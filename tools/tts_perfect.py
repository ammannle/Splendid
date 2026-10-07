#!/usr/bin/env python3
"""Ms Stimme, Wort für Wort geprüft (Chatterbox Multilingual + faster-whisper).

Aufruf (Umgebung mit torch, chatterbox-tts, faster-whisper):
  python tools/tts_perfect.py <Referenz.wav> <Ausgabeordner> [Indizes, z. B. 3,7]
Danach: python3 tools/tts.py --wavdir <Ausgabeordner>

Strenger als tts_robust.py:
  - Jedes Soll-Wort muss in der Spracherkennung vorkommen (Abgleich per Ausrichtung, Beugung erlaubt),
    Eigennamen dürfen in Originalschreibweise oder Lautschrift erkannt werden.
  - Kein zusätzliches Wort, keine erfundene Silbe am Ende, keine Pause über 0,9 s, Sprechtempo plausibel.
  - Erst am Stück (bis RUNS Versuche), sonst Satz für Satz (je bis SRUNS Versuche); der zusammengesetzte
    Clip wird erneut geprüft. Nicht bestandene Szenen werden mit neuen Zufallswerten wiederholt (ROUNDS).
  - Bericht: <Ausgabeordner>/report.txt
"""
import os, re, sys, difflib
import torch, torchaudio as ta
sys.path.insert(0, os.path.dirname(__file__))
import tts
from tts_robust import NUM, SAY, norm, sentences
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from faster_whisper import WhisperModel

RUNS, SRUNS, ROUNDS = 5, 8, 4
# Eigennamen (Lautschrift): Erkennung schreibt sie verschieden, daher unscharfer Abgleich
NAMES = {'schiffre', 'lö', 'kwantum', 'spekter', 'wesper', 'splondiehd', 'roajal', 'loket', 'pupp', 'barrandoff', 'dänjub', 'emm',
         'karolinenthal', 'karlsbad', 'nassau', 'mühlbrunnkolonnade', 'veitsberg', 'pilsen', 'augsburg', 'böhmen', 'kaiserbad', 'grandhotel'}
# Lautschrift -> so schreibt die Erkennung den Namen üblicherweise
ALT = {'lö': ['le'], 'schiffre': ['chiffre', 'schiffer', 'shiffre'], 'spekter': ['spectre', 'specter', 'spektor'],
       'kwantum': ['quantum'], 'wesper': ['vesper'], 'splondiehd': ['splendide', 'splendid'], 'kasino': ['casino'],
       'roajal': ['royale', 'royal'], 'streht': ['straight', 'strait'], 'flasch': ['flush'], 'barrandoff': ['barrandov'],
       'dänjub': ['danube', 'danjub'], 'haus': ['house'], 'emm': ['m', 'em'], 'loket': ['lokett', 'locket'], 'pupp': ['pup', 'pub']}
FUNC = {'die', 'der', 'das', 'den', 'dem', 'ein', 'und', 'es', 'in', 'an', 'am', 'im', 'zu', 'um', 'so', 'ab'}

def toks(t):
    t = re.sub(r'\b00\b', 'doppelnull', t.lower())
    t = re.sub(r'doppel[\s-]*null', 'doppelnull', t).replace('-', ' ')
    t = re.sub(r'\d+', lambda m: ' ' + ({0: 'null'} | NUM).get(int(m[0]), m[0]) + ' ', t)
    t = re.sub(r'doppel[\s-]*null', 'doppelnull', t)
    t = t.replace('ß', 'ss').replace('ph', 'f')
    t = re.sub(r'c(?!h)', 'k', t)
    return [w for w in re.sub(r'[^a-zäöü ]', ' ', t).split() if w]

def same(r, h):
    """Normales Wort: gleich, oder nur die Endung weicht ab (Beugung); der Wortanfang muss stimmen."""
    if r == h: return True
    n = min(4, len(r))
    return h[:n] == r[:n] and difflib.SequenceMatcher(None, r, h).ratio() >= .8

def sim(r, h):
    best = difflib.SequenceMatcher(None, r, h).ratio()
    for a in ALT.get(r, []): best = max(best, difflib.SequenceMatcher(None, a, h).ratio())
    return best

def align(ref, hyp):
    """Globale Ausrichtung; liefert Paare (i, j) mit i/j = None für Lücken."""
    n, m = len(ref), len(hyp)
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i
    for j in range(1, m + 1): S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = sim(ref[i - 1], hyp[j - 1])
            S[i][j] = max(S[i - 1][j - 1] + (2 * s - 1), S[i - 1][j] - 1, S[i][j - 1] - 1)
    i, j, out = n, m, []
    while i or j:
        if i and j and abs(S[i][j] - (S[i - 1][j - 1] + 2 * sim(ref[i - 1], hyp[j - 1]) - 1)) < 1e-9:
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i and abs(S[i][j] - (S[i - 1][j] - 1)) < 1e-9:
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    return out[::-1]

def check(asr, text, wav):
    """Prüft einen Clip. Rückgabe: (bestanden, Wertung, Fehlerliste, Endzeit, Erkennung)."""
    seg, _ = asr.transcribe(wav, language='de', beam_size=5, word_timestamps=True, condition_on_previous_text=False)
    hw = [w for s in seg for w in s.words]
    hyp, hwi = [], []
    for k, w in enumerate(hw):
        for t in toks(w.word): hyp.append(t); hwi.append(k)
    ref = toks(text)
    # getrennt erkannte Komposita („Grand Hotel“) wieder zusammenfügen, wenn das Soll-Wort sie enthält
    rs = set(ref); j = 0
    while j < len(hyp) - 1:
        w = hyp[j] + hyp[j + 1]
        if hyp[j] not in rs and any(difflib.SequenceMatcher(None, w, r).ratio() >= .85 for r in rs):
            hyp[j:j + 2] = [w]; hwi[j:j + 2] = [hwi[j + 1]]
        else: j += 1
    errs, last = [], None
    for i, j in align(ref, hyp):
        if i is not None and j is not None:
            good = sim(ref[i], hyp[j]) >= .55 if (ref[i] in ALT or ref[i] in NAMES) else same(ref[i], hyp[j])
            if good: last = (i, j); continue
            errs.append(f'{ref[i]}≠{hyp[j]}')
        elif i is not None:
            if ref[i] in FUNC and len(ref) > 6: errs.append(f'(-{ref[i]})')   # kurzes Füllwort: leichter Fehler
            else: errs.append(f'-{ref[i]}')
        else:
            errs.append(f'+{hyp[j]}')
    hard = [e for e in errs if not e.startswith('(')]
    a, sr = ta.load(wav)
    dur = a.shape[-1] / sr
    end = hw[hwi[last[1]]].end if last else (hw[-1].end if hw else dur)
    if last and last[0] != len(ref) - 1: hard.append('ende')
    # lange Pausen und Tempo
    gaps = [hw[k + 1].start - hw[k].end for k in range(len(hw) - 1)]
    if gaps and max(gaps) > .9: hard.append(f'pause{max(gaps):.1f}')
    wps = len(ref) / max(.5, end - (hw[0].start if hw else 0))
    if wps < 1.6 or wps > 4.2: hard.append(f'tempo{wps:.1f}')
    score = 1 - .2 * len(hard) - .05 * (len(errs) - len(hard))
    return not hard, score, errs + [h for h in hard if h not in errs], end, ' '.join(w.word.strip() for w in hw)

def trim(wav, end):
    a, sr = ta.load(wav)
    a = a[:, :min(a.shape[-1], int((end + .14) * sr))]
    f = min(int(.05 * sr), a.shape[-1]); a[:, -f:] *= torch.linspace(1, 0, f)
    return a

def main(ref, outdir, only=None):
    os.makedirs(outdir, exist_ok=True)
    caps = [c for c in tts.captions(open(tts.HTML, encoding='utf-8').read()) if c]
    m = ChatterboxMultilingualTTS.from_pretrained(device='cpu')
    asr = WhisperModel('medium', device='cpu', compute_type='int8')
    V = dict(exaggeration=0.5, cfg_weight=0.5, temperature=0.6)
    tmp = os.path.join(outdir, '_tmp.wav')
    rep = open(os.path.join(outdir, 'report.txt'), 'a', encoding='utf-8')
    off = int(os.environ.get('SEEDOFF', 0))

    def gen(text, seed):
        torch.manual_seed(seed)
        w = m.generate(text, language_id='de', audio_prompt_path=ref, **V)
        ta.save(tmp, w, m.sr)
        ok, sc, errs, end, hyp = check(asr, text, tmp)
        return ok, sc, errs, trim(tmp, end), hyp

    def best_of(text, n, seed):
        best = None
        for k in range(n):
            r = gen(text, seed + k * 101)
            if best is None or r[1] > best[1]: best = r
            if r[0] and r[1] >= 1: break
        return best

    for i, c in enumerate(caps):
        if only and i not in only: continue
        f = os.path.join(outdir, f'm_{tts.key(c)}.wav')
        if os.path.exists(f) and not only: continue
        text = norm(c)
        res = None
        for rnd in range(ROUNDS):
            base = 7 + i * 13 + off + rnd * 7919
            r = best_of(text, RUNS, base)
            if res is None or r[1] > res[1]: res = r
            if res[0]: break
            if len(sentences(text)) > 1:
                parts = []
                for j, snt in enumerate(sentences(text)):
                    s = best_of(snt, SRUNS, base + 900 + j * 7)
                    parts += [s[3], torch.zeros(1, int(m.sr * .2))]
                ta.save(tmp, torch.cat(parts[:-1], 1), m.sr)
                ok, sc, errs, end, hyp = check(asr, text, tmp)
                if sc > res[1]: res = (ok, sc, errs, trim(tmp, end), hyp + ' (satzweise)')
                if res[0]: break
        ok, sc, errs, a, hyp = res
        ta.save(f, a, m.sr)
        line = f"{i:2d} {'OK ' if ok else 'XX '}{sc:.2f} {' '.join(errs) or '-'} | {hyp}"
        print(line, flush=True); rep.write(line + '\n'); rep.flush()
    if os.path.exists(tmp): os.remove(tmp)

def recheck(outdir):
    """Nur prüfen: alle vorhandenen Clips erneut gegen den Soll-Text abgleichen."""
    caps = [c for c in tts.captions(open(tts.HTML, encoding='utf-8').read()) if c]
    asr = WhisperModel('medium', device='cpu', compute_type='int8')
    bad = []
    for i, c in enumerate(caps):
        f = os.path.join(outdir, f'm_{tts.key(c)}.wav')
        if not os.path.exists(f): print(i, 'FEHLT'); bad.append(i); continue
        ok, sc, errs, end, hyp = check(asr, norm(c), f)
        print(f"{i:2d} {'OK ' if ok else 'XX '}{sc:.2f} {' '.join(errs) or '-'} | {hyp}", flush=True)
        if not ok: bad.append(i)
    print('NICHT BESTANDEN:', ','.join(map(str, bad)) or '-')

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--check': recheck(a[1]); sys.exit()
    main(a[0], a[1], set(int(x) for x in a[2].split(',')) if len(a) > 2 else None)
