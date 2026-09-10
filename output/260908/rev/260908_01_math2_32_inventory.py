"""Read-only source inventory; not a mathematical or release gate."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCES = [
    'output/260830/260830_01_math2_graded_new_forms_32.md',
    'output/260830/260830_02_math2_unused_axes_32.md',
]

def measure():
    result = []
    for name in SOURCES:
        raw = (ROOT / name).read_bytes()
        text = raw.decode('utf-8-sig')
        body, answers = text.split('# 정답 · 해설 · 유형', 1)
        ids = re.findall(r'^\*\*([ABCD]\d+)\.\*\*', body, re.M)
        answer_ids = re.findall(r'^\| ([ABCD]\d+)(?: ⚠️)? \|', answers, re.M)
        sid = re.search(r'^set_id: (\S+)', text, re.M)[1]
        result.append(dict(path=name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
            set_id=sid, set_id_valid=bool(re.fullmatch(r'SET-\d{6}-[a-z0-9]+-\d+', sid)),
            expected=ids, observed=answer_ids,
            duplicates=sorted({x for x in ids + answer_ids if ids.count(x)>1 or answer_ids.count(x)>1}),
            missing=sorted(set(ids)-set(answer_ids)), extra=sorted(set(answer_ids)-set(ids)),
            partition={c:sum(x.startswith(c) for x in ids) for c in 'ABCD'},
            gate_status=re.search(r'^gate_status: (.*)', text, re.M)[1],
        ))
    return result

if __name__ == '__main__':
    data = measure()
    print(json.dumps(data, ensure_ascii=False, indent=2))
    print('STRUCTURAL_ONLY: mathematical_audit=NOT_RUN; release=BLOCKED')
    raise SystemExit(1 if any(not r['set_id_valid'] or r['duplicates'] or r['missing'] or r['extra'] for r in data) else 0)
