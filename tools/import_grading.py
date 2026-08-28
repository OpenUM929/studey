#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""import_grading.py — validate a grading TSV and append it to ATTEMPT_LOG.tsv.

DATA_STANDARD §6 enforcement point: schema (§5.1), enums (§4.1), ID patterns (§1.3).
- Atomic policy: if ANY row violates the standard, NOTHING is appended and every
  violation is reported (ledger integrity over partial acceptance).
- BOM preserved on read/write; append-only; never rewrites existing rows.
- WEAK_LEDGER is NEVER written here — only human-readable proposals are printed
  (state machine transitions require teacher confirmation; plan D8/§5).
- After appending, MASTERY.tsv is regenerated via build_mastery.build().

- Simulation guard (260826, ruling 260826_02 BF4): ATTEMPT_LOG is append-only and
  MASTERY/WEAK_LEDGER are derived from it, so a fake row can never be taken back.
  Rows marked `note=simulation` are therefore accepted ONLY into a sandbox student dir
  (name starts with `_`, e.g. `student/_sim`), which is created on demand. When writing
  to a sandbox the tool hashes every OTHER ledger under student/ before and after and
  proves them untouched.

Usage:
  python import_grading.py <grading.tsv> [--student-dir student/S01]
                           [--index analysis/catalog/index.tsv] [--dry-run]
  python import_grading.py sim.tsv --student-dir student/_sim   # simulation sandbox
Grading TSV = same 12 columns as ATTEMPT_LOG (web export or hand-written).
"""
import hashlib
import io
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_mastery import build as build_mastery_body, DEFAULT_INDEX, ROOT  # noqa: E402

ATTEMPT_HEADER = ["date", "set_id", "qnum", "main_type", "aux_types", "tier", "df",
                  "mark_code", "student_answer", "correct_answer", "fail_code", "note"]
RE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_SET = re.compile(r"^SET-\d{6}-[a-z0-9]+-\d+$")
RE_TYPE = re.compile(r"^[A-Z]{1,3}\d?-\d{2}$")
RE_TIER = re.compile(r"^T[1-4]$")
RE_DF = re.compile(r"^DF[1-9](,DF[1-9])*$")
RE_FAIL = re.compile(r"^E\d{1,2}$")
MARK_ENUM = {"correct", "unsure", "wrong", "blank"}


def validate_row(r, idx_types):
    errs = []
    cols = r.split("\t")
    if len(cols) != len(ATTEMPT_HEADER):
        return [f"column count {len(cols)} != {len(ATTEMPT_HEADER)}"]
    v = dict(zip(ATTEMPT_HEADER, cols))
    if not RE_DATE.match(v["date"]):
        errs.append("date not ISO YYYY-MM-DD")
    if not RE_SET.match(v["set_id"]):
        errs.append("set_id pattern violation (§1.3)")
    if not v["qnum"].isdigit():
        errs.append("qnum not integer")
    if not RE_TYPE.match(v["main_type"]) or v["main_type"] not in idx_types:
        errs.append(f"main_type '{v['main_type']}' unknown/unregistered")
    if v["aux_types"] != "-":
        for t in v["aux_types"].split(","):
            if not RE_TYPE.match(t) or t not in idx_types:
                errs.append(f"aux_types entry '{t}' unknown/unregistered")
    if not RE_TIER.match(v["tier"]):
        errs.append("tier must be T1..T4")
    if v["df"] != "-" and not RE_DF.match(v["df"]):
        errs.append("df must be DF1..DF9 list or '-'")
    if v["mark_code"] not in MARK_ENUM:
        errs.append(f"mark_code '{v['mark_code']}' not in enum §4.1")
    for c in ("student_answer", "correct_answer"):
        if "\r" in v[c]:
            errs.append(f"{c} contains newline")
    if v["fail_code"] != "-" and not RE_FAIL.match(v["fail_code"]):
        errs.append("fail_code must be E-code or '-'")
    # §5.1 ASCII-only rule (§0 / §1.4 "stored values are ASCII codes"): every one of the
    # 12 columns. Hangul/symbols belong to LABEL_MAP at render time, never to the ledger.
    for c in ATTEMPT_HEADER:
        if not v[c].isascii():
            bad = "".join(sorted({ch for ch in v[c] if not ch.isascii()}))[:12]
            errs.append(f"{c} contains non-ASCII ({bad}) — §5.1 ASCII-only")
    # §4.1-A: fail_code is an attribution, meaningful only on wrong rows.
    if v["fail_code"] != "-" and v["mark_code"] != "wrong":
        errs.append(f"fail_code set on mark_code '{v['mark_code']}' — §4.1-A allows it "
                    "only on 'wrong'")
    return errs


SIM_RE = re.compile(r"\bsim(ulation|ulated)?\b", re.I)


def is_sandbox(student_dir: Path) -> bool:
    """Sandbox convention: the student dir's own name starts with '_' (student/_sim)."""
    return student_dir.name.startswith("_")


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ledger_snapshot(exclude_dir: Path) -> dict:
    """sha256 of every ledger TSV under student/ EXCEPT the target dir's own."""
    out = {}
    base = (ROOT / "student").resolve()
    exclude = exclude_dir.resolve()
    if not base.exists():
        return out
    for p in sorted(base.rglob("*.tsv")):
        try:
            p.resolve().relative_to(exclude)
            continue          # inside the target dir — expected to change
        except ValueError:
            pass
        out[p.resolve().as_posix()] = sha256(p)
    return out


