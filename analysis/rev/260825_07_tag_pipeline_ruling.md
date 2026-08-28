---
title: "Ruling — tag pipeline (decision 260825_07 / report 260825_01)"
source: analysis/rev/260825_07_tag_pipeline_decision.md
created: 260825
author: rev-arbiter (Claude Code, Opus — tier-3)
status: approved (with amendments)
---

# Ruling 07 — tag pipeline

## Independent verification performed (not quote-trust)

| check | method | result |
|-------|--------|--------|
| F9 | `node -e` running `web/parser.js` against the real `output/260822/공통수학2_도형의방정식_모의40.md` | `problems 0 typeIdFilled 0` — **empirically reproduced** |
| F1–F3 | direct read parser.js:9 (`TAG_RE`), :92 (`parseAnswerTable`), :145-148 (fallback) | confirmed |
| F4 | full read of parser.js (181 lines) — no `DF` token, no df field in the 12-field object (:149-162) | confirmed |
| F5 | regex count over 모의40 | 40 body tags · 40 answer rows · aux only at L446 |
| F6 | parser.js:13-18 | exactly 4 rows (과학/영어/수학/국어) |
| F7/F8 | app.js:4-10, 203, 256-262, 268, 327-333, 336-337 | confirmed |
| F9 footprint | tools/md2quiz.py `convert_file` section loop (`cur = None` on `#{1,2}` headings) | same defect confirmed |

**All 9 findings stand. No disagreement.**

## Arbiter's own new finding — A1 (blocks the proposed fix as written)

The reports state that every body tag is `[ID · Tier · DFlist]`. That is **incomplete**.
Machine census of all 40 body tags:

- 34 tags: `SM2-nn · Tn · DF…`
- **6 tags carry a fourth slot — a 함정(trap) code**:
  `SM2-18 · T3 · DF1·DF2·DF4 · E5`, `SM2-25 · … · E5`, `SM2-24 · … · E9`,
  `SM2-29 · … · E5`, `SM2-28 · T3 · DF1·DF2 · E5`, `SM2-28 · T4 · … · E9`

`E1~E9` is a registered code family (`analysis/catalog/TYPE_MASTER.md` L159 ff., and
CODE_REGISTRY §2 lists 함정 `E1~E9` among the confusable families).

Consequence: the corrected RE proposed in report 01
`\[([A-Za-z0-9\-]+)\s*·\s*(T\d)(?:\s*·\s*(DF\d+(?:·DF\d+)*))?\s*\]`
**fails on all 6** of those tags (tested — 6/40 non-match), i.e. it would silently drop
6 items' type IDs after the fix. CB1 therefore cannot be approved as written.

Amended form (tested — **40/40 match, 0 unclassified tail tokens**):

```
\[\s*([A-Za-z0-9]+(?:-\d+)?)\s*·\s*(T\d)((?:\s*·\s*[^\]·]+)*)\s*\]
```
then split group 3 on `·` and classify each token by shape:
`DF\d` → df[] · `E\d` → trap[] · `+?SM2?-\d+` → aux[] · anything else → keep raw in
`tagExtra[]` (never discard — unknown slots must survive, principle 3).

Bracketless answer-table cell (39 plain + 1 with aux):
`^\s*([A-Za-z0-9]+(?:-\d+)?)\s*·\s*(T\d)(?:\s*\(보조\s*([A-Za-z0-9\-]+)\))?`

## Rulings

| question | ruling | evidence | note |
|----------|--------|----------|------|
| F1–F9 | **approve** (all 9 stand) | table above; F9 reproduced live (`problems=0`) | F9 is the blocking defect — fix it first, F1–F4 only surface afterwards |
| Q1 (a) minimal vs (b) full rewrite of 모의40 tags | **(a) approve · (b) reject** | 40/40 body tags are already in the standard form; the only real gap is item 16's missing aux. A "full rewrite" would be a large edit to a released paper that changes almost nothing | The corpus is richer than the spec (it carries E-codes). Widen the **standard** to the corpus, do not rewrite the corpus to a narrower standard. This reverses t1+t2's lean, on evidence they did not have |
| A1 (arbiter) trailing E-codes | **new defect — must be absorbed into CB1** | 6/40 tags carry `· E5`/`· E9`; t1's proposed RE fails on all 6 | amended RE given above |
| CB1 parser.js RE overhaul | **approve with amendment** | must use the amended RE + tail-token classifier + `tagExtra[]` passthrough; SUBJECT_MAP completion and frontmatter priority approved as proposed | subject codes must come from DATA_STANDARD §5.8 (7 codes), not ad-hoc |
| CB2 F9 section-reset fix (parser.js + md2quiz.py) | **approve** | verified in both files; keep the two implementations byte-equivalent in behaviour | highest priority — nothing else is observable until this lands |
| CB3 app.js 4-state scoring + ledger export | **approve** | O/△/X//(백지) is a user-fixed decision; current 2-state cannot express △ or / | export TSV must be UTF-8 **with BOM** (DATA_STANDARD §0) and must carry `set_id`, `qnum`, `main_type`, `aux_types`, `tier`, `df`, `mark_code` so it feeds ATTEMPT_LOG §5.1 directly |
| CB4 item-16 aux tag `+SM2-11` | **approve** | body tag L165 lacks the aux the answer table records at L446; same in `_part2_직선.md` L106 | write it in the standard slot: `[SM2-13 · T4 · DF1·DF2·DF5·DF8 (+SM2-11)]` |
| CB5 full tag standardisation | **reject** | consequence of Q1=(a) | if a future paper introduces a genuinely non-conforming tag, raise a new review then |

## Conditions on application

1. CB2 before CB1 — otherwise the RE fix cannot be tested against real data.
2. After CB1, re-run the node harness on 모의40 and `_part2_직선.md`; the acceptance
   criterion is **40 problems, 40 typeId filled, 40 tier filled, 6 trap codes captured,
   1 aux captured**. Record the run in a REV_LOG trace row.
3. `analysis/catalog/DIFFICULTY_RUBRIC.md` is the DF definition canon — report 01 cites
   the pre-rename path `난이도_루브릭.md`. Use the current name when applying.

## history
- 260825 arbiter ruling. Verified F1–F9 independently (live node run for F9), found new
  defect A1 (trap-code slot in 6/40 tags breaks the proposed RE), ruled Q1=(a) against the
  t1+t2 lean, approved CB1(amended)·CB2·CB3·CB4, rejected CB5.
