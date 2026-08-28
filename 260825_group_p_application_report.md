---
title: "Group P application report — six rulings applied & verified"
created: 260825
author: opencode main loop (ox-alpha session)
scope: Post-arbiter application phase (rulings 07–12) + independent pre-checks
purpose: Self-contained verification package for Claude Code (rev-arbiter class)
location_note: Repo ROOT by the same user convention as 260825_session_report.md.
related: [260825_session_report.md](260825_session_report.md) covers Groups K–O.
---

# Group P Application Report — 260825

## 0. 요약 (Korean executive summary)

Claude Code(rev-arbiter)의 판정서 6건을 받은 뒤, 메인 루프가 **반영 전 독립 재검증**을
먼저 수행해 판정의 하중을 받는 주장(A1 RE 실패 6건·QS-4 사실오류·B1 배점 밴드·H 행번호
인용 등)을 전부 원본 데이터로 재실행해 확인했다(모두 성립, 경미한 인용 소소착오 2건만 기록).
이어 판정서가 지정한 순서대로 반영했다: **CB2(F9 섹션 리셋) 선행 → CB1 수정 RE+12-CB1
QUIZ_STANDARD 개정 한 변경세트 → CB3 app.js 4상태 채점+TSV 내보내기**, 그리고 카탈로그
5종(science·history·english·social·math1·korean)+CODE_REGISTRY 예약 행. 코드 트랙은
판정서의 수용기준을 node 헤니스로 통과했다 — **모의40: 40문항 / typeId 40 / tier 40 /
함정코드 6 / 보조 1**(파이썬 미러 동일). 원장(_index R3 6행·검토서 status approved ×6 ·
HISTORY ×6 · REV_LOG 반영 흔적 절)까지 동기화했다. 커밋은 없다.

```
Pipeline : [t1⇄t2]▶[arbiter rulings]▶[독립 재검증]▲▶[CB2→CB1+QS→CB3]▶[catalogs ×6]▶[ledger sync]
Next     : 사용자 확인 → (필요 시) 커밋 지시 / 다음 주기: 미결 이월분 처리
```

## 1. Pre-application re-verification (not quote-trust)

Every load-bearing ruling claim was re-executed against source artifacts before any edit.

