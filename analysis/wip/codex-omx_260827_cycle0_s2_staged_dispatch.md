# Codex/OMX WIP — Cycle 0 S2 staged dispatch

Owner: Codex/OMX coordinator (Sol)
Date: 2026-08-27
Write ownership: this file only; external type-proposer owns its separate WIP.

| timestamp (KST) | status | scope | completed evidence | NEXT |
|---|---|---|---|---|
| 2026-08-27 | prepared | 11 S1-complete 2025-2 corpus units / 315 items | Workload sizing applied: EX-science-20252M (29) reserved for isolated comparison; 10 operational units / 286 items have exact <=10-item slices, exclusive files, stop/resume, and single-session/no-parallel constraints in output/260827/260827_04_type-proposer_operational_wave.md. | User-copy the 260827_04 relay to one external Claude Code Opus main session; do not start the reserved comparison pilot until the real Codex team runtime start gate passes. |
| 2026-08-27 | blocked | Codex assurance team pilot | $TMUX empty; tmux absent; no .omx/state/team. No independent Codex lane was dispatched or simulated. | Re-run the pilot start gate in a real supported team runtime; preserve the frozen SHA-256 or re-freeze. |

| 2026-08-27 | in_progress | Codex-only advisory representative / EX-science-20252M / 29 items | Three <=10-item slices completed under output/260827/benchmark/type-proposer-cycle0/codex-only/EX-science-20252M/; 29/29 coverage, 2 conditional existing matches, 27 explicit holds, 0 IDs or canonical/ledger applications. | Start the 10 operational units (286 items / 34 <=10-item slices) only as the same Codex-only advisory track; preserve all external-only authority boundaries. |

- Codex-only advisory operations / EX-english-20252M / 32 items: selected 1-27 in three bounded slices (10/10/7), written 1-5 in one 5-item slice. Completed 32/32 coverage; all existing-type mappings conditional pending English course-scope decision; 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-english-20252M/`.

- Codex-only advisory operations / EX-info-20252M / 25 items: selected 1-18 in two bounded slices (10/8), short-answer 1-7 in one 7-item slice. Completed 25/25 coverage; all rows HOLD because `info → IN` is only a provisional §3 mapping and the required information catalog/range-guard onboarding remains incomplete; 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-info-20252M/`.

- Codex-only advisory operations / EX-math2-20252M / 22 items: written 1-4 in one 4-item slice and short-answer 1-18 in two bounded slices (10/8). Completed 22/22 coverage; 19 conditional existing mappings, 3 HOLD rows, including short 17 BLOCKED by the unresolved transcription span `(나)`/`f(k)`; 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-math2-20252M/`.

- Codex-only advisory operations / EX-social-20252M / 25 items: selected 1-20 in two bounded slices (10/10), written 1-5 in one 5-item slice. Completed 25/25 coverage; 23 conditional existing mappings and 2 HOLD rows (selection 19, written 5 lack an explicit existing content axis; all mapping is conditional pending 통합사회2 scope guard); 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-social-20252M/`.

- Codex-only advisory operations / EX-history-20252M / 29 items: selected 1-20 in two bounded slices (10/10), short-answer 1-6 and written 1-3 in one 9-item slice. Completed 29/29 coverage; all 29 rows HOLD because the source is 한국사2 while the canonical catalog is 한국사1, no 한국사2 range guard exists, and E-6 세부 유형화 remains deferred; 0 new IDs, catalog edits, ledger rows, answer claims, or grading-criteria proposals. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-history-20252M/`.

- Codex-only advisory operations / EX-korean-20252F / 31 items: selected 1-25 and short-answer 1-6 in four bounded slices (8/10/10/3). Completed 31/31 coverage; 28 conditional existing mappings and 3 HOLD rows (selected 24–25 and short-answer 6 require an approved media-type structure; all mappings remain conditional pending 공통국어2 scope guard); 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-korean-20252F/`.
- Codex-only advisory operations / EX-english-20252F / 33 items: selected 1-28 and written 1-5 in four bounded slices (10/10/8/5). Completed 33/33 coverage; 33 conditional existing mappings pending 공통영어2 scope compatibility; 0 HOLD rows, new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-english-20252F/`.

- Codex-only advisory operations / EX-science-20252F / 33 items: selected 1-24 and short-answer 1-9 in four bounded slices (10/10/10/3). Completed 33/33 coverage; 6 conditional existing mappings (BI-02 ×1, ER-05 ×1, ER-06 ×3, GT-04 ×1) pending 통합과학2 semantic and scope compatibility, and 27 HOLD rows (5 BLOCKED by bindata-only graphs/tables or conversion blanks); 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-science-20252F/`.

- Codex-only advisory operations / EX-social-20252F / 27 items: selected 1-22 and short-answer 1-5 in three bounded slices (10/10/7). Completed 27/27 coverage; 19 conditional F/D mappings pending 통합사회2 scope compatibility and 8 HOLD rows for population, migration, resource, and energy content lacking an approved axis; 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-social-20252F/`.

- Codex-only advisory operations / EX-history-20252F / 29 items: selected 1-23 and short-answer 1-6 in three bounded slices (10/10/9). Completed 29/29 coverage; all 29 rows HOLD because the source is 한국사2 while the canonical catalog is 한국사1 and no 한국사2 curriculum range guard or approved taxonomy exists; 0 new IDs, catalog edits, ledger rows, or answer claims. Evidence: `output/260827/benchmark/type-proposer-cycle0/codex-only/EX-history-20252F/`.
