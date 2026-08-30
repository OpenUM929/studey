# EX-math2-20252M Sol 독립 근거 감사 보고서

Pipeline: EX-math2-20252M preflight → author complete → **independent evidence audit complete (REVISE)** → adversarial review → gatekeeper
Stage: Codex/OMX = gpt-5.6-sol — 22개 ID·17개 동결 입력·3개 author 산출물을 독립 재검사했다. ID/형식/정본 ID gate는 통과했으나 `items.tsv`의 S-17·S-18 한국어 데이터가 문자 `?`로 훼손되었고 W-04 인용 범위가 frozen span과 달라 author gate의 `warnings=0/failures=0`은 완전성 증거가 아니다.
Team: mode=actual-team; lead=independent evidence auditor | gpt-5.6-sol | evidence-auditor | completed; lanes=evidence-auditor = gpt-5.6-sol = high | independent evidence auditor | audit | completed | exclusive output `output/260828/diagnostic/math2-method-comparison/codex-team/audit/EVIDENCE_AUDIT_260828.md` | `.codex/agents/assessment-evidence-auditor-sol.toml`; independence=independent; planned/unavailable/failed lanes=none
Next: gatekeeper는 author가 S-17·S-18 행의 훼손을 고치고 W-04 citation span을 frozen schema와 정합화한 뒤 동일한 독립 content-integrity gate를 재실행할 때까지 comparison/external relay를 시작하지 않는다.

## 1. 판정

- **권고: `REVISE`**
- 외부 역할 승인이나 정식 `type-proposer` 승인 판정이 아니다.
- 진단 내용의 대부분은 transcript와 정본에 부합하고 22-ID exact cover도 통과한다. 그러나 acceptance schema의 per-item record는 단순 비공란이 아니라 의미 있는 한국어 기록이어야 한다. `author/items.tsv:22-23`은 합계 389개의 리터럴 `?`를 포함해 S-17·S-18의 배정·근거·Tier 근거·함정 필드를 실질적으로 읽을 수 없다.
- 모든 문항은 `pNN.png`가 0개이므로 formal proposer readiness는 계속 **BLOCKED**다. S-17은 별도로 `f` 정의가 없어 원천 수준에서도 **BLOCKED**다(`corpus/EX-math2-20252M/transcript.md:134-136`, `corpus/EX-math2-20252M/verify_log.tsv:8`).

## 2. 런타임·독립성·쓰기 경계

| 항목 | 관측값 | 판정 |
|---|---|---|
| native canonical task identity | `/root/math2_sol_evidence_audit` | PASS |
| lane/model/depth | `evidence-auditor = gpt-5.6-sol = high` | PASS |
| persona/role | independent evidence auditor / unsupported-claim disproof | PASS |
| role instruction | `.codex/agents/assessment-evidence-auditor-sol.toml` | PASS |
| target-role instruction | `.claude/agents/type-proposer.md` | PASS |
| opaque host ID | 런타임이 별도 ID를 노출하지 않았으므로 추론·기재하지 않음 | PASS |
| exclusive output | 이 파일 한 개만 작성 | PASS |
| prohibited exposure | Opus 제출물, 이전 Codex diagnostic/trace, critique 산출물은 읽지 않음 | PASS |
| child/external dispatch | 없음 | PASS |

독립 context 근거: author draft를 읽기 전에 아래 §3의 1~4단계를 완료하고, transcript에서 직접 22개 heading ID와 source span을 재구성했으며, 정본을 대조해 독립 분류 기준을 먼저 세웠다. 그 뒤에만 frozen checker와 author 산출물을 열었다.

## 3. 필수 읽기 순서 로그

