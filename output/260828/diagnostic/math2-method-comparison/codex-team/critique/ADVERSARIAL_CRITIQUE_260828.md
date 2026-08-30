# EX-math2-20252M Sol author 독립 적대적 비평

Pipeline: EX-math2-20252M capability experiment → author complete → **independent adversarial critique BLOCKED** → gatekeeper integration → optional external comparison
Stage: Codex/OMX = gpt-5.6-sol — 22개 ID와 9개 통합군을 독립 재계산·비평했으나, `items.tsv`의 S-17·S-18 내용 훼손과 비평 lane의 check-script 사전 열람 순서 이탈 때문에 본 lane을 `BLOCKED`로 판정한다.
Team: mode=actual-team; lead=adversarial critic | gpt-5.6-sol | assessment-adversarial-critic-sol | completed-with-blocker; lanes=adversarial-critic = gpt-5.6-sol = high | adversarial critic | independent critique | completed, BLOCKED | `.codex/agents/assessment-adversarial-critic-sol.toml` | exclusive output `output/260828/diagnostic/math2-method-comparison/codex-team/critique/ADVERSARIAL_CRITIQUE_260828.md`; independence=independent semantic recomputation, read-order limitation disclosed; planned/unavailable/failed lanes=audit unavailable and not read
Next: gatekeeper는 본 BLOCKED를 유지하고 author의 두 손상 행과 과도 통합군을 수정·재검증한 새 artifact, 그리고 별도 재배정된 critic의 완전한 사전 열람 증거가 모두 존재할 때만 다음 gate를 재개한다.

## 1. 판정과 권한 경계

- **최종 권고: BLOCKED (advisory only).** 외부 Opus 비교, catalog 갱신, ledger append, release 또는 외부 역할 승인으로 진행하면 안 된다.
- author가 `formal proposer readiness BLOCKED`와 no-pNN/answer-key-null 경계를 명시한 점은 타당하다(`author/AUTHOR_REPORT_260828.md:3-10,189-198`). 그러나 `substantive diagnostic analysis complete`라는 결론은 손상된 per-item 행과 의미적으로 성립하지 않는 일부 통합군 때문에 그대로 수용할 수 없다.
- 이 문서는 author를 고치지 않으며 corpus, canonical, ledger, WIP, gate, comparison, relay를 수정하지 않는다.

## 2. runtime·독립 문맥·독점 출력

- native canonical task: `/root/math2_sol_adversarial_critique`
- lane = model = reasoning depth: `adversarial-critic = gpt-5.6-sol = high`
- 실행 표면에서 관찰된 역할/깊이: host가 이 canonical task에 `assessment-adversarial-critic-sol`, `gpt-5.6-sol`, `high`를 배정해 노출했다. opaque host agent ID는 노출되지 않았으므로 추론하지 않는다.
- 역할 지침: `.codex/agents/assessment-adversarial-critic-sol.toml`; 목표 역할 지침: `.claude/agents/type-proposer.md`.
- 독립 문맥: author를 읽기 전에 frozen manifest 17개 hash, 152-line transcript, meta, verify log, 관련 canonicals, 22개 ID와 고위험 문항을 독립 재계산했다. audit artifact는 사용할 수 없었고 읽지 않았다. Opus 결과와 이전 Codex diagnostic/trace도 읽지 않았다.
- exclusive output: 이 파일 하나만 작성했다.
- **독립 증명의 한계:** author artifact 자체의 runtime 문구는 자기기술일 뿐 host-authenticated execution identity의 독립 증명이 아니다(`docs/CODEX_TEAM_ASSURANCE_GUIDE.md:16`). gatekeeper가 별도의 host 실행 증거와 대조해야 한다. 본 lane 역시 opaque 실행 ID가 없으므로 canonical task/model/depth보다 강한 실행 신원은 주장하지 않는다.

### 입력·artifact hash

