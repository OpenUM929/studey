---
actor: Codex/OMX
model: Sol
task: cycle0_S2_type_propose_relay
target: 2025-2학기 신규 11개 corpus의 external Claude Code Opus type-proposer 제안
status: in-progress
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | S2 회람 사전점검·패키지 | done | output/260827/260827_03_type-proposer_relay.md | .claude/agents/type-proposer.md(모델 opus·write surface)와 REV_GUIDE §6-b를 읽고 11 corpus/315문항/필수 산출물 33개/375,238 bytes를 실측했다. |
| 2 | External Opus 유형 제안 | waiting-external | output/260827/260827_03_<ID>_{type_analysis,catalog_update}.md | 외부 Claude Code CLI / Opus가 11 ID별 제안서 22개·verify_log append·자기 WIP를 작성해야 한다. Codex/OMX는 응답/승인을 추정하지 않는다. |

NEXT: 사용자가 [CC 회람]을 별도 Claude Code Opus CLI에 전달한 뒤, 지정된 22개 제안서와 type-proposer WIP가 생기면 이를 읽어 S3 review loop를 시작한다.
| 1a | S2 측정 정정 | done | output/260827/260827_03_type-proposer_relay.md | 초안의 item_count 정규식이 실제 meta.yml 키 items와 불일치하여 외부 전달 전 0문항/잘못된 byte 표기를 탐지했다. items로 재측정해 11개·315문항·33/33 산출물·373,834 bytes로 회람을 교체했다. |

NEXT: 사용자가 [CC 회람]을 별도 Claude Code Opus CLI에 전달한 뒤, 지정된 22개 제안서와 type-proposer WIP가 생기면 이를 읽어 S3 review loop를 시작한다.
