"""Proposal-only propagation fixtures. No imports/execution of canonical main."""
import ast
import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'tools/regen_rubric_values.py'
CANDIDATE = Path(__file__).with_name('260911_08_info_ab50_q1_regen_candidate.py')

class ReachedDerive(Exception):
    pass

def run(path, output, code, execution_error=False):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    def tool_output():
        if execution_error:
            raise OSError('fixture execution unavailable')
        return output, code
    def derive(out):
        raise ReachedDerive()
    namespace = {'tool_output': tool_output, 'derive': derive, 'NL': '\n'}
    exec(compile(ast.Module(body=[main], type_ignores=[]), str(path), 'exec'), namespace)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        try:
            result = namespace['main']()
        except ReachedDerive:
            result = 'derive'
        except OSError:
            result = 'uncaught'
    return result, capture.getvalue()

OK = ('[GATE 0 PASS] undetected=0\n[GATE 1 PASS] undetected=0\n'
      '[OK] GATE 1 undetected=0 / GATE 3 mismatches=0\n')
CASES = [
    ('clean_reaches_derive_not_global_pass', OK, 0, False, 'derive'),
    ('child_exit1', OK, 1, False, 1),
    ('warning_only', OK + '[WARN] duplicate candidate\n', 0, False, 1),
    ('failure_text_exit0', OK + '[FAIL] mismatch\n', 0, False, 1),
    ('partial_historical_permission_not_override', OK + '[FAIL] partial; historical permission\n', 1, False, 1),
    ('infrastructure_exit2', OK, 2, False, 2),
    ('signal_exit', OK, -9, False, 2),
    ('fixture_abort', '[ABORT] fixture regression\n', 1, False, 2),
    ('gate0_failure', '[GATE 0 FAIL]\n', 1, False, 2),
    ('empty_output', '', 0, False, 2),
    ('missing_gate1', OK.replace('[GATE 1 PASS] undetected=0\n', ''), 0, False, 2),
    ('execution_unavailable', '', 0, True, 2),
]
results=[]
for name,out,code,error,expected in CASES:
    actual,printed=run(CANDIDATE,out,code,error)
    baseline,_=run(BASE,out,code,error)
    assert actual == expected, (name,actual,expected)
    if expected in (1,2) and out:
        assert out in printed, (name,'raw output lost')
    results.append(dict(name=name,expected=expected,actual=actual,baseline=baseline))
# Live integration covers propagation only; source defects must stay visible.
p=subprocess.run([sys.executable,'tools/measure_score_bands.py'],cwd=ROOT,capture_output=True)
out=(p.stdout+p.stderr).decode('utf-8','replace').replace('\r\n','\n')
actual,printed=run(CANDIDATE,out,p.returncode)
assert actual == 1, (p.returncode,actual)
assert out in printed
report=dict(scope='Q1 propagation pilot ONLY; not full Q1 or release gate',fixtures=results,
            fixture_count=len(results),fixture_failures=0,
            live=dict(child_exit=p.returncode,contract_exit=actual,warnings=sum('[WARN]' in l for l in out.splitlines()),
                      output_sha256=hashlib.sha256(out.encode()).hexdigest()),
            protected={str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [BASE,ROOT/'tools/measure_score_bands.py',ROOT/'analysis/catalog/DIFFICULTY_RUBRIC.md']})
print(json.dumps(report,indent=2))