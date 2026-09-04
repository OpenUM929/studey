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
6. **정지 조건 — 라운드는 반드시 끝난다 (260829 신설).** rule 2·3은 *언제 닫히는가*만 정했고
   *닫히지 않을 때 무엇을 하는가*는 비워 뒀다. 그 결과 260829 탐지실패 감사는
   라운드1 `BLOCKED` → 라운드2 `REVISE-BEFORE-USER-KEY` + 라운드3 요청으로,
   **매 라운드가 새 선행조건을 추가하며 끝나** 정지 보장이 없는 상태가 됐다.
   각 라운드가 진짜 결함을 찾았더라도 정지 규칙 없는 검토는 산출물을 0으로 만든다.
   - **a. open unit 단조 축소.** 모든 라운드는 머리말에 `open units: {ID, ...}` 집합을 명시한다.
     다음 라운드의 집합은 이전 집합의 **진부분집합**이어야 한다. 크기가 줄지 않은 라운드가
     한 번 나오면 라운드를 더 돌리지 않고 **미해결 unit을 그대로 사용자 결정으로 올린다.**
   - **b. 신규 선행조건 신설 금지.** 라운드는 **동결 입력에서 도출되지 않는 새 요건**을
     차단 사유로 세울 수 없다. 새 우려는 `follow-up:` 항목으로 별도 기록하되 현 라운드의
     종결을 막지 못한다. 차단 사유가 되려면 그 요건이 동결 입력 안에서 **실측으로 위반**됨을
     보여야 한다(§6-d 폐쇄 의무).
   - **c. 수렴 3요건.** `수렴` 선언은 ① 신규 critical 0건 ② 모든 unit이 evidence-backed
     (§6-d의 `evidence` 열이 빈 unit 0건) ③ open 집합 공집합 — **셋 모두** 성립할 때만 쓴다.
     하나라도 미달이면 `수렴`이 아니라 `▲ blocked + 미달 요건`이다.
   - **d. 상한 도달 시.** rule 3의 라운드 상한에 닿으면 미해결 unit을 **그대로 제출**한다.
     라운드를 연장하거나 새 라운드 종류를 만들어 대체하지 않는다.
   근거: 260829 라운드2 자기기록(`CODEX_TEAM_RESPONSE_TO_RULING.md` §7이 라운드3을 요청하며
   S-18·exact-16·warning·typed-closure 4건을 **새 차단 조건으로 신설**).

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
| **Substantive review when the external lane is unavailable** (260828 신설) | main loop (Claude Code Opus) | own report under `analysis/rev/` or `output/<YYMMDD>/rev/` + own WIP. **tier 라벨(t1/t2/t3) 사용 금지** — `reviewer:` 는 `unset`, `author:` 에 "메인 세션"을 명시한다. `_index`·`REV_LOG` 기입은 허용하되 reviewer 열에 `main-loop`로 적는다 |
| Pre-gate: blind solve of every set | `solve-back-verifier` | **own WIP only — no other files** (report-only otherwise); findings feed tier-1 |
| Post-gate: novelty · achievement value · answer-key construction (260830 신설) | `item-quality-auditor` | own `*_item_quality_audit.md` under `output/<YYMMDD>/rev/` + own WIP. **공유 원장에는 기입하지 않는다** — 메인 루프가 대신 기입한다(동시 작성자 충돌 방지) |
| Forecast authoring (Claude Code Opus) | `forecast-writer` | own report under `analysis/forecast/` + own WIP |
| Forecast tier-1 review | `forecast-reviewer` | own reports + `_index` rows + REV_LOG + own WIP |
| Forecast tier-2 audit | `forecast-auditor` | own `*_second.md` + `_index` rows + REV_LOG + own WIP |
| Forecast final ruling (Claude Code Opus) | `forecast-arbiter` | `*_ruling.md` + REV_LOG + own WIP |

No two actors write the same file concurrently; `_index.md` rows are the sole shared touchpoint.

**메인 루프 대행 행의 발동 조건 (260828 신설).** 위 표 마지막 행은 **3단계 루프를 건너뛰는
통로가 아니다.** 다음 두 조건이 **모두** 성립할 때만 쓴다: (a) 담당 배우(외부 Claude Code
레인 또는 Codex/OMX 레인)가 쿼터 소진·런타임 부재 등으로 **실행 불가**임이 관측됐고,
(b) 사용자가 대행을 지시했다. 산출물은 **제안 등급**이며 승인·투입 허가를 스스로 부여하지
못한다 — 담당 배우가 복구되면 그 산출물은 정규 tier-1 입력으로 재투입한다. 대행 사실과
불가 사유는 보고서 머리말에 적는다. 근거: 260828 시스템 감사 S5 — 이 행이 없던 동안
Codex 레인 중단으로 수행된 실질 감사 2건이 규정 밖 작업이 되어 원장에 흔적이 남지 않았다.