1. **역할/목표 역할 먼저**: `AGENTS.md`, `.codex/agents/assessment-evidence-auditor-sol.toml`, `.claude/agents/type-proposer.md`를 읽었다. 목표 역할의 핵심은 page evidence 필수, affected item `BLOCKED`, 5~12 type consolidation, 정본/ledger read-only다(`.claude/agents/type-proposer.md`, Absolute rules 1~6 및 Procedure 1~8).
2. **preflight/schema/gate**: `TEAM_PREFLIGHT_260828.md`, `AUTHOR_INPUT_MANIFEST_260828.tsv`, `EXPECTED_ITEM_IDS_260828.tsv`, `ACCEPTANCE_SCHEMA_260828.md`, `check_experiment.py`, 두 비교 manifest를 읽었다. `TEAM_PREFLIGHT_260828.md:9-13`은 22 items/152 lines/3 bindata/no pNN/answer_key null/S-17 defect를 고정하고, `ACCEPTANCE_SCHEMA_260828.md:3-16`은 per-item 10필드와 aggregate 10개 항목을 고정한다.
3. **동결 입력을 직접 감사**: author manifest 17파일의 byte/SHA-256을 재계산해 17/17 PASS를 확인했다. 그 뒤 transcript/meta/verify_log, 3 bindata, `_README`, `math2.md`, `COMMON_TYPES.md`, `TYPE_MASTER.md`, `DIFFICULTY_RUBRIC.md`, `CODE_REGISTRY.md`, curriculum, forecast guide, assurance guide, AGENTS를 직접 읽었다. transcript heading에서 author와 독립적으로 기대 ID를 생성했다.
4. **독립 source finding 선확정**: W-01..S-18의 내용 축을 먼저 분류했다. 핵심 기준은 SM2-01/02/03/07/08/09/10/11/12/13/15/19/21/25/26/27/31/33 정본 정의, S-05·S-12 decision-request 필요성, S-17 source-defect `BLOCKED`, S-18의 내분·수직·넓이 결합이다.
5. **그 이후 author 읽기**: 먼저 `python .../check_experiment.py --phase author`를 실행한 다음에만 `author/items.tsv`, `author/types.tsv`, `author/AUTHOR_REPORT_260828.md`를 읽고 독립 결과와 비교했다.

## 4. 동결 입력·author 산출물 해시

### 4.1 입력 manifest

- 재계산 결과: `manifest_ok=17/17`; byte mismatch 0; SHA-256 mismatch 0; missing 0.
- manifest 직접 근거: `AUTHOR_INPUT_MANIFEST_260828.tsv:2-18`.
- corpus 실측: transcript 152 lines; `meta.yml:7` items=22; `meta.yml:13` answer_key=null.
- image 실측: `corpus/EX-math2-20252M/_images/` 아래 `pNN.png` 0개; bindata 3파일은 존재하고 frozen hash가 맞지만 Pillow에서 모두 `UnidentifiedImageError`였다. 따라서 bindata 존재는 page citation 또는 rendered evidence가 아니다.

### 4.2 감사 시점 author artifact hash

| artifact | bytes | SHA-256 |
|---|---:|---|
| `author/items.tsv` | 15029 | `8316ef0a656f80de2506c3b10d5c7d9f60a10e833d36d5be71c8947d99e9fe6a` |
| `author/types.tsv` | 6987 | `acc5b56a8e0f40e3eb34b395132d0980386aecfb99c47e08b1fba55136fe3968` |
| `author/AUTHOR_REPORT_260828.md` | 16235 | `28e1f8401eff3acc27e0c5bcf36984df4a59b3ca75876bf7a06ca8897df11772` |

## 5. 재현 가능한 identifier gate

### 5.1 expected/observed set

- expected identifiers: `[W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18]`
- observed identifiers: `[W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18]`
- duplicate identifiers: `[]`
- missing identifiers: `[]`
- extra identifiers: `[]`
- 판정: **PASS**. row count가 아니라 transcript heading-derived set과 `items.tsv:item_id` set을 비교했다.

### 5.2 type membership exact cover

- expected: 위 22개 ID.
- observed membership order: `[W-01,S-02,W-02,S-06,W-03,W-04,S-03,S-15,S-01,S-04,S-18,S-05,S-13,S-07,S-14,S-08,S-09,S-10,S-12,S-11,S-16,S-17]`
- duplicate: `[]`; missing: `[]`; extra: `[]`.
- groups: 9개로 허용 범위 5~12 안이다.
- 판정: **PASS**. `author/types.tsv:2-10`의 `member_item_ids`를 분해해 집합 차이와 중복을 직접 계산했다.

