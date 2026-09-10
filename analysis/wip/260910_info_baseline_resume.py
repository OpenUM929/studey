"""Read-only source audit; writes only a new coordinator evidence snapshot."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def snap(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

def main():
    old = json.loads((ROOT / 'output/260910/260910_03_info_selfcheck.json').read_text(encoding='utf-8'))
    records = old['inputs'] + old['artifacts']
    changed = [r['path'] for r in records if snap(r['path']) != r]
    assert not changed, changed
    home = ROOT / 'output/260908'
    inventory = [snap(p.relative_to(ROOT).as_posix()) for p in sorted(home.iterdir()) if p.is_file()]
    source = 'output/260908/260908_04_info_midterm_26_questions.md'
    text = (ROOT / source).read_text(encoding='utf-8')
    found = list(re.finditer(r'^\*\*(\d+)\.\*\*', text, re.M))
    observed = [int(m[1]) for m in found]
    expected = list(range(1, 27))
    duplicates = sorted({i for i in observed if observed.count(i) > 1})
    missing, extra = sorted(set(expected)-set(observed)), sorted(set(observed)-set(expected))
    assert observed == expected and not duplicates
    items = [{'id': f'prior26/{m[1]}', 'text': text[m.start():found[i+1].start() if i+1<len(found) else len(text)]}
             for i,m in enumerate(found)]
    manifest = json.loads((ROOT / 'analysis/wip/260909_info_textbook_intake_manifest.json').read_text(encoding='utf-8'))
    textbook_changed = [r['path'] for r in manifest['files'] if any(snap(r['path'])[k] != r[k] for k in ('bytes','sha256'))]
    assert not textbook_changed, textbook_changed
    result = dict(executor='Codex/OMX', grade='proposal', inventory=inventory,
                  existing_snapshots_verified=len(records), textbook_snapshots_verified=len(manifest['files']),
                  question_source=snap(source), expected_ids=expected, observed_ids=observed,
                  duplicate_ids=duplicates, missing_ids=missing, extra_ids=extra, items=items,
                  previous_comparison_source_sha256='e635fdd5f27edc96e7a9c96cffa6a474058d835078ec174d344204884fe456ce',
                  current_comparison_source=snap('output/260908/260908_04_info_midterm_26.md'),
                  warnings=['prior26_source_changed_recomparison_required', 'independent_astra_pilot_model_mismatch',
                            'textbook_content_not_yet_fully_refined'], release_status='BLOCKED')
    dest=ROOT / 'output/260910/rev/260910_10_info_baseline_resume.json'
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('inventory','items')},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
