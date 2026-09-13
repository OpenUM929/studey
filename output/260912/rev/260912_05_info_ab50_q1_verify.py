"""Replay the whole author bundle and check frozen artifacts without writes to canon."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = '260912_05_info_ab50_q1_'
commands = []
for suffix, args in [('regression_test.py', ['--no-save']), ('caller_test.py', ['--no-save'])]:
    cmd = [sys.executable, str(HERE / (P + suffix))] + args
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True)
    commands.append(dict(command=cmd, exit=r.returncode,
                         stdout=r.stdout.decode('utf-8'), stderr=r.stderr.decode('utf-8')))
    assert r.returncode == 0 and not r.stderr, commands[-1]

static = []
for path in sorted(HERE.glob(P + '*.py')):
    text = path.read_text(encoding='utf-8')
    compile(text, str(path), 'exec')
    ast.parse(text)
    trailing = [i for i, line in enumerate(text.splitlines(), 1) if line.rstrip() != line]
    assert not trailing, (path, trailing)
    static.append(str(path.relative_to(ROOT)))
for base, candidate, patch in [
    ('tools/regen_rubric_values.py', 'repaired_candidate.py', 'integrated.patch'),
    ('tools/check_assurance_contract.py', 'assurance_candidate.py', 'assurance.patch')]:
    a = (ROOT / base).read_text(encoding='utf-8')
    b = (HERE / (P + candidate)).read_text(encoding='utf-8')
    expected = ''.join(difflib.unified_diff(a.splitlines(True), b.splitlines(True), fromfile='a/' + base, tofile='b/' + base))
    assert expected == (HERE / (P + patch)).read_text(encoding='utf-8')

manifest_path = HERE / (P + 'manifest.json')
manifest_checked = False
if manifest_path.exists():
    for x in json.loads(manifest_path.read_text(encoding='utf-8'))['files']:
        b = (ROOT / x['path']).read_bytes()
        assert len(b) == x['bytes'] and hashlib.sha256(b).hexdigest() == x['sha256'], x['path']
    manifest_checked = True
result = dict(scope='author verification only', commands=commands, static_compiled=static,
              exact_patches=True, unexpected_harness_warnings=0, manifest_checked=manifest_checked,
              gaps=['ruff/mypy/pytest not installed; no dependencies added',
                    'full assurance/build not run: no production changes; known global blockers remain'])
(HERE / (P + 'validation.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(commands=len(commands), exit=0, static_files=len(static), exact_patches=True,
                      unexpected_harness_warnings=0, manifest_checked=manifest_checked)))