- frozen manifest: `AUTHOR_INPUT_MANIFEST_260828.tsv` SHA-256 `6C006D9931AE77B34528BCE50A8DF8CCCC7722FEAEF41AA5A9538CB2B7C9084E`; 17/17 byte/hash 일치, warnings 0.
- expected IDs: `EXPECTED_ITEM_IDS_260828.tsv` SHA-256 `37D63195B73C1E810EB9607A588D990924BB61A23A9A50E52448C6863FE5861D`.
- author artifacts: `items.tsv` `8316EF0A656F80DE2506C3B10D5C7D9F60A10E833D36D5BE71C8947D99E9FE6A`; `types.tsv` `ACC5B56A8E0F40E3EB34B395132D0980386AECFB99C47E08B1FBA55136FE3968`; `AUTHOR_REPORT_260828.md` `28E1F8401EFF3ACC27E0C5BCF36984DF4A59B3CA75876BF7A06CA8897DF11772`.

## 3. 실제 read-order log

1. **author 전:** `.codex/agents/assessment-adversarial-critic-sol.toml`, `TEAM_PREFLIGHT_260828.md`, `AUTHOR_INPUT_MANIFEST_260828.tsv`, `EXPECTED_ITEM_IDS_260828.tsv`, `ACCEPTANCE_SCHEMA_260828.md`, input-delta/reference manifests, `.claude/agents/type-proposer.md`, `docs/CODEX_TEAM_ASSURANCE_GUIDE.md`를 읽었다.
2. **author 전:** manifest 17개 hash를 모두 재검증하고 `transcript.md`, `meta.yml`, `verify_log.tsv`, `math2.md`, `COMMON_TYPES.md`, `TYPE_MASTER.md`, `DIFFICULTY_RUBRIC.md`, `curriculum_2022.md`를 읽었다. bindata 세 파일은 manifest hash와 존재만 확인했으며 일반 image evidence로 해석하지 않았다.
3. **author 전:** transcript section/headings에서 22개 ID를 독립 생성하고, S-05·S-07·S-12·S-14·S-15·S-17 및 전 22개 item→canonical provisional map을 계산했다.
4. **그 뒤:** `author/items.tsv`, `author/types.tsv`, `author/AUTHOR_REPORT_260828.md`와 staged author reports를 읽었다. audit은 읽지 않았다.
5. **절차 이탈:** `check_experiment.py`의 **소스 본문은 author를 읽은 뒤** 검사했다. 명령/경로와 gate 결과는 사전 인지했지만, assignment가 요구한 source-level 사전 열람 순서를 충족하지 못했다. 의미 재계산은 author 전 완료되어 semantic independence는 남지만, 완전한 read-order conformance에 대한 충분한 독립 증명은 없다. **severity high / disposition block**.

## 4. 식별자·membership 독립 gate

- expected: `[W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18]`
- observed item rows: `[W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06,S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16,S-17,S-18]`
- observed type memberships: `[W-01,S-02,W-02,S-06,W-03,W-04,S-03,S-15,S-01,S-04,S-18,S-05,S-13,S-07,S-14,S-08,S-09,S-10,S-12,S-11,S-16,S-17]`
- duplicate item IDs: `[]`; missing item IDs: `[]`; extra item IDs: `[]`.
- duplicate memberships: `[]`; missing memberships: `[]`; extra memberships: `[]`.
- **제한:** exact-cover는 통과하지만 semantic validity는 증명하지 않는다. 현재 checker는 필드가 비었는지만 검사하고(`check_experiment.py:103-106,119-128`), 문자 훼손·근거 타당성·group invariant는 검사하지 않는다.

## 5. 고위험 문항 독립 재계산

