#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""origin_data 의 .hwp 원안 1건을 corpus/<ID>/ 정제 유닛으로 변환한다 (1차 정제 = 전사만).

WHY THIS EXISTS (260902)
------------------------
F4(1학기 원본 24건)의 정제가 「소유자 판정 대기」로 미뤄져 있었다. 24회를 손으로 반복하면
반드시 어긋난다 — CLAUDE.md 원칙 12-b(자는 손이 아니라 코드가 만든다)를 정제 단계에도 적용해
기계화한다. 같은 입력에서 같은 산출물이 나오고, 수율 격차는 사람의 기억이 아니라 게이트가 센다.

**이 도구는 분류를 하지 않는다.** CLAUDE.md 원칙 1의 용어 정의대로 1차 정제(REFINE)는 전사이며,
유형ID·변형축·함정·Tier 는 한 글자도 쓰지 않는다. 그 판단은 `type-proposer` 의 몫이다.

수율 게이트 (`.claude/agents/type-extractor.md` 의 .hwp 축 — 페이지 중앙값 규칙은 .hwp 에
적용되지 않는다):
  (i)  문항 수율 — 표지가 **스스로 선언한** 문항 수와 실측을 대조한다.
  (ii) 이미지 수율 — 본문 이미지 참조 수와 추출된 bindata 파일 수를 대조한다.
격차는 **추측으로 채우지 않는다**. verify_log 에 `unreadable` 행으로 남기고 exit 3 을 반환한다
(원칙 11: 게이트는 fail-closed, 통과를 exit code 하나로 정의하지 않으므로 호출자는 요약행도 읽는다).

사용:
    python tools/build_corpus_unit.py <src.hwp> <CORPUS_ID> --exam-code 2024-1M [--force]
