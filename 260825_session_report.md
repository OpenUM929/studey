---
title: Session Work Report — 260825 continuation session
created: 260825
author: opencode main loop (ox-alpha session)
scope: Group K finalization · Group L · Group M · Group N · Group O
purpose: Independent verification package for Claude Code (rev-arbiter class)
location_note: Placed at repo ROOT by explicit user request (exception to zone conventions).
---

# Session Work Report — 260825

## 0. 요약 (Korean executive summary)

이번 세션(연속 세션)에서는 네 그룹의 작업을 수행했다.
① **Group K 마무리** — 파일명 로마자화의 누락분 해소: 정전 상호 참조 치환,
`analysis/student/` 한글명 산출물 6건 영문 개명(git mv 추적 유지), 2차 참조 스윕,
최종 감사 통과(생존 문서 구명 참조 0·한글 파일명 0·staged rename 21건).
② **Group L** — 서브에이전트 전원(당시 7종)에 **진행 흐름도 보고 기능** 표준 장착:
반환값 첫 줄에 파이프라인 지도+현재 위치 `▲` 마커+단계 정보+다음 주체 인계 경로.
REV_GUIDE §3 규칙 5로 법제화. ③ **Group M** — 회차 예측 프로세스 정비:
예측 전용 4역할 에이전트 신설(forecast-writer/reviewer/auditor/arbiter, 기존 rev-*와
별개 인스턴스), FORECAST_GUIDE 전면 영어 재작성(+§0 파이프라인 절), 판단 계열 5종에
**2층 페르소나**(고정층 교사·출제 전문가 + 가변층 `Target cohort: grade 1 (2026)`) 보강,
정전 5종 갱신(CLAUDE.md 행·REV_GUIDE 다이어그램/매핑/Actors 표·README 흐름 블록·
DATA_STANDARD v1.6 actor enum). ④ **Group N** — 대기 검토서 6건 처리:
rev 홈 위생 수선+`_index.md` 원장 신설 → **t2 독립 교차검증 6건**(regex 재실행·머신
카운트·스캔 PNG 5면 직접 판독; 성실한 PARTIAL 표기) → **결정요청 패키지 6건**
(260825_07~12) → 장부 갱신. 현재 6건 모두 `submitted` — Claude Code(rev-arbiter)
판정 대기. ⑤ **Group O** — PRD 잔여 일몰 + 3층 구축(사용자 "순차 진행" 전체 승인):
migration ledger stale 행 동기화, A12를 DATA_STANDARD **v1.7 §1.5**로 명문화,
계획서 P0/P1/P3 착수 승인·실행(`build_catalog_index`→index.tsv **131행** CODE_REGISTRY
전수 일치 · SUP-M2-2026/meta.yml · S01 원장 4종 BOM+WK-01 시딩 · share/SHARE_LOG),
도구 4종 완성과 임시 디렉터리 end-to-end dry-run 통과(원자적 거부 exit=2 확인),
CLAUDE.md 「원장 운용」 행 추가. 커밋은 하지 않음(사용자 지시 대기).

## 1. Scope of this report

Prior same-day groups (G 검증 사료 체계, H three-tier protocol + language policy,
J role re-partition + authoring gate, K filename romanization main pass) are recorded in
[`output/260825/260825_01_artifact_management_prd.md`](output/260825/260825_01_artifact_management_prd.md).
**This report covers only the continuation session**: K-final → L → M → N → O.

### User decisions driving this session (verbatim intent)

| # | Decision | Consequence |
|---|---|---|
| D1 | 진행 단계마다 흐름도를 보여주며 현재 단계 정보·결과를 사용자에게 제공하도록 서브에이전트에 기능 추가 | Group L |
| D2 | 예상 문제 만드는 과정도 정비 | Group M |
| D3 | 예측의 제안자·1차·2차 심사자·최종 결정자는 **기존 체인 재활용 금지**, 별도 서브에이전트 — 출제 전문가 페르소나 필수 | forecast-* 4종 신설 |
| D4 | 고1 특화 vs 일반화 질의 → 결론: **특화 유지하되 가변층으로 격리**(진급 시 한 줄 교체) | two-layer persona |
| D5 | 기존 데이터 정제 측 페르소나 감사 지시 → 갭 확인 → "**모두 보강 진행**" | backfill ×5 |
| D6 | "순차 진행을 하고 클로드 코드 검증 문서에 업데이트" + 질의 응답: **전체 승인**(P0소급·P1·P3·P4부분) / A12는 **§1.3 명문화** / **커밋 안 함** | Group O |
| D7 | 검토서 6건 판정 처리 선택 | Group N |

