# REV GUIDE — three-tier review protocol & report spec (canonical)

> Defines how deliverables are reviewed when issues or doubts are found: a **three-tier
> loop** that raises completeness round by round and closes with a binding external
> ruling. Reports are self-contained — an AI with zero project context can judge from one file.
> Language policy (260825): new/updated content is English-first; Korean survives only in
> legacy text, proper nouns, and existing filenames.

## 0. Absolute rule — no-fix interference (highest priority)

- **A reviewer (human or agent) never directly modifies a document it did not author.**
- Defects found in someone else's artifact go into `<proposed_fixes>` as **checkbox
  requests** (`- [ ]`). Approved items only are applied later **by the authoring owner**
  (type-extractor definition / item-writer / user).
- A reviewer editing the original is a process violation.

## 1. Location · naming · handoff ledger

| Item | Rule |
|------|------|
| Folder | Deliverables inside `output/` → `output/<YYMMDD>/rev/` · everything else (catalogs, guides, corpus, system web/tools) → `analysis/rev/`. One-line test: *target inside `output/` ⇒ its-round rev/, otherwise always `analysis/rev/`* (details: `DOC_LOCATION.md` §2) |
| Report name | `YYMMDD_NN_NAME.md` — date / daily sequence per home / English snake-case NAME |
| Tier-2 report | `YYMMDD_NN_NAME_second.md` |
| Decision request | `YYMMDD_NN_NAME_decision.md` (§6) |
| Ruling | `YYMMDD_NN_NAME_ruling.md` (written by tier-3 only) |
| Entry list | each rev home keeps `HISTORY.md` (static registry of reports) |
| **Handoff ledger** | each rev home keeps **`_index.md`** (LIVE round state — the single shared touchpoint between tiers; form below) |
| Global log | `analysis/REV_LOG.md` (append-only) |

### `_index.md` standard form (append-only rows)

```markdown
# Review handoff ledger — <home>

state: in-round | round: N | waiting: t1 | overall: in progress
<!-- state: in-progress | converged | submitted | approved | revise-required | rejected -->

| date | R | reviewer | target | issue summary | detail doc | reflect_state | next action |
|------|---|----------|--------|---------------|------------|----------------|-------------|
| 260825 | 1 | t1 | transcript.md | 3 type assignments disputed | 260825_02_types.md | flagged | owner-fix then t2 cross-check |

Rules: rows append-only · reflect_state: `flagged`→`fixed`→`re-verified` ·
consecutive clean rows from BOTH tiers ⇒ set header state `converged` ·
same issue re-raised twice ⇒ next action `escalate` immediately.
```

Division of labor: `HISTORY.md` = static list of documents; `_index.md` = living round
state and inter-tier messages.

## 2. Review report structure (order matters)

```markdown
---
title: "<review title>"
source: <target path>
source_location: "<where>"
created: <YYYY-MM-DD>
author: <writer>
status: pending | in-round | converged | submitted | approved | revise-required | rejected | closed
reviewer: <reply author or unset>
---

# Review NN — <title>

<document>        ← faithful excerpts of the item/solution under review + source metadata
</document>

<context>         ← 3–5 sentences of background an outsider lacks (school, curriculum, catalogs)
</context>

<findings>        ← verified facts + computation process (code/recheck included). No suspicions
</findings>

<questions>       ← numbered questions that force a direction
</questions>

<proposed_fixes>  ← fix proposals as checkbox approval requests (- [ ])  (see §0)
</proposed_fixes>

<output_format>   ← lock the reply format: | question | verdict | evidence | proposal |
</output_format>

## history         ← append-only: date · change. Never rewrite history (principle 3)
```

Tier-2 (`*_second.md`) replaces `<findings>` with `<my_findings>` (independent check,
done before reading tier-1) plus a `<cross_judgment>` table:
`| tier-1 point | my verdict | evidence | agree/disagree |`.

### §2-b Per-target review criteria

**A. Problem sets** (`output/<YYMMDD>/*.md`)
recomputation via python·sympy (mandatory) · answer uniqueness · condition sufficiency /
contradiction / redundancy · scope guard (`curriculum_2022.md` 🚧) · notation conventions ·
within-set duplication · solution middle-step recomputation · descriptive-item grading-criteria coverage.

