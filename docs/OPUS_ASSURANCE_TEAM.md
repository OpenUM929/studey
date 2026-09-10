# Opus-assurance Codex team

## Objective

Maximize the reliability of a Codex/OMX advisory result through real high-depth Sol separation of duties. This team is designed to challenge an external Opus result constructively; it does not assert that a Sol team replaces or exceeds Opus.

## Required lanes

| Lane | Native definition | Model / depth | Authority | Exclusive output |
|---|---|---|---|---|
| author | `.codex/agents/assessment-author-sol.toml` | Sol / runtime-recorded high | substantive bounded draft | author draft only |
| evidence auditor | `.codex/agents/assessment-evidence-auditor-sol.toml` | Sol / runtime-recorded high | source and traceability audit | audit report only |
| adversarial critic | `.codex/agents/assessment-adversarial-critic-sol.toml` | Sol / runtime-recorded high | defect discovery and challenge | critique report only |
| gatekeeper | `.codex/agents/assessment-gatekeeper-sol.toml` | Sol / runtime-recorded high | advisory readiness verdict | gate report and relay fields only |

The author cannot audit or gate its own work. Auditor and critic use separate contexts and report independently. Each lane must retain runtime evidence (identity, observed model/depth, exclusive output path, and produced artifact path). The gatekeeper does not repair work. If the runtime cannot actually run all lanes, this is `BLOCKED`, not a reduced solo experiment.

## Execution contract

1. Freeze a user-approved small slice, hashes, item count, exact schema, and output directory.
2. The author completes the full schema—not an abstention-only baseline.
3. The auditor independently verifies source evidence before seeing the author draft.
4. The critic independently challenges the author and audit after its own source sample and independent context proof.
5. The gatekeeper runs deterministic checks. It compares expected item identifiers from the frozen corpus to observed assignments; No row-count-only, percentage-only, or slice-total-only coverage result can pass. It issues only `READY-FOR-EXTERNAL-EVALUATION`, `REVISE`, or `BLOCKED`.
6. Only a ready team package is sent to external Opus for advisory evaluation.

## External-use protection

External Opus comparison defaults to one main session, one active slice, no subagent dispatch, explicit usage stop threshold, and no automatic retry. Higher concurrency requires explicit user approval for that run.

## Continuity boundary

Codex assurance lanes stop before a new slice when remaining context is 60% or less. On Codex quota exhaustion they write only to their assigned exclusive checkpoint/output path, report `HOLD — resource exhausted`, and return control without model downgrade, replacement fan-out, automatic retry, or busy-wait. The leader resumes only after a `resume audit` verifies fresh quota, frozen hashes, artifact hashes, runtime identities, exclusive ownership, no conflicting writer, and exact WIP `NEXT`. External Opus is never covered by this automatic-resume path; its one-session/one-pilot/no-automatic-continuation rule remains absolute.

## Output bundle for Opus

Each ready experiment contains only these immutable advisory artifacts:

1. `input_snapshot.json`
2. `author/<task>_draft.md`
3. `audit/<task>_evidence_audit.md`
4. `critic/<task>_adversarial_review.md`
5. `gate/<task>_gate_report.md`
6. `external/<task>_opus_evaluation_relay.md`

No bundle may modify canonicals, ledgers, corpus, official verify logs, rulings, or release state.

## Type-analysis completeness

For a type-analysis experiment, the immutable author bundle must show per-item assignment or `BLOCKED`, expected item identifiers, observed identifiers, duplicates/missing/extra result, source citations, consolidation, two or more observed variation axes per reusable type, observed traps, source-axis-labelled importance, `COMMON_TYPES` comparison, catalog disposition, and `HARVEST_LOG`/`EXTRACTION_LOG` drafts. Missing rendered evidence blocks the affected claim; it is never a reason to invent a page citation.

## 260910 사용자 우선 지침: Astra 단독 운영

현재 모델/팀 운영은 `docs/ASTRA_EXECUTION_POLICY.md`를 우선 적용한다.
`gpt-6-astra` 단독 실행; 기존 팀 발주·재개 중단; 검토·감사·맹목 풀이·최종 판정은 Astra 전용이며 Sol 참여 금지.
Astra 팀장 + Sol 비감사 보조는 성능 부족 실측 후 사용자 결정으로만 검토 가능한 미승인 대안이다.
이전 팀 필수·Sol 배정·외부 Opus 필수 서술은 현재 실행의 선행조건이 아니다.
자기검산을 독립 감사로 표시하지 않으며 독립 단계는 깨끗한 Astra 컨텍스트에서 순차 수행한다.
배포 증거·작성/감사 분리·append-only·two-key는 유지한다. 모델 지침 개정은 배포 승인이 아니다.