## 2. Group K-final — filename romanization completed

### 2.1 Canonical cross-references fixed (missed in main pass)

`analysis/REV_GUIDE.md`, `analysis/DOC_LOCATION.md` contained references to the OLD names
(`REV_지침.md`, `시험예측_지침.md`, `문서위치_표준.md`) because the first sweep file-list
omitted the renamed analysis/*.md files themselves. 7 replacements applied via ordered
token rules (same rules as main pass).

### 2.2 Student-zone deliverables romanized (user policy covers 산출물 명칭)

All six were tracked; renamed with `git mv` (history preserved):

| Old (Hangul) | New (romanized) |
|---|---|
| `analysis/student/사회_한국사_영어_오답분석.md` | `wrong_analysis_social_history_english.md` |
| `analysis/student/수학_오답분석.md` | `wrong_analysis_math.md` |
| `analysis/student/종합보고서.md` | `comprehensive_report.md` |
| `analysis/student/종합진단_리포트_v2.md` | `comprehensive_diagnosis_report_v2.md` |
| `analysis/student/통합과학_오답분석.md` | `wrong_analysis_science.md` |
| `analysis/student/학습코칭_직언_260721.md` | `coaching_notes_260721.md` |

Second reference sweep replaced remaining mentions + internal cross-links:
24 more replacements across 10 files (`raw/README.md`, `docs/PROMPT_math2.md`,
`DIFFICULTY_RUBRIC.md`, `math1.md`, `TYPE_MASTER.md`, 4 student files, `student/_README.md`).
Bare Korean document TITLES inside legacy bodies were left untouched (content-level Korean
is allowed; only NAMES change).

### 2.3 Final audit (all passed)

1. Old-name token scan over living docs (CLAUDE.md, README, docs/*, analysis/*.md except
   append-only logs, catalog/*, .claude/agents/*, student/*, forecast/*, corpus/_README,
   extracted/README, raw/README): **0 hits**
2. Hangul-named `.md/.tsv/.py` outside data/history zones (`origin_data`, `extracted`,
   `output`, `web`, `analysis/rev` snapshots): **0 hits**
3. Markdown link resolution over living docs: **0 broken** — two known false positives
   documented: DATA_STANDARD inline-code artifact `` `M\|F\|P\d{2}` `` matched by the
   link regex, and `english.md:106` prose "[A][B](또는 (A)(B))" (answer-format prose,
   not a link)
4. `git status --short`: **21 staged renames (R)** = 14 catalog/guide moves + PROMPT_math2
   + 6 student files; REV_GUIDE/DOC_LOCATION moved via os.rename while untracked (no
   commit history existed — lossless)
5. PRD records: K1–K4 pre-existing, **K5 appended** documenting the extension above.

## 3. Group L — progress-map reporting (all sub-agents)

### What was added

Every agent definition gained a mandatory `## Progress reporting` section: the return
value MUST OPEN with a three-part header —

```
Pipeline : <canonical stage diagram of its chain>
              ▲ done            ← current stage marker
Stage    : facts (trigger · inputs · counts/verdicts)
Next     : next actor + handoff path
```

Blocked runs must mark `▲ blocked + reason` (failure concealment impossible).
`solve-back-verifier` embeds its verdict directly in the map (`▲ VERDICT: PASS | HOLD`).

### Canonical diagrams codified (REV_GUIDE §3 round-rule 5, added this session)

- extraction `[refine]▶[propose]▶[review t1⇄t2 ≤5R]▶[arbiter]▶[apply]`
- authoring `[create]▶[pre-gate solve-back]▶[practice: t1 | exam: t1⇄t2]▶[arbiter]▶[release]`

### Files edited (then-7 agents)

`.claude/agents/{type-extractor,type-proposer,item-writer,solve-back-verifier,rev-writer,rev-auditor,rev-arbiter}.md`
PRD record: **L1**.

## 4. Group M — forecast pipeline overhaul + two-layer persona

### 4.1 Persona audit finding (triggered by user question)

CLAUDE.md's persona ("고등학교 1학년 담당 교사이자 문항 출제 전문가") had **never been
migrated into agent definitions**. Audit result:

| Agent | Before | Verdict |
|---|---|---|
| item-writer | school+grade mentioned, no teacher/expert identity | gap → backfilled |
| type-proposer | role name only | gap → backfilled |
| rev-writer / rev-auditor / rev-arbiter | tier role names only | gap → backfilled |
| type-extractor | no persona | **correct by design** (pure transcription, judgment banned — Group J) |
| solve-back-verifier | "solve like a student seeing it first time" | **correct by design** (blind-solve anti-persona; teacher persona would contaminate) |

### 4.2 Two-layer persona standard (D4)

Applied verbatim to all 9 judgment-side agents (5 backfilled + 4 new):

```
Fixed layer:    "You are a Sangsang High subject teacher and expert exam-item writer"
Variable layer: "Target cohort: grade 1 (2026) — update only when the workspace advances a grade."
```

Rationale recorded: every evidence base (catalogs, corpus, measured split patterns,
terminology, point-value bands) is grade-1 data; generalizing to "high-school teacher"
would import out-of-evidence patterns. Advancement requires wholesale catalog/corpus
rebuild anyway, at which point the single cohort line updates mechanically.

### 4.3 Dedicated forecast chain (D3) — four NEW agents

Separate instances from the rev-* chain; no shared write surface. Protocol mechanics
inherit REV_GUIDE §1·§3·§6 by reference; each definition adds only forecast-specific
checklists.

| File | Model | Role | Distinctive content |
|---|---|---|---|
| `.claude/agents/forecast-writer.md` | opus | authors A~E grading, E-blindspot list, reflect/cover metrics, distribution advice under `analysis/forecast/<YYMMDD>_<term-code>-<subject_code>.md`; proposal-class, never touches catalogs/logs | procedure summary mirroring FORECAST_GUIDE; downstream obligations stated in §4 advice |
| `.claude/agents/forecast-reviewer.md` | sonnet | tier-1, one pass | 8-item checklist: scope-evidence order, no silent grade upgrades, primary>secondary, metric honesty (no fabricated numbers), E-list vs FULL in-scope catalog, distribution feasibility vs real point-value bands/Tier norms, downstream obligations, post-scoring append-only cleanliness |
| `.claude/agents/forecast-auditor.md` | sonnet | tier-2 ≤5R | INDEPENDENT recomputation: re-derives grades from cited evidence before reading reasoning, diffs, classifies deltas; duplicate-dispute escalation |
| `.claude/agents/forecast-arbiter.md` | opus | binding ruling on escalation only | 5 forecast ruling criteria incl. "fabricated metric ⇒ revise-required by itself"; write surface = own `*_ruling.md` + one REV_LOG row |

### 4.4 Differential governance (user-approved option)

Scope CONFIRMED (school-notice based) → single tier-1 pass.
Scope UNCONFIRMED (⚠️ pattern-inferred) → full t1⇄t2 rounds (≤5), disputes escalate to
`forecast-arbiter`.

### 4.5 FORECAST_GUIDE.md — full English rewrite

- All original content preserved semantically: data grades (primary/secondary/tertiary ↔
  `verified` / `verified(workbook)` / `demonstration`), "drilled ≠ will be tested",
  "unmeasured" rule, scope-determination order (notice > historical split pattern;
  2026-S1 math1 measured pattern kept verbatim in substance), ⚠️ marking duty,
  reflect/cover/blindspot definitions, A~E table, deliverable template, post-scoring loop.
- NEW §0 Pipeline & actors (diagram + differential governance table + handoff row).
- Filename aligned to term-code convention `<YYMMDD>_<term-code>-<subject_code>.md`.
- §5 template gains **downstream obligations**: sets built FROM a forecast carry
  `intended_use: practice|exam`, pass the solve-back pre-gate, release needs arbiter +
  user confirmation (REV_GUIDE §3-b).
- Korean history rows preserved verbatim; new English history entry appended.

### 4.6 Canonical-document sync

| File | Change |
|---|---|
| `CLAUDE.md` | prediction workflow row: actor cell `—` → `forecast-writer` 작성 · 차등 검토(t1 / t1⇄t2 ≤5R) → 분쟁시 `forecast-arbiter`, 메인 루프 구동 |
| `analysis/REV_GUIDE.md` | §3 rule 5: third canonical diagram (forecast); §3-b: new **Forecast** mapping paragraph; §5 Actors table: +4 rows (writer/reviewer/auditor/arbiter with write surfaces) |
| `README.md` | new flow block "회차 예측 흐름 (전용 체인)" + shortest-path entry "회차 예측이 필요할 때" |
| `docs/DATA_STANDARD.md` | **v1.6**: verify_log actor enum +`forecast-writer`·`forecast-reviewer`·`forecast-auditor`·`forecast-arbiter`; history row |
| PRD | **Group M** record (M1–M7 checkboxes) |

## 5. Verification performed this session (reproducible)

| # | Check | Method | Result |
|---|---|---|---|
| V1 | 11/11 agents contain `Progress reporting` + `▲` | python scan of `.claude/agents/*.md` | PASS |
| V2 | Persona+cohort present on exactly the 9 judgment-side agents; absent on type-extractor & solve-back-verifier | keyword scan (`expert exam-item writer`, `Target cohort`) | PASS |
| V3 | FORECAST_GUIDE body (before `# History`) Hangul count = 0 | regex `[가-힣]` | PASS |
| V4 | Hanzi contamination in all 11 agents = 0 | regex `[一-鿿]` | PASS |
| V5 | REV_GUIDE third diagram / §3-b Forecast paragraph / Actors +4 rows | token presence (`- forecast \``[scope-fix]▶`, `**Forecast** (dedicated chain`, 4 table rows) | PASS |
| V6 | DATA_STANDARD enum contains `forecast-auditor` AND `v1.6` | grep | PASS |
| V7 | CLAUDE.md prediction row filled; README ≥2 `forecast-writer` mentions | grep | PASS |
| V8 | Broken links across CLAUDE.md / README / REV_GUIDE / FORECAST_GUIDE | relative-target existence walk | PASS (2 known false positives, §2.3-3) |
| V9 | Working tree state | `git status --short` | 21 staged R + modifications + 4 untracked new agents (~63 paths at last count) |

## 6. Independent verification guide (for Claude Code)

Reproduce any claim above without trusting this report:

1. **Agents**: list `.claude/agents/` → expect 11 files; grep `-l "Progress reporting"` → 11;
   grep -L "Target cohort" → exactly `type-extractor.md`, `solve-back-verifier.md`.
2. **Renames**: `git status --short | findstr "^R"` → expect 21 rename pairs matching §2.2
   tables; `Test-Path analysis/forecast/../student/comprehensive_report.md` style probes.
3. **Old-name residue**: search living-doc set for tokens `REV_지침|시험예측_지침|문서위치_표준|
   출제유형_마스터|난이도_루브릭|공통유형\.md|생성_운영지침|catalog/(수학|공통수학2|통합과학|
   통합사회|한국사|영어|국어)\.md|영어_지문수준|PROMPT_공통수학2` → 0 hits expected
   (EXTRACTION_LOG.md / REV_LOG.md / output/** / analysis/rev/** are EXEMPT historical zones).
4. **Guide rewrite**: read `analysis/FORECAST_GUIDE.md` — §0 exists, A~E table intact,
   Korean only in History block; template shows term-code filename + downstream obligations.
5. **Canonical sync**: grep `forecast-writer` in CLAUDE.md / README.md / REV_GUIDE.md /
   docs/DATA_STANDARD.md → present in all four; DATA_STANDARD history contains `v1.6`.
6. **Protocol coherence**: REV_GUIDE §3 rule 5 lists THREE diagrams; §3-b has three
   mapping paragraphs (Extraction–analysis / Authoring / Forecast).
7. **Nothing committed**: `git log --oneline -3` unchanged from session start; all changes
   live in working tree/index awaiting user instruction.

## 7. Open items (explicitly NOT done)

- No git commits (user instruction pending). Index holds staged renames only.
- Actual forecast report NOT generated (user chose process-overhaul-only; first run would
  be 2026-2M math2 in ⚠️ UNCONFIRMED mode → full review path).
- Six review reports: `submitted` — awaiting rev-arbiter rulings via user relay of
  decision packages 07–12; owner-applied fixes come AFTER rulings.
- **Plan P2 blocked** on those rulings (parser.js F1~F6·F9, app.js 4-state, 모의40 16번,
  QUIZ_STANDARD revision, and the deferred 모의40 frontmatter insertion all queue behind it).
- Remaining backlog: H9 legacy Korean→English migration, tools/·web/ README documentation,
  부교재 93문항 재판독 (별도 세션, D7 결정).
- Known cosmetic debt: DATA_STANDARD link-checker false positive (inline-code regex),
  english.md answer-format prose flagged by naive link regex — both documented, both
  harmless. Tool quirk (documented in docstring): single wrong → `unstable` until
  wrong≥2-or-blank≥1 lands in last3.

## 8. Traceability

- PRD checkbox ledger: [`output/260825/260825_01_artifact_management_prd.md`](output/260825/260825_01_artifact_management_prd.md)
  — Groups K5, L1, M1–M7, N0–N4, O1–O6 added this session (running total: ~66 done / 3 deferred).
- Procedure canons touched: `analysis/FORECAST_GUIDE.md` (rewrite), `analysis/REV_GUIDE.md`
  (rule 5, §3-b, §5), `docs/DATA_STANDARD.md` (**v1.7**), CLAUDE.md (forecast row + 원장 운용 row),
  `output/260825/plan_3layer_architecture.md` (§7 checkboxes + status + A11 history).

## 9. Group N — six pending reviews → decision-request stage (added 260825 late session)

### What happened
User picked "검토서 6건 판정 처리" as next step. Executed end-to-end:

| Stage | Deliverable |
|---|---|
| N0 hygiene | `analysis/rev/HISTORY.md` living-header links fixed (2 stale old-name refs); history rows preserved |
| N1 ledger | `analysis/rev/_index.md` created per REV_GUIDE §1 (now 12 rows: 6 t1 + 6 t2) |
| N2 cross-check | `260825_0N_*_second.md` ×6 — t2 verdicts: **01 9/9 CONFIRMED · 02 5C+2P+7 pass · 03 4C+3P · 04 5C+1P+4 pass · 05 8C+1P · 06 4/4 CONFIRMED** |
| N3 packages | `260825_07~12_*_decision.md` ×6 (§6 format; numbered open questions; conditional-approval options for PARTIAL items) |
| N4 bookkeeping | report frontmatters 대기→submitted ×6 · HISTORY status column · REV_LOG +8 rows · PRD Group N |

### t2 evidence base (independently re-derived, not quote-trusted)
- Report 01: Python regex re-execution (4 samples), counts (tagLines=40·tableRows=40·aux@446),
  static reads (SUBJECT_MAP 4 rows, LS 5 keys, 2-state scoring, DATA-only export,
  4-store reset), section-reset chain parser.js+md2quiz.py.
- Report 02: txt point marks (24기말 3.3–3.6 / 25중간 2.3–2.7), stem anchors
  (24중간 #17=Na⁺/O₂; DNA@24기말#17), **PNG reads: 26중간 p03 (3:1 item = #7),
  26기말 p07 (단답형1=p-n 다이오드, zero mechanics)**.
- Report 03: header verbatims ×4 (24기말 선택21·단답5 / 25기말 선택24·단답6), machine
  counts (24중간 고려4·조선0 / 25중간 고려16·조선9 / 25기말 근대5·고려0).
- Report 04: headers (서답형 5 ×3 rounds), [2.1점], 실업률@24중간 L251, 25f-soc pts
  3.5–5.0, identical 2026-병기 preamble ×3 catalogs.
- Report 05: **PNG reads: 26중간 수학 p01 (단답형20+서술형4), 26기말 p01 (단답형23 단독),
  26기말 p07 (#22 4.85점·#23 5점)**; korean paren-points (1.7@#16, 4.0@#11), 겹받침=#6,
  자기결정성=#18, 제29항=ㄹ→ㄷ; student docs (취약 후보·18번 확정).
- Report 06: fresh greps (df/aux/frontmatter/scope_confirmed/set_id = all 0; registry
  lacks T-/W- prefixes).

### Known limitations (recorded in every *_second.md)
1. Explore subagents were unavailable (provider outage) → t2 executed by main loop;
   independence is procedural (fresh evidence, no quote-trust), not contextual.
2. 2024/2025 txts preserve exam table layout with syllable-split artifacts → item-level
   renumbering for 02-S6/S7 and 03-H4–H6 NOT independently reproduced → marked PARTIAL,
   packaged with conditional-approval (teacher spot-check) options.
3. Live node execution of parser.js not repeated (no browser env) — static chain deemed
   sufficient; noted in second opinion.

### Handoff to Claude Code (rev-arbiter relay)
User relays these six files (self-contained per REV_GUIDE §6):
`analysis/rev/260825_07_tag_pipeline_decision.md` · `08_science_catalog_decision.md` ·
`09_history_catalog_decision.md` · `10_english_social_catalog_decision.md` ·
`11_math_korean_catalog_decision.md` · `12_quiz_standard_decision.md`.
Each ends with a ruling table (| question | ruling | evidence | note |). After rulings
return: owner applies approved fixes + trace rows + principle-4 forbidden/caution entries,
then _index reflect_state flagged→fixed→re-verified.

## 10. Verification additions for Group N (extend §6 checklist)

8. **Ledger**: `analysis/rev/_index.md` exists, 12 data rows, header `state: submitted`.
9. **Second opinions**: 6 files matching `analysis/rev/*_second.md`; each carries
   verdict tables whose PARTIAL entries give reasons (no silent overclaims).
10. **Packages**: 6 files `260825_07~12_*_decision.md`, each with `<document>` `<rounds>`
    `<open_questions>` `<output_format>` blocks.
11. **Status coherence**: grep `status: 대기` in analysis/rev → 0 hits (6 became
    `submitted`); HISTORY.md shows `**submitted**` ×6.
12. **REV_LOG**: new rows reference decisions 07–12 with links that resolve.

## 11. Group O — PRD residual sweep + 3-layer P1/P3 construction

### User approvals (question-tool answers, verbatim intent)
전체 승인(O1~O6, P4는 부분) · A12 = DATA_STANDARD §1.3 명문화 · 커밋 안 함.

### What was built

| Stage | Deliverable | Verification |
|---|---|---|
| O1 ledger sync | migration-ledger §4 rows aligned to PRD reality (A13/A14/A1–A4/A9/A15 done; A10 annotated as absorbed by K5) + PRD A10 row updated | manual diff vs PRD §9 |
| O2 = A12 | DATA_STANDARD **v1.7** — new §1.5: round-shared answer keys get NO corpus ID (subject_code precondition), tracked via HARVEST_LOG note + meta.yml answer_key, INDEX ID `-`, location preserved | history row v1.7 |
| O3 = P1 (+A11) | `tools/build_catalog_index.py` NEW → `analysis/catalog/index.tsv` **131 data rows** (BOM); per-prefix counts == CODE_REGISTRY §1 exactly. `corpus/SUP-M2-2026/meta.yml` (§5.7 fields, honest nulls). `student/S01/{profile.md,ATTEMPT_LOG.tsv,MASTERY.tsv,WEAK_LEDGER.tsv}` all BOM; WK-01 seeded state=found. `share/SHARE_LOG.tsv`. A11 line in plan history | see V10–V14 below |
| O4 = P3 | `build_mastery.py` · `import_grading.py` · `build_report.py` (+catalog_index from O3). Dry-run in `%TEMP%\opencode\o_dryrun`: valid 5-row TSV → append+regen+proposals+HTML+SHARE_LOG all PASS; invalid mark_code → atomic ABORT exit=2; E5 wrongs matched to open WK-01; S01 ledgers untouched (D6) | exit codes 0/0/2 recorded |
| O5 = P4 partial | CLAUDE.md 작업 흐름 표 「원장 운용」 row. 모의40 frontmatter DEFERRED to post-P2 (parser lacks frontmatter support — QS-3) | row present |
| O6 records | plan §7: P0/P1/P3 `[x]`, P4 partial+deferred note, P2 blocked-note; plan frontmatter status 진행중; migration ledger A11/A12 `[x]`; PRD Group O block | this section |

### Engineering notes (honest record)
1. index.tsv generation hit two real bugs during development, both fixed and re-verified:
   column order mismatch vs header, and sheet-unit fallback. Final rule set: explicit
   `영역/단원` field → math2 `영역 Gn` section-heading fallback → `-`. SM2-14 (field-less
   block) resolves to I-2/2.직선의방정식 correctly; carry-forward approach was REJECTED
   after it bled across sheet boundaries.
2. Same `readlines()`-on-str bug existed in three tools (copy-paste origin) — fixed in
   all three; noted here because Claude Code should not mistake the pattern for sabotage.
3. Console CP949 garbling affects DISPLAY only; all verifications read files via Python
   UTF-8 and assert on bytes/values, never on console text.
4. MASTERY status ladder is deterministic & documented in build_mastery docstring;
   conservative default (`unstable`) for non-empty non-mastered non-weak states.
5. import_grading is ATOMIC by design: any violating row aborts the whole file
   (ledger integrity over partial acceptance) — deviation from a possible row-level
   reading of §6, deliberately chosen and documented in its docstring.

## 12. Verification additions for Group O (extend §6 checklist)

13. **Index**: `python tools/build_catalog_index.py --check` → PASS; file has BOM,
    131 data rows; prefix counts SM=18·SM2=33·K=12·T=12·W=4·science=37·social=7·history=8.
14. **Ledgers**: all four S01/share TSVs start with EF BB BF; WEAK_LEDGER row 2 has
    10 columns, col6=`found`; ATTEMPT_LOG header-only (empty); MASTERY=131×unmeasured.
15. **Regeneration conformance (§6)**: `python tools/build_mastery.py --check` → PASS
    (real MASTERY equals regeneration from empty log).
16. **Dry-run artifacts**: rerun the fixture commands from PRD Group O4 in a fresh temp
    dir — expect appended rows, SM2-13 last3=`oa-` status unstable, invalid-row run
    exits 2 with zero appends, report HTML contains no external refs.
17. **Plan coherence**: plan_3layer_architecture.md §7 shows P0/P1/P3 checked, P2 blocked,
    P4 partial; frontmatter status mentions arbiter wait.
18. **Nothing committed**: git log unchanged; working tree additionally holds new
    tools(4)+index.tsv+S01/+share/+meta.yml (~+15 paths).

## 13. Group P — rulings applied (post-arbiter, added 260825 final)

Claude Code returned six `*_ruling.md` files (tier-3). Independent re-verification by the
main loop confirmed every load-bearing claim before application: A1 reproduced (t1 RE
fails exactly the six E-slot tags, amended RE 40/40), QS-4 premise false (CODE_REGISTRY
L20/L46/L38 + english.md L17/L113 all real), B1 bands machine-checked against answer-key
grids, H-citations landed line-by-line. Then the coordinator applied:

| Track | Applied | Acceptance |
|---|---|---|
| Code (07+12) | CB2 F9 reset fix first → CB1 amended RE + SUBJECT_MAP §5.8 + frontmatter priority (parser.js & md2quiz.py behaviour-identical) → CB3 app.js four-state O/△/X// + 🧾 TSV export (§5.1 12 cols, BOM) · QUIZ_STANDARD rewrite (four-slot standard + tolerance rule, §5.8 reference, schema df/traps/auxTypes/tagExtra + set-meta contract, CB4 replaced by registry cross-ref) | **node harness PASS — 모의40: 40 problems / 40 typeId / 40 tier / 6 traps / 1 aux** (python mirror identical) |
| science.md | P1–P15 (40 exact-match substitutions): per-round band table w/ 26-mid shift, map notation + item numbers, 장석 correction + composite dual-attribution, round swaps (P4–P7·P11·P12), P14 bounds machine-re-derived, P15 untyped-item register | 이력 rows + 금지·주의 on swapped types |
| history.md | Q1 measured table · Q3 with the mandatory 24-final clause · P4/P5 round fixes (의정부/육조 = 24기말 #4·5, printed numbers) · P6 조광조/삼강행실도 = 24기말 **번호 미확정** (alignment non-unique ⇒ not pinned, per ruling fallback) · E-6 created minimal + full 30-item inventory · E-5 stars re-derived | 금지·주의: keyword-search failure lesson |
| english/social | relabel ×2 (science excluded) · W-01 condition strengthened, 24중간 서답형3→W-04 (content verified: 저자-학생 대화 조언 L92) · T-11→T-02 move recorded · P2 numbers withheld (raw distinct sets only) · backlogs registered in 미결 | |
| math/korean | Q1(b)-extended wording (중간18 확정 / 기말19+미완22·23 / 9번 후보 추정) · P2 단답20+서술4 · P3 기말 단답23 단독 · P5 확정/추정 병기 의무 금지·주의 · korean P6 선택형 한정(세부 1.5 명시) · 매체 신설 CODE_REGISTRY §5 예약 행 | |

Ledger sync: `_index.md` R3 ruling rows ×6 (state: approved, reflect_state fixed),
report statuses submitted→approved ×6, HISTORY status column ×6, REV_LOG application-trace
section appended. Nothing committed.

## 14. Verification additions for Group P

19. **Acceptance rerun**: `node -e` harness on 모의40 → `problems=40 typeId=40 tier=40
    traps=6 aux=1 extra=0`; trap items 21·26·29·33·34·35 match the census.
20. **Mirror parity**: python `convert_file` returns identical counts (40/40/40/6/1).
21. **Substitution integrity**: all catalog edits applied via exact-match pairs with
    count==1 assertion (science 9+31, history 13+2 blocks, eng/so 8+6, math/kor 6+6,
    registry 1) — zero MISS on final runs.
22. **Ledger coherence**: `_index.md` has 18 data rows (12 prior + 6 t3); grep
    `status: submitted` over analysis/rev reports = 0; HISTORY shows approved ×6.

## 15. Group P-wrap — closing the three leftover items

| Item | Action | Verification |
|---|---|---|
| plan §7 P2/P4 + status | P2 cell → `[x]` (Group P, ruled order, acceptance numbers cited; browser-click check deferred to first real use) · P4 frontmatter clause → done · frontmatter `status:` → 완료 | read-back greps |
| 07-CB4 body slot | 모의40 item 16 body tag now `[SM2-13 · T4 · DF1·DF2·DF5·DF8 (+SM2-11)]` per QS canonical form | W7: exactly one occurrence |
| Parser paren-aux robustness | classifyTail (js+py mirrors) extracts `(+ID)` even when it shares a `·`-token with the last DF code — the QS-documented spacing previously misrouted it to tagExtra | acceptance rerun `40 40 40 6 1 extra=0`, python parity identical |
| 모의40 frontmatter | `set_id: SET-260822-math2-40 / subject_code: math2 / scope_confirmed: false / intended_use: practice` inserted (QS contract verbatim) | data.js exposes setId+scopeConfirmed:false badge |
| Input-scope guard | md2quiz main now skips non-quiz md under output/ (no answer table AND <3 body tags) — planning docs (PRD·migration ledger·plan) no longer pollute data.js: **14 → 6 sources**, problems still 65 | X1 skip log lists all three; X3 exclusion assert |

## 16. Verification additions for Group P-wrap

23. **Post-CB4 acceptance**: node harness `40 40 40 6 1 0` (traps/aux unchanged — table
    aux wins over body aux via conditional fill, no duplicates).
24. **Mirror parity after classifyTail change**: python `40 40 40 6 1 0`.
25. **Badge exposure**: rebuilt `web/data.js` carries `SET-260822-math2-40`,
    `scopeConfirmed: false`, `practice`; index.html rebuilt (121,552 B, external refs 0).
26. **Guard regression**: quiz part-files still converted (6 sources incl. _part1–4),
    only planning docs skipped.
