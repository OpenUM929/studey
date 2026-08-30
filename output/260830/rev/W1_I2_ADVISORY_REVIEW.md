---
title: "W1-I2 독립 자문 검토"
source: output/260830/parts/W1_I2.md
source_location: "SET-260830-math2-40 / W1-I2"
created: 2026-08-30
author: Codex/OMX
actor: Codex/OMX
responsibility: rev-writer
status: in-round
reviewer: unset
configured_model: gpt-5.6-sol
configured_reasoning_depth: high
observed_model: unavailable
observed_reasoning_depth: unavailable
independence: fork_turns=none
grade: advisory
advisory_verdict: revise-required
review_scope: "items 7,8,9,10,11,13,14,15,16; nine novelty rows; frozen author WIP"
---

# Review W1-I2 — 독립 자문 검토

<document>

검토 대상은 `output/260830/parts/W1_I2.md`의 문항 `7,8,9,10,11,13,14,15,16`과 같은 stem의 `W1_I2.novelty.tsv` 9행이다. 작성자 WIP는 검토 경계와 동결 해시 확인에만 사용했다. 이 보고서는 새 `rev-writer` 검토자가 수학·유일성·조건 삭제·Tier/DF·신규성·정적 형식을 문항별로 다시 계산한 결과이며, 선행 채팅 판단이나 `code-reviewer`가 이 파일을 작성했다는 주장을 하지 않는다.

동결 입력은 모두 일치했다.

| path | bytes | SHA-256 | result |
|---|---:|---|---|
| `output/260830/parts/W1_I2.md` | 10842 | `8596861e72c9cf1c2af8ec27807d896b5ac6c09879f24c608d9b52499eb253e8` | match |
| `output/260830/parts/W1_I2.novelty.tsv` | 5385 | `c97e182c3b37e8673682554afad21f5fcc42d5c7ff2b5ab67ee0268fee2710d8` | match |
| `analysis/wip/item-writer_260830_SET-260830-math2-40_W1_I2.md` | 9932 | `5a38364f2cf4d2d8ce15d4526f3f1864a4ce0b61314a458fb5cad6736565b494` | match |

</document>

<context>

이번 세트는 고1 공통수학2 도형의 방정식 연습 문항이다. `analysis/catalog/AUTHORING_GUIDE.md:48,55-59`는 가장 가까운 카탈로그·선행 세트에 비해 비수치 축을 최소 2개 바꾸도록 요구하며, 좌표 평행이동이나 숫자 교체는 축으로 세지 않는다. `analysis/catalog/AUTHORING_GUIDE.md:15`는 조건을 하나씩 삭제했을 때 답이 유지되면 잉여 조건으로 판정한다. `analysis/curriculum_2022.md:93`은 벡터를 범위 밖으로 고정한다. 검토자는 허용된 카탈로그, prior A/B, P1 및 novelty 도구만 읽었고 `origin_data/`와 `corpus/`는 읽지 않았다.

</context>

<findings>

## §0 자문 결론

- Coverage: 문항 **9/9**, novelty row **9/9**, 조건 삭제 **9/9**.
- 독립 exact solve-back과 정답 유일성: **PASS 9/9**.
- novelty CLI 계약: **PASS**, exact IDs `7,8,9,10,11,13,14,15,16`, duplicates/missing/extra 모두 빈 목록, `warnings=0`, `exit=0`.
- 의미 신규성: **7/9 지지**. 11번은 prior A #12 대비 유효한 비수치 축이 1개뿐이고, 15번은 prior A #14에 이미 있는 “최솟값+최적점 좌표 결합 목표”를 새 축으로 잘못 주장한다.
- 조건 삭제: **8/9 통과**. 16번의 “원점이 아닌”은 양의 넓이 4에서 이미 도출된다.
- Tier/DF: **9/9 지지**. 표기된 Tier와 활성 DF가 실제 단계·조건 결합·분기·통찰에 대응한다.
- 정적 구조: 문항/태그/정답/해설/함정 블록과 서술형 채점 기준은 통과한다. 다만 13번 해설은 범위 밖 `\overrightarrow{}` 표기를 사용하고, 14번 line 176은 두 번째 `qquad` 앞의 역슬래시가 빠졌다.
- 확인된 finding: **5건** (`HIGH 2`, `MEDIUM 3`). 수학 오류·정답 불일치는 0건이다.
- **Advisory verdict: revise-required.** 작성자 수정과 새 해시 아래 재검토 전에는 다음 게이트로 넘기지 않는다. 이는 승인·외부 solve-back·릴리스 판정이 아니다.

