from pathlib import Path
import json,collections,datetime
from PIL import Image
ROOT=Path(__file__).resolve().parents[3];DIR=Path(__file__).resolve().parent;OUT=ROOT/'screenshots/cross-platform';expected=set();modes=collections.Counter();summary={}
for p in ['firefox','androidchrome']:
 rows=json.loads((DIR/(p+'-results.json')).read_text());assert len(rows)==79
 ids=[r['id'] for r in rows if r['result']=='Failed']+['screen-'+s for s in ['login','register','forgot-step1','forgot-step2','profile']]
 for r in rows:
  if r['result']!='Failed':
   stale=OUT/(p+'_'+r['id']+'.png')
   if stale.exists():stale.unlink()
 details=[]
 for id in ids:
  f=OUT/(p+'_'+id+'.png');expected.add(f.name);im=Image.open(f).convert('RGB');w,h=im.size
  if p=='androidchrome':assert (w,h)==(1080,2424),(f,im.size)
  else:assert w>=1280 and h>800,(f,im.size)
  lower=im.crop((0,h//2,w,h));small=lower.resize((max(1,w//4),max(1,h//8)),resample=Image.Resampling.NEAREST)
  yellow=sum(1 for r,g,b in small.get_flattened_data() if r>245 and g>245 and b<20)
  assert yellow>30,('Overlay not visible',f,yellow)
  meta=json.loads((DIR/(p+'-evidence-'+id+'.json')).read_text());modes[meta['mode']]+=1
  if p=='firefox':assert meta['mode']=='chrome context, real browser address bar'
  details.append({'file':f.name,'width':w,'height':h,'yellowSamples':yellow,'mode':meta['mode']})
 summary[p]={'failed':len(ids)-5,'overviews':5,'images':details}
assert {f.name for f in OUT.glob('*.png')}==expected,('Extra/missing images',expected^{f.name for f in OUT.glob('*.png')})
result={'images':len(expected),'allOverlaysVisible':True,'modes':dict(modes),'platforms':summary,'validatedAt':datetime.datetime.now().astimezone().isoformat()}
(DIR/'image-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('Verified',len(expected),'images; real browser/device capture modes; overlays visible.');print(dict(modes))