| ID | 독립 재계산 | author 대비 판정 |
|---|---|---|
| S-05 | 교점은 `x=2(k-1)/(k+2)`, `y=2(4-k)/(k+2)`이고 제1사분면 조건은 정확히 `1<k<4`이다(`transcript.md:70-73`). 분모 부호·strict boundary가 핵심이다. | exact catalog match 없음/decision request는 타당하나 T1은 루브릭과 불안정하다. |
| S-07 | 원 중심에서 `y=x+6`까지 거리는 `3√2`, 반지름은 `√2`; 정삼각형 높이는 `[2√2,4√2]`, 넓이차는 `8√3`이다(`transcript.md:79-81`). | SM2-25 주축은 타당하다. S-14와의 같은 통합군은 부당하다. |
| S-12 | 역삼각부등식으로 상한은 `AB=5`; 직선 AB와 x축의 교점 `P=(-2/3,0)`에서 등호가 성립한다(`transcript.md:97-100`). | SM2-02 확장/신규 decision request는 타당하다. S-10과 같은 생성 유형으로 합치면 안 된다. |
| S-14 | 중심 `(4,3)`, 반지름 3인 원과 `y=mx`의 위치 조건은 `0≤m≤24/7`; 정수 기울기 0,1,2,3 중 m=0은 접선 1점, 나머지는 각 2점이라 총 7점이다(`transcript.md:105-107`). | 주축은 SM2-25가 아니라 **SM2-18 원-직선 위치 관계**가 더 직접적이다(`math2.md:266-272`). |
| S-15 | 보기 순서대로 변환된 중심은 `(3,-2),(-7,-2),(3,0),(3,-2),(1,0)`이므로 첫째·넷째 식이 g를 나타낸다(`transcript.md:108-119`). | SM2-31은 타당하며, 현재 transcript는 C-09의 `수학 ㄱㄴㄷ 0건` 절대문과 직접 긴장한다(`COMMON_TYPES.md:66-72`). 정답 주장 목적이 아니라 식 변환 구조 확인이다. |
| S-17 | 해당 span에는 `f(a)`, `f(k)`만 있고 `f(…) = …` 정의가 0건이다(`transcript.md:124-136`; `verify_log.tsv:8`). | item assignment와 Tier 모두 BLOCKED여야 한다. partial geometry를 reusable type evidence로 사용하면 안 된다. |

## 6. material challenge table

