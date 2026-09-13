"""Author regression evidence for ruling 04; never an independent approval.

--baseline records the three known failures against frozen candidate 01.
Default tests candidate 05 and writes evidence only beside this script.
"""
import ast
import contextlib
import copy
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASELINE = '--baseline' in sys.argv
PREFIX = '260912_05_info_ab50_q1_'
CANDIDATE = HERE / (('260912_01_info_ab50_q1_integrated_candidate.py') if BASELINE
                    else PREFIX + 'repaired_candidate.py')


def load(path):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    nodes = [n for n in tree.body if not isinstance(n, ast.If) and not
             (isinstance(n, ast.Assign) and any(isinstance(t, ast.Attribute) for t in n.targets))]
    ns = {'__file__': str(path), '__name__': 'author_regression'}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), ns)
    return ns


def stamp(path):
    b = path.read_bytes()
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


ruling = HERE / '260912_04_info_ab50_q1_independent_ruling.md'
frozen = json.loads(re.findall(r'```json\n(.*?)\n```', ruling.read_text(encoding='utf-8'), re.S)[0])
protected = [dict(path=k, **v) for k, v in frozen['protected'].items()]
for row in frozen['frozen'] + protected:
    assert stamp(ROOT / row['path']) == {k: row[k] for k in ('bytes', 'sha256')}, row['path']
guard = {str(p.relative_to(ROOT)): stamp(p) for p in
         list(HERE.glob('260912_0[1-4]*')) +
         [ROOT / x['path'] for x in protected] + [ROOT / 'tools/check_assurance_contract.py']}
ns = load(CANDIDATE)
snapshot = {}
for line in (ROOT / 'output/260911/rev/260911_04_info_ab50_repair_spec.md').read_text(encoding='utf-8').splitlines():
    if line.startswith('| EX-'):
        uid, tb, th, mb, mh = [x.strip() for x in line.strip('|').split('|')]
        assert uid not in snapshot
        snapshot[uid] = {'transcript.md': dict(bytes=int(tb), sha256=th),
                         'meta.yml': dict(bytes=int(mb), sha256=mh)}
source, coverage = ns['frozen_source'](ROOT / 'corpus', snapshot)
expected = sorted(set(source.values()))
raw = (HERE / '260912_01_info_ab50_measure_raw.txt').read_text(encoding='utf-8')
contract = dict(snapshot=snapshot, dispositions={u: 'eligible' for u in source})


def call(module, data, output='', child=0):
    module['tool_output'] = lambda: (output, child)
    with tempfile.TemporaryDirectory(prefix='ab50-regression-') as tmp:
        path = Path(tmp) / 'synthetic-contract.json'
        path.write_text(json.dumps(data), encoding='utf-8')
        argv = sys.argv[:]
        sys.argv = ['candidate', '--source-contract', str(path)]
        capture = io.StringIO()
        try:
            with contextlib.redirect_stdout(capture):
                code = module['main']()
        finally:
            sys.argv = argv
    return code, capture.getvalue()


def derive(output):
    return ns['derive'](output, expected) if BASELINE else ns['derive'](output, expected, list(source))


def accepts(output):
    try:
        derive(output)
        return True
    except (ValueError, TypeError, KeyError, AttributeError, IndexError, ZeroDivisionError, SystemExit):
        return False


cases = []
for status in ('partial', 'unresolved'):
    for uid in source:
        data = copy.deepcopy(contract)
        data['dispositions'][uid] = status
        code, out = call(ns, data)
        preserved = False
        if not BASELINE:
            report = next(json.loads(l) for l in out.splitlines() if l.startswith('{') and 'dispositions' in l)
            preserved = (report['dispositions'] == data['dispositions'] and
                         report['state_units'][status] == [uid] and
                         report['coverage'] == coverage and uid in report['evidence_missing'] and
                         all(v['status'] == 'not-run' for v in report['downstream'].values()))
        cases.append(dict(id='state/' + status + '/' + uid, actual=code,
                          passed=code == 1 and (BASELINE or preserved), evidence_preserved=preserved))