## 6. source existence·citation·page availability

| check | evidence | 판정 |
|---|---|---|
| 17 frozen inputs 존재/해시 | manifest rows 2~18 재계산 17/17 | PASS |
| transcript-derived item headings | `transcript.md:31-146`에서 W 4개, S 18개 | PASS |
| items primary source path 존재 | `author/items.tsv:2-23`의 첫 citation path 전부 존재 | PASS |
| primary source span | 21개는 frozen span과 동일. W-04만 author `44-48`, frozen expected `44-51` | **FAIL (비치명)** |
| W-04 material support | 실제 문항 본문은 `transcript.md:44-48`; frozen `44-51`은 blank와 다음 section header를 포함 | PASS (내용 근거), 단 exact-span 정합 필요 |
| canonical citation locations | 각 SM2 rationale가 인용한 `math2.md` 범위에 해당 ID 정의가 존재 | PASS |
| registered type IDs/prefix | 사용된 SM2 ID 19개 모두 `CODE_REGISTRY.md:17-19`의 `SM2` 및 `math2.md`의 SM2-01..33에 존재 | PASS |
| pNN pages | glob 결과 0; author도 전 행 `BLOCKED-no-pNN` | **BLOCKED** |
| bindata | 3파일 존재·hash PASS이나 모두 일반 image decoder에서 식별 실패 | **BLOCKED as rendered evidence** |
| S-17 f definition | transcript와 verify_log가 정의 부재를 직접 명시 | **BLOCKED** |

## 7. 22개 per-item 근거 감사

`PASS`는 transcript-level diagnostic assignment와 limitation 처리의 지지 여부다. 별도의 formal page-evidence gate는 전 문항 `BLOCKED-no-pNN`이다.

| ID | 독립 source/type finding → author 비교 | direct evidence | 판정 |
|---|---|---|---|
| W-01 | 수직 직선 결정 → SM2-08 일치 | `transcript.md:31-34`; `math2.md:147-153`; `items.tsv:2` | PASS |
| W-02 | 지름 양끝점으로 원 결정 → SM2-15 일치 | `transcript.md:35-38`; `math2.md:234-242`; `items.tsv:3` | PASS |
| W-03 | 평행이동 후 x축 대칭 합성 → SM2-31 일치 | `transcript.md:39-43`; `math2.md:407-415`; `items.tsv:4` | PASS |
| W-04 | 포물선 이동 역추적+평행선 거리 → SM2-27/11 내용 일치. 단 frozen exact span과 불일치 | `transcript.md:44-48`; expected file row 5=`44-51`; `items.tsv:5`=`44-48` | **FAIL (citation span)** |
| S-01 | 내분점 직접 계산 → SM2-03 | `transcript.md:52-54`; `math2.md:78-86`; `items.tsv:6` | PASS |
| S-02 | 평행·수직 계수 결합 → SM2-08 | `transcript.md:55-59`; `math2.md:147-153`; `items.tsv:7` | PASS |
| S-03 | 점 이동 후 직선 위 → SM2-26 | `transcript.md:60-64`; `math2.md:354-360`; `items.tsv:8` | PASS |
| S-04 | 내분점+수직직선 → SM2-03/08 | `transcript.md:65-69`; cited canonical ranges; `items.tsv:9` | PASS |
| S-05 | 매개 직선 교점의 제1사분면 범위; exact catalog match 없음 → ID-free decision request 적절 | `transcript.md:70-73`; `math2.md:137-145`; `items.tsv:10` | PASS |
| S-06 | 원 결정+축 현 길이 → SM2-15/19 | `transcript.md:74-78`; `math2.md:234-242,275-281`; `items.tsv:11` | PASS |
| S-07 | 원 위 점-직선 거리 극값을 정삼각형 넓이로 환원 → SM2-25/11 | `transcript.md:79-81`; `math2.md:176-183,337-343`; `items.tsv:12` | PASS |
| S-08 | 외심·등거리 → SM2-01 | `transcript.md:82-85`; `math2.md:52-61`; `items.tsv:13` | PASS |
| S-09 | AP=BP 자취/수직이등분선+포물선 조건 → SM2-01/09 | `transcript.md:86-88`; `math2.md:52-61,156-163`; `items.tsv:14` | PASS |
| S-10 | 두 축 경유 거리합 최소를 대칭으로 환원 → SM2-33 | `transcript.md:89-93`; `math2.md:439-452`; `items.tsv:15` | PASS |
| S-11 | 두 직선 동시 접원 중심=등거리 자취 → SM2-12 | `transcript.md:94-96`; `math2.md:187-195`; `items.tsv:16` | PASS |
| S-12 | 축 위 자유점의 거리차 극값; SM2-02 exact pattern 밖 → ID-free decision request 적절 | `transcript.md:97-100`; `math2.md:65-74`; `items.tsv:17` | PASS |
| S-13 | 직선 다발+점-직선 거리 최대 → SM2-10/11 | `transcript.md:101-104`; `math2.md:166-183`; `items.tsv:18` | PASS |
| S-14 | 원 위 정수 기울기 점 개수 → SM2-25의 개수/경계 축 | `transcript.md:105-107`; `math2.md:337-343`; `items.tsv:19` | PASS |
| S-15 | 이동을 f(x,y) 식으로 판정 → SM2-31. C-01/C-09 boundary request는 과도한 확정 없이 보류 | `transcript.md:108-119`; `COMMON_TYPES.md:66-94`; `items.tsv:20` | PASS |
| S-16 | 예각 이등분선+원 위 접선 → SM2-12/21 | `transcript.md:120-123`; `math2.md:187-195,293-300`; `items.tsv:21` | PASS |
| S-17 | source defect를 BLOCKED로 둔 방향은 맞지만 per-item 필드 225개 `?`로 훼손되어 rationale/tier/trap 검증 불가 | `transcript.md:124-137`; `verify_log.tsv:8`; `items.tsv:22` | **FAIL (artifact); source BLOCKED** |
| S-18 | report의 내분+수직+넓이 진단은 source와 대체로 맞지만 required per-item 필드 164개 `?`로 훼손 | `transcript.md:138-146`; `AUTHOR_REPORT_260828.md:88-89`; `items.tsv:23` | **FAIL (artifact)** |

