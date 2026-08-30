---
task: SET-260830-math2-40_W1_I3A
actor: Codex/OMX
role: item-author
status: done
intended_use: practice
exclusive_writer: /root/math2_w1_i3a_author
exclusive_outputs:
  - output/260830/parts/W1_I3A.md
  - output/260830/parts/W1_I3A.novelty.tsv
  - analysis/wip/item-writer_260830_SET-260830-math2-40_W1_I3A.md
---

# W1-I3A authoring WIP

| slice | unit IDs | result | verification |
|---|---|---|---|
| 1 | 17,18,19,21,22,23,24 | authored 7 figure-independent Korean items with exact SM2-15/T1, SM2-17/T2, SM2-18/T3, SM2-19/T2, SM2-20/T2, SM2-21/T3, SM2-22/T3 assignments | exact solve-back PASS 7/7; deletion/uniqueness PASS 7/7; novelty CLI PASS warnings=0 exit=0; static/render PASS |
| 2 (R1) | 17,18,19,21,22,23,24 | applied frozen advisory findings F1-F9; redesigned 17/22/23/24, corrected item 18 DF, repaired all literal spacing tokens, regenerated affected novelty evidence | exact solve-back PASS 7/7; strict deletion PASS 7/7; semantic novelty PASS 7/7 author audit; novelty CLI PASS warnings=0 exit=0; static/render PASS |

## Equation and condition-deletion audit

- 17: midpoint `(-1,4)`, `r²=13`, general form coefficients `(2,-8,4)`, target `-2`. Deleting either diameter endpoint leaves the specified diameter and circle undetermined.
- 18: `r²=t²+(t-3)²-(2t-5)=2(t-2)²+6`; unique equality parameter `t=2`; positivity proves a circle for every real `t`. Deleting the displayed family or real-parameter domain destroys the requested minimization; no added branch condition is present.
- 19: (가) gives `-3<t<3`; (나) gives `t<1 or t>7`; integer intersection `{-2,-1,0}`, sum `-3`. Delete (가): infinitely many negative integers satisfy (나); delete (나): candidates become `{-2,-1,0,1,2}` and target changes to `0`; delete integrality: infinitely many solutions.
- 21: chord half-length gives `d=4`; line distance `|k+5|/√5=4`; roots `-5±4√5`, product `-55`. Delete chord length: `k` is undetermined; delete fixed circle: distance/radius is undetermined. Both branches form real chords and target depends on both.
- 22: tangent family `y=-x+c`; distance gives `c=±2`; positive-intercept condition uniquely selects `c=2`; area `2`. Delete the positive-intercept condition: two tangent lines remain and only one bounds the requested positive-axis triangle, so the named line is not unique. Delete tangency or slope: infinitely many lines remain.
- 23: `OQ=13`, `OH=25/13`, `PH=60/13`; upper contact point `(38/13,86/13)`, sum `124/13`. Delete `b>2`: lower symmetric contact point `(38/13,-34/13)` gives sum `4/13`, so target changes; delete external point or circle: contact point is undetermined.
- 24: tangent condition yields `27m²-48m+7=0`; reciprocal sum `(48/27)/(7/27)=48/7`. The point and circle are both necessary to determine the line family and tangency equation. `OP=2√13>3`, discriminant `1548>0`, and product `7/27≠0` verify existence, distinctness, and definition of the target.

## Semantic novelty audit

- Compared item-by-item against `output/260822/공통수학2_도형의방정식_모의40.md`, `output/260829/260829_02_math2_comprehensive_25.md`, and qualified pilot `output/260830/parts/P1.md`.
- Each ledger row names at least two substantive nonnumeric changes. Coordinate, coefficient, length, sign, and symbol changes were not counted as axes.
- Item 21 deliberately uses inverse chord-length recovery for a line family; it does not use prior A 19's simultaneous area-bisector/center-joining omission route.

## Verification evidence

- Exact SymPy solve-back: `17=-2`; `18=(min r²,t)=(6,2)`; `19={-2,-1,0}, sum=-3`; `21 k=-5±4√5, product=-55`; `22 c=2, area=2`; `23 P=(38/13,86/13), sum=124/13`; `24 27m²-48m+7=0, reciprocal sum=48/7`. Result `PASS 7/7`.
- Required novelty command: `python -X utf8 tools/check_novelty_ledger.py --set output/260830/parts/W1_I3A.md --ledger output/260830/parts/W1_I3A.novelty.tsv --required-count 7`.
- Novelty output: `expected_ids=['17','18','19','21','22','23','24']`, same observed IDs, `duplicate_ids=[]`, `missing_ids=[]`, `extra_ids=[]`, `warnings=0`, `novelty-gate: PASS`, `exit=0`.
- Static/render scan: item headers and type/Tier sequence exact; answer/solution/trap counts `7/7/7`; 76 display-math delimiters balanced; 7 item blocks; no duplicate separators, figure dependency, odd math-delimiter lines, or malformed `quad`; TSV schema 8 columns and 7 exact rows. Result `PASS`.
- §1-B applicable sweep: scope confirmed by authorized curriculum; no descriptive item so grading-criteria coverage is not applicable; every solution contains intermediate equations; separators and bold answers are consistent; DF and E codes are postfix-separated; no duplicate separator; all seven ledger rows evidence two nonnumeric axes; `FAIL=0`.

## Frozen hashes

