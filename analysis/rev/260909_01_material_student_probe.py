"""Read-only diagnostic; not an acceptance ruler or a ledger writer."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
for path in sorted((ROOT / "student/S01").glob("*.tsv")):
    raw = path.read_bytes()
    rows = list(csv.reader(raw.decode("utf-8-sig").splitlines(), delimiter="\t"))
    results.append({
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bom": raw.startswith(b"\xef\xbb\xbf"),
        "header": rows[0],
        "rows": len(rows) - 1,
        "bad_width_lines": [i for i, row in enumerate(rows[1:], 2) if len(row) != len(rows[0])],
        "non_ascii_cells": sum(not cell.isascii() for row in rows[1:] for cell in row),
    })
print(json.dumps(results, ensure_ascii=False, indent=2))
