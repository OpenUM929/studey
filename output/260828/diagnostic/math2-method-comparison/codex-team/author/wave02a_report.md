# EX-math2-20252M 유형 분석 역량 실험 — author wave-02a

## 1. 범위·권한·증거 상태

- 이 문서는 동일한 Codex assurance-team author lane이 pilot 승인 뒤 수행한 **wave-02a 10문항 진단 초안**이다. 외부 Opus 역할이나 승인 권한을 갖지 않는다.
- 포함: 정확히 `S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16`.
- 제외: `S-17,S-18`; 이 파일에서 시작·분류·통합하지 않았다. 전체 22문항 통합도 수행하지 않았다.
- 모든 행의 렌더 근거는 `BLOCKED-no-pNN`이다. transcript line 근거로 진단 배정은 가능하지만 정식 proposer readiness는 BLOCKED다.
- S-15의 `BIN0002.bmp`는 frozen bindata로 존재하나 `pNN.png` 페이지가 아니다. host viewer와 Pillow가 이 파일을 일반 BMP로 해석하지 못했으므로 렌더 페이지 대용으로 사용하지 않았다.
- `answer_key: null`. 정답·정답값·정답 선지·풀이 결과를 주장하지 않는다.
- canonical changes: none. corpus, catalog, COMMON_TYPES, ledger, verify_log, WIP, pilot 파일을 수정하지 않았다.
- Opus 제출물과 종전 Codex diagnostic/trace는 계속 열거나 검색하지 않았다.

## 2. runtime identity와 재개 감사

- runtime identity: native canonical task name `/root/math2_sol_author`
- lane = model = reasoning depth: `author = gpt-5.6-sol = high`
- 역할 지침: `.codex/agents/assessment-author-sol.toml`
- 목표 책임 지침: `.claude/agents/type-proposer.md`
- exclusive output: `author/wave02a_items.tsv`, `author/wave02a_report.md`
- 재개 감사: leader가 같은 lane에 wave-02a를 재배정했고, 새 exclusive 파일 두 개는 작성 전 존재하지 않았다. pilot 파일은 존재함을 확인했으며 수정하지 않았다.
- frozen input 검사: `manifest_ok=17/17`, `warnings=0`, `failures=0`, `experiment-gate: PASS phase=inputs`.

## 3. identifier exact-cover 결과

- expected identifiers: `[S-07, S-08, S-09, S-10, S-11, S-12, S-13, S-14, S-15, S-16]`
- observed identifiers: `[S-07, S-08, S-09, S-10, S-11, S-12, S-13, S-14, S-15, S-16]`
- duplicate identifiers: `[]`
- missing identifiers: `[]`
- extra identifiers: `[]`
- wave completeness: diagnostic assigned 10/10, item-level `assignment_or_BLOCKED` 0/10. 단, formal readiness는 no pNN 때문에 10/10 BLOCKED다.

## 4. method trace

1. 동일 manifest의 byte/hash 17개를 다시 검증하고 updated `check_experiment.py`의 `wave2a` exact slice가 `all_expected[10:20]`임을 확인했다.
2. 기존 제안보다 먼저 `transcript.md:79-123`을 읽어 S-07~S-16의 원문 구조를 고정했다.
3. S-15는 transcript의 텍스트·ㄱ~ㅁ 식과 frozen `BIN0002.bmp` 존재를 확인했다. bindata 디코딩 실패를 숨기지 않고 no pNN 한계로 유지했다.
4. 그 뒤 기존 과목 유형과 COMMON_TYPES를 대조해 기존 유형, 결합 유형, ID 미부여 결정 요청을 구분했다.
5. 원문 배점과 DIFFICULTY_RUBRIC의 단계·조건·발상·분기 축으로 Tier를 진단했으며 answer solve-back은 하지 않았다.
6. 아래 9개 wave-local 주 유형 그룹은 10개 ID를 중복 없이 정확히 덮는다. 전체 22문항 consolidation은 leader의 후속 배정까지 보류한다.

## 5. wave-local consolidation

중요도 표기 원칙: 이번 기출축은 동일한 `2025-2M` 한 회차이므로 항목 수가 둘이어도 `★(기출 1회)`를 넘기지 않는다. 기존 workbook 별은 별도 부교재축으로만 인용한다.