| # | challenge | evidence | severity | required disposition |
|---:|---|---|---|---|
| 1 | **S-17·S-18 per-item record가 ASCII `?`로 훼손되어 exact schema가 실질적으로 실패했다.** S-17 행에 225개, S-18 행에 164개 literal `?`가 있고 rationale/tier basis/trap/citation이 읽을 수 없다. | `author/items.tsv:22-23`; 반면 보고서는 모든 세부 필드가 비공란이라고만 주장한다(`AUTHOR_REPORT_260828.md:91`). checker는 nonblank만 검사한다(`check_experiment.py:103-106`). | **critical** | **block** — 손상되지 않은 두 행과 문자 무결성 검사가 없으면 author complete/gate PASS를 인정하지 않는다. |
| 2 | **fresh `--phase author` PASS는 false assurance다.** ID/schema-header/exact-cover만 보며 손상 문자와 의미 타당성을 탐지하지 못한다. 실제로 손상 행이 있는 현재 artifact가 warnings 0/failures 0/PASS다. | `check_experiment.py:86-128,131-151`; fresh output: `warnings=0`, `failures=0`, `experiment-gate: PASS phase=author`. | **critical** | **block** — gatekeeper가 content-integrity와 semantic checks를 별도로 실패 처리해야 한다. |
| 3 | **DIAG-G06의 S-14 catalog match가 잘못되어 S-07과의 통합이 성립하지 않는다.** S-07은 원 위 점의 거리 극값(SM2-25)이지만 S-14는 기울기 매개 직선과 원의 접/할 관계(SM2-18) 후 정수/교점 수를 센다. | `author/types.tsv:7`; `transcript.md:79-81,105-107`; `math2.md:266-272,337-343`. | **high** | **revise** — S-14를 SM2-18 중심으로 재분류하고 G06에서 분리한다. |
| 4 | **DIAG-G03은 SM2-26/27/31과 SM2-11을 ‘이동’이라는 상위 주제만으로 합친 과도 통합이다.** 점 단일이동(S-03), 포물선 이동량 역추적+평행선 거리(W-04), 합성/식 표현(W-03,S-15)은 생성 invariant와 Tier가 다르다. | `author/types.tsv:4`; `AUTHOR_REPORT_260828.md:99`; canonical의 서로 다른 패턴 `math2.md:354-369,407-415`. | **high** | **revise** — 최소 SM2-26, SM2-27, SM2-31 계열을 분리하거나 primary invariant를 보존하는 grouping으로 다시 작성한다. |
| 5 | **DIAG-G05는 ‘매개변수’만 공유하고 풀이 원리가 다르다.** S-05는 두 직선 교점 좌표의 유리부등식/사분면 범위, S-13은 직선 다발 공통점과 점-직선 거리 최대이다. author 스스로 S-05를 exact no-match로 둔 채 S-13과 reusable group으로 합쳤다. | `author/types.tsv:6`; `items.tsv:10,18`; `transcript.md:70-73,101-104`; `math2.md:166-183`. | **high** | **revise** — S-05 decision-request를 독립시키고 S-13은 SM2-10/11 결합으로 유지한다. |
| 6 | **DIAG-G08은 거리합 최소와 거리차 최대를 하나의 생성 유형으로 섞었다.** S-10은 연속 대칭과 삼각부등식의 합 equality, S-12는 역삼각부등식과 직선-자취의 equality feasibility이다. variation axis가 서로 다른 해결 원리를 나열할 뿐 공통 생성 골격을 제시하지 않는다. | `author/types.tsv:9`; `transcript.md:89-100`; `math2.md:65-74,439-452`. | **high** | **revise** — S-10 SM2-33과 S-12 decision request를 분리한다. |
| 7 | **DIAG-G04의 S-18 match와 축은 충분히 뒷받침되지 않는다.** SM2-13은 삼각형 넓이/절편 구조인데 S-18은 원 위 P, OQ 내분, OP 수직선과 AQ 교점, 사각형 OARP 넓이를 결합한다. SM2-03은 구성 일부일 뿐 reusable primary type가 아니다. 해당 item 행도 훼손됐다. | `author/types.tsv:5`; `author/items.tsv:23`; `transcript.md:138-146`; `math2.md:78-86,198-205`. | **high** | **block/revise** — S-18을 손상 없이 재분석하고, solve-path invariant를 확인하기 전 SM2-13/통합군 주장을 제거한다. |
| 8 | **DIAG-G09가 source-defect BLOCKED인 S-17을 variation/member evidence로 사용한다.** exact-cover를 맞추기 위한 membership은 가능해도 이를 9개 `reusable diagnostic group`의 한 variation으로 쓰면 결손 문항이 관찰 근거처럼 보인다. T3 잠정도 정의 누락 뒤 실제 요구 복잡도를 확정할 수 없어 부당하다. | `author/types.tsv:10`; `AUTHOR_REPORT_260828.md:88,95-107`; `transcript.md:124-136`; `verify_log.tsv:8`. | **high** | **revise** — S-17은 별도 `BLOCKED bucket`으로 두고 importance/variation/Tier 증거에서 제외한다. |
| 9 | **Tier 기준이 S-05와 S-17에서 내부 모순이다.** S-05 행은 분모 부호와 strict inequality 분기를 인정하면서 T1로 두는데 T1은 단일 개념·1~2단계이고 DF8 분기는 상향 요인이다. S-17은 완결 요구가 사라졌는데 T3를 잠정 부여했다. | `author/items.tsv:10,22`; `DIFFICULTY_RUBRIC.md:35-42,49-79`; `AUTHOR_REPORT_260828.md:76,88`. | **high** | **revise** — S-05는 T1/T2 또는 T2로 제한적 재판정하고, S-17 Tier는 BLOCKED로 바꾼다. |
| 10 | **C-05 ‘강화’는 근거가 약하다.** C-05의 특징은 풀이 과정·부분점수·명시 채점 조건인데 transcript는 서술형/단답형 구획과 `구하시오`만 보여 준다. author도 문항별 채점표/부분점수 조건이 없다고 인정한다. | `COMMON_TYPES.md:44-51`; `AUTHOR_REPORT_260828.md:137-140`; `transcript.md:29-50`. | **medium** | **revise** — C-05는 `insufficient evidence/형식만 관찰`로 낮추고 강화 근거로 쓰지 않는다. |
| 11 | **author runtime identity의 독립 proof는 artifact 내부에 없다.** canonical task/model/depth 자기기술은 있으나 host execution identity나 별도 관찰 증거는 이 세 artifact에 없다. | `AUTHOR_REPORT_260828.md:12-25`; `CODEX_TEAM_ASSURANCE_GUIDE.md:16`. | **medium** | **accept-with-limit** — gatekeeper가 host-authenticated lane evidence와 hash를 별도 대조해야 한다. |
| 12 | **no-pNN/S-17 권한 경계 자체는 보수적으로 지켜졌다.** 페이지 번호·답·f 정의를 만들지 않았고 canonical write를 주장하지 않았다. | `AUTHOR_REPORT_260828.md:3-10,189-198`; `items.tsv:2-23`; `ACCEPTANCE_SCHEMA_260828.md:13-19`. | **low** | **accept-with-limit** — 이 제한은 유지하되 위 critical/high 결함을 상쇄하지 않는다. |

