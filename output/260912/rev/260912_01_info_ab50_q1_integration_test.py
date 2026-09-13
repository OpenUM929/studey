"""Author-only integration tests; no canonical mutations or eligibility ruling."""
import ast
import contextlib
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CANDIDATE=HERE/'260912_01_info_ab50_q1_integrated_candidate.py'
BASE=ROOT/'tools/regen_rubric_values.py'

def load(path):
    tree=ast.parse(path.read_text(encoding='utf-8'))
    # Omit stdout-wrapper and __main__ side effects; preserve function bodies.
    nodes=[n for n in tree.body if not isinstance(n,ast.If) and not
           (isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) for t in n.targets))]
    ns={'__file__':str(path),'__name__':'candidate_test'}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'),ns)
    return ns

ns=load(CANDIDATE)
protected=[ROOT/'tools/measure_score_bands.py',BASE,ROOT/'analysis/catalog/DIFFICULTY_RUBRIC.md']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
p=subprocess.run([sys.executable,'tools/measure_score_bands.py','--per-item'],cwd=ROOT,capture_output=True)
live=(p.stdout+p.stderr).decode('utf-8','replace').replace('\r\n','\n')
(HERE/'260912_01_info_ab50_measure_raw.txt').write_text(live,encoding='utf-8')
# Derive source metadata strata directly. All-source strata are diagnostic ONLY,
# not an approved set of statistically eligible units.
snapshot={}
for line in (ROOT/'output/260911/rev/260911_04_info_ab50_repair_spec.md').read_text(encoding='utf-8').splitlines():
    if line.startswith('| EX-'):
        uid,tb,th,mb,mh=[x.strip() for x in line.strip('|').split('|')]
        if uid in snapshot: raise AssertionError('duplicate input')
        snapshot[uid]={'transcript.md':{'bytes':int(tb),'sha256':th},'meta.yml':{'bytes':int(mb),'sha256':mh}}
source,coverage=ns['frozen_source'](ROOT/'corpus',snapshot)
expected=sorted(set(source.values()))
v=ns['derive'](live,expected)
assert v['source_coverage']['coverage']['missing']==[]
assert v['source_coverage']['coverage']['extra']==[]
# Original gate0 unchanged, now reachable for diagnostic six-stratum values.
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    gate0=ns['gate0'](v,{(str(x.stat().st_size),hashlib.sha256(x.read_bytes()).hexdigest()[:16]) for x in protected[:2]})
assert gate0==0,buf.getvalue()

cases=[]
def rejects(name,output=live,exp=expected):
    try: ns['derive'](output,exp)
    except (ValueError,TypeError,KeyError,AttributeError,IndexError,ZeroDivisionError,SystemExit):
        cases.append({'name':name,'rejected':True}); return
    raise AssertionError('missed '+name)
stratum=re.search(r'^([FM]-\d{4})\s+n=\d+\s+fit=\d+\s+[\d.]+%.*$',live,re.M)
assert stratum
rejects('missing_stratum',live[:stratum.start()]+live[stratum.end():])
rejects('duplicate_stratum',live+'\n'+stratum.group(0)+'\n')
rejects('same_count_replacement',live[:stratum.start()]+stratum.group(0).replace(stratum.group(1),'F-2099')+live[stratum.end():])
rejects('expected_extra',exp=expected+['M-2099'])
rejects('empty_output','')
rejects('duplicate_ALL',live+'\n'+re.search(r'^ALL\s+.*$',live,re.M).group(0)+'\n')
rejects('duplicate_outside',live+'\n'+re.search(r'^--\s+outside band.*$',live,re.M).group(0)+'\n')
rejects('missing_outside',re.sub(r'^--\s+outside band.*$','',live,flags=re.M))
rejects('duplicate_tier',live+'\n'+re.search(r'^T1\s+\[.*$',live,re.M).group(0)+'\n')
rejects('all_sum_corruption',re.sub(r'^(ALL\s+n=)(\d+)',lambda m:m[1]+str(int(m[2])+1),live,count=1,flags=re.M))

# Exercise real main branches with explicitly synthetic authority inputs.
original_tool=ns['tool_output']; original_frozen=ns['frozen_source']; argv=sys.argv[:]
with tempfile.TemporaryDirectory() as d:
    contract=Path(d)/'fixture.json'
    contract.write_text(json.dumps({'snapshot':{},'dispositions':{'fixture':'eligible'}}),encoding='utf-8')
    ns['frozen_source']=lambda root,snapshot:({'fixture':expected[0]}, {'fixture_only':True})
    sys.argv=['candidate','--source-contract',str(contract)]
    for name,output,code,want in [('live_failure',live,p.returncode,1),('empty', '',0,2),
                                  ('abort','[ABORT] fixture',1,2),('exit2','broken',2,2)]:
        ns['tool_output']=lambda output=output,code=code:(output,code)
        capture=io.StringIO()
        with contextlib.redirect_stdout(capture): got=ns['main']()
        assert got==want,(name,got)
        assert not output or output in capture.getvalue()
        cases.append({'name':'main_'+name,'exit':got})
    # All success markers but invalid schema must fail CLOSED at derive.
    output='[GATE 0 PASS] undetected=0\n[GATE 1 PASS] undetected=0\n[OK] GATE 1 undetected=0 / GATE 3 mismatches=0\n'
    ns['tool_output']=lambda:(output,0)
    with contextlib.redirect_stdout(io.StringIO()): got=ns['main']()
    assert got==2
    cases.append({'name':'main_malformed_success','exit':got})
ns['tool_output']=original_tool; ns['frozen_source']=original_frozen; sys.argv=argv
# CLI with no approved source contract: real subprocess, no mock.
q=subprocess.run([sys.executable,str(CANDIDATE)],cwd=ROOT,capture_output=True)
assert q.returncode==2
# Old and new measurement invocations are byte-equal: measurement never changed.
p2=subprocess.run([sys.executable,'tools/measure_score_bands.py','--per-item'],cwd=ROOT,capture_output=True)
assert p.returncode==p2.returncode and p.stdout==p2.stdout and p.stderr==p2.stderr
item_lines=[l for l in live.splitlines() if re.match(r'^EX-\S+\s+\d+\s+[\d.]+\s+[\d.]+\s+(T[1-4]|OUT)\s*$',l)]
assert item_lines
assert before=={str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in protected}
print(json.dumps(dict(scope='author diagnostic integration; NOT release or eligibility approval',
                     cases=cases,failures=0,original_gate0_output=buf.getvalue(),
                     live_child_exit=p.returncode,live_warnings=live.count('[WARN]'),
                     source_coverage=coverage,diagnostic_strata=expected,
                     per_item_rows=len(item_lines),measurement_byte_equal=True,
                     protected_unchanged=True,cli_without_contract=q.returncode),indent=2))