**자(ruler)는 어떤 배우의 write surface도 아니다 (260828 신설, CLAUDE.md 원칙 12).** 수용기준·
기대값 표·게이트 코드는 위 표의 어느 행에도 쓰기 대상으로 들어가지 않는다. 검토받는 쪽은 물론
검토하는 쪽도 자기 판정에 쓰는 자를 그 라운드 안에서 고치지 않는다 — 고쳐야 한다고 판단되면
결정요청으로 올리고, 자가 바뀌면 그 자로 내려진 판정은 전부 stale이 되어 재실행 전까지 인용할 수
없다. 근거: 260828 감사 F2-b·F6·F9.

**two-key 대상 목록 (260902 신설, 판정 `output/260831/rev/260831_08_arbiter_ruling_resign.md`
BF-R4).** 위 문단은 원칙을 적었을 뿐 **어떤 파일이 자인지**를 적지 않아, 실행 레인이 「이건 자가
아니라 도구」라고 스스로 판단할 여지가 남아 있었다. 아래가 그 목록이며 **이 표가 정본이다 —
다른 문서는 재열거하지 말고 이곳을 가리킨다**(CLAUDE.md 원칙 9-c-ii).

| 파일 | 무엇인가 | 왜 two-key인가 |
|---|---|---|
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | 자 본체(수용기준·기대값 표) | 재는 대상이 자기 눈금을 고치면 F9가 재현된다 |
| `tools/measure_score_bands.py` | 자의 근거 수치를 산출하는 측정기 | 출력이 곧 자의 내용이다 |
| `tools/regen_rubric_values.py` | 자를 재생성·대조하는 게이트 | **읽기 전용이어도 대상이다** — 12-c가 보호하는 것은 자를 *바꾸는 행위*가 아니라 **자가 무엇인지 결정하는 권한**이고, 이 도구가 통과시키는 것이 곧 자의 내용이 된다. 자를 못 고쳐도 자를 재는 자를 고치면 F9는 그대로 성립한다 |

- 두 열쇠 = **사용자 승인 + 감사권한자(`rev-arbiter`) 판정**. 어느 한쪽만으로는 성립하지 않으며,
  반영 시 원장에 **bytes + sha256(16) 사슬** 재동결 행을 남긴다.
- `tools/regen_rubric_values.py`의 **허용목록(ALLOW)에 자리를 추가하는 것도 이 표의 대상**이다 —
  허용목록 한 줄이 곧 「이 자리는 안 봐도 된다」는 자의 개정이기 때문이다.
- 이 세 파일 중 하나라도 바뀌면 그 자로 내려진 판정은 전부 stale이며 재실행 전까지 인용 금지다.
- **실행 레인(Codex/OMX 포함)은 이 세 파일을 소비만 한다.** 문제를 발견하면 우회하지 말고
  결정요청으로 올린다(원칙 12-a). 게이트 명령과 수용기준은 §5-a.

**§5-a. 자 게이트 (260902 신설, 판정 BF-R3·Q7).** 자·측정기·재생성기 중 하나라도 바뀌면 아래를
**파이프 없이** 실행하고 네 수치를 함께 인용한다. `exit 0` 하나로 끝내지 않는다(원칙 11).

```
python tools/measure_score_bands.py > /dev/null 2>&1 ; echo "exit=$?"     기대: exit=0
python tools/regen_rubric_values.py > /dev/null 2>&1 ; echo "exit=$?"     기대: exit=0
python tools/regen_rubric_values.py
   기대 문자열: "[GATE 0 PASS] undetected=0" · "stale=0 lines=0 residual=0"
   기대 카운트: ":" 로 시작하는 지적 행 0줄 · "[WARN]" 0줄
```

이 게이트는 `tools/check_assurance_contract.py` 구조 검사 6이 자동으로 돌린다 — 손으로 돌리는
것을 잊어도 규정 도달 검사에서 걸린다.

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

