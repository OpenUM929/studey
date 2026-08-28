---
title: "Ruling — math·korean catalogs (decision 260825_11 / report 260825_05)"
source: analysis/rev/260825_11_math_korean_catalog_decision.md
created: 260825
author: rev-arbiter (Claude Code, Opus — tier-3)
status: approved (with amendments)
---

# Ruling 11 — math1·korean catalogs

## Independent verification performed

**M5 — re-read of both student documents (the load-bearing one):**

- `analysis/student/wrong_analysis_math.md` L28: `⚠️ 유일한 취약 후보: 9번 (SM-11 무리식
  제곱근 성질) (신뢰도 중)`; L57: `중간 9번 개수 오답(추정)`.
- `analysis/student/comprehensive_diagnosis_report_v2.md` L35: 공통수학 중간 —
  `15 확정 + 4 보류 / **1 확정 (18번)**`; **L36: 공통수학 기말 — `1 확정(19) + 미완 2(22·23)`**;
  L59: `수학중간 18 | 이차함수 최대·최소 | 125 → 10`.

So the catalog's "1학기 수학에서 **유일하게 틀린 문항** = 중간 9번" is wrong three ways:
9번 is an *estimated candidate*, a confirmed wrong answer exists at 중간 18번, **and the
report itself missed that 기말 19번 is also a confirmed wrong answer with 22·23 unfinished**.
Any replacement wording that mentions only 중간 18번 is still incomplete.

**M6 — korean point band re-measured across all four rounds:** 24중간 2.2~2.8 · 24기말
3.0~4.0 · 25중간 **1.7**~3.3 · 25기말 …~4.0. But the raw minimum in 25기말 is **1.5**, and
those 1.5 marks sit at `2025/기말/국어.txt` L52-53 — sub-item points inside a 서답형
(`(1) ㉠ : ( ) (1.5 점)`), not selected-response items. So "1.7~4.0" is right **only if the
line says 선택형**; the current line does not distinguish.

## Rulings

| question | ruling | evidence | note |
|----------|--------|----------|------|
| Q1 M5 fix direction | **(b) replace with the confirmed facts — extended** | the two student docs above | (a) merely softens a claim that is also factually incomplete. Required wording: "중간 **확정 오답 18번**(이차함수 최대·최소, 125→10) · 기말 **확정 오답 19번**(+ 미완 22·23). 중간 9번(SM-11 무리식)은 **취약 후보(추정 · 신뢰도 중)**." The 기말 19번 clause is the arbiter's addition — report 05 omitted it |
| Q2 M1 upper bound | **per-round split** | 26중간 lower 2.7; 26기말 #22 4.85 · #23 5.0 · #18 4.55 · #19 4.56 · #11~13 4.3 | Write "중간 2.7~4.x / 기말 ~5.0", not a merged "2.7~5.0". The merged range hides that the finals band is materially higher — the same information loss ruled against in 08/Q1 and 09/Q1 |
| Q3 korean 누락 (K-01 24중간 · K-10 25중간 · 매체 신설) | **defer to next cycle — register the backlog now** | additive completeness, not error correction; current term priority is 공통수학2 | Same disposition as ruling 10/Q3. Write the itemised list into korean.md 미결 with the date. **매체 유형 신설 requires a CODE_REGISTRY §5 pre-registration entry** (new number under the existing `K` prefix, append-only, no renumbering) — do not mint it inside the catalog alone |
| P1 math L5 배점 | **approve** (Q2 = per-round form) | M1 | |
| P2 L196 단답형 20 + 서술형 4 | **approve** | 26중간 p01 cover | resolves the catalog's self-contradiction (it cites 단답형 items 9~16 while claiming 단답형 8) |
| P3 L236 후반 서술형 → 단답형 10~23 | **approve** | 26기말 p01 cover: `단답형 23문항` 단독 | |
| P4 L5 "전 문항 풀이 과정·답 요구형" | **approve** | M4; L199 already limits this correctly to 서술형 | wording: "단답형 = 답만 요구 / 서술형 = 풀이 과정 서술" |
| P5 L221 단정 표기 | **approve** (Q1 = (b) extended form) | M5 | this is a 원칙위반 correction — also add a 금지·주의 line: "학생 데이터 인용은 확정/추정 등급을 반드시 병기한다" (REV_GUIDE §7) |
| P6 korean 배점 2.1~3.7 → 1.7~4.0 | **approve with a required qualifier** | M6 re-measurement | The line must read **"선택형 1.7~4.0점"**. Bare "1.7~4.0" is unsafe: the raw minimum in the corpus is 1.5 (25기말 서답형 세부 배점, L52-53). Add "서답형 세부 배점은 1.5점까지 내려감" |
| P7 K-01 "6번(겹받침 제10항)" | **approve** | 25기말 국어 L71-79 | |
| P8 K-09 17~21 → 18·20 (<보기>) + 17·19·21 | **approve** | 25기말 국어 L191-222 | |
| P9 K-02 "사이시옷 29항" → 제29항 ㄹ→ㄷ | **approve** | 24기말 국어 L44 | the 이튿날/사이시옷 link belongs to 제28항 and stays with K-04 — do not delete it, re-label it |
| P10 korean 누락 | **defer** (Q3) | | register in 미결 |

## Note for the applier (paths changed 260825)

Report 05 cites pre-rename paths. Current names: `analysis/catalog/math1.md`,
`analysis/catalog/korean.md`, `analysis/student/wrong_analysis_math.md`,
`analysis/student/comprehensive_diagnosis_report_v2.md`. Line numbers in report 05 refer to
the pre-rename snapshot and may have drifted — locate by content, not by line number.

## history
- 260825 arbiter ruling. Re-read both student docs and found report 05's M5 correction
  itself incomplete (기말 19번 확정 오답 omitted); re-measured the korean band and found the
  proposed "1.7~4.0" unsafe without a 선택형 qualifier (raw corpus minimum is 1.5, a 서답형
  sub-point). Ruled Q1=(b) extended, Q2 = per-round split, Q3 = defer-with-registered-backlog.
  8 checkboxes approved outright, P6 approved with a required qualifier, P10 deferred.
