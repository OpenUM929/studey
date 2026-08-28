---
actor: Codex/OMX coordinator
task: cycle0_s3_opus_comparison_relay
status: done
updated: 2026-08-27
---

# Codex/OMX WIP — Cycle 0 S3 external comparison relay

| no | scope | state | artifact | evidence |
|---:|---|---|---|---|
| 1 | 11 corpus / 315 items | done | output/260827/benchmark/type-proposer-cycle0/comparison/INPUT_MANIFEST_260827.tsv | 33 frozen corpus-input hashes |
| 2 | Codex-only advisory outputs | done | output/260827/benchmark/type-proposer-cycle0/comparison/CODEX_ARTIFACT_MANIFEST_260827.tsv | 49 artifact hashes |
| 3 | External Opus comparison request | done | output/260827/benchmark/type-proposer-cycle0/comparison/260827_01_codex_only_comparison_request.md | one-session/no-subagent/sliced audit constraints |

NEXT: Wait for output/260827/benchmark/type-proposer-cycle0/opus/OPUS_COMPARISON_EVALUATION_260827.md; do not infer a verdict or modify canonical artifacts before reading it.
| 4 | Relay persistence and post-return comparison setup | done | output/260827/benchmark/type-proposer-cycle0/comparison/260827_01_CC_RELAY.md; output/260827/benchmark/type-proposer-cycle0/comparison/260827_02_blind_comparison_score_template.md | exact six-field relay saved; blind scoring remains pending external reply |

NEXT: Read and validate output/260827/benchmark/type-proposer-cycle0/opus/OPUS_COMPARISON_EVALUATION_260827.md only after it exists; then populate no score until input identity and no-canonical-change declarations pass.
| 260828 | Coordinator (Codex/OMX) | created separate external assurance/satisfaction evaluation relay | comparison/260828_01_opus_codex_assurance_evaluation_request.md | pending external reply at output/260827/benchmark/type-proposer-cycle0/opus/OPUS_CODEX_ASSURANCE_EVALUATION_260828.md; C1–C8 intentionally not applied |
