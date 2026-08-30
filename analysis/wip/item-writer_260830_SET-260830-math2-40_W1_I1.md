---
actor: Codex/OMX
responsibility: item-writer
set_id: SET-260830-math2-40
bundle: W1_I1
status: done
intended_use: practice
exclusive_writer: Codex/OMX item-author W1-I1
exclusive_outputs:
  - output/260830/parts/W1_I1.md
  - output/260830/parts/W1_I1.novelty.tsv
  - analysis/wip/item-writer_260830_SET-260830-math2-40_W1_I1.md
lane: item-author = gpt-5.6-sol = medium
observed_model: unavailable
observed_reasoning_depth: unavailable
independence: fork_turns=none
instruction: .claude/agents/item-writer.md
---

# W1-I1 author WIP

## Staffing and bounded slice

| objective | exact units | source density / known defects | schema | write surface | lane | workload / concurrency | gate | stop / resume |
|---|---|---|---|---|---|---|---|---|
| Author five final no-figure Korean practice items | 5: `1=SM2-01/T1`, `2=SM2-02/T2`, `3=SM2-03/T2`, `4=SM2-04/T2`, `5=SM2-06/T2` | Catalog definitions plus two frozen prior sets and qualified P1 pilot; known risk is SM2-03 external-division deletion and numeric-swap novelty | full prompt, answer, complete solution, trap, descriptive grading criteria, exact type/Tier/DF tag; 8-column novelty TSV | the three paths in frontmatter only | item-author = gpt-5.6-sol = medium; observed runtime model/depth unavailable | one five-item slice, max concurrency 1 | exact solve 5/5, condition deletion, semantic novelty, type/Tier/static scan, required novelty CLI | stop after fresh PASS and hashes; resume only if a downstream reviewer returns a finding |

Pilot basis: `output/260830/parts/P1.md` and `output/260830/rev/P1_ADVISORY_REREVIEW_R2.md` were inspected before this wave. The pilot's explicit answer/solution/trap blocks, per-descriptive grading criteria, branch-dependent condition test, and eight-column novelty evidence pattern were retained. No `origin_data/` or `corpus/` path was read.

## Slice table

| slice | unit IDs | result | dropped | validation | status |
|---|---|---|---:|---|---|
| W1-I1 | 1, 2, 3, 4, 5 | five final items and five novelty rows written | 0 | exact solve 5/5; condition deletion 5/5; type/Tier exact; static/render PASS; novelty warnings 0 exit 0 | done |

## Semantic novelty proof

| item | invariant retained | visible nonnumeric axis changes | nearest-prior comparison and solving-route difference | verdict |
|---:|---|---|---|---|
| 1 | equal-distance locus is the perpendicular bisector | (a) constrained point → full-plane locus equation; (b) target distance/radius → line equation | Catalog #1-2/#1-3 and prior A #1 solve for a point or a coordinate expression; prior B #1 constructs a circumcenter from three vertices. This item expands one equality and cancels quadratic terms to determine the entire locus, with no axis constraint or third vertex. | PASS |
| 2 | a one-parameter squared-distance sum is minimized at a quadratic vertex | (a) axis/segment → oblique line; (b) weighted two-point/path sum → unweighted three-point square sum; (c) minimum value → optimizer coordinate | Prior A #2 places a point on an equilateral-triangle side and minimizes a two-term weighted sum. Prior B #14 reflects one endpoint to minimize a nonsquared path length. Here three independent distance squares are accumulated and completed to a square after oblique-line parameterization. | PASS |
| 3 | internal-division coordinates are endpoint-weighted averages | (a) fixed ratio → variable `k:(2-k)`; (b) quadrant/coordinate target → circle-interior region and continuous parameter interval | Prior A #3 converts a fixed ratio plus quadrant into an integer count; prior B #2 directly calculates one fixed internal point. This item remains strictly in-scope internal division, converts the point to a linearly parameterized coordinate, and then solves a circle-interior quadratic inequality. No external-division term or external point is used. | PASS |
| 4 | a prescribed distance on a whole line produces two opposite direction-component solutions | (a) one-sided extension → whole-line two-branch construction around B; (b) coordinate extrema/one coordinate → area of the triangle formed by both solutions and the origin | Prior A #4 uses two branches only to compare coordinate sums; prior B #21 fixes one branch and then computes a centroid. This item must retain both opposite candidates and transfer them into a determinant-area computation, so its target cannot be obtained by either prior route. | PASS |
| 5 | the centroid divides a triangle into three equal-area subtriangles | (a) midpoint/equilateral data → directly supplied centroid of a general triangle; (b) centroid coordinate or known equilateral subarea → area involving an unknown vertex | Prior A #5 reconstructs a vertex from a midpoint and asks for a centroid coordinate combination. Prior B #7 starts from a fully known equilateral triangle. This item avoids reconstructing C in the main route by transferring `[BCG]` to the fully known `[ABG]`, then uses the coordinate determinant; reconstruction is only an independent check. | PASS |

