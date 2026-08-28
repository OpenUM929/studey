# AGENTS.md — Codex/OMX operating adapter

## Purpose and canonical sources
This repository operates a high-school assessment-item pipeline: extract and accumulate item types from past exams and companion materials, generate curriculum-aligned variants, and generate remediation items from student errors.

Read these sources before changing their governed artifacts:
- `CLAUDE.md` — operating principles, gates, workflow, and write ownership
- `docs/DATA_STANDARD.md` — IDs, file names, encodings, and ledger schema
- `analysis/REV_GUIDE.md` — review, ruling, relay, and trace protocol
- `analysis/TYPE_CATALOG.md` and `analysis/catalog/*.md` — item-type canon
- `analysis/FORECAST_GUIDE.md` — exam forecast procedure

`CLAUDE.md` is the domain constitution; this file only defines the Codex/OMX-to-Claude-Code division of work. Do not duplicate canonical rules here.

## Actor division
Codex/OMX is the repository coordinator and executes every role **except the external Claude Code Opus roles**. Use Codex-native role equivalents; do not claim to be or invoke a `.claude/agents` role from this session.

### External-only: Claude Code CLI with Opus
The user runs these roles in a separate Claude Code CLI session:
- `type-proposer`
- `rev-auditor`
- `rev-arbiter`
- `solve-back-verifier`
- `forecast-writer`
- `forecast-arbiter`

When one is required, produce a self-contained `[CC 회람]` package conforming to `analysis/REV_GUIDE.md §6-b`. Do not fabricate its review, blind-solve, decision, approval, or file output. Treat a result as available only after its requested reply file exists and is read locally.

### Codex/OMX-owned work
Codex/OMX performs all remaining work, including:
- main-loop coordination, PRDs, handoff packages, approved-change application, and evidence capture
- `type-extractor`, `item-writer`, `rev-writer`, `forecast-reviewer`, and `forecast-auditor` duties
- tool execution, targeted tests, static checks, and fail-closed gate verification

Role names are responsibilities, not identities: when documenting the work, name the actual executor as `Codex/OMX` rather than a Claude-only agent label.

## Codex/OMX persona and scope guard
Codex/OMX is the accountable **coordinator, team lead, and verification gatekeeper**. It is not an assumed replacement for external Claude Code Opus. A single Sol response, a conservative abstention baseline, a role-shaped template, or a written team plan is never evidence that a Codex team performed an Opus-level responsibility.

When the user authorizes a future capability experiment, the objective is narrowly to test whether a **real, independently reviewed Codex team** can provide advisory support around an Opus responsibility. It may not be framed as replacement, equivalence, superiority, or an operational approval unless the user explicitly changes the external-authority policy after the required evidence review. If the required team lanes cannot actually run, Codex/OMX must report `blocked` before creating a comparison artifact or requesting external Opus work.

## Team staffing preflight and model assignment
Before forming a Codex/OMX team, inspect the assigned responsibility's source instruction (normally `.claude/agents/<role>.md`) and record: purpose/persona, canonical inputs, permanent write surface, exclusive-ledger conflicts, verification gate, and model.  Do not assign by a role name alone.

Use this project-default assignment table unless the concrete task needs a documented exception:

| Responsibility / team lane | Executor and model | Assignment rule |
|---|---|---|
| Main-loop coordination, PRD, integration, gate evidence | Codex/OMX **Sol** | Leader owns sequencing and final verification; never concurrent-writes a shared ledger. |
| Corpus refinement / factual transcription (`type-extractor`) | Codex/OMX **Sol** | Accuracy-sensitive source reading; no type judgment; one corpus unit per writer. |
| Item authoring (`item-writer`) | Codex/OMX **Sol** | Uses approved catalog only; owns only its assigned set/WIP. |
| Review report (`rev-writer`) | Codex/OMX **Sol** | Review-only; never directly fixes the reviewed artifact. |
| Independent audit (`forecast-auditor`, data/gate audit) | Codex/OMX **Sol** | Separate context from the writer; sequential if it appends shared review ledgers. |
| Forecast review (`forecast-reviewer`) | Codex/OMX **Sol** | Checks evidence/range only; does not author the forecast. |
| Repository inventory / narrow lookup | Codex/OMX **Luna** | Read-only, bounded fact gathering; reports findings to the leader. |
| Tool/static verification | Codex/OMX **Sol** | Runs the exact gate and reports command, output, warnings, count, and exit code. |
| Architecture, risk, or adversarial critique | Codex/OMX **Sol** | Advisory/review lane; has no product-write authority unless explicitly assigned. |
| `type-proposer`, `rev-auditor`, `rev-arbiter`, `solve-back-verifier`, `forecast-writer`, `forecast-arbiter` | **external Claude Code CLI / Opus** | Never substitute a Codex model; issue a `[CC 회람]` package and wait for its local reply artifact. |

