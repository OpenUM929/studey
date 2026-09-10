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
- `item-quality-auditor`
- `forecast-writer`
- `forecast-arbiter`

When one is required, produce a self-contained `[CC 회람]` package conforming to `analysis/REV_GUIDE.md §6-b`. Do not fabricate its review, blind-solve, decision, approval, or file output. Treat a result as available only after its requested reply file exists and is read locally.

### Codex/OMX-owned work
Codex/OMX performs all remaining work, including:
- main-loop coordination, PRDs, handoff packages, approved-change application, and evidence capture
- `type-extractor`, `item-writer`, `rev-writer`, `forecast-reviewer`, `forecast-auditor`, and `set-release-manager` duties
- tool execution, targeted tests, static checks, and fail-closed gate verification

Role names are responsibilities, not identities: when documenting the work, name the actual executor as `Codex/OMX` rather than a Claude-only agent label.

**`set-release-manager` 특칙 (260908 신설).** 이 배우는 승인분을 **반영**하는 단계라 Codex/OMX
소유지만, 그 입력인 맹목 풀이·품질감사·arbiter 판정은 **외부 Opus 소유**다. 따라서 이 배우를
돌릴 때 그 게이트 결과를 **자기 계산으로 대체하거나 추정하지 않는다** — 회신 파일이 로컬에
존재하고 읽힌 뒤에만 통과로 취급한다. 세트 전수 커버리지가 안 되면 `▲ blocked`이고,
「배포가능」 표기는 그 커버리지 실측(원본 N · 외부 검증 M 병기) 없이는 쓸 수 없다.
정의는 `.claude/agents/set-release-manager.md`, 권한 경계는 `analysis/REV_GUIDE.md` §5.

## Codex/OMX persona and scope guard
Codex/OMX is the accountable **coordinator, team lead, and verification gatekeeper**. It is not an assumed replacement for external Claude Code Opus. A single Sol response, a conservative abstention baseline, a role-shaped template, or a written team plan is never evidence that a Codex team performed an Opus-level responsibility.

When the user authorizes a future capability experiment, the objective is narrowly to test whether a **real, independently reviewed Codex team** can provide advisory support around an Opus responsibility. It may not be framed as replacement, equivalence, superiority, or an operational approval unless the user explicitly changes the external-authority policy after the required evidence review. If the required team lanes cannot actually run, Codex/OMX must report `blocked` before creating a comparison artifact or requesting external Opus work.

## Team staffing preflight and model assignment
Before forming a Codex/OMX team, inspect the assigned responsibility's source instruction (normally `.claude/agents/<role>.md`) and record: purpose/persona, canonical inputs, permanent write surface, exclusive-ledger conflicts, verification gate, and model.  Do not assign by a role name alone.

Use this project-default assignment table unless the concrete task needs a documented exception:

