#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""_redact_key.py - build the blind-solve copy of an item set.

A blind solve is only a gate if the solver cannot see the answer, the derivation,
or the trap. Stripping the answer table alone is NOT enough for this set - three
separate channels leak:

  1. the key section itself         "# 정답 · 해설 · 유형" and everything after it
  2. the 27 `[근거: ...]` tags      name the source item each problem came from
  3. 채점 조건 sentences with 오답  announce the exact error path the item tests
     (e.g. "`b`를 7로 쓴 답은 오답이다" hands over the E5 경계 오류 trap)

plus the authoring blockquote "**검증 상태**: ..." which reports the author's own
solve-back result. All four are removed here; the format constraints inside 채점
조건 ("정수 하나만 쓴다", "두 값을 `a b` 순서로") are kept, because the solver needs
to know the expected answer shape.

260909 - five of the 근거 tags wrap onto a second line. The first version dropped
only the line carrying the opening "[근거:", so the tails survived, and one tail
read "EX-info-20252M 선택 8(`if a % i == 0` 판정 후 누적)" - the answer to item 18's
blank (가). Tags are now consumed to their closing bracket, and the fail-closed
check compares against the exact line set instead of guessing at a shape.

Usage:  python analysis/wip/_redact_key.py <set.md> <out.md>
Exit:   0 written | 1 refused (a leak channel survived, or the key was not found)
"""
import io
import re
import sys

KEY_HEAD = re.compile(r"^# 정답")
GRIT = re.compile(r"\[근거:")
VERIFY = re.compile(r"^>\s*\*\*검증 상태\*\*")
SENT = re.compile(r"[^.。]*오답[^.。]*\.?")


def grit_block_lines(text):
    """Every line of every [근거: ...] block, wrapped continuations included."""
    got, inside = [], False
    for ln in text.split("\n"):
        if KEY_HEAD.match(ln):
            break
        if inside:
            got.append(ln)
            if "]" in ln:
                inside = False
            continue
        if GRIT.search(ln):
            got.append(ln)
            if "]" not in ln.split("[근거:", 1)[1]:
                inside = True
    return got


def redact(text):
    lines = text.split("\n")
    out, drop_quote, drop_grit = [], False, False
    for ln in lines:
        if KEY_HEAD.match(ln):
            break
        if VERIFY.match(ln):
            drop_quote = True
            continue
        if drop_quote:
            # keep swallowing the rest of that blockquote
            if ln.startswith(">"):
                continue
            drop_quote = False
        if drop_grit:
            # a [근거: ...] tag may wrap onto following lines; swallow to its ']'
            if "]" in ln:
                drop_grit = False
            continue
        if GRIT.search(ln):
            if "]" not in ln.split("[근거:", 1)[1]:
                drop_grit = True
            continue
        if "오답" in ln:
            ln = SENT.sub("", ln).rstrip()
            if ln.strip() in (">", ">*", ""):
                continue
        out.append(ln)
    return "\n".join(_close_tails(out))


def _close_tails(lines):
    """S8 6회차 A-1: 「오답」 절·줄을 지우면 **직전 줄**의 쉼표가 문장 끝에 남는다.

    실제 사례는 21번 채점 조건이었다 — 두 줄 중 뒷줄만 「오답」을 담고 있어서 통째로
    사라졌고, 앞줄이 「…으로 쓴 답,」 로 절단된 채 게이트 입력물에 실렸다.
    줄 하나만 보고는 판정할 수 없다(앞줄에는 「오답」이 없다). 그래서 이웃을 본다:
    쉼표로 끝난 줄 다음이 빈 줄·구분선·다른 블록이면 그 쉼표는 이어질 곳을 잃은 것이다.

    원칙 12: 자를 재는 도구도 감사 대상이다.
    """
    TAIL = (",", "，", "·", "…", ";")
    CLOSED = (".", "。", ":", "：", "*", "`", ">", ")", "」")
    out = list(lines)
    for i, ln in enumerate(out):
        s = ln.rstrip()
        if not s.endswith(TAIL):
            continue
        nxt = out[i + 1].strip() if i + 1 < len(out) else ""
        if s.lstrip().startswith(">"):
            continues = nxt.startswith(">")
        else:
            continues = bool(nxt) and nxt != "---"
        if continues:
            continue
        s = s.rstrip("".join(TAIL) + " \t")
        if s and not s.endswith(CLOSED):
            s += "."
        out[i] = s
    return out


def main():
    if len(sys.argv) != 3:
        print("usage: _redact_key.py <set.md> <out.md>")
        return 1
    src, dst = sys.argv[1], sys.argv[2]
    text = io.open(src, encoding="utf-8-sig").read()
    if not any(KEY_HEAD.match(l) for l in text.split("\n")):
        print("[err] answer-key heading '# 정답' not found - refusing to fake a blind solve")
        return 1
    red = redact(text)
    # fail-closed: prove every channel is gone before writing
    leaks = []
    if any(KEY_HEAD.match(l) for l in red.split("\n")):
        leaks.append("key section")
    if GRIT.search(red):
        leaks.append("근거 tags")
    survivors = set(grit_block_lines(text)) & set(red.split("\n"))
    if survivors:
        leaks.append("근거 tag continuation lines (%d)" % len(survivors))
    if "오답" in red:
        leaks.append("오답 hints")
    if VERIFY.search(red):
        leaks.append("검증 상태")
    if leaks:
        print("[err] refusing to write - leak channels survived: " + ", ".join(leaks))
        return 1
    io.open(dst, "w", encoding="utf-8", newline="\n").write(red)
    n_items = len(re.findall(r"^\*\*\d+\.\*\*", red, re.M))
    print("[ok] %s -> %s  (%d lines, %d items, key+근거(다줄 포함)+오답 removed)"
          % (src, dst, red.count("\n") + 1, n_items))
    return 0


if __name__ == "__main__":
    sys.exit(main())