**B. Refined corpus artifacts** (`corpus/<ID>/transcript.md · meta.yml · verify_log.tsv`)
transcription fidelity vs `corpus/_images/<ID>/pNN.png` (coefficients/coordinates byte-equal) ·
item-count match (transcript ↔ meta.yml) · every cited evidence page exists ·
correct `[unreadable]` handling · forecast metadata completeness (grade citation,
per-item point values, counted verb-form endings).

**C. Proposal documents** (`output/<YYMMDD>/*_type_analysis.md · *_catalog_update.md` —
type-proposer output)
per-item assignment traceable to transcript lines + page evidence · consolidation validity
(5–12 types, no over-splitting) · variation-axis completeness (≥2 real axes per type) ·
new-entry drafts exactly match the `catalog/_README` template · proposed IDs legal under
CODE_REGISTRY (prefix collision check, F-scope notation like `한국사:F-03`) ·
duplicate-semantics check against existing catalog types · importance-star evidence
citations · scope-guard marks on 🚧-touching types · verify_log classify/merge/grade rows
present with actor `type-proposer`.

**D. System code** (`web/*.js` · `tools/*.py` · 파서·내보내기·집계 배관) — 260826 신설

> 신설 사유: 260825 판정 07 반영분에서 결함 3건(CRLF로 프론트매터 전량 파싱 실패 ·
> 5지선다 선택지 전 과목 실패 · 내보내기 TypeError)이 **t1→t2→t3 3단계를 모두 통과**했다.
> 원인은 라운드 부족이 아니라 **A~C에 코드 대상 기준이 없어 전원이 정적 검토만 한 것**이다
> (t2 자기 기록: "Live node run NOT repeated — static chain deemed sufficient").
> 라운드 반복은 이 구멍을 메우지 못하므로 실행 검증을 규격으로 못박는다.

- **실행 검증 필수** — 코드 대상 검토는 **실제로 돌린 결과**로만 clean을 선언한다.
  정규식을 눈으로 읽고 내린 판단은 근거가 아니다(위 3건이 전부 그렇게 통과했다).
- **변경세트 1:1 커버리지** — 판정이 CB1·CB2·CB3처럼 여러 변경세트를 승인하면
  **각 변경세트마다 실행 케이스 1건 이상**을 둔다. 한 세트의 통과가 다른 세트를 대변하지 않는다.
- **계약 층위별 검사** — 문항 단위 카운트만 세지 말고 최소 세 층을 각각 확인한다:
  ① 항목 층(문항 수·태그 슬롯) ② **세트 메타 층**(set_id·subject·scope_confirmed 등
  frontmatter 계약) ③ **출력 층**(내보내기·저장 산출물을 실제로 생성해 스키마와 대조).
- **입력 다양성** — 대표 입력 1건으로 끝내지 않는다. 대상 기능이 과목·형식에 따라 갈리면
  **갈리는 쪽마다** 입력을 댄다(예: 서답형 100% 세트만 검사하면 5지선다 경로가 통째로 미검).
  개행 코드(CRLF/LF)·인코딩·빈 값·경계 입력을 포함한다.
- **미러 구현 대조** — 같은 로직의 복수 구현(`parser.js` ⇄ `md2quiz.py`)이 있으면
  동일 입력으로 **전 필드**를 비교한다. 일부 카운트 일치를 "동작 동일"로 보고하지 않는다.
- **환경 부재 시** — 실행할 수 없으면 clean이 아니라 `▲ blocked + 사유`로 기록하고
  실행 가능한 주체에게 넘긴다. **정적 검토로 대체 선언하는 것을 금지한다.**

**E. Operating plans · PRDs** (`output/<YYMMDD>/*_prd.md` · roadmaps · cycle plans) — 260826 신설

> 신설 사유: 260826 Cycle-0 PRD 게이트에서 tier-3가 새로 찾은 차단 결함 4건(BF1~BF4)은 모두
> **PRD를 이웃 정본과 1:1로 대조했으면 t1·t2가 잡았을 것**들이었다(CLAUDE.md L60,
> `catalog/_README` L43~45, 도구 소스, DATA_STANDARD §5.1). §2-b가 A~D만 규정해
> 계획 문서에 적용할 기준이 없었고, 그 결과 검토가 표면(오탈자·카운트)에 머물렀다.
> §2-b D 신설과 **같은 종류의 구멍**이므로 같은 방식으로 규격화한다.