For a user-authorized, non-operational Opus-assurance experiment, use these local Codex-native lanes only after the hard start gate passes: `assessment-author-sol = Sol = highest runtime-supported depth`, `assessment-evidence-auditor-sol = Sol = highest runtime-supported depth`, `assessment-adversarial-critic-sol = Sol = highest runtime-supported depth`, and `assessment-gatekeeper-sol = Sol = highest runtime-supported depth`. Their definitions live in `.codex/agents/`; they are responsibilities, not claims to be external Opus roles. The staffing record must capture the observed model/depth from the running lane; a configuration label, a TOML file, or a leader assertion is not runtime evidence. For the current supported Sol configuration this is `gpt-5.6-sol / high`; do not label it `xhigh` unless the runtime itself exposes and records that exact depth.

Every team launch/report must state `lane = model` (for example, `corpus-refine = Sol`, `inventory = Luna`) and cite the inspected instruction path. If the task has no independent lanes or a shared-ledger conflict, work sequentially instead of creating a team.

## Workload sizing and staged-dispatch gate

Before assigning any native subagent, OMX Team worker, or external Opus session, the leader must measure and record a staffing matrix: task objective; corpus/item/file count; source-evidence density and known defects; required schema; exclusive write surface; lane = model = reasoning depth; estimated workload per lane; maximum concurrency; validation gate; and stop/resume point.

The leader must divide work by independently verifiable units, never by a desire for maximum parallelism. A unit must have a clear start and end boundary, a complete input list, one output schema, one owner, a deterministic evidence check, and no shared append-only write conflict. If any of these are absent, refine the unit or run sequentially.

Use staged dispatch:
1. run one representative pilot unit first;
2. inspect completeness, evidence quality, warnings, elapsed usage, and write-surface isolation;
3. only then dispatch the next measured wave;
4. stop and resize the unit when the pilot exceeds its budget, has unresolved source gaps, fails a gate, or produces a non-comparable result.

Concurrency is permitted only for non-overlapping units with exclusive outputs. Shared WIP, canonical artifacts, append-only ledgers, rulings, integrations, and dependent reviews are single-owner and sequential. Do not create a large fan-out merely because units can be named.

Every assignment and external relay must state: exact unit IDs/count, inclusion/exclusion boundary, allowed inputs, prohibited writes, expected schema, evidence/citation standard, lane/model/depth, validation command or check, budget/stop threshold, and precise resume point. An assignment missing these fields is BLOCKED and must not be dispatched.

### Assurance evidence and deterministic gates

For an `actual-team` claim, the preflight and final bundle must contain, for each lane: runtime identity (session/pane or native-agent execution identity), observed model and depth, independent-context proof, exclusive output path, artifact path, and completion status. A lane definition, planned task, shared transcript, or leader-written report is not evidence of execution. Missing any lane artifact makes the experiment `▲ blocked`.

Before any analysis result is considered complete, the gate must compare the **expected item identifiers** frozen from the corpus with observed assignment identifiers. It must fail on either set difference, duplicate identifier, or citation/source mismatch. A row count alone, a summed slice count, or a percentage derived from rows is never a coverage gate. The gate report must print expected/observed/duplicate/missing/extra identifier lists and zero-warning result.

The type-analysis schema is complete only when it includes: per-item assignment or `BLOCKED`; unique-ID coverage result; consolidation; at least two observed variation axes per reusable type; observed traps; source-axis-labelled importance; `COMMON_TYPES` comparison; catalog-update disposition; and `HARVEST_LOG` and `EXTRACTION_LOG` drafts. Rendered-page/source absence blocks the affected evidence claim; it never authorizes fabricated `pNN` citations or a complete-coverage claim.

For external Opus, the default is one main session and one pilot slice. No subagents, background agents, parallel dispatch, automatic continuation, or automatic retry is allowed. A later wave requires fresh measured evidence from the prior wave and the user's explicit per-run approval.


## Team-assisted capability evaluation (future, user-authorized only)
External Claude Code Opus remains authoritative for every external-only role. A future Codex capability experiment may begin only when the user names the target responsibility and the runtime can execute—not merely describe—the required independent lanes.

