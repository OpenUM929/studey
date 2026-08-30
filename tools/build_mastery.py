#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_mastery.py — regenerate MASTERY.tsv from ATTEMPT_LOG.tsv × index.tsv.

DATA_STANDARD §5.2 / §6: regenerated artifact, hand edits forbidden (--check detects).

Rules implemented (documented where the standard leaves room):
- Attempts are attributed to `main_type` only; aux_types are evidence, not attempts.
- `last3` = first letters of the 3 most recent marks (file order == chronological),
  newest LEFT, padded right with '-' (e.g. "oaw").
- status_code deterministic ladder:
    unmeasured : attempts == 0
    weak       : among last3, wrong >= 2 or blank >= 1
    mastered   : last3 all correct AND at least one of them is Tier T3+
    unstable   : anything else with attempts > 0 (conservative default;
                 includes correct-only streaks shorter than 3)
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ATTEMPT = ROOT / "student" / "S01" / "ATTEMPT_LOG.tsv"
DEFAULT_INDEX = ROOT / "analysis" / "catalog" / "index.tsv"
DEFAULT_OUT = ROOT / "student" / "S01" / "MASTERY.tsv"

HEADER = ["type_id", "unit", "importance", "attempts", "o_count", "amb_count",
          "wrong_count", "blank_count", "last3", "status_code"]
MARKS = ("correct", "unsure", "wrong", "blank")
INITIALS = {"correct": "o", "unsure": "a", "wrong": "w", "blank": "b"}
TIER_NUM = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}


def read_tsv(path):
    text = Path(path).read_text(encoding="utf-8-sig")
    return [l.split("\t") for l in text.splitlines() if l.strip()]


def aggregate(attempt_rows):
    """attempt_rows: dict rows keyed by header. Returns {type_id: [row dicts]} in order."""
    order, buckets = [], {}
    for r in attempt_rows:
        t = r["main_type"]
        if t not in buckets:
            buckets[t] = []
            order.append(t)
        buckets[t].append(r)
    return order, buckets


def classify(marks_tiers):
    n = len(marks_tiers)
    if n == 0:
        return "unmeasured"
    last3 = marks_tiers[:3]  # newest first
    ws = sum(1 for m, _ in last3 if m == "wrong")
    bs = sum(1 for m, _ in last3 if m == "blank")
    if ws >= 2 or bs >= 1:
        return "weak"
    if n >= 3 and all(m == "correct" for m, _ in last3) and \
       any(TIER_NUM.get(t, 0) >= 3 for _, t in last3):
        return "mastered"
    return "unstable"


def build(attempt_path=DEFAULT_ATTEMPT, index_path=DEFAULT_INDEX):
    idx = read_tsv(index_path)
    ihdr, irows = idx[0], idx[1:]
    icols = {c: i for i, c in enumerate(ihdr)}
    att = read_tsv(attempt_path)
    ahdr, arows_raw = att[0], att[1:]
    acols = {c: i for i, c in enumerate(ahdr)}

    entries = []  # ordered index entries (tid, unit, importance)
    for r in irows:
        entries.append((r[icols["type_id"]], r[icols["unit_major"]] + "/" + r[icols["unit_minor"]],
                        r[icols["importance"]]))
    known = {e[0] for e in entries}

    order, buckets = aggregate(
        [{c: r[acols[c]] for c in ahdr} for r in arows_raw])
    warnings = []
    for t in order:
        if t not in known:
            warnings.append(f"type {t} not in index.tsv — appended as extra row")

    out_rows, seen = [], set()
    seq = entries + [(t, "-", "-") for t in order if t not in known]
    for tid, unit, imp in seq:
        seen.add(tid)
        rs = buckets.get(tid, [])
        marks_tiers = [(r["mark_code"], r.get("tier", "-")) for r in rs]
        counts = {m: sum(1 for mk, _ in marks_tiers if mk == m) for m in MARKS}
        last3 = "".join(INITIALS[mk] for mk, _ in marks_tiers[:3]).ljust(3, "-")
        out_rows.append([tid, unit, imp, str(len(rs)), str(counts["correct"]),
                         str(counts["unsure"]), str(counts["wrong"]), str(counts["blank"]),
                         last3, classify(marks_tiers)])
    for t in order:
        if t not in seen:
            pass  # already emitted via seq ordering above
    body = "\t".join(HEADER) + "\n" + "".join("\t".join(r) + "\n" for r in out_rows)
    return body, warnings


def main():
    check = "--check" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    attempt = Path(args[0]) if len(args) > 0 else DEFAULT_ATTEMPT
    index = Path(args[1]) if len(args) > 1 else DEFAULT_INDEX
    out = Path(args[2]) if len(args) > 2 else DEFAULT_OUT
    body, warnings = build(attempt, index)
    # Principle 11: warnings print BEFORE any [OK] line, so a reader never sees a pass
    # marker ahead of the problem that invalidates it (the ordering defect recorded for
    # build_catalog_index.py --check).  An attempt row naming a type absent from index.tsv
    # is an integrity defect — a stale index or a mistyped type_id — not an advisory.
    for w in warnings:
        print("[WARN]", w)
    if check:
        existing = out.read_text(encoding="utf-8-sig") if out.exists() else None
        if existing != body:
            print("[FAIL] MASTERY.tsv differs from regeneration"); return 1
        print(f"[OK] MASTERY.tsv matches regeneration ({len(body.splitlines()) - 1} rows)")
    else:
        out.write_text(body, encoding="utf-8-sig", newline="")
        print(f"[OK] wrote {out} ({len(body.splitlines()) - 1} rows)")
    if warnings:
        # Fail-closed: the regeneration still happened, but the gate does not pass.
        print(f"[FAIL] {len(warnings)} unknown type(s) in ATTEMPT_LOG — gate not passed")
        return 1
    print(f"warnings={len(warnings)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