### W2A-G01 — 원 위 점과 직선거리 기반 넓이 극값: S-07
- 대응: SM2-25 주축 + SM2-11 보조.
- variation axis 1: 원의 중심·반지름과 고정 직선의 위치.
- variation axis 2: 거리 극값을 변환하는 도형량(정삼각형 넓이 ↔ 일반 삼각형 높이 ↔ 거리 차).
- observed trap: 중심거리에서 반지름 가감 누락, 정삼각형 높이-변 관계 역전.
- importance: `★(기출축: 2025-2M 1회)` / `★★(부교재축: SM2-25 3문항, SM2-11 주 3문항+보조 다수)`.
- COMMON_TYPES: 서답형 C-05/C-09 강화; 새 공통후보 없음.
- catalog disposition: 기존 결합 사례 diff 후보, no pNN HOLD.

### W2A-G02 — 등거리 자취와 외심: S-08,S-09
- 대응: SM2-01 주축; S-09는 SM2-09 보조.
- variation axis 1: 등거리 대상(세 꼭짓점 ↔ 두 교점).
- variation axis 2: 구하는 점의 추가 자취(자유 평면 ↔ 포물선 위)와 선별 조건(없음 ↔ 양수 x).
- observed trap: 등거리식의 이차항 상쇄 누락, 수직이등분선/양수 선별 누락.
- importance: `★(기출축: 2025-2M 1회, 같은 회차 2문항)` / `★★(부교재축: SM2-01 2문항)`.
- COMMON_TYPES: C-05/C-09 강화.
- catalog disposition: 직접 외심형과 포물선 결합형의 existing diff 후보, no pNN HOLD.

### W2A-G03 — 두 대칭축을 지나는 최단경로: S-10
- 대응: SM2-33.
- variation axis 1: 경유 제약선(x축 ↔ y축 ↔ y=x ↔ 일반 직선)과 순서.
- variation axis 2: 경로 항 수와 요구값(최솟값 ↔ 그때의 점 ↔ 넓이/둘레).
- observed trap: 대칭 대상 선택과 합성 순서 오류.
- importance: `★(기출축: 2025-2M 1회)` / `★★★(부교재축: SM2-33 4문항)`.
- COMMON_TYPES: C-05/C-09 강화.
- catalog disposition: 핵심 골격 실제시험 사례 후보, no pNN HOLD.

### W2A-G04 — 각 이등분선·직선 등거리: S-11
- 대응: SM2-12. S-16의 선행 축으로도 관찰된다.
- variation axis 1: 두 직선의 관계(직각 ↔ 일반각)와 중심/점의 고정 좌표.
- variation axis 2: ± 이등분선의 선별 단서(중심 좌표 ↔ 예각 ↔ 사분면).
- observed trap: 두 이등분선 중 하나 누락 또는 잘못된 가지 선택.
- importance: `★(기출축: 2025-2M 1회, S-11 주축·S-16 보조)` / `★★(부교재축: SM2-12 3문항)`.
- COMMON_TYPES: 복수해 선별을 요구하지만 ㄱㄴㄷ 형식은 아님.
- catalog disposition: 원 중심의 동시접선과 접점 선별 결합 사례 후보, no pNN HOLD.

### W2A-G05 — 축 위 점의 두 거리 차 극값: S-12
- 대응: ID 미부여 decision request; SM2-02 확장 여부 검토.
- variation axis 1: 움직이는 점의 자취(x축 ↔ y축 ↔ 일반 직선/선분).
- variation axis 2: 목표식(`|PA-PB|` 최댓값 ↔ `PA+PB` 최솟값 ↔ 제곱거리 조합).
- observed trap: 삼각부등식과 역삼각부등식 혼동, 등호 성립 위치 미검토.
- importance: `★(기출축: 2025-2M 1회)` / `부교재축 exact match 미확인; 인접 SM2-02는 ★★`.
- COMMON_TYPES: C-05/C-09 강화.
- catalog disposition: SM2-02 확장 또는 신규 유형 결정 요청; ID 미발급, no pNN HOLD.

