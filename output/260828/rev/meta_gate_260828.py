"""2차 안전 울타리 — 감사권한자(tier-1/rev) 소유 메타 게이트.

CLAUDE.md 원칙 8에 따라 이 도구는 codex-team 소유 파일을 **읽기만** 한다.
1차 게이트(check_experiment.py, gatekeeper 소유)가 author 레인만 겨냥하는 데 반해,
이 도구는 **gatekeeper가 만든 자(ruler) 자체**를 측정 대상으로 삼는다.

원칙 11: 통과 판정은 exit code 하나가 아니라
  `warnings=<실측> + failures=<실측> + meta-gate: PASS` 3줄이 모두 맞아야 한다.
warnings/failures 는 리터럴이 아니라 리스트 길이에서 계산된다(F1 재발 방지).

usage:
  python output/260828/rev/meta_gate_260828.py --check all
  python output/260828/rev/meta_gate_260828.py --check freeze|integrity|signal|coverage|staleness
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
FREEZE_PATH = Path(__file__).resolve().parent / "RULER_FREEZE_260828.tsv"
TEAM_DIR = REPO / "output/260828/diagnostic/math2-method-comparison/codex-team"
GATE_SRC = TEAM_DIR / "check_experiment.py"

AUTHOR_ARTIFACTS = ("author/items.tsv", "author/types.tsv", "author/AUTHOR_REPORT_260828.md")
VERDICT_DOCS = ("audit/EVIDENCE_AUDIT_260828.md", "critique/ADVERSARIAL_CRITIQUE_260828.md")

MOJIBAKE_MARKS = ("�",)
# 문장 종결 물음표로 인정하는 앞/뒤 문맥
QM_PREV_OK = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)]\"'")
# 닫는 백틱은 의도적으로 제외한다: `?? 1?` 같은 훼손 스팬의 마지막 물음표가
# "단어문자 뒤 + 백틱 앞"이라는 이유로 정상 종결 물음표로 오인되는 것을 막는다(실측 false negative 1건).
QM_NEXT_OK = set(" \n\r\t)\"'")


def load_freeze() -> list[dict[str, str]]:
    with FREEZE_PATH.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256_of(path: Path) -> tuple[str, int]:
    payload = path.read_bytes()
    return hashlib.sha256(payload).hexdigest(), len(payload)


def scan_questionmarks(text: str) -> list[tuple[int, str]]:
    """물음표 중 '문장 종결로 설명되지 않는' 것만 훼손 후보로 반환.

    허용 1: 백틱 스팬 내용이 오직 ?/U+FFFD 로만 이루어진 경우(그 문자 자체를 인용).
    허용 2: 앞이 단어문자/닫는괄호이고 뒤가 공백·줄끝인 진짜 의문문 종결.
    """
    allowed: set[int] = set()
    for match in re.finditer(r"`([^`\n]*)`", text):
        inner = match.group(1)
        if inner and set(inner) <= {"?", "�"}:
            allowed.update(range(match.start(1), match.end(1)))

    hits: list[tuple[int, str]] = []
    lines_start = [0]
    for index, char in enumerate(text):
        if char == "\n":
            lines_start.append(index + 1)

    def line_of(pos: int) -> int:
        low, high = 0, len(lines_start) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if lines_start[mid] <= pos:
                low = mid
            else:
                high = mid - 1
        return low + 1

    for index, char in enumerate(text):
        if char not in ("?",) and char not in MOJIBAKE_MARKS:
            continue
        if char == "?" and index in allowed:
            continue
        if char == "?":
            prev = text[index - 1] if index else "\n"
            nxt = text[index + 1] if index + 1 < len(text) else "\n"
            if prev in QM_PREV_OK and nxt in QM_NEXT_OK:
                continue
        start = max(0, index - 28)
        end = min(len(text), index + 28)
        hits.append((line_of(index), text[start:end].replace("\n", " ")))
    return hits


def check_freeze(failures: list[str], warnings: list[str]) -> None:
    rows = load_freeze()
    ok = 0
    for row in rows:
        path = REPO / row["path"]
        if not path.exists():
            failures.append(f"freeze missing file: {row['path']}")
            continue
        digest, size = sha256_of(path)
        if size != int(row["bytes"]) or digest != row["sha256"]:
            failures.append(
                f"RULER DRIFT ({row['role']}): {row['path']} "
                f"frozen={row['sha256'][:12]}/{row['bytes']}B "
                f"now={digest[:12]}/{size}B"
            )
        else:
            ok += 1
    print(f"freeze_ok={ok}/{len(rows)}")


def check_integrity(failures: list[str], warnings: list[str]) -> None:
    """1차 게이트가 면제한 영역까지 문자 무결성을 확장 적용한다."""
    targets = sorted(
        path
        for path in TEAM_DIR.rglob("*")
        if path.is_file() and path.suffix in {".md", ".tsv", ".py"}
    )
    total = 0
    for path in targets:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        hits = scan_questionmarks(text)
        if not hits:
            continue
        total += len(hits)
        rel = path.relative_to(REPO).as_posix()
        owner = "gatekeeper" if path.parent == TEAM_DIR else path.parent.name
        detail = "; ".join(f"L{line}:{ctx.strip()}" for line, ctx in hits[:3])
        failures.append(f"content-integrity ({owner}) {rel}: {len(hits)} hit(s) -> {detail}")
    print(f"integrity_files_scanned={len(targets)} integrity_hits={total}")


def check_signal(failures: list[str], warnings: list[str]) -> None:
    """1차 게이트가 상수 리터럴을 지표처럼 출력하는지 정적 검사(F1)."""
    if not GATE_SRC.exists():
        failures.append(f"gate source missing: {GATE_SRC}")
        return
    source = GATE_SRC.read_text(encoding="utf-8-sig")
    vacuous = []
    for index, line in enumerate(source.splitlines(), start=1):
        for match in re.finditer(r'print\(\s*f?"([a-z_]+)=(\d+)"\s*\)', line):
            vacuous.append((index, match.group(1), match.group(2)))
    for line_no, metric, value in vacuous:
        failures.append(
            f"vacuous-signal check_experiment.py:{line_no}: "
            f"'{metric}={value}' is a constant literal, not a computed count"
        )
    print(f"vacuous_signal_count={len(vacuous)}")


def check_coverage(failures: list[str], warnings: list[str]) -> None:
    """1차 게이트의 보고서 검사에 무결성 검사가 실제로 걸려 있는지(F3)."""
    if not GATE_SRC.exists():
        failures.append(f"gate source missing: {GATE_SRC}")
        return
    source = GATE_SRC.read_text(encoding="utf-8-sig")
    match = re.search(r"def require_report\(.*?\n(?=\ndef |\nif __name__)", source, re.S)
    body = match.group(0) if match else ""
    if not body:
        failures.append("coverage: require_report() not found in gate source")
        return
    has_integrity = ("\\ufffd" in body) or ("ufffd" in body) or ("corrupt" in body)
    if not has_integrity:
        failures.append(
            "coverage: require_report() applies marker-presence only; "
            "no content-integrity check -> TEAM_PREFLIGHT_260828.md:34 capability claim "
            "is broader than the code"
        )
    # 게이트가 자기 소유 파일(자)을 스캔 대상에 넣는지
    scans_own = "ACCEPTANCE_SCHEMA" in source or "TEAM_PREFLIGHT" in source
    if not scans_own:
        failures.append(
            "coverage: gate never reads its own ruler files "
            "(ACCEPTANCE_SCHEMA / TEAM_PREFLIGHT); measurer is exempt from measurement"
        )
    print(f"coverage_checks=2 coverage_failures={len([f for f in failures if f.startswith('coverage:')])}")


def check_staleness(failures: list[str], warnings: list[str]) -> None:
    """판정 문서가 인용한 author 해시가 현재본과 일치하는지(F5)."""
    current = {}
    for rel in AUTHOR_ARTIFACTS:
        path = TEAM_DIR / rel
        if path.exists():
            current[rel] = sha256_of(path)[0]
    for rel in VERDICT_DOCS:
        path = TEAM_DIR / rel
        if not path.exists():
            failures.append(f"staleness: verdict doc missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        cited = set(match.group(0).lower() for match in re.finditer(r"\b[0-9a-fA-F]{8,64}\b", text))
        if not cited:
            failures.append(f"staleness: {rel} cites no artifact hash at all")
            continue
        matched = [
            rel_a
            for rel_a, digest in current.items()
            if any(digest.startswith(token) or token.startswith(digest[:8]) for token in cited)
        ]
        if len(matched) < len(current):
            missing = sorted(set(current) - set(matched))
            failures.append(
                f"STALE VERDICT: {rel} does not cite the current hash of {','.join(missing)} "
                f"(current: {', '.join(f'{k}={v[:8]}' for k, v in current.items() if k in missing)}) "
                f"and carries no supersession marker check"
            )
    print(f"staleness_author_artifacts={len(current)} staleness_verdict_docs={len(VERDICT_DOCS)}")


CHECKS = {
    "freeze": check_freeze,
    "integrity": check_integrity,
    "signal": check_signal,
    "coverage": check_coverage,
    "staleness": check_staleness,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", choices=("all", *CHECKS), default="all")
    args = parser.parse_args()

    failures: list[str] = []
    warnings: list[str] = []
    selected = list(CHECKS) if args.check == "all" else [args.check]
    for name in selected:
        print(f"--- {name} ---")
        CHECKS[name](failures, warnings)

    print(f"checks_run={len(selected)}")
    print(f"warnings={len(warnings)}")
    print(f"failures={len(failures)}")
    for item in warnings:
        print(f"WARN: {item}")
    for item in failures:
        print(f"FAIL: {item}")
    if failures or warnings:
        print("meta-gate: FAIL")
        return 1
    print(f"meta-gate: PASS check={args.check}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
