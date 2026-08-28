---
title: "Decision request — tag pipeline fixes (report 260825_01)"
sources: web/parser.js · web/app.js · tools/md2quiz.py · docs/QUIZ_STANDARD.md · output/260822/공통수학2_도형의방정식_모의40.md
created: 260825
requested_by: main-loop
state: submitted
---

# Decision request 07 — tag pipeline (F1–F9)

<document>
Current state (verified by t2 re-execution): parser.js TAG_RE `/\[([A-Za-z0-9\-]+)·?(T\d)\s*\]`
rejects spaced body tags and DF tails (F1) and bracketless answer-table cells (F2);
no DF field exists (F4); SUBJECT_MAP lacks social/history and math1/2 split (F6); scoring
is 2-state correct/wrong (F7); persistence = 5 localStorage keys, export excludes student
data, reset wipes all (F8); splitSections resets collection on unit `##` headings →
0 problems parsed from real paper (F9, mirrored in tools/md2quiz.py L86–176).
Full findings: analysis/rev/260825_01_tag_pipeline_mismatch.md (t1) ·
260825_01_tag_pipeline_mismatch_second.md (t2, 9/9 CONFIRMED).
</document>

<rounds>
_index.md: 1 round, t1 flagged → t2 cross-checked (9/9 confirmed, no disputes).
t1 opinion: all 9 stand; Q3 option (b) aligns with the fix. t2 concurs.
</rounds>

<open_questions>
1. (t1 Q3) Tag standard rewrite scope for 모의40:
   (a) minimal — add aux `+SM2-11` to item 16 body tag only;
   (b) full — rewrite all 40 tags to standard `[type·Tier·DFlist(+aux)]`.
   t1+t2 lean (b) for consistency with parser fix; it is a large change to a released
   paper → needs explicit approval.
2. Checkbox approvals (proposed_fixes 1–5 of report 01):
   CB1 parser.js RE overhaul + aux/DF extraction + SUBJECT_MAP completion + frontmatter priority
   CB2 F9 section-reset fix (parser.js + md2quiz.py)
   CB3 app.js 4-state scoring (O/△/X//) + ledger export button (TSV+BOM)
   CB4 모의40/_part2 item-16 aux tag addition
   CB5 (conditional on Q1=b) full tag standardization of 모의40
</open_questions>

<output_format>
| question | ruling | evidence | note |
|----------|--------|----------|------|
| Q1 (a/b) | | | |
| CB1..CB5 | approve/reject each | | |
| any F-disagreement | | | |
</output_format>
