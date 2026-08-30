---
lane: code-reviewer
configured_model: gpt-5.6-sol
configured_reasoning_depth: high
observed_model: unavailable
observed_reasoning_depth: unavailable
independence: fork_turns=none
grade: advisory
verdict: revise-required
review_scope: P1 items 6,12,20,30,40 and five novelty rows
---

# P1 독립 자문 검토

## §0 요약

- 검토 범위: **5/5** (`6, 12, 20, 30, 40`), novelty 행 **5/5**.
- 수학 정답/유일성: **5/5 PASS**. SymPy 정확 연산으로 전 문항을 독립 재계산했다.
- 신규성 도구 계약: **evidence-contract PASS** (`warnings=0`, `exit=0`).
- 의미 신규성: **supported 3/5** (`6, 30, 40`), **not-supported 2/5** (`12, 20`). 도구 PASS는 의미 신규성을 증명하지 않는다.
- 난이도: `6=T3`, `12=T2`, `20=T3`, `40=T4`는 지지한다. `30=T4`는 지지하지 않으며 현재 구조는 **T3**가 타당하다.
- 형식/범위: 12번 해설에 literal LaTeX 결함 1건, 6번 해설에 범위 밖 벡터 표기 1건이 있다.
- 판정: **revise-required**. 의미 신규성 미지원 문항이 있으므로 후속 wave는 **BLOCKED**이다. 이는 외부 검증·승인·출시 판정이 아니다.

Finding counts: HIGH 2 / MEDIUM 3 / LOW 1 / total 6.

## §1 동결 해시와 쓰기 표면

| path | bytes | SHA-256 | result |
|---|---:|---|---|
| `output/260830/parts/P1.md` | 7257 | `ff10cfd8159c14973f8fffa8f1ab784c944faa2c71784442e9aa0e0b2f249fa9` | frozen match |
| `output/260830/parts/P1.novelty.tsv` | 2886 | `a401cada8a374d44242ee6714341fb9c8010995c3ead0f6a296dbc085204f7d7` | frozen match |
| `analysis/wip/item-writer_260830_SET-260830-math2-40_P1.md` | 4463 | `24678f284896393ec60934de7ac4ce3f748cb9da94b9f6e1b2f8bc3a5ee3ffa2` | frozen match |

Author write-surface isolation: the author WIP declares exactly the three paths above. Their timestamps form one contiguous pilot window (`00:38:54`–`00:41:33` KST); other files under `output/260830` predate it (`00:17`–`00:32`). No attributable write outside the declared author surface was observed. The repository is a shared dirty workspace, so unrelated paths cannot be attributed to this author from Git status alone; no such attribution is claimed.

## §2 문항별 독립 검토

