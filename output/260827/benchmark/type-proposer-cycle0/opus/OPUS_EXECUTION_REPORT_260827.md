---
artifact_kind: external_execution_report
source: user-provided Claude Code Opus session transcript
preservation_status: verbatim-transcript
recovery_status: restored_from_conversation_evidence
authority: incident evidence only; not a type proposal, audit, ruling, or approval
---

# Opus execution report preservation copy (2026-08-27)

Recovery rule: The transcript below is preserved from the external Claude Code Opus session report supplied by the user. Codex/OMX did not infer, complete, or rewrite an external result.

```text
Snapshot verified and all 11 type-proposer instances are dispatched — one per corpus, each with a non-overlapping two-file write surface.

Pre-flight, measured before dispatch:

┌───────────────────────────────┬────────────────────────────────────┐
│             Check             │               Result               │
├───────────────────────────────┼────────────────────────────────────┤
│ input_snapshot.json hashes    │ 46/46 match, 0 mismatch, 0 missing │
├───────────────────────────────┼────────────────────────────────────┤
│ Corpus units                  │ 11                                 │
├───────────────────────────────┼────────────────────────────────────┤
│ Item total (Σ meta.yml items) │ 315 — matches contract exactly     │
└───────────────────────────────┴────────────────────────────────────┘

Five integrity flags found up front (recorded in opus/WIP.md, and pushed into every instance's brief so none of them papers over the gap):

- F1 — no rendered pages, in all 11 units. corpus/_images/<ID>/ holds only bindata/; every meta.yml has render_dpi: null, render_tool: hwp2md.py. The relay asks for pNN citations, but that evidence does not exist. Since <constraints> bars fabricated page citations, instances cite L<transcript line> instead and declare the gap — the one place I deliberately deviate from <requests> 3.
- F2 — scope guard has no comparison source for 8 of 11 units. curriculum_2022.md contains only 통합과학 and 공통수학2 sections. 성취기준 fields for korean/english/social/history/info go to blocked, not to guesswork.
- F3 — 정보 onboarding incomplete. No analysis/catalog/info.md; IN is in CODE_REGISTRY §3 but absent from §1, with only 2 of the 8 §6 onboarding items done. No IN-nn may be minted — it becomes a decision request.
- F4 — no answer key reaches the analysis in any unit. 7 units have answer_key: null; the other 4 name a file that is not among the 46 frozen inputs. Asserting answers is barred everywhere.
- F5 — EX-math2-20252M carries a transcription-stage unresolved span (item 17 풀이표 (나)).

Isolation held: nothing under codex-sol/ was opened except input_snapshot.json.

Two deliberate spec adjustments, both logged in WIP.md §4: the agents' analysis/wip/** slice files and their verify_log.tsv appends are suspended (the relay forbids touching both), so progress returns to me and verify_log rows survive as draft text inside each catalog_update.md. opus/WIP.md stays single-owner — mine — which is what makes 11-way parallelism safe here.

I'll fill the per-corpus checkpoint table and verify paths, counts, citations, and the isolation boundary as the returns arrive.

✻ Waiting for 11 background agents to finish

● Agent "type-proposer EX-english-20252F" failed: Agent terminated early due to an API error: You've hit your session limit · resets 9:50pm (Asia/Seoul)
You've hit your session limit · resets 9:50pm (Asia/Seoul)
Continuing automatically at 9:50pm · esc to cancel

● Usage limit reached · continuing automatically at 9:50pm · esc or type to cancel

✻ Waiting for 10 background agents to finish

● Agent "type-proposer EX-korean-20252F" failed: Agent terminated early due to an API error: You've hit your session limit · resets 9:50pm (Asia/Seoul)
You've hit your session limit · resets 9:50pm (Asia/Seoul)
Continuing automatically at 9:50pm · esc to cancel

✻ Waiting for 9 background agents to finish

● Agent "type-proposer EX-science-20252M" failed: Agent terminated early due to an API error: You've hit your session limit · resets 9:50pm (Asia/Seoul)
You've hit your session limit · resets 9:50pm (Asia/Seoul)
Continuing automatically at 9:50pm · esc to cancel

✻ Waiting for 8 background agents to finish

● Agent "type-proposer EX-social-20252F" failed: Agent terminated early due to an API error: You've hit your session limit · resets 9:50pm (Asia/Seoul)
You've hit your session limit · resets 9:50pm (Asia/Seoul)
Continuing automatically at 9:50pm · esc to cancel
```