**측정 증거는 주장과 함께 이동한다 (260901 신설)** — (b)의 재검증 의무는 260826부터 있었는데도
260831 한 라운드에서 **날조 주장 5건**이 그대로 발신됐다: 실재하지 않는 정본 경로
`analysis/DIFFICULTY_RUBRIC.md`(정본은 `analysis/catalog/`) · 인용 파일에 존재하지 않는 「발견」 3건 ·
`_index.md:18` 표 손상 보고(수신 측·판정자·발신자 재측정 **3중 반증**) · 잔여 9건이 살아 있는데
「BF1~BF7 전건 반영 완료」. 규칙은 있었다. 없었던 것은 **검증된 주장과 날조된 주장이 회람문 위에서
똑같이 보인다**는 사실에 대한 방어다. 그래서 (b)를 다음으로 조인다.

- **(f) 인라인 증거** — 회람문의 모든 카운트·행번호·「알려진 결함」 주장은 **그 자리에 증거를 달고**
  간다: 실행한 명령과 그 출력(또는 매칭 행 1줄 인용). 증거 없는 숫자는 기본값이 `⚠️미확인`이다.
  - **(f-1) 기입 순서 (260902 신설 — 판정 `260831_06` E3·E3-C1 구속)** —
    **기입할 값은 그 편집이 끝난 뒤 다시 측정한다.** 편집 전에 잰 값을 편집 후 문서에 옮겨 적으면
    그것은 인용이 아니라 창작이다. 해시·바이트수·카운트는 **문서를 닫기 직전** 재측정한 값만 쓴다.
    명령이 다르면 값도 다르다 — 동결된 값을 재확인할 때는 **동결 명령 그 자체**를 실행한다.
    **모집단에 이 문서 자신이나 이 문서가 만들 원장 행이 포함되면, 숫자만 적지 말고 측정 경계를
    함께 적는다** — `<명령> @ <시점·제외조건>` 형식으로, 예: 「이 문서와 이 라운드의 원장 행을
    제외한 시점의 값」. 자기참조 모집단에서 맨 숫자는 재현되지 않는다(260902 실측 3/3 드리프트).
    근거: 260901 오기 3종이 전부 「편집 완료 전 기입」 하나의 원인이었고(closure 2/32 + 모집단 밖
    1건), 260902 라운드에서 자기참조 카운트 3건이 **전건 드리프트**했다(3/3) — 그 3건 중 하나가
    이 조항을 요청한 패킷 자신의 숫자였다.
- **(g) 범위는 전수 grep으로 못 박는다** — 「반영했다」고 적을 때는 파일명이 아니라 **전수 grep 명령과
  그 출력 카운트**로 범위를 고정한다. 잔여 카운트 없는 「완료」는 상태 보고가 아니다.
  (판정 측 대칭 의무: 260831_04 F1 — 구속수정도 파일 목록 또는 전수 grep으로 적용 범위를 못 박는다.)
- **(h) 수신자 우선 조항** — 회람문은 다음 한 줄로 닫는다:
  「이 지시문의 값이 원문과 어긋나면 지시가 아니라 **실측을 따르고 그 사실을 회신하라**.」
  위 5건 중 `_index.md:18` 날조를 실제로 잡아낸 것이 이 경로였다(수신 측 `rev-writer`의 원문 대조 반박).

> **동반 갱신 목록 (§6-b 개정 시)** — 이 규격을 고치면 같은 작업에서 함께 점검한다(CLAUDE.md 원칙 10):
> `CLAUDE.md` 공통 실행 규격 ①·①-b · §6-c(역방향 대칭) · §6-d (1) 요청 패킷 필드 ·
> `.claude/agents/` 중 §6-b를 인용하는 5종(`rev-writer` · `rev-arbiter` · `type-proposer` ·
> `forecast-writer` · `forecast-arbiter`).

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
   측정 시점과 자기참조 모집단의 취급은 **§6-b (f-1)** 을 따른다(260902 신설).
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

### §6-d 판정 요청·판정문 표준 규격 (260829 신설)