결과: transcript-level PASS 19, FAIL 3(W-04 exact citation, S-17/S-18 content integrity). 별도 formal page evidence BLOCKED 22/22; source-defect BLOCKED 1(S-17).

## 8. consolidation·importance·COMMON_TYPES·catalog 감사

| 항목 | evidence | 판정 |
|---|---|---|
| 5~12 reusable groups | 9 groups, `types.tsv:2-10` | PASS |
| membership exact exclusive cover | duplicate/missing/extra 모두 0 | PASS |
| variation axes ≥2/group | 두 axis 열 모두 9/9 비공란이고 관측 문항 간 실제 차이를 기술 | PASS |
| observed traps | 9/9 비공란; item source 구조와 정본 함정 축에 부합 | PASS |
| source-axis importance | 기출축 `★(2025-2M 1회)`와 부교재축을 `/`로 분리; 같은 회차 다문항을 연도 반복으로 부풀리지 않음 | PASS |
| workbook star/count | SM2-08 2, 15 3, 19 2, 26 2, 27 3, 31 2, 03 2, 13 4, 07 2, 10 3, 11 주3, 25 3, 01 2, 09 4, 33 4, 02 3, 12 3, 21 2를 `math2.md`와 대조 | PASS |
| COMMON_TYPES diff | C-05/C-09 강화와 S-15 C-01/C-09 경계를 분리; 새 C-nn 미발급 | PASS |
| catalog disposition | existing diff / ID-free decision request / S-17 BLOCKED를 분리하고 canonical 적용하지 않음 | PASS |
| type semantics | DIAG-Gnn은 실험 내부 그룹이라고 명시해 canonical ID로 오인하지 않음 | PASS |
| S-17 grouping limitation | 완결 유형·importance는 부여하지 않았으나 exact cover를 위해 G09 membership만 유지 | PASS with limitation |

## 9. acceptance schema checklist

