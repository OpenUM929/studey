# 260828_05 Guidance and role remediation plan

## Purpose

Prevent a repeat of the failed Codex-only comparison: a solo or planned team was
reported as if it were an executed independent team, and a duplicate row masked a
missing assessment item.

## In-scope files and owners

| Surface | Owner for this remediation | Change |
|---|---|---|
| `AGENTS.md` | Codex/OMX coordinator | Runtime proof, pilot sizing, deterministic item-ID gates, and external relay stop rules. |
| `docs/CODEX_TEAM_ASSURANCE_GUIDE.md` | Codex/OMX coordinator | Executed-lane evidence contract and type-analysis acceptance schema. |
| `docs/OPUS_ASSURANCE_TEAM.md` | Codex/OMX coordinator | Align model/depth claims with runtime proof and enforce independence ordering. |
| `.codex/agents/assessment-*.toml` | Codex/OMX coordinator | Bounded roles, exclusive outputs, and machine-checkable result fields. |
| `.claude/agents/type-proposer.md` | Codex/OMX coordinator (external role definition only) | Fail-closed evidence, unique item-ID coverage, and complete proposal schema. |
| `tools/check_assurance_contract.py` | Codex/OMX coordinator | Regression/static conformance check for the above safeguards. |

## Locked behaviour (regression requirements)

1. No `actual-team` result is valid without per-lane runtime identity, independent
   context proof, exclusive output path, and produced artifact path.
2. The configured/observed model and reasoning depth must be recorded exactly;
   unsupported depth labels are blocked rather than inferred.
3. Coverage is an equality test of expected versus observed item identifiers. Row
   counts alone cannot pass; duplicates and missing identifiers are fatal.
4. A type-analysis proposal has assignment, consolidation, axes, observed traps,
   source-labelled importance, common-type comparison, catalog-diff disposition,
   and HARVEST/EXTRACTION drafts. Missing fields block readiness.
5. Missing rendered/source evidence makes affected items `BLOCKED`; it cannot be
   converted into a claimed complete proposal or a fabricated page citation.
6. An Opus comparison relay is one session and one measured pilot slice only; it
   cannot start before the local gate has produced all required artifacts.

## Validation

Run `python tools/check_assurance_contract.py`. It must report zero failures.
Then parse all four TOML role files with Python `tomllib` and inspect the diff
limited to the six surfaces above. No canonical catalog, ledger, corpus, or
historical audit artifact is changed by this remediation.

## Stop/resume

Stop after the static gate passes. The next operational step is a new frozen,
single Math2 pilot only after actual independent-team runtime availability is
proven; otherwise it remains `▲ blocked`.
