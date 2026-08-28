# Codex team assurance runbook

## Purpose and non-authority

This runbook governs a future, user-authorized experiment in which a real Codex/OMX team provides advisory analysis around an external Claude Code Opus responsibility. It does not assume that Sol equals, exceeds, or replaces Opus. External Opus remains the operational authorizer, reviewer, and release gatekeeper.

## Persona contract

- **Coordinator / leader = Sol:** protects scope, budget, write ownership, and stop conditions; never presents a plan as completed team work.
- **Author = Sol:** performs the same substantive, bounded deliverable required by the experiment.
- **Evidence auditor = Sol:** independently checks sources, counts, citations, and unsupported claims; it does not repair the author output.
- **Adversarial reviewer = Sol:** searches for omissions, invalid consolidation, scope errors, and false confidence; it does not repair the author output.
- **Gatekeeper = Sol:** integrates only verified findings and may declare `blocked`, never an external-role approval.
- **Luna:** read-only inventory only. **Terra:** official-reference gathering only. Neither may author, score, or decide the experiment.

Every substantive lane uses the highest runtime-supported Sol capability and records the observed model/depth. Each report states `lane = model = reasoning depth`, runtime identity, exclusive output path, produced artifact path, and the role-instruction path inspected before assignment. A configured value or role TOML alone is not runtime identity.

## Hard start gate

Start only after all conditions hold:

1. The user has named the target responsibility and approved a small input slice.
2. The leader has frozen the inputs, hashes, required output schema, and measured item count.
3. The runtime can execute all three independent substantive lanes. A document, prompt, or simulated result is not a lane.
4. Each lane has an exclusive write surface; shared WIP and append-only ledgers have one owner.
5. The external Opus side, if used, has one main session and one pilot slice by default, an explicit budget/stop threshold, no automatic retry, and no parallel dispatch unless the user explicitly approves that run.
6. The deterministic gate has an expected item identifiers list frozen from the corpus and a complete type-analysis schema.

If any condition fails, record `blocked` and do not create a comparison output or external benchmark request.

## Experiment sequence

1. **Freeze** — verify hashes, paths, item count, and schema.
2. **Author** — Sol produces the full substantive result for the approved slice.
3. **Evidence audit** — independent Sol lane validates every material source claim and deterministic gate.
4. **Adversarial review** — independent Sol lane records defects, uncertainty, and required exclusions.
5. **Gate** — leader verifies runtime identity and produced artifacts for author/audit/review, then compares expected item identifiers with observed assignments. No row-count-only, slice-total, or percentage-only check can pass coverage. Missing, duplicate, extra, or unsupported identifiers block the run.
6. **Optional external comparison** — only after the above gate passes, request an external Opus result for the same slice and schema. Compare advisory outputs without changing canonicals.
7. **Stop** — one result never establishes substitution. Retain the external-authority rule until the user explicitly changes it after at least three comparable, independently reviewed experiments.

## Prohibited shortcuts

- No solo Sol baseline may be labelled a team result.
- No abstention-only result may be compared as equivalent to a substantive result.
- No external Opus role is dispatched merely to compensate for missing Codex team capability.
- No parallel external dispatch, automatic retry, invented citation, invented identifier, canonical edit, ledger append, or release decision occurs in an experiment.
- No missing rendered/source evidence is converted into a fabricated page citation or a complete result. Affected items are `BLOCKED`.

## Context, quota, and resume gate

No lane begins a new bounded slice when remaining context is 60% or less. The lane finishes only its current safe slice or writes an exclusive checkpoint; the leader then records the active stage, frozen input and produced-artifact hashes, completed identifiers, validation output, exclusive owner, blocker, exact `NEXT`, and next validation command before compaction.

When a Codex/OMX usage/session quota or rate limit is exhausted, each affected lane writes a **resource-exhaustion checkpoint**, reports `HOLD — resource exhausted`, and stops new submissions. It must not switch to a weaker model, launch replacement workers, automatically retry, or busy-wait. If the host exposes a reset time and can retain or schedule the run, the leader permits one continuation after that time. Otherwise the next continuation starts without redoing completed slices.

Every continuation begins with a **resume audit**: verify fresh quota, frozen input hashes, artifact hashes, runtime identities, exclusive-write ownership, absence of a conflicting writer, WIP `NEXT`, and the next deterministic validation command. Any mismatch is `BLOCKED`. This section does not relax the external Opus rule: external work never auto-continues or auto-retries and remains one main session plus one pilot slice per approved run.

## Type-analysis acceptance schema

The author draft and the gate input must include all of the following: per-item assignment or `BLOCKED`; expected item identifiers; observed identifiers; duplicate/missing/extra identifier results; source citations; consolidation; at least two observed variation axes per reusable type; observed traps; source-axis-labelled importance; `COMMON_TYPES` comparison; catalog-update disposition; and `HARVEST_LOG`/`EXTRACTION_LOG` drafts. The auditor verifies every material claim; the critic challenges the semantic grouping and student-facing generation risk. Any missing field is `BLOCKED`, not a prose-quality warning.
