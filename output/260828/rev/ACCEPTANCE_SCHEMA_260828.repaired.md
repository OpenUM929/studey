# Exact acceptance schema — Math2 Sol assurance experiment

> 제안본 (`output/260828/rev/`, 감사권한자 작성). 원본 `codex-team/ACCEPTANCE_SCHEMA_260828.md`는
> 수정하지 않았다(원칙 8). 승인 시 gatekeeper가 원본에 반영한다.
> 변경 2건: (1) 훼손 문자 5개 복원 (2) §2 유형 통합 기준 개정.

## Per-item record (22 unique IDs)
`item_id | source_lines | rendered_evidence_status | assignment_or_BLOCKED | existing_type_or_decision_request | rationale | tier | tier_basis | observed_trap | confidence`

## Required aggregate sections
1. Expected/observed/duplicate/missing/extra identifier lists.
2. **Consolidation into reusable types under an exclusive exact cover of all 22 item IDs.**
   **No fixed row-count band is imposed.** Every row must be a genuine reusable type carrying at
   least two observed variation axes, **or** an explicitly labelled `BLOCKED-` bucket for a
   source-defect item. Bookkeeping umbrella rows that merge independent generators solely to meet
   a count are prohibited. If the honest type count would exceed the reviewer's expectation, that is
   reported as a finding about the corpus, not absorbed by the artifact.
3. Observed traps and source-axis-labelled importance (`★★ (기출 2회)` / `★★★ (부교재 9문항)`
   형식으로 축을 병기한다; never workbook/exam blended).
4. `COMMON_TYPES.md` comparison with reinforce/no-match disposition.
5. Catalog update disposition: existing diff, new decision request, or no-change. No irreversible ID minting.
6. Draft `HARVEST_LOG` row and `EXTRACTION_LOG` entry; never append canonicals.
7. Evidence limitations: no `pNN.png`; bindata is locatable but is not a page citation. S-17 source defect must remain explicit.
8. Method trace and exact runtime identity/model/depth; exclusive-output declaration.
9. Deterministic schema/identifier check output. Row count alone is forbidden.
10. Korean artifact language. No answer claims because `answer_key: null`.

## Escalation duty (260828 신설)
If any acceptance criterion in this document is **unsatisfiable** against the frozen source, the lane
must stop and file a decision request instead of engineering a conforming artifact. Producing a row,
label, or grouping whose only purpose is to satisfy a criterion the lane believes to be wrong is a
gate violation, even when the workaround is honestly labelled.
근거: 260828 감사 F6 — 정직한 primary generator 수가 16 이상인데 상한이 12여서 만족 불가능했고,
author는 `DIAG-U10`·`DIAG-U11` 우산 행으로 우회했다.

## Verdict constraint
Formal proposer readiness is BLOCKED while page rendering is absent. The experiment may still produce a substantive diagnostic analysis and compare it with the already-submitted diagnostic Opus artifact, but it must not claim a formal proposal, external-role approval, canonical update, or release decision.

## 동반 갱신 목록 (원칙 10)
§2를 위 문안으로 개정하면 **다음 두 곳을 같은 작업에서 고쳐야 한다.**

- `check_experiment.py:143` — `if not 5 <= len(rows) <= 12:` 를 제거하거나 상한을 없앤다.
  이 줄을 그대로 두면 개정된 기준을 만족하는 16행 `types.tsv`가 게이트에서 FAIL한다.
- `TEAM_PREFLIGHT_260828.md` — 수용기준을 인용하는 문장이 있으면 함께 갱신한다.
