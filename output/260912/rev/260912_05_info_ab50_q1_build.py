"""Reproduce proposal-only B1/B2/B3 and caller diffs; never install them."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = '260912_05_info_ab50_q1_'


def save(name, text):
    path = HERE / (PREFIX + name)
    if path.exists():
        assert path.read_bytes() == text.encode('utf-8'), 'refuse different existing artifact: ' + str(path)
    else:
        path.write_bytes(text.encode('utf-8'))


def replace(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


old = (HERE / '260912_01_info_ab50_q1_integrated_candidate.py').read_text(encoding='utf-8')
new = replace(old, 'def expected_strata(source_strata, dispositions):',
              'class SourceIncomplete(ValueError):\n    """Valid frozen input whose official population remains unresolved."""\n\n\n'
              'def expected_strata(source_strata, dispositions):')
new = replace(new, "raise ValueError('official population unresolved')", "raise SourceIncomplete('official population unresolved')")
new = replace(new, 'def derive(out, source_expected):', 'def derive(out, source_expected, source_units):')
new = replace(new, "    rows = [l for l in dist.group(1).split(NL)[1:] if l.strip()]",
              "    if dist is None:\n        raise ValueError('incomplete distribution section')\n"
              "    rows = [l for l in dist.group(1).split(NL)[1:] if l.strip()]\n"
              "    # Diagnostic ALL-unit output is not the eligible statistical population.\n"
              "    v['distribution_coverage'] = require_equal(source_units, [l.split()[0] for l in rows])")
new = replace(new, 'def main():', 'def _main_impl():')
new = replace(new, "        source_expected = expected_strata(source, contract['dispositions'])\n        print(json.dumps(coverage, sort_keys=True))",
'''        states = contract['dispositions']
        if not isinstance(states, dict):
            raise ValueError('dispositions must be an object')
        require_equal(list(source), list(states))
        if not all(s in ('eligible', 'not-applicable', 'partial', 'unresolved') for s in states.values()):
            raise ValueError('unknown disposition')
        state_units = {s: sorted(u for u in source if states[u] == s)
                       for s in ('eligible', 'not-applicable', 'partial', 'unresolved')}
        evidence_missing = {u: ['source completeness or eligibility evidence incomplete']
                            for u in source if states[u] in ('partial', 'unresolved')}
        report = dict(coverage=coverage, dispositions=states, state_units=state_units,
                      evidence_missing=evidence_missing, diagnostic_units=sorted(source),
                      statistical_units=state_units['eligible'])
        try:
            source_expected = expected_strata(source, states)
        except SourceIncomplete:
            report['downstream'] = {s: dict(status='not-run', reason='source-incomplete', exit=None)
                                    for s in ('measurement', 'derivation', 'gate0', 'ruler-comparison')}
            print(json.dumps(report, sort_keys=True))
            print('[BLOCKED] source stage incomplete; downstream NOT RUN (not PASS)')
            return 1
        print(json.dumps(report, sort_keys=True))''')
new = replace(new, "        if set(contract) != {'snapshot', 'dispositions'}:",
              "        if not isinstance(contract, dict) or set(contract) != {'snapshot', 'dispositions'}:")
new = replace(new, "        source, coverage = frozen_source('corpus', contract['snapshot'])",
              "        if not isinstance(contract['snapshot'], dict):\n            raise ValueError('snapshot must be an object')\n"
              "        source, coverage = frozen_source('corpus', contract['snapshot'])")
new = replace(new, "print('measurement_exit=%d contract_exit=%d' % (code, contract_exit))",
              "print('measurement_exit=%d stage_measurement_exit=%d' % (code, contract_exit))")
new = replace(new, 'v = derive(out, source_expected)', 'v = derive(out, source_expected, list(source))')
new = new.replace("        print('contract_exit=2')\n", '')
new = replace(new, "# [FAIL] path: gate0() returns 1 on planted undetected, prints [GATE 0 FAIL] and exits 2",
'''def main():
    # Single terminal marker after every required check or an explicit early stop.
    try:
        result = _main_impl()
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, AttributeError, IndexError) as exc:
        print('[BLOCKED] input/execution failure: %s' % exc)
        result = 2
    print('contract_exit=%d' % result)
    return result


# [FAIL] path: gate0() returns 1 on planted undetected, prints [GATE 0 FAIL] and exits 2''')
ast.parse(new)
gate = lambda code: ast.dump(next(n for n in ast.parse(code).body if isinstance(n, ast.FunctionDef) and n.name == 'gate0'))
base = (ROOT / 'tools/regen_rubric_values.py').read_text(encoding='utf-8')
assert gate(base) == gate(old) == gate(new)
save('repaired_candidate.py', new)
save('repair_delta.patch', ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
     fromfile='a/output/260912/rev/260912_01_info_ab50_q1_integrated_candidate.py',
     tofile='b/output/260912/rev/' + PREFIX + 'repaired_candidate.py')))
save('integrated.patch', ''.join(difflib.unified_diff(base.splitlines(True), new.splitlines(True),
     fromfile='a/tools/regen_rubric_values.py', tofile='b/tools/regen_rubric_values.py')))

caller = (ROOT / 'tools/check_assurance_contract.py').read_text(encoding='utf-8')
updated = replace(caller, '[sys.executable, str(ROOT / "tools/regen_rubric_values.py")],',
                  '[sys.executable, str(ROOT / "tools/regen_rubric_values.py"),\n'
                  '         "--source-contract", str(ROOT / "analysis/info_ab50_source_contract.json")],')
save('assurance_candidate.py', updated)
save('assurance.patch', ''.join(difflib.unified_diff(caller.splitlines(True), updated.splitlines(True),
     fromfile='a/tools/check_assurance_contract.py', tofile='b/tools/check_assurance_contract.py')))

spec = ROOT / 'output/260911/rev/260911_04_info_ab50_repair_spec.md'
snapshot = {}
locators = {}
for number, line in enumerate(spec.read_text(encoding='utf-8').splitlines(), 1):
    if line.startswith('| EX-'):
        uid, tb, th, mb, mh = [x.strip() for x in line.strip('|').split('|')]
        assert uid not in snapshot
        snapshot[uid] = {'transcript.md': dict(bytes=int(tb), sha256=th),
                         'meta.yml': dict(bytes=int(mb), sha256=mh)}
        locators[uid] = number
save('source_contract.json', json.dumps(dict(snapshot=snapshot, dispositions={u: 'unresolved' for u in snapshot}), indent=2) + '\n')
evidence = dict(author='Codex/OMX (main loop)', grade='proposal', model='unverified', reasoning_depth='unverified',
                input_owner='Codex/OMX author: candidate supply only',
                approval_owner='user policy key + independent ruling authority',
                policy_key=None, exact_patch_audit_key=None,
                proposed_supply_path='analysis/info_ab50_source_contract.json', installed=False,
                snapshot_source=dict(path=str(spec.relative_to(ROOT)), sha256=hashlib.sha256(spec.read_bytes()).hexdigest()),
                units={})
for uid, files in snapshot.items():
    refs = {}
    for name, info in files.items():
        path = ROOT / 'corpus' / uid / name
        b = path.read_bytes()
        assert len(b) == info['bytes'] and hashlib.sha256(b).hexdigest() == info['sha256']
        refs[name] = dict(path=str(path.relative_to(ROOT)), **info, source_locator='entire file; byte-only check',
                          snapshot_locator='line ' + str(locators[uid]))
    evidence['units'][uid] = dict(disposition='unresolved', source_files=refs,
        declared_selective_count=None, declared_descriptive_count=None,
        observed_item_ids=None, parsed_score_ids=None,
        printed_id_coverage=dict(expected=None, observed=None, duplicates=None, missing=None, extra=None, status='blocked'),
        eligibility_approval=None, historical_permission=None,
        closure_evidence=None, missing_evidence=['printed-ID verification', 'count/sum axes', 'statistical eligibility approval'])
save('source_evidence.json', json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
print('proposal files generated; protected files not written; gate0 AST unchanged; source files checked=', len(snapshot) * 2)