- **이웃 정본 1:1 대조 (필수)** — 계획의 각 단계에 대해 *그 단계를 규정하는 정본 조항*을 찾아
  **표로 대조**한다: `단계 | 정본 근거(파일·행) | 계획이 적은 산출물 | 정본이 요구하는 산출물 | 일치?`.
  근거 조항을 찾지 못한 단계는 clean이 아니라 **미근거로 표시**한다. 대조 없이 내린 clean은 무효다.
- **판정 가능한 게이트** — 각 게이트의 수용기준이 **판정 가능한가**를 본다. "⚠ 마킹한다",
  "문자수가 급감하면" 같은 문구는 임계값·조치가 없으면 판정 불가 → 결함. 수치 임계와
  임계 초과 시 조치를 요구한다(§3 rule 4-a의 수용기준 규격 준용).
- **비가역 산출물 식별 (필수)** — 계획이 만드는 것 중 **되돌릴 수 없는 것**을 전부 열거하게 한다:
  비가역 식별자(코퍼스ID·유형ID·접두어·subject_code)·append-only 원장 행·삭제 불가 로그.
  각각에 대해 "확정 시점이 언제이고, 그 전에 어떤 정책 결정이 끝나 있어야 하는가"를 확인한다
  (CLAUDE.md 원칙 9). 정책 미결인 채 확정 시점을 지나는 단계 = **차단 결함**.
- **도구 의존 게이트는 §2-b D를 적용** — 계획이 `tools/*.py`·`web/*.js` 실행을 게이트로 쓰면
  그 게이트는 코드 대상이다. exit code 단독 기준은 거부하고 `명령 + 기대 출력 + 경고 0줄 + 기대 카운트`를
  요구한다(CLAUDE.md 원칙 11). 도구가 하드코딩 목록을 갖고 있으면 **계획이 그 목록의 갱신을 포함하는지** 확인한다.
- **동반 갱신 커버리지** — 계획이 정본 1건을 고친다고 적으면, 그 정본을 참조하는 문서·에이전트 정의·
  도구 코드가 같은 반영 목록에 있는지 본다(CLAUDE.md 원칙 10 / CODE_REGISTRY §6).
- **실데이터 보호** — 계획에 시뮬·데모·테스트 실행이 있으면 샌드박스 경로와 무손상 증거(해시)를
  요구한다. "표식을 달아 구분한다"는 방어는 append-only 원장에서 **성립하지 않는다**.

> **동반 갱신 목록 (§2-b 개정 시 함께 고칠 것)** — 본 §2-b의 기준 목록을 늘리거나 고치면
> 같은 작업에서 `.claude/agents/rev-writer.md`·`rev-auditor.md`·`rev-arbiter.md`의 검토 절차
> 항목을 함께 갱신한다. 정본만 고치고 에이전트 정의를 두면 아무도 새 기준을 적용하지 않는다
> (실증: D 신설 후 두 정의의 목록이 A·B·C에 머물렀다). CLAUDE.md 원칙 10.

### Operating thresholds
- Individual file: math error, scope violation, answer mismatch.
- Bundled file: minor notation/formatting issues.

## 3. Three-tier round protocol

```
[Codex/OMX]  refine: type-extractor (pure transcription — runs BEFORE proposing)
[claude code] create/propose (Opus, authoring owner of this thread):
              type-proposer → output/<YYMMDD>/ proposals | item-writer → problem sets
[Codex/OMX]  main loop = coordinator (drives rounds, applies approved fixes)
   tier-1 rev-writer ⇄ tier-2 rev-auditor      (via _index.md rows)
        ├─ defect found → owner fixes (trace row: verify_log corrected / new REV_LOG row) → re-review
        ├─ same issue twice → escalate to tier-3 immediately
        └─ max 5 rounds → submit unresolved disputes anyway
[claude code] tier-3 rev-arbiter (Opus, same repo): approve | revise-required | reject
   approve → coordinator applies → closed    revise-required → back to in-round
   reject → close with reasons
```

Status flow:

```
pending → in-round ⇄ (fix cycles) → converged → submitted → approved → closed
                                          └→ revise-required → in-round
                                          └→ rejected → closed
```