| item | math | conditions | tier | novelty | format | verdict |
|---:|---|---|---|---|---|---|
| 6 | **PASS.** `AC=(8,4)`, perpendicular line through `B` gives `D=(4+t,-1-2t)`. `20=(1/4)(4√5)(|t|√5)=5|t|`, so `t=±4`; `y_D<-1` selects `D=(8,-9)`. | **PASS.** For the selected point, `P=(1,0), Q=(5,2), R=(7,-2), S=(3,-4)`, adjacent dot product is `0`, and area magnitude is `20`. Nonadjacent supporting-line intersections `(7,-2)` and `(3,-4)` lie outside at least one corresponding segment, so `ABCD` is concave but non-self-intersecting; the midpoint rectangle is nondegenerate. | **T3 supported:** proof + inverse coordinate branch + half-plane selection activates DF1/DF2/DF4. | **evidence-contract PASS; semantic novelty supported.** Relative to catalog `SM2-05` and prior A #6, the conclusion changes from midpoint coincidence to a rectangle iff proof and adds area/half-plane vertex recovery; prior B #7/#18 uses different centroid/area-bisector routes. | **REVISE:** solution uses `\overrightarrow{AC}`, `\overrightarrow{BD}` and “실수배” (`P1.md:18`), while `analysis/curriculum_2022.md:93` excludes vectors. No figure is needed. | revise-required |
| 12 | **PASS.** `l:y=2x`; midpoint gives `-2a+b=5`, perpendicularity gives `a+2b=0`; determinant `-5≠0`, hence `(a,b)=(-2,1)` and `a+b=-1`. | **PASS with a minor rigor note.** The perpendicular condition excludes `a=2` (a vertical `AB` cannot be perpendicular to slope `2`), but the slope division should state this before using `(b+1)/(a-2)`. | **T2 supported:** standard line construction plus two linear conditions; no genuine branch or nonstandard insight. | **evidence-contract PASS; semantic novelty not-supported.** Prior A #9 (`output/260822/...모의40.md:111-115`) already recovers an unknown endpoint from the midpoint and perpendicular conditions. Constructing `l` from a point and parallelism is one real changed axis, but `ab→a+b` and the ledger's “other endpoint recovery” claim do not supply a second changed solving axis. Prior B #15 being different does not cure the collision with prior A. | **FAIL:** `P1.md:47` contains `,quad` instead of `,\quad`, so literal `quad` renders as variables/text. | revise-required |
| 20 | **PASS.** `k=2h+3`, `r=k` in quadrant II, and `(h-2)^2+(k-1)^2=k^2` give `h^2-8h-1=0`. Only `h=4-√17<0`, with `k=11-2√17>0`, is valid. | **PASS.** The other root lies in quadrant I; the stated quadrant selects exactly one positive radius. | **T3 supported:** three conditions, a quadratic, and quadrant branch selection activate DF1/DF2/DF8. | **evidence-contract PASS; semantic novelty not-supported.** Prior A #18 (`...모의40.md:195-202`) already has the same one-axis tangency + center-line + pass-point quadratic skeleton. The quadrant selection changes the final branch/target, but the claimed first axis (“one axis instead of both axes”) is not changed against that nearest prior. Prior B #5 differs, but the every-prior requirement still fails. | PASS; no figure needed and all concepts are in I-3 scope. | revise-required |
| 30 | **PASS.** External tangent: `144=169-(r2-r1)^2`, so `r2-r1=5`. Internal tangent: `88=169-(r1+r2)^2`, so `r1+r2=9`. Positivity/order give `(r1,r2)=(2,7)` and the stated equations. | **PASS.** `r1+r2=9<13` proves the circles are externally disjoint and both internal common tangents exist; `|r2-r1|=5<13` also confirms external common tangents. | **T4 not supported; T3 supported.** The tangent types and formulas are named explicitly, the centers make `d=13` immediate, and the route is two substitutions plus a linear system. It lacks the T4 rubric's hidden condition and DF5 + (DF3 or DF7) insight/novelty load (`DIFFICULTY_RUBRIC.md:67-79`). | **evidence-contract PASS; semantic novelty supported.** Unlike prior A #30 (`...모의40.md:306-323`) and prior B #24 (`260829_02...md:239-245`), both radii are simultaneously inverted from the external/internal measurements, and the ordered circle equations are the target. | PASS; formulas, existence check, Korean notation, and no-figure sufficiency are sound. | revise-required |
| 40 | **PASS.** Reflecting gives `A'=(4,-3)`, `B'=(-2,5)` and lower bound `A'B'=10`. The segment `(4-6t,-3+8t)` meets the x-axis at `t=3/8`, `P=(7/4,0)`, then the y-axis at `t=2/3`, `Q=(0,7/3)`; direct substitution gives total `10`. | **PASS.** `0<3/8<2/3<1` proves the required order and equality attainment. Equality in the chained triangle inequality forces the same collinear order, and each axis intersection is unique, so `P,Q` are unique. | **T4 supported:** two reflections, three-segment unfolding, equality/order feasibility, and unique optimizer supply DF1 4+, DF2, DF5, DF7. | **evidence-contract PASS; semantic novelty supported.** Prior A #39/#40 and prior B #14/#25 use one boundary or a boundary+circle; this item uses two distinct ordered coordinate-axis boundaries and requires both equality points. | PASS; within the permitted x/y-axis reflection scope and figure-independent. | pass |

## §3 세트 수준 게이트

Exact novelty command:

```text
python -X utf8 tools/check_novelty_ledger.py --set output/260830/parts/P1.md --ledger output/260830/parts/P1.novelty.tsv --required-count 5
expected_ids=['6', '12', '20', '30', '40']
observed_ids=['6', '12', '20', '30', '40']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
exit=0
```

Independent exact-arithmetic decisive output:

```text
ID6 area_roots= [-4, 4]; selected D=(8,-9); midpoint rectangle area magnitude=20; non-self-intersecting=True
ID12 solutions= [{a: -2, b: 1}]; answer=-1; unique=True
ID20 valid_QII= [{h: 4 - sqrt(17), k: 11 - 2*sqrt(17)}]; unique=True
ID30 valid= [{r1: 2, r2: 7}]; ext_len=12; int_len=2*sqrt(22); four_common_tangents=True
ID40 tP=3/8; tQ=2/3; ordered=True; lower_bound=10; total=10; unique_axis_intersections=True
solve_back=PASS 5/5
```

