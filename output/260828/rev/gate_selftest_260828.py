"""R3 참조 구현 — 게이트가 **일부러 심은 결함을 실제로 잡는지** 증명하게 한다.

배경: F1(`warnings=0` 하드코딩)과 F3(보고서 본문 무결성 미검사)은 사람이 코드를 정독해서
찾았다. 이 방식은 확장되지 않는다 — 게이트가 길어지면 읽는 사람이 없고, 죽어 있는 검사는
조용히 통과한다. `TEAM_PREFLIGHT_260828.md:34`의 능력 주장 역시 산문이라 코드와 어긋나도
아무 신호가 없다.

이 도구는 codex-team 트리를 **샌드박스로 복사**한 뒤 알려진 결함을 하나씩 심고,
1차 게이트(`check_experiment.py`)가 그 결함마다 **새 실패를 내는지**를 차등 비교한다.
검출기가 자기 검출 능력을 실증한 적이 없으면 그것은 검증되지 않은 검출기다.

CLAUDE.md 원칙 8·9-b: 실원본은 읽기만 하고, 모든 변형은 샌드박스에서만 일어난다.
실행 전후로 원본 해시를 출력해 무손상을 증거로 남긴다.
CLAUDE.md 원칙 11: 통과 판정은 exit 0 + `undetected=0` + `selftest: PASS` 가 모두 맞을 때뿐이다.

usage:
  python output/260828/rev/gate_selftest_260828.py
  python output/260828/rev/gate_selftest_260828.py --keep --workdir <dir>
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # 리다이렉션 시 콘솔 코드페이지(cp1252)로 떨어지는 것 방지
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[3]
TEAM_DIR = REPO / "output/260828/diagnostic/math2-method-comparison/codex-team"
PHASE = "author"

ITEM_COL = {
    "item_id": 0,
    "source_lines": 1,
    "rendered_evidence_status": 2,
    "assignment_or_BLOCKED": 3,
    "existing_type_or_decision_request": 4,
    "rationale": 5,
    "tier": 6,
    "tier_basis": 7,
    "observed_trap": 8,
    "confidence": 9,
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8-sig").splitlines()


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cell(root: Path, rel: str, item_id: str, column: str, value: str) -> None:
    """items.tsv 특정 행·열을 치환한다(csv 인용 규칙을 건드리지 않도록 행 단위 조작)."""
    path = root / rel
    lines = read_lines(path)
    index = ITEM_COL[column]
    for position, line in enumerate(lines):
        fields = line.split("\t")
        if fields and fields[0] == item_id:
            fields[index] = value
            lines[position] = "\t".join(fields)
            break
    else:
        raise SystemExit(f"selftest bug: row {item_id} not found in {rel}")
    write_lines(path, lines)


def mut_items_mojibake(root: Path) -> None:
    path = root / "author/items.tsv"
    lines = read_lines(path)
    for position, line in enumerate(lines):
        fields = line.split("\t")
        if fields and fields[0] == "S-01":
            fields[ITEM_COL["rationale"]] = "?" + fields[ITEM_COL["rationale"]][1:]
            lines[position] = "\t".join(fields)
            break
    write_lines(path, lines)


def mut_report_mojibake(root: Path) -> None:
    path = root / "author/AUTHOR_REPORT_260828.md"
    text = path.read_text(encoding="utf-8-sig")
    path.write_text(text + "\n?? ??? ?? ? ?? ?? ??\n", encoding="utf-8")


def mut_s17_tier(root: Path) -> None:
    cell(root, "author/items.tsv", "S-17", "tier", "T2")


def mut_s17_assignment(root: Path) -> None:
    cell(root, "author/items.tsv", "S-17", "assignment_or_BLOCKED", "SM2-21")


def mut_blank_field(root: Path) -> None:
    cell(root, "author/items.tsv", "S-03", "observed_trap", "")


def mut_control_char(root: Path) -> None:
    cell(root, "author/items.tsv", "S-06", "confidence", "high\x01")


def mut_duplicate_id(root: Path) -> None:
    path = root / "author/items.tsv"
    lines = read_lines(path)
    row = next(line for line in lines if line.split("\t")[0] == "S-05")
    write_lines(path, lines + [row])


def mut_missing_id(root: Path) -> None:
    path = root / "author/items.tsv"
    lines = [line for line in read_lines(path) if line.split("\t")[0] != "S-09"]
    write_lines(path, lines)


def mut_types_undercount(root: Path) -> None:
    path = root / "author/types.tsv"
    lines = [line for line in read_lines(path) if line.strip()]
    write_lines(path, lines[:5])


def mut_ruler_edit(root: Path) -> None:
    """자 자체를 조작한다 — 1차 게이트가 자기 자를 검증하지 않음을 실증."""
    path = root / "EXPECTED_ITEM_IDS_260828.tsv"
    lines = read_lines(path)
    for position, line in enumerate(lines):
        fields = line.split("\t")
        if fields and fields[0] == "W-04":
            fields[5] = "999"
            lines[position] = "\t".join(fields)
            break
    write_lines(path, lines)


def mut_schema_ruler_edit(root: Path) -> None:
    """수용기준 문서를 훼손한다 — 게이트가 자기 소유 md를 읽지 않음을 실증."""
    path = root / "ACCEPTANCE_SCHEMA_260828.md"
    path.write_text("# ????\n\n?? ?? ??? ????.\n", encoding="utf-8")


FIXTURES: list[tuple[str, str, object, str]] = [
    # (name, 기대 실패 문자열(정규식), mutator, 무엇을 증명하는가)
    ("items_mojibake", r"content-integrity failure", mut_items_mojibake, "author TSV 문자 무결성"),
    ("s17_tier", r"S-17 tier must be BLOCKED", mut_s17_tier, "S-17 BLOCKED 규칙(tier)"),
    ("s17_assignment", r"S-17 assignment must remain BLOCKED", mut_s17_assignment, "S-17 BLOCKED 규칙(assignment)"),
    ("blank_field", r"blank fields", mut_blank_field, "공란 검사"),
    ("control_char", r"control-character failure", mut_control_char, "제어문자 검사"),
    ("duplicate_id", r"identifier mismatch", mut_duplicate_id, "ID 중복 검사"),
    ("missing_id", r"identifier mismatch", mut_missing_id, "ID 누락 검사"),
    ("types_undercount", r"type membership is not an exclusive exact cover", mut_types_undercount, "exact cover 검사"),
    ("report_mojibake", r"content-integrity|corrupt", mut_report_mojibake, "보고서 본문 무결성 (F3 예상 미검출)"),
    ("ruler_edit", r"expected|ruler|EXPECTED_ITEM_IDS", mut_ruler_edit, "자 무결성 (예상 미검출)"),
    ("schema_ruler_edit", r"ACCEPTANCE_SCHEMA|acceptance", mut_schema_ruler_edit, "수용기준 무결성 (예상 미검출)"),
]


def run_gate(root: Path) -> tuple[int, str, set[str], int]:
    proc = subprocess.run(
        [sys.executable, str(root / "check_experiment.py"), "--phase", PHASE],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    out = proc.stdout + proc.stderr
    fails = {line for line in out.splitlines() if line.startswith("FAIL: ")}
    match = re.search(r"^warnings=(\d+)$", out, re.M)
    warnings_value = int(match.group(1)) if match else -1
    return proc.returncode, out, fails, warnings_value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workdir")
    parser.add_argument("--keep", action="store_true")
    args = parser.parse_args()

    before = {
        path.relative_to(TEAM_DIR).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(TEAM_DIR.rglob("*"))
        if path.is_file()
    }
    print(f"source_files={len(before)}")

    base_dir = Path(args.workdir) if args.workdir else Path(tempfile.mkdtemp(prefix="gate_selftest_"))
    base_dir.mkdir(parents=True, exist_ok=True)

    sandbox = base_dir / "_baseline"
    if sandbox.exists():
        shutil.rmtree(sandbox)
    shutil.copytree(TEAM_DIR, sandbox)
    base_code, _, base_fails, base_warnings = run_gate(sandbox)
    print(f"baseline_exit={base_code} baseline_failures={len(base_fails)} baseline_warnings={base_warnings}")
    if base_code != 0 or base_fails:
        print("FAIL: baseline is not clean; differential selftest needs a passing baseline")
        return 1

    detected: list[str] = []
    undetected: list[str] = []
    warning_values = {base_warnings}
    rows: list[tuple[str, str, str, int, str]] = []

    for name, pattern, mutate, purpose in FIXTURES:
        work = base_dir / name
        if work.exists():
            shutil.rmtree(work)
        shutil.copytree(TEAM_DIR, work)
        mutate(work)
        code, _, fails, warnings_value = run_gate(work)
        warning_values.add(warnings_value)
        new_fails = sorted(fails - base_fails)
        hit = any(re.search(pattern, line) for line in new_fails)
        verdict = "DETECTED" if hit else "UNDETECTED"
        (detected if hit else undetected).append(name)
        sample = new_fails[0].replace(str(work), "<sandbox>")[:96] if new_fails else "(no new failure)"
        rows.append((name, verdict, purpose, code, sample))

    print("")
    print("fixture\tverdict\texit\tnew_failure_sample")
    for name, verdict, purpose, code, sample in rows:
        print(f"{name}\t{verdict}\t{code}\t{sample}")
    print("")
    print(f"fixtures={len(FIXTURES)} detected={len(detected)} undetected={len(undetected)}")
    print(f"warnings_values_observed={sorted(warning_values)}")

    failures: list[str] = []
    if len(warning_values) == 1 and warning_values == {0}:
        failures.append(
            f"VACUOUS SIGNAL: 'warnings=' stayed 0 across baseline + {len(FIXTURES)} planted defects "
            "-> the warning channel carries no information (F1 mechanically confirmed)"
        )
    for name in undetected:
        purpose = next(p for n, _, _, p in FIXTURES if n == name)
        failures.append(f"UNDETECTED fixture '{name}': {purpose}")

    after = {
        path.relative_to(TEAM_DIR).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(TEAM_DIR.rglob("*"))
        if path.is_file()
    }
    drift = sorted(key for key in before if before[key] != after.get(key))
    print(f"source_unchanged={before == after} drifted={drift or '[]'}")
    if before != after:
        failures.append("SANDBOX LEAK: source tree changed during selftest")

    if not args.keep and not args.workdir:
        shutil.rmtree(base_dir, ignore_errors=True)
    else:
        print(f"workdir={base_dir}")

    print(f"failures={len(failures)}")
    for item in failures:
        print(f"FAIL: {item}")
    if failures:
        print("selftest: FAIL")
        return 1
    print("selftest: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