| required section/field | location | 판정 |
|---|---|---|
| per-item 10-column schema | `items.tsv:1` exact column equality | PASS |
| 22 unique IDs | `items.tsv:2-23` | PASS |
| meaningful per-item contents | S-17/S-18 literal `?` corruption | **FAIL** |
| identifier lists | `AUTHOR_REPORT_260828.md:27-37` | PASS |
| consolidation 5~12 | report `:93-107`, `types.tsv:2-10` | PASS |
| ≥2 observed axes/type | `types.tsv` axis columns | PASS |
| observed traps | items/types trap columns, report `:119-125` | PASS except corrupted S-17/S-18 item rows |
| source-axis importance | report `:127-133`, types importance column | PASS |
| COMMON_TYPES comparison | report `:135-146` | PASS |
| catalog update disposition | report `:148-161` | PASS |
| HARVEST_LOG draft | report `:163-174` | PASS |
| EXTRACTION_LOG draft | report `:176-187` | PASS |
| no pNN/S-17/answer_key limitations | report `:189-198`; corpus evidence | PASS/BLOCKED as declared |
| runtime/method/exclusive output | report `:12-25`, `:39-62` | PASS |
| deterministic output | report `:200-229` and fresh rerun | PASS mechanically, **insufficient semantically** |
| Korean artifact language | report/types are Korean; items S-17/S-18 are materially corrupted | **FAIL** |

## 10. type-ID·prefix legality

- 사용된 정본 ID: `[SM2-01,SM2-02,SM2-03,SM2-07,SM2-08,SM2-09,SM2-10,SM2-11,SM2-12,SM2-13,SM2-15,SM2-19,SM2-21,SM2-22,SM2-25,SM2-26,SM2-27,SM2-31,SM2-33]`.
- `SM2`는 `CODE_REGISTRY.md:17-19,42-46`에 공통수학2 prefix로 등록되어 있고, 사용 ID는 모두 `math2.md` SM2-01..33 안에 존재한다. unregistered ID=`[]`.
- S-05/S-12는 새 ID를 발급하지 않고 decision request로 남겼다. PASS.
- `DIAG-G01`..`DIAG-G09`는 report `:61,95`에서 canonical type ID가 아닌 실험 내부 group label로 명시했다. 비가역 ID minting 아님. PASS.
- S-17 row의 `SM2-22` 문자열은 훼손 문맥 속 잠정 후보 언급일 뿐이며 report `:155-161`과 types `G09`는 판정을 BLOCKED로 유지한다. 다만 row 자체는 읽을 수 없어 FAIL 원인이 남는다.

## 11. material claim 감사

### PASS

1. 22 items/4+18 구조, 152 lines, answer_key null은 corpus와 일치한다(`transcript.md:16-21`, `meta.yml:7,13`).
2. no pNN, formal proposer BLOCKED, no answer claim은 실제 파일 상태와 acceptance verdict에 일치한다(`ACCEPTANCE_SCHEMA_260828.md:13-19`, author report `:7-10,189-198`).
3. S-17 정의 결손을 임의 보충하지 않은 결론은 source와 일치한다.
4. ID sets와 type exact cover는 직접 재계산해 일치했다.
5. source-axis importance를 past-exam year axis와 workbook item-count axis로 분리했다.
6. S-15를 즉시 C-01로 확정하지 않고 boundary request로 둔 것은 `COMMON_TYPES.md:21-29,66-94`와 source 사이 긴장을 정직하게 보존한다.

### FAIL/BLOCKED

1. **author 완결성 주장 과대**: report `:5,36,91,198`은 22-item complete/nonblank diagnostic을 주장하지만 `items.tsv:22-23`은 의미 보존에 실패했다. 비공란 검사는 content-integrity 검사가 아니다.
2. **checker false negative**: `check_experiment.py:103-106,119-123`은 blank만 검사하고 literal `?`/encoding corruption을 검사하지 않는다. 따라서 fresh `warnings=0`, `failures=0`, `PASS phase=author`는 S-17/S-18 완전성을 입증하지 못한다.
3. **exact citation mismatch**: W-04 frozen span은 `EXPECTED_ITEM_IDS_260828.tsv:5`의 44-51이나 author는 `items.tsv:5`와 report `:71`에서 44-48이다. 내용 증거는 충분하지만 frozen schema와 exact equality는 실패했다.
4. **rendered evidence BLOCKED**: pNN 0이고 bindata도 decoder에서 열리지 않으므로 어떤 row도 formal page citation PASS로 전환할 수 없다.

