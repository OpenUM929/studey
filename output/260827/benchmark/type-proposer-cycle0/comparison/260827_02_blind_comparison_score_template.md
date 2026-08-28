---
artifact_kind: blind_comparison_score_template
status: pending_external_reply
created: 2026-08-27
scope: non-canonical benchmark only
---

# Codex-only ↔ Opus comparison score sheet

## Preconditions

Do not score until the external reply exists at `../opus/OPUS_COMPARISON_EVALUATION_260827.md`, its declared input hashes match `INPUT_MANIFEST_260827.tsv`, and it explicitly states that no canonical changes were made. A missing reply, hash mismatch, or missing limitation statement is `▲ blocked`, not a zero score.

## Blind-label procedure

1. Copy the Codex advisory findings and the Opus evaluation findings into separate temporary packets labelled `A` and `B` without actor/model names.
2. A teacher evaluates each packet against the same representative evidence set: EX-science-20252M items 1–29 and the two deterministic spot items named in the request.
3. Reveal actor labels only after all rows below are completed. This worksheet records the revealed mapping in the final section.
4. This comparison never authorizes a catalog, ledger, corpus, or release change.

## Deterministic checks

| check | expected evidence | Codex packet | Opus packet | pass/fail/blocked |
|---|---|---|---|---|
| input identity | 33 rows and matching SHA-256 in INPUT_MANIFEST_260827.tsv |  |  |  |
| declared corpus coverage | 11 units / 315 meta.yml items |  |  |  |
| no invented authority | advisory-only boundary; no canonical writes |  |  |  |
| representative slice coverage | 10 + 10 + 9 = 29 EX-science-20252M items |  |  |  |
| sampling limitation | two deterministic spot items named and bounded |  |  |  |

## Evidence-quality rubric

| criterion | operational definition | score A (0–2) | score B (0–2) | evidence path/line |
|---|---|---:|---:|---|
| traceability | every material claim points to corpus evidence or explicitly states an evidence gap |  |  |  |
| scope discipline | curriculum/catalog gaps become HOLD or conditional, not fabricated mappings |  |  |  |
| type-match discipline | existing IDs are cited; no illegal new ID or status promotion appears |  |  |  |
| defect discovery | catches material traceability, count, or boundary defects without false certainty |  |  |  |
| operational clarity | conclusion distinguishes sampled evidence, unverified scope, and next required stage |  |  |  |

Scoring: 0 = materially unsupported; 1 = partially supported or incomplete; 2 = evidence-backed and bounded. Do not aggregate a score when any deterministic check is `blocked`.

## Result after label reveal

| packet | actor | model/session | total /10 | deterministic gate | teacher judgment | critical defect? |
|---|---|---|---:|---|---|---|
| A |  |  |  |  |  |  |
| B |  |  |  |  |  |  |

## Decision rule

One benchmark cannot establish substitution. Record only whether this single comparison is usable evidence. The project policy remains: at least three comparable completed tasks, zero critical Sol misses, and no regression on the agreed scorecard before any replacement recommendation.
