---
task: SET-260830-math2-40_P1
actor: Codex/OMX
role: item-writer pilot
model: gpt-5.6-sol
reasoning_depth: medium
status: done
intended_use: practice
exclusive_owner: output/260830/parts/P1.md; output/260830/parts/P1.novelty.tsv; analysis/wip/item-writer_260830_SET-260830-math2-40_P1.md
---

# Frozen-input gate

All 12 allowed inputs were recomputed before authoring; byte counts and SHA-256 values matched the assignment exactly. Hash gate exit code: 0. No `origin_data` or corpus PDF/transcript was read.

# Slice record

| slice | exact item IDs | result | validation | warnings |
|---|---|---|---|---|
| P1 pilot | 6, 12, 20, 30, 40 | authored 5 final candidates | self-solve 5/5; novelty PASS; count/type/Tier PASS | 0 final |

# First-pass self solve-back equations

- ID 6 / SM2-05: $PQ\parallel AC$, $QR\parallel BD$, hence rectangle iff $AC\perp BD$. With $AC=(8,4)$, write $D=(4+t,-1-2t)$. Area $20=\frac14(4\sqrt5)(|t|\sqrt5)=5|t|$, so $t=\pm4$; $y_D<-1$ uniquely selects $t=4$, $D=(8,-9)$.
- ID 12 / SM2-09: $l:y=2x$. Midpoint condition gives $b=2a+5$; perpendicular condition gives $a+2b=0$. Determinant is $-5\ne0$ and the unique solution is $(a,b)=(-2,1)$, so $a+b=-1$.
- ID 20 / SM2-16: $k=2h+3$, $r=k$ in quadrant II. Point condition gives $(h-2)^2+(k-1)^2=k^2$, hence $h^2-8h-1=0$. Roots $4\pm\sqrt{17}$; only $4-\sqrt{17}<0$, yielding unique $r=11-2\sqrt{17}>0$.
- ID 30 / SM2-24: $d=13$. External segment gives $(r_2-r_1)^2=169-144=25$; internal segment gives $(r_1+r_2)^2=169-88=81$. Positivity and $r_1<r_2$ give $r_2-r_1=5$, $r_1+r_2=9$, uniquely $(r_1,r_2)=(2,7)$. Existence check: $2+7<13$.
- ID 40 / SM2-33: reflect to $A'=(4,-3)$ and $B'=(-2,5)$. $A'B'=10$. Segment $(4-6t,-3+8t)$ hits the x-axis at $t=3/8$, $P=(7/4,0)$, then the y-axis at $t=2/3$, $Q=(0,7/3)$. Since $0<3/8<2/3<1$, equality is attained uniquely.

# Novelty evidence summary

Each item names two non-numeric changes in `P1.novelty.tsv`. The route changes are, respectively: theorem-to-inverse-coordinate proof, constructed-bisector-to-endpoint recovery, quadrant-selected radical radius, dual-tangent simultaneous radius inversion, and sequential two-boundary unfolding. Prior sets were used only for nearest-structure comparison.

# Validation evidence

The first independent exact-arithmetic pass exposed an author arithmetic slip in ID 6 (`20=5|t|` had initially been followed by `|t|=2`). The item, solution, trap, grading criterion, and WIP equation were corrected to `|t|=4`, and every gate below was rerun from the corrected files.

Independent SymPy/exact-arithmetic solve, final literal summary:

```text
ID6 area_roots= [-4, 4] selected_D= [(8, -9)] unique= True
ID12 solutions= [{a: -2, b: 1}] answer= -1 unique= True
ID20 all= [{h: 4 - sqrt(17), k: 11 - 2*sqrt(17)}, {h: 4 + sqrt(17), k: 2*sqrt(17) + 11}] valid= [{h: 4 - sqrt(17), k: 11 - 2*sqrt(17)}] radius= 11 - 2*sqrt(17) unique= True
ID30 all_positive= [{r1: 2, r2: 7}, {r1: 7, r2: 2}] valid= [{r1: 2, r2: 7}] unique= True
ID40 tP= 3/8 P= (7/4, 0) tQ= 2/3 Q= (0, 7/3) ordered= True total= 10 unique_intersections= True
self_solve_back: PASS 5/5
```

Novelty gate command:

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

Local count/type/Tier sweep, literal summary:

```text
item_count= 5
observed_id_type_tier= [('6', 'SM2-05', 'T3'), ('12', 'SM2-09', 'T2'), ('20', 'SM2-16', 'T3'), ('30', 'SM2-24', 'T4'), ('40', 'SM2-33', 'T4')]
expected_id_type_tier= [('6', 'SM2-05', 'T3'), ('12', 'SM2-09', 'T2'), ('20', 'SM2-16', 'T3'), ('30', 'SM2-24', 'T4'), ('40', 'SM2-33', 'T4')]
duplicate_ids= []
missing_ids= []
extra_ids= []
type_tier_sweep: PASS
stale_value_sweep: PASS
exit=0
```

AUTHORING_GUIDE §1-B local sweep: descriptive grading criteria present for ID 6; all solutions include intermediate equations; no tables; answer formatting is consistent; tags use separated DF/E postfix notation; no doubled separators; five items each have two evidenced non-numeric novelty axes; ledger coverage 5/5 with FAIL count 0.

NEXT: coordinator may consume these candidate artifacts and route `output/260830/parts/P1.md` to the required external `solve-back-verifier`; no external solve-back approval or release is claimed here.