## 12. findings

### Critical

| ID | finding | direct evidence | severity | disposition |
|---|---|---|---|---|
| C-01 | S-17/S-18 per-item semantic fields가 literal `?` 225/164개로 훼손되어 acceptance schema의 의미 있는 한국어 record가 아님 | `author/items.tsv:22-23`; `ACCEPTANCE_SCHEMA_260828.md:3-5,16` | critical | author artifact 수정 후 content-integrity gate 재실행. auditor는 직접 수리하지 않음 |
| C-02 | frozen checker가 위 훼손을 검출하지 못한 채 PASS하여 gate evidence가 불충분함 | `check_experiment.py:103-106,119-123,186-193`; fresh command output | critical | gatekeeper는 `warnings=0/failures=0`만으로 다음 단계 진입 금지; literal replacement/`?` 검사 추가 또는 별도 독립 check 필요 |
| C-03 | no pNN으로 모든 formal page-evidence claim이 BLOCKED | pNN_count=0; `ACCEPTANCE_SCHEMA_260828.md:13,18-19` | critical for formal proposal, expected experiment limitation | diagnostic comparison 가능 여부는 gatekeeper가 수정본과 critic을 통합해 판단; formal proposal/approval은 금지 |

### Noncritical

| ID | finding | direct evidence | severity | disposition |
|---|---|---|---|---|
| N-01 | W-04 author citation은 실제 본문 44-48을 정확히 가리키지만 frozen expected end=51과 exact string이 다름 | expected row 5; items row 5 | noncritical | frozen range convention에 맞추거나 gate가 narrower-supporting range를 허용한다고 명시 |
| N-02 | bindata 3개가 확장자와 달리 일반 decoder에서 열리지 않음. author는 S-15에서만 명시하고 overall limitation에서는 BIN0002/BIN0003를 기록함 | Pillow independent check; author report `:50,173,194` | noncritical because no pNN already blocks | rendered evidence로 사용 금지 유지 |
| N-03 | S-04 Tier T1은 구조상 3단계로 T2 경계지만 author가 스스로 uncertainty를 기록 | `items.tsv:9`; rubric `:49-65` | noncritical | adversarial reviewer가 semantic difficulty만 재검토 |

## 13. 명령·출력 증거

### 13.1 frozen author checker

```text
python output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py --phase author
manifest_ok=17/17
expected=W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18
observed=W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18
duplicate=[]
missing=[]
extra=[]
type_membership_gate:
expected=W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18
observed=W-01,S-02,W-02,S-06,W-03,W-04,S-03,S-15,S-01,S-04,S-18,S-05,S-13,S-07,S-14,S-08,S-09,S-10,S-12,S-11,S-16,S-17
duplicate=[]
missing=[]
extra=[]
warnings=0
failures=0
experiment-gate: PASS phase=author
exit_code=0
```

### 13.2 independent content-integrity 결과

```text
ITEM-SCHEMA PASS
TYPE-SCHEMA PASS
TYPE-MEMBERSHIP duplicate=[] missing=[] extra=[] group_count=9
SOURCE-MISSING=[]
PNN-COUNT=0
UNREGISTERED_SM2_IDS=[]
ITEM-CONTENT-DEFECT S-17 literal_question_marks=225 blank=[]
ITEM-CONTENT-DEFECT S-18 literal_question_marks=164 blank=[]
MANIFEST-RECHECK=17/17
```

### 13.3 stop condition

현재 결과는 `REVISE`다. S-17/S-18 per-item row의 의미 보존과 W-04 exact-span 정합이 재검증되기 전에는 audit PASS 또는 `PASS-FOR-ADVERSARIAL-REVIEW`로 승격하지 않는다. 이 보고서는 comparison이나 external relay를 승인하지 않는다.