Round rules:
1. One round = one tier's pass over current artifact state, recorded as `_index.md` rows.
2. Closure requires **two consecutive clean rounds from both tiers**, then either the
   user's declaration or a tier-3 `approved` ruling. Agents cannot self-declare convergence.
3. Escalation triggers: round cap reached OR identical dispute repeated twice.
4. Every owner-applied fix leaves an append-only trace (verify_log `corrected` row or a
   new REV_LOG row) — silent rewrites are forbidden.
4-a. **수용기준 규격 (코드 대상 판정, 260826 의무화).** tier-3 판정이 코드 변경을 승인할 때
   제시하는 수용기준은 다음을 만족해야 하며, 미달인 판정은 반영 주체가 **되돌려 보완을
   요구한다**(수용기준이 부실하면 반영은 통과하는데 결함은 남는다 — 260826 실증).
   - 승인한 **변경세트마다** 실행 명령과 기대값을 적는다(§2-b D의 1:1 커버리지).
   - 명령은 **복붙 실행 가능**해야 하고, 기대값은 눈으로 대조 가능한 구체적 수치·문자열이다.
   - §2-b D의 **세 층**(항목·세트 메타·출력)을 모두 덮는지 자기점검한다. 못 덮는 층이 있으면
     그 사실을 판정서에 명시한다 — 침묵은 "덮었다"로 읽히므로 금지.
   - 반영 주체는 수용기준을 **재실행**해 통과를 확인하고, 결과를 반영 보고서에 그대로 싣는다.
5. **Progress maps** (260825): every sub-agent return OPENS with the canonical stage
   diagram of its pipeline, current stage marked `▲`, then stage facts, then results:
   - extraction `[refine]▶[propose]▶[review t1⇄t2 ≤5R]▶[arbiter]▶[apply]`
   - authoring `[create]▶[pre-gate solve-back]▶[practice: t1 | exam: t1⇄t2]▶[arbiter]▶[release]`
   - forecast `[scope-fix]▶[grading A~E]▶[report]▶[review: t1 confirmed | t1⇄t2 ≤5R + arbiter on dispute, unconfirmed]▶[handoff]`
   The user must see position + outcome at a glance; blocked runs mark `▲ blocked + reason`.

### §3-b Pipeline mappings (260825)

**Extraction–analysis**: refine (Codex/OMX, `type-extractor`) → propose (Claude Code,
`type-proposer` writes `output/<YYMMDD>/` proposals per §2-b C) → t1⇄t2 rounds on those
proposals → arbiter ruling → coordinator applies approved changes to canonicals
(catalogs · HARVEST_LOG · EXTRACTION_LOG) with trace rows.

**Authoring**: `item-writer` creates a set recording `intended_use: practice|exam`
(DATA_STANDARD §5.8) → **pre-gate**: `solve-back-verifier` blind-solves EVERY set
(mandatory, both paths) →
- practice sets — single tier-1 pass; findings applied by item-writer with trace → done;
- exam sets — full t1⇄t2 rounds → converged → decision request → arbiter ruling.
**Release rule**: an exam set enters student use ONLY after arbiter `approve` AND user
confirmation. Unapproved sets must carry a visible not-released marker in output/.

**Forecast** (dedicated chain — separate instances from rev-*): `forecast-writer`
(Claude Code Opus) authors the report per FORECAST_GUIDE → differential review:
scope CONFIRMED (notice-based) = single tier-1 pass by `forecast-reviewer`;
scope UNCONFIRMED (⚠️ inferred) = full `forecast-reviewer` ⇄ `forecast-auditor` rounds
(≤5) with disputes escalating to `forecast-arbiter` → handoff: coordinator passes the
A~E grade table to item-writer distribution. Post-scoring appends to the same report
(FORECAST_GUIDE §6). Protocol mechanics inherit §1·§3·§6; forecast-specific checklists
live in the agent definitions.

## 4. analysis/REV_LOG.md format (append-only)

```markdown
| 날짜 | 검토서 | 요약(한 줄) | 상태 | 반영처 |
```
Rows never deleted; status changes become NEW rows. Section comments per folder allowed.

## 5. Actors

