---
title: "t2 second opinion — 260825_01 tag pipeline"
source: analysis/rev/260825_01_tag_pipeline_mismatch.md
created: 260825
author: rev-auditor role (main loop; explore subagents unavailable — infra fallback)
verdict_summary: 9/9 findings CONFIRMED
---

# Second opinion — report 01 (tag pipeline)

## Method
Independent re-execution, not quote-trust: Python `re` re-ran TAG_RE against 4 samples;
static re-read of parser.js/app.js/md2quiz.py; recount of 모의40/_part2 markers.
Live node run NOT repeated (no browser env) — static chain deemed sufficient.

## Verdicts

| # | Verdict | Independent evidence |
|---|---|---|
| F1 | CONFIRMED | `[SM2-01 · T1 · DF1]`=False · `[SM2-01·T1]`=True · `[SM2-01·T1 · DF1]`=False (re-run) |
| F2 | CONFIRMED | `SM2-13·T4`=False (bracketless cell unreachable) |
| F3 | CONFIRMED (static) | fallback path exists but corpus tags are standalone lines; stemTagSameLine=0 |
| F4 | CONFIRMED | no DF token anywhere in parser.js |
| F5 | CONFIRMED | tagLines=40 · tableRows=40 · aux only @446 · part2 aux=1 |
| F6 | CONFIRMED | SUBJECT_MAP has exactly 4 rows (과학/영어/수학/국어) — no social/history/math split |
| F7 | CONFIRMED | LS=5 keys; auto-assign 2-value; mark() called only with correct/wrong |
| F8 | CONFIRMED | exportStandalone serializes DATA only; reset clears 4 student stores |
| F9 | CONFIRMED (static) | splitSections resets cur on `#{1,2}` headings; 모의40 has 4 unit `##` headings after `## 서답형` (first L18 `## I-1 평면좌표 (1~6번)`); md2quiz.py carries same reset (cur=None at L86/99/161/176) |

## Discrepancies vs report
- None material. md2quiz.py reset lines span 86–176 (report cited 173–176) — same defect, wider footprint.

## Position for arbiter
All 9 findings stand. Q3 option (b) full-tag rewrite aligns with F1/F4 fix; requires
user approval per principle 8. Checkboxes 5/5 forwarded as approval requests.
