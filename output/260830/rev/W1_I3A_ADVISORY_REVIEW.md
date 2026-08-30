---
lane: code-reviewer
configured_model: gpt-5.6-sol
configured_reasoning_depth: high
observed_model: unavailable
observed_reasoning_depth: unavailable
independence: fork_turns=none
grade: advisory
verdict: revise-required
review_scope: W1-I3A items 17,18,19,21,22,23,24; seven novelty rows; both priors; P1 and clean R2 review
---

# W1-I3A 독립 자문 검토

## §0 결론

- Coverage: 문항 **7/7**, novelty row **7/7**, frozen input **3/3 match**.
- 독립 exact solve-back/유일성: **PASS 7/7**.
- novelty CLI 계약: **PASS**, exact IDs `17,18,19,21,22,23,24`, `warnings=0`, `exit=0`.
- 그러나 의미 신규성은 **4/7만 지지**된다. 17·22·24는 가장 가까운 카탈로그 구조에 대한 2개 비수치 축을 입증하지 못했고, 23은 카탈로그 유형 경계를 잘못 잡았다.
- 조건 삭제: 22의 두 양의 절편 조건 중 하나가 잉여이고, 23의 “원의 외부에 있는”은 주어진 좌표와 “두 접선”에서 이미 도출된다.
- Tier/DF: Tier 자체는 7/7 수용 가능하나, 18의 `DF5`는 정형 완전제곱 최소화에 의해 활성화되지 않는다.
- 정적/렌더: 문항·태그·구분선·수식 delimiter·무그림 구조는 PASS. 단, 19와 21의 세 식에 `\qquad`가 아닌 literal `qquad`가 있어 렌더 토큰은 FAIL.
- **Verdict: revise-required** (advisory only). 이 상태로 외부 solve-back/release에 넘기지 않는다.

## §1 Frozen inputs

| path | bytes | SHA-256 | result |
|---|---:|---|---|
| `output/260830/parts/W1_I3A.md` | 7032 | `c59623920b5ff674f91ea6f034cd46b1cbacdb582340e3cd62a517dc71f24e1d` | match |
| `output/260830/parts/W1_I3A.novelty.tsv` | 5182 | `ccd7ac8091d6561010e463d1232803b046d37b4adf616db3bdf070406ad9c8a1` | match |
| `analysis/wip/item-writer_260830_SET-260830-math2-40_W1_I3A.md` | 5048 | `376405834e7b1b4b0bad3bb06b46bfb578f5c52ab252702fa36afe5912abc447` | match |

## §2 문항별 독립 검토

| item | exact solve / uniqueness | condition deletion | Tier / DF | semantic novelty | no-figure / static / scope | result |
|---:|---|---|---|---|---|---|
| 17 | 중심 `(-1,4)`, `r²=13`, `(a,b,c)=(2,-8,4)`, 답 `-2`; 유일. | 두 지름 끝점은 원의 중심·반지름 결정에 필요. | `T1·DF1` 지지. | **미입증.** 카탈로그는 `#3-3`을 같은 유형 발생으로 열거하고 지름 양 끝점·방정식/계수 표적을 이미 변형 축으로 명시하지만 ledger는 `#3-1/#3-23`만 최근접으로 제시한다. 두 번째 비수치 축이 고정되지 않았다. | 수학/범위/무그림 PASS. | revise-required |
| 18 | `r²=2(t-2)²+6`; 최소 `6`, 유일한 `t=2`; 모든 실수에서 실제 원. | 실수 정의역과 방정식 family가 최소화 문제를 결정한다. | `T2` 지지. **`DF5`는 미활성**: 정형 완전제곱/꼭짓점 계산이다. | 최소 방향 + 최소값과 등호 매개변수 동시 요구가 prior A 20/B 16 및 카탈로그 최대/넓이 표적과 구별되어 지지. | PASS. | revise-required (DF tag) |
| 19 | `|t|<3`, `|t-4|>3` → `{-2,-1,0}`, 합 `-3`; 유일. | (가)/(나)/정수 조건 각각 삭제 시 해집합 또는 유한성이 바뀐다. | `T3·DF1·DF2·DF4·E5` 지지. | 두 평행선의 상반 위치관계 + 열린 경계 정수합으로 prior A 21/B 10과 구별; 지지. | 거리 비교가 정석이며 판별식 불필요. 단 line 55 렌더 토큰 FAIL. | revise-required (format) |
| 21 | 현 반길이 `3`, 중심거리 `d=4`, `k=-5±4√5`, 곱 `-55`; 두 현 모두 실재. | 원/직선족/현 길이 모두 필요. | `T2·DF1·DF8` 지지. | 고정 직선에서 현 길이 정방향인 prior B 9를 역산하고 두 parameter 곱을 요구; prior A 19와도 다른 경로라 지지. | **SM2-19 유효.** `L=2√(r²-d²)`와 점-직선 거리만 사용해 판별식 우회가 없다. 단 lines 79,83 렌더 토큰 FAIL. | revise-required (format) |
| 22 | `c=±2`, 양의 절편 branch `c=2`, 넓이 `2`; 유일. | **FAIL:** 기울기 `-1`이면 두 절편은 모두 `c`; `x`절편 양수만 또는 `y`절편 양수만 남겨도 같은 직선을 고른다. | `T2·DF1·DF8` 지지. | **미입증:** 카탈로그 `SM2-20 #3-20`이 이미 “접선 + 축과의 삼각형 넓이”이고, moved-center tangent/branch selection/area가 그대로다. ledger의 두 축은 가장 가까운 카탈로그 구조를 넘지 못한다. | 무그림/범위 PASS. | revise-required |
| 23 | 접점 `(38/13,-34/13)`, `(38/13,86/13)`; `b>2`가 위 접점과 `124/13`을 유일 선택. | `b>2`는 필요. **“원의 외부에 있는”은 좌표로 `OQ=13>5`이고 두 접선을 명시해 도출되므로 잉여.** | 계산 난도 `T3`은 수용 가능. | ledger 비교가 잘못된 유형 경계 위에 있어 PASS를 지지할 수 없다. | 수학/무그림/범위 PASS. | revise-required |
| 24 | `27m²-48m+7=0`, 판별식 `1548>0`, 곱 `7/27≠0`, 역수합 `48/7`; 수직선 `x=8`은 중심거리 `6>3`이라 접선이 아니어서 누락 없음. | 점/원/접선 조건 모두 필요; 두 기울기와 역수도 정의됨. | `T3·DF1·DF2·DF5` 수용 가능. | **미입증:** 카탈로그 `SM2-22 #3-19`가 이미 점을 지나는 직선 다발 → 거리식 → 기울기 이차방정식 → 근과 계수 관계다. 역수합으로 바꾼 표적 1축 외 두 번째 비수치 축이 없다. | 범위/무그림 PASS. line 159의 `OP`는 중심 `O`를 정의하지 않은 표기. | revise-required |