| Responsibility / team lane | Executor and model | Assignment rule |
|---|---|---|
| Main-loop coordination, PRD, integration, gate evidence | Codex/OMX **Sol** | Leader owns sequencing and final verification; never concurrent-writes a shared ledger. |
| Corpus refinement / factual transcription (`type-extractor`) | Codex/OMX **Sol** | **1차 정제 전담 — 전사만, 분류 아님**: HWP/DOC→PDF화→`PyMuPDF` 이미지(`corpus/_images/<ID>/pNN.png`)→`transcript.md`(도표 문항 이미지 링크 포함, 인용 산문 지문은 P-지문 예외 `corpus/_README.md` §2-a)→`verify_log.tsv`/`meta.yml` 채움. **분류 판단 금지 — 유형ID·변형축·함정 한 글자도 적지 않는다. 산출물은 `corpus/<ID>/`에만 둔다.** Gate: `transcript.md`+`_images`+`verify_log`+`meta.yml` 4필드 완성 전 **1차 분류 진입 금지**(one corpus unit per writer). **1차 정제 ≠ 1차 분류 — 정제물은 분류의 입력일 뿐 분류가 아니다.** |
| Item authoring (`item-writer`) | Codex/OMX **Sol** | Uses approved catalog only; owns only its assigned set/WIP. |
| Review report (`rev-writer`) | Codex/OMX **Sol** | Review-only; never directly fixes the reviewed artifact. |
| Independent audit (`forecast-auditor`, data/gate audit) | Codex/OMX **Sol** | Separate context from the writer; sequential if it appends shared review ledgers. |
| Forecast review (`forecast-reviewer`) | Codex/OMX **Sol** | Checks evidence/range only; does not author the forecast. |
| Repository inventory / narrow lookup | Codex/OMX **Luna** | Read-only, bounded fact gathering; reports findings to the leader. |
| Tool/static verification | Codex/OMX **Sol** | Runs the exact gate and reports command, output, warnings, count, and exit code. |
| Architecture, risk, or adversarial critique | Codex/OMX **Sol** | Advisory/review lane; has no product-write authority unless explicitly assigned. |
| 1차 분류 / type proposal (`type-proposer`) + 독립 검증·판정(`rev-auditor`, `rev-arbiter`, `solve-back-verifier`, `item-quality-auditor`, `forecast-writer`, `forecast-arbiter`) | **external Claude Code CLI / Opus** | **1차 분류는 외부 Opus 전담 — 분류는 1차 정제물(`transcript.md`+`pNN.png`)을 다시 읽어 한 문항씩 유형에 배정하는 작업이며, 카탈로그 `출제 빈도`를 옮겨 적는 것은 분류가 아니다.** Never substitute a Codex model; issue a `[CC 회람]` package and wait for its local reply artifact. |

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

**Dispatch gate (260901; mirrors CLAUDE.md 공통 실행 규격 ⑥).** Delegating to any subagent, worker, or external session requires (i) the user's **explicit** instruction and (ii) a **measured** remaining-budget check recorded in the dispatch order itself. A generic "go ahead / 진행해줘 / continue / ok / ." **is** an execution approval and does cover dispatch — it means "check the budget and, if it is sufficient, start now." Do not spend a user turn asking again; that is waste too. The sequence is: measure the budget, dispatch immediately if it passes, otherwise switch to one of the fallbacks below and say so in one line. Ask only when the budget fails **and** both fallbacks are closed (e.g. 원칙 8 forbids editing the target directly). The 260901 incident was caused by skipping the budget check, not by reading a short approval as consent — narrowing the reading of approval would burden the user without touching the actual cause. This budget check is a **dispatch-only gate**: it is not applied to work the leader performs directly, because direct work keeps its context and WIP and can simply be resumed, and slice checkpoints already cover interruption — the cost is charged only where a termination can destroy the whole result. If the budget cannot be measured, treat it as **insufficient** (fail-closed), and take one of two paths instead of dispatching: (1) **do it directly** after reading that actor's own definition file so its persona, scope guard, write surface, and prohibitions are honoured — without borrowing its tier label — or (2) **dispatch one bounded slice at a time**, verifying each artifact by measurement before issuing the next, so a mid-run termination cannot destroy completed work. After any dispatch, the leader verifies the artifacts by grep/hash before reporting: a lost reply is not lost work, and a delivered reply is not proof of completion. Evidence: 260901, a dispatch made without re-checking a session that had already hit a rate limit; the agent finished its work and then died mid-reply, consuming the session's remaining subagent quota.


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
- Keep the ruler separate from the work (CLAUDE.md 원칙 12). Acceptance criteria, expected-identifier tables, and gate code are **consumed, never revised**, by the lane they measure. An unsatisfiable or self-contradictory criterion is a decision request to the user/`rev-arbiter`, never something to route around with placeholder rows. Expected-value tables are regenerated from the source by code and re-derived on every gate run; editing one by hand converts it from a ruler into an artifact. Any ruler change needs a second key — an audit-authority re-freeze row — and invalidates every verdict issued under the old ruler until re-measured.
- **Which files are the ruler is not a judgement call for the executing lane.** The canonical two-key subject list lives in `analysis/REV_GUIDE.md` §5 — read it there and do not re-enumerate it here (CLAUDE.md 원칙 9-c-ii); a copied list drifts from the original. The Codex/OMX lane **consumes those files read-only**, including the read-only regenerator: what that tool lets through becomes the ruler's content, so being unable to edit the ruler is no protection if the lane can edit the thing that measures it. Adding an entry to the regenerator's allowlist is itself a ruler change. Any change to a listed file arrives through the `[Codex/OMX 지시]` block after both keys (user approval + `rev-arbiter` ruling) and lands with a bytes + sha256(16) re-freeze row in the ledger.
- **Label the actor you actually are.** When the main loop performs work directly under the §5 stand-in row, the artifact is `proposal` grade and carries `author: 메인 루프` — never another actor's tier label (`t1`/`t2`/`binding`). The same holds in reverse: Codex/OMX output is labelled as the Codex/OMX lane, not as the Claude Code lane that ordered it.
- **Types and trends are the objective function; bare numbers are incidental** (CLAUDE.md 원칙 13, 260910). Transcribe every printed value as-is, but grade the *effort and the blocking condition*: stem-demanded action, stimulus presentation, **formula structure and notation**, `<조건>` boxes, choice structure, shared-stimulus grouping, score band, unit cues and trap wording must be exact — illegibility there is `▲ blocked`. A single coefficient, coordinate, or table cell is not type information: log it `unreadable`/`observed` and keep going, and never adjudicate whether it is a misprint. The exception is a number the item is built around (special angle, integer root, perfect-square discriminant), which is type information. Score-sum and item-count checks remain **omission detectors** (원칙 11-a) and this rule never reinterprets a ruler's acceptance criteria (원칙 12-a).
- A gate passes only with its command, expected output, zero warnings, expected count, and fresh evidence. Otherwise it is blocked. The ruler gate itself is `analysis/REV_GUIDE.md` §5-a and runs automatically inside `tools/check_assurance_contract.py` structural check 6.
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
## 문제 정본 저장·인덱스 동기화 (260908)

