from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_PATH = ROOT / "EXPECTED_ITEM_IDS_260828.tsv"
MANIFEST_PATH = ROOT / "AUTHOR_INPUT_MANIFEST_260828.tsv"

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
]


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def expected_ids() -> list[str]:
    _, rows = read_tsv(EXPECTED_PATH)
    return [row["item_id"] for row in rows]


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


def check_manifest(failures: list[str]) -> None:
    _, rows = read_tsv(MANIFEST_PATH)
    ok = 0
    for row in rows:
        path = Path(row["path"])
        if not path.exists():
            failures.append(f"manifest missing: {path}")
            continue
        payload = path.read_bytes()
        actual_hash = hashlib.sha256(payload).hexdigest()
        if len(payload) != int(row["bytes"]):
            failures.append(f"manifest byte mismatch: {path}")
        elif actual_hash != row["sha256"]:
            failures.append(f"manifest hash mismatch: {path}")
        else:
            ok += 1
    print(f"manifest_ok={ok}/{len(rows)}")


def require_columns(actual: list[str], required: list[str], path: Path, failures: list[str]) -> None:
    if actual != required:
        failures.append(f"schema mismatch: {path}; expected={required}; observed={actual}")


def check_items(path: Path, expected: list[str], failures: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        failures.append(f"missing item artifact: {path}")
        print_id_result(compare_ids(expected, []))
        return []
    columns, rows = read_tsv(path)
    require_columns(columns, ITEM_COLUMNS, path, failures)
    observed = [row.get("item_id", "") for row in rows]
    result = compare_ids(expected, observed)
    print_id_result(result)
    if result["duplicate"] or result["missing"] or result["extra"]:
        failures.append(f"identifier mismatch: {path}")
    for index, row in enumerate(rows, start=2):
        missing_values = [column for column in ITEM_COLUMNS if not row.get(column, "").strip()]
        if missing_values:
            failures.append(f"blank fields at {path}:{index}: {','.join(missing_values)}")
        corrupted_values = [
            column
            for column in ITEM_COLUMNS
            if "?" in row.get(column, "") or "\ufffd" in row.get(column, "")
        ]
        if corrupted_values:
            failures.append(
                f"content-integrity failure at {path}:{index}: "
                f"{','.join(corrupted_values)}"
            )
        control_values = [
            column
            for column in ITEM_COLUMNS
            if any(ord(char) < 32 and char not in "\t\n\r" for char in row.get(column, ""))
        ]
        if control_values:
            failures.append(
                f"control-character failure at {path}:{index}: "
                f"{','.join(control_values)}"
            )
    by_id = {row.get("item_id", ""): row for row in rows}
    if "S-17" in expected and "S-17" in by_id:
        blocked_row = by_id["S-17"]
        if "BLOCKED" not in blocked_row.get("assignment_or_BLOCKED", ""):
            failures.append("S-17 assignment must remain BLOCKED")
        if blocked_row.get("tier", "").strip() != "BLOCKED":
            failures.append("S-17 tier must be BLOCKED")
    return rows


def check_types(path: Path, expected: list[str], failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing type artifact: {path}")
        return
    columns, rows = read_tsv(path)
    require_columns(columns, TYPE_COLUMNS, path, failures)
    if not 5 <= len(rows) <= 12:
        failures.append(f"type group count outside 5..12: {len(rows)}")
    members: list[str] = []
    for index, row in enumerate(rows, start=2):
        missing_values = [column for column in TYPE_COLUMNS if not row.get(column, "").strip()]
        if missing_values:
            failures.append(f"blank fields at {path}:{index}: {','.join(missing_values)}")
        corrupted_values = [
            column
            for column in TYPE_COLUMNS
            if "?" in row.get(column, "") or "\ufffd" in row.get(column, "")
        ]
        if corrupted_values:
            failures.append(
                f"content-integrity failure at {path}:{index}: "
                f"{','.join(corrupted_values)}"
            )
        members.extend(item.strip() for item in row.get("member_item_ids", "").split(",") if item.strip())
    result = compare_ids(expected, members)
    print("type_membership_gate:")
    print_id_result(result)
    if result["duplicate"] or result["missing"] or result["extra"]:
        failures.append("type membership is not an exclusive exact cover")


def require_report(path: Path, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing report: {path}")
        return
    text = path.read_text(encoding="utf-8-sig")
    required_markers = [
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
    for marker in required_markers:
        if marker not in text:
            failures.append(f"report marker missing: {marker}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--phase",
        choices=("inputs", "pilot", "wave2a", "author", "final"),
        required=True,
    )
    args = parser.parse_args()
    failures: list[str] = []
    check_manifest(failures)
    all_expected = expected_ids()
    if args.phase == "pilot":
        check_items(ROOT / "author" / "pilot_items.tsv", all_expected[:10], failures)
        require_report(ROOT / "author" / "pilot_report.md", failures)
    elif args.phase == "wave2a":
        check_items(ROOT / "author" / "wave02a_items.tsv", all_expected[10:20], failures)
        require_report(ROOT / "author" / "wave02a_report.md", failures)
    elif args.phase in {"author", "final"}:
        check_items(ROOT / "author" / "items.tsv", all_expected, failures)
        check_types(ROOT / "author" / "types.tsv", all_expected, failures)
        require_report(ROOT / "author" / "AUTHOR_REPORT_260828.md", failures)
    if args.phase == "final":
        for relative in (
            "audit/EVIDENCE_AUDIT_260828.md",
            "critique/ADVERSARIAL_CRITIQUE_260828.md",
            "GATE_REPORT_260828.md",
            "SOL_OPUS_COMPARISON_REPORT_260828.md",
            "260828_CC_RELAY_SOL_OPUS_COMPARISON.md",
            "LANE_RUNTIME_EVIDENCE_260828.tsv",
        ):
            if not (ROOT / relative).exists():
                failures.append(f"missing final artifact: {relative}")
    print(f"warnings=0")
    print(f"failures={len(failures)}")
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        print("experiment-gate: FAIL")
        return 1
    print(f"experiment-gate: PASS phase={args.phase}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