## Condition-deletion proof

Each stem condition was deleted one at a time before acceptance. A condition is retained only if the answer/solution set changes or the condition defines the named object/assessment contract.

| item | deletion test | exact effect | result |
|---:|---|---|---|
| 1 | delete either endpoint; delete `PA=PB`; delete `P(x,y)` | without an endpoint the distance comparison is undefined; without equality every plane point is allowed instead of one line; coordinates are definitionally required to request an equation | PASS |
| 2 | delete line; delete A; delete B; delete C | no line gives centroid `(3,1)` instead of `(4,2)`; deleting A gives `(9/2,3/2)`; deleting B gives `(15/4,9/4)`; deleting C gives `(15/4,9/4)`; every result differs from the full answer | PASS |
| 3 | delete circle-interior condition; delete either endpoint; delete internal-division relation | deleting the region gives the full internal-division domain `0<k<2` instead of `1-√2/2<k<1+√2/2`; deleting an endpoint or the division relation leaves P undefined. Positivity `0<k<2` is not a decorative separate condition: it follows definitionally from the two positive terms of an internal-division ratio. | PASS |
| 4 | delete line; delete length ratio; delete A or B; delete origin/triangle target | line deletion leaves a full circle of candidates; ratio deletion leaves all points on the line; endpoint deletion makes AB or the B-reference undefined; target-point deletion makes the requested area undefined | PASS |
| 5 | delete A, B, or G; delete centroid relation; delete full-solution instruction | A/B/G deletion makes the determinant or comparison triangle undetermined; without centroid status, equal areas and C are undetermined; deleting the instruction changes the descriptive grading contract | PASS |

No decorative side condition remained. The initially explicit `0<k<2` in item 3 was removed from the stem because internal division already entails positivity; it is derived in the solution instead. The parenthetical clarification that `AB`, `BC` denote lengths in item 4 was also removed as redundant notation.

## Exact solve-back and uniqueness

Fresh SymPy exact-arithmetic results:

```text
item1 locus=12*x-12*y-12 -> x-y-1=0; unique_locus=True
item2 f(t)=6*t**2-48*t+118=6*(t-4)**2+22; P=(4,2); unique=True
item3 P=(3*k-2,3*k); center-distance squared=18*(k-1)**2; range=(1-sqrt(2)/2,1+sqrt(2)/2); unique_range=True
item4 C1=(10,13); C2=(-2,-3); determinant area=2; exactly two line solutions=True
item5 C_check=(2,6); area(ABG)=area(BCG)=9/2; unique=True
solve_back=PASS 5/5
condition_deletion=PASS 5/5
```

Middle equations were checked independently from final answers. Item 2's minimum value is `22` but its requested optimizer is `(4,2)`; item 3 uses a strict interior inequality; item 4 retains both whole-line branches; item 5's direct determinant and reconstructed-C determinant agree.