문항을 생성·교체·수정하면 `CLAUDE.md`의 「문제 완성본 관리」와
`analysis/DOC_LOCATION.md` §3-1을 적용한다. 최종 게이트 통과 후 기존 output 날짜별 저장소의
정본·별도 문제지·답지/해설과 `output/_index.md`를 같은 작업에서 갱신하고 감사 이력을 남긴다.
미검증 문항은 `검토필요`로 기록하며 작성자 자기검산을 외부 Opus 독립검증으로 표시하지 않는다.
문제 작성만으로 완료 선언하지 않는다. 기존 N축 예외와 two-key·write surface는 그대로 유지한다.

## Context-continuity checkpoint
When remaining model context reaches 60% or less, the coordinator must not begin another slice. It first finishes the current bounded slice or records its exact WIP checkpoint, writes the same state through `omx state write` and `omx notepad notepad_write_working` when those runtime surfaces are available, then compacts before the next slice. The checkpoint must preserve: active PRD stage, completed evidence and validation output, immutable input/artifact hashes, WIP `NEXT`, exclusive-write owner, blockers, and the next verification command. If an explicit context meter or compaction command is unavailable, checkpoint after the bounded slice and allow the host's compaction/continuation mechanism; do not claim that compaction was manually executed. Compacting is not a reason to omit the mandatory four-line progress map, skip validation, or relabel an unfinished stage as complete.

## Usage-quota continuity and resume

For Codex/OMX-owned work, a model usage/session quota or rate-limit reset notice is a resource boundary, not a reason to downgrade the assigned model, fan out retries, or discard work. Finish only the already-started bounded slice when safe, then create a **resource-exhaustion checkpoint** containing the same fields above plus the observed reset time, lane runtime identities, completed unit identifiers, exclusive output paths, and the exact resume command. Mark the WIP and progress map `HOLD — resource exhausted`, stop new model submissions, and never busy-wait or repeatedly poll the service.