## §1 문항별 독립 검토

| item | exact math / uniqueness | condition deletion | Tier / DF | semantic novelty | static / scope | result |
|---:|---|---|---|---|---|---|
| 7 | 기울기 `-2/3`, y절편 `5/3`; 서로 다른 두 점이 직선을 유일 결정한다. | 두 점 중 하나를 지우면 직선·절편이 미결정이므로 통과. | `T1·DF1` 지지: 한 개념의 직접 계산이다. | **지지.** prior A #8/B #4의 매개변수 공선·근 집계에서 두 고정점 직선 결정과 직접 절편 추출로 조건 방향과 목표가 모두 바뀐다. | PASS. | pass |
| 8 | `h²-4h+3=0`에서 `h=1,3`; 제곱거리 `(BH²,AH²)=(2,18),(10,10)`이므로 `h=1`, `x+y-1=0`만 남는다. | y축·수선의 발·`B∈l`·`BH<AH` 중 하나를 지우면 미결정 또는 두 직선이 남는다. | `T2·DF1·DF2` 지지. | **지지.** 순방향 투영에서 미지 발을 통한 직선 역결정으로 바뀌고 길이 부등식 분기가 추가된다. | PASS. | pass |
| 9 | 기준 교점 `(13/7,11/7)`, 같은 비영 절편 `a=24/7`, 직선 `7x+7y-24=0`; 유일. | 비영 조건을 지우면 원점을 지나는 기준교점 연결선도 “두 절편이 0”인 퇴화 후보가 된다. 나머지 조건도 모두 결정성에 필요하다. | `T2·DF1·DF2` 지지. | **지지.** prior A #10의 거리·복수해 다발과 달리 절편 상등 구조로 유일 방정식을 정한다. | PASS. | pass |
| 10 | 선택점 `(16/11,32/11)`, `OP²=1280/121`, `N=1280`; 유일. 제1사분면 삭제 시 `(-16/5,32/5)`와 목표 `256/5`가 추가된다. | 제1사분면·거리비·직선거리·원점과 같은 쪽이 각각 해집합 또는 목표값을 바꾼다. | `T3·DF1·DF2·DF4` 지지. | **지지.** prior A #14의 곡선 최적화 대신 축거리 자취·절댓값 거리·반평면 역선별을 결합한다. | PASS. | pass |
| 11 | `|3x-1|=|4x+7|`의 두 해 `-8,-6/7`, 따라서 `PQ=50/7`; 정확히 두 점이다. | `y=1` 또는 두 기준 직선 중 하나를 지우면 두 점이 결정되지 않는다. | `T3·DF1·DF2·DF4` 지지. | **미지지.** prior A #12도 같은 두 직선 등거리 절댓값의 두 분기를 한 보조 직선과 교차한다. `x축→y=1`은 좌표 평행이동이라 축 0개이고, `x좌표 곱→두 점 사이 거리`만 유효한 1개 축이다. | 수학 표기는 동작한다. “법선벡터”라는 어휘는 계수 제곱합 `5`로 바로 바꿀 수 있으나, 이 보고서는 명시적 벡터 연산·표기 finding과 구분해 별도 finding으로 세지 않는다. | revise-required |
| 13 | `q=±4`; 음의 분기는 `AQ∩BC=(-24,32)`라 선분 조건을 위반한다. 양의 분기에서 `P=(24/7,32/7)`, 행렬식 넓이 `5/7`; 유일. | 넓이·`x=3`·`Q∈AP`·`P∈BC`가 각각 후보 제거와 좌표 결정에 필요하다. | `T3·DF1·DF2·DF7` 지지. | **지지.** 직접 cevian 분할이 아니라 중간 넓이→광선→변 교점→새 작은 삼각형 넓이의 연쇄다. | **FAIL.** `W1_I2.md:137`의 `\overrightarrow{CP}`, `\overrightarrow{CQ}`는 `curriculum_2022.md:93`의 벡터 범위 밖 규칙을 어긴다. | revise-required |
| 14 | 고정점 `(5/3,4/3)`. 세 기울기 영역은 `m≤-8/5`, `-4/7≤m≤7/8`, `m≥5/4`; `k=2` 수직선을 포함한 정수해는 정확히 `-5..7`, 합 `13`. | 두 선분·끝점 포함·정수 조건·직선 가족 중 하나를 지우면 허용 집합 또는 목표가 바뀐다. | `T4·DF1·DF2·DF5·DF7` 지지: 두 방향집합 교차, 유리변환, 숨은 수직선 복구가 활성이다. | **지지.** prior A #13의 한 선분·직접 기울기 매개변수에 두 번째 선분 교차와 유리변환/수직 분기가 추가된다. | 구조는 PASS이나 `W1_I2.md:176`의 두 번째 `qquad`가 `\qquad`가 아니어서 렌더 토큰 FAIL. | revise-required |
| 15 | 두 거리식은 각각 `(22-7x)/5`, `(x+6)/5`; 좌우 미분계수 `-7/5,1/5`로 공통 끝점 `(2,1)`이 유일 최소, `m=8/5`, 목표 `11`. | 곡선 자취와 기준 직선은 모두 필요하며 별도 잉여 조건은 없다. | `T3·DF1·DF2·DF4` 지지. | **미지지.** prior A #14도 거리 최솟값 `m`과 최적점 좌표 `t`를 구해 결합값 `m²+t`를 묻는다. ledger의 “최솟값만→최소점 좌표와 결합값” 주장은 사실과 다르며, 유효한 변화는 포물선→절댓값 그래프 1축뿐이다. | PASS. | revise-required |
| 16 | `b=2a/(a-1)`. `ab=8`에서 기울기 `-2`, `ab=-8`의 두 기울기 합 `12`, 전체 합 `10`; 서로 다른 세 직선이다. | **FAIL.** 넓이 4에서 `|ab|=8`, 따라서 `a,b≠0`이 자동으로 따른다. “원점이 아닌”을 지워도 해·기울기 합이 같다. | `T4·DF1·DF2·DF5·DF7` 지지: 부호 분기와 Vieta 대칭합 통찰이 활성이다. | **지지.** 양의 절편 하나를 구하는 구조에서 부호가 다른 절편까지 포함한 세 직선의 기울기 대칭합으로 조건 방향과 목표가 모두 바뀐다. | 서술형 채점 기준 PASS. | revise-required |

