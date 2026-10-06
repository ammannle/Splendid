import sys,os,re,difflib,torch,torchaudio as ta
sys.path.insert(0,'/home/user/splendid/tools');import tts,tts_chatterbox as T
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from faster_whisper import WhisperModel
m=ChatterboxMultilingualTTS.from_pretrained(device='cpu');w=WhisperModel('small',device='cpu',compute_type='int8')
caps=[c for c in tts.captions(open(tts.HTML).read()) if c];ref=sys.argv[1];out=sys.argv[2];idx=[int(x) for x in sys.argv[3].split(',')]
N=lambda t:re.sub(r'[^a-zäöüß ]','',t.lower().replace('-',' ')).split()
for i in idx:
  pieces=[]
  for sn in T.sentences(T.norm(caps[i])):
    best=None
    for k in range(6):
      torch.manual_seed(1000+i*37+k*11);a=m.generate(sn,language_id='de',audio_prompt_path=ref,**T.VOICE['m'])
      ta.save('tmp_s.wav',a,m.sr);seg,_=w.transcribe('tmp_s.wav',language='de',beam_size=5);hyp=' '.join(s.text for s in seg)
      r,h=N(sn),N(hyp);sc=difflib.SequenceMatcher(None,r,h).ratio()-max(0,len(h)-len(r))*.08
      if best is None or sc>best[0]:best=(sc,a,hyp)
      if sc>.93:break
    print(i,round(best[0],2),sn[:50],'=>',best[2][:80],flush=True);pieces+=[best[1],torch.zeros(1,int(m.sr*.16))]
  ta.save(f'{out}/m_{tts.key(caps[i])}.wav',torch.cat(pieces[:-1],1),m.sr)
