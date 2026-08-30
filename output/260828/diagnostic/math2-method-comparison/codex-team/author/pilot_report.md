# EX-math2-20252M 유형 분석 역량 실험 — author pilot-01

## 1. 성격과 권한 경계

- 이 문서는 **Codex assurance team의 assessment evidence author**가 작성한 10문항 한정 진단 초안이다. 외부 Claude Code Opus `type-proposer`의 산출물·승인·판정을 대신하지 않는다.
- 형식 상태: **진단 분석은 수행, 정식 제안은 BLOCKED**. 원문 전사 위치는 확인되지만 문항별 렌더 페이지 `pNN.png`가 없으므로 정식 제안에 필요한 페이지 근거를 충족하지 못한다.
- 모든 문항의 `rendered_evidence_status`는 `BLOCKED-no-pNN`이다. bindata는 위치를 특정할 수 있는 원본 포함 파일일 뿐 페이지 인용이 아니며, pilot-01 문항 W-01~W-04·S-01~S-06에는 bindata 참조가 없다.
- `answer_key: null`. 정답·정답값·정답 검증 주장을 하지 않는다.
- 카탈로그·공통유형·HARVEST_LOG·EXTRACTION_LOG·verify_log·corpus·WIP를 수정하지 않았다. 아래 갱신 내용은 모두 비가역 조치가 아닌 **결정 요청 또는 초안**이다.
- Opus 제출물 및 `output/260828/diagnostic/math2-method-comparison/opus/` 아래 파일은 열거나 검색하지 않았다. 기존 Codex 진단 분석·trace 파일도 읽지 않았다.

## 2. runtime identity 및 독립성

- runtime identity: native canonical task name `/root/math2_sol_author`
- lane = model = reasoning depth: `author = gpt-5.6-sol = high`
- persona/role: assessment evidence author / 독립 근거색인 초안 작성자
- 역할 지침: `.codex/agents/assessment-author-sol.toml`
- 비교 대상 책임 지침: `.claude/agents/type-proposer.md`
- 독립성: frozen author manifest와 명시적으로 허용된 preflight/schema/check 파일만 사용했으며, Opus 비교물은 보지 않았다.
- exclusive output: `output/260828/diagnostic/math2-method-comparison/codex-team/author/pilot_items.tsv`, `output/260828/diagnostic/math2-method-comparison/codex-team/author/pilot_report.md`

## 3. 무결성 및 고유 ID 적용 범위

- measured total experiment: 22문항(W-01~W-04, S-01~S-18).
- 이 pilot의 고정 범위는 정확히 10문항이며 S-07은 시작하지 않았다.
- expected identifiers: `[W-01, W-02, W-03, W-04, S-01, S-02, S-03, S-04, S-05, S-06]`
- observed identifiers: `[W-01, W-02, W-03, W-04, S-01, S-02, S-03, S-04, S-05, S-06]`
- duplicate identifiers: `[]`
- missing identifiers: `[]`
- extra identifiers: `[]`
- pilot completeness: 10/10 식별자를 한 번씩 기록했다. 진단 배정 10, item-level `assignment_or_BLOCKED` 0이다. 단, **정식 proposer readiness는 10/10 모두 no pNN 때문에 BLOCKED**이다.

## 4. 근거 우선 method trace

