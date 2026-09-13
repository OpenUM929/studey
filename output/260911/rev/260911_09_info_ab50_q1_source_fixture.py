"""Author tests of an unapplied candidate; not independent approval."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
p=HERE/'260911_09_info_ab50_q1_source_candidate.py'
spec=importlib.util.spec_from_file_location('candidate',p)
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
results=[]
def reject(name, fn):
    try: fn()
    except (ValueError, OSError): results.append({'case':name,'rejected':True}); return
    raise AssertionError('missed: '+name)

ids=['F-2024','M-2024']
rows=[('F-2024',5,4),('M-2024',5,4)]
tiers=[('T1',2),('T2',2),('T3',2),('T4',2)]
def run(r=rows,t=(10,8,2),ts=tiers,o=2):
    return c.validate_aggregate(ids,r,t,ts,o)
assert run()['fit_fraction']=='4/5'
results.append({'case':'normal','passed':True})
reject('missing',lambda:run(rows[:1]))
reject('duplicate',lambda:run(rows+[rows[0]]))
reject('same_count_replacement',lambda:run([rows[0],('M-2025',5,4)]))
reject('extra',lambda:run(rows+[('F-2025',0,0)]))
reject('sum',lambda:run(t=(11,8,3)))
reject('fit_above_n',lambda:run([('F-2024',5,6),('M-2024',5,2)]))
reject('negative',lambda:run(o=-1))
reject('noninteger',lambda:run(o=2.0))
reject('residual',lambda:run(t=(10,8,1)))
reject('tier_total',lambda:run(ts=[('T1',1),('T2',2),('T3',2),('T4',2)]))
reject('tier_duplicate',lambda:run(ts=[('T1',2)]*4))
reject('outside',lambda:run(o=1))
reject('zero_fit',lambda:run(t=(10,0,10)))
source={'EX-info-20252F':'F-2025','EX-info-20252M':'M-2025'}
assert c.expected_strata(source,dict.fromkeys(source,'eligible'))==['F-2025','M-2025']
for status in ['partial','unresolved','invented']:
 reject(status,lambda status=status:c.expected_strata(source,dict.fromkeys(source,status)))
reject('missing_disposition',lambda:c.expected_strata(source,{}))
reject('all_nonapplicable',lambda:c.expected_strata(source,dict.fromkeys(source,'not-applicable')))
with tempfile.TemporaryDirectory() as tmp:
 root=Path(tmp); uid='EX-info-20252F'; d=root/uid; d.mkdir()
 (d/'meta.yml').write_text('exam_code: "2025-2F"\n',encoding='utf-8')
 (d/'transcript.md').write_text('fixture only',encoding='utf-8')
 snapshot={uid:{n:{'bytes':len((d/n).read_bytes()),'sha256':hashlib.sha256((d/n).read_bytes()).hexdigest()} for n in ['meta.yml','transcript.md']}}
 assert c.frozen_source(root,snapshot)[0][uid]=='F-2025'
 (d/'transcript.md').write_text('drift',encoding='utf-8')
 reject('source_drift',lambda:c.frozen_source(root,snapshot))
 (root/'EX-info-20252M').mkdir()
 reject('source_added',lambda:c.frozen_source(root,snapshot))
 reject('source_missing',lambda:c.frozen_source(root/uid,snapshot))
# Full live source bytes and metadata only: no invented eligibility approval.
snapshot={}
for line in (HERE/'260911_04_info_ab50_repair_spec.md').read_text(encoding='utf-8').splitlines():
 if line.startswith('| EX-'):
  uid,tb,th,mb,mh=[x.strip() for x in line.strip('|').split('|')]
  if uid in snapshot: raise AssertionError('duplicate snapshot row')
  snapshot[uid]={'transcript.md':{'bytes':int(tb),'sha256':th},'meta.yml':{'bytes':int(mb),'sha256':mh}}
strata,coverage=c.frozen_source(ROOT/'corpus',snapshot)
reject('live_unresolved_not_pass',lambda:c.expected_strata(strata,dict.fromkeys(strata,'unresolved')))
print(json.dumps(dict(tests=results,failures=0,live_source_coverage=coverage,
                     source_metadata_strata=sorted(set(strata.values())),
                     files_checked=len(snapshot)*2,
                     official_eligibility='UNRESOLVED; no dispositions signed here'),indent=2))