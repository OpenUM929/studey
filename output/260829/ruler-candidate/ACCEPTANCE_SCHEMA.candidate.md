---
artifact: ruler-candidate
stage: S1
status: candidate-only
grade: advisory
freeze_authority: none
observed_model_depth: unavailable
---

# Math2 assessment-analysis acceptance schema — S1 candidate

This candidate is not approved, frozen, or suitable for a measured run.  A different identity and
fresh context must qualify it in S2; an audit authority plus the user's second key must refreeze it
in S3 before any S4 consumer uses it.

## 1. Per-item record

Every expected item identifier occurs exactly once in this order:

`item_id | source_lines | rendered_evidence_status | assignment_or_BLOCKED | existing_type_or_decision_request | rationale | tier | tier_basis | observed_trap | confidence | generator_id`

`generator_id` is a structured primary-generator equivalence label supported by the frozen source
and cited catalog evidence.  It is not a free row-count control.  A source-defect item uses a
`BLOCKED-` generator identifier and remains excluded from reuse metrics.

## 2. Type partition and maximality

The type table uses exactly these columns:

`group_id | member_item_ids | type_disposition | variation_axis_1 | variation_axis_2 | observed_trap | importance_source_axis | common_types_disposition | catalog_disposition | generator_id | row_kind`

Rules:

1. `row_kind` is one of `reusable`, `singleton`, or `blocked`.
2. Every item belongs to exactly one primary row; duplicate, missing, and extra identifiers fail.
3. Rows are the maximal equivalence classes induced by the per-item `generator_id`.  Every distinct
   item-side generator occurs in exactly one type row, and that row's members equal the full class.
   Splitting one generator across singleton rows and merging different generators into an umbrella
   row both fail.
4. `reusable` means a non-blocked equivalence class with at least two observed items and at least two
   observed variation axes.  `singleton` means a non-blocked one-item class.  `blocked` is reserved
   for a source-defect class and is excluded from the reuse numerator and denominator.
5. The primary partition is an exclusive exact cover.  Secondary relationships may be documented
   only as non-cover references and never add membership.
6. There is no lower bound, upper bound, or hard-coded expected row total.  The observed totals are
   report-only and are compared with a regeneration from item-side generator identifiers.
7. Bookkeeping umbrella rows are prohibited even when honestly labelled.

The reference expansion of the frozen 260828 evidence is report-only:
`rows=16 reusable=6 singleton=9 blocked=1 items=22 uncovered=0`.

## 3. Span ruler

The expected item table is regenerated from the frozen transcript.  Boundaries are Markdown
headings matching `^#{1,6}\s`, horizontal rules matching
`^(-{3,}|\*{3,}|_{3,})\s*$`, and EOF.  Rule `rule_a` ends an item on the line immediately before
the next boundary.  No item-specific line correction is permitted.

## 4. Content and evidence integrity

The gate checks schema equality, identifier equality, source-span equality, blank required fields,
replacement characters, unexplained question-mark corruption, control characters, S-17 BLOCKED
status, report markers, report content integrity, candidate-schema markers, and generated-ruler
equality.  Report presence alone is insufficient.

Required aggregate report markers are: expected identifiers, observed identifiers, duplicate
identifiers, missing identifiers, extra identifiers, COMMON_TYPES, HARVEST_LOG draft,
EXTRACTION_LOG draft, runtime identity, no pNN, and answer_key: null.

## 5. Warning and verdict contract

The checker collects warning strings in a list, prints `warnings=<computed count>` before its final
PASS or FAIL marker, prints every warning, and returns nonzero when either warnings or failures are
nonempty.  Success requires exit zero, a computed warning count of zero, a computed failure count of
zero, and `experiment-gate: PASS`.

## 6. Escalation and authority

If a frozen-source criterion is unsatisfiable, the implementer files a decision request instead of
changing the source, seed set, threshold, expected table, or evidence boundary to obtain a pass.
This S1 implementer cannot qualify, refreeze, approve, release, benchmark, or consume this candidate.

## history

- 260829 — S1 candidate created from 260829_02 execution instruction.  Fixed row-count bounds are
  removed; generator maximality, horizontal-rule span boundaries, computed warnings, report/schema
  integrity, and differential self-test obligations are specified.  No freeze or approval granted.