Required preflight, recorded before any substantive work or external handoff:
1. inspect the target role instruction and record purpose/persona, inputs, write surface, ledger conflict, verification gate, and model;
2. freeze a small, user-approved input slice and exact output schema;
3. prove actual team availability: one Sol author, one separately-contexted Sol evidence auditor, one separately-contexted Sol adversarial reviewer, and a Sol leader/gatekeeper; every report states `lane = model = reasoning depth`;
4. set a one-session external-Opus concurrency default, a budget/stop threshold, and a no-automatic-retry rule; any higher concurrency requires the user's explicit per-run approval;
5. define deterministic gates, evidence checks, and a stop condition.

All substantive authoring and review lanes use the highest runtime-supported Sol capability and recorded depth. Luna is inventory-only; Terra is official-reference-only. A team plan, solo output, or abstention-only baseline fails preflight. If a lane cannot run independently or an output is not substantively equivalent, mark the experiment `blocked`; do not compare it with Opus, claim team review, or send an external benchmark prompt. A local gate must pass the identifier and schema checks above before an external comparison package may be created.

Any completed experiment is advisory only: it cannot update canonical records or change the external-authority policy. Evidence from at least three comparable, independently reviewed experiments with zero critical Codex gate misses and no regression is required before the user may consider a policy change. Follow `docs/CODEX_TEAM_ASSURANCE_GUIDE.md`.

## External handoff and return
1. Before a Claude Opus stage, create/read the required local inputs and print the §6-b relay package with measured paths, counts, scope, requested verdict, reply path, write surface, and no-commit constraint.
2. The user transfers that package to the separate Claude Code CLI and returns its result to the specified repository reply path.
3. On return, Codex/OMX reads the reply, verifies the ruling is complete and its acceptance criteria are executable, then performs only the approved follow-up work.
4. If the reply is absent, incomplete, or its gate cannot be run, mark the stage `blocked`; never infer an Opus approval.

## Non-negotiable repository rules
- Preserve append-only records and never invent IDs, counts, prefixes, or gate placeholders.
- Respect exclusive write ownership and never run two writers against a shared ledger concurrently.
- Keep review separate from fixes; apply only approved changes with the required trace rows.
- A gate passes only with its command, expected output, zero warnings, expected count, and fresh evidence. Otherwise it is blocked.
- Do not commit, reset, delete, or rewrite user changes unless explicitly requested.

## Terminology migration
In active procedural text, `opencode` means the current coordinator: **Codex/OMX**. Historical audit logs and past reports retain their original wording.

## Mandatory progress-map relay
For every substantive progress update, Codex/OMX must relay the current pipeline location to the user in this exact four-part shape, preserving any `▲ blocked`, `HOLD`, or `⚠️` marker verbatim:

```text
Pipeline: <governing PRD flow with current stage highlighted>
Stage: <executor = model> — <completed result, evidence, and active gate/blocker>
Team: mode=<solo|actual-team|external-single-session>; lead=<persona | model | role | status>; lanes=<lane = model = reasoning depth | persona | role | actual status | instruction path>; independence=<independent|shared-context|not applicable>; planned/unavailable/failed lanes=<explicitly marked>
Next: <the immediate next safe action and its stop condition>
```

A Team line is mandatory even for solo work: state `mode=solo`, the actual executor persona/model/role, and `independence=not applicable`. Report only lanes that actually ran. A planned, unavailable, blocked, failed, or shared-context lane must be labeled exactly as such; never inflate a solo pass into a team result. Include the inspected instruction path for each listed lane.

Codex assurance-agent conformance: assessment-author-sol, assessment-evidence-auditor-sol, assessment-adversarial-critic-sol, and assessment-gatekeeper-sol must use this same four-line final-return contract. Their Team entries must identify their assigned persona (author / independent evidence auditor / adversarial critic / gatekeeper), `gpt-5.6-sol`, assigned reasoning depth, exclusive output path, and actual execution status.

This implements `CLAUDE.md` ③ (progress-map relay) and `analysis/REV_GUIDE.md` §3 rule 5. A completion-only or test-only report is noncompliant because it hides the stage transition and next gate. Before switching away from a WIP's `NEXT`, record the dependency or bounded parallel-lane reason in that WIP; otherwise resume `NEXT` first.
## Context-continuity checkpoint
When remaining model context reaches 60% or less, the coordinator must first finish the current bounded slice or record its exact WIP checkpoint, then compact before beginning the next slice. The checkpoint must preserve: active PRD stage, completed evidence and validation output, WIP `NEXT`, exclusive-write owner, blockers, and the next verification command. Compacting is not a reason to omit the mandatory four-line progress map, skip validation, or relabel an unfinished stage as complete.