## §3 Findings and minimal repairs

### [HIGH] F1 — item 17 novelty evidence omits the closest catalog occurrence
File: `output/260830/parts/W1_I3A.novelty.tsv:2` (stem `output/260830/parts/W1_I3A.md:1`)

`analysis/catalog/math2.md:236-240` lists `#3-3` and explicitly includes the diameter-endpoint construction and equation/asked-expression axes. The ledger instead compares only `#3-1/#3-23`, so the claimed two-axis change is not established against the closest known catalog occurrence.

**Minimal repair:** redesign 17 with a second explicit nonnumeric structural change beyond diameter endpoints and coefficient-expression target, then rewrite the row so both axes are evidenced against the canonical catalog description. Do not manufacture a PASS from the two allowed priors alone.

### [HIGH] F2 — item 22 repeats the canonical `SM2-20 #3-20` route
File: `output/260830/parts/W1_I3A.md:94-112`; ledger `output/260830/parts/W1_I3A.novelty.tsv:6`

The catalog states `#3-20 접선 + 축과의 삼각형 넓이` (`analysis/catalog/math2.md:284-290`). Item 22 uses exactly fixed-slope tangent → two parallel lines → positional branch → coordinate-axis triangle area. Center/slope/radius changes are numeric, not novelty axes.

**Minimal repair:** replace at least two nonnumeric axes (for example, change the condition direction/unknown placement and a non-area target) while preserving `SM2-20`; update the ledger and rerun semantic review.

### [HIGH] F3 — item 23 is outside the assigned `SM2-21` invariant
File: `output/260830/parts/W1_I3A.md:116-136`; ledger `output/260830/parts/W1_I3A.novelty.tsv:7`

`SM2-21` is the tangent at a circle point / contact-chord type using `x₁x+y₁y=r²` (`analysis/catalog/math2.md:293-300`). Item 23 instead starts from an external point and reconstructs one of its tangent points by the right triangle/projection route, which belongs to the `SM2-22` external-point family (`analysis/catalog/math2.md:303-309`). Retagging alone would duplicate item 24 and leave the required SM2-21 coverage absent.

**Minimal repair:** redesign 23 so its primary invariant is a tangent at a circle point or the contact chord, retain two genuine axes, and regenerate its novelty row. Only retag to SM2-22 if the coordinator separately re-freezes the coverage ruler and supplies a replacement SM2-21 item.

### [HIGH] F4 — item 24 has only one nonnumeric change from catalog representative `#3-19`
File: `output/260830/parts/W1_I3A.md:140-163`; ledger `output/260830/parts/W1_I3A.novelty.tsv:8`

The exact core route—external point line family, distance equals radius, quadratic in slope, Vieta—is already the canonical `#3-19` route. Asking the reciprocal sum instead of a sum/product is one target-axis transformation; moved coordinates/radius are numeric.

**Minimal repair:** add a second structural axis that changes the condition-to-target path rather than merely post-processing the same Vieta pair, then update the row.

