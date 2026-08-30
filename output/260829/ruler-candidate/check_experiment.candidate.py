"""S1 candidate gate for the Math2 assessment-analysis artifacts.

The gate is a candidate implementation, not a freeze or approval.  It accepts
explicit artifact paths so the differential self-test can operate only inside
temporary/fixture trees.  No measured output is modified.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from types import ModuleType

sys.dont_write_bytecode = True


REPO = Path(__file__).resolve().parents[3]
CANDIDATE_DIR = Path(__file__).resolve().parent
DEFAULT_TRANSCRIPT = REPO / "corpus/EX-math2-20252M/transcript.md"
DEFAULT_SCHEMA = CANDIDATE_DIR / "ACCEPTANCE_SCHEMA.candidate.md"
GENERATOR_PATH = CANDIDATE_DIR / "gen_expected_ids.candidate.py"

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
LEGACY_ITEM_COLUMNS = ITEM_COLUMNS[:-1]

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
LEGACY_TYPE_COLUMNS = TYPE_COLUMNS[:-2]
ROW_KINDS = {"reusable", "singleton", "blocked"}

REPORT_MARKERS = [
    "expected identifiers",
    "observed identifiers",
    "duplicate identifiers",
    "missing identifiers",
    "extra identifiers",
    "COMMON_TYPES",
    "HARVEST_LOG draft",
    "EXTRACTION_LOG draft",
    "runtime identity",
    "no pNN",
    "answer_key: null",
]

SCHEMA_MARKERS = [
    "status: candidate-only",
    "grade: advisory",
    "freeze_authority: none",
    "generator_id",
    "row_kind",
    "maximal equivalence classes",
    "There is no lower bound, upper bound, or hard-coded expected row total",
    "Bookkeeping umbrella rows are prohibited",
    "experiment-gate: PASS",
    "cannot qualify, refreeze, approve, release, benchmark, or consume",
]


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def generator_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("candidate_expected_generator", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load generator: {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compare_ids(expected: list[str], observed: list[str]) -> dict[str, list[str]]:
    counts = Counter(observed)
    return {
        "expected": expected,
        "observed": observed,
        "duplicate": sorted(item for item, count in counts.items() if count > 1),
        "missing": sorted(set(expected) - set(observed)),
        "extra": sorted(set(observed) - set(expected)),
    }


def print_id_result(result: dict[str, list[str]]) -> None:
    for key in ("expected", "observed", "duplicate", "missing", "extra"):
        print(f"{key}={','.join(result[key]) or '[]'}")


def bad_control(value: str) -> bool:
    return any(ord(char) < 32 and char not in "\t\n\r" for char in value)


def corrupted(value: str) -> bool:
    return "?" in value or "\ufffd" in value


def require_columns(
    actual: list[str],
    required: list[str],
    path: Path,
    failures: list[str],
) -> None:
    if actual != required:
        failures.append(f"schema mismatch: {path}; expected={required}; observed={actual}")


def load_expected(
    transcript: Path,
    expected_path: Path | None,
    failures: list[str],
) -> list[dict[str, str]]:
    module = generator_module()
    regenerated = module.derive_rows(transcript)
    if expected_path is None:
        return regenerated
    columns, supplied = read_tsv(expected_path)
    require_columns(columns, module.OUTPUT_COLUMNS, expected_path, failures)
    if supplied != regenerated:
        supplied_by_id = {row.get("item_id", ""): row for row in supplied}
        regenerated_by_id = {row["item_id"]: row for row in regenerated}
        changed = sorted(
            item_id
            for item_id in set(supplied_by_id) | set(regenerated_by_id)
            if supplied_by_id.get(item_id) != regenerated_by_id.get(item_id)
        )
        failures.append(
            "expected ruler mismatch against transcript regeneration: "
            f"changed={','.join(changed) or '[]'}"
        )
    return regenerated


def check_schema(path: Path, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing acceptance schema: {path}")
        return
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if corrupted(text) or bad_control(text):
        failures.append(f"ACCEPTANCE_SCHEMA content-integrity failure: {path}")
    missing = [marker for marker in SCHEMA_MARKERS if marker not in text]
    if missing:
        failures.append(
            f"acceptance schema marker missing: {path}; markers={','.join(missing)}"
        )


def check_items(
    path: Path,
    expected_rows: list[dict[str, str]],
    failures: list[str],
    warnings: list[str],
) -> tuple[list[dict[str, str]], dict[str, str]]:
    expected_ids = [row["item_id"] for row in expected_rows]
    expected_by_id = {row["item_id"]: row for row in expected_rows}
    if not path.exists():
        failures.append(f"missing item artifact: {path}")
        print_id_result(compare_ids(expected_ids, []))
        return [], {}
    columns, rows = read_tsv(path)
    row_required_columns = ITEM_COLUMNS
    if columns == LEGACY_ITEM_COLUMNS:
        warnings.append(f"legacy item schema has no generator_id: {path}")
        row_required_columns = LEGACY_ITEM_COLUMNS
    require_columns(columns, ITEM_COLUMNS, path, failures)
    observed = [row.get("item_id", "") for row in rows]
    result = compare_ids(expected_ids, observed)
    print("item_identifier_gate:")
    print_id_result(result)
    if result["duplicate"] or result["missing"] or result["extra"]:
        failures.append(f"identifier mismatch: {path}")

    generator_by_item: dict[str, str] = {}
    for index, row in enumerate(rows, start=2):
        missing_values = [
            column for column in row_required_columns if not row.get(column, "").strip()
        ]
        if missing_values:
            failures.append(f"blank fields at {path}:{index}: {','.join(missing_values)}")
        corrupted_values = [
            column for column in columns if corrupted(row.get(column, ""))
        ]
        if corrupted_values:
            failures.append(
                f"content-integrity failure at {path}:{index}: {','.join(corrupted_values)}"
            )
        control_values = [
            column for column in columns if bad_control(row.get(column, ""))
        ]
        if control_values:
            failures.append(
                f"control-character failure at {path}:{index}: {','.join(control_values)}"
            )
        item_id = row.get("item_id", "")
        generator_id = row.get("generator_id", "").strip()
        if item_id and generator_id:
            generator_by_item[item_id] = generator_id
        expected = expected_by_id.get(item_id)
        if expected:
            wanted_source = (
                f"{expected['source_path']}:{expected['start_line']}-{expected['end_line']}"
            )
            observed_source = row.get("source_lines", "").split(";", 1)[0].strip()
            if observed_source != wanted_source:
                failures.append(
                    f"source span mismatch: {item_id} expected={wanted_source} "
                    f"observed={observed_source}"
                )

    by_id = {row.get("item_id", ""): row for row in rows}
    if "S-17" in expected_by_id and "S-17" in by_id:
        blocked_row = by_id["S-17"]
        if "BLOCKED" not in blocked_row.get("assignment_or_BLOCKED", ""):
            failures.append("S-17 assignment must remain BLOCKED")
        if blocked_row.get("tier", "").strip() != "BLOCKED":
            failures.append("S-17 tier must be BLOCKED")
        generator_id = blocked_row.get("generator_id", "").strip()
        if generator_id and not generator_id.startswith("BLOCKED-"):
            failures.append("S-17 generator_id must start with BLOCKED-")
    return rows, generator_by_item


def is_umbrella(row: dict[str, str]) -> bool:
    text = " ".join(row.values()).lower()
    signals = (
        "umbrella",
        "bookkeeping",
        "우산",
        "서로 독립 subgroup",
        "하나의 reusable type가 아님",
    )
    return any(signal in text for signal in signals)


def row_members(row: dict[str, str]) -> list[str]:
    return [
        item.strip()
        for item in row.get("member_item_ids", "").split(",")
        if item.strip()
    ]


def reference_expansion(
    rows: list[dict[str, str]], expected_ids: list[str]
) -> tuple[int, int, int, int, int, int]:
    expanded = reusable = singleton = blocked = 0
    members: list[str] = []
    for row in rows:
        current = row_members(row)
        members.extend(current)
        kind = row.get("row_kind", "").strip()
        if is_umbrella(row):
            expanded += len(current)
            singleton += len(current)
        elif kind == "blocked" or row.get("group_id", "").startswith("BLOCKED-"):
            expanded += 1
            blocked += 1
        elif kind == "reusable" or len(current) >= 2:
            expanded += 1
            reusable += 1
        else:
            expanded += 1
            singleton += 1
    uncovered = len(set(expected_ids) - set(members))
    return expanded, reusable, singleton, blocked, len(set(members)), uncovered


def check_types(
    path: Path,
    expected_ids: list[str],
    item_rows: list[dict[str, str]],
    generator_by_item: dict[str, str],
    failures: list[str],
    warnings: list[str],
) -> None:
    if not path.exists():
        failures.append(f"missing type artifact: {path}")
        return
    columns, rows = read_tsv(path)
    row_required_columns = TYPE_COLUMNS
    if columns == LEGACY_TYPE_COLUMNS:
        warnings.append(f"legacy type schema has no generator_id/row_kind: {path}")
        row_required_columns = LEGACY_TYPE_COLUMNS
    require_columns(columns, TYPE_COLUMNS, path, failures)

    umbrellas = [row.get("group_id", "") for row in rows if is_umbrella(row)]
    print(f"umbrella_rows={len(umbrellas)} ids={','.join(umbrellas) or '[]'}")
    for group_id in umbrellas:
        failures.append(f"umbrella row prohibited: {group_id}")

    members: list[str] = []
    type_rows_by_generator: dict[str, list[dict[str, str]]] = defaultdict(list)
    for index, row in enumerate(rows, start=2):
        missing_values = [
            column for column in row_required_columns if not row.get(column, "").strip()
        ]
        if missing_values:
            failures.append(f"blank fields at {path}:{index}: {','.join(missing_values)}")
        corrupted_values = [column for column in columns if corrupted(row.get(column, ""))]
        if corrupted_values:
            failures.append(
                f"content-integrity failure at {path}:{index}: {','.join(corrupted_values)}"
            )
        control_values = [column for column in columns if bad_control(row.get(column, ""))]
        if control_values:
            failures.append(
                f"control-character failure at {path}:{index}: {','.join(control_values)}"
            )
        current = row_members(row)
        members.extend(current)
        generator_id = row.get("generator_id", "").strip()
        if generator_id:
            type_rows_by_generator[generator_id].append(row)
        kind = row.get("row_kind", "").strip()
        if kind and kind not in ROW_KINDS:
            failures.append(f"invalid row_kind at {path}:{index}: {kind}")

    result = compare_ids(expected_ids, members)
    print("type_membership_gate:")
    print_id_result(result)
    if result["duplicate"] or result["missing"] or result["extra"]:
        failures.append("type membership is not an exclusive exact cover")

    expected_by_generator: dict[str, set[str]] = defaultdict(set)
    for item_id, generator_id in generator_by_item.items():
        expected_by_generator[generator_id].add(item_id)
    if item_rows and not generator_by_item:
        failures.append("generator equivalence unavailable: item rows have no generator_id")

    for generator_id, generator_rows in sorted(type_rows_by_generator.items()):
        if len(generator_rows) != 1:
            group_ids = [row.get("group_id", "") for row in generator_rows]
            failures.append(
                "generator equivalence violation: "
                f"generator_id={generator_id} split across groups={','.join(group_ids)}"
            )
        actual_members = {
            item for row in generator_rows for item in row_members(row)
        }
        expected_members = expected_by_generator.get(generator_id, set())
        if actual_members != expected_members:
            failures.append(
                "generator equivalence violation: "
                f"generator_id={generator_id} expected={','.join(sorted(expected_members)) or '[]'} "
                f"observed={','.join(sorted(actual_members)) or '[]'}"
            )

    missing_generators = sorted(set(expected_by_generator) - set(type_rows_by_generator))
    extra_generators = sorted(set(type_rows_by_generator) - set(expected_by_generator))
    if missing_generators or extra_generators:
        failures.append(
            "generator equivalence violation: "
            f"missing_generators={','.join(missing_generators) or '[]'} "
            f"extra_generators={','.join(extra_generators) or '[]'}"
        )

    item_by_id = {row.get("item_id", ""): row for row in item_rows}
    for index, row in enumerate(rows, start=2):
        current = row_members(row)
        is_blocked = any(
            item_by_id.get(item_id, {}).get("tier", "") == "BLOCKED"
            or "BLOCKED" in item_by_id.get(item_id, {}).get("assignment_or_BLOCKED", "")
            for item_id in current
        )
        expected_kind = "blocked" if is_blocked else ("reusable" if len(current) >= 2 else "singleton")
        kind = row.get("row_kind", "").strip()
        if kind and kind != expected_kind:
            failures.append(
                f"row_kind mismatch at {path}:{index}: expected={expected_kind} observed={kind}"
            )

    expanded, reusable, singleton, blocked, item_count, uncovered = reference_expansion(
        rows, expected_ids
    )
    print(
        "reference_expansion "
        f"rows={expanded} reusable={reusable} singleton={singleton} blocked={blocked} "
        f"items={item_count} uncovered={uncovered}"
    )


def require_report(path: Path, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing report: {path}")
        return
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if corrupted(text) or bad_control(text):
        failures.append(f"report content-integrity failure: {path}")
    for marker in REPORT_MARKERS:
        if marker not in text:
            failures.append(f"report marker missing: {marker}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--types", type=Path, required=True)
    parser.add_argument("--items", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--transcript", type=Path, default=DEFAULT_TRANSCRIPT)
    parser.add_argument("--expected", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    failures: list[str] = []
    warnings: list[str] = []
    report = args.report or args.items.parent / "AUTHOR_REPORT_260828.md"

    expected_rows = load_expected(args.transcript, args.expected, failures)
    expected_ids = [row["item_id"] for row in expected_rows]
    check_schema(args.schema, failures)
    item_rows, generator_by_item = check_items(
        args.items, expected_rows, failures, warnings
    )
    check_types(
        args.types,
        expected_ids,
        item_rows,
        generator_by_item,
        failures,
        warnings,
    )
    require_report(report, failures)

    print(f"warnings={len(warnings)}")
    print(f"failures={len(failures)}")
    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures or warnings:
        print("experiment-gate: FAIL")
        return 1
    print("experiment-gate: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
