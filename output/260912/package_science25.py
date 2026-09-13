"""Synchronize this draft's master and derivatives, never grant release approval."""
from pathlib import Path
from decimal import Decimal
from collections import Counter
import hashlib
import json
import re

root = Path(__file__).resolve().parent
base = '260912_01_science_midterm25'
qpath, apath = root/(base+'_questions.md'), root/(base+'_answers.md')
q, a = qpath.read_text(encoding='utf-8'), apath.read_text(encoding='utf-8')
markers = ['<!-- SCIENCE25:QUESTIONS:START -->', '<!-- SCIENCE25:QUESTIONS:END -->',
           '<!-- SCIENCE25:ANSWERS:START -->', '<!-- SCIENCE25:ANSWERS:END -->']
assert all(m not in q+a for m in markers)
qid = [int(n) for n in re.findall(r'^\*\*(\d+)\.\*\*', q, re.M)]
aid = [int(n) for n in re.findall(r'^\| (\d+) \| \*\*', a, re.M)]
essay_ids = [int(n) for n in re.findall(r'^### (\d+) ', a, re.M)]
assert essay_ids == list(range(21,26)), essay_ids
expected = list(range(1,26))
assert qid == aid == expected, (qid, aid)
scores = [Decimal(x) for x in re.findall(r'^\*\*\d+\.\*\*.*?\(([\d.]+)점\)', q, re.M)]
assert len(scores) == 25 and sum(scores) == 100, scores
assert sum(scores[:20]) == 60 and sum(scores[20:]) == 40
master = markers[0]+'\n'+q+markers[1]+'\n\n'+markers[2]+'\n'+a+markers[3]+'\n'
mpath = root/(base+'.md')
mpath.write_text(master, encoding='utf-8', newline='\n')
loaded = mpath.read_text(encoding='utf-8')
for path, start, end, original in [(qpath,markers[0],markers[1],q),(apath,markers[2],markers[3],a)]:
    derived = loaded.split(start+'\n',1)[1].split(end,1)[0]
    assert derived == original
    # Preserve existing byte encoding/newlines when normalized content is identical.
    assert path.read_text(encoding='utf-8') == derived
report = {'status':'structural-only-not-release-approval', 'expected':expected,
          'questions_observed':qid, 'answers_observed':aid,
          'duplicates':[n for n,c in Counter(qid).items() if c>1],
          'missing':sorted(set(expected)-set(qid)), 'extra':sorted(set(qid)-set(expected)),
          'scores':list(map(str,scores)), 'total':str(sum(scores)),
          'derived_content_equal':True, 'warnings':[],
          'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (mpath,qpath,apath)}}
out=root/'rev'/'260912_06_science_package_check.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
