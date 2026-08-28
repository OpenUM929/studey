# S2 operational wave relay — 10 corpus units (286 items)

Created by: Codex/OMX main loop (Sol)
Date: 2026-08-27
Status: ready for user-copied external Claude Code Opus execution
Supersedes: the unsafe 11-way-dispatch interpretation of `260827_03_type-proposer_relay.md`; it does not delete or amend that historical relay.

## Dispatch record

- Purpose: advance every non-benchmark 2025-2 corpus through the external-only `type-proposer` stage.
- Reserved benchmark unit: `EX-science-20252M` (29 items). It is excluded from this operational wave and remains isolated at `output/260827/benchmark/type-proposer-cycle0/`.
- Operational scope: 10 corpus units / 286 items / 30 source artifacts / 34 explicit item slices; item slices are <=10 items.
- Execution shape: exactly one Claude Code main session, strictly sequential corpus and slice order, no subagents, no background agents, no parallel dispatch, no automatic continuation, and no retry after a quota/error stop.
- Stop/resume: after any error, context/quota warning, integrity-blocking finding, or unavailable source page, save only the named external WIP checkpoint and stop. A later user-authorized session resumes from its `NEXT` pointer; it must not redo completed slices.

```text
[CC 회람] 260827_04 — 2025-2학기 운영 10개 코퍼스 유형 제안 (순차·단일 세션)
<target> Process these ten refined corpus units in exact order and declared <=10-item slices: (1) corpus/EX-english-20252M/ — 32 items: 1-10, 11-20, 21-30, 31-32; (2) corpus/EX-info-20252M/ — 25: 1-10, 11-20, 21-25; (3) corpus/EX-math2-20252M/ — 22: 1-10, 11-20, 21-22; (4) corpus/EX-social-20252M/ — 25: 1-10, 11-20, 21-25; (5) corpus/EX-history-20252M/ — 29: 1-10, 11-20, 21-29; (6) corpus/EX-korean-20252F/ — 31: 1-10, 11-20, 21-30, 31; (7) corpus/EX-english-20252F/ — 33: 1-10, 11-20, 21-30, 31-33; (8) corpus/EX-science-20252F/ — 33: 1-10, 11-20, 21-30, 31-33; (9) corpus/EX-social-20252F/ — 27: 1-10, 11-20, 21-27; (10) corpus/EX-history-20252F/ — 29: 1-10, 11-20, 21-29. Read each unit's transcript.md, meta.yml, verify_log.tsv, and corpus/_images/<ID>/; then read analysis/catalog/_README.md, COMMON_TYPES.md, TYPE_MASTER.md, DIFFICULTY_RUBRIC.md, CODE_REGISTRY.md, analysis/curriculum_2022.md, its subject catalog, and analysis/FORECAST_GUIDE.md. Measured scope: 286 meta.yml items / 30 source artifacts. EX-science-20252M is deliberately excluded as the isolated comparison pilot.
<touched> Codex/OMX created this relay and analysis/wip/codex-omx_260827_cycle0_s2_staged_dispatch.md this round. S1 previously refined only the ten target corpus units' transcript.md, meta.yml, verify_log.tsv and updated analysis/EXTRACTION_LOG.md. No catalog, HARVEST_LOG, or benchmark result was changed.
<executor> type-proposer (external Claude Code CLI / Opus; instruction inspected: .claude/agents/type-proposer.md). Its defined role is the authoring owner that performs per-item type assignment, consolidation, and catalog-update drafts from a refined corpus.
<requests> 1) For each unit, report integrity as ready | ready-with-flags | blocked after transcript↔meta.yml↔verify_log and page spot-checks. 2) For every non-blocked unit, write the two Korean proposal documents with all per-item assignments, 5-12 consolidated types, axes/traps/star evidence, common-pattern comparison, and new/existing catalog diffs; report complete | partial | blocked. 3) Append classify, merge, and grade rows with evidence pages to only that unit's verify_log.tsv. 4) If catalog-ID policy or evidence is insufficient, make no ID claim: record a decision request. 5) Work only one named slice at a time; after each slice append one checkpoint to the WIP and set NEXT before beginning another slice.
<reply> For each ID write output/260827/260827_04_<ID>_type_analysis.md and output/260827/260827_04_<ID>_catalog_update.md (20 documents total), and write only analysis/wip/type-proposer_260827_cycle0_2025S2_operational.md. Each document must follow .claude/agents/type-proposer.md and analysis/REV_GUIDE.md §2-b C. The final WIP row must list completed IDs/slices, paths, assigned count, new-draft count, update-diff count, common-pattern count, flags, and NEXT. If stopped, return the same fields with status partial/blocked and no claim that unfinished slices were reviewed.
<constraints> One main Claude Code session only. Do NOT spawn agents/subagents, background tasks, parallel workers, or automatic continuations; do NOT retry after a quota/API/context failure. Process the listed corpus/slice order sequentially. Write only the 20 named output proposal files, the ten target verify_log.tsv append surfaces, and your one named WIP; never modify catalog files, HARVEST_LOG, EXTRACTION_LOG, transcript.md, meta.yml, benchmark paths, or another WIP. No commit. Preserve append-only rows. Do not invent page citations, IDs, answers, counts, or scope coverage: use ⚠️미확인 / decision request and stop at the checkpoint when a required source is absent. Before each new corpus verify the prior WIP NEXT pointer and before ending verify paths/counts/warnings.
```

## Frozen input measurements

| ID | items | transcript lines | SHA-256(transcript.md) | existing verify rows |
|---|---:|---:|---|---:|
| EX-english-20252M | 32 | 258 | 689ab514074f52b35f0fc501ca69152a9d4b4fd368888fca7c4eb836085d80bb | 4 |
| EX-info-20252M | 25 | 137 | ea58deff67189a55cc5e4da902bfb0a3e35ab02a8434af1244776d80c87afe94 | 3 |
| EX-math2-20252M | 22 | 104 | 9f8304db309aad65fb5ad3c097adb3edbb8883e6eca7ff8dc898a107f354ba10 | 3 |
| EX-social-20252M | 25 | 253 | c5cc7d6c8fad82636a4aba3ed37579ad81a341737ecbb713757f0653ca33fdcd | 3 |
| EX-history-20252M | 29 | 248 | b96cb003b38fad7aafb9c7396c9e318c3afe1151c0f8fb9f54e5bbb1e765f1e8 | 3 |
| EX-korean-20252F | 31 | 407 | 2f8cbdc630155886b89daf56d882cf8432c4c28d52f3925e3ebb4b8a5d18e879 | 3 |
| EX-english-20252F | 33 | 282 | 3c2464f6b95a216c8011e9c1b873d20f40d61fc8d4ed1075e7d8d5985695ea75 | 3 |
| EX-science-20252F | 33 | 312 | 8cf3a26aafc7512a963b4ccca3de71e61e4944018de665b297789d7ac0d99547 | 3 |
| EX-social-20252F | 27 | 229 | 5a07364fdb17278beeb2e6ca6115e1ba78844d2d4751e1a06e4030a4eeec7cdb | 3 |
| EX-history-20252F | 29 | 222 | a5b61e25276b566e6566e2877f53aeae161facdde4ba0d6f8e5843f31d68a8c4 | 3 |
| **Total** | **286** |  |  |  |

## Gate before a claim of completion

`[GATE] external return exists: exactly 20 named proposal documents + one WIP; all claimed complete units have assigned count = meta.yml items; verify_log additions are append-only and contain classify/merge/grade evidence; no catalog or ledger writes.`

No external output has been created by this document.
