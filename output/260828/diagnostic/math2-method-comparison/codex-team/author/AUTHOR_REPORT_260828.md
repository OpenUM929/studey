# EX-math2-20252M Codex assurance author 진단 보고서 — revision 1

## 1. 성격·권한·수정 범위

- 이 문서는 Codex assurance-team의 assessment evidence author가 작성한 22문항 진단 초안의 1차 수정본이다.
- 외부 Claude Code Opus `type-proposer`의 제안·판정·승인을 대신하지 않는다.
- 전 문항에 rendered page가 없어 `no pNN`이며 formal proposal readiness는 22/22 `BLOCKED-no-pNN`이다.
- `answer_key: null`. 정답, 정답 조합, 수치 결과, solve-back 인증을 주장하지 않는다.
- S-17은 `f` 정의가 없는 source defect이므로 assignment와 Tier가 모두 정확히 `BLOCKED`다.
- revision input으로 독립 감사 `audit/EVIDENCE_AUDIT_260828.md`와 독립 비평 `critique/ADVERSARIAL_CRITIQUE_260828.md`를 읽었다. 두 review artifact는 수정하지 않았다.
- Opus 제출물과 종전 Codex diagnostic/trace는 계속 열거나 검색하지 않았다.
- corpus, canonical, ledger, WIP, pilot/wave, audit/critique, gate 파일을 수정하지 않았다.

## 2. runtime identity·독립성·exclusive write

- runtime identity: native canonical task name `/root/math2_sol_author`
- opaque host ID: 실행 표면에 별도 노출되지 않아 추론하지 않음
- lane = model = reasoning depth: `author = gpt-5.6-sol = high`
- role instruction: `.codex/agents/assessment-author-sol.toml`
- target-role instruction: `.claude/agents/type-proposer.md`
- exclusive-write declaration: revision에서는 아래 세 author 파일만 수정했다.
  1. `output/260828/diagnostic/math2-method-comparison/codex-team/author/items.tsv`
  2. `output/260828/diagnostic/math2-method-comparison/codex-team/author/types.tsv`
  3. `output/260828/diagnostic/math2-method-comparison/codex-team/author/AUTHOR_REPORT_260828.md`

## 3. revision findings와 disposition

| review finding | revision disposition |
|---|---|
| S-17·S-18의 ASCII 손상 | 두 행을 UTF-8 한국어로 다시 작성했고 ASCII 물음표·U+FFFD를 제거 |
| W-04 source span | coordinator correction에 따라 `transcript.md:44-48` 유지 |
| S-14 primary invariant | SM2-18 원-직선 위치 관계를 주축으로 변경, SM2-25는 개수 요구 보조로 제한 |
| SM2-26·27·31 과도 통합 | S-03, W-04, W-03·S-15를 각각 DIAG-G05, G04, G03으로 분리 |
| S-05와 S-13 과도 통합 | S-05를 DIAG-G07 decision-request로 독립, S-13은 U11 내부 독립 subgroup로 분리 표기 |
| S-10과 S-12 과도 통합 | 12-row 상한 때문에 같은 U10 bookkeeping row에 있으나 서로 독립 subgroup이며 reusable type 통합이 아니라고 명시 |
| S-07과 S-14 오통합 | 서로 다른 U10과 U11로 분리, S-07은 SM2-25, S-14는 SM2-18 primary |
| S-17의 reusable evidence 사용 | 별도 `BLOCKED-G12` exact-cover bucket으로 분리하고 variation·importance evidence에서 제외 |
| S-18 SM2-13 과대 주장 | SM2-13 주장을 제거하고 SM2-03/08을 구성 요소로만 기록한 ID-free 복합 좌표기하 decision request로 변경 |
| S-05 Tier | 배점 신호와 DF8의 긴장을 반영해 T2 경계로 상향 |
| S-17 Tier | 정확히 `BLOCKED`로 변경 |
| C-05 강화 과대 주장 | 전 문서에서 `insufficient evidence·형식만 관찰`로 하향 |
| C-09/S-15 경계 | ㄱ~ㅁ 모두 고르기와 C-09 절대문 사이의 decision evidence를 유지 |

## 4. identifier integrity

- expected identifiers: `[W-01, W-02, W-03, W-04, S-01, S-02, S-03, S-04, S-05, S-06, S-07, S-08, S-09, S-10, S-11, S-12, S-13, S-14, S-15, S-16, S-17, S-18]`
- observed identifiers: `[W-01, W-02, W-03, W-04, S-01, S-02, S-03, S-04, S-05, S-06, S-07, S-08, S-09, S-10, S-11, S-12, S-13, S-14, S-15, S-16, S-17, S-18]`
- duplicate identifiers: `[]`
- missing identifiers: `[]`
- extra identifiers: `[]`
- item counts: diagnostic assigned 21 / explicit item-level BLOCKED 1(S-17) / formal no-pNN BLOCKED 22.