- Authorized-input manifest SHA-256 (path + per-file digest over the 15 supplied read inputs): `44f0f5d0a1cddad94c3a2074a717a9dca4fd380c3a7544ba1198ca24fb4b8a96`.
- `output/260830/parts/W1_I3A.md`: 7032 bytes, SHA-256 `c59623920b5ff674f91ea6f034cd46b1cbacdb582340e3cd62a517dc71f24e1d`.
- `output/260830/parts/W1_I3A.novelty.tsv`: 5182 bytes, SHA-256 `ccd7ac8091d6561010e463d1232803b046d37b4adf616db3bdf070406ad9c8a1`.

## R1 remediation history

- Frozen review verified before editing: `output/260830/rev/W1_I3A_ADVISORY_REVIEW.md`, 13160 bytes, SHA-256 `f33a7e3276022f17d555385bf7d61f27da81fc66e2a55ed018150c1443f2b205`.
- The slice-1 equation/deletion evidence and hashes above are retained as historical frozen evidence and are superseded by this R1 section for redesigned items 17, 22, 23, and 24.
- F1 item 17: replaced diameter-endpoint/general-coefficient route with three-point circle determination. Symmetric points A/B generate the center locus; point C fixes `t=3/2`; radius `5/2`. Non-numeric axes versus catalog #3-3 are three pass-points with a derived perpendicular-bisector locus, and radius target rather than equation/coefficient target.
- F2/F6 item 22: inverted the fixed-slope tangent route. The tangent is fixed while the circle-center parameter is unknown; `a=±√5`, and the non-area target is center distance `2√5`. No positivity condition remains.
- F3/F7 item 23: restored the SM2-21 tangent-at-point invariant `ax+by=25`. Incidence through Q gives `6a+8b=25`, the circle gives `a²+b²=25`, and `b<0` selects the unique point with answer `(7+√3)/2`. No derived externality descriptor remains.
- F4/F9 item 24: defined `O(0,0)` and added inverse parameter recovery. The slope quadratic `(p²-4)m²-6pm+5=0` plus the given sum gives `p=-1 or 4`; `p>0` selects 4; the distinct structural target is tangent length `√21`. Tag is honest `DF1·DF2·DF9`.
- F5 item 18: removed inactive `DF5`; retained `T2·DF1` for the routine 2–3 step completion-of-squares route.
- F8: repaired all three literal `qquad` tokens. Final scan reports `literal_qquad=[]`, `literal_quad=[]` while preserving valid `\qquad` and `\quad` commands.

## R1 strict condition-deletion audit

- 17: deleting any one of A, B, or C leaves only two prescribed points and infinitely many circles; all three points are required. The coordinates independently prove noncollinearity, so no redundant descriptor is stated.
- 18: deleting the parameterized circle family removes the minimized quantity; the real domain is the declared parameter domain, and no branch selector is present.
- 19: deleting (가) leaves infinitely many negative integers under (나); deleting (나) changes the set to `{-2,-1,0,1,2}` and the sum to 0; deleting integrality gives infinitely many real values.
- 21: deleting the chord length leaves k undetermined; deleting the circle or line family removes the radius/distance relation. Both absolute-value branches are required by the product target.
- 22: deleting tangency leaves every center parameter possible; deleting the fixed line or circle family removes the distance equation. The two center solutions are both required to define `PQ`.
- 23: deleting Q-incidence leaves every point of the lower semicircle possible; deleting `b<0` leaves two contact points whose target values `(7∓√3)/2` differ; deleting the circle removes the tangent-at-point locus.
- 24: deleting the slope-sum condition leaves p undetermined; deleting `p>0` additionally permits `p=-1`, changing the tangent length from `√21` to `√6`; deleting the circle or point family removes the tangent equation. The statement that both slopes and their sum exist also excludes the vertical-tangent degeneracy `p²=4` rather than adding a redundant condition.

## R1 verification and frozen candidate hashes

- Exact solve-back: `17 r=5/2`; `18 (min r²,t)=(6,2)`; `19 sum=-3`; `21 product=-55`; `22 PQ=2√5`; `23 a+b=(7+√3)/2`; `24 p=4, tangent length=√21`. Result `PASS 7/7` with unique/branch checks.
- Semantic author audit against the full SM2-15/17/18/19/20/21/22 catalog descriptions, prior A, prior B, and qualified P1: supported 7/7; each ledger row names two substantive nonnumeric axes and does not count coordinate/coefficient/sign changes.
- Type/Tier sequence: `SM2-15/T1, SM2-17/T2, SM2-18/T3, SM2-19/T2, SM2-20/T2, SM2-21/T3, SM2-22/T3`, exact 7/7. Tier/DF routes: 17 `DF1`; 18 `DF1`; 19 `DF1·DF2·DF4·E5`; 21 `DF1·DF8`; 22 `DF1·DF8`; 23 `DF1·DF2·DF4·E6`; 24 `DF1·DF2·DF9`.
- Static/render: exact headers and tags; answer/solution/trap `7/7/7`; 78 display delimiters balanced; six separators; no duplicate separators, figure dependency, odd math lines, literal `qquad`, or literal `quad`. PASS.
- Novelty CLI required-count 7: expected/observed IDs `17,18,19,21,22,23,24`; duplicates/missing/extra `[]`; warnings `0`; `novelty-gate: PASS`; exit `0`.
- `output/260830/parts/W1_I3A.md`: 7255 bytes, SHA-256 `f3585d02532b9ae9cd87367e689dd791e62360d287fca3a29611cea1111de0c5`.
- `output/260830/parts/W1_I3A.novelty.tsv`: 5477 bytes, SHA-256 `34e126e9c79df7cd06e2a7e6a061fba2ec865bac8afeb692e86aaef39541b5b6`.

NEXT: parent coordinator freezes the R1 candidate and routes it to independent advisory re-review; stop until a fresh review artifact exists. No external solve-back, integration, or shared-ledger write is authorized by this author lane.
