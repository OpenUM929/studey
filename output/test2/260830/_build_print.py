#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output/test2/260830 프린트 패키지 생성기 (260830)

원본 4개 세트(.md)를 A4 인쇄용 HTML로 변환한다.

A4 배치 규칙 (사용자 요구, 260830):
  1. 한 문항은 두 페이지에 걸쳐 쪼개지지 않는다.
  2. 어떤 문항의 시작 위치가 본문 영역의 80% 지점보다 아래가 되면
     그 문항은 다음 페이지로 넘긴다.
  두 규칙은 브라우저 로드 시 JS가 실제 렌더 높이를 측정해 페이지를 확정한다
  (CSS만으로는 "80% 아래면 넘김"을 표현할 수 없다).

재실행: python output/test2/260830/_build_print.py
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent

SETS = [
    dict(slug="40제_도형의방정식_모의40",
         src="output/260822/공통수학2_도형의방정식_모의40.md",
         set_id="SET-260822-math2-40",
         title="공통수학2 「도형의 방정식」 예상 문제 40제",
         sub="2026 상산고 1학년 2학기 · 전 40문항 서답형(단답 32 · 서술 8)"),
    dict(slug="25제_종합평가",
         src="output/260829/260829_02_math2_comprehensive_25.md",
         set_id="SET-260829-math2-25",
         title="공통수학2 「도형의 방정식」 종합평가 25제",
         sub="2026 상산고 1학년 2학기 · 25문항 100점 50분 · 전 문항 서답형"),
    dict(slug="32제_난이도별신형",
         src="output/260830/260830_01_math2_graded_new_forms_32.md",
         set_id="SET-260830-math2-32",
         title="공통수학2 「도형의 방정식」 난이도별 신형 32제",
         sub="2026 상산고 1학년 2학기 · A~D단계 32문항 125점"),
    dict(slug="32u제_미사용변형축",
         src="output/260830/260830_02_math2_unused_axes_32.md",
         set_id="SET-260830-math2-32u",
         title="공통수학2 「도형의 방정식」 미사용 변형축 32제",
         sub="2026 상산고 1학년 2학기 · A~D단계 32문항 121점"),
]

