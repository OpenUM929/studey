---
artifact_kind: codex_team_assurance_preflight
status: blocked
date: 2026-08-27
target: bounded advisory type-proposal experiment
---

# Highest-depth Codex team preflight

## Intended actual staffing

| lane | model | reasoning | instruction | exclusive write surface |
| --- | --- | --- | --- | --- |
| author | Sol (`gpt-5.6-sol`) | xhigh | `.codex/agents/assessment-author-sol.toml` | `codex-team/author/` |
| evidence-auditor | Sol (`gpt-5.6-sol`) | xhigh | `.codex/agents/assessment-evidence-auditor-sol.toml` | `codex-team/audit/` |
| adversarial-critic | Sol (`gpt-5.6-sol`) | xhigh | `.codex/agents/assessment-adversarial-critic-sol.toml` | `codex-team/critic/` |
| gatekeeper | Sol (`gpt-5.6-sol`) | xhigh | `.codex/agents/assessment-gatekeeper-sol.toml` | `codex-team/gate/` |

## Hard-start checks

| condition | evidence | result |
| --- | --- | --- |
| actual independent lanes can run | `TMUX` is empty | blocked |
| OMX Team runtime prerequisite | `tmux -V` cannot resolve the command | blocked |
| OMX installation | `omx --version` = `oh-my-codex v0.20.5` | pass |
| existing Team state can resume | no `.omx/state/team/` directory | no active team |
| external Opus evidence is preserved | `opus/OPUS_EXECUTION_REPORT_260827.md` exists | pass |

## Verdict

`BLOCKED — no actual independent Codex team runtime in this session.`

This is not a team result. It creates no solo Sol substitute, simulated review, or comparison result, and it does not restart external Opus work.

## Resume gate

1. tmux is installed and the leader runs OMX CLI inside tmux.
2. A small user-approved slice, frozen manifest/hash, and exact result schema exist.
3. The four Sol lanes above run in separate contexts and exclusive output paths.
4. Only after the gatekeeper returns `READY-FOR-EXTERNAL-EVALUATION` may external Opus receive one session, one slice, no parallel dispatch, and no automatic retry.
