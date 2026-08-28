---
title: "t2 second opinion — 260825_05 math·korean catalogs"
source: analysis/rev/260825_05_catalog_math_korean_minor.md
created: 260825
author: rev-auditor role (main loop; explore subagents unavailable — infra fallback)
verdict_summary: 8 CONFIRMED · 1 PARTIAL · 누락 후보 not re-verified
---

# Second opinion — report 05 (math·korean)

## Method
PNG page reads (26중간 수학 p01, 26기말 수학 p01·p07); parenthesized-point scans for
korean txts (points use `(4.0점)` form, not `[ ]` — report's bracket notation was its own
normalization); student-doc line checks; catalog line verifications.

## Verdicts

| # | Verdict | Independent evidence |
|---|---|---|
| M1 | CONFIRMED | 26기말 p07 read: **#22 [4.85점] · #23 [5점]** — upper bound 5.0; catalog `2.7~4.2` wrong (lower 2.7 stands) |
| M2 | CONFIRMED | 26중간 p01 cover read: `총 7쪽, 단답형 20문항, 서술형 4문항` — catalog `단답형 8 + 서술형` self-contradictory (its own cited items 9–16 ARE 단답형) |
| M3 | CONFIRMED | 26기말 p01 cover read: `총 7쪽, 단답형 23문항` — 서술형 none; catalog `후반 서술형` wrong |
| M4 | PARTIAL | cover confirms 단답형/서술형 split; item-level "답만 요구" not page-verified — but M2 already exposes the preamble overstatement |
| M5 | CONFIRMED | wrong_analysis_math.md carries `취약 후보 … (신뢰도 ??)` wording; comprehensive_diagnosis_report_v2.md records `15 확정 + 4 추정 / 1 확정 (18번)` — "유일하게 틀린 문항" is an overstatement twice over |
| M6 | CONFIRMED | 25중간 #16 `(1.7점)` @L444; 25기말 #11 `(4.0점)` @L114; distinct-pt sets — true band 1.7~4.0; catalog `2.1~3.7` wrong |
| M7 | CONFIRMED | 25기말 #6 (L71) `<보기>` = 표준발음법 **제10항 겹받침** (L73) — number omitted in catalog invites 5번 confusion |
| M8 | CONFIRMED | 25기말 #18 (L197) attaches 자기결정성 이론 `<보기>` (L199) — block `17~21` over-attributes |
| M9 | CONFIRMED | 24기말 L44: 제29항 = 끝소리 'ㄹ' + 어미 연결 → ㄹ→ㄷ 규정 — NOT 사이시옷(제28항); catalog label wrong |

## Position for arbiter
All P1–P9 merit approval (M4/P4 conditional on Q1-style wording choice).
누락 후보 (26중간 17–20·26기말 10–23 유형, K-01 24중간 보강, K-10, 매체 신설): not
re-verified — forward for arbiter's scope decision (Q3).
Note for packages: catalog file is now `analysis/catalog/math1.md` / `korean.md`
(renamed 260825); student docs renamed likewise — apply new paths when fixing.
