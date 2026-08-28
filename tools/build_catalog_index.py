#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_catalog_index.py — regenerate analysis/catalog/index.tsv (DATA_STANDARD §5.4).

Scans subject catalogs for `## 유형 <ID>: ...` blocks and emits the type index
(join source for MASTERY / reports). Regenerated file — hand edits forbidden
(DATA_STANDARD §6); use --check to detect them.

Conventions (documented here because the standard shows an example, not a rule):
- unit_major/unit_minor derive from the block's `영역/단원` field.
  math2 uses the sheet table of its own header: I-1..I-4 → major "I.도형의방정식",
  minor "1.평면좌표" style. All other catalogs: split at first whitespace
  (major = leading token, minor = remainder or "-").
- status_code mapping = DATA_STANDARD §4.4.
- Expected per-prefix counts come from CODE_REGISTRY §1; mismatches are reported.

Scope note: all 7 subject catalogs are indexed. The F-prefix collision
(social/history) is safe here because subject_code is part of the join key
(CODE_REGISTRY §2 requires exactly this scoping in ledgers).
"""
import io
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):     # cp949 consoles choke on non-ASCII diagnostics
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "analysis" / "catalog"
OUT_PATH = CATALOG_DIR / "index.tsv"

SUBJECT_FILES = {
    "math1.md": "math1",
    "math2.md": "math2",
    "english.md": "english",
    "science.md": "science",
    "social.md": "social",
    "history.md": "history",
    "korean.md": "korean",
}

# CODE_REGISTRY §1 — expected counts per prefix family (None = don't assert).
EXPECTED = {
    "SM": 18, "SM2": 33, "K": 12, "T": 12, "W": 4,
    "F": None,  # dual-owner (social+history): assert per-file below
    "GB": None, "GT": None, "MC": None, "ER": None, "CH": None, "BI": None,
    "UN": None,  # science total asserted as sum == 37
}

STATUS_MAP = {
    "검증(부교재)": "verified_aux",
    "검증": "verified",
    "시연": "demo",
    "폐기": "deprecated",
}

TYPE_RE = re.compile(r"^##\s+유형\s+([A-Z]{1,3}\d?-\d{2})\s*:", re.M)
SECTION_RE = re.compile(r"^#\s+영역\s+G(\d)", re.M)  # math2 sheet sections G1..G4
FIELD_RE = lambda name: re.compile(r"^-\s*" + re.escape(name) + r"\s*:\s*(.*)$", re.M)

# math2 sheet table (source: catalog/math2.md 시트 개요) — keeps §5.4 example shape.
MATH2_SHEETS = {
    "I-1": ("I.도형의방정식", "1.평면좌표"),
    "I-2": ("I.도형의방정식", "2.직선의방정식"),
    "I-3": ("I.도형의방정식", "3.원의방정식"),
    "I-4": ("I.도형의방정식", "4.도형의이동"),
}


def parse_units(raw: str):
    """Split an 영역/단원 value into (major, minor)."""
    raw = raw.split("/")[0].split("[")[0].strip()
    if not raw:
        return "-", "-"
    code = raw.split()[0]
    if code in MATH2_SHEETS:
        return MATH2_SHEETS[code]
    rest = raw[len(code):].strip()
    return code, (rest if rest else "-")


def parse_importance(block: str) -> str:
    m = re.search(r"중요도\s*:?\s*(★+)", block)
    return m.group(1) if m else "-"


def parse_status(block: str) -> str:
    m = FIELD_RE("상태").search(block)
    if not m:
        return "-"
    val = m.group(1).strip()
    for key in STATUS_MAP:  # longest-first semantics via explicit order
        if val.startswith(key) and key == "검증(부교재)":
            return STATUS_MAP[key]
        if key != "검증(부교재)" and (val == key or val.startswith(key + " ")):
            return STATUS_MAP[key]
    # plain 검증 when not the 부교재 variant
    if val.startswith("검증") and not val.startswith("검증(부교재)"):
        return "verified"
    return "-"


def extract_blocks(text: str):
    """Yield (start_offset, id, block_text, section_gnum|None) preserving document order."""
    ids = list(TYPE_RE.finditer(text))
    secs = [(m.start(), int(m.group(1))) for m in SECTION_RE.finditer(text)]
    out = []
    for i, m in enumerate(ids):
        end = ids[i + 1].start() if i + 1 < len(ids) else len(text)
        gnum = None
        for s_start, s_num in secs:
            if s_start < m.start():
                gnum = s_num
            else:
                break
        out.append((m.start(), m.group(1), text[m.start():end], gnum))
    return out


def natural_key(tid: str):
    prefix, num = tid.rsplit("-", 1)
    return prefix, int(num)


def build():
    rows = []          # (subject, tid, major, minor, importance, status)
    per_prefix = {}
    problems = []
    for fname, subject in SUBJECT_FILES.items():
        path = CATALOG_DIR / fname
        if not path.exists():
            problems.append(f"missing catalog: {fname}")
            continue
        text = path.read_text(encoding="utf-8")
        for _, tid, block, gnum in extract_blocks(text):
            m = FIELD_RE("영역/단원").search(block)
            if m:
                major, minor = parse_units(m.group(1))
            elif subject == "math2" and gnum is not None:
                # sheet section heading (영역 Gn) — verified structural fallback
                major, minor = MATH2_SHEETS.get(f"I-{gnum}", ("-", "-"))
            else:
                major, minor = "-", "-"
            rows.append((tid, subject, major, minor, parse_importance(block), parse_status(block)))
            prefix = tid.split("-")[0]
            per_prefix.setdefault(prefix, {}).setdefault(subject, 0)
            per_prefix[prefix][subject] += 1

    # Unregistered catalog files (260826, ruling 260826_02 BF3).
    # A catalog file that nobody registered in SUBJECT_FILES used to be skipped in
    # SILENCE — adding info.md would have produced a passing index with the subject
    # missing. Anything carrying type blocks must be registered or explicitly excluded.
    for path in sorted(CATALOG_DIR.glob("*.md")):
        if path.name in SUBJECT_FILES:
            continue
        n = len(TYPE_RE.findall(path.read_text(encoding="utf-8")))
        if n:
            problems.append(
                f"unregistered catalog: {path.name} holds {n} type blocks but is not in "
                f"SUBJECT_FILES - register it (CODE_REGISTRY sec.6 onboarding #6) "
                f"or it stays skipped")

    # Unregistered prefixes: a new prefix must be declared in EXPECTED (None = no assertion)
    # so that adding types cannot silently bypass the registry count check.
    for prefix in sorted(per_prefix):
        if prefix not in EXPECTED:
            problems.append(
                f"prefix {prefix} not declared in EXPECTED - add it (value or None) per "
                f"CODE_REGISTRY sec.1/sec.6")

    # duplicate check across the whole index
    seen = {}
    for r in rows:
        seen.setdefault(r[0], []).append(r[1])
    for tid, subs in sorted(seen.items()):
        if len(subs) > 1 and len(set(subs)) == 1:
            problems.append(f"duplicate {tid} within same subject")

    # registry assertions
    for prefix, expect in EXPECTED.items():
        got = sum(per_prefix.get(prefix, {}).values())
        if expect is not None and got != expect:
            problems.append(f"{prefix}: registry expects {expect}, found {got}")
    sci = sum(per_prefix.get(p, {}).get("science", 0) for p in
              ("GB", "GT", "MC", "ER", "CH", "BI", "UN"))
    if sci != 37:
        problems.append(f"science 7-prefix total: registry expects 37, found {sci}")

    rows.sort(key=lambda r: (r[1], natural_key(r[0])))
    header = ["type_id", "subject_code", "unit_major", "unit_minor", "importance", "status_code"]
    body = "\t".join(header) + "\n" + "".join("\t".join(r) + "\n" for r in rows)
    return body, rows, problems


def main():
    check_only = "--check" in sys.argv
    body, rows, problems = build()
    existing = OUT_PATH.read_text(encoding="utf-8-sig") if OUT_PATH.exists() else None
    if check_only:
        if existing is None:
            print("[FAIL] index.tsv missing"); return 1
        if existing != body:
            print("[FAIL] index.tsv differs from regeneration (hand edit?)"); return 1
        print(f"[OK] index.tsv matches regeneration ({len(rows)} rows)")
    else:
        with open(OUT_PATH, "w", encoding="utf-8-sig", newline="") as f:
            f.write(body)
        per_subj = {}
        for subj, *_ in rows:
            per_subj[subj] = per_subj.get(subj, 0) + 1
        for subj in sorted(per_subj):
            print(f"  {subj}: {per_subj[subj]} types")
        print(f"[OK] wrote {OUT_PATH} ({len(rows)} data rows)")
    if problems:
        # fail-closed (260826, ruling 260826_02 BF3 · CLAUDE.md 원칙 11): --check used to
        # return 0 here, so a gate defined as "exit 0" passed while problems were printed.
        # Any consistency issue now fails, in both modes.
        print("[WARN] consistency issues:")
        for p in problems:
            print("  -", p)
        print(f"[FAIL] {len(problems)} consistency issue(s) — gate not passed")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