| Role | Actor | Write surface |
|------|-------|---------------|
| Pure transcription & evidence | `type-extractor` (Codex/OMX) | corpus unit files + verify_log transcribe/unreadable rows + own WIP |
| Primary type analysis (Claude Code Opus) | `type-proposer` | own proposal docs + verify_log classify/merge/grade rows + own WIP |
| Tier-1 review · coordination · replies | `rev-writer` | own reports + `_index` rows + REV_LOG + own WIP |
| Tier-2 independent audit | `rev-auditor` | own `*_second.md` + `_index` rows + REV_LOG + own WIP |
| Tier-3 final ruling (Claude Code Opus, same repo) | `rev-arbiter` | `*_ruling.md` + REV_LOG + own WIP |
| Applies approved fixes | authoring owner (`type-proposer` · `item-writer` / user) via coordinator | artifacts + trace rows |
| Drives rounds · convergence bookkeeping | main loop | `_index` header state · status fields |
| Pre-gate: blind solve of every set | `solve-back-verifier` | **own WIP only — no other files** (report-only otherwise); findings feed tier-1 |
| Forecast authoring (Claude Code Opus) | `forecast-writer` | own report under `analysis/forecast/` + own WIP |
| Forecast tier-1 review | `forecast-reviewer` | own reports + `_index` rows + REV_LOG + own WIP |
| Forecast tier-2 audit | `forecast-auditor` | own `*_second.md` + `_index` rows + REV_LOG + own WIP |
| Forecast final ruling (Claude Code Opus) | `forecast-arbiter` | `*_ruling.md` + REV_LOG + own WIP |

No two actors write the same file concurrently; `_index.md` rows are the sole shared touchpoint.

**WIP = `analysis/wip/<actor>_<YYMMDD>_<task>.md`** — the slice checkpoint mandated by CLAUDE.md
「서브에이전트 공통 실행 규격」②. Exclusive ownership: an actor writes only its OWN WIP and never
touches another's; only the user prunes finished files. **WIP is never cited as evidence** in a
report or ruling (`analysis/wip/_README.md`) — checkpoints are a crash-recovery aid, not a record;
the append-only trace of applied fixes lives in verify_log `corrected` rows and REV_LOG (§3 rule 4).
Listing WIP here closes the 260826 contradiction where following the runtime protocol would itself
have violated this write-surface table (ruling 260826_02 BF8).

**Tool-grant coupling (260826 3차 — 정의 감사 반영).** 이 표의 write surface는 **해당 배우의
`.claude/agents/*.md` `tools:` 줄에 Write(공유 원장에 행을 덧붙이는 배우는 Edit까지)가 실제로
있어야** 성립한다. 정본이 "쓰라"고 하는데 도구가 없으면 그 배우는 셸로 우회하거나 지침을 어긴다
— 실측으로 `forecast-reviewer`·`forecast-auditor`·`solve-back-verifier` 3종이 이 상태였다.
역으로 **셸은 write surface의 우회로가 아니다**: PowerShell/Bash는 계산·조회용이며, 이 표 밖의
파일을 리다이렉션으로 만들거나 덧붙이지 않는다. 두 문장은 각 에이전트 정의에도 함께 적는다.
> **동반 갱신 목록 (§5 개정 시)** — 배우를 추가·삭제하거나 write surface를 바꾸면 같은 작업에서
> 그 배우의 `.claude/agents/*.md` `tools:` 줄과 CLAUDE.md 「서브에이전트 공통 실행 규격 ④」를
> 함께 점검한다. (CLAUDE.md 원칙 10)

## 6. Decision-request package (tier-3 input)

File `YYMMDD_NN_NAME_decision.md`, self-contained even though the arbiter has repo access:

```markdown
---
title / source(s) / created / requested_by: main-loop / state: submitted
---
<document>      excerpts of final artifact state
<rounds>        _index.md excerpt (all rounds) + tier-1 and tier-2 final opinions
<open_questions> numbered disputes needing a ruling (empty if pure confirmation gate)
<output_format> | question | ruling | evidence | note |
```

### §6-b Relay message spec (user-copied handoff, 260826)

The user physically copies each request into the Claude Code session, so the main loop
MUST print a relay message in the conversation whenever work is handed to a Claude Code
actor (`type-proposer`, tier-3 rulings by `rev-arbiter`, `forecast-writer`,
`forecast-arbiter`). Required fields — the receiving side states their absence instead of
guessing:

