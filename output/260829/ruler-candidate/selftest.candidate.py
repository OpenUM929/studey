"""Differential self-test for the S1 candidate ruler.

The eleven planted defects are the unchanged 260828 seed set.  Every mutation
occurs in a temporary candidate baseline; the frozen inputs are hashed before
and after.  A missed seed is reported, never removed or weakened.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from types import ModuleType

sys.dont_write_bytecode = True


REPO = Path(__file__).resolve().parents[3]
CANDIDATE_DIR = Path(__file__).resolve().parent
CHECKER = CANDIDATE_DIR / "check_experiment.candidate.py"
GENERATOR = CANDIDATE_DIR / "gen_expected_ids.candidate.py"
SCHEMA = CANDIDATE_DIR / "ACCEPTANCE_SCHEMA.candidate.md"
TRANSCRIPT = REPO / "corpus/EX-math2-20252M/transcript.md"
TEAM_DIR = REPO / "output/260828/diagnostic/math2-method-comparison/codex-team"

FROZEN_INPUTS = [
    REPO / "corpus/EX-math2-20252M/transcript.md",
    REPO / "corpus/EX-math2-20252M/meta.yml",
    TEAM_DIR / "check_experiment.py",
    TEAM_DIR / "ACCEPTANCE_SCHEMA_260828.md",
    TEAM_DIR / "EXPECTED_ITEM_IDS_260828.tsv",
    TEAM_DIR / "author/types.tsv",
    TEAM_DIR / "author/items.tsv",
    REPO / "output/260828/rev/ACCEPTANCE_SCHEMA_260828.repaired.md",
    REPO / "output/260828/rev/meta_gate_260828.py",
    REPO / "output/260828/rev/gen_expected_ids_260828.py",
    REPO / "output/260828/rev/gate_selftest_260828.py",
    REPO / "analysis/REV_GUIDE.md",
    REPO / "output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md",
]

ITEM_COLUMNS = [
    "item_id",
    "source_lines",
    "rendered_evidence_status",
    "assignment_or_BLOCKED",
    "existing_type_or_decision_request",
    "rationale",
    "tier",
    "tier_basis",
    "observed_trap",
    "confidence",
    "generator_id",
]
TYPE_COLUMNS = [
    "group_id",
    "member_item_ids",
    "type_disposition",
    "variation_axis_1",
    "variation_axis_2",
    "observed_trap",
    "importance_source_axis",
    "common_types_disposition",
    "catalog_disposition",
    "generator_id",
    "row_kind",
]
ITEM_INDEX = {column: index for index, column in enumerate(ITEM_COLUMNS)}


def load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def members(row: dict[str, str]) -> list[str]:
    return [item.strip() for item in row["member_item_ids"].split(",") if item.strip()]


def umbrella(row: dict[str, str]) -> bool:
    text = " ".join(row.values()).lower()
    return "umbrella" in text or "bookkeeping" in text or "우산" in text


def build_baseline(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    generator = load_module(GENERATOR, "selftest_generator")
    expected_rows = generator.derive_rows(TRANSCRIPT)
    write_tsv(root / "expected.tsv", generator.OUTPUT_COLUMNS, expected_rows)
    shutil.copy2(SCHEMA, root / "schema.md")
    shutil.copy2(TEAM_DIR / "author/AUTHOR_REPORT_260828.md", root / "report.md")

    _, original_types = read_tsv(TEAM_DIR / "author/types.tsv")
    expanded_types: list[dict[str, str]] = []
    generator_by_item: dict[str, str] = {}
    for row in original_types:
        current = members(row)
        if umbrella(row):
            for item_id in current:
                generator_id = f"GEN-{item_id}"
                generator_by_item[item_id] = generator_id
                expanded = dict(row)
                expanded.update(
                    {
                        "group_id": f"GEN-{item_id}",
                        "member_item_ids": item_id,
                        "type_disposition": f"단독 primary-generator 진단군: {item_id}",
                        "catalog_disposition": f"{item_id} 독립 generator fixture expansion; no pNN HOLD",
                        "generator_id": generator_id,
                        "row_kind": "singleton",
                    }
                )
                expanded_types.append(expanded)
            continue
        is_blocked = row["group_id"].startswith("BLOCKED-")
        generator_id = "BLOCKED-S17" if is_blocked else row["group_id"]
        for item_id in current:
            generator_by_item[item_id] = generator_id
        expanded = dict(row)
        expanded["generator_id"] = generator_id
        expanded["row_kind"] = (
            "blocked" if is_blocked else ("reusable" if len(current) >= 2 else "singleton")
        )
        expanded_types.append(expanded)
    write_tsv(root / "types.tsv", TYPE_COLUMNS, expanded_types)

    _, original_items = read_tsv(TEAM_DIR / "author/items.tsv")
    candidate_items: list[dict[str, str]] = []
    for row in original_items:
        candidate = dict(row)
        item_id = candidate["item_id"]
        candidate["generator_id"] = generator_by_item[item_id]
        if item_id == "W-04":
            candidate["source_lines"] = candidate["source_lines"].replace(":44-48", ":44-49", 1)
        candidate_items.append(candidate)
    write_tsv(root / "items.tsv", ITEM_COLUMNS, candidate_items)


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8-sig").splitlines()


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cell(root: Path, item_id: str, column: str, value: str) -> None:
    path = root / "items.tsv"
    lines = read_lines(path)
    index = ITEM_INDEX[column]
    for position, line in enumerate(lines):
        fields = line.split("\t")
        if fields and fields[0] == item_id:
            fields[index] = value
            lines[position] = "\t".join(fields)
            break
    else:
        raise RuntimeError(f"selftest row not found: {item_id}")
    write_lines(path, lines)


def mut_items_mojibake(root: Path) -> None:
    path = root / "items.tsv"
    lines = read_lines(path)
    fields = lines[1].split("\t")
    fields[ITEM_INDEX["rationale"]] = "?" + fields[ITEM_INDEX["rationale"]][1:]
    lines[1] = "\t".join(fields)
    write_lines(path, lines)


def mut_report_mojibake(root: Path) -> None:
    path = root / "report.md"
    path.write_text(path.read_text(encoding="utf-8-sig") + "\n?? ??? ??\n", encoding="utf-8")


def mut_s17_tier(root: Path) -> None:
    cell(root, "S-17", "tier", "T2")


def mut_s17_assignment(root: Path) -> None:
    cell(root, "S-17", "assignment_or_BLOCKED", "SM2-21")


def mut_blank_field(root: Path) -> None:
    cell(root, "S-03", "observed_trap", "")


def mut_control_char(root: Path) -> None:
    cell(root, "S-06", "confidence", "high\x01")


def mut_duplicate_id(root: Path) -> None:
    path = root / "items.tsv"
    lines = read_lines(path)
    row = next(line for line in lines if line.split("\t")[0] == "S-05")
    write_lines(path, lines + [row])


def mut_missing_id(root: Path) -> None:
    path = root / "items.tsv"
    write_lines(path, [line for line in read_lines(path) if line.split("\t")[0] != "S-09"])


def mut_types_undercount(root: Path) -> None:
    path = root / "types.tsv"
    lines = read_lines(path)
    write_lines(path, lines[:-1])


def mut_ruler_edit(root: Path) -> None:
    path = root / "expected.tsv"
    lines = read_lines(path)
    for position, line in enumerate(lines):
        fields = line.split("\t")
        if fields and fields[0] == "W-04":
            fields[5] = "999"
            lines[position] = "\t".join(fields)
            break
    write_lines(path, lines)


def mut_schema_ruler_edit(root: Path) -> None:
    (root / "schema.md").write_text("# ????\n\n?? ??\n", encoding="utf-8")


FIXTURES: list[tuple[str, str, object, str]] = [
    ("items_mojibake", r"content-integrity failure", mut_items_mojibake, "item TSV character integrity"),
    ("s17_tier", r"S-17 tier must be BLOCKED", mut_s17_tier, "S-17 BLOCKED tier"),
    ("s17_assignment", r"S-17 assignment must remain BLOCKED", mut_s17_assignment, "S-17 BLOCKED assignment"),
    ("blank_field", r"blank fields", mut_blank_field, "required-field presence"),
    ("control_char", r"control-character failure", mut_control_char, "control-character integrity"),
    ("duplicate_id", r"identifier mismatch", mut_duplicate_id, "duplicate identifier"),
    ("missing_id", r"identifier mismatch", mut_missing_id, "missing identifier"),
    ("types_undercount", r"type membership is not an exclusive exact cover", mut_types_undercount, "exact cover"),
    ("report_mojibake", r"report content-integrity failure", mut_report_mojibake, "report body integrity"),
    ("ruler_edit", r"expected ruler mismatch", mut_ruler_edit, "generated ruler integrity"),
    ("schema_ruler_edit", r"ACCEPTANCE_SCHEMA|acceptance schema", mut_schema_ruler_edit, "acceptance schema integrity"),
]


def run_gate(root: Path) -> tuple[int, str, set[str], int]:
    proc = subprocess.run(
        [
            sys.executable,
            "-X",
            "utf8",
            str(CHECKER),
            "--types",
            str(root / "types.tsv"),
            "--items",
            str(root / "items.tsv"),
            "--report",
            str(root / "report.md"),
            "--transcript",
            str(TRANSCRIPT),
            "--expected",
            str(root / "expected.tsv"),
            "--schema",
            str(root / "schema.md"),
        ],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = proc.stdout + proc.stderr
    fail_lines = {line for line in output.splitlines() if line.startswith("FAIL: ")}
    match = re.search(r"^warnings=(\d+)$", output, re.M)
    warning_count = int(match.group(1)) if match else -1
    return proc.returncode, output, fail_lines, warning_count


def hashes(paths: list[Path]) -> dict[str, str]:
    return {
        path.relative_to(REPO).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep", action="store_true")
    parser.add_argument("--workdir", type=Path)
    args = parser.parse_args()

    before = hashes(FROZEN_INPUTS)
    managed_temp = args.workdir is None
    root = args.workdir or Path(tempfile.mkdtemp(prefix="ruler_candidate_selftest_"))
    baseline = root / "baseline"
    build_baseline(baseline)

    baseline_code, baseline_output, baseline_fails, baseline_warnings = run_gate(baseline)
    print(
        f"baseline_exit={baseline_code} baseline_failures={len(baseline_fails)} "
        f"baseline_warnings={baseline_warnings}"
    )
    if baseline_code != 0 or baseline_fails or baseline_warnings != 0:
        print("FAIL: baseline is not clean")
        print(baseline_output)
        if managed_temp and not args.keep:
            shutil.rmtree(root, ignore_errors=True)
        return 1

    detected: list[str] = []
    undetected: list[str] = []
    rows: list[tuple[str, str, int, str]] = []
    for name, pattern, mutator, purpose in FIXTURES:
        work = root / name
        shutil.copytree(baseline, work)
        mutator(work)
        code, _output, fail_lines, _warning_count = run_gate(work)
        new_failures = sorted(fail_lines - baseline_fails)
        hit = any(re.search(pattern, line) for line in new_failures)
        verdict = "DETECTED" if hit else "UNDETECTED"
        (detected if hit else undetected).append(name)
        sample = new_failures[0].replace(str(work), "FIXTURE_ROOT") if new_failures else "(no new failure)"
        rows.append((name, verdict, code, sample[:180]))

    print("fixture\tverdict\texit\tnew_failure_sample")
    for name, verdict, code, sample in rows:
        print(f"{name}\t{verdict}\t{code}\t{sample}")

    after = hashes(FROZEN_INPUTS)
    source_unchanged = before == after
    print(
        f"detected={len(detected)} undetected={len(undetected)} "
        f"source_unchanged={source_unchanged}"
    )
    if undetected:
        for name in undetected:
            purpose = next(purpose for fixture, _pattern, _mutator, purpose in FIXTURES if fixture == name)
            print(f"FAIL: UNDETECTED fixture {name}: {purpose}")
    if not source_unchanged:
        drift = sorted(key for key in before if before.get(key) != after.get(key))
        print(f"FAIL: source drift: {','.join(drift)}")

    if args.keep or not managed_temp:
        print(f"workdir={root}")
    else:
        shutil.rmtree(root, ignore_errors=True)

    if undetected or not source_unchanged:
        print("selftest: FAIL")
        return 1
    print("selftest: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
