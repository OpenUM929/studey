#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2quiz.py — output/ 의 마크다운 문제지를 웹 뷰어용 data.js 로 변환.

표준 입력 형식은 docs/QUIZ_STANDARD.md 참고.
- 본문:  **N.** 줄기 + 지문 + ①~⑤ 보기 (객관식) / 보기 없음 (서답형)
- 말미:  # 정답 · 해설 · 유형  표 (| N | 정답 | 유형ID·Tier | 해설 |)
- 문항 번호(N)로 본문과 답안을 병합.

사용:  python tools/md2quiz.py [--out web/data.js] [--root .]
"""
import sys, os, re, json, argparse, glob
from datetime import datetime

CIRCLED = "①②③④⑤"
OPTION_RE = re.compile(r"^\s*([①②③④⑤])\s*(.*)$")
PROB_RE = re.compile(r"^\s*\*\*(\d+)\.\*\*\s*(.*)$")
TAG_RE = re.compile(r"\[([A-Za-z0-9\-]+)·?(T\d)\s*\]")
H1_RE = re.compile(r"^\s*#\s+(.*)$")
ANSWER_H_RE = re.compile(r"^\s*#\s*정답")

SUBJECT_MAP = [
    (re.compile(r"통합과학|과학"), "science"),
    (re.compile(r"영어"), "english"),
    (re.compile(r"수학"), "math"),
    (re.compile(r"국어"), "korean"),
]


def detect_subject(text):
    for pat, key in SUBJECT_MAP:
        if pat.search(text):
            return key
    return "unknown"


SPLIT_OPTION_RE = re.compile(r"\s*([①②③④⑤])\s*")
LEADING_OPTION_RE = re.compile(r"^\s*([①②③④⑤])\s*(.*)$")


def _split_line_options(ln):
    """한 줄에 ①…②…③… 가 몰려 있어도 circle-number 경계로 쪼갠다.
    단, 줄이 원숫자로 '시작'할 때만 선지로 간주하므로,
    지문 중간에 들어간 numbering(예: 'The three causes are ① heat, ② moisture.')은
    회피되어 passage 로 남는다. 반환: (option_list, 나머지_텍스트)."""
    if not LEADING_OPTION_RE.match(ln):
        return [], ln
    parts = SPLIT_OPTION_RE.split(ln)  # re.Pattern.split (capture group 포함)
    # split 결과: ['', '①', 'text', '②', 'text', ...] 형태
    opts = []
    i = 1
    while i + 1 < len(parts):
        num = parts[i]
        body = parts[i + 1].strip()
        if body:
            opts.append(num + " " + body)
        i += 2
    return opts, ""


def parse_options_and_passage(lines):
    """problem 블록 본문(줄기 제외)에서 passage 와 options 를 분리.
    한 줄에 선지가 여러 개 몰려 있어도 각각 별도 option 으로 분리한다."""
    passage_parts = []
    options = []
    in_option = False
    for ln in lines:
        opts, _ = _split_line_options(ln)
        if opts:
            in_option = True
            options.extend(opts)
        else:
            if in_option:
                # 보기 이후 텍스트는 무시(보통 없음)
                continue
            if ln.strip():
                passage_parts.append(ln.strip())
    passage = "\n".join(passage_parts).strip()
    return passage, options


def split_problems(section_lines):
    """## 선택형 / ## 서답형 섹션 본문을 번호별 블록으로 분리."""
    blocks = []
    cur = None
    for ln in section_lines:
        m = PROB_RE.match(ln)
        if m:
            if cur is not None:
                blocks.append(cur)
            cur = {"number": int(m.group(1)), "stem": m.group(2).strip(),
                   "body": []}
        else:
            if cur is not None:
                # 다음 섹션 헤더(# or ##) 만나면 종료
                if re.match(r"^\s*#{1,2}\s", ln):
                    blocks.append(cur)
                    cur = None
                else:
                    cur["body"].append(ln)
    if cur is not None:
        blocks.append(cur)
    return blocks