### W2A-G06 — 직선 다발의 점-직선 거리 최댓값: S-13
- 대응: SM2-10 주축 + SM2-11 보조.
- variation axis 1: 직선 다발의 두 생성식과 매개변수 배치.
- variation axis 2: 공통점에서 부여하는 추가 조건(고정점 거리 최대 ↔ 특정 거리 ↔ 평행/수직).
- observed trap: 직선 다발 구조를 못 보고 k식 계산으로 과잉 진입, 최대 방향 판정 오류.
- importance: `★(기출축: 2025-2M 1회)` / `★★(부교재축: SM2-10 3문항, SM2-11 주 3문항+보조 다수)`.
- COMMON_TYPES: C-05/C-09 강화.
- catalog disposition: 두 existing 유형의 직접 결합 diff 후보, no pNN HOLD.

### W2A-G07 — 원과 정수 기울기 직선의 교점 개수: S-14
- 대응: SM2-25.
- variation axis 1: 기울기 후보의 수 체계(정수 ↔ 자연수 ↔ 유리수 범위 제한).
- variation axis 2: 원의 위치와 교점 수 선별(두 점 ↔ 접점 하나 ↔ 만나지 않음).
- observed trap: 접선 끝값 중복, 한 직선의 두 교점을 하나로 세기, 수직선의 부당한 포함.
- importance: `★(기출축: 2025-2M 1회)` / `★★(부교재축: SM2-25 3문항)`.
- COMMON_TYPES: C-09의 개수형·E5 경계 축 강화.
- catalog disposition: SM2-25의 개수 요구 variation 실제시험 사례 후보, no pNN HOLD.

### W2A-G08 — f(x,y) 이동식의 ㄱ~ㅁ 복수 판정: S-15
- 대응: SM2-31; COMMON_TYPES C-01/C-09 boundary decision request.
- variation axis 1: 이동 조합(평행 ↔ 축대칭 ↔ 좌표교환)과 합성 순서.
- variation axis 2: 응답 구조(식 직접 작성 ↔ 여러 식에서 모두 고르기)와 보기 수.
- observed trap: 도형 이동과 식 대입 부호의 방향 혼동, 좌표교환과 축대칭 혼동, 복수정답 누락.
- importance: `★(기출축: 2025-2M 1회)` / `★★(부교재축: SM2-31 2문항)`.
- COMMON_TYPES: C-01과 완전 일치는 아님(①~⑤ 합답 조합 없음). 그러나 C-09의 절대 서술인 `수학 ㄱㄴㄷ 0건`과 긴장한다. rendered page 복구 후 C-01/C-09 경계 diff를 결정 요청해야 한다.
- catalog disposition: SM2-31 실제시험 보기형 사례 + COMMON_TYPES 경계 결정 요청, no pNN HOLD.

### W2A-G09 — 예각 이등분선으로 접점 결정 후 원의 접선: S-16
- 대응: SM2-12 주축 + SM2-21 보조.
- variation axis 1: 이등분할 두 직선과 선택 조건(예각 ↔ 둔각, 사분면).
- variation axis 2: 접선 요구값(방정식 ↔ y절편 ↔ 기울기/계수 조합).
- observed trap: 다른 이등분선 선택, 사분면 누락, 접점 공식의 좌표 오대입.
- importance: `★(기출축: 2025-2M 1회)` / `★★(부교재축: SM2-12 3문항, SM2-21 2문항)`.
- COMMON_TYPES: C-05/C-09 강화.
- catalog disposition: 기존 유형 결합 diff 후보, no pNN HOLD.

## 6. COMMON_TYPES 비교 종합

- **C-05 reinforcement**: S-07~S-16은 단답형 구획 안에 있으며 수치·개수·모두 고르기 응답을 요구한다. 다만 채점표나 부분점수 조건은 전사에 없으므로 그 세부는 주장하지 않는다.
- **C-09 reinforcement with one material tension**: S-07~S-14,S-16은 5지선다 없이 `구하시오`형이고, 대부분 그림 비의존이다. 그러나 S-15는 `<보기>` ㄱ~ㅁ에서 `모두 고르시오`를 사용해 `수학은 ㄱㄴㄷ 0건`이라는 C-09 문구와 긴장한다.
- **C-01 no exact match / boundary request**: S-15는 ㄱ~ㅁ 복수판정이지만 ①~⑤ 합답 조합이 아니므로 C-01 강화로 단정하지 않는다. `수학 단답형 보기-복수기입`이라는 예외인지 rendered evidence 확보 후 결정해야 한다.
- **C-02 limited**: S-15에 도식이 있으나 중심·반지름이 본문에도 명시되고 transcript에 보기 식이 모두 있어, 그림이 필수 자료인지 단정하지 않는다.
- 새 C-nn ID를 제안하거나 부여하지 않는다.