def weak_proposals(new_rows, all_rows, ledger_path):
    """Print-only WEAK_LEDGER suggestions. Never writes."""
    print("--- WEAK_LEDGER proposals (human decision required) ---")
    open_states = []
    p = Path(ledger_path)
    if p.exists():
        lines = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        for r in (l.split("\t") for l in lines):
            if len(r) >= 6 and r[5] in ("found", "prescribing", "retesting"):
                open_states.append(r)
    wrong_axes = {}
    unsure_by_type = {}
    for r in new_rows:
        v = dict(zip(ATTEMPT_HEADER, r.split("\t")))
        if v["mark_code"] == "wrong" and v["fail_code"] != "-":
            wrong_axes.setdefault(v["fail_code"], []).append(v["main_type"])
        if v["mark_code"] == "unsure":
            unsure_by_type[v["main_type"]] = unsure_by_type.get(v["main_type"], 0) + 1
    total_unsure = {}
    for line in all_rows:
        v = dict(zip(ATTEMPT_HEADER, line))
        if v["mark_code"] == "unsure":
            total_unsure[v["main_type"]] = total_unsure.get(v["main_type"], 0) + 1
    proposed = False
    for axis, types in sorted(wrong_axes.items()):
        covered = [r[0] for r in open_states if axis in r[3].split(",")]
        if covered:
            print(f"  [{axis}] wrong in {sorted(set(types))} — already covered by open "
                  f"{','.join(covered)} → consider relapse only after resolve+re-wrong")
        else:
            print(f"  propose NEW row: axis={axis} state=found evidence_types="
                  f"{','.join(sorted(set(types)))} (teacher confirms & names WK-nn)")
        proposed = True
    for t, n in sorted(total_unsure.items()):
        if n >= 2:
            print(f"  △×2 promotion candidate: type {t} has {n} unsure marks → may enter "
                  f"as found (plan D2)")
            proposed = True
    if not proposed:
        print("  (none)")