1. `AUTHOR_INPUT_MANIFEST_260828.tsv`와 `EXPECTED_ITEM_IDS_260828.tsv`를 먼저 읽고 입력 경계와 pilot 식별자를 고정했다.
2. `check_experiment.py --phase inputs`로 17개 manifest의 byte/hash를 확인했다: `manifest_ok=17/17`, `warnings=0`, `failures=0`, `experiment-gate: PASS phase=inputs`.
3. 기존 제안이나 Opus 결과보다 먼저 `corpus/EX-math2-20252M/transcript.md`, `meta.yml`, `verify_log.tsv`를 읽었다. pilot 문항 근거는 transcript의 정확한 행 범위 31-78이다.
4. 그 뒤 허용된 정본 `analysis/catalog/math2.md`, `COMMON_TYPES.md`, `TYPE_MASTER.md`, `DIFFICULTY_RUBRIC.md`, `CODE_REGISTRY.md`, `analysis/curriculum_2022.md`, `analysis/FORECAST_GUIDE.md`와 assurance/role 지침을 대조했다.
5. 각 문항을 기존 유형 또는 ID 미부여 결정 요청에 진단 배정하고, 배점 신호와 DF 특징으로 Tier를 판정했다. 정식 페이지 인용은 생성하지 않았다.
6. 주 유형 기준으로 8개 재사용 그룹에 정확히 한 번씩 배치하고, 보조 유형은 교차 연결로만 기록했다.

## 5. 문항별 진단 요약

| ID | 1차 진단 | 근거 | Tier | 정식 상태 |
|---|---|---|---|---|
| W-01 | SM2-08 | `transcript.md:31-34`; `math2.md:147-153` | T1 | BLOCKED-no-pNN |
| W-02 | SM2-15 | `transcript.md:35-38`; `math2.md:234-242` | T2 | BLOCKED-no-pNN |
| W-03 | SM2-31 | `transcript.md:39-43`; `math2.md:407-415` | T3 | BLOCKED-no-pNN |
| W-04 | SM2-27 + SM2-11 | `transcript.md:44-48`; `math2.md:176-183,363-369` | T3 | BLOCKED-no-pNN |
| S-01 | SM2-03 | `transcript.md:52-54`; `math2.md:78-86` | T1 | BLOCKED-no-pNN |
| S-02 | SM2-08 | `transcript.md:55-59`; `math2.md:147-153` | T1 | BLOCKED-no-pNN |
| S-03 | SM2-26 | `transcript.md:60-64`; `math2.md:354-360` | T1 | BLOCKED-no-pNN |
| S-04 | SM2-08 + SM2-03 | `transcript.md:65-69`; `math2.md:78-86,147-153` | T1(경계 검토) | BLOCKED-no-pNN |
| S-05 | 신규 결정 요청 후보 | `transcript.md:70-73`; SM2-07 대조 `math2.md:137-145` | T1(DF8 검토) | BLOCKED-no-pNN |
| S-06 | SM2-19 + SM2-15 | `transcript.md:74-78`; `math2.md:234-242,275-281` | T1 | BLOCKED-no-pNN |

## 6. 통합 유형(consolidation) — 주 유형 exact cover

중요도는 두 축을 섞지 않는다. 아래 `기출축`은 이 pilot의 2025-2M 한 회차 관찰이므로 모두 `★(기출 1회)`이다. `부교재축`은 기존 `math2.md`의 별을 그대로 인용한다. `S-05`는 기존 일치 유형이 없어 부교재축 별을 부여하지 않는다.

### G-P01 — 평행·수직으로 직선 결정: W-01, S-02, S-04
- 진단 대응: SM2-08 주축. S-04에는 SM2-03 내분점이 보조 결합된다.
- variation axis 1: 기준 직선의 제시형(일반형 계수 ↔ 두 점으로 결정되는 직선).
- variation axis 2: 추가 조건(주어진 점 통과 ↔ 계수 미정 직선의 평행·수직 동시 만족 ↔ 내분점 통과).
- observed trap: 기울기 부호/음의 역수 오류, 내분비 순서 오류, 조건 하나 누락.
- 중요도: `★(기출축: EX-math2-20252M 1회, W-01·S-02·S-04)` / `★★(부교재축: SM2-08 2문항; math2.md:147-153)`.
- catalog disposition: 실제 시험 대표 예시·결합 축 추가의 existing diff 후보이나 no pNN이므로 HOLD.