## 7. catalog disposition과 결정 요청

- existing diff 후보: SM2-01, SM2-09, SM2-10, SM2-11, SM2-12, SM2-21, SM2-25, SM2-31, SM2-33.
- 신규/확장 결정 요청 1: S-12를 SM2-02의 목표식 variation으로 확장할지 `거리차 극값` 별도 유형으로 둘지 결정 필요. ID 미부여.
- COMMON_TYPES 결정 요청 2: S-15 rendered page가 확보되면 C-01과 C-09의 `ㄱㄴㄷ` 경계를 재검토해야 한다.
- source-axis 별은 현재 기출 1회와 workbook 내부 문항 수를 혼합하지 않는다.
- 모든 status promotion, 빈도 추가, 별 변경, 대표 예시 추가는 no pNN 때문에 HOLD다.

## 8. HARVEST_LOG draft

> canonical append가 아닌 내용 초안이다. 허용 입력에 ledger 열 스키마가 없으므로 임의 스키마를 확정하지 않는다.

- corpus unit: `EX-math2-20252M`
- bounded unit: `wave-02a`, IDs `S-07..S-16` 정확히 10개
- existing evidence candidates: `SM2-01,SM2-09,SM2-10,SM2-11,SM2-12,SM2-21,SM2-25,SM2-31,SM2-33`
- decision requests: `S-12 SM2-02 확장 vs 신규`; `S-15 C-01/C-09 경계`
- weakness evidence: `no pNN`, `BIN0002 bindata-only and undecodable as ordinary BMP`, `answer_key null`
- disposition: `진단 분석 only; canonical append 금지`

## 9. EXTRACTION_LOG draft

> canonical append가 아닌 엔트리 내용 초안이다.

- source: `corpus/EX-math2-20252M/transcript.md:79-123`, S-15 bindata `BIN0002.bmp`
- expected/observed: exact 10/10; duplicate/missing/extra 없음
- assigned/BLOCKED: diagnostic assigned 10, item-level assignment BLOCKED 0, formal no-pNN BLOCKED 10
- wave-local consolidation: 9 primary exact-cover groups; full 22-item consolidation not started
- COMMON_TYPES: C-05/C-09 다수 강화, S-15는 C-01/C-09 경계 결정 요청
- canonical changes: none
- resume point: leader inspection 뒤 S-17,S-18 및 full integration을 별도 배정할 때만 재개

## 10. evidence gaps·정지선

- no pNN: 10개 모두 정식 페이지 인용과 페이지-전사 대조가 불가능하다.
- S-15: BIN0002는 manifest hash가 맞지만 일반 이미지 디코더로 읽히지 않았다. transcript의 exact lines만 진단 근거로 사용했다.
- answer_key: null: 정답·복수정답 조합·수치 결과 검증을 하지 않았다.
- S-12: exact catalog match가 없어 confidence low인 decision request다.
- S-08: 개별 문항 행에 배점 표기가 보이지 않아 transcript의 전체 배점 순서(line 20)를 Tier 보조 근거로 사용했다.
- S-17,S-18과 full consolidation은 수행하지 않았다.

## 11. deterministic schema/identifier check output

작성 전 frozen input 검사:

```text
manifest_ok=17/17
warnings=0
failures=0
experiment-gate: PASS phase=inputs
```

wave-02a 검사 명령:

```text
python output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py --phase wave2a
manifest_ok=17/17
expected=S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16
observed=S-07,S-08,S-09,S-10,S-11,S-12,S-13,S-14,S-15,S-16
duplicate=[]
missing=[]
extra=[]
warnings=0
failures=0
experiment-gate: PASS phase=wave2a
```
