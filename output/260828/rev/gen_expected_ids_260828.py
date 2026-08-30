"""R1 참조 구현 — 자(ruler)를 손으로 쓰지 말고 **동결 원본에서 생성**한다.

배경: `EXPECTED_ITEM_IDS_260828.tsv`는 사람이 타이핑한 표이고, W-04 범위는 파서 버그를
출력 쪽에서 손으로 고친 결과다(`TEAM_PREFLIGHT_260828.md:33` 자인). 그 결과 자가 무엇을
측정하는지가 코드가 아니라 산문에만 남았고, 측정 후 자 변경을 사후에 해시로 잡을 수밖에 없었다.

이 도구는 `corpus/EX-math2-20252M/transcript.md` 하나에서 item_id·행범위를 **결정론적으로
재생성**하고, 현행 자와 대조한다. gatekeeper가 이 방식을 채택하면 "자를 손으로 고치는" 조작은
다음 실행에서 덮어써지므로 **실패 모드 자체가 소멸**한다.

CLAUDE.md 원칙 8: codex-team 파일은 읽기만 한다. `--emit`은 rev/ 안에만 쓴다.
CLAUDE.md 원칙 11: 통과 판정은 exit 0 + `warnings=0` + `diff_count=0` 세 줄이 모두 맞을 때뿐이다.

usage:
  python output/260828/rev/gen_expected_ids_260828.py
  python output/260828/rev/gen_expected_ids_260828.py --emit
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TRANSCRIPT = REPO / "corpus/EX-math2-20252M/transcript.md"
SHIPPED = REPO / "output/260828/diagnostic/math2-method-comparison/codex-team/EXPECTED_ITEM_IDS_260828.tsv"
EMIT_TO = Path(__file__).resolve().parent / "EXPECTED_ITEM_IDS_260828.regenerated.tsv"

SECTION_PREFIX = {"서술형 문항": "W", "단답형 문항": "S"}

RE_SECTION = re.compile(r"^#\s+(.+?)\s*$")
RE_ITEM = re.compile(r"^##\s+(\d+)\.\s*$")
RE_BOUNDARY = re.compile(r"^(#{1,6}\s|-{3,}\s*$)")


def parse(lines: list[str]) -> list[dict[str, object]]:
    """항목 헤딩과 경계선만으로 행범위를 유도한다. 어떤 값도 손으로 적지 않는다."""
    boundaries = [no for no, text in enumerate(lines, start=1) if RE_BOUNDARY.match(text)]
    items: list[dict[str, object]] = []
    prefix = ""
    for no, text in enumerate(lines, start=1):
        section = RE_SECTION.match(text)
        if section and section.group(1) in SECTION_PREFIX:
            prefix = SECTION_PREFIX[section.group(1)]
            continue
        item = RE_ITEM.match(text)
        if not item or not prefix:
            continue
        nxt = next((b for b in boundaries if b > no), len(lines) + 1)
        body = range(no + 1, nxt)
        last_nonblank = max((n for n in body if lines[n - 1].strip()), default=no)
        items.append(
            {
                "item_id": f"{prefix}-{int(item.group(1)):02d}",
                "section": "written" if prefix == "W" else "short-answer",
                "number": int(item.group(1)),
                "start_line": no,
                "end_rule_a": nxt - 1,        # 다음 경계 직전까지 (후행 공백 1줄 포함)
                "end_rule_b": last_nonblank,  # 마지막 비공백 행까지
            }
        )
    return items


def read_shipped() -> dict[str, tuple[int, int]]:
    with SHIPPED.open(encoding="utf-8-sig", newline="") as handle:
        return {
            row["item_id"]: (int(row["start_line"]), int(row["end_line"]))
            for row in csv.DictReader(handle, delimiter="\t")
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rule", choices=("a", "b"), default="a")
    parser.add_argument("--emit", action="store_true", help="재생성 결과를 rev/ 안에 기록")
    args = parser.parse_args()

    lines = TRANSCRIPT.read_text(encoding="utf-8-sig").splitlines()
    derived = parse(lines)
    shipped = read_shipped()

    print(f"transcript_lines={len(lines)}")
    print(f"derived_items={len(derived)} shipped_items={len(shipped)}")

    failures: list[str] = []
    warnings: list[str] = []

    derived_ids = [row["item_id"] for row in derived]
    if derived_ids != list(shipped):
        failures.append(f"identifier set differs: derived={derived_ids} shipped={list(shipped)}")

    # 두 규칙 각각이 현행 자를 재현하는지 — 재현하는 규칙이 없으면 자는 생성물이 아니다.
    rule_diffs: dict[str, list[str]] = {}
    for rule in ("a", "b"):
        diffs = []
        for row in derived:
            item_id = str(row["item_id"])
            if item_id not in shipped:
                continue
            want = (int(row["start_line"]), int(row[f"end_rule_{rule}"]))
            got = shipped[item_id]
            if want != got:
                diffs.append(f"{item_id}: rule_{rule}={want[0]}-{want[1]} shipped={got[0]}-{got[1]}")
        rule_diffs[rule] = diffs
        print(f"rule_{rule}_diff_count={len(diffs)}")

    if rule_diffs["a"] and rule_diffs["b"]:
        failures.append(
            "NO SINGLE RULE REPRODUCES THE SHIPPED RULER "
            f"(rule_a diffs={len(rule_diffs['a'])}, rule_b diffs={len(rule_diffs['b'])}) "
            "-> the ruler is hand-authored, not generated"
        )
    for line in rule_diffs[args.rule]:
        failures.append(f"diff(rule_{args.rule}) {line}")

    if args.emit:
        with EMIT_TO.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
            writer.writerow(
                ["item_id", "section", "number", "source_path", "start_line", "end_line", "derivation_rule"]
            )
            for row in derived:
                writer.writerow(
                    [
                        row["item_id"],
                        row["section"],
                        row["number"],
                        "corpus/EX-math2-20252M/transcript.md",
                        row["start_line"],
                        row[f"end_rule_{args.rule}"],
                        f"rule_{args.rule}",
                    ]
                )
        print(f"emitted={EMIT_TO.relative_to(REPO).as_posix()}")

    print(f"warnings={len(warnings)}")
    print(f"failures={len(failures)}")
    for item in warnings:
        print(f"WARN: {item}")
    for item in failures:
        print(f"FAIL: {item}")
    if failures or warnings:
        print("ruler-generation: FAIL")
        return 1
    print(f"ruler-generation: PASS rule={args.rule}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
