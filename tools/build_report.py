#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_report.py — single-file HTML report from S01 ledgers (+ SHARE_LOG append).

Plan §5: external-reference-free HTML; every number is DERIVED from the ledgers —
no hand-written narrative. Appends one SHARE_LOG.tsv row per build (append-only).

Sections: summary stats · mastery table (index join) · open weaknesses · coverage.
Empty ledgers render an empty-state report (first run before any grading).
Usage:
  python build_report.py [--student-dir student/S01] [--index analysis/catalog/index.tsv]
"""
import datetime
import io
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MARK_SYM = {"correct": "O", "unsure": "△", "wrong": "X", "blank": "/"}
STATUS_SYM = {"mastered": "🟢 숙달", "unstable": "🟡 불안정", "weak": "🔴 취약",
              "unmeasured": "⬜ 미측정"}
CSS = """body{font-family:'Malgun Gothic',sans-serif;margin:2rem;color:#222}
h1{border-bottom:2px solid #4a6fa5} h2{color:#4a6fa5}
table{border-collapse:collapse;margin:.8rem 0} th,td{border:1px solid #bbb;padding:.35rem .7rem;font-size:.9rem}
th{background:#eef3fa} .num{text-align:right} .warn{background:#fff3cd;padding:.6rem;border-radius:4px}
.meta{color:#666;font-size:.85rem}"""


def read_tsv(p):
    if not p.exists():
        return [], []
    lines = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    rows = [l.split("\t") for l in lines]
    return rows[0], rows[1:]


def table(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td{' class=num' if c.replace('.','').isdigit() else ''}>{c}</td>"
                                    for c in r) + "</tr>" for r in rows)
    return f"<table><tr>{head}</tr>{body}</table>"


def main():
    argv = sys.argv[1:]
    student_dir = ROOT / "student" / "S01"
    index = ROOT / "analysis" / "catalog" / "index.tsv"
    if "--student-dir" in argv:
        v = argv[argv.index("--student-dir") + 1]
        student_dir = Path(v) if Path(v).is_absolute() else ROOT / v
    if "--index" in argv:
        v = argv[argv.index("--index") + 1]
        index = Path(v) if Path(v).is_absolute() else ROOT / v
    share_log = ROOT / "share" / "SHARE_LOG.tsv"
    if "--share-log" in argv:
        v = argv[argv.index("--share-log") + 1]
        share_log = Path(v) if Path(v).is_absolute() else ROOT / v
    share_log.parent.mkdir(parents=True, exist_ok=True)

    ahdr, arows = read_tsv(student_dir / "ATTEMPT_LOG.tsv")
    ai = {c: i for i, c in enumerate(ahdr)}
    mhdr, mrows = read_tsv(student_dir / "MASTERY.tsv")
    whdr, wrows = read_tsv(student_dir / "WEAK_LEDGER.tsv")

    n = len(arows)
    dist = {k: 0 for k in MARK_SYM}
    set_ids = set()
    for r in arows:
        dist[r[ai["mark_code"]]] += 1
        set_ids.add(r[ai["set_id"]])
    acc = (dist["correct"] / n * 100) if n else 0.0

    unmeasured = sum(1 for r in mrows if r[mhdr.index("status_code")] == "unmeasured") \
        if mhdr else 0
    weak_types = [r for r in mrows if mhdr and r[mhdr.index("status_code")] == "weak"]
    open_weak = [r for r in wrows if whdr and len(r) > 5 and r[5] != "resolved"]

    parts = [f"<h1>S01 학습 리포트</h1>",
             f"<p class=meta>generated {datetime.date.today().isoformat()} · "
             f"source: ATTEMPT_LOG/MASTERY/WEAK_LEDGER × index.tsv (all numbers derived)</p>"]
    if n == 0:
        parts.append('<p class=warn>아직 채점 기록이 없습니다(빈 원장). '
                     '웹 채점 → 「채점 원장 내보내기」 또는 손작성 TSV를 import_grading에 '
                     '넣으면 이 리포트가 채워집니다.</p>')
    else:
        parts.append(f"<h2>요약</h2><p>시도 {n}문항 ({', '.join(sorted(set_ids))}) · "
                     f"정답률 {acc:.1f}% · O {dist['correct']} / △ {dist['unsure']} / "
                     f"X {dist['wrong']} / / {dist['blank']}</p>")
    if mrows and mhdr:
        mi = {c: i for i, c in enumerate(mhdr)}
        rows = [[r[mi["type_id"]], r[mi["unit"]], r[mi["importance"]], r[mi["attempts"]],
                 r[mi["last3"]], STATUS_SYM.get(r[mi["status_code"]], r[mi["status_code"]])]
                for r in mrows]
        parts.append(f"<h2>유형별 숙련도 (미측정 {unmeasured}/{len(mrows)})</h2>" +
                     table(["유형", "단원", "중요도", "시도", "최근3", "상태"], rows))
    if weak_types:
        parts.append("<h2>약점 유형 (MASTERY=weak)</h2>" +
                     table(["유형", "단원"], [[r[0], r[1]] for r in weak_types]))
    if open_weak and whdr:
        wi = {c: i for i, c in enumerate(whdr)}
        rows = [[r[wi["wk_id"]], r[wi["axis"]], r[wi["state"]], r[wi["resolve_condition"]]]
                for r in open_weak]
        parts.append("<h2>진행 중 약점 (WEAK_LEDGER)</h2>" +
                     table(["ID", "축", "상태", "해소 조건"], rows))
    html = ("<!DOCTYPE html><html lang=ko><head><meta charset=utf-8>"
            "<title>S01 report</title><style>" + CSS + "</style></head><body>"
            + "".join(parts) + "</body></html>")

    reports_dir = student_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    ymd = datetime.date.today().strftime("%y%m%d")
    out = reports_dir / f"{ymd}_report.html"
    out.write_text(html, encoding="utf-8")
    print(f"[OK] wrote {out}")

    summary = f"시도 {n}문항·정답률 {acc:.0f}%·진행중 약점 {len(open_weak)}건"
    with io.open(share_log, "a", encoding="utf-8-sig", newline="") as f:
        f.write("\t".join([ymd, "S01", f"reports/{out.name}", summary, "-"]) + "\n")
    print(f"[OK] appended SHARE_LOG row ({share_log})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