## 7. 9개 type group별 판정

| group | members | 판정 | 근거/필수 처분 |
|---|---|---|---|
| DIAG-G01 | W-01,S-02 | **accept-with-limit** | 둘 다 SM2-08 평행·수직 invariant를 공유한다. no-pNN 한계만 유지한다. |
| DIAG-G02 | W-02,S-06 | **accept-with-limit** | 둘 다 원 결정 단계가 있으나 S-06의 주 요구는 SM2-19 현 길이다. ‘SM2-15/19 결합 evidence’ 이상으로 단일 canonical type처럼 쓰지 않는다. |
| DIAG-G03 | W-03,W-04,S-03,S-15 | **revise** | SM2-26/27/31을 상위 주제 하나로 과도 통합했다. primary generator별 분리 필요. |
| DIAG-G04 | S-01,S-04,S-18 | **block** | S-18 행 손상 및 SM2-13 부정합. S-18 재분석 전 재사용 불가. |
| DIAG-G05 | S-05,S-13 | **revise** | 매개변수 외 공통 풀이 invariant가 없다. S-05 decision request를 독립시킨다. |
| DIAG-G06 | S-07,S-14 | **revise** | S-14의 직접 match는 SM2-18이며 S-07과 다른 생성 골격이다. |
| DIAG-G07 | S-08,S-09 | **accept-with-limit** | 등거리/수직이등분선 invariant와 두 observed axes가 실제로 공유된다. |
| DIAG-G08 | S-10,S-12 | **revise** | 거리합-대칭과 거리차-역삼각부등식은 같은 reusable type가 아니다. |
| DIAG-G09 | S-11,S-16,S-17 | **block/revise** | S-11/S-16의 이등분선 축은 인정되지만 S-17은 source-defect BLOCKED라 variation/Tier evidence에서 제외해야 한다. |

## 8. schema completeness 판정