### G-P02 — 지름 양 끝점으로 원 결정: W-02
- 진단 대응: SM2-15.
- variation axis 1: 중심 결정 정보(지름 양 끝점 ↔ 중심이 놓인 직선 ↔ 현의 수직이등분선).
- variation axis 2: 요구값(원의 방정식 ↔ 중심/반지름 ↔ 계수 조합).
- observed trap: 지름을 반지름으로 오인, 표준형 중심 부호 오류.
- 중요도: `★(기출축: EX-math2-20252M 1회, W-02)` / `★★(부교재축: SM2-15 3문항; math2.md:234-242)`.
- catalog disposition: 지름 양 끝점 변형의 실제 시험 근거 추가 후보이나 no pNN이므로 HOLD.

### G-P03 — 평행이동 후 축대칭 합성: W-03
- 진단 대응: SM2-31.
- variation axis 1: 이동 벡터의 x·y 성분.
- variation axis 2: 두 번째 대칭축(x축 ↔ y축 ↔ 원점 ↔ y=x)과 합성 순서.
- observed trap: 합성 순서 역전, x축 대칭의 y부호 누락, 도형 이동과 식 대입 부호 혼동.
- 중요도: `★(기출축: EX-math2-20252M 1회, W-03)` / `★★(부교재축: SM2-31 2문항; math2.md:407-415)`.
- catalog disposition: SM2-31의 기존 대표 골격과 직접 일치하는 실제 시험 근거 후보이나 no pNN이므로 HOLD.

### G-P04 — 포물선 이동 역추적과 직선 사이 거리: W-04
- 진단 대응: SM2-27 주축 + SM2-11 보조.
- variation axis 1: 이동량을 주는 방식(직접 벡터 ↔ 원상·이동된 포물선의 정점 비교).
- variation axis 2: 이동된 직선에 부가하는 요구(상 방정식 ↔ 축 절편/넓이 ↔ 원래 직선과의 거리).
- observed trap: 계수 단순 비교로 이동량 오판, 직선 이동식 반대 부호, 평행선 거리 분모 누락.
- 중요도: `★(기출축: EX-math2-20252M 1회, W-04)` / `★★(부교재축: SM2-27 3문항; SM2-11 주 3문항+보조 다수; math2.md:176-184,363-369)`.
- catalog disposition: 두 기존 유형의 결합 사례 existing diff 후보이나 no pNN이므로 HOLD.

### G-P05 — 내분점 좌표의 직접 적용: S-01
- 진단 대응: SM2-03. S-04의 보조 축으로도 관찰된다.
- variation axis 1: 내분비와 두 끝점 좌표.
- variation axis 2: 요구값(내분점 좌표 직접 요구 ↔ 내분점을 다른 직선 조건에 투입).
- observed trap: 가중치 순서 역전, 좌표별 부호 계산 오류.
- 중요도: `★(기출축: EX-math2-20252M 1회, S-01; S-04 보조)` / `★★(부교재축: SM2-03 2문항; math2.md:78-86)`.
- catalog disposition: 실제 시험의 내분 직접형 및 결합형 근거 후보이나 no pNN이므로 HOLD. 외분 관련 범위 경고는 이 pilot 문항에는 해당하지 않는다.

### G-P06 — 이동한 점의 직선 위 조건: S-03
- 진단 대응: SM2-26.
- variation axis 1: 이동 벡터의 방향과 크기.
- variation axis 2: 이동 후 조건(직선 위 ↔ 축 위 ↔ 다른 특수점과의 관계).
- observed trap: 음의 이동 방향 역전, 원래 점을 식에 대입.
- 중요도: `★(기출축: EX-math2-20252M 1회, S-03)` / `★★(부교재축: SM2-26 2문항; math2.md:354-360)`.
- catalog disposition: 기존 variation axis인 이동 후 특정 직선 위 조건의 실제 시험 근거 후보이나 no pNN이므로 HOLD.

