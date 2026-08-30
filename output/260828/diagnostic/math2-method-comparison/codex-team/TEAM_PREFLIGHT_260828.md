# Actual-team preflight ? EX-math2-20252M Sol rerun

## Authorization and objective
- User authorization: rerun the failed Codex/Sol work, compare it with the submitted Opus result, create a result report, then prepare a package for a new external Opus comparison.
- Target responsibility inspected: `.claude/agents/type-proposer.md` ? subject-teacher/expert-item-writer analytical layer; proposal docs only; canonicals read-only; deterministic unique-ID gate; page evidence required.
- Comparison target: submitted Opus diagnostic `output/260828/diagnostic/math2-method-comparison/opus/OPUS_MATH2_PERSONA_ROLE_METHOD_EVALUATION_260828.md`; it is comparison-only and hidden from the author until author completion.
- Authority: advisory diagnostic only; no claim of Opus replacement/equivalence/approval.

## Frozen scope
- Corpus unit: `EX-math2-20252M`; 22 items; expected IDs: W-01..W-04 and S-01..S-18.
- Pilot: 10 items `W-01..W-04, S-01..S-06`; then measured waves `S-07..S-16` (10) and `S-17..S-18` (2) only if the pilot identifier/schema gate passes.
- Source evidence density: 152 transcript lines, 3 bindata files, no pNN render pages, answer_key null. Known defect: S-17 has no source definition for f; it must remain explicit BLOCKED/limited.
- Input delta: corpus transcript/meta/verify_log, CODE_REGISTRY, and type-proposer instruction changed after the Opus run; `_README`, FORECAST_GUIDE, bindata, assurance guide, and AGENTS are newly frozen. Therefore comparison must be labelled non-identical-input/current-state rerun.

## Staffing matrix
| lane | objective / unit | allowed inputs | exclusive output | prohibited writes | lane = model = depth | workload | validation / stop |
|---|---|---|---|---|---|---|---|
| gatekeeper | freeze/integrate 22 IDs and compare | all manifests, lane artifacts, Opus reference after author completes | `codex-team/` coordinator reports only | corpus, canonicals, ledgers, lane reports | gatekeeper = gpt-5.6-sol = high | preflight + final gate | stop on missing lane/runtime/schema/ID proof |
| author | substantive diagnostic type analysis, staged 10+10+2 | author manifest only; Opus artifact prohibited until completion | `author/` only | canonicals, corpus, ledgers, audit/critique | author = gpt-5.6-sol = high | 22 items, pilot first | pilot must have exact 10 IDs, schema fields, zero dup/missing/extra; otherwise stop |
| evidence-auditor | independent source/ID/schema audit | frozen inputs first, then author | `audit/` only | author, critic, canonicals, corpus, ledgers | evidence-auditor = gpt-5.6-sol = high | 22 items/claims | stop on source/hash mismatch; PASS/FAIL/BLOCKED per claim |
| adversarial-critic | challenge semantics/scope/student risk | frozen inputs first, then author; audit optional only after independent check | `critique/` only | author, audit, canonicals, corpus, ledgers | adversarial-critic = gpt-5.6-sol = high | 22 items + schema | block critical unsupported grouping or false readiness |

- Maximum concurrency: author alone; after author completes, auditor and critic may run concurrently because outputs are exclusive and no shared ledger is written.
- Runtime evidence required: native agent execution ID, observed model/depth, independent-context statement, artifact path, completion status.
- Validation gate: `python output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py --phase <pilot|author|final>`. It prints expected/observed/duplicate/missing/extra IDs and warning count.
- Stop/resume: author stops after pilot if gate fails; otherwise resumes at S-07. Auditor/critic start only after full author artifact exists. External relay is created only after all three lane artifacts and gate report exist; comparison limitations remain explicit.

## Hard-start result
- Inputs, item IDs, schema, write surfaces, staged units, budgets, and gates are frozen.
- Native role-routed Sol lanes are available through host-authenticated collaboration execution identities. Lane execution proof must still be captured from actual returns; planned entries are not execution evidence.

## Post-audit preflight correction
- The initial heading parser set W-04 to lines 44-51 by stopping at the next numeric heading; lines 49-51 are blank/section-header material, not part of W-04. Independent audit confirmed the supporting item text is exactly lines 44-48. The coordinator corrected only this derived range in `EXPECTED_ITEM_IDS_260828.tsv`; item identity, source content, hashes, and assignment scope did not change.
- The deterministic checker now rejects ASCII `?`, Unicode replacement characters, control-character corruption, and any S-17 row whose assignment/tier is not explicitly `BLOCKED`. The pre-revision author artifact intentionally fails this strengthened gate until the author repairs its exclusive outputs.