| 요구 항목 | 결과 |
|---|---|
| per-item assignment 또는 BLOCKED | **FAIL** — 22행은 있으나 S-17/S-18의 필수 의미 필드가 훼손됨 |
| unique-ID expected/observed/duplicate/missing/extra | PASS — 두 item/membership set 모두 exact cover |
| 5~12 consolidation | 형식 PASS(9), **의미 FAIL** — G03/G05/G06/G08/G09 과도·오분류 |
| type당 observed variation axes ≥2 | 형식 PASS, 의미 제한 — 다른 해결 원리를 축으로 나열한 group이 있음 |
| observed traps | 형식 PASS, S-17/S-18 FAIL/제한 |
| source-axis importance | PASS-WITH-LIMIT — 기출 1회/부교재축 분리는 했으나 no-pNN 때문에 canonical 반영은 HOLD |
| COMMON_TYPES comparison | REVISE — S-15 경계는 타당, C-05 강화는 unsupported |
| catalog disposition | REVISE — S-14/S-18 match와 group 경계 수정 필요 |
| HARVEST_LOG/EXTRACTION_LOG drafts | 형식 PASS, upstream semantic 결함 때문에 적용 BLOCKED |
| no-pNN/S-17 boundary | PASS-WITH-LIMIT |
| runtime/method trace | self-report 존재, 독립 host proof는 gatekeeper 확인 필요 |
| Korean artifact | **FAIL/PARTIAL** — S-17/S-18 한국어 내용 389문자가 `?`로 훼손됨 |

## 9. student-facing generation hazards

1. **잘못된 유형 이식:** S-14를 SM2-25로 생성하면 원-직선 접/할의 매개변수 범위·끝점 1개 처리가 사라지고 단순 거리극값/점개수 문항으로 변질된다.
2. **과도 통합에 따른 조건 누락:** G03/G05/G08을 하나의 생성 template로 쓰면 ‘이동’, ‘매개변수’, ‘거리 극값’이라는 표면어만 남고 핵심 equality condition·분기·합성 순서가 빠진다.
3. **S-18 구조 오생성:** 내분을 주축으로만 보면 원의 중심 A, OP 수직, AQ 교점, 사각형 넓이와 기울기 선별의 상호 제약이 잉여 또는 모순이 될 수 있다. 독립 solve-back 없이 변형 생성에 사용하면 안 된다.
4. **Tier 오표시:** S-05를 T1 template로 복제하면 분모 부호·strict inequality·교집합을 제거하거나, 유지한 채 T1로 잘못 라벨링할 위험이 있다.
5. **C-05 오이식:** 실제 채점 조건이 없는데 C-05 강화로 보면 생성 시 원문에 없던 부분점수/풀이조건을 출제자 관행으로 과잉 삽입할 수 있다.
6. **결손 보충 위험:** S-17의 group/Tier를 유지하면 후속 생성기가 정의되지 않은 f를 관행적으로 보충하거나 partial geometry를 완결 유형처럼 재사용할 수 있다.

## 10. formal no-pNN / S-17 boundary

- 22문항 모두 pNN page가 없으므로 page citation, page-transcript 대조, formal proposer readiness, status/frequency/star/example 반영은 **BLOCKED**다. bindata path/hash는 page evidence가 아니다.
- `answer_key: null`이므로 author가 수치 정답이나 정답 조합을 공식 evidence로 주장하지 않은 것은 맞다. 본 비평의 산술은 type/trap 구조를 시험하는 독립 recomputation이며 answer-key 인증이 아니다.
- S-17은 f 정의 복구 전 assignment, Tier, catalog disposition, variation-axis evidence, generation readiness가 모두 **BLOCKED**다. `(가)` 또는 partial geometry가 읽혀도 `f(k)` 요구를 완결시키지 못한다.
- S-17/S-18 손상 행을 고치기 전에는 ID exact-cover와 row nonblank만으로 완성도를 주장할 수 없다.

## 11. validation evidence

### fresh repository gate

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
```

### independent content gate

```text
manifest hash check: PASS files=17 warnings=0
transcript lines=152
item IDs: duplicate=[] missing=[] extra=[]
type memberships: duplicate=[] missing=[] extra=[]
S-17 literal question marks=225
S-18 literal question marks=164
content-integrity result=FAIL
```

최종적으로 deterministic ID gate는 PASS지만 content/semantic/read-order gate는 FAIL이다. 따라서 전체 권고는 **BLOCKED**다.