def parse_answer_table(lines):
    """# 정답 · 해설 · 유형 표를 {N: {answer, typeId, tier, explanation}} 로.

    섹션엔 헤더 행이 없으므로, 첫 '|' 시작 행부터 표로 간주.
    표 이후 빈 줄이 아닌 다른 텍스트가 나오면 종료.
    """
    answers = {}
    in_table = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("|"):
            in_table = True
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not cells:
                continue
            if cells[0] in ("문항", "") or set(cells[0]) <= set("-: "):
                continue  # 헤더/구분선
            try:
                num = int(re.match(r"\s*(\d+)", cells[0]).group(1))
            except (ValueError, AttributeError):
                continue
            # cells: [문항, 정답, 유형ID·Tier, 해설]
            answer = cells[1] if len(cells) > 1 else ""
            type_tier = cells[2] if len(cells) > 2 else ""
            explanation = cells[3] if len(cells) > 3 else ""
            tm = TAG_RE.search(type_tier)
            type_id = tm.group(1) if tm else ""
            tier = tm.group(2) if tm else ""
            answers[num] = {
                "answer": answer,
                "typeId": type_id,
                "tier": tier,
                "explanation": explanation,
            }
        elif in_table and s:
            # 표 종료 후 다른 텍스트 블록 시작
            break
    return answers


def convert_file(md_path, source_key):
    text = open(md_path, encoding="utf-8").read()
    raw_lines = text.split("\n")

    title = ""
    for ln in raw_lines:
        m = H1_RE.match(ln)
        if m:
            title = m.group(1).strip()
            break
    subject = detect_subject(title + " " + os.path.basename(md_path))

    # 섹션 분할
    sections = {"select": [], "essay": [], "answer": []}
    cur = None
    for ln in raw_lines:
        s = ln.strip()
        if s.startswith("## 선택형"):
            cur = "select"
            continue
        if s.startswith("## 서답형") or s.startswith("## 서술형") or s.startswith("## 단답형"):
            cur = "essay"
            continue
        if ANSWER_H_RE.match(ln):
            cur = "answer"
            continue
        if re.match(r"^\s*#{1,2}\s", ln) and cur not in (None, "answer"):
            # 다른 섹션 헤더(예: 지문 난이도 검증) -> 본문 섹션 종료
            if cur in ("select", "essay"):
                cur = None
            continue
        if cur is not None:
            sections[cur].append(ln)

    sel_blocks = split_problems(sections["select"])
    ess_blocks = split_problems(sections["essay"])
    answers = parse_answer_table(sections["answer"])

    problems = []
    for blk in sel_blocks + ess_blocks:
        num = blk["number"]
        passage, options = parse_options_and_passage(blk["body"])
        qtype = "choice" if options else "essay"
        ans = answers.get(num, {})
        # 줄기에서 유형ID·Tier 추출(답안표 누락 시 보완)
        stem = blk["stem"]
        if not ans.get("typeId"):
            tm = TAG_RE.search(stem)
            if tm:
                ans["typeId"] = tm.group(1)
                ans["tier"] = tm.group(2)
        problems.append({
            "id": "%s#%d" % (source_key, num),
            "sourceKey": source_key,
            "subject": subject,
            "number": num,
            "qtype": qtype,
            "stem": re.sub(r"\s*\[[^\]]*\]\s*$", "", stem).strip(),
            "passage": passage,
            "options": options,
            "answer": ans.get("answer", ""),
            "typeId": ans.get("typeId", ""),
            "tier": ans.get("tier", ""),
            "explanation": ans.get("explanation", ""),
        })

    missing = [str(p["number"]) for p in problems if not p["answer"]]
    if missing:
        print("  [warn] %s: 답안표 누락 문항 %s" % (md_path, ",".join(missing)))
    return {
        "file": md_path,
        "title": title,
        "subject": subject,
        "problems": problems,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="web/data.js")
    args = ap.parse_args()

    out_root = os.path.join(args.root, "output")
    if not os.path.isdir(out_root):
        print("output/ 없음:", out_root)
        sys.exit(1)

    all_problems = []
    sources = []
    for md_path in sorted(glob.glob(os.path.join(out_root, "**", "*.md"),
                                    recursive=True)):
        rel = os.path.relpath(md_path, args.root).replace("\\", "/")
        source_key = os.path.basename(os.path.dirname(md_path)) or "root"
        print("변환:", rel)
        info = convert_file(md_path, source_key)
        sources.append({
            "file": rel,
            "title": info["title"],
            "subject": info["subject"],
            "count": len(info["problems"]),
        })
        all_problems.extend(info["problems"])

    data = {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "sources": sources,
        "problems": all_problems,
    }
    out_path = os.path.join(args.root, args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("window.QUIZ_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write(";\n")
    print("OK -> %s  (문항 %d개, 파일 %d개)" %
          (args.out, len(all_problems), len(sources)))


if __name__ == "__main__":
    main()