If the host can safely retain the run or schedule one continuation, wait until the reported reset time and perform exactly one **resume audit** before continuing. If the host cannot remain alive or schedule a wake-up, end the current turn without asking the user to restate or reapprove ordinary work; the next automatic or user continuation must begin with the same resume audit and continue from WIP `NEXT`, never redo completed slices. The resume audit verifies fresh quota availability, frozen input hashes, produced artifact hashes, exclusive-write ownership, no conflicting active writer, and the next validation command. Any mismatch is `▲ blocked`.

This automatic-resume rule applies only to Codex/OMX-owned execution. External Claude Code Opus remains one main session and one pilot slice with no background agents, automatic continuation, or automatic retry; a later external run still requires the measured prior result and the user's explicit per-run approval.

## 동반 갱신 목록 (CLAUDE.md 원칙 10)
이 문서를 개정하면 **같은 작업에서** 아래를 함께 점검한다. 한쪽만 고치면
"규정은 있는데 아무도 안 지키는" 구멍이 생긴다.

- `CLAUDE.md`(같은 규정의 Claude Code 측 서술) · `tools/check_assurance_contract.py` TEXT_REQUIREMENTS · `tools/sync_global_continuity_guidance.py` · `README.md`

목록 자체의 존재는 `tools/check_assurance_contract.py`가 검사한다.
근거: 260828 시스템 감사 S3 — 원칙 10이 8개 정본 중 1개에만 구현돼 있었다.

 ## 사용자 승인: Opus 불가 시 Astra 대체 특칙

  이 특칙은 이 문서의 기존 외부 Opus 전용 규정, 모델 배정표,
  대체 금지 및 비운영 실험 한정 규정보다 우선한다.

  - 1차 분류(type-proposer)는 이미지화까지는 terra 모델을 사용한다. 
    Opus를 사용할 수 없으면 해당 분류 단계를 terran로 수행한다.
  - Opus를 사용할 수 없는 경우, 1차 분류를 제외한 작업·맹목 풀이·
    품질감사·독립 검토·최종 판정은 Codex 네이티브 서브에이전트로
    수행할 수 있다.
  - 이 대체 경로의 모든 서브에이전트와 작업자 모델은 gpt-6-astra로
    명시한다. 해당 모델을 실행할 수 없으면 다른 모델로 몰래 대체하지 않는다.
  - 작성자·독립 감사자·판정자는 서로 다른 실행 컨텍스트로 분리한다.
    맹목 풀이에는 문제와 허용 참고자료만 제공하고 정답·기존 해설·
    작성자 결론은 전달하지 않는다.
  - 별도 컨텍스트는 파일 접근 격리 자체를 보장하지 않으므로,
    허용 입력과 금지 입력을 명시하고 실제 읽은 자료를 기록한다.
  - 실제 실행 모델, 입력 및 산출물 해시, 문항 식별자 전수 커버리지,
    감사 결과와 수정 후 재검증을 기록한다.
  - 작성자 자기검산을 독립 감사로 표시하지 않는다.
  - 기존 검증 기준, append-only, 작성·감사 분리 및 two-key 절차는 유지한다.
    대체된 감사·판정 역할도 같은 절차를 따른다.
  - 이 특칙 적용을 위해 CLAUDE.md, analysis/REV_GUIDE.md,
    관련 역할 정의와 검사 규칙의 충돌 부분을 함께 개정한다.

## 260910 사용자 우선 지침: Astra 단독 운영

현재 모델/팀 운영은 `docs/ASTRA_EXECUTION_POLICY.md`를 우선 적용한다.
`gpt-6-astra` 단독 실행; 기존 팀 발주·재개 중단; 검토·감사·맹목 풀이·최종 판정은 Astra 전용이며 Sol 참여 금지.
Astra 팀장 + Sol 비감사 보조는 성능 부족 실측 후 사용자 결정으로만 검토 가능한 미승인 대안이다.
이전 팀 필수·Sol 배정·외부 Opus 필수 서술은 현재 실행의 선행조건이 아니다.
자기검산을 독립 감사로 표시하지 않으며 독립 단계는 깨끗한 Astra 컨텍스트에서 순차 수행한다.
배포 증거·작성/감사 분리·append-only·two-key는 유지한다. 모델 지침 개정은 배포 승인이 아니다.