## Tier / DF and format sweep

| item | exact target | observed structure | support |
|---:|---|---|---|
| 1 | SM2-01 / T1 / DF1 | one equality, quadratic cancellation, line normalization; one direct concept and one route | exact T1 |
| 2 | SM2-02 / T2 / DF1·DF3 | line parameterization, three-distance data accumulation, complete square, optimizer recovery | exact T2 |
| 3 | SM2-03 / T2 / DF1·DF3 | internal-point coordinate, circle-region substitution, quadratic inequality/domain check | exact T2 |
| 4 | SM2-04 / T2 / DF1·DF8 | two explicit direction branches followed by one determinant; no hidden insight or extended inverse chain | exact T2 |
| 5 | SM2-06 / T2 / DF1·DF3 | equal-area interpretation plus one coordinate determinant; descriptive criteria supplied | exact T2 |

Static/render scan:

```text
item_headers=['1','2','3','4','5']
type_tier_observed=[('SM2-01','T1'),('SM2-02','T2'),('SM2-03','T2'),('SM2-04','T2'),('SM2-06','T2')]
type_tier_exact=True
tag_df_slots=['DF1','DF1·DF3','DF1·DF3','DF1·DF8','DF1·DF3']
answer_blocks=5
solution_blocks=5
descriptive_items=['5']
grading_criteria=1
figure_dependencies=[]
circled_option_lines=[]
duplicate_separators=False
odd_bold_marker=0
static_render_scan=PASS
exit=0
```

AUTHORING_GUIDE §1-B: scope is confirmed as the I. 도형의 방정식 unit, so no unconfirmed-scope header is needed in this split part; descriptive criteria 1/1; middle equations 5/5; no table in this part; bold answer blocks 5/5; DF/E postfix syntax clean (no E code required); no duplicate separator; two-axis novelty 5/5; ledger coverage 5/5 with FAIL 0.

## Novelty evidence-contract CLI

Command:

```text
python -X utf8 tools/check_novelty_ledger.py --set output/260830/parts/W1_I1.md --ledger output/260830/parts/W1_I1.novelty.tsv --required-count 5
```

Fresh output:

```text
expected_ids=['1', '2', '3', '4', '5']
observed_ids=['1', '2', '3', '4', '5']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
exit=0
```

This CLI proves the evidence contract only. The semantic proof is the item-indexed comparison above and the five detailed TSV rows.

## Frozen hashes

Primary authorized inputs:

| path | SHA-256 |
|---|---|
| `.claude/agents/item-writer.md` | `b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2` |
| `analysis/catalog/math2.md` | `959414ba8ff8754e8d2331b2afd7385f42e93a9dcbb3c24d36022fb4191fd0d0` |
| `analysis/catalog/COMMON_TYPES.md` | `dd3541e3857e10bd71efd48144e29d4419bb9ebbd5bb56e64d3e9f20cd093e05` |
| `analysis/catalog/TYPE_MASTER.md` | `ff45bdf8f6f46689ccd68a5caa645e5c7be54bca456684f0483bee82db24bea9` |
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | `1533e2930d10fd30dc0f2dd371f22ce87035556bc5b5367e8abaf2bcebee0f69` |
| `analysis/catalog/AUTHORING_GUIDE.md` | `737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea` |
| `analysis/curriculum_2022.md` | `a746c017bf394e28a3c0fc73ceb3858af6323861abe1dd50101acf4c5cb4b58a` |
| `output/260822/공통수학2_도형의방정식_모의40.md` | `cdd6d528f6250ea24d43ebd7b50e85824284521c70b4967f7aaef8e4c2663324` |
| `output/260829/260829_02_math2_comprehensive_25.md` | `bac3216b3d2ab9a6d292e10e7632205a596404e6625b4add28b647298c608965` |
| `output/260830/parts/P1.md` | `69e5e9da451c8c86e283a70cc31ad6e731b24d77b9b7021b518d397d6b87b4c6` |
| `output/260830/parts/P1.novelty.tsv` | `84d13437b102c0581753d4103f270e664193dd94e2fc48678f545713c6313f0a` |
| `output/260830/rev/P1_ADVISORY_REREVIEW_R2.md` | `52a8d22cbfbcccb6c88b9a3a3001a364ad80a329640217ee630ded8e491dd53b` |
| `tools/check_novelty_ledger.py` | `7ecb8c0acbb83cd25ce399b3365efb0389b1773d46f41a38d9b82c586dc1ed7d` |