"""
import argparse
import hashlib
import io
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 표지 선언 줄. 260902 실측: 37유닛에서 `◑ 총( N )쪽, 선택형( N )문항, <서답형|서술형|단답형>( N )문항`
# 계열이 지배적이고, 수학처럼 선택형이 아예 없는 시험지는 `◑ 총( N )쪽, 단답형( N )문항` 으로 적는다
# (실측 3건). 괄호·공백 유무는 시험지마다 다르므로 둘 다 허용한다.
RE_DECL_LINE = re.compile(r"◑[^\n]{0,20}총[^\n]{0,80}쪽[^\n]{0,80}")
RE_PAGES = re.compile(r"총\s*\(?\s*(\d+)\s*\)?\s*쪽")
RE_CHOICE = re.compile(r"선택형\s*\(?\s*(\d+)\s*\)?\s*문항")
RE_ESSAY = re.compile(r"(?:서답형|서술형|단답형)\s*\(?\s*(\d+)\s*\)?\s*문항")
# 배점 표기는 대괄호와 소괄호 두 계열이 공존한다 — 260902 실측: `[3.0 점 ]`(수학·사회 계열) 과
# `(2.8점)`(국어·과학 계열). 종전 판본은 대괄호만 봐서 국어 20241M·20251M·20251F 와 과학
# 20241F 를 「배점 전량 소실」로 **오진**했다. 오타 `(2,8점)` 도 실재하므로 소수점은 `.` `,` 둘 다 받는다.
# 배점은 **괄호 묶음 하나가 문항 하나**다. 낱개 "점"을 세면 묶음 표기에서 어긋난다 —
# 실측: 영어 20241M 의 서답형은 `[(A)2 점,( B)3 점, 총 5점 ]` 처럼 한 묶음에 "점"이 셋이고,
# 줄바꿈까지 걸쳐 있어 낱개 계수는 32문항을 30으로 셌다. 그래서 묶음 단위로 세고 DOTALL 을 쓴다.
# 대괄호(`[3.0 점 ]`)와 소괄호(`(2.8점)`) 두 계열이 공존하므로 대괄호를 먼저 걷어낸 뒤 소괄호를
# 세어 **중복 계수를 막는다**(묶음 안에 소괄호가 들어 있다).
RE_SCORE_SQ = re.compile(r"\[[^\[\]]*?점[^\[\]]*?\]", re.S)
RE_SCORE_RD = re.compile(r"\([^()]*?\d[^()]*?점[^()]*?\)", re.S)


def count_scores(text):
    """배점 묶음 수. 대괄호 묶음을 먼저 세고 지운 뒤 소괄호 묶음을 센다."""
    sq = RE_SCORE_SQ.findall(text)
    rest = RE_SCORE_SQ.sub(" ", text)
    return len(sq) + len(RE_SCORE_RD.findall(rest))
# 문두. 260902 실측 24형태: `[ 서술형N ]` `[서술형N]` `[ 서답형N(서술) ]` `[ 단답형 N번 ]`
# `[ 서술형 N-N ]` `[서답형 N(단답) N점 각 N점]` … 괄호 안 갈래·번호·배점이 뒤에 붙는다.
# 반면 `[ 선택형 N ∼N, 서답형 N ]` · `[N, 서답형N ]` 은 **지문 공유 범위 머리말**이지 문두가 아니므로
# 대괄호 내용이 갈래 이름으로 **시작**할 것을 요구해 배제한다.
RE_STEM = re.compile(r"\[\s*(?:서술형|서답형|단답형)\s*(\d+)[^\]\[]*\]")
RE_IMG = re.compile(r"\[\[([^\]\[]+)\]\]")
# 수학 시험지는 문두(`[ 단답형n ]`)를 쓰지 않고 문항을 `1.` `2.` 로만 번호 매긴다(실측 4유닛).
RE_NUMBERED = re.compile(r"^\s*(\d{1,2})\s*\.\s", re.M)
RE_ID = re.compile(r"^(?:EX|SUP|NY)-[a-z0-9_]+-\d{5}[MF]$")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def extract(src, txt_out, bindata_dir):
    """hwp2md.py 로 변환 텍스트와 bindata 를 얻는다. 실패는 즉시 예외."""
    cmd = [sys.executable, str(ROOT / "tools/hwp2md.py"), str(src), str(txt_out),
           "--bindata", str(bindata_dir)]
    proc = subprocess.run(cmd, capture_output=True, cwd=str(ROOT))
    tail = (proc.stdout or b"").decode("utf-8", "replace").strip().splitlines()
    if proc.returncode != 0:
        sys.stderr.write((proc.stderr or b"").decode("utf-8", "replace"))
        raise SystemExit("[FAIL] hwp2md 실패 (exit %d): %s" % (proc.returncode, src))
    last = tail[-1] if tail else ""
    m = re.search(r"bindata=(\d+)\s+imgrefs=(\d+)", last)
    if not m:
        raise SystemExit("[FAIL] hwp2md 요약행을 읽지 못했다: %r" % last)
    return int(m.group(1)), int(m.group(2))


def measure(text):
    """표지 선언과 본문 실측을 각각 잰다. 없는 값은 지어내지 않고 None 으로 둔다.

    **비교 가능한 양만 비교한다** (260902 정정). 종전 판본은 「첫 문두 앞의 배점 표식 수」를
    선택형 실측으로 삼았는데, 국어처럼 지문을 선택형과 서술형이 **공유**하는 시험지에서는
    서술형 문두가 선택형 한가운데 나타나 분리점이 무너진다. 실측 결과 이 착오 하나로 18유닛 중
    8유닛이 「+4~+11 초과」라는 거짓 격차를 냈다. 선택형 문항 수를 본문에서 직접 세는 관측량은
    이 전사본에 존재하지 않으므로, 선택형은 **선언값을 사실로 삼고** 배점 표식 수는 참고값으로만
    적는다. 서답형은 문두가 문항마다 하나씩 있어 실제로 셀 수 있으므로 그것만 대조한다.
    """
    m = RE_DECL_LINE.search(text[:6000])
    line = m.group(0) if m else ""
    dec = {
        "line": line or None,
        "pages": int(RE_PAGES.search(line).group(1)) if RE_PAGES.search(line) else None,
        "choice": int(RE_CHOICE.search(line).group(1)) if RE_CHOICE.search(line) else None,
        # 한 줄에 갈래가 둘 올 수 있다 — `단답형( 18 )문항, 서술형( 4 )문항`(실측 수학 2유닛).
        # 첫 매치만 읽으면 4문항이 통째로 사라져 게이트가 거짓 격차를 낸다.
        "essay": (sum(int(v) for v in RE_ESSAY.findall(line))
                  if RE_ESSAY.search(line) else None),
    }
    stems = list(RE_STEM.finditer(text))
    obs = {
        "scores": count_scores(text),
        "essay_stems": len(set(m.group(1) for m in stems)),
        "numbered": len(set(RE_NUMBERED.findall(text))),
    }
    refs = RE_IMG.findall(text)
    return dec, obs, refs


def render_transcript(cid, src, dec, obs, refs, bindata_names, text):
    fence = "```"
    while fence in text:
        fence += "`"
    lines = []
    a = lines.append
    a("# transcript — %s" % cid)
    a("")
    a("- 원본: `%s`" % src.as_posix())
    a("- 전사 기준: `tools/hwp2md.py` 변환 텍스트(hwp5html 경유 — 표 내용과 이미지 마커 보존).")
    a("- 전사 방식: 변환 텍스트를 축자 보존하고, 문항수·배점표식·이미지 참조를 **원문 선언과 대조**한다.")
    a("  **이미지 내용·정답·유형 판단은 하지 않는다** (CLAUDE.md 원칙 1 — 1차 정제 = 전사).")
    a("- 생성: `tools/build_corpus_unit.py` (결정론적 재현 가능, 원칙 12-b).")
    a("- 개행: 변환 텍스트의 CRLF 를 **LF 로 정규화**했다(내용 무변경 — 혼합 개행 파일이 되면"
      " 앵커 편집 한 번이 전면 재작성이 된다). 기존 코퍼스 유닛도 LF 단일이다.")
    a("")
    a("## 0. 사실 header")
    a("")
    dec_txt = []
    dec_txt.append("총 %s쪽" % dec["pages"] if dec["pages"] is not None else "총 쪽수 ⚠️미확인")
    dec_txt.append("선택형 %s문항" % dec["choice"] if dec["choice"] is not None
                   else "선택형 문항수 ⚠️미확인")
    dec_txt.append("서답형 %s문항" % dec["essay"] if dec["essay"] is not None
                   else "서답형 문항수 ⚠️미확인")
    a("- 인쇄 선언: %s." % ", ".join(dec_txt))
    if dec["line"]:
        a("  - 선언 원문: `%s`" % dec["line"].strip())
    a("- 실측 배점 표식: **%d건** (`[3.0 점 ]`·`(2.8점)` 두 계열 모두 계수. 서답형 소문항 배점이"
      " 섞이므로 문항 수 이상일 수 있고, **미만이면 격차**로 잡는다)." % obs["scores"])
    a("- 본문 번호 문항(`n.` 행머리): **%d건**." % obs["numbered"])
    a("- 실측 서답형 문두(`[ 서술형n ]`·`[ 서답형n(단답) ]` 등 실측 24형태): **%d건**."
      % obs["essay_stems"])
    a("- 이미지 참조: %d회 / 고유 %d건 / bindata 파일 %d건."
      % (len(refs), len(set(refs)), len(bindata_names)))
    gaps = gap_list(dec, obs, refs, bindata_names)
    if gaps:
        a("")
        a("> ⚠️ **수율 격차 — 추측으로 채우지 않았다.** 아래 항목은 `verify_log.tsv` 의")
        a("> `unreadable` 행에 같은 문면으로 남아 있다. 해소는 원본 재판독이 필요하다.")
        for g in gaps:
            a("> - %s" % g)
    a("")
    a("## 1. 이미지 참조 대조")
    a("")
    if refs:
        for name in sorted(set(refs)):
            present = "" if name in bindata_names else "  ⚠️ **bindata 파일 없음**"
            a("- `[[%s]]` → `corpus/_images/%s/bindata/%s`%s" % (name, cid, name, present))
        orphan = sorted(n for n in bindata_names if n not in set(refs))
        if orphan:
            a("")
            a("- 본문 참조가 없는 bindata 파일 %d건: %s"
              % (len(orphan), ", ".join("`%s`" % n for n in orphan)))
    else:
        a("- 본문 이미지 참조 **0건**.")
    a("")
    a("## 2. 원문 전사 (변환 텍스트 보존)")
    a("")
    a(fence + "text")
    a(text.rstrip("\n"))
    a(fence)
    a("")
    return "\n".join(lines)


def gap_list(dec, obs, refs, bindata_names):
    """추측으로 채울 수 없는 자리만 격차로 센다.

    선언에 `선택형` 이 없는 것은 결함이 아니다 — 수학 시험지는 서답형 100%(CLAUDE.md 페르소나 절)
    라서 표지가 `총( N )쪽, 단답형( N )문항` 으로만 선언한다(실측 3건). 없는 것을 못 읽었다고
    적으면 게이트가 정상 상태를 결함으로 보고한다.
    """
    gaps = []
    if dec["line"] is None:
        gaps.append("표지 선언 줄(`◑ 총 …쪽…`)을 찾지 못했다 — 쪽수·문항수를 지어내지 않는다.")
        return gaps
    if dec["pages"] is None:
        gaps.append("표지 선언 줄은 찾았으나 쪽수를 읽지 못했다: `%s`" % dec["line"].strip())
    # 문두는 그것을 쓰는 시험지에서만 관측량이다. 수학처럼 `1.` 번호만 쓰는 시험지는
    # stems=0 이 정상이므로 격차로 세지 않는다 — 없는 표기를 못 찾았다고 적으면 거짓 격차다.
    # 문두는 그것을 쓰는 갈래에서만 관측량이다. 수학 시험지는 `단답형 18 + 서술형 4` 를 선언하고
    # 서술형 4건만 문두를 쓰며 단답형 18건은 `1.` 번호만 매긴다(실측 2유닛). 따라서 문두가 선언
    # 합계보다 **적은 것은 정상**이고, **많으면** 선언과 본문이 어긋난 것이라 격차다.
    if obs["essay_stems"] and dec["essay"] is not None and obs["essay_stems"] > dec["essay"]:
        gaps.append("서답형 — 표지 선언 **%d문항** vs 문두 실측 **%d건** (차 %+d). "
                    "변환에서 문두가 소실됐거나 표기가 다른 자리가 있다."
                    % (dec["essay"], obs["essay_stems"],
                       obs["essay_stems"] - dec["essay"]))
    total = (dec["choice"] or 0) + (dec["essay"] or 0)
    if total and obs["scores"] == 0:
        gaps.append("배점 표식 — 표지가 **%d문항**을 선언했는데 본문 배점 표식이 **0건**이다. "
                    "변환 과정에서 배점이 통째로 소실됐다. "
                    "Tier 판정은 이 유닛에서 배점을 근거로 삼을 수 없다." % total)
    elif total and obs["scores"] < total:
        gaps.append("배점 표식 — 표지 선언 **%d문항**보다 배점 표식이 **%d건**으로 적다(차 %+d). "
                    "배점이 인쇄되지 않았거나 변환에서 소실된 문항이 있다."
                    % (total, obs["scores"], obs["scores"] - total))
    missing = sorted(set(refs) - set(bindata_names))
    if missing:
        gaps.append("이미지 — 본문이 참조하는데 bindata 에 없는 파일 %d건: %s"
                    % (len(missing), ", ".join(missing)))
    return gaps


def write_unit(cid, src, exam_code, dec, obs, refs, bindata_names, text, today):
    unit = ROOT / "corpus" / cid
    unit.mkdir(parents=True, exist_ok=True)
    tr = render_transcript(cid, src, dec, obs, refs, bindata_names, text)
    (unit / "transcript.md").write_bytes(tr.encode("utf-8"))

    # 문항 수는 표지 선언이 정본이다. 선언이 없는 자리만 실측으로 메우고, 선택형은 본문에서
    # 셀 수 있는 관측량이 아니므로 선언이 없으면 0으로 둔다(수학 시험지의 정상 상태).
    items = (dec["choice"] or 0) + (dec["essay"] if dec["essay"] is not None else obs["essay_stems"])
    meta = [
        "id: %s" % cid,
        'title: "%s"' % src.name,
        "grade: 1",
        'exam_code: "%s"' % exam_code,
        "variant: master",
        "pages: %s" % (dec["pages"] if dec["pages"] is not None else "null"),
        "items: %d" % items,
        "render_dpi: null",
        'render_tool: "hwp2md.py"',
        "transcribed_at: %s" % today,
        'method: "hwp2md.py(hwp5html) 변환 텍스트 축자 보존 + build_corpus_unit.py 수율 대조"',
        "confidence: %s" % ("medium" if gap_list(dec, obs, refs, bindata_names) else "high"),
        "answer_key: null",
        "catalog_ref: null",
        "",
    ]
    (unit / "meta.yml").write_bytes("\n".join(meta).encode("utf-8"))

    header = "date\tstep\ttarget\tdecision\tevidence\treason\tconfidence\tactor"
    rows = [header]
    ev = "%s → corpus/%s/transcript.md" % (src.as_posix(), cid)
    rows.append("\t".join([
        today, "transcribe",
        "전체 문항(선언 선택형 %s·서답형 %s)" % (dec["choice"], dec["essay"]),
        "transcribed", ev,
        "hwp2md.py(hwp5html)로 변환한 텍스트를 축자 보존해 전사했다. 배점 표식 실측 %d건(참고값), "
        "서답형 문두 %d건, 이미지 참조 %d회/고유 %d건. 유형·정답 판단은 추가하지 않았다."
        % (obs["scores"], obs["essay_stems"], len(refs), len(set(refs))),
        "high", "main-loop"]))
    rows.append("\t".join([
        today, "transcribe", "이미지 %d회/%d건" % (len(refs), len(set(refs))),
        "transcribed",
        "corpus/_images/%s/bindata (%d파일)" % (cid, len(bindata_names)),
        "본문 마커와 추출 파일을 대조했다. 이미지 내용 판단은 하지 않는다.",
        "high" if not (set(refs) - set(bindata_names)) else "medium", "main-loop"]))
    for g in gap_list(dec, obs, refs, bindata_names):
        plain = g.replace("**", "").replace("\t", " ")
        rows.append("\t".join([
            today, "transcribe", "수율 격차", "unreadable", ev,
            plain + " 추측으로 채우지 않고 격차를 그대로 남긴다.",
            "low", "main-loop"]))
    (unit / "verify_log.tsv").write_bytes(("\n".join(rows) + "\n").encode("utf-8"))
    return unit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=pathlib.Path)
    ap.add_argument("corpus_id")
    ap.add_argument("--exam-code", required=True)
    ap.add_argument("--today", default="2026-09-02")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if not RE_ID.match(args.corpus_id):
        raise SystemExit("[FAIL] 코퍼스ID 형식 위반: %s" % args.corpus_id)
    src = (ROOT / args.source).resolve() if not args.source.is_absolute() else args.source
    if src.suffix.lower() != ".hwp":
        raise SystemExit("[FAIL] .hwp 가 아니다: %s" % src)
    if not src.is_file():
        raise SystemExit("[FAIL] 원본이 없다: %s" % src)

    unit = ROOT / "corpus" / args.corpus_id
    if (unit / "transcript.md").exists() and not args.force:
        print("SKIP  %-26s 이미 존재 (멱등) — 덮어쓰려면 --force" % args.corpus_id)
        return 0

    images = ROOT / "corpus/_images" / args.corpus_id / "bindata"
    images.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="corpusunit-") as tmp:
        txt_out = pathlib.Path(tmp) / "converted.txt"
        n_bin, n_ref = extract(src, txt_out, images)
        # 개행은 LF 로 정규화한다. hwp2md 변환 텍스트는 CRLF 인데 이 도구가 붙이는 머리말은
        # LF 라서, 그대로 두면 **혼합 개행 파일**이 된다 — 앵커 편집 한 번이 전면 재작성이 되는
        # 상태이고 tools/textpatch.py 가 260902부터 쓰기를 거부하는 바로 그 형태다.
        # 기존 코퍼스 유닛(EX-social-20252M 등)도 LF 단일이므로 관례와도 맞는다.
        # 개행 코드는 내용이 아니므로 축자 보존 원칙에 저촉되지 않는다(§0에 명시한다).
        text = txt_out.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")

    names = sorted(p.name for p in images.iterdir() if p.is_file())
    dec, obs, refs = measure(text)
    # hwp2md 의 imgrefs 는 <img> 치환 횟수이고 여기 refs 는 본문 마커 출현 횟수라
    # 같은 양이 아니다(같은 그림을 두 번 쓰면 어긋난다 — 실측 14 vs 12). 등식을 걸지 않는다.
    # 의미 있는 대조는 **본문이 참조하는 파일이 실제로 추출됐는가** 이고 그건 gap_list 가 잰다.
    if n_bin != len(names):
        raise SystemExit("[FAIL] bindata 파일 수 불일치: 디렉터리 %d vs hwp2md %d "
                         "(같은 양이므로 어긋나면 추출이 깨진 것이다)" % (len(names), n_bin))
    try:
        rel = src.relative_to(ROOT)
    except ValueError:
        rel = src
    write_unit(args.corpus_id, rel, args.exam_code, dec, obs, refs, names, text, args.today)

    gaps = gap_list(dec, obs, refs, names)
    print("UNIT  %-26s pages=%s declared=%s+%s stems=%s scores=%d imgrefs=%d/%d bindata=%d gaps=%d"
          % (args.corpus_id, dec["pages"], dec["choice"], dec["essay"],
             obs["essay_stems"], obs["scores"], len(refs), len(set(refs)),
             len(names), len(gaps)))
    for g in gaps:
        print("      gap: %s" % g.replace("**", ""))
    return 3 if gaps else 0


# --------------------------------------------------------------------------
# 자기 검출력 증명 (CLAUDE.md 원칙 12-d)
#
# 이 게이트는 260902에 「격차 18건 → 0건」으로 **내가 손봐서** 통과시킨 것이다. 매 수정은
# 원본에서 찾은 실제 원인(소괄호 배점 표기 · 묶음 배점 · `단답형` 선언 키워드 · 수학의 번호 매김)에
# 근거했지만, **그 사실만으로는 게이트가 여전히 결함을 잡는다는 증거가 되지 않는다** — 260828 F9가
# 명명한 「눈금 손질」과 겉모습이 같기 때문이다. 그래서 알려진 결함을 심어 매 실행 검출을 확인한다.
# 게이트의 합격 판정은 `[OK]` 문자열이 아니라 `undetected=0` 이다(원칙 11).
# --------------------------------------------------------------------------
def _self_test():
    base = (
        "국어과 제 1학기 중간고사 문제지\n"
        "◑ 총( 7 )쪽, 선택형( 3 )문항, 서답형( 2 )문항\n"
        "1. 첫 문항이다. [2.5 점 ]\n"
        "2. 둘째 문항이다. (2.8점)\n"
        "3. 셋째 문항이다. [ 3.2점 ]\n"
        "[ 서술형1 ] 넷째. [(A)2 점,( B)3 점, 총 5점 ]\n"
        "[ 서답형2(단답) ] 다섯째. [4 점 ]\n"
        "[[BIN0001.jpg]]\n")
    files = ["BIN0001.jpg"]
    seeded = caught = 0

    def check(label, text, names, want):
        """want = 격차가 잡혀야 하면 True."""
        nonlocal seeded, caught
        seeded += 1
        dec, obs, refs = measure(text)
        gaps = gap_list(dec, obs, refs, names)
        got = bool(gaps)
        if got == want:
            caught += 1
        else:
            print("  FAIL %s: 기대 %s, 실제 %s %s"
                  % (label, "격차" if want else "무격차",
                     "격차" if got else "무격차", gaps[:1]))

    # 0) 무결점 원본은 통과해야 한다 (거짓 양성 방지 — 자가 너무 넓으면 이것부터 깨진다)
    check("0 정상", base, files, False)
    # 1) 배점 묶음 1개 소실 -> 선언 5문항 vs 배점 4묶음
    check("1 배점 1개 소실", base.replace(" [2.5 점 ]", ""), files, True)
    # 2) 배점 전량 소실
    check("2 배점 전량 소실",
          re.sub(r"[\[(][^\[\]()]*?점[^\[\]()]*?[\])]", "", base), files, True)
    # 3) bindata 파일 결손 (본문은 참조하는데 파일이 없다)
    check("3 이미지 결손", base, [], True)
    # 4) 표지 선언 줄 소실
    check("4 선언 줄 소실",
          "\n".join(l for l in base.split("\n") if "◑" not in l), files, True)
    # 5) 쪽수만 읽히지 않는 선언
    check("5 쪽수 불명", base.replace("총( 7 )쪽", "총(   )쪽"), files, True)
    # 6) 문두가 선언보다 많다 (선언 2 vs 문두 3)
    check("6 문두 초과", base + "[ 서술형3 ] 여섯째. [1 점 ]\n", files, True)
    # 7) 문두가 선언보다 적은 것은 **정상**이다 — 수학처럼 번호만 매기는 갈래가 섞인다
    check("7 문두 부족은 정상", base.replace("[ 서답형2(단답) ] 다섯째.", "5. 다섯째."),
          files, False)
    # 8) 묶음 배점을 낱개로 세면 놓치는 자리 — 묶음 계수가 유지되는지
    seeded += 1
    if count_scores("[(A)2 점,( B)3 점,\n총 5점 ]") == 1:
        caught += 1
    else:
        print("  FAIL 8: 묶음 배점을 %d 로 셌다 (기대 1)"
              % count_scores("[(A)2 점,( B)3 점,\n총 5점 ]"))
    # 9) 지문 공유 머리말은 문두가 아니다
    seeded += 1
    _, obs9, _ = measure(base + "[ 선택형 1 ~2, 서답형 1 ] 머리말\n")
    if obs9["essay_stems"] == 2:
        caught += 1
    else:
        print("  FAIL 9: 범위 머리말을 문두로 셌다 (%d, 기대 2)" % obs9["essay_stems"])

    print("build_corpus_unit self-test: seeded=%d undetected=%d" % (seeded, seeded - caught))
    return 0 if caught == seeded else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    sys.exit(main())