ANSWER_HEAD = re.compile(r"^#\s*정답\s*·\s*해설", re.M)
ITEM_SPLIT = re.compile(r"^\*\*([A-D]?\d+)\.\*\*\s*", re.M)
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
TAGLINE = re.compile(r"^`?\[(?:SM2-\d\d|[A-Z])")
ROW = re.compile(r"^\|\s*([A-D]?\d+)\s*(⚠️)?\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def inline(s):
    """마크다운 인라인 → HTML. 이스케이프 뒤에 적용한다."""
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # *l* 처럼 뒤에 한글 조사가 바로 붙는 경우가 많으므로 뒤쪽 경계는 `*` 만 배제한다.
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = s.replace(r"\|", "|")
    # 직선 이름으로 쓰이는 홑글자 l 을 변수 표기(이탤릭)로 세운다.
    # 이 문서군에는 영어 단어가 없어 오검출 위험이 없다.
    s = re.sub(r"(?<![A-Za-z<>/])l(?![A-Za-z>])", "<em>l</em>", s)
    return s


def body_to_html(lines, drop_meta=True):
    """문항 본문 줄 목록 → HTML 문단."""
    out, buf = [], []

    def flush():
        if buf:
            out.append("<p>" + "<br>".join(inline(x) for x in buf) + "</p>")
            buf.clear()

    for ln in lines:
        t = ln.rstrip()
        if not t.strip() or t.strip() == "---":
            flush()
            continue
        if drop_meta and (t.startswith(">") or TAGLINE.match(t.strip())):
            continue
        if drop_meta and t.lstrip().startswith("⚠️ **"):
            continue
        buf.append(t)
    flush()
    return "\n".join(out)


def parse(md_path):
    raw = md_path.read_text(encoding="utf-8")
    raw = re.sub(r"^---\n.*?\n---\n", "", raw, count=1, flags=re.S)  # frontmatter
    m = ANSWER_HEAD.search(raw)
    problems_src, answers_src = (raw[:m.start()], raw[m.start():]) if m else (raw, "")

    # ---- 문제부: 섹션 헤딩 + 문항 ----
    blocks = []           # [("section", text) | ("item", no, html)]
    parts = ITEM_SPLIT.split(problems_src)
    # parts[0] = 첫 문항 이전(제목·머리말·첫 섹션 헤딩)
    lead = parts[0]
    for ln in lead.split("\n"):   # HEADING은 줄 단위 패턴이다(finditer에 re.M이 없음)
        hm = HEADING.match(ln)
        if not hm:
            continue
        lvl, txt = hm.group(1), hm.group(2).strip()
        if len(lvl) >= 2 or txt.startswith(("A단계", "B단계", "C단계", "D단계")):
            blocks.append(("section", txt))
    for i in range(1, len(parts), 2):
        no, chunk = parts[i], parts[i + 1]
        lines = chunk.split("\n")
        # 문항 본문은 첫 헤딩 전까지. 헤딩 이후는 다음 절의 표제와 그 머리말인데,
        # 머리말(근거 유형·Tier 분포 등)은 교사용 메타라 학생 문제지에서 뺀다.
        keep, tail_heads = [], []
        seen_heading = False
        for ln in lines:
            hm = HEADING.match(ln)
            if hm:
                seen_heading = True
                txt = hm.group(2).strip()
                if txt:
                    tail_heads.append(txt)
                continue
            if not seen_heading:
                keep.append(ln)
        blocks.append(("item", no, body_to_html(keep)))
        for t in tail_heads:
            blocks.append(("section", t))

    # ---- 해설부: 표 행 + 채점 기준 ----
    ans, rubric = [], []
    cur_rub = None
    in_rubric = False          # "채점 기준" 절 안에 들어왔는가
    for ln in answers_src.split("\n"):
        rm = ROW.match(ln)
        if rm and rm.group(1) and not ln.startswith("| 문항") and "---" not in ln:
            ans.append(dict(no=rm.group(1), warn=bool(rm.group(2)),
                            answer=rm.group(3), typ=rm.group(4), sol=rm.group(5)))
            continue
        hm = HEADING.match(ln)
        if hm:
            lvl, txt = len(hm.group(1)), hm.group(2).strip()
            if "채점" in txt and "기준" in txt:
                # 절 표제(예: "# 서술형 채점 기준")인지 개별 문항 기준인지 구분한다.
                if re.match(r"^[A-D]?\d+", txt):
                    cur_rub = dict(title=txt, lines=[]); rubric.append(cur_rub)
                else:
                    in_rubric, cur_rub = True, None
                continue
            if in_rubric and re.match(r"^[A-D]?\d+", txt):
                # 채점 기준 절 안의 "### 21번 [6점]" 형식
                cur_rub = dict(title=txt, lines=[]); rubric.append(cur_rub)
                continue
            in_rubric, cur_rub = False, None
            continue
        if cur_rub is not None and ln.strip():
            cur_rub["lines"].append(ln.rstrip())
    return blocks, ans, rubric


CSS = """
:root{--ink:#111;--mute:#555;--rule:#bbb;--accent:#1a4a7a}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:"Malgun Gothic","맑은 고딕","Apple SD Gothic Neo",sans-serif;
  color:var(--ink);background:#8a8a8a;font-size:10.5pt;line-height:1.62;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:210mm;height:297mm;padding:16mm 15mm 14mm;
  background:#fff;margin:8mm auto;box-shadow:0 2px 14px rgba(0,0,0,.35);overflow:hidden}
.page-inner{position:relative;height:100%;overflow:hidden}
.masthead{border-bottom:2px solid var(--accent);padding-bottom:3mm;margin-bottom:5mm}
.masthead h1{font-size:15pt;margin:0 0 1.5mm;letter-spacing:-.3px}
.masthead .sub{font-size:9pt;color:var(--mute)}
.namebar{margin-top:3mm;font-size:9.5pt;color:var(--mute);display:flex;gap:10mm}
.namebar span{border-bottom:1px solid var(--rule);padding:0 0 1mm;min-width:38mm}
.notice{font-size:8.6pt;color:var(--mute);border:1px solid var(--rule);
  border-left:3px solid var(--accent);padding:2.5mm 3mm;margin:0 0 5mm;line-height:1.5}
.section{font-size:11.5pt;font-weight:700;color:var(--accent);
  border-bottom:1px solid var(--rule);padding-bottom:1.5mm;margin:0 0 4mm}
/* 직선 이름 l 은 고딕에서 대문자 I·숫자 1과 구별되지 않는다(260830 육안 검수).
   변수는 수학 관행대로 세리프 이탤릭으로 세운다. */
em{font-family:"Times New Roman",Cambria,serif;font-style:italic;font-size:1.06em}
.item{margin:0 0 6.5mm;padding-left:9mm;position:relative;font-size:11pt}
.item .no{position:absolute;left:0;top:0;font-weight:700;color:var(--accent);min-width:9mm}
.item p{margin:0 0 1.6mm}
.item p:last-child{margin-bottom:0}
.ans{margin:0 0 4.5mm;padding-left:9mm;position:relative;font-size:9.6pt}
.ans .no{position:absolute;left:0;top:0;font-weight:700;color:var(--accent)}
.ans .val{font-weight:700}
.ans .typ{font-size:8.4pt;color:var(--mute);margin-left:2mm}
.ans .sol{color:#333;margin-top:1mm;line-height:1.55}
.rub{margin:0 0 5mm;font-size:9.4pt}
.rub h3{font-size:10pt;margin:0 0 1.5mm;color:var(--accent)}
.rub div{margin:0 0 .8mm}
code{font-family:Consolas,"D2Coding",monospace;font-size:.92em;background:#f2f2f2;padding:0 2px}
.pfoot{position:absolute;left:15mm;right:15mm;bottom:7mm;display:flex;
  justify-content:space-between;font-size:8pt;color:#888;
  border-top:1px solid #e2e2e2;padding-top:1.5mm}
@media print{
  body{background:#fff}
  .page{margin:0;box-shadow:none;break-after:page;page-break-after:always}
  .page:last-child{break-after:auto;page-break-after:auto}
  .noprint{display:none!important}
}
@page{size:A4 portrait;margin:0}
.noprint{position:fixed;top:8px;left:50%;transform:translateX(-50%);z-index:99;
  background:#fff;border:1px solid #bbb;border-radius:4px;padding:6px 12px;
  font-size:12px;box-shadow:0 2px 8px rgba(0,0,0,.25)}
.noprint button{font:inherit;cursor:pointer;padding:3px 10px;margin-left:8px}
"""

JS = """
// A4 페이지 확정 — 사용자 규칙(260830):
//   (1) 한 문항은 페이지를 넘어 쪼개지지 않는다.
//   (2) 문항의 시작 위치가 본문 높이의 80%보다 아래면 다음 페이지로 넘긴다.
// CSS로는 (2)를 표현할 수 없으므로 실제 렌더 높이를 측정해 배치한다.
(function () {
  var START_LIMIT = 0.80;
  // px(브라우저 측정)와 pt(PDF 실측) 사이의 반올림 차이로 경계에서 0.3pt가량
  // 새어 나가는 것을 막는 여유. 규칙을 느슨하게 하는 방향이 아니라 조이는 방향이다.
  var GUARD_PX = 4;
  var src = document.getElementById('source');
  var sheet = document.getElementById('sheet');
  var meta = JSON.parse(document.getElementById('meta').textContent);
  var nodes = Array.prototype.slice.call(src.children);

  var page = null, inner = null, limitPx = 0, pageNo = 0;

  function newPage(withMast) {
    pageNo++;
    page = document.createElement('div');
    page.className = 'page';
    inner = document.createElement('div');
    inner.className = 'page-inner';
    page.appendChild(inner);
    var f = document.createElement('div');
    f.className = 'pfoot';
    f.innerHTML = '<span>' + meta.setId + '</span><span>' + meta.kind +
                  ' &middot; ' + pageNo + '</span>';
    page.appendChild(f);
    sheet.appendChild(page);
    limitPx = inner.clientHeight;
    if (withMast) {
      var m = document.getElementById('masthead');
      if (m) { inner.appendChild(m); }
      var n = document.getElementById('notice');
      if (n) { inner.appendChild(n); }
    }
    return inner;
  }

  // 마지막 자식의 바닥 좌표. scrollHeight는 마지막 요소의 아래 margin을
  // 브라우저에 따라 빼먹으므로 offsetTop+offsetHeight+marginBottom으로 잰다.
  function used() {
    var last = inner.lastElementChild;
    if (!last) { return 0; }
    var mb = parseFloat(getComputedStyle(last).marginBottom) || 0;
    return last.offsetTop + last.offsetHeight + mb;
  }
  function isEmpty() { return inner.children.length === 0; }

  newPage(true);
  var pendingSection = [];      // 연속된 섹션 제목을 모두 보존한다

  nodes.forEach(function (node) {
    // 섹션 제목은 단독으로 페이지 끝에 남지 않도록 다음 문항과 함께 옮긴다.
    if (node.classList.contains('section')) { pendingSection.push(node); return; }

    // 규칙 (2): 시작 위치가 본문 높이의 80%보다 아래면 다음 페이지에서 시작한다.
    // 섹션 제목이 앞에 붙으면 그만큼 시작 위치가 내려가므로, 제목을 먼저 얹은 뒤
    // "문항이 실제로 시작할 y"를 재서 판정한다(제목 높이를 빠뜨리면 규칙이 새어 나간다).
    var hadContent = !isEmpty();
    pendingSection.forEach(function (s) { inner.appendChild(s); });
    if (hadContent && used() + GUARD_PX >= limitPx * START_LIMIT) {
      pendingSection.forEach(function (s) {
        if (s.parentNode === inner) { inner.removeChild(s); }
      });
      newPage(false);
      pendingSection.forEach(function (s) { inner.appendChild(s); });
    }
    inner.appendChild(node);

    // 규칙 (1): 페이지를 넘겨 쪼개지지 않게, 안 들어가면 통째로 다음 페이지로.
    if (used() > limitPx) {
      var moved = pendingSection;
      inner.removeChild(node);
      moved.forEach(function (s) {
        if (s.parentNode === inner) { inner.removeChild(s); }
      });
      if (!isEmpty()) {                 // 빈 페이지를 새로 만들지 않는다
        newPage(false);
      }
      moved.forEach(function (s) { inner.appendChild(s); });
      inner.appendChild(node);
      // 한 문항이 빈 페이지보다 큰 경우에만 넘침을 허용한다(쪼갤 수 없으므로).
    }
    pendingSection = [];
  });

  pendingSection.forEach(function (s) { inner.appendChild(s); });
  src.remove();
  document.getElementById('pagecount').textContent = pageNo;
})();
"""


def page_html(title, meta, masthead, notice, blocks_html, kind):
    import json
    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<title>{esc(title)}</title>
<style>{CSS}</style></head><body>
<div class="noprint">A4 {esc(kind)} · 총 <b id="pagecount">-</b>쪽
<button onclick="window.print()">인쇄</button></div>
<script type="application/json" id="meta">{json.dumps(meta, ensure_ascii=False)}</script>
<div id="sheet"></div>
<div id="source" style="position:absolute;left:-9999px;top:0;width:180mm">
{blocks_html}
</div>
<div style="position:absolute;left:-9999px">
  <div id="masthead" class="masthead">{masthead}</div>
  {notice}
</div>
<script>{JS}</script>
</body></html>
"""


def build(cfg):
    src = ROOT / cfg["src"]
    blocks, ans, rubric = parse(src)

    mast = (f'<h1>{esc(cfg["title"])}</h1>'
            f'<div class="sub">{esc(cfg["sub"])}</div>')
    namebar = ('<div class="namebar"><span>학년 반 번호</span>'
               '<span>이름</span><span>점수</span></div>')
    notice = ('<div id="notice" class="notice">'
              '⚠️ <b>범위 미확정</b> — 2학기 시험범위는 학교 공지·진도표 미확인 상태의 추정이다. '
              '⚠️ <b>자료 등급</b> — 근거 유형 SM2-01~33은 전부 <b>검증(부교재)</b>이며 기출 확인분이 아니다. '
              '⛔ <b>미투입</b> — 맹목 풀이 게이트 재통과 전이므로 실전 투입 전 교사 검수가 필요하다.'
              '</div>')

    # 문제지
    ph = []
    for b in blocks:
        if b[0] == "section":
            ph.append(f'<div class="section">{inline(b[1])}</div>')
        else:
            ph.append(f'<div class="item"><span class="no">{b[1]}.</span>{b[2]}</div>')
    p = OUT / f'{cfg["slug"]}_문제.html'
    p.write_text(page_html(cfg["title"] + " — 문제", {"setId": cfg["set_id"], "kind": "문제"},
                           mast + namebar, notice, "\n".join(ph), "문제지"), encoding="utf-8")

    # 해설지
    ah = []
    for a in ans:
        warn = " ⚠️" if a["warn"] else ""
        ah.append('<div class="ans"><span class="no">{no}.</span>'
                  '<span class="val">{val}</span>{w}<span class="typ">{typ}</span>'
                  '<div class="sol">{sol}</div></div>'.format(
                      no=a["no"], val=inline(a["answer"]), w=warn,
                      typ=inline(a["typ"]), sol=inline(a["sol"])))
    for r in rubric:
        rows = "".join(f"<div>{inline(x)}</div>" for x in r["lines"])
        ah.append(f'<div class="rub"><h3>{inline(r["title"])}</h3>{rows}</div>')
    q = OUT / f'{cfg["slug"]}_해설.html'
    q.write_text(page_html(cfg["title"] + " — 정답·해설", {"setId": cfg["set_id"], "kind": "해설"},
                           mast + '<div class="sub" style="margin-top:2mm">정답 · 해설 · 근거 유형 ID'
                           ' — <b>교사용</b></div>', notice,
                           "\n".join(ah), "해설지"), encoding="utf-8")

    shutil.copy2(src, OUT / f'{cfg["slug"]}_원본.md')
    return len(blocks), len(ans), len(rubric), p.name, q.name


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for cfg in SETS:
        nb, na, nr, pf, qf = build(cfg)
        items = sum(1 for b in parse(ROOT / cfg["src"])[0] if b[0] == "item")
        print(f'{cfg["slug"]:<24} 문항 {items:>2} · 해설행 {na:>2} · 채점기준 {nr} → {pf} / {qf}')
