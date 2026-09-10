"""Read-only provenance check; stdout is evidence, not an approval gate."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def snapshot(record):
    path = ROOT / record['path']
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    return dict(path=record['path'], expected_bytes=record['bytes'],
                expected_sha256=record['sha256'], observed_bytes=len(data),
                observed_sha256=digest,
                match=len(data) == record['bytes'] and digest == record['sha256'])


def main():
    current = json.loads((ROOT / 'output/260910/260910_03_info_selfcheck.json').read_text(encoding='utf-8'))
    historical = json.loads((ROOT / 'output/260910/rev/260910_02_info_novelty_text_screen.json').read_text(encoding='utf-8'))
    # Exclude historical author/products, which intentionally changed in revisions1/2.
    products = {r['path'] for r in current['inputs'] + current['artifacts']
                if not r['path'].startswith('corpus/')}
    source_records = [r for r in historical['inputs'] if r['path'] not in products]
    direct = [snapshot(r) for r in current['inputs'] + current['artifacts']]
    sources = [snapshot(r) for r in source_records]
    changed = {r['path'] for r in sources if not r['match']}
    affected = []
    for path in sorted((ROOT / 'output/260910').glob('*info_composite_*.novelty.tsv')):
        with path.open(encoding='utf-8-sig', newline='') as stream:
            for row in csv.DictReader(stream, delimiter='\t'):
                if any(source in row['nearest_prior'] for source in changed):
                    affected.append({'item': row['item_id'], 'nearest_prior': row['nearest_prior']})
    result = dict(executor='Codex/OMX', grade='proposal', independent=False,
                  direct=direct, comparison_sources=sources,
                  changed_comparison_sources=sorted(changed),
                  directly_affected_current_rows=affected,
                  limitation='Nearest-source impact only; not a full novelty review.',
                  status='BLOCKED' if changed or not all(r['match'] for r in direct) else 'UNCHANGED')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['status'] == 'BLOCKED' else 0


if __name__ == '__main__':
    raise SystemExit(main())
