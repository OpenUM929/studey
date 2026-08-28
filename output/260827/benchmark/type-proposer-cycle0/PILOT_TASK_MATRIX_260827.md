# Comparison pilot task matrix — EX-science-20252M

Created by: Codex/OMX coordinator (Sol)
Date: 2026-08-27
Status: BLOCKED — actual Codex team runtime is unavailable in this session
Purpose: reserve one representative corpus for a genuine, isolated **Codex assurance team vs external Opus** comparison. This is not an Opus-replacement claim.

## Why this unit is reserved

- ID: `EX-science-20252M`
- Measured input: 29 items, 316 transcript lines, 32,682 bytes across transcript/meta/verify-log; transcript SHA-256 `ae49901e3b1c6f491552da427b421fe7e36ce05d352ee5539cd2971179c27c14`; existing verification rows: 3.
- It is excluded from the 10-unit operational wave, keeping both actors on exactly the same frozen input and preventing cross-write interference.
- Task slices: `1-10`, `11-20`, `21-29`. No worker receives more than ten item assignments in a slice.

## Staffing preflight

| lane | model / depth | inspected instruction | exclusive output surface | product-write authority |
|---|---|---|---|---|
| author | Sol / xhigh | `.codex/agents/assessment-author-sol.toml` | `.../codex-team/author/` | none |
| evidence auditor | Sol / xhigh | `.codex/agents/assessment-evidence-auditor-sol.toml` | `.../codex-team/evidence-audit/` | none |
| adversarial critic | Sol / xhigh | `.codex/agents/assessment-adversarial-critic-sol.toml` | `.../codex-team/critic/` | none |
| gatekeeper | Sol / xhigh | `.codex/agents/assessment-gatekeeper-sol.toml` | `.../codex-team/gate/` | none |
| coordinator | Sol / high | `AGENTS.md`, `docs/CODEX_TEAM_ASSURANCE_GUIDE.md` | `.../codex-team/integration/` | none |

All lanes read the frozen corpus and canonical references. No lane writes a catalog, ledger, transcript, meta file, or external result. The author completes its bounded slice outputs first; auditor and critic review those outputs in separate contexts; the gatekeeper verifies files, counts, citations, and unresolved flags. The coordinator reports evidence only.

## Start gate

Required before dispatch:

1. A real multi-agent runtime is present, with independent lanes and report return paths.
2. The four instruction paths above are re-read; each lane/model/depth and exclusive surface is recorded.
3. The frozen input hash above still matches; otherwise re-freeze both actors' inputs.
4. The full task matrix records objective, 3 slices, input paths, write prohibitions, output schema, evidence rule, validation command, budget stop, and resume point.
5. External Opus receives a separate one-main-session pilot relay with no subagents, no background/parallel work, no automatic continuation or retry.

Current evidence: `$TMUX` is empty and `tmux` is not installed; `omx --version` is `0.20.5`; `.omx/state/team/` is absent. Therefore no actual team may be represented, simulated, or compared from this session.

## Expected isolated artifacts after the gate

```text
output/260827/benchmark/type-proposer-cycle0/
  codex-team/author/EX-science-20252M_type_analysis.md
  codex-team/author/EX-science-20252M_catalog_update.md
  codex-team/evidence-audit/EX-science-20252M_evidence_audit.md
  codex-team/critic/EX-science-20252M_critic.md
  codex-team/gate/EX-science-20252M_gate.md
  opus/EX-science-20252M_type_analysis.md
  opus/EX-science-20252M_catalog_update.md
  comparison/EX-science-20252M_blind_score.md
```

The Opus historical incident record remains preserved at `opus/OPUS_EXECUTION_REPORT_260827.md`. It is evidence of the failed 11-way dispatch, not a proposal output.

## Stop condition

Stop and retain only checkpoints if a runtime/budget/integrity/citation gate fails. No scoring, equivalence inference, catalog update, or operational approval occurs until both independently produced artifact sets exist and the blind-score checklist is complete.