> **신설 사유.** §6·§6-b는 판정을 *요청하는* 형식만 정했고 **판정문 자체의 형식은 비어 있었다.**
> 그 결과 260829_01 판정에서 서로 다른 세 종류의 오류가 한꺼번에 났고, 셋 다 형식으로 막을 수
> 있는 것이었다: (i) `check_experiment.py`의 PASS 마커를 실측 없이 `[OK]`로 인용 — 실제 값은
> `:230` `experiment-gate: PASS` (ii) span 규칙 `^#{1,6}\s`를 제안하면서 22행 전수에 돌려보지
> 않음 — 돌렸으면 S-18 반례(146↔148)가 즉시 나왔다 (iii) 제안 등급 배우(§5 메인 루프 대행)가
> `binding`·`approve` 라벨을 스스로 부여 — §5는 대행 산출물을 제안 등급으로 한정한다.
> 대칭으로 라운드2 응답도 반례 1건만 제시하고 **최소 수리의 폐쇄를 시험하지 않아** 필요 개정을
> 5종으로 과대 산정했다(실측: 경계 토큰에 수평선 1종만 추가하면 21/22 복원, 잔여 이탈은
> 손수정된 W-04 단독). 과소명세와 과대범위는 **같은 누락 — 폐쇄 시험 부재**에서 나온다.

#### (1) 요청 패킷 (`§6` 결정요청서 + `§6-b` 회람문에 추가되는 필수 필드)

1. `<frozen_inputs>` — `path | bytes | sha256 | role` 표. `role` ∈
   `source | derived | ruler | evidence | output`.
   **직접경로 폐쇄 의무**: 동결 산출물 본문에 **경로 문자열로 등장하는 모든 파일**은 이 표에
   있거나 `<excluded>`에 사유와 함께 적혀야 한다. 어느 쪽에도 없으면 그 패킷은 불완전이다.
   (근거: F10 — 동결 목록을 피측정 레인이 작성하고, 자기 산출물이 `source_path` 열로 지목하는
   원천 3종을 빼서 "측정 불가"를 자기 판정으로 냈다.)
   **표에 적는 bytes·sha256은 패킷을 닫기 직전 재측정한 값이어야 하고, 패킷 자신이나 이 라운드의
   원장 행이 모집단에 드는 카운트에는 측정 경계를 병기한다 — §6-b (f-1)** (260902 신설, 판정
   `260831_06` E3-C1: 260902 패킷의 자기참조 카운트 3건이 하루 안에 전건 드리프트했다).
2. `<units>` — 판정 단위마다 고유 ID(`Q1`·`BF3` 등) + **판정 가능한 질문형** + `verdict enum`
   + `reproduce:` 재실행 명령 1줄. 산문 요청은 unit이 아니다.
3. `<actor_grade>` — 요청받는 배우와 그 **권한 등급**을 요청 측이 미리 적는다(아래 (3)).
4. `<open_units>` — 이 라운드 시작 시점의 미해결 집합(§3 rule 6-a의 단조 축소 대상).
5. `<out_of_scope>` — 이번 라운드에서 판정하지 않을 것. 비면 "전부 판정 대상"으로 읽힌다.
6. 기존 §6-b 6필드(`<target>`·`<touched>`·`<executor>`·`<requests>`·`<reply>`·`<constraints>`).

#### (2) 판정문 표준 — 고정 절 + 고정 열

절 순서 고정: `frontmatter` → `§0 판정 요약표` → `§1 독립 재검증` → `§2 unit별 판정` →
`§3 follow-up(비차단)` → `§4 open units(남은 집합)` → `## history`.

**§0 요약표는 아래 7열을 그대로 쓴다.**

```
| unit | verdict | grade | evidence | measured | closure | note |
```

- `verdict` ∈ `approve | revise-required | reject | insufficient-evidence`.
- `grade` — **판정자가 고르지 않고 배우에서 유도한다**(아래 (3)). 자기 등급 상향 금지.
- `evidence` — **재실행 가능한 명령 또는 `path:line`**. 비어 있으면 `verdict`는 강제로
  `insufficient-evidence`이고 다른 값을 쓸 수 없다.
- `measured` — `yes | no`. unit 본문이 인용한 **모든 리터럴**(마커 문자열·ID·정규식·카운트·
  경로)이 **이 라운드에서 명령으로 산출된 값**이면 `yes`. 하나라도 기억·유추·형제 도구에서
  옮겨 적은 값이면 `no`이고, 그 unit은 `insufficient-evidence`로 강등된다.
  (CLAUDE.md 원칙 9-c-i·ii의 판정문 적용 — 사본 열거는 반드시 원본과 어긋난다.)