Frozen authored artifacts at completion:

| path | bytes | SHA-256 |
|---|---:|---|
| `output/260830/parts/W1_I1.md` | 5228 | `9b88ef8f7ff31ac807f26ac8e05a0325dc0244e488945c9c92ff0b51de821d91` |
| `output/260830/parts/W1_I1.novelty.tsv` | 3374 | `f730dfb764c3b565ef26d588723daa14a2589fae142730e3f9e034d09d2fe128` |

No shared ledger, canonical catalog, prior set, pilot, review artifact, origin data, corpus file, or repository history was written.

NEXT: coordinator freezes all three W1-I1 artifact hashes and routes this five-item candidate to a separate review/solve-back gate; stop here unless a concrete finding is returned.

## R1 remediation slice — current state (supersedes initial item-4 and DF evidence above)

Frozen review consumed without modification:

| path | bytes | SHA-256 | verdict |
|---|---:|---|---|
| `output/260830/rev/W1_I1_ADVISORY_REVIEW.md` | 13321 | `4f72bdde2d350ea70e3ad156d57881728dc52e52439fa2ecc58e8fcc517df7e6` | revise-required |

| slice | exact units | permitted writes | result | validation | status |
|---|---|---|---|---|---|
| W1-I1-R1 | finding 1: item 4 semantic redesign; finding 2: items 2/3/5 DF correction | `W1_I1.md`, `W1_I1.novelty.tsv`, this WIP only | item 4 rebuilt; DF3 removed from 2 and 5; item 3 changed to DF1·DF2 with simultaneous-condition rationale | solve 5/5; deletion 5/5; all-prior/P1 semantic comparison 5/5; exact tag/static PASS; novelty warnings 0 exit 0 | done; awaiting independent re-review |

### Finding closure

1. **Item 4 novelty — closed by substantive redesign, not ledger relabeling.** The old whole-line/two-branch item was deleted. The current item places C on the **segment** AB and uses `BC=(1/3)AB`, so direction is fixed from B toward A before the coordinate is computed. It then asks for `[OAC]`, not coordinate extrema, a centroid, or an area formed from two symmetric candidates.
   - Against catalog SM2-04 representative #1-8 and prior A #4: `whole line + two branches + linear coordinate extrema` changes to `segment interior + one directed branch + determinant area involving A and C`.
   - Against catalog representative #1-9 and prior B #21: `one-sided extension + endpoint coordinate/centroid continuation` changes to `segment interior + triangle-area target`.
   - Against qualified P1: P1 contains no SM2-04 item. Its determinant/area items use midpoint rectangles, rhombus diagonals, or center/contact geometry, not a segment length-ratio direction selection. No solving-route collision was found.
   - These are two visible nonnumeric axes against every nearest prior: **location/direction domain** and **target/solution route**.
2. **DF correction — closed.** Items 2 and 5 now carry DF1 only. Neither direct prose coordinate bundle activates DF3. Item 4's former DF8 was removed because the segment condition leaves one branch. No replacement code was invented.
3. **Item 3 DF2 rationale — active and recorded.** Solving requires both simultaneously active restrictions: (a) internal-division positivity and coordinate relation `P=(3k−2,3k)`, and (b) strict circle-interior inequality. The answer is the intersection of the region-derived interval with the internal-division domain. Deleting either condition changes or destroys the solution set. Therefore DF2 is active alongside DF1; DF3 is not.
4. **Reviewer clarification adopted.** `P(x,y)` in item 1 is notation, not an independent mathematical condition. The initial WIP wording counting its deletion as a condition test is withdrawn; the mathematical deletion test is endpoints plus `PA=PB` only.

