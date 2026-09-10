"""Freeze existing questions for an isolated blind-solve pilot; no product edits."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def snapshot(path):
    data = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def main():
    old = json.loads((ROOT / 'output/260910/260910_03_info_selfcheck.json').read_text(encoding='utf-8'))
    for record in old['inputs'] + old['artifacts']:
        assert snapshot(record['path']) == record, record['path']
    questions = {}
    source_records = []
    for letter, number in [('A', '01'), ('B', '02')]:
        path = f'output/260910/260910_{number}_info_composite_{letter.lower()}_questions_review.md'
        text = (ROOT / path).read_text(encoding='utf-8')
        matches = list(re.finditer(r'^\*\*(\d+)\.\*\*', text, re.M))
        ids = [f'{letter}/{m[1]}' for m in matches]
        assert ids == [f'{letter}/{i}' for i in range(1, 26)], ids
        for i, match in enumerate(matches):
            questions[ids[i]] = text[match.start():matches[i+1].start() if i+1 < len(matches) else len(text)]
        source_records.append(snapshot(path))
    target = 'analysis/wip/260910_info_astra_pilot_questions.md'
    content = '# Blind input: A/1-A/5 only\n\n' + '\n'.join(questions[f'A/{i}'] for i in range(1, 6))
    dest = ROOT / target
    if dest.exists():
        assert dest.read_text(encoding='utf-8') == content
    else:
        dest.write_text(content, encoding='utf-8', newline='\n')
    manifest = dict(executor='Codex/OMX', stage='blind-pilot', expected_ids=list(questions),
                    pilot_ids=[f'A/{i}' for i in range(1, 6)], sources=source_records,
                    pilot_input=snapshot(target), original_snapshots_verified=len(old['inputs'] + old['artifacts']),
                    dispatch_budget='Remaining quota not exposed: insufficient; bounded single-slice fallback (2).',
                    objective='Independent blind answers and condition checks; not release approval.',
                    lane='blind-solve = gpt-6-astra = high (requested, runtime confirmation required)',
                    density='5 Python code-trace items, each output plus explanation; no images.',
                    schema='Per-ID derived answer, state trace, sufficiency/uniqueness, defects; actual reads and hashes.',
                    exclusive_output='analysis/wip/solve-back-verifier_260910_info_astra_pilot.md',
                    max_concurrency=1, stop='Five items or first resource/input/model mismatch; checkpoint each item.',
                    resume='Verify pilot artifact and model evidence before authorizing another slice.',
                    no_release=True)
    out = ROOT / 'analysis/wip/260910_info_astra_dispatch.json'
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
