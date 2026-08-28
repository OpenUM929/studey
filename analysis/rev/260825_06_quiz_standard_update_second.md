---
title: "t2 second opinion — 260825_06 QUIZ_STANDARD revision request"
source: analysis/rev/260825_06_quiz_standard_update.md
created: 260825
author: rev-auditor role (main loop; explore subagents unavailable — infra fallback)
verdict_summary: 4/4 findings CONFIRMED
---

# Second opinion — report 06 (QUIZ_STANDARD)

## Method
Fresh greps over docs/QUIZ_STANDARD.md and analysis/catalog/CODE_REGISTRY.md; cross-read
of DATA_STANDARD sections cited by the report.

## Verdicts

| # | Verdict | Independent evidence |
|---|---|---|
| QS-1 | CONFIRMED | QUIZ_STANDARD contains `df`×0 · `aux`×0 — spec defines only tight-form `[유형ID·Tier]` while real papers use spaced+DF form (모의40 evidence re-confirmed in report-01 t2) |
| QS-2 | CONFIRMED | §1 subject mapping lists only 영어/통합과학(+과학); DATA_STANDARD §5.8 defines 7 subject codes incl. social/history/math1/math2 |
| QS-3 | CONFIRMED | schema fields lack df/aux_types; `scope_confirmed`×0 · `set_id`×0 · frontmatter×0 in QUIZ_STANDARD — DATA_STANDARD §5.8/§6 contract unimplementable from this spec alone |
| QS-4 | CONFIRMED | example IDs `T-01`/`W-01` pass the §1.3 regex but CODE_REGISTRY registers NO T-/W- prefix — registration-principle violation, and `T-01` visually collides with Tier codes |

## Position for arbiter
All 4 findings stand; checkboxes 1–4 are coherent with report-01 fixes (same tag
standard target). Q4 (REV_LOG TSV): t2 leans 안 a) keep MD — human-curated layer per
DATA_STANDARD §0, conversion benefit currently nil; final ruling to arbiter/user.
Q5 (scope_confirmed default false): t2 agrees default-false is fail-safe and matches
모의40's own ⚠️ self-declaration — recommend uphold.