1. `<target>` — decision-request/report path(s)
2. `<touched>` — files created▸/modified by the requesting side THIS round
3. `<executor>` — exact subagent name (`rev-arbiter` | `type-proposer` | `forecast-writer` |
   `forecast-arbiter`) or `본체 직접`
4. `<requests>` — numbered questions (mirror of `<open_questions>`)
5. `<reply>` — ruling path pattern + format ref (this §6)
6. `<constraints>` — write surface, no-commit, verify-don't-trust

Form: ONE fenced block titled ``[CC 회람] YYMMDD_NN — 요약``, six labeled lines inside,
so the user can copy it verbatim without editing. Evidence basis: ruling 260825_12
citation slips and the 08 count mismatch showed the receiving side needs exact paths and
counts; explicit constraints prevent write-surface disputes.

**Authoring stance (mandatory — CLAUDE.md ①-b)**: the relay is a production Claude Code
prompt, not an FYI. Written by the main loop in a prompt-engineer stance: (a) fully
self-contained — target, scope, ruling format, reply path close inside the block;
(b) every path/filename/count re-verified immediately before printing (grep · zip list ·
ledger read); unverifiable values are labeled `⚠️미확인`, never guessed; (c) `<executor>`
carries a one-line rationale citing the chosen agent's own definition; (d) requests are
answerable question forms with a verdict enum; (e) constraints are phrased so the
receiver can self-check compliance. A relay violating (a)–(e) may be returned by the
receiving side with the gap named instead of being executed on guesses.

**Proportionality of the return right (260826, ruling 260826_02 BF9)**: returning a relay is an
EXCEPTION path, not a default. To return one, the receiver must state **which of (a)–(e) is missing,
how, and why that gap makes a ruling impossible**. If a ruling is still possible despite the gap,
the receiver does NOT return the relay — it proceeds and records the complaint in the ruling's
`<notes>`. Basis: compliance costs one grep before printing, and the first relay written under this
spec had all three of its measured claims verified correct (ruling 260826_02 V12) — so returning
over a cosmetic defect withholds a ruling the requester is entitled to.

### §6-c Execution-order spec (Claude Code → Codex/OMX, 260826)

§6-b covers only the Codex/OMX → Claude Code direction. The return leg had **no spec at all**,
and the gap showed: after ruling 260826_02 Round 2 the Claude Code side approved the cycle and
then asked "shall we start S0?" in prose — the executing side received no runnable instruction.
A ruling that approves work but does not hand it over has not finished.

**Rule.** Whenever the Claude Code side (a) issues an `approve` ruling that unblocks a stage,
(b) applies owner fixes that clear a stage-blocking condition, or (c) is asked for the next
step, it MUST print an **execution order** in the conversation for the user to copy into
Codex/OMX. Same prompt-engineer stance as §6-b (a)–(e), plus:

1. `<stage>` — stage ID from the governing PRD + the ruling/condition that unblocked it
2. `<executor>` — Codex/OMX executor (`type-extractor` | `item-writer` | `메인 루프`) + one-line
   rationale from that actor's own definition. **Name the WIP path** (CLAUDE.md ②) since the
   executor must checkpoint per slice
3. `<inputs>` — every path the executor reads, with **measured** counts/bytes/hashes taken
   immediately before printing. Unmeasurable values are `⚠️미확인`, never guessed
4. `<outputs>` — exact paths to create, and the canonical spec each must satisfy (§ reference)
5. `<gate>` — the PRD acceptance criterion **verbatim**, as `command + expected output string
   + 0 warning lines + expected count`. No placeholders (CLAUDE.md 원칙 9-c-iii). If it cannot
   be run in that environment the stage is `▲ blocked`, not passed
6. `<constraints>` — write surface, no-commit, append-only ledgers, sandbox paths
7. `<report>` — what to send back and where, so the next relay can be written without re-asking

Form: ONE fenced block titled ``[OC 지시] YYMMDD_NN — 요약``, so the user copies it verbatim.
Known-defect disclosure is mandatory: if a tool the executor will run has a known limitation
or was just fixed, say so with the measured evidence (e.g. `hwp2md.py` HWP image loss, ruling
260826_02 condition C1) — the executor cannot see this session's findings.

## 7. Post-application feedback (CLAUDE.md principle 4)

Applied fixes about "out-of-scope / terminology / difficulty" must also be recorded into
the relevant catalog type's forbidden/caution entries so the same mistake never repeats.

