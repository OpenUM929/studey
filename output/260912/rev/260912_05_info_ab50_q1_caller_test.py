"""Real CLI input failures + unchanged assurance checks around staged command.

Only the proposed production paths are redirected inside an isolated caller block;
neither production caller nor its contract supply path is installed.
"""
import ast
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = '260912_05_info_ab50_q1_'
CANDIDATE = HERE / (P + 'repaired_candidate.py')
CONTRACT = HERE / (P + 'source_contract.json')
data = json.loads(CONTRACT.read_text(encoding='utf-8'))
first = next(iter(data['snapshot']))
cases = []
before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in
          [ROOT / 'tools/check_assurance_contract.py', ROOT / 'tools/regen_rubric_values.py',
           ROOT / 'tools/measure_score_bands.py', ROOT / 'analysis/catalog/DIFFICULTY_RUBRIC.md']}


def run_case(name, args, want):
    cmd = [sys.executable, str(CANDIDATE)] + args
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True)
    out = result.stdout.decode('utf-8')
    err = result.stderr.decode('utf-8')
    markers = re.findall(r'(?<![A-Za-z_])contract_exit=(\d+)', out)
    assert result.returncode == want and markers == [str(want)], (name, result.returncode, out, err)
    assert not err and out.rstrip().endswith('contract_exit=' + str(want)), (name, err)
    cases.append(dict(id=name, command=cmd, exit=result.returncode, stdout=out, stderr=err))
    return result


with tempfile.TemporaryDirectory(prefix='ab50-input-') as tmp:
    folder = Path(tmp)
    run_case('no_arguments', [], 2)
    run_case('missing_contract', ['--source-contract', str(folder / 'absent.json')], 2)
    unresolved = run_case('unresolved_real_snapshot', ['--source-contract', str(CONTRACT)], 1)
    variants = dict(malformed=b'{', invalid_utf8=b'\xff', root_array=b'[]', null=b'null')
    for name in ('hash_drift', 'missing_unit', 'unknown_state', 'state_array', 'snapshot_array', 'extra_field', 'mixed_partial'):
        value = copy.deepcopy(data)
        if name == 'hash_drift': value['snapshot'][first]['meta.yml']['sha256'] = '0' * 64
        if name == 'missing_unit': del value['dispositions'][first]
        if name == 'unknown_state': value['dispositions'][first] = 'invented'
        if name == 'state_array': value['dispositions'] = []
        if name == 'snapshot_array': value['snapshot'] = []
        if name == 'extra_field': value['approval'] = True
        if name == 'mixed_partial': value['dispositions'][first] = 'partial'
        variants[name] = json.dumps(value).encode('utf-8')
    for name, content in variants.items():
        path = folder / (name + '.json')
        path.write_bytes(content)
        run_case(name, ['--source-contract', str(path)], 1 if name == 'mixed_partial' else 2)
    # Synthetic eligibility is ONLY a measurement execution control, not evidence.
    synthetic = copy.deepcopy(data)
    synthetic['dispositions'] = {u: 'eligible' for u in synthetic['snapshot']}
    path = folder / 'synthetic-eligible.json'
    path.write_text(json.dumps(synthetic), encoding='utf-8')
    measured = run_case('synthetic_eligible_live_measurement', ['--source-contract', str(path)], 1)
    assert '[WARN]' in measured.stdout.decode('utf-8')

    caller_text = (HERE / (P + 'assurance_candidate.py')).read_text(encoding='utf-8')
    base_text = (ROOT / 'tools/check_assurance_contract.py').read_text(encoding='utf-8')
    def block(text):
        return next(n for n in ast.parse(text).body if isinstance(n, ast.If) and
                    isinstance(n.test, ast.Call) and isinstance(n.test.func, ast.Name) and n.test.func.id == 'all')
    node = block(caller_text)
    old = block(base_text)
    # Only subprocess argv may change. Every pre-existing caller check is identical.
    old_call = next(n for n in ast.walk(old) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'run')
    new_call = next(n for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'run')
    normalized = copy.deepcopy(node)
    next(n for n in ast.walk(normalized) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'run').args = copy.deepcopy(old_call.args)
    assert ast.dump(normalized) == ast.dump(old)
    caller_cases = []
    real_run = subprocess.run
    for name, staged_contract in [('unresolved', CONTRACT), ('absent', folder / 'absent.json'), ('measurement_warn', path)]:
        failures = []
        commands = []
        def staged_run(cmd, **kwargs):
            assert cmd == [sys.executable, str(ROOT / 'tools/regen_rubric_values.py'),
                           '--source-contract', str(ROOT / 'analysis/info_ab50_source_contract.json')]
            forwarded = [cmd[0], str(CANDIDATE), cmd[2], str(staged_contract)]
            commands.append(dict(proposed=cmd, staged=forwarded))
            return real_run(forwarded, **kwargs)
        namespace = dict(ROOT=ROOT, sys=sys, RULER_SUBJECTS=list(before), fail=failures.append)
        # The imported subprocess module is temporarily redirected only at this boundary.
        subprocess.run = staged_run
        try:
            exec(compile(ast.Module(body=[node], type_ignores=[]), '<isolated-caller-block>', 'exec'), namespace)
        finally:
            subprocess.run = real_run
        assert failures and any('exit=' in f for f in failures)
        assert any('stale' in f for f in failures)
        if name != 'measurement_warn': assert any('detector' in f for f in failures)
        if name == 'measurement_warn': assert any('warning line' in f for f in failures)
        caller_cases.append(dict(id=name, commands=commands, failures=failures,
                                 exit=namespace['proc'].returncode,
                                 stdout=namespace['out']))

assert before == {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in before}
assert set(data['snapshot']) == set(data['dispositions'])
sidecar = json.loads((HERE / (P + 'source_evidence.json')).read_text(encoding='utf-8'))
assert set(sidecar['units']) == set(data['snapshot'])
assert all(x['printed_id_coverage']['expected'] is None and x['eligibility_approval'] is None for x in sidecar['units'].values())
result = dict(scope='author-only CLI/caller tests; staged paths; no approval',
              cli_cases=cases, caller_cases=caller_cases, failures=0, stderr_warnings=0,
              caller_checks_ast_unchanged=True, protected_unchanged=True,
              source_evidence_unit_coverage=dict(expected=sorted(data['snapshot']), observed=sorted(sidecar['units']),
                                                 duplicates=[], missing=[], extra=[]))
if '--no-save' not in sys.argv:
    (HERE / (P + 'caller_result.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(cli_cases=len(cases), caller_cases=len(caller_cases), failures=0,
                      stderr_warnings=0, caller_checks_ast_unchanged=True, protected_unchanged=True)))