| # | Ruling claim | Re-verification method | Result |
|---|---|---|---|
| RV-1 | 07/A1 — t1's corrected RE fails exactly 6 body tags | ran both REs over all 40 body tags of 모의40 | t1 RE fails = 6 (L216·259·294·346·354·362); amended RE = 40/40; failing set == SM2-18·25·24·29·28(T3)·28(T4) |
| RV-2 | 07/A1 — E codes are a registered family | TYPE_MASTER ~L159 window + CODE_REGISTRY 함정 family grep | present |
| RV-3 | 07 — answer table "39 plain + 1 aux" | row census `\|\s*\d+\s*\|…ID·T\d` | 40 rows; exactly one `(보조 SM2-11)` at L446 (item 16) |
| RV-4 | 12/QS-4 overturn | CODE_REGISTRY L20 (`T/W → english.md` row), §3 L46 (`english → T·W`), §2 L38 (T-01 vs T2 rule), english.md L17 `T-01` / L113 `W-01`, example file is an English paper tagged `[T-01·T2]` | all present ⇒ premise of QS-4 indeed false |
| RV-5 | 08/B1 band table | parsed both 2025 정답.txt grids; quoted science columns found verbatim as the stride-5 column at offset 4 (25기말 min/max 3.0/3.9, 25중간 2.3/2.7); 2024 endpoints present in question-txt marks | confirmed (26중간 3.4~4.0 remains scan-attested by t1+arbiter, not machine-re-run here) |
| RV-6 | 08 content-line citations | 16 line citations window-checked (책상237·원궤도247·마이토콘드리아292·단백질300·양파201·관성 단답1@257-259…) | all resolve |
| RV-7 | 09 H-citations | direct reads: 강감찬/윤관@172, 관리선발@164, 지방행정구역@179, `[4-5]`@40+3.7@44+3.8@50, 설순/행실@58, 조광조@75, 정효공주@157, 삼강행실도 never named corpus-wide, H7 keyword census exact, 24기말 고려11·조선11 | all confirm |
| RV-8 | 10/E3·E6·C1 | Chaparral 추론[3.5점]@L58-66 no graph/table; 통사 기말 5점×4/중간 10점×4 zones; raw distinct sets contain 2.0 (three rounds) & 4.0 (two) ⇒ "2.1~3.6" unsafe | confirmed |
| RV-9 | 11 student-doc facts | wrong_analysis_math L28/L57, diag v2 L35/L36/L59 read directly — incl. the arbiter's addition (기말 확정19+미완22·23) which IS in diag L36 | confirmed; korean raw min 1.5 @25기말 L52-53 inside 서답형 sub-item |
| RV-10 | Procedure compliance (write surface) | git status scan: web/parser.js·app.js·tools/md2quiz.py·docs/QUIZ_STANDARD.md·catalog/*.md·legacy student docs all UNMODIFIED by arbiter; reports stayed `submitted`; `_index.md` untouched | compliant |

Recorded nits (do not affect verdicts): ruling 12 cites the example as
`공통영어1_모의문제_25.md` while the actual name is `공통영어1_모의25.md`, and quotes a
literal `"subject": "english"` that the file does not contain (Englishness is evident from
content/tags). CC's chat summary said package 08 has 20 ruling rows; the table has 19
(all 19 decision items ruled — nothing missing). Six rows carry an empty evidence cell
with the rationale living in the note/approve text.

## 2. Code track — applied in the ruled order

Order enforced: **CB2 first** (F9 observable-zero otherwise), then **CB1+12-CB1 as one
change-set**, then CB3.

### 2.1 CB2 — F9 section reset (parser.js + md2quiz.py, behaviour-identical)

Root cause reproduced: unit headers (`## I-2 직선의 방정식 …`) reset the question zone,
so sections came out empty (`problems=0`). Fix in both implementations: section state is
driven ONLY by type keywords (선택형 / 서답형·서술형·단답형 / 정답·해설) at any heading
level; other headings are kept as zone content (splitProblems still flushes the previous
block there); trailing auxiliary sections (채점 기준·요약·검증) never change state.

### 2.2 CB1 (amended) — tag pipeline

- `BODY_TAG_RE` = arbiter's tested four-slot form; `CELL_TAG_RE` handles bracketless
  answer cells with optional `(보조 ID)`.
- Tail classifier: `DF\d→df[]`, `E\d→traps[]`, `+ID→aux[]`, unknown → `tagExtra[]`
  (never discarded — principle 3).
- Slots merge regardless of where typeId came from (table or stem/stimulus — tags may sit
  in the passage line).
- SUBJECT_MAP completed to the seven §5.8 codes (math1/math2 split via 공통수학2·도형의
  방정식 keywords; social·history added; legacy `math` retired).
- YAML frontmatter priority: `subject_code` overrides inference; `scope_confirmed`
  absent ⇒ false (fail-safe, §5.8); setId/unit/intended_use captured.

### 2.3 12-CB1/CB2/CB3/CB4 — QUIZ_STANDARD rewrite

Four-slot standard + tolerance rule documented; section-state rule written down;
subject mapping now references DATA_STANDARD §5.8 instead of restating it; schema adds
`df[]/traps[]/auxTypes[]/tagExtra[]` plus the set-meta frontmatter contract and extended
`sources[]`; CB4 executed as the ruled replacement — example IDs kept, one cross-reference
line to CODE_REGISTRY §1/§2 added.

### 2.4 CB3 — app.js four-state scoring + ledger export

Marks = correct/unsure/wrong/blank (§4.1 enum; UI O/△/X//). Choice items keep auto O/X;
essay mark-row gained △ and /(백지) buttons. New 🧾 export builds ATTEMPT_LOG §5.1's 12
columns (`set_id,qnum,main_type,aux_types,tier,df,mark_code,…`), UTF-8 **with BOM**, ready
for `tools/import_grading.py`.

### 2.5 Acceptance (ruled criterion)

```
node harness (web/parser.js on 모의40):
  problems=40  typeId=40  tier=40  traps=6  aux=1  extra=0
  trap items: 21(SM2-18·E5) 26(SM2-25·E5) 29(SM2-24·E9) 33(SM2-29·E5) 34(SM2-28·E5) 35(SM2-28·E9)
  aux item : 16(SM2-11)
python mirror convert_file(): identical counts.
Rebuilds: web/data.js regenerated; web/index.html rebuilt via build_web.py (external refs 0).
```

Engineering trail (honest): two intermediate defects were caught by the harness itself —
(i) table-sourced answers didn't merge stem-side slots (traps=0), fixed by unconditional
merge; (ii) slots live in stimulus lines, not stems, so the body is scanned when the stem
has no tag. Both fixes applied symmetrically to parser.js and md2quiz.py.

## 3. Catalog track — approved fixes applied

All edits were executed as exact-match substitution pairs with a `count==1` assertion
(any MISS aborts the whole pass; final runs had zero MISS).

| File | Ruling | Applied (highlights) | Substitutions |
|---|---|---|---|
| science.md | 08 P1–P15 | P1 per-round band table + "26중간부터 3.4~4.0 상향"(26기말 미측정) · P2 map notation GB ●●●(+단답)/GT ● + legend + real item numbers into GB/GT freq fields · P3 장석51% correction + composite dual-attribution annotations on CH-05·CH-06 · P4 BI-03 24중간→24기말 · P5 관성 = 24기말 단답형1, 25중간 **20번**(버스 보기 ㄱ) · P6 renumbering (18/19·20·23/24) · P7 −1 shift + 물순환 15번 → ER-05 · P8 Li+H₂O → CH-04 · P9 8→14 · P10 stray 서술형 refs removed · P11 7번 · P12 4회 + map cell · P13 26기말 24번 · P14 bounds machine-re-derived before writing (condition met) · P15 untyped candidates registered | 9 + 31 |
| history.md | 09 | Q1 measured per-round structure table · Q3 sentence **with the mandatory 24기말 clause** · preamble relabel (inherited 10/Q1-b) · P4 F-02 → 24중간 · P5 관리선발·5도양계 → 24중간, 의정부/육조 = 24기말 **4·5번** (numbers printed in source) · P6 조광조·삼강행실도 = 24기말 **번호 미확정** — point-column pinning attempted, alignment starts {0,1,2} non-unique ⇒ not pinned, per the ruling's fallback · Q2(b) E-6 created minimal (주제 축 + counts) **plus full inventory** 선택 2–24(+1 미추출)·단답 1–6 · F-nn extension rule noted scoped `한국사:F-nn` · E-5 stars re-derived ('2025 기말 핵심' premise corrected) · keyword-search-failure 금지·주의 on swapped types | 13 + 2 blocks |
| english.md | 10 | relabel ×1 · P1 서답형 5~6 · P2 numbers withheld — raw distinct sets recorded ({1.0~6.0}/{2.0~8.0}/{2.0~10.0}×2) + sel/sa separation left as 미결 (naive sectioning hit the cover page; honest failure recorded) · P3 T-11 '25중간 4' → T-02 pure-inference (move recorded in both entries) · Q2 W-01 condition strengthened; '24중간 서답형3' removed after content check (저자–학생 대화 조언 @L92 = W-04 pattern) · Q3 backlog registered | 8 |
| social.md | 10 | relabel ×1 · P5 exact wording (중간 10점×4 / 기말 5점×4, 세부 1~6 가변) in preamble+F-07+guide · P7 2025 split (중간 ~3.3 verified in grid / 기말 3.5~5.0) · P6 D-7 실업률 서술형4 → 24중간(L251) · P9 backlog registered | 6 |
| math1.md | 11 | P1 중간 2.7~4.x / 기말 ~5.0 · P2 guide 단답형 20+서술형 4 · P3 기말 후반 = 단답형 10~23 (미결 wording fixed) · P4 단답=답만/서술=과정 구분 · P5 Q1(b)-extended paragraph (중간18 확정·기말19+미완22·23·9번 후보 추정) + 금지·주의 "확정/추정 병기 의무" | 6 |
| korean.md | 11 | P6 "**선택형** 1.7~4.0" + 서답 세부 1.5 명시 · P7 K-01 L71-79 anchor · P8 K-09 17·19·21+18·20(<보기>) · P9 제29항 ㄹ→ㄷ (이튿날=제28항, K-04 link kept & relabelled) · Q3/P10 backlog + 매체 신설 note | 6 |
| CODE_REGISTRY.md | 11-Q3 | §5 new rule: 매체 영역 신설은 기존 `K` prefix 아래 신규 번호, registry pre-registration required (reservation recorded; catalog-local minting forbidden) | 1 |

Every round-attribution fix carries an 이력 row (`260825 — 검토서 NN/판정 NN 반영`) and,
where the error was an attribution swap, a 금지·주의 line per REV_GUIDE §7 / ruling
conditions. science.md is deliberately NOT relabelled for 2026 scans (ruling 10 explicitly
excludes it — its 2026 citations are item-level).

## 4. Ledger sync

- `analysis/rev/_index.md`: header → `state: approved | round: 3 | waiting: -`; six t3
  rows appended (reflect_state `flagged→fixed`, next action notes REV_LOG trace).
  Now 18 data rows total.
- Review reports 01–06: frontmatter `status: submitted → approved` (main-loop surface).
- `analysis/rev/HISTORY.md`: status column ×6 → `approved(판정 반영)`.
- `analysis/REV_LOG.md`: new section 「판정 반영 (owner apply — 메인 루프, 260825)」 with
  six trace rows (rule 4: no silent rewrites).
- `docs/DATA_STANDARD.md` §7 exception row for QUIZ_STANDARD marked 해소(260825).
- Regeneration checks still green: `build_catalog_index.py --check` (131 rows),
  `build_mastery.py --check` PASS.

## 5. Honest deviations & notes for the auditor

1. **Pre-existing drift in output/260822**: HEAD (commit 5e0b04d) already contains 3
   E-slot tags; the working tree has 6 (plus `_part3/_part4` edits). This is uncommitted
   evolution from the earlier 260822 session — Group P made **zero** writes to
   output/260822/*.md (all today's catalog/doc writes are enumerated in §3–4). The
   arbiter's A1 census ran on the working tree, which is also what md2quiz/parser consume.
2. English per-round selected/essay band separation was attempted and failed honestly
   (cover-page false positive); raw distinct sets were installed and the separated bands
   remain a registered 미결 item — matching ruling 10-P2's "only the lower bound 2.2 is
   settled" restraint.
3. History P6 item numbers intentionally left unpinned (non-unique alignment), per the
   ruling's explicit fallback — do not "helpfully" add numbers later without evidence.
4. Console CP949 mojibake affects display only; every check above asserts on bytes/values
   read as UTF-8 inside Python/node.

## 6. Independent verification checklist (reproducible)

1. **Acceptance rerun**:
   `node -e "const fs=require('fs');global.window={};eval(fs.readFileSync('web/parser.js','utf8'));const p=window.QuizParser.convertText(fs.readFileSync('output/260822/공통수학2_도형의방정식_모의40.md','utf8'),'m').problems;console.log(p.length,p.filter(x=>x.typeId).length,p.filter(x=>x.tier).length,p.reduce((a,x)=>a+x.traps.length,0),p.reduce((a,x)=>a+x.auxTypes.length,0))"`
   → expect `40 40 40 6 1`.
2. **Python parity**: `python -c "import sys;sys.path.insert(0,'tools');import md2quiz;
   r=md2quiz.convert_file('output/260822/공통수학2_도형의방정식_모의40.md','m');
   p=r['problems'];print(len(p),sum(bool(x['typeId']) for x in p),sum(bool(x['tier']) for x in p),sum(len(x['traps']) for x in p),sum(len(x['auxTypes']) for x in p))"`
   → expect `40 40 40 6 1`.
3. **F9 regression**: revert-test optional — old logic produced `problems=0`; current
   splitSections keeps unit headers as content (grep `## I-2 직선의 방정식` handling).
4. **QUIZ_STANDARD**: contains 네 슬롯 standard, tolerance/tagExtra rule, §5.8 reference
   (no restated subject table), schema fields `df/traps/auxTypes/tagExtra`, set-meta block,
   and the CB4 replacement line citing CODE_REGISTRY §1/§2; T-01/W-01 untouched.
5. **Catalog spot greps**: science `3.4~4.0(상향)` & `복합((가) 광물 비율 ↔ (나) 생명체
   물질 비율)` & `6회 중 4회`; history `E-6 근거 문항 목록` & `24기말 = 근대사 단독`(bold-
   stripped) & `번호 미확정`; english `전제 조건: 문법-필수 지시…`; social `중간 10점×4(서술형)
   / 기말 5점×4`; math1 `기말 19번 확정 오답(+미완 22·23)` & `확정/추정 등급을 반드시 병기`;
   korean `선택형 1.7~4.0점` & `1.5점까지 내려감`; registry `매체 영역(국어) 예약`.
6. **Ledger**: `_index.md` data rows == 18 and header `state: approved`;
   `grep "status: submitted" analysis/rev/*.md` over reports == 0 hits; HISTORY shows
   `approved(판정 반영)` ×6; REV_LOG ends with the owner-apply section (≥6 rows referencing
   `_ruling.md`).
7. **Regenerators**: `python tools/build_catalog_index.py --check` and
   `python tools/build_mastery.py --check` both exit 0.
8. **Nothing committed**: `git log --oneline -1` still `5e0b04d…`; all changes live in
   the working tree/index awaiting user instruction.

# history
- 260825: created by main loop after applying rulings 07–12; documents pre-application
  re-verification, ordered code track with acceptance run, catalog substitutions with
  exact-match integrity, ledger sync, deviations, and this checklist.