### G-P07 — 매개변수 직선 교점의 사분면 범위: S-05
- 진단 대응: **신규 결정 요청 후보, ID 미부여**. SM2-07은 공선·두 점을 지나는 직선 결정 중심이라 정확 일치로 단정하지 않는다.
- variation axis 1: 두 직선의 기울기·절편 중 매개변수 배치.
- variation axis 2: 교점의 영역 조건(제1사분면 ↔ 다른 사분면 ↔ 축/반평면)과 경계 포함 여부.
- observed trap: 분모 0 또는 부호 분기 누락, `x>0`·`y>0`의 교집합 누락, 사분면에 등호 포함.
- 중요도: `★(기출축: EX-math2-20252M 1회, S-05)` / `부교재축: exact match 미확인`.
- catalog disposition: `SM2-07 확장`과 `별도 신규 유형 결정 요청` 중 선택 필요. ID는 발급하지 않으며 no pNN 때문에 정식 결정도 HOLD.

### G-P08 — 원 결정 후 축이 만드는 현의 길이: S-06
- 진단 대응: SM2-19 주축 + SM2-15 보조.
- variation axis 1: 반지름 결정 정보(통과점 ↔ 방정식 계수 ↔ 다른 원과의 관계).
- variation axis 2: 현을 만드는 직선(y축 ↔ x축 ↔ 일반 직선)과 요구값(현 길이 ↔ 반현 ↔ 넓이 이등분).
- observed trap: 기존 원과 새 원의 반지름이 같다고 오인, 중심-축 거리와 반현 혼동.
- 중요도: `★(기출축: EX-math2-20252M 1회, S-06)` / `★★(부교재축: SM2-19 2문항, SM2-15 3문항; math2.md:234-242,275-281)`.
- catalog disposition: 두 기존 유형의 결합 사례 existing diff 후보이나 no pNN이므로 HOLD.

## 7. observed traps 종합

1. **부호·순서**: 수직 기울기의 음의 역수(W-01/S-02/S-04), 이동식의 반대 부호와 합성 순서(W-03/W-04/S-03).
2. **비와 길이의 역할 혼동**: 내분 가중치 순서(S-01/S-04), 지름과 반지름(W-02), 중심-축 거리와 반현(S-06).
3. **경계·경우 분기**: 사분면은 축을 포함하지 않는 엄격 부등식이고 교점식의 분모 부호/평행 예외를 확인해야 한다(S-05). 이는 TYPE_MASTER의 E5·C10/DIFFICULTY_RUBRIC의 DF8과 연결되나, 실제 풀이·정답 주장은 하지 않는다.
4. **조건 결합 누락**: S-04에서 내분점과 수직 조건 중 하나만 쓰거나, W-04에서 이동량 추적과 평행선 거리 중간 단계를 생략하는 오류.

## 8. COMMON_TYPES 비교

- **C-05 reinforcement(제한적)**: transcript가 W-01~W-04를 `서술형`, S-01~S-06을 `단답형`으로 구분한다(`transcript.md:29-50`). 따라서 서답형·서술형 형식 관행은 강화된다. 다만 문항별 채점 조건/부분점수표는 전사에 없으므로 그 세부는 강화 근거로 주장하지 않는다(`COMMON_TYPES.md:44-51`).
- **C-09 reinforcement**: 10/10이 선택형·ㄱㄴㄷ 없이 수치·범위·방정식을 요구하는 서답 구조이며 발문은 `구하시오`로 끝난다. pilot 10문항은 그림 없이 성립한다(`transcript.md:31-78`; `COMMON_TYPES.md:66-94`).
- **C-00 reinforcement(시험지 단위)**: 5쪽, 서술 4+단답 18, 중간/기말/수행 30/30/40, 저작권 문구가 전사 머리에 기록되어 있다(`transcript.md:6-21`; `COMMON_TYPES.md:13-19`). 이는 pilot 개별 유형의 중요도와는 분리한다.
- **no-match/미강화**: C-01 ㄱㄴㄷ, C-02 자료 제시형, C-04 대화/채점형, C-06 실생활 소재는 pilot에서 관찰되지 않는다. 새 C-nn 후보는 제안하지 않는다.