# History
- 260826 (3rd) — **서브에이전트 정의 감사** 반영(사용자 특례 승인, 결과 보고서
  `AGENT_AUDIT_260826.md`): §5에 **Tool-grant coupling** 주석 신설. 계기는 정본과 도구 권한의
  불일치 3건(위 주석의 실측 목록)으로, "규정은 있는데 실행이 불가능한" 상태였다 — §2-b D/E 신설
  때와 같은 종류의 구멍이므로 같은 방식으로 규격화했다. 11개 정의 전부에 '셸은 우회로가 아니다' ·
  산출물 한국어 명시를 추가하고, t2/t3 페르소나를 작성자와 분리했다(감사 C1).
- 260826 (2nd) — tier-3 판정 260826_02 반영: **§2-b E(운영 계획·PRD) 신설 + §5 WIP 등재(BF8) +
  §6-b 반려권 비례성(BF9)**. E 신설 사유는 D와 동형이다 — 계획 문서에 적용할 기준이 없어
  t1·t2가 표면 검토에 머물렀고, tier-3가 이웃 정본 대조만으로 차단 결함 4건을 새로 찾았다.
  E = 이웃 정본 1:1 대조표·판정 가능한 게이트(수치 임계)·비가역 산출물 식별·도구 게이트는 D 적용·
  동반 갱신 커버리지·실데이터 보호. 아울러 §2-b에 **동반 갱신 목록**(개정 시 rev-* 3종 정의 동시 갱신)을
  달았다 — D 신설 후 에이전트 정의가 A·B·C에 머문 사고가 실제로 있었다(CLAUDE.md 원칙 10).
- 260826 — 사용자 판정(검토서 260826_01 Q3) 반영: **§2-b D(System code) 신설 + §3 Round rule 4-a 의무화.**
  검토 결과 기존 라운드 로직으로는 대체 불가였다 — §2-b가 A(문제세트)·B(corpus)·C(제안서)만 규정해 코드 대상
  기준이 없었고, 그 결과 t1·t2·t3 전원이 정적 검토만 수행(t2 자기기록: "Live node run NOT repeated —
  static chain deemed sufficient")해 결함 3건이 3단계를 모두 통과했다. 라운드를 더 도는 것은 이 구멍을
  메우지 못하므로 실행 검증 자체를 규격화했다. D=실행 검증 필수·변경세트 1:1 커버리지·계약 3층(항목/세트메타/출력)
  ·입력 다양성(개행코드·과목별 형식)·미러 구현 전 필드 대조·환경 부재 시 blocked(정적 대체 선언 금지),
  4-a=판정의 수용기준이 갖춰야 할 최소 규격과 반영 주체의 재실행 의무.
- 260825: §1 location split (deliverable rev vs analysis/rev) — misfiled catalog reviews moved.
- 260825 (2nd): **three-tier protocol overhaul** — user decision: tier-1/tier-2 iterate
  automatically inside opencode (main-loop driven, ≤5 rounds, duplicate-dispute escalation),
  tier-3 final arbiter runs in Claude Code (Opus) on the same repo; handoff ledger
  `_index.md` introduced; per-target criteria §2-b; decision-request package §6;
  full English rewrite under the new language policy. Written by: main loop.
- 260825 (3rd): **role re-partition** (user decision) — proposer/t1/t2/t3 agent chain:
  type analysis moved from opencode transcriber to Claude Code `type-proposer`;
  type-extractor reduced to pure transcription; review target for extraction pipeline =
  proposal documents (§2-b C added); §3-b pipeline mappings incl. authoring pre-gate
  (solve-back-verifier mandatory for every set) and practice/exam split with release rule.
- 260826 (3rd): **§6-c neu — execution-order spec for the return leg (Claude Code → opencode).**
  §6-b regulated only the inbound direction; the outbound leg had no spec, so ruling 260826_02
  Round 2 ended in prose ("shall we start S0?") and the executing side got nothing runnable.
  §6-c requires an `[OC 지시]` block with stage · executor+WIP path · measured inputs · outputs+spec refs ·
  verbatim gate (no placeholders) · constraints · report-back, plus mandatory disclosure of known/just-fixed
  tool defects. Mirrored into CLAUDE.md ①-c. Written by: main loop (user instruction).

