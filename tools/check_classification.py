#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_classification.py — 1차 분류 표준 템플릿 게이트 (stub, v1.0)

목적: docs/templates/CLASSIFICATION_TEMPLATE.md §7·§8을 코드로 집행.
현재는 스텁 — S2에서 S3 동결 전까지는 advisory(경고만)로 동작해야 하며,
S3 동결 후 fail-closed로 전환한다.

Usage:
  python tools/check_classification.py --check output/260902/EX-math2-20252M_classification.md
  python tools/check_classification.py --check output/260901/260901_03_SUP-math2-2026_classification_TRUE.md

Checks (fail-closed when frozen):
  1. §0 게이트: 예상==관측==§1 행 수, L? 0건
  2. 동반 TSV 2종 존재·BOM·11열·헤더 일치
  3. Markdown §1 표와 _items.tsv item_id byte-equal
  4. reusable row는 variation_axis_1·2 둘 다 채움
  5. rendered_evidence_status 분기 표기

Status: candidate-only — 본 파일 자체는 템플릿의 일부이며, S2 자격·S3 재동결 전에는
정식 게이트로 쓰지 않는다. (ACCEPTANCE_SCHEMA.candidate §6)
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "docs/templates/CLASSIFICATION_TEMPLATE.md"
SCHEMA = ROOT / "tools/schemas/classification.schema.json"

ITEMS_HEADER = [
    "item_id", "source_lines", "rendered_evidence_status",
    "assignment_or_BLOCKED", "existing_type_or_decision_request",
    "rationale", "tier", "tier_basis", "observed_trap", "confidence", "generator_id",
]
TYPES_HEADER = [
    "group_id", "member_item_ids", "type_disposition",
    "variation_axis_1", "variation_axis_2", "observed_trap",
    "importance_source_axis", "common_types_disposition",
    "catalog_disposition", "generator_id", "row_kind",
]

def main():
    import argparse
    ap = argparse.ArgumentParser(description="1차 분류 템플릿 게이트 (stub)")
    ap.add_argument("--check", metavar="MD", help="classification markdown 경로")
    args = ap.parse_args()

    if not args.check:
        print(f"[INFO] template: {TEMPLATE}")
        print(f"[INFO] schema  : {SCHEMA}")
        print(f"[INFO] items header: {' | '.join(ITEMS_HEADER)}")
        print(f"[INFO] types header: {' | '.join(TYPES_HEADER)}")
        print("[INFO] usage: python tools/check_classification.py --check <md>")
        return 0

    md = Path(args.check)
    if not md.exists():
        print(f"[FAIL] not found: {md}")
        return 1

    text = md.read_text(encoding="utf-8")
    warnings = []
    failures = []

    # 1. L? 플레이스홀더 검출
    lq = text.count("L?")
    if lq:
        failures.append(f"L? placeholder {lq}건 - source_lines 미기재 (fail-closed)")

    # 2. 게이트 표 존재
    if "## §0" not in text and "## 0." not in text:
        warnings.append("S0 gate section not found - check template S0 header")

    # 3. 동반 TSV 존재 (추정 경로)
    stem = md.stem.replace("_classification", "").replace("_TRUE", "")
    # 실제 파일명은 <YYMMDD>_<NN>_<corpus-id>_classification.md 이므로 corpus-id 추출 시도
    # 스텁에서는 존재 여부만 경고
    items_tsv = md.with_name(md.stem.replace("_classification", "_classification_items.tsv").replace("_TRUE", ""))
    types_tsv = md.with_name(md.stem.replace("_classification", "_classification_types.tsv").replace("_TRUE", ""))
    # 더 관대한 탐색: 같은 디렉터리의 *_items.tsv
    siblings = list(md.parent.glob("*_items.tsv"))
    if not siblings and not items_tsv.exists():
        warnings.append(f"companion _items.tsv not found (expected {items_tsv.name}) - S8 requires 2 TSVs")
    siblings2 = list(md.parent.glob("*_types.tsv"))
    if not siblings2 and not types_tsv.exists():
        warnings.append(f"companion _types.tsv not found (expected {types_tsv.name})")

    # 4. reusable 축 2개 키워드 검사 (휴리스틱)
    if "variation_axis" in text.lower() or "변형축" in text:
        pass
    else:
        if "## §2" in text or "## 2." in text:
            warnings.append("S2 consolidation: variation_axis keyword not found - check reusable 2 axes")

    print(f"warnings={len(warnings)} failures={len(failures)}")
    for w in warnings:
        print(f"[WARN] {w}")
    for f in failures:
        print(f"[FAIL] {f}")

    # 스텁은 advisory — failures가 있어도 S3 동결 전까지는 exit 0을 유지할 수 있으나,
    # L?는 명백한 fail-closed이므로 실패로 처리한다.
    if failures:
        print("experiment-gate: FAIL (stub)")
        return 1
    if warnings:
        print("experiment-gate: PASS (with warnings — advisory, S3 동결 전)")
        return 0
    print("experiment-gate: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