## 5. staged method trace

1. **pilot-01**: manifest와 expected schema를 고정하고 `transcript.md:31-78`을 canonical보다 먼저 읽어 W-01..W-04,S-01..S-06을 작성했다. pilot gate가 exact 10 PASS한 뒤 멈췄다.
2. **wave-02a**: 같은 manifest를 다시 검증하고 `transcript.md:79-123`을 읽어 S-07..S-16을 작성했다. BIN0002는 bindata일 뿐 page evidence로 사용하지 않았다. wave2a gate가 exact 10 PASS한 뒤 멈췄다.
3. **wave-02b**: `transcript.md:124-146`과 `verify_log.tsv:8`을 읽었다. S-17의 f 정의 부재를 BLOCKED로 보존하고 S-18은 transcript 구조만 진단했다.
4. **integration v1**: 22 item rows와 9개 진단 통합군을 만들고 author gate를 통과했다.
5. **독립 review**: auditor는 S-17/S-18 문자 손상과 W-04 range convention을, critic은 S-14 오분류·과도 통합·Tier·C-05 문제를 지적했다.
6. **revision 1**: 손상 행을 복구하고 primary generator를 분리했다. 5~12 row 제약과 semantic truth가 충돌하는 잔여 singleton은 `BLOCKED exact-cover bookkeeping umbrella`로 표시해 reusable type처럼 주장하지 않았다.

## 6. revised per-item diagnostic index

| ID | exact source | revised diagnostic assignment | Tier | limitation |
|---|---|---|---|---|
| W-01 | `transcript.md:31-34` | SM2-08 | T1 | BLOCKED-no-pNN |
| W-02 | `transcript.md:35-38` | SM2-15 | T2 | BLOCKED-no-pNN |
| W-03 | `transcript.md:39-43` | SM2-31 | T3 | BLOCKED-no-pNN |
| W-04 | `transcript.md:44-48` | SM2-27 primary + SM2-11 secondary | T3 | BLOCKED-no-pNN |
| S-01 | `transcript.md:52-54` | SM2-03 | T1 | BLOCKED-no-pNN |
| S-02 | `transcript.md:55-59` | SM2-08 | T1 | BLOCKED-no-pNN |
| S-03 | `transcript.md:60-64` | SM2-26 | T1 | BLOCKED-no-pNN |
| S-04 | `transcript.md:65-69` | SM2-03 + SM2-08 | T1 boundary | BLOCKED-no-pNN |
| S-05 | `transcript.md:70-73` | ID-free decision request: parameter-line intersection quadrant range | T2 boundary | BLOCKED-no-pNN |
| S-06 | `transcript.md:74-78` | SM2-15 then SM2-19 | T1 | BLOCKED-no-pNN |
| S-07 | `transcript.md:79-81` | SM2-25 primary + SM2-11 secondary | T2 | BLOCKED-no-pNN |
| S-08 | `transcript.md:82-85` | SM2-01 | T2 | BLOCKED-no-pNN |
| S-09 | `transcript.md:86-88` | SM2-01 + SM2-09 | T2 | BLOCKED-no-pNN |
| S-10 | `transcript.md:89-93` | SM2-33 | T2 | BLOCKED-no-pNN |
| S-11 | `transcript.md:94-96` | SM2-12 | T2 | BLOCKED-no-pNN |
| S-12 | `transcript.md:97-100` | ID-free decision request: distance-difference maximum | T2 | BLOCKED-no-pNN |
| S-13 | `transcript.md:101-104` | SM2-10 primary + SM2-11 secondary | T3 | BLOCKED-no-pNN |
| S-14 | `transcript.md:105-107` | SM2-18 primary + SM2-25 secondary | T3 | BLOCKED-no-pNN |
| S-15 | `transcript.md:108-119`, `BIN0002.bmp` | SM2-31 + COMMON_TYPES boundary request | T3 | BLOCKED-no-pNN; bindata-only |
| S-16 | `transcript.md:120-123` | SM2-12 + SM2-21 | T3 | BLOCKED-no-pNN |
| S-17 | `transcript.md:124-137`, `verify_log.tsv:8` | **BLOCKED** | **BLOCKED** | undefined f + BLOCKED-no-pNN |
| S-18 | `transcript.md:138-146` | ID-free complex coordinate-geometry decision request; SM2-03/08 are components only | T3 | exact generator uncertain + BLOCKED-no-pNN |