Static format scan:

```text
item_headers=['6', '12', '20', '30', '40']
unmatched_dollar_lines=[]
duplicate_separators=False
literal_quad_without_slash=[47]
vector_tokens=[18]
markdown_static_scan=FAIL
```

No `lsp_diagnostics` or `ast_grep_search` tool is registered in this runtime. The targets are Markdown/TSV rather than typed source; therefore the exact CLI, exact-arithmetic solve-back, line-level literal scan, and manual canonical review are the available diagnostics. No approval is issued.

## §4 Ordered findings and minimal repair proposals

1. **[HIGH] Item 12 semantic novelty is unsupported** — `output/260830/parts/P1.novelty.tsv:3`; collision evidence `output/260822/공통수학2_도형의방정식_모의40.md:111-115`. The prior already uses the same endpoint-recovery skeleton. **Minimal repair:** redesign the item, not the ledger: keep the perpendicular-bisector invariant but change a second structural axis that changes the route (for example a rhombus/diagonal or locus/area target), rather than changing only the final coordinate combination. Then rewrite the novelty row against prior A #9 and rerun the gate.
2. **[HIGH] Item 20 semantic novelty is unsupported** — `P1.novelty.tsv:4`; collision evidence `...모의40.md:195-202`. The claimed “one axis + center line + pass point” axis is already prior A #18. **Minimal repair:** replace that quadratic skeleton with a genuinely different condition route (for example one-axis tangency plus two-point/other geometric determination), retain a nonnumeric branch axis, and re-evidence both axes against A #18/#19 and B #5.
3. **[MEDIUM] Item 30 is over-tiered as T4** — `P1.md:83-108`; rubric `analysis/catalog/DIFFICULTY_RUBRIC.md:67-79`. Named formulas + immediate `d` + sum/difference system is standard T3 inverse work, not the required hidden-condition/insight bundle. **Minimal repair:** either retag to `T3` and remove unsupported `DF5`, or redesign the stem so the tangent type/branch must be inferred and add a genuinely coupled second-stage target if slot 30 must remain T4.
4. **[MEDIUM] Item 6 solution uses an explicitly out-of-scope vector representation** — `P1.md:18-20`; scope guard `analysis/curriculum_2022.md:93`. **Minimal repair:** replace vector language with slopes: `AC` has slope `1/2`, hence the perpendicular line `BD` through `B` has slope `-2`; set `x_D=4+t`, so `D=(4+t,-1-2t)`.
5. **[MEDIUM] Item 12 contains malformed literal LaTeX** — `P1.md:47`. `,quad` is not `\quad` and will render as letters. **Minimal repair:** change it to `,\quad` (or split the two equations onto separate display lines) and rerun the literal scan.
6. **[LOW] Item 12 divides by `a-2` without stating the excluded vertical case** — `P1.md:47`. The geometry does exclude `a=2`, so the result is correct, but the intermediate justification is incomplete. **Minimal repair:** state that `l` has slope `2`, hence `AB` has slope `-1/2` and therefore `a≠2`, before writing the quotient.

All fixes are proposals only. The item author owns changes to `P1.md`, its novelty ledger, and the author WIP.

## §5 Stop / resume

**STOP: revise-required; next wave BLOCKED.** Resume only after the author supplies new frozen bytes/SHA-256 for the changed P1 artifacts. On resume: (1) re-freeze hashes, (2) rerun the exact novelty CLI, (3) independently solve all changed items, (4) recheck semantic novelty for 12/20 against both prior sets, (5) recheck the 30 Tier decision, and (6) rerun the literal/scope scan. External solve-back authority and release approval remain outside this advisory lane.

Pipeline: SET-260830-math2-40 → P1 author pilot → **independent advisory review: revise-required** → novelty remediation → external solve-back (not started)
Stage: Codex/OMX = gpt-5.6-sol — 5/5 math recomputation PASS and evidence-contract PASS, but semantic novelty fails for 12/20; wave is BLOCKED pending author repair.
Team: mode=solo; lead=code reviewer | gpt-5.6-sol | advisory reviewer | complete; lanes=code-reviewer = gpt-5.6-sol = high | independent advisory reviewer | complete, review-only | this task + `.claude/agents/item-writer.md` + `analysis/catalog/AUTHORING_GUIDE.md`; independence=independent (`fork_turns=none`); planned/unavailable/failed lanes=none
Next: author redesigns 12/20, retags or redesigns 30, and repairs 6/12 notation; stop condition is new frozen hashes plus zero-warning novelty gate and a clean re-review.
