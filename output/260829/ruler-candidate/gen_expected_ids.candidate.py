"""Generate the candidate item-span ruler from the frozen transcript.

This is an S1 candidate.  It does not freeze or approve its own output.  The
only source of item identifiers and line spans is the transcript supplied on
the command line.  Headings, horizontal rules, and EOF are boundaries.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterable, TextIO


REPO = Path(__file__).resolve().parents[3]
DEFAULT_TRANSCRIPT = REPO / "corpus/EX-math2-20252M/transcript.md"
SECTION_PREFIX = {"서술형 문항": "W", "단답형 문항": "S"}
SECTION_NAME = {"W": "written", "S": "short-answer"}
RE_SECTION = re.compile(r"^#\s+(.+?)\s*$")
RE_ITEM = re.compile(r"^##\s+(\d+)\.\s*$")
RE_BOUNDARY = re.compile(r"^(?:#{1,6}\s|(?:-{3,}|\*{3,}|_{3,})\s*$)")
OUTPUT_COLUMNS = [
    "item_id",
    "section",
    "number",
    "source_path",
    "start_line",
    "end_line",
    "pilot_wave",
    "derivation_rule",
]


def repo_label(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO).as_posix()
    except ValueError:
        return resolved.as_posix()


def pilot_wave(position: int) -> str:
    if position <= 10:
        return "pilot-01"
    if position <= 20:
        return "wave-02a"
    return "wave-02b"


def derive_rows(transcript: Path) -> list[dict[str, str]]:
    """Derive every row without item-specific line constants."""
    lines = transcript.read_text(encoding="utf-8-sig").splitlines()
    boundaries = [
        line_no
        for line_no, text in enumerate(lines, start=1)
        if RE_BOUNDARY.match(text)
    ]
    rows: list[dict[str, str]] = []
    prefix = ""
    for line_no, text in enumerate(lines, start=1):
        section = RE_SECTION.match(text)
        if section and section.group(1) in SECTION_PREFIX:
            prefix = SECTION_PREFIX[section.group(1)]
            continue
        item = RE_ITEM.match(text)
        if not item or not prefix:
            continue
        next_boundary = next(
            (boundary for boundary in boundaries if boundary > line_no),
            len(lines) + 1,
        )
        number = int(item.group(1))
        position = len(rows) + 1
        rows.append(
            {
                "item_id": f"{prefix}-{number:02d}",
                "section": SECTION_NAME[prefix],
                "number": str(number),
                "source_path": repo_label(transcript),
                "start_line": str(line_no),
                "end_line": str(next_boundary - 1),
                "pilot_wave": pilot_wave(position),
                "derivation_rule": "rule_a",
            }
        )
    return rows


def write_rows(rows: Iterable[dict[str, str]], handle: TextIO) -> None:
    writer = csv.DictWriter(
        handle,
        fieldnames=OUTPUT_COLUMNS,
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", type=Path, default=DEFAULT_TRANSCRIPT)
    parser.add_argument("--emit", action="store_true")
    args = parser.parse_args()

    rows = derive_rows(args.transcript)
    if args.emit:
        write_rows(rows, sys.stdout)
        return 0

    identifiers = [row["item_id"] for row in rows]
    duplicates = sorted({item for item in identifiers if identifiers.count(item) > 1})
    failures: list[str] = []
    warnings: list[str] = []
    if duplicates:
        failures.append(f"duplicate item identifiers: {','.join(duplicates)}")
    if not rows:
        failures.append("no item headings derived from transcript")
    if any(row["derivation_rule"] != "rule_a" for row in rows):
        failures.append("non-rule_a row emitted")
    print(f"transcript_lines={len(args.transcript.read_text(encoding='utf-8-sig').splitlines())}")
    print(f"derived_items={len(rows)}")
    print(f"warnings={len(warnings)}")
    print(f"failures={len(failures)}")
    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures or warnings:
        print("ruler-generation: FAIL")
        return 1
    print("ruler-generation: PASS rule=rule_a")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
