"""Read-only author-side consistency diagnostics. Does not certify novelty or release."""
from pathlib import Path
import hashlib,json,re
from collections import Counter

root=Path('output/260907')
baseline=json.loads((root/'260907_02_math2_revision_baseline.json').read_text(encoding='utf-8'))
coverage=json.loads((root/'260907_02_math2_coverage.json').read_text(encoding='utf-8'))
for count,path in [(25,'output/260829/260829_02_math2_comprehensive_25.md'),(40,'output/260822/공통수학2_도형의방정식_모의40.md')]:
    t=Path(path).read_text(encoding='utf-8-sig'); b=baseline[path]['text']
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==coverage[str(count)]['source_sha256']
    matches=list(re.finditer(r'^\*\*(\d+)\.\*\*',t,re.M)); ids=[m.group(1) for m in matches]
    expected=[str(i) for i in range(1,count+1)]; assert ids==expected
    types={}; tiers=[]
    for m in matches:
        block=t[m.start():].split('\n---',1)[0]
        tag=re.search(r'`?\[(SM2-[^\]\n]+)\]',block).group(1)
        types[m.group(1)]=set(re.findall(r'SM2-\d{2}',tag))
        tiers.append(re.search(r'\bT[1-4]\b',tag).group())
    rows=dict(re.findall(r'^\| (\d+) \|(.*)$',t,re.M))
    assert list(rows)==expected
    assert all(types[n]==set(re.findall(r'SM2-\d{2}',rows[n].split('|')[1])) for n in expected)
    assert set.union(*types.values())=={f'SM2-{i:02}' for i in range(1,34)}
    assert '\n---\n---\n' not in t
    for kind in ['questions','answers']:
        p=root/f'260907_02_math2_{count}_{kind}_review.md'
        v=p.read_text(encoding='utf-8'); assert '검토용·미투입' in v
        observed=re.findall(r'^\*\*(\d+)\.\*\*',v,re.M) if kind=='questions' else re.findall(r'^\| (\d+) \|',v,re.M)
        assert observed==expected
        if kind=='questions':
            assert '# 정답' not in v and not re.search(r'^\| \d+ \|',v,re.M)
    grading=list(re.finditer(r'^### (\d+)번.*$',t,re.M))
    score_totals={}
    for m in grading:
        block=t[m.start():].split('\n###',1)[0].split('\n---',1)[0]
        total=sum(map(int,re.findall(r'^- .*?… (\d+)점',block,re.M)))
        n=int(m.group(1)); wanted={21:6,22:6,23:6,24:7,25:7}[n] if count==25 else 6
        assert total==wanted,(count,n,total,wanted); score_totals[n]=total
    assert len(grading)==(5 if count==25 else 8)
    print(f'SET={count} expected={expected} observed={ids} duplicate=[] missing=[] extra=[] tag_mismatch=0 types=33 tiers={dict(Counter(tiers))} grading={score_totals}')
idx=Path('output/_index.md').read_text(encoding='utf-8')
assert len(re.findall(r'^\| SET-',idx,re.M))==65
assert not re.search(r'^\| SET-.*\| 정본 \|',idx,re.M)
print('ARTIFACT_CHECK_OK sets=2 questions=65 answers=65 grading=13 index=65 release_approved=0 warnings=0')