세부 rationale, tier_basis, observed_trap, confidence는 `items.tsv`의 exact 10-column schema에 기록했다.

## 7. 12-row exact-cover design

### 7.1 semantic rows
1. `DIAG-G01` W-01,S-02 — SM2-08.
2. `DIAG-G02` W-02,S-06 — shared circle-determination stage, but W-02 final SM2-15 and S-06 final SM2-19 are distinguished.
3. `DIAG-G03` W-03,S-15 — SM2-31 transformation composition and equation expression.
4. `DIAG-G04` W-04 — standalone SM2-27 primary generator with SM2-11 secondary.
5. `DIAG-G05` S-03 — standalone SM2-26 point translation.
6. `DIAG-G06` S-01,S-04 — SM2-03 internal division; S-04 adds SM2-08.
7. `DIAG-G07` S-05 — standalone ID-free decision request.
8. `DIAG-G08` S-08,S-09 — SM2-01 equidistance; S-09 adds SM2-09.
9. `DIAG-G09` S-11,S-16 — SM2-12 angle-bisector invariant; S-16 adds SM2-21.

### 7.2 non-reusable bookkeeping rows required by the 12-row ceiling
- `DIAG-U10` S-07,S-10,S-12 — **BLOCKED exact-cover bookkeeping only**. It contains three explicitly independent subgroups: SM2-25 distance extremum, SM2-33 reflected shortest path, and reverse-triangle-inequality decision request. S-10 and S-12 are not one reusable type.
- `DIAG-U11` S-13,S-14,S-18 — **BLOCKED exact-cover bookkeeping only**. It contains three explicitly independent subgroups: SM2-10/11, SM2-18 primary, and unsupported-exact-match S-18 decision request. S-05 and S-13 remain separated, and S-14 is not grouped with S-07.
- `BLOCKED-G12` S-17 — source-defect exact-cover bucket only. It supplies no variation-axis, importance, COMMON_TYPES, or generation evidence.

`types.tsv` has 12 rows and exact exclusive membership cover. U10/U11/G12 are not called reusable types; their nonblank axis fields document subgroup separation or BLOCKED status rather than invented common variation axes.

## 8. observed variations and traps

### supported reusable or provisional semantic rows
- G01 varies direct line construction versus coefficient determination; trap is slope sign and negative reciprocal.
- G02 varies circle determination evidence and final output; trap is diameter-radius and chord-distance confusion.
- G03 varies transformation composition and response mode; trap is order and substitution-sign reversal.
- G04 varies how a parabola translation is inferred and which line property follows; trap is coefficient comparison and parallel-distance denominator.
- G05 varies translation vector and post-translation locus; trap is direction reversal.
- G06 varies direct internal-point output versus a perpendicular-line follow-up; trap is weight order.
- G07 varies parameter placement and strict region condition; trap is denominator sign and intersection of inequalities.
- G08 varies equidistance target and locus restriction; trap is missing the perpendicular-bisector or positive-coordinate filter.
- G09 varies angle-bisector source and subsequent tangent output; trap is wrong plus-minus branch or quadrant.

### non-reusable rows
- U10 and U11 list each independent subgroup's observed trap separately and do not aggregate importance.
- G12 records only the source-integrity trap of inventing an absent f definition.

## 9. source-axis importance

- Current past-exam evidence is one round, `2025-2M`; every supported subgroup is at most `★(기출 1회)`.
- Multiple items in the same round do not raise the year-repetition axis.
- Workbook stars remain separate: for example SM2-33 `★★★(부교재 4문항)`, SM2-18 `★★`, SM2-31 `★★`.
- G01-G09 keep past-exam and workbook axes separate.
- U10/U11 explicitly block aggregate importance and list subgroup axes separately.
- S-17 is excluded from all importance evidence. Partial readable geometry does not count as type frequency.

## 10. COMMON_TYPES comparison

- **C-05 insufficient evidence**: transcript shows `서술형` and `단답형` sections, but it does not provide the scoring conditions, partial-credit allocation, or explicit solution-process requirements that define C-05(`COMMON_TYPES.md:44-51`). Therefore only response-format observation is recorded; no C-05 reinforcement is claimed.
- **C-09 supported with boundary evidence**: most items are non-five-choice `구하시오` forms. S-15 uses ㄱ~ㅁ `모두 고르시오`, which directly tensions the absolute C-09 statement that mathematics has zero such forms(`COMMON_TYPES.md:66-94`).
- **C-01 no exact match**: S-15 has no ①~⑤ combination-choice layer, so it is not promoted to C-01. The C-01/C-09 boundary remains an ID-free decision request pending pNN.
- **C-02 limited**: S-15 has bindata but the textual center/radius and options are in transcript; image dependence is not asserted.
- S-17 is excluded from COMMON_TYPES evidence.