### [MEDIUM] F5 — item 18 claims inactive `DF5`
File: `output/260830/parts/W1_I3A.md:41`

The solution is routine general-form completion of squares and quadratic-vertex minimization. It does not require the DF5 insight class (substitution/symmetry/induction or comparable conceptual jump).

**Minimal repair:** remove `DF5` and retain `T2` based on the actual 2–3 step DF1 path, or redesign the item to require a genuine DF5 insight.

### [MEDIUM] F6 — item 22 has a deletable half-condition
File: `output/260830/parts/W1_I3A.md:96`

For `y=-x+c`, both intercepts equal `c`. Either “x-intercept positive” or “y-intercept positive” alone selects `c=2`, so “both positive” fails the strict deletion audit.

**Minimal repair:** keep only one positivity condition. This does not cure F2; novelty still needs redesign.

### [MEDIUM] F7 — item 23 states derived externality as a condition
File: `output/260830/parts/W1_I3A.md:118`

From the supplied coordinates, `OQ=13>5`; moreover the stem already says there are two tangents. Deleting “원의 외부에 있는” changes no solution or uniqueness.

**Minimal repair:** delete the derived descriptor, or replace it with a condition that genuinely selects/changes the target during the SM2-21 redesign.

### [MEDIUM] F8 — three malformed LaTeX spacing tokens
File: `output/260830/parts/W1_I3A.md:55,79,83`

Literal `qquad` is rendered as math letters, not spacing. The author WIP’s claim of “no malformed quad” is false for these frozen bytes.

**Minimal repair:** replace each `,qquad` with `,\qquad` and rerun the static/render scan.

### [LOW] F9 — item 24 uses undefined center notation
File: `output/260830/parts/W1_I3A.md:159`

`OP` appears although the center was never named `O`.

**Minimal repair:** introduce `O(2,-1)` before using `OP`, or write the center-to-`P` distance explicitly.

## §4 Deterministic evidence

Exact novelty command:

```text
python -X utf8 tools/check_novelty_ledger.py --set output/260830/parts/W1_I3A.md --ledger output/260830/parts/W1_I3A.novelty.tsv --required-count 7
expected_ids=['17', '18', '19', '21', '22', '23', '24']
observed_ids=['17', '18', '19', '21', '22', '23', '24']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
exit=0
```

Exact arithmetic decisive output:

```text
17 center=(-1,4) r2=13 coeffs=(2,-8,4) answer=-2
18 r2=2*t**2-8*t+14 vertex=2 min=6
19 solutions=[-2,-1,0] sum=-3
21 roots=-5±4*sqrt(5) distances=[4,4] product=-55
22 c=[-2,2] selected=2 area=2
23 tangent_points=[(38/13,-34/13),(38/13,86/13)] sums=[4/13,124/13]
24 poly=27*m**2-48*m+7 discr=1548 reciprocal_sum=48/7 vertical_distance(x=8)=6
solve_back=PASS 7/7
```

Static scan:

```text
item_headers=['17','18','19','21','22','23','24']
tag_count=7
separator_count=6
display_delimiters=76 balanced=True
figure_dependencies=[]
malformed_math_tokens=[line55 literal_qquad, line79 literal_qquad, line83 literal_qquad]
structural/no-figure=PASS
render-token=FAIL
```

No `lsp_diagnostics` or `ast_grep_search` tool is registered in this runtime. The reviewed targets are Markdown/TSV rather than source code; exact arithmetic, the repository novelty CLI, token/static scans, and canonical/manual comparison are the available diagnostics. No fallback/workaround branch exists in the reviewed artifacts.

## §5 Stop / next gate

**STOP: advisory revise-required.** Math correctness alone passes, but the bundle fails frozen acceptance on catalog type/novelty, strict condition deletion, DF evidence, and render tokens. The author must repair only its exclusive targets, regenerate the WIP evidence, and return new frozen hashes before another independent advisory review. No external solve-back, approval, release, or ledger update is authorized by this report.

Pipeline: SET-260830-math2-40 → Wave 1 authoring → **W1-I3A independent advisory review: revise-required** → author repair → fresh review → external solve-back (not started)
Stage: Codex/OMX = gpt-5.6-sol — exact math 7/7 and novelty CLI contract pass, but HIGH findings remain for items 17/22/23/24; condition/DF/render findings also require repair.
Team: mode=solo; lead=code reviewer | gpt-5.6-sol | independent advisory reviewer | complete; lanes=code-reviewer = gpt-5.6-sol = high | independent reviewer | review-only complete | `C:\dev\study\AGENTS.md`, `.claude/agents/item-writer.md`, `analysis/catalog/math2.md`, `analysis/catalog/AUTHORING_GUIDE.md`; independence=independent (`fork_turns=none`); planned/unavailable/failed lanes=observed runtime model/depth proof unavailable
Next: parent freezes this review, routes findings to the W1-I3A author, and stops until repaired candidate/novelty/WIP hashes and a zero-malformed-token scan are supplied.