## 9. catalog update disposition

- existing diff 후보: SM2-03, SM2-08, SM2-11, SM2-15, SM2-19, SM2-26, SM2-27, SM2-31에 `EX-math2-20252M`의 실제 시험 사례를 추가할 가능성이 있다.
- 중요도 전환 원칙: 위 후보는 현 부교재축 별을 그대로 유지하고, 기출축은 2025-2M 한 회 관찰인 `★(기출 1회)`로 별도 표기해야 한다. 한 회로 ★★/★★★를 만들지 않는다.
- 신규 decision request: S-05를 SM2-07 확장으로 처리할지, `매개변수 직선 교점의 사분면 범위`라는 별도 유형으로 처리할지 검토가 필요하다. 신규 ID는 발급하지 않았다.
- **정식 갱신 처분: HOLD**. no pNN이므로 status promotion, 대표 예시 추가, 빈도/별 변경, 코드 발급을 실행하지 않는다.

## 10. HARVEST_LOG draft

> 아래는 기록 내용 초안이며 canonical에 append하지 않는다. 실제 ledger 열 구조는 이번 허용 입력에 포함되지 않아 임의 스키마를 주장하지 않는다.

- corpus unit: `EX-math2-20252M`
- bounded unit: `pilot-01` / 10 IDs `[W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06]`
- diagnostic existing-type evidence: `SM2-03, SM2-08, SM2-11, SM2-15, SM2-19, SM2-26, SM2-27, SM2-31`
- decision request: `S-05 — SM2-07 확장 vs 별도 신규 유형; ID 미부여`
- evidence weakness: `no pNN; transcript line evidence only; answer_key null`
- disposition: `진단 초안, 정식 반영 HOLD, canonical append 금지`

## 11. EXTRACTION_LOG draft

> 아래는 로그 엔트리 내용 초안이며 canonical에 append하지 않는다.

- source: `corpus/EX-math2-20252M/transcript.md:31-78`, `meta.yml`, `verify_log.tsv`
- expected/observed: exact 10/10, duplicate/missing/extra 모두 없음
- assigned/BLOCKED: diagnostic assigned 10 / item-level assignment BLOCKED 0; formal proposer readiness BLOCKED 10(no pNN)
- consolidation: 8 primary exact-cover groups, secondary links recorded separately
- COMMON_TYPES: C-05 제한적 강화, C-09 강화, C-00 시험지 단위 강화; 새 공통유형 후보 없음
- canonical changes: none
- next condition: 독립 evidence audit 이전에 pilot gate PASS가 필요하며, author는 이 pilot에서 S-07을 시작하지 않음

## 12. evidence gaps와 정지 조건

- no pNN: 형식적 페이지 인용과 전사-렌더 대조 불가. 실제 페이지 번호를 추정하거나 만들지 않았다.
- answer_key: null: 정답값 및 풀이 정합성 검증을 수행하지 않았다.
- S-05 유형 경계: 현 카탈로그와 exact match가 불명확하므로 confidence low, ID 결정 요청으로 유지한다.
- W-01~W-04의 10점 서술형은 세부 배점표가 없어 Tier를 원문 점수로 직접 매핑하지 않고 인지 복잡도로 판정했다.
- 본 pilot는 이 두 파일과 pilot gate 실행 후 즉시 멈춘다. S-07은 leader의 재배정 전 시작하지 않는다.

## 13. deterministic schema/identifier check output

입력 동결 검사(작성 전):

```text
manifest_ok=17/17
warnings=0
failures=0
experiment-gate: PASS phase=inputs
```

pilot 산출물 검사 명령과 최종 출력:

```text
python output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py --phase pilot
manifest_ok=17/17
expected=W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06
observed=W-01,W-02,W-03,W-04,S-01,S-02,S-03,S-04,S-05,S-06
duplicate=[]
missing=[]
extra=[]
warnings=0
failures=0
experiment-gate: PASS phase=pilot
```