## 11. catalog disposition

### existing diff candidates — never applied
- `SM2-01, SM2-03, SM2-08, SM2-09, SM2-10, SM2-11, SM2-12, SM2-15, SM2-18, SM2-19, SM2-21, SM2-25, SM2-26, SM2-27, SM2-31, SM2-33`.
- S-14 now uses SM2-18 as primary and SM2-25 only as secondary count-axis support.
- W-04 is cited at the corrected exact content range `transcript.md:44-48`.
- Every status, frequency, representative example, and star update is HOLD because no pNN exists.

### ID-free decisions
1. S-05: extend SM2-07 or define a separate parameter-line quadrant-range type.
2. S-12: extend SM2-02 or define a separate distance-difference extremum type.
3. S-15: clarify C-01/C-09 boundary for mathematics ㄱ~ㅁ multiple-response form.
4. S-18: determine a reusable solve-path invariant only after independent solve-back; do not claim SM2-13 now.
5. S-17: all assignment, Tier, catalog disposition, and generation readiness remain BLOCKED until f definition is recovered.

No irreversible ID was created.

## 12. HARVEST_LOG draft

> canonical append가 아닌 revision 내용 초안이다. 실제 ledger schema를 새로 만들지 않는다.

- unit: `EX-math2-20252M`; exact 22 IDs
- assigned: 21; source-defect BLOCKED: S-17; formal no-pNN BLOCKED: 22
- primary correction: `S-14 SM2-18 primary + SM2-25 secondary`
- separated generators: `SM2-26 S-03`, `SM2-27 W-04`, `SM2-31 W-03/S-15`, `S-05 decision request`, `S-13 SM2-10/11`, `S-10 SM2-33`, `S-12 decision request`
- unresolved decision requests: S-05, S-12, S-15 COMMON_TYPES boundary, S-18 exact generator
- excluded evidence: S-17 variation, importance, COMMON_TYPES, catalog frequency
- evidence weakness: no pNN, bindata-only images, answer_key null
- disposition: advisory diagnostic revision only; canonical append prohibited

## 13. EXTRACTION_LOG draft

> canonical append가 아닌 revision 엔트리 초안이다.

- method: transcript-first staged `10 + 10 + 2`, author v1, independent audit/critique, bounded revision 1
- item gate target: exact W-01..W-04,S-01..S-18
- type gate target: 12 rows, exact exclusive cover, with 9 semantic rows + 2 BLOCKED bookkeeping umbrellas + 1 S-17 BLOCKED bucket
- content integrity: ASCII question mark 0, U+FFFD 0, prohibited control characters 0 expected
- counts: assigned 21 / item BLOCKED 1 / formal no-pNN BLOCKED 22 / irreversible IDs 0
- COMMON_TYPES: C-05 insufficient, C-09 supported with S-15 boundary evidence
- canonical changes: none
- next: separate-context auditor and critic recheck; author has no further work after PASS

## 14. evidence gaps and conclusion

1. no pNN blocks formal page citation for all 22 items.
2. answer_key: null blocks official answer validation.
3. S-17 undefined f blocks assignment, Tier, reusable grouping, importance, and generation.
4. S-15 bindata is not page evidence.
5. S-18 exact reusable invariant remains a decision request; SM2-13 is not claimed.
6. U10/U11 are bookkeeping artifacts caused by the 12-row ceiling, not reusable type proposals.
7. Runtime identity inside this artifact is self-report; gatekeeper must pair it with host-authenticated lane evidence.

Conclusion: **substantive diagnostic revision complete; formal proposal BLOCKED; independent re-audit and re-critique required**.

## 15. deterministic schema/identifier check output

Validation command:

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
observed=W-01,S-02,W-02,S-06,W-03,S-15,W-04,S-03,S-01,S-04,S-05,S-08,S-09,S-11,S-16,S-07,S-10,S-12,S-13,S-14,S-18,S-17
duplicate=[]
missing=[]
extra=[]
warnings=0
failures=0
experiment-gate: PASS phase=author
```

Targeted content-integrity and diff checks:

```text
files=3 ascii_question_mark_count=0 replacement_character_count=0 prohibited_control_count=0
git_diff_check=PASS exit=0
```