- `closure` — 규칙·정규식·임계값·기대 카운트를 **제안하거나 반박하는** unit에 필수.
  `k/N` 형식으로 **모집단 전수 실행 결과**를 적는다.
  - 제안 측: 제안한 규칙을 전수에 돌려 잔여 불일치 `k/N`과 그 목록을 적는다. 미실행이면
    `insufficient-evidence`.
  - 반박 측: 반례 제시로 끝내지 않고 **최소 수리를 구성해 전수에 돌린 `k/N`** 을 함께 적는다.
    최소 수리를 시험하지 않고 필요 개정 목록을 늘린 unit은 `note`에 `over-scoped`로 표시하고,
    그 초과분은 차단 사유가 아니라 §3 `follow-up`으로 내린다(§3 rule 6-b).
- **플레이스홀더 금지** — `N`·`<...>`·TBD는 판정문 어디에도 쓰지 않는다(원칙 9-c-iii).
- **새 검출기 제안에는 fixture 의무** — 판정이 새 검사·스키마·폐쇄 규칙을 요구하면,
  그것이 **잡아내는 알려진 실패 사례 1건 이상**을 지목한다. 실패 사례가 없는 검출기는
  검증되지 않은 검출기이므로(원칙 12-d) 차단 요건이 아니라 `follow-up`이다.

#### (3) 권한 등급표 — 판정자가 아니라 배우가 결정한다

| 판정 배우 | 등급 | 쓸 수 있는 라벨 |
|---|---|---|
| `rev-arbiter` (fresh context, §5) | `binding` | approve · revise-required · reject |
| `forecast-arbiter` (fresh context) | `binding` | 〃 |
| 메인 루프 대행 (§5 마지막 행) | `proposal` | **proposal-approve · proposal-revise · proposal-reject** |
| Codex/OMX advisory 레인 | `advisory` | 〃 (advisory- 접두) |
| 자기 산출물의 작성자 | 등급 없음 | 판정 불가 — 결정요청으로 올린다 |

`binding`은 **fresh context가 실제로 성립할 때만** 쓴다. 이전 라운드의 발견을 이미 알고 있는
세션은 fresh가 아니며, 그 사실을 `frontmatter: independence:`에 적더라도 등급이 올라가지 않는다.
등급을 초과한 라벨이 발견되면 반영 주체는 **되돌려 등급 정정을 요구한다**(§3 rule 4-a 준용).

> **동반 갱신 목록 (§6-d 개정 시)** — 이 규격을 고치면 같은 작업에서
> `.claude/agents/rev-arbiter.md`·`forecast-arbiter.md`의 출력 형식 항목과 CLAUDE.md
> 「서브에이전트 공통 실행 규격 ①·①-b」를 함께 점검한다. (CLAUDE.md 원칙 10)

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
- 260901: **§6-b (f)(g)(h) 신설 — 측정 증거는 주장과 함께 이동한다.** (b)의 재검증 의무는
  260826부터 있었으나 260831 한 라운드에서 날조 주장 5건이 발신됐다. 규칙 부재가 아니라 **검증
  여부가 회람문 위에서 보이지 않는 것**이 원인이므로, (f) 인라인 증거(명령+출력) · (g) 범위는
  전수 grep 카운트로 고정 · (h) 수신자 우선 조항을 추가했다. §6-b 동반 갱신 목록도 함께 신설.
  근거: 판정 `output/260831/rev/260831_04_arbiter_ruling_K1.md` F1 + 메인 루프 자기 신고 5건.
  Written by: main loop (user instruction).
- 260902 (2nd) — tier-3 판정 `output/260831/rev/260831_08_arbiter_ruling_resign.md` 반영:
  **§5 「two-key 대상 목록」 + §5-a 「자 게이트」 신설.** 종전 §5는 「자는 어떤 배우의 write
  surface도 아니다」는 원칙만 적고 **어떤 파일이 자인지** 적지 않아, 실행 레인이 「이건 자가 아니라
  도구」라고 스스로 판정할 여지가 남아 있었다. 판정 Q7이 그 구멍을 닫았다 — 읽기 전용 재생성기도
  대상이며, 12-c가 보호하는 것은 자를 바꾸는 행위가 아니라 **자가 무엇인지 결정하는 권한**이다.
  게이트는 `tools/check_assurance_contract.py` 구조 검사 6이 자동 실행하며, 검출력을 심은 결함
  1건으로 실증했다(자 `(510행)` -> `(462행)` 주입 -> ruler gate FAIL 3줄, 복원 후 sha 동일).
  동반 갱신: `CLAUDE.md` 원칙 12-c·동반 갱신 목록 · `AGENTS.md` Non-negotiable rules ·
  `tools/check_assurance_contract.py`. Written by: main loop (user instruction).
