---
artifact_kind: external_opus_codex_assurance_evaluation_request
status: pending
date: 2026-08-28
requested_by: Codex/OMX coordinator
scope: non-canonical advisory capability evaluation
---

# External Opus evaluation — Codex/OMX assurance and type-proposer-role support

## Purpose and boundary

Evaluate whether the **actual Codex-only advisory output** provides satisfactory support for the work normally expected from the external Opus `type-proposer` role. This is a capability and process evaluation, not a formal type proposal, approval, catalog ruling, or authorization to change canonical files.

Do not equate the documented Codex assurance-team design with actual team execution. The evaluated run was **solo** because the available runtime had no supported team session. No subagent output may be credited as executed unless it exists among the frozen artifacts.

This evaluation must not declare Codex/OMX, Sol, a solo run, or a future team a replacement for external Opus. It may identify narrowly bounded support work that is promising only as shadow-mode evidence.

## Evidence to read in this order

1. External-role contract: `.claude/agents/type-proposer.md`
2. Codex comparison-audit request: `output/260827/benchmark/type-proposer-cycle0/comparison/260827_01_codex_only_comparison_request.md`
3. Frozen inputs manifest (33 files): `output/260827/benchmark/type-proposer-cycle0/comparison/INPUT_MANIFEST_260827.tsv`
4. Frozen Codex-artifacts manifest (49 files): `output/260827/benchmark/type-proposer-cycle0/comparison/CODEX_ARTIFACT_MANIFEST_260827.tsv`
5. Codex advisory artifacts: `output/260827/benchmark/type-proposer-cycle0/codex-only/`
6. Your completed evidence audit: `output/260827/benchmark/type-proposer-cycle0/opus/OPUS_COMPARISON_EVALUATION_260827.md`
7. Codex staffing/assurance policy: `AGENTS.md` sections “Team staffing preflight and model assignment” and “Sol-to-Opus substitution evaluation”.

Known state: the previous Opus audit found C1–C8 and rated the track `revise-required` / `not-ready`. Those corrections are **not applied** in this request. Assess the current state honestly; do not ask the coordinator to silently repair artifacts during this evaluation.

## Required evaluation questions

Answer each with `satisfactory | partially-satisfactory | unsatisfactory | blocked`, evidence, and a narrowly scoped reason.

1. **Evidence discipline:** Does the Codex output preserve traceability, fail-closed handling, and non-invention expected of support work for the Opus type-proposer role?
2. **Analytical completeness:** Does the actual output meet the Opus type-proposer contract for item coverage, type consolidation, variation axes, catalog-draft readiness, and scope/prefix application?
3. **Assurance quality:** Separately assess (a) the actual solo execution and (b) the documented future team design. State clearly that planned agents/models/personas are not executed evidence.
4. **Operational safety:** Did the run protect canonical files, respect external-role boundaries, and report runtime/team limitations without fabrication?
5. **User-facing satisfaction:** Given the user's request for a strong team to compensate for any gap versus Opus, is the current result satisfactory as (a) an advisory evidence index, (b) a type-proposer deliverable, and (c) a benchmark candidate?
6. **Permitted shadow scope:** Identify only the support activities Codex/OMX may perform in future shadow mode without being presented as a substitute for Opus. Mark every role decision, formal proposal, review convergence, ruling, and release gate as external-Opus-authoritative unless policy explicitly changes.

## Required overall conclusion

Choose exactly one:

- `not-satisfactory — remediation required before any comparison`
- `partially-satisfactory — advisory-only, not comparable to Opus role output`
- `satisfactory-for-defined-shadow-scope — not a role substitution`
- `blocked — evidence cannot support a conclusion`

A conclusion that implies “Opus replacement,” “Opus-equivalent,” or “team execution occurred” is invalid.

## Reply format

Write only the reply file below, using frontmatter:

```yaml
artifact_kind: external_opus_codex_assurance_evaluation
status: satisfactory | partially-satisfactory | unsatisfactory | blocked
date: 2026-08-28
executor: external Claude Code Opus
scope: non-canonical advisory capability evaluation
canonical_changes: none
```

Then include:

1. a one-paragraph scope and actual-vs-planned-team declaration;
2. a six-question verdict table: `question | verdict | direct evidence | limitation`;
3. a three-row satisfaction table for advisory evidence index / type-proposer deliverable / benchmark candidate;
4. a permitted-shadow-scope table: `activity | allowed as Codex shadow work? | why | Opus authority retained`;
5. only necessary remediation requests as `- [ ]` checkboxes; and
6. an explicit no-canonical-changes and no-commit declaration.

Reply path:

`output/260827/benchmark/type-proposer-cycle0/opus/OPUS_CODEX_ASSURANCE_EVALUATION_260828.md`

## Constraints

- Use **one Opus main session only**.
- Do not invoke subagents, background agents, parallel tasks, automatic continuation, or automatic retry.
- Read and evaluate only; write exactly the reply file above.
- Do not modify catalog files, ledgers, corpus files, WIP, review logs, existing output artifacts, tool code, manifests, or commits.
- Do not score this as a blind benchmark and do not treat the previous audit report as an independent Opus type-proposer output.
