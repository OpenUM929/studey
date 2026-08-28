# Codex-only provisional type analysis — EX-science-20252M, slice 1-10

> Status: in progress / advisory only. Analyst: Codex/OMX (Sol, single owner). This is not an Opus-role proposal or a release/approval artifact.

## Frozen input and integrity

- Sources read: corpus/EX-science-20252M/transcript.md lines 70-190; meta.yml; verify_log.tsv; analysis/catalog/science.md; analysis/curriculum_2022.md.
- Meta declaration: 23 selected + 6 written = 29 items (meta items: 29). This slice covers selected items 1-10 only.
- Evidence limitation: rendered pNN.png pages are absent; transcript holds bindata references only. Citations below deliberately use transcript lines (L…), not fabricated pages.
- Answer limitation: the metadata names an answer key, but it is not part of this frozen local evidence chain. No answer assertion is made.
- Scope limitation: the source calls itself 통합과학2, while the available curriculum guard explicitly distinguishes 통합과학1 and 통합과학2 (curriculum L8-9); the existing science catalog is headed 통합과학1. Any unmatched/new semantic is held for a scope-and-prefix decision.

## Per-item assignment / hold table

| item | provisional type or hold | rationale | provisional tier | transcript evidence | confidence |
|---:|---|---|---|---|---|
| 1 | HOLD-SC2-NUCLEAR-FUSION | 태양 중심 핵반응의 핵종·질량결손 비교. Existing catalog headings cover UN/CH/BI/MC/ER but no matching 핵융합 반응 type was located. | T2 | L85-94 | medium |
| 2 | ER-05 (conditional) | 태양에너지로 물의 상태 변화와 광합성-탄소 순환을 연결하는 지구계 순환 판단. Catalog ER-05 is 탄소 순환·물 순환; course-label mismatch remains. | T2 | L96-105 | medium |
| 3 | HOLD-SC2-NUCLEAR-FUSION-ENERGY | KSTAR 기사와 핵융합 연료·질량결손·플라스마 조건을 판단. Existing catalog does not expose a same-semantic type. | T2 | L107-116 | medium |
| 4 | GT-04 (conditional) | 빅데이터의 대량·다양성 성질을 판별. GT-04 covers information signal/storage, not an exact big-data definition; retain conditional match. | T1 | L118-123 | medium |
| 5 | HOLD-SC2-BIG-DATA-PREDICTION | 공공 감시와 빅데이터 예측의 속도·정확성·개인정보를 비교. GT-04 is too broad for a confirmed existing-type reuse. | T2 | L125-137 | medium |
| 6 | BI-06 (conditional) | 광합성과 산소 호흡의 물질 변화 및 스트로마톨라이트 연결 판단. BI-06 includes 물질대사 but not this exact diagram/concept combination. | T2 | L139-143 | low — diagram-dependent |
| 7 | HOLD-SC2-REDOX-HYDROGEN-IRON | 수소환원제철에서 산화·환원 및 탄소배출을 연결. Existing catalog headings show no redox-process type. | T2 | L145-154 | medium |
| 8 | HOLD-SC2-REDOX-REACTION-EQUATION | 세 반응식의 환원 물질을 고르는 구조이나 변환 텍스트가 반응식을 비워 두었다. | BLOCKED | L156-165; verify_log EQED 81건 note | low |
| 9 | HOLD-SC2-REDOX-FLAME-COPPER | 구리 산화/환원, 불꽃 구역, 질량 변화의 탐구 해석. Existing catalog headings show no exact redox-lab type. | T2 | L167-179 | medium |
| 10 | HOLD-SC2-METAL-DISPLACEMENT | Ag/Cu/Al 계의 전자 이동과 금속 반응성을 판단. 그림·화학식 일부 공란으로 보수적 hold. | T3 | L181-190 | low — diagram/formula dependent |

## Consolidation observed in this slice

- **Conditional existing reuse**: ER-05 (item 2) and GT-04 (item 4), only after curriculum/course compatibility is affirmed.
- **Candidate semantic families, not IDs**: nuclear-fusion concepts (items 1, 3); big-data prediction/privacy (5); redox process/lab/displacement (7-10); metabolism diagram (6).
- **Observed construction pattern**: most items use three-statement ㄱ·ㄴ·ㄷ combination options (L89-94, L100-105, L111-116, L118-123, L132-137, L149-154, L174-179, L185-190). This is evidence for an existing common-pattern check later, not a new common-type claim.

## Mandatory holds and next action

1. Do not mint type IDs: course scope and current science prefix applicability are unresolved.
2. Do not turn conditional matches into catalog diffs until scope compatibility is decided.
3. Item 8 needs a source-render/EQED reconstruction that can make the three reaction equations visible; this slice cannot infer them.
4. Before any difficulty/answer claim, locate the actual answer-key artifact or state that it is unavailable.

## Slice checkpoint

- Coverage: 10/10 rows; 2 conditional existing matches; 8 holds; 0 new type drafts; 0 applied changes.
- Next: write the no-application catalog-diff record for this slice, then inspect items 11-20.