## §2 확인된 finding과 최소 수정

### 1. [HIGH] 11번은 prior A #12 대비 비수치 신규성 축이 1개뿐이다

**Evidence:** `W1_I2.novelty.tsv:6`; 대상 `W1_I2.md:100-121`; prior A `output/260822/공통수학2_도형의방정식_모의40.md:135-140`; 신규성 경계 `AUTHORING_GUIDE.md:48,55-59`.

prior A #12는 두 직선 등거리 절댓값의 `±` 분기를 x축과 교차하고 두 x좌표의 곱을 묻는다. 11번은 같은 분기를 `y=1`과 교차하고 두 점의 거리를 묻는다. `x축→y=1`은 좌표 평행이동일 뿐 비수치 축이 아니므로, 유효한 변화는 목표 `좌표 곱→점 사이 거리` 하나다. CLI PASS는 행 스키마와 ID 커버리지만 증명하며 이 의미 주장을 구제하지 않는다.

**Minimal repair:** 등거리 불변량을 유지하되 prior A #12와 다른 조건 방향 또는 미지수 배치를 하나 더 설계한다. 좌표축을 다른 평행선으로 옮기는 수정은 축으로 세지 말고, 수정 후 가장 가까운 prior와 2축을 다시 적어 semantic review와 novelty CLI를 재실행한다.