### Current item-4 exact solution and condition minimality

```text
A=(1,1), B=(7,10), B-A=(6,9)
C=B-(1/3)(B-A)=(5,7)
[OAC]=(1/2)|1*7-1*5|=1
unique_segment_point=True

delete segment condition:
  C_alt=B+(1/3)(B-A)=(9,13)
  [OAC_alt]=(1/2)|1*13-1*9|=2
  requested value changes from 1 to {1,2}
delete BC=(1/3)AB: continuum of segment points and areas
delete A or B: AB or the reference ratio is undefined
delete O/A/C triangle target: requested quantity is undefined
condition_deletion_item4=PASS
```

The segment condition is therefore not decorative. It changes both the solution set and the requested value. Wording remains the SM2-04 curriculum-aligned direction-component/length-ratio formulation and does not use the deleted external-division term or internal-division terminology.

### R1 full solve/deletion regression

```text
item1=12*x-12*y-12 -> x-y-1; unique=True
item2=6*t**2-48*t+118; vertex=4; P=(4,2); minimum=22; unique=True
item2 deletions: no_line=(3,1), omit_A=(9/2,3/2), omit_B=(15/4,9/4), omit_C=(15/4,9/4)
item3 P=(3*k-2,3*k); center_distance_squared=18*(k-1)**2
item3 range=(1-sqrt(2)/2,1+sqrt(2)/2); within_internal_domain=True; unique=True
item4 C=(5,7); area=1; deleted_segment_alt=(9,13); alt_area=2
item5 C=(2,6); ABG=9/2; BCG=9/2; unique=True
solve_back=PASS 5/5
condition_deletion=PASS 5/5
```

### R1 current type/Tier/static sweep

```text
headers=['1','2','3','4','5']
tags=[
  ('SM2-01','T1','DF1'),
  ('SM2-02','T2','DF1'),
  ('SM2-03','T2','DF1·DF2'),
  ('SM2-04','T2','DF1'),
  ('SM2-06','T2','DF1')
]
answers=5 solutions=5 traps=5 descriptive_grading=1/1
figure_dependencies=[] circled_options=[] duplicate_separators=False
item3_internal_only=True
static_render_scan=PASS
exit=0
```

Tier remains exact: item 1 is one direct equality/cancellation concept (T1); items 2–5 each require a standard 2–3-step coordinate route without a hidden insight chain (T2). DF codes now describe only active features.

### R1 novelty evidence-contract gate

```text
python -X utf8 tools/check_novelty_ledger.py --set output/260830/parts/W1_I1.md --ledger output/260830/parts/W1_I1.novelty.tsv --required-count 5
expected_ids=['1', '2', '3', '4', '5']
observed_ids=['1', '2', '3', '4', '5']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
exit=0
```

The CLI remains evidence-contract-only. Current semantic novelty is supported 5/5 by the initial proof for items 1, 2, 3, 5 and the replacement item-4 proof above, checked against both prior sets and P1.

### R1 frozen authored artifacts

| path | bytes | SHA-256 |
|---|---:|---|
| `output/260830/parts/W1_I1.md` | 5005 | `5c88905b650c9d4a162be396f771dae8bacb08370b091e7e0139576f25d524d9` |
| `output/260830/parts/W1_I1.novelty.tsv` | 3484 | `103e7b8f5e1d56192feb65e33a09edd480209e34c8da26a250fad53297be96f4` |

NEXT: coordinator freezes the R1 set, ledger, and WIP hashes and routes them to independent advisory re-review; do not route external solve-back until the two review findings are independently closed.
