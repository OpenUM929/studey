---
title: "Decision request — QUIZ_STANDARD revision (report 260825_06)"
sources: docs/QUIZ_STANDARD.md · docs/DATA_STANDARD.md · analysis/catalog/CODE_REGISTRY.md
created: 260825
requested_by: main-loop
state: submitted
---

# Decision request 12 — QUIZ_STANDARD (QS-1–4, Q4–Q5)

<document>
Target: docs/QUIZ_STANDARD.md (spec canon for the web viewer input). t2 CONFIRMED all 4:
QS-1 spec defines only tight-form tags (`df`×0 `aux`×0 in file) while real papers use
spaced+DF form; QS-2 subject mapping lacks social/history and math1/2 split vs
DATA_STANDARD §5.8's 7 codes; QS-3 schema lacks df/aux_types and any set-meta contract
(`scope_confirmed`×0 `set_id`×0 `frontmatter`×0) so §6 enforcement is unimplementable;
QS-4 example IDs T-01/W-01 pass §1.3 regex but are unregistered prefixes (CODE_REGISTRY
has no T-/W- entries) and visually collide with Tier codes. Details:
260825_06_*.md · *_second.md. Companion: report 01 parser fixes target the same standard.
</document>

<rounds>
1 round; t2: 4/4 confirmed. No disputes.
</rounds>

<open_questions>
1. (t1 Q4) REV_LOG TSV conversion: (a) keep MD (human-curated layer, DATA_STANDARD §0; conversion benefit currently nil — t2 leans a), or (b) convert (requires REV_GUIDE §4 revision as separate item + migration plan)?
2. (t1 Q5) scope_confirmed default false for legacy papers without frontmatter: uphold? (t2: yes — fail-safe; matches 모의40's own ⚠️ self-declaration.)
3. Checkbox approvals CB1–CB4 (tag standard section · subject mapping via DATA_STANDARD §5.8 · schema+frontmatter contract · real-ID examples). CB5 (REV_LOG TSV) is explicitly out-of-scope/separate.
</open_questions>

<output_format>
| question | ruling | evidence | note |
|----------|--------|----------|------|
| Q4 (a/b) | | | |
| Q5 uphold? | | | |
| CB1..CB4 | approve/reject each | | |
</output_format>