### 2. [HIGH] 15번 novelty row가 prior A #14의 기존 목표를 새 축으로 잘못 기술한다

**Evidence:** `W1_I2.novelty.tsv:9`; 대상 `W1_I2.md:197-224`; prior A `output/260822/공통수학2_도형의방정식_모의40.md:147-153`; 카탈로그 `analysis/catalog/math2.md:176-184`.

prior A #14는 거리 최솟값 `m`과 그때의 x좌표 `t`를 모두 구해 `m²+t`를 묻는다. 15번도 최솟값과 최소점 좌표를 구해 `5m+a+b`를 묻는다. 따라서 ledger의 “최솟값만 묻는 대신 최소점 좌표와 거리의 결합값”은 선행 문항의 실제 발문과 모순된다. 포물선→절댓값 그래프라는 곡선 종류 변화만 유효하고, 동일한 최적화 결과의 계수·좌표 결합 변경은 두 번째 구조 축이 아니다.

**Minimal repair:** 곡선 종류 외에 조건 방향·미지수 배치·목표량 중 하나를 실제 풀이 골격이 달라지도록 재설계한다. 단순히 `5m+a+b`의 계수나 문자만 바꾸지 말고, 새 2축을 prior A #14와 직접 대조한다.

### 3. [MEDIUM] 13번 해설이 범위 밖 벡터 표기를 사용한다

**Evidence:** `W1_I2.md:137`; 범위 가드 `analysis/curriculum_2022.md:93`.

해설의 `\overrightarrow{CP}`, `\overrightarrow{CQ}`는 벡터를 직접 도입한다. 계산 자체는 좌표 행렬식으로 이미 표현할 수 있으므로 수학 정답에는 영향이 없지만, 공통수학2 범위 밖 표기를 해설에 넣는다.

**Minimal repair:** “두 점의 좌표 차를 행렬식에 대입하면”으로 바꾸고 곧바로 현재의 `1/2|...|` 식을 제시한다. 벡터 화살표와 벡터 용어를 쓰지 않는다.

### 4. [MEDIUM] 16번의 “원점이 아닌” 조건은 넓이 4에서 이미 도출된다

**Evidence:** `W1_I2.md:228-242`; 조건 잉여 규칙 `AUTHORING_GUIDE.md:15`.

축 절편을 `A=(a,0)`, `B=(0,b)`라 하면 넓이 조건은 `|ab|/2=4`, 즉 `|ab|=8`이다. 따라서 `a=0` 또는 `b=0`은 불가능하고 A, B가 원점이 아니라는 사실은 자동으로 성립한다. 해당 문구를 삭제해도 세 직선과 기울기 합 `10`이 그대로다.

**Minimal repair:** stem에서 “각각 원점이 아닌 점”을 삭제하고 “x축, y축과 각각 A, B에서 만나는”으로 쓴다. 해설의 별도 `a≠0,b≠0` 조건 주장도 넓이식에서 도출된 사실로 정리한다.

### 5. [MEDIUM] 14번에 역슬래시가 빠진 literal `qquad`가 있다

**Evidence:** `W1_I2.md:176`.

세 기울기 구간을 나열하는 식의 첫 간격은 `\qquad`이지만 두 번째는 literal `qquad`라 수학 글자로 렌더된다.

