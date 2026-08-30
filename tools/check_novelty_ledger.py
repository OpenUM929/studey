#!/usr/bin/env python3
"""Fail-closed coverage and evidence checks for problem-set novelty ledgers.

This tool validates the auditable contract around semantic novelty.  It cannot prove that a
mathematical idea is original; that remains a reviewer judgment.  It does prove that every
item has one unique evidence row, two non-empty non-cosmetic axis claims, a structural
difference statement, a nearest-prior reference, a PASS verdict, and a matching main type.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path


HEADER = [
    "item_id",
    "type_id",
    "invariant",
    "non_numeric_axis_1",
    "non_numeric_axis_2",
    "structural_difference",
    "nearest_prior",
    "verdict",
]
ITEM_RE = re.compile(r"^\*\*(\d+)\.\*\*", re.MULTILINE)
TYPE_RE = re.compile(r"\b(SM2-\d{2})\b")
COSMETIC_TOKEN_RE = re.compile(
    r"(?:숫자|수치|계수|좌표|길이|각도|개수|부호|문자명?|상수|값)"
    r"(?:\s*(?:변경|교체|조정|바꿈|치환))?",
    re.IGNORECASE,
)
SEPARATOR_RE = re.compile(r"[\s,;/+·→↔:()\[\]{}=_-]+")


def parse_items(markdown: str) -> tuple[list[str], dict[str, str]]:
    matches = list(ITEM_RE.finditer(markdown))
    ids: list[str] = []
    types: dict[str, str] = {}
    for index, match in enumerate(matches):
        item_id = match.group(1)
        ids.append(item_id)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        block = markdown[match.start() : end]
        type_matches = TYPE_RE.findall(block)
        if type_matches:
            # The first SM2 tag in the item block is the main type. Later tags may be
            # explicit auxiliaries such as `(+SM2-11)` and must not replace the main type.
            types[item_id] = type_matches[0]
    return ids, types


def read_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    failures: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        raw_rows = list(reader)
    observed_header = raw_rows[0] if raw_rows else None
    if observed_header != HEADER:
        failures.append(f"header_mismatch expected={HEADER} observed={observed_header}")
    rows: list[dict[str, str]] = []
    for line_number, raw_row in enumerate(raw_rows[1:], start=2):
        if len(raw_row) != len(HEADER):
            failures.append(
                f"row={line_number} field_count={len(raw_row)} expected={len(HEADER)}"
            )
        normalized = (raw_row + [""] * len(HEADER))[: len(HEADER)]
        rows.append(dict(zip(HEADER, normalized)))
    return rows, failures


def axis_is_cosmetic_only(value: str) -> bool:
    stripped = value.strip()
    if not stripped:
        return True
    remainder = COSMETIC_TOKEN_RE.sub("", stripped)
    remainder = re.sub(r"[-+]?\d+(?:\.\d+)?", "", remainder)
    remainder = SEPARATOR_RE.sub("", remainder)
    return remainder == ""


def sort_ids(values: set[str] | list[str]) -> list[str]:
    return sorted(values, key=lambda value: (not value.isdigit(), int(value) if value.isdigit() else value))


def validate(set_path: Path, ledger_path: Path, required_count: int | None) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []

    expected_ledger_path = set_path.with_suffix(".novelty.tsv")
    if ledger_path.resolve(strict=False) != expected_ledger_path.resolve(strict=False):
        failures.append(
            f"ledger_path_mismatch expected={expected_ledger_path} observed={ledger_path}"
        )

    markdown = set_path.read_text(encoding="utf-8-sig")
    expected_sequence, set_types = parse_items(markdown)
    expected_counts = Counter(expected_sequence)
    expected_ids = set(expected_sequence)
    if not expected_ids:
        failures.append("set_has_no_item_headers")
    for item_id, count in expected_counts.items():
        if count > 1:
            failures.append(f"duplicate_set_item_id={item_id} count={count}")
    if required_count is not None and len(expected_ids) != required_count:
        failures.append(f"required_count={required_count} observed_set_items={len(expected_ids)}")

    rows, ledger_failures = read_ledger(ledger_path)
    failures.extend(ledger_failures)
    observed_sequence = [(row.get("item_id") or "").strip() for row in rows]
    observed_counts = Counter(observed_sequence)
    observed_ids = {item_id for item_id in observed_sequence if item_id}
    duplicates = {item_id for item_id, count in observed_counts.items() if item_id and count > 1}
    missing = expected_ids - observed_ids
    extra = observed_ids - expected_ids

    if duplicates:
        failures.append(f"duplicate_ledger_ids={sort_ids(duplicates)}")
    if missing:
        failures.append(f"missing_ledger_ids={sort_ids(missing)}")
    if extra:
        failures.append(f"extra_ledger_ids={sort_ids(extra)}")

    for row_number, row in enumerate(rows, start=2):
        item_id = (row.get("item_id") or "").strip()
        type_id = (row.get("type_id") or "").strip()
        invariant = (row.get("invariant") or "").strip()
        axis_1 = (row.get("non_numeric_axis_1") or "").strip()
        axis_2 = (row.get("non_numeric_axis_2") or "").strip()
        difference = (row.get("structural_difference") or "").strip()
        nearest = (row.get("nearest_prior") or "").strip()
        verdict = (row.get("verdict") or "").strip().upper()

        if not item_id:
            failures.append(f"row={row_number} empty_item_id")
        if not TYPE_RE.fullmatch(type_id):
            failures.append(f"item={item_id or '?'} invalid_type_id={type_id!r}")
        elif item_id in set_types and set_types[item_id] != type_id:
            failures.append(
                f"item={item_id} type_mismatch set={set_types[item_id]} ledger={type_id}"
            )
        elif item_id in expected_ids and item_id not in set_types:
            failures.append(f"item={item_id} set_type_tag_missing")
        if len(invariant) < 5:
            failures.append(f"item={item_id or '?'} invariant_missing_or_too_short")
        if axis_is_cosmetic_only(axis_1):
            failures.append(f"item={item_id or '?'} axis_1_numeric_or_cosmetic={axis_1!r}")
        if axis_is_cosmetic_only(axis_2):
            failures.append(f"item={item_id or '?'} axis_2_numeric_or_cosmetic={axis_2!r}")
        if axis_1 and axis_1 == axis_2:
            failures.append(f"item={item_id or '?'} duplicate_axis_claim={axis_1!r}")
        if len(difference) < 20:
            failures.append(f"item={item_id or '?'} structural_difference_too_short")
        if nearest.lower() in {"", "-", "none", "n/a", "없음"}:
            failures.append(f"item={item_id or '?'} nearest_prior_missing")
        if verdict != "PASS":
            failures.append(f"item={item_id or '?'} verdict={verdict or '<empty>'}")

    print(f"expected_ids={sort_ids(expected_ids)}")
    print(f"observed_ids={sort_ids(observed_ids)}")
    print(f"duplicate_ids={sort_ids(duplicates)}")
    print(f"missing_ids={sort_ids(missing)}")
    print(f"extra_ids={sort_ids(extra)}")
    print(f"warnings={len(warnings)}")
    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")
    print(f"novelty-gate: {'PASS' if not failures and not warnings else 'FAIL'}")
    return failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", dest="set_path", required=True, type=Path)
    parser.add_argument("--ledger", dest="ledger_path", required=True, type=Path)
    parser.add_argument("--required-count", type=int)
    args = parser.parse_args()

    try:
        failures, warnings = validate(args.set_path, args.ledger_path, args.required_count)
    except (OSError, UnicodeError, csv.Error) as exc:
        print("expected_ids=[]")
        print("observed_ids=[]")
        print("duplicate_ids=[]")
        print("missing_ids=[]")
        print("extra_ids=[]")
        print("warnings=0")
        print(f"FAIL: {type(exc).__name__}: {exc}")
        print("novelty-gate: FAIL")
        return 1
    return 0 if not failures and not warnings else 1


if __name__ == "__main__":
    sys.exit(main())