m = re.search(r'=== selective-score distribution ===\n(.*?)\n\n', raw, re.S)
body = m.group(1)
rows = body.splitlines()[1:]
ns['require_equal'](list(source), [r.split()[0] for r in rows])
for kind in ('delete', 'duplicate', 'same_count_replace'):
    for row in rows:
        uid = row.split()[0]
        replacement = '' if kind == 'delete' else row + '\n' + row if kind == 'duplicate' else row.replace(uid, uid + '-synthetic', 1)
        output = raw[:m.start(1)] + body.replace(row, replacement, 1) + raw[m.end(1):]
        cases.append(dict(id='distribution/' + kind + '/' + uid, passed=not accepts(output)))
normal_control = accepts(raw)

# Synthetic clean output is ONLY for terminal wiring, never source acceptance.
clean = '\n'.join(l for l in raw.splitlines() if '[WARN]' not in l and '[FAIL]' not in l)
clean += '\n[OK] GATE 1 undetected=0 / GATE 3 mismatches=0\n'
for name, want in (('ruler_stale', 1), ('local_fixture_failed', 2), ('synthetic_clean', 0)):
    mod = load(CANDIDATE)
    if name == 'local_fixture_failed':
        mod['gate0'] = lambda *args: 1
    if name == 'synthetic_clean':
        for fn in ('role_scan', 'ident_scan', 'moved_literals'):
            mod[fn] = lambda *args: []
        mod['residue_scan'] = lambda *args: ([], [])
        mod['git_baseline'] = lambda *args: (None, None)
        mod['gate0'] = lambda *args: 0
    code, out = call(mod, contract, clean)
    markers = re.findall(r'(?<![A-Za-z_])contract_exit=(\d+)', out)
    cases.append(dict(id='terminal/' + name, actual=code, markers=markers,
                      passed=code == want and markers == [str(want)]))

expected_ids = sorted(['state/' + s + '/' + u for s in ('partial', 'unresolved') for u in source] +
                      ['distribution/' + k + '/' + u for k in ('delete', 'duplicate', 'same_count_replace') for u in source] +
                      ['terminal/' + k for k in ('ruler_stale', 'local_fixture_failed', 'synthetic_clean')])
case_coverage = ns['require_equal'](expected_ids, [x['id'] for x in cases])
legacy = None
if not BASELINE:
    # Reuse every legacy assertion; only route candidate, new required unit argument,
    # and raw output destination. Do not change frozen test or saved evidence.
    path = HERE / '260912_01_info_ab50_q1_integration_test.py'
    code = path.read_text(encoding='utf-8')
    code = code.replace('260912_01_info_ab50_q1_integrated_candidate.py', CANDIDATE.name)
    code = code.replace("ns['derive'](live,expected)", "ns['derive'](live,expected,list(source))")
    code = code.replace("ns['derive'](output,exp)", "ns['derive'](output,exp,list(source))")
    with tempfile.TemporaryDirectory(prefix='ab50-legacy-') as tmp:
        dest = Path(tmp) / 'raw.txt'
        code = code.replace("(HERE/'260912_01_info_ab50_measure_raw.txt')", 'Path(' + repr(str(dest)) + ')')
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            exec(compile(code, str(path), 'exec'), {'__file__': str(path), '__name__': 'legacy_replay'})
        legacy = json.loads(capture.getvalue())
        assert dest.read_text(encoding='utf-8') == raw
    assert len(legacy['cases']) == 15 and legacy['failures'] == 0
    assert 'planted=11 undetected=0' in legacy['original_gate0_output']

assert guard == {p: stamp(ROOT / p) for p in guard}
failed = [x['id'] for x in cases if not x['passed']]
result = dict(scope='author-only regression; not independent or release approval', baseline=BASELINE,
              candidate=dict(path=str(CANDIDATE.relative_to(ROOT)), **stamp(CANDIDATE)),
              source_coverage=coverage, case_coverage=case_coverage, cases=cases,
              failed=failed, normal_control=normal_control, legacy=legacy,
              protected_and_previous_unchanged=True)
dest = HERE / (PREFIX + ('baseline_result.json' if BASELINE else 'regression_result.json'))
if '--no-save' not in sys.argv:
    dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(result=str(dest), cases=len(cases), failures=len(failed),
                      normal_control=normal_control, coverage=case_coverage,
                      legacy_cases=len(legacy['cases']) if legacy else None)))
if BASELINE:
    assert len(failed) == 302 and normal_control
else:
    assert not failed and normal_control