**Minimal repair:** 두 번째 `,qquad`를 `,\qquad`로 고친 뒤 literal-token 정적 검사를 재실행한다.

## §3 결정적 검증 증거

동결 ID/스키마 gate의 정확한 명령과 출력:

```text
python -X utf8 tools/check_novelty_ledger.py --set output/260830/parts/W1_I2.md --ledger output/260830/parts/W1_I2.novelty.tsv --required-count 9
expected_ids=['7', '8', '9', '10', '11', '13', '14', '15', '16']
observed_ids=['7', '8', '9', '10', '11', '13', '14', '15', '16']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
exit=0
```

독립 exact arithmetic 명령은 PowerShell here-string으로 검증 스크립트를 표준입력에 전달한 `python -X utf8 -`였으며 종료코드는 0이다. 결정적 출력:

```text
item7 slope=-2/3 y_intercept=5/3 unique_two_points=True
item8 h_roots=[1, 3] branches=[(1, 2, 18, True), (3, 10, 10, False)] selected_line=x+y-1 unique=True
item9 intersection=(13/7,11/7) equal_intercept=24/7 line=7x+7y-24 unique=True
item10 deleted_first_quadrant_candidates=[(16/11, 32/11, 1280/121), (-16/5, 32/5, 256/5)] selected=(16/11, 32/11, 1280/121) N=1280 unique=True
item11 x_roots=[-8, -6/7] PQ=50/7 unique_pair=True
item13 q_candidates=[-4,4] negative_intersection=(-24,32) negative_on_BC_segment=False positive_P=(24/7,32/7) area=5/7 unique=True
item14 tested_integer_solutions=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7] complete_pattern=-5..7 sum=13 vertical_k2_included=True
item15 left_derivative=-7/5 right_derivative=1/5 common_endpoint=(2,1) m=8/5 target=11 unique=True
item16 a_pos=[2] slopes_pos=[-2] a_neg=[-2 + 2*sqrt(2), -2*sqrt(2) - 2] slopes_neg=[4*sqrt(2) + 6, 6 - 4*sqrt(2)] slope_sum=10 distinct_lines=True
solve_back=PASS 9/9
exit=0
```

정적 검사는 같은 방식의 `python -X utf8 -` UTF-8 line/token scan으로 실행했고 종료코드는 0이다.

```text
item_headers=['7', '8', '9', '10', '11', '13', '14', '15', '16']
answer_blocks=9 solution_blocks=9 trap_blocks=9 grading_criteria=2
explicit_vector_notation=[line137 overrightarrow]
vector_vocabulary=[line108 법선벡터]
literal_qquad_lines=[176]
odd_dollar_lines=[]
duplicate_separators=False
figure_dependencies=[]
static_structure=PASS; curriculum_scope=FAIL(item13); render_token=FAIL(item14)
exit=0
```

재현에 사용한 허용 참조 해시:

| path | bytes | SHA-256 |
|---|---:|---|
| `.claude/agents/rev-writer.md` | 9634 | `8fb12eeffd9d213bef414f833247cf3787325cd986d5e6176691c7cf02c2f513` |
| `analysis/REV_GUIDE.md` | 39376 | `4e81654e0bf9c293d945a415baca887c7052a589aa796ee25a25b161f79cc305` |
| `analysis/catalog/math2.md` | 48979 | `959414ba8ff8754e8d2331b2afd7385f42e93a9dcbb3c24d36022fb4191fd0d0` |
| `analysis/catalog/AUTHORING_GUIDE.md` | 10369 | `737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea` |
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | 12744 | `1533e2930d10fd30dc0f2dd371f22ce87035556bc5b5367e8abaf2bcebee0f69` |
| `analysis/curriculum_2022.md` | 7012 | `a746c017bf394e28a3c0fc73ceb3858af6323861abe1dd50101acf4c5cb4b58a` |
| `output/260822/공통수학2_도형의방정식_모의40.md` | 46751 | `cdd6d528f6250ea24d43ebd7b50e85824284521c70b4967f7aaef8e4c2663324` |
| `output/260829/260829_02_math2_comprehensive_25.md` | 26551 | `bac3216b3d2ab9a6d292e10e7632205a596404e6625b4add28b647298c608965` |
| `output/260830/parts/P1.md` | 9424 | `69e5e9da451c8c86e283a70cc31ad6e731b24d77b9b7021b518d397d6b87b4c6` |
| `tools/check_novelty_ledger.py` | 8333 | `7ecb8c0acbb83cd25ce399b3365efb0389b1773d46f41a38d9b82c586dc1ed7d` |