def main():
    argv = sys.argv[1:]
    dry = "--dry-run" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    src = Path(args[0])
    student_dir = Path(ROOT / "student" / "S01")
    index = DEFAULT_INDEX
    for flag, default in (("--student-dir", None), ("--index", None)):
        if flag in argv:
            val = argv[argv.index(flag) + 1]
            if flag == "--student-dir":
                student_dir = Path(val) if Path(val).is_absolute() else ROOT / val
            else:
                index = Path(val) if Path(val).is_absolute() else ROOT / val
    attempt_path = student_dir / "ATTEMPT_LOG.tsv"
    ledger_path = student_dir / "WEAK_LEDGER.tsv"

    raw = src.read_text(encoding="utf-8-sig")
    lines = [l for l in raw.split("\n") if l.strip()]
    header = lines[0].rstrip("\r").split("\t")
    problems = []
    if header != ATTEMPT_HEADER:
        problems.append(f"header mismatch: expected {ATTEMPT_HEADER}, got {header}")
        body_rows = []
    else:
        body_rows = [l.rstrip("\r") for l in lines[1:]]

    idx_text = index.read_text(encoding="utf-8-sig")
    idx_types = {l.split("\t")[0] for l in idx_text.splitlines()[1:] if l.strip()}
    valid = []
    for i, row in enumerate(body_rows, start=2):
        errs = validate_row(row, idx_types)
        if errs:
            problems.append(f"line {i}: " + "; ".join(errs))
        else:
            valid.append(row)

    if problems:
        print("[ABORT] nothing appended — violations:")
        for p_ in problems:
            print("  -", p_)
        return 2

    # --- simulation / sandbox guard (260826, ruling 260826_02 BF4) ---
    note_i = ATTEMPT_HEADER.index("note")
    sim_lines = [i for i, row in enumerate(valid, start=2)
                 if SIM_RE.search(row.split("\t")[note_i])]
    sandbox = is_sandbox(student_dir)
    if sim_lines and not sandbox:
        shown = ", ".join(str(i) for i in sim_lines[:8])
        more = f" (+{len(sim_lines) - 8} more)" if len(sim_lines) > 8 else ""
        print(f"[ABORT] {len(sim_lines)} row(s) marked as simulation — lines {shown}{more} — "
              f"target the REAL ledger {attempt_path}")
        print("        ATTEMPT_LOG is append-only and MASTERY/WEAK_LEDGER derive from it: "
              "fake rows cannot be removed and pollute the ledger permanently.")
        print("        Re-run into a sandbox instead:  --student-dir student/_sim")
        return 2
    if not student_dir.exists():
        if sandbox:
            student_dir.mkdir(parents=True, exist_ok=True)
            print(f"[OK] created sandbox {student_dir}")
        else:
            print(f"[ABORT] student dir does not exist: {student_dir}")
            print("        (typo? a simulation sandbox must be named with a leading '_')")
            return 2

    existing = attempt_path.read_text(encoding="utf-8-sig") if attempt_path.exists() else ""
    all_rows = [l for l in existing.split("\n")[1:] if l.strip()]
    before = ledger_snapshot(student_dir) if sandbox else {}
    rc = 0
    if dry:
        print(f"[DRY] would append {len(valid)} rows to {attempt_path}")
    else:
        with io.open(attempt_path, "a", encoding="utf-8-sig", newline="") as f:
            if not existing.strip():
                f.write("\t".join(ATTEMPT_HEADER) + "\n")   # fresh sandbox ledger
            for row in valid:
                f.write(row + "\n")
        print(f"[OK] appended {len(valid)} rows to {attempt_path}")
        body, warnings = build_mastery_body(attempt_path, index)
        out = student_dir / "MASTERY.tsv"
        out.write_text(body, encoding="utf-8-sig", newline="")
        print(f"[OK] regenerated {out}")
        for w in warnings:
            print("[WARN]", w)
    if sandbox:
        # Evidence that the real ledgers were not touched (BF4 ②), printed either way.
        after = ledger_snapshot(student_dir)
        root = ROOT.resolve()
        broken = [k for k in before if before[k] != after.get(k)]
        print(f"--- sandbox integrity: {len(before)} ledger file(s) outside "
              f"{student_dir.name} ---")
        for k in sorted(before):
            rel = Path(k).relative_to(root).as_posix()
            ok = before[k] == after.get(k)
            print(f"  {'OK  ' if ok else 'FAIL'} {rel}  sha256={before[k][:16]}...")
        if broken:
            print(f"[FAIL] {len(broken)} real ledger file(s) changed during a sandbox run")
            rc = 1
        else:
            print("[OK] real ledgers untouched")
    weak_proposals(valid, all_rows + valid, ledger_path)
    return rc


if __name__ == "__main__":
    sys.exit(main())