`lsp_diagnostics`와 `ast_grep_search`는 이 런타임에 등록되지 않았다. 대상은 Markdown/TSV이므로 exact arithmetic, 저장소 novelty CLI, UTF-8 token/static scan, 카탈로그·prior 의미 대조를 사용했다.

</findings>

<questions>

1. 작성자는 11번과 15번을 각각 가장 가까운 prior 대비 실제 비수치 축 2개가 되도록 재설계할 것인가?
2. 작성자는 13번의 벡터 표기와 14번의 malformed LaTeX token을 범위·렌더 규칙에 맞게 제거할 것인가?
3. 작성자는 16번의 잉여 “원점이 아닌” 조건을 삭제하고 조건 삭제 근거를 새 WIP에 갱신할 것인가?

</questions>

<proposed_fixes>

- [ ] 11번에 좌표 평행이동이 아닌 두 번째 비수치 구조 축을 추가하고 novelty row를 다시 쓴다.
- [ ] 15번을 prior A #14와 다른 두 비수치 축이 되도록 재설계하고 false target-axis 주장을 제거한다.
- [ ] 13번 해설의 `\overrightarrow{}`를 좌표 행렬식 설명으로 바꾼다.
- [ ] 16번 stem의 “원점이 아닌” 잉여 조건과 그에 종속된 해설 표현을 정리한다.
- [ ] 14번 line 176의 literal `qquad`를 `\qquad`로 고치고 exact solve, condition deletion, Tier/DF, semantic novelty, 정적 scan, novelty CLI를 새 해시 아래 모두 재실행한다.

</proposed_fixes>

<output_format>

작성자 회신은 다음 형식을 사용한다.

| question | verdict (`accept`/`reject`/`needs-decision`) | evidence | proposal/new hash |
|---|---|---|---|

</output_format>

## history

- 2026-08-30 · Codex/OMX `rev-writer`가 W1-I2 9문항/9 novelty 행을 독립 재검산하고 advisory `revise-required` finding 5건을 기록했다. 할당상 공유 `_index.md`·`REV_LOG` 쓰기는 금지되어 갱신하지 않았다.

Pipeline: SET-260830-math2-40 → W1-I2 author frozen → **rev-writer independent advisory review: revise-required** → author repair → fresh advisory review → external solve-back (not started)
Stage: Codex/OMX = gpt-5.6-sol — exact math/uniqueness 9/9 and novelty CLI pass; ▲ blocked by semantic novelty items 11/15, item 13 scope, item 16 redundancy, and item 14 render token.
Team: mode=solo; lead=review writer | gpt-5.6-sol | Codex/OMX rev-writer | complete; lanes=rev-writer = gpt-5.6-sol = high | fresh advisory report writer/reviewer | complete, exclusive output `output/260830/rev/W1_I2_ADVISORY_REVIEW.md` | `.claude/agents/rev-writer.md`; independence=independent (`fork_turns=none`); planned/unavailable/failed lanes=observed runtime model/depth proof unavailable
Next: author repairs the five checkbox findings and returns newly frozen set/novelty/author-WIP hashes; stop until those hashes exist, with no approval or external solve-back claim.
