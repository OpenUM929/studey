# External Opus evaluation relay template — Codex assurance team

Use this template only after the gatekeeper verdict is `READY-FOR-EXTERNAL-EVALUATION`. Replace every bracketed value with freshly measured values; if a value is unavailable, write `⚠️미확인` and request a blocked verdict rather than guessing.

```text
[CC 회람] <YYMMDD_NN> — Codex assurance-team advisory evaluation
<target> Evaluate the ready advisory bundle at <bundle root>: frozen input <input_snapshot path, hash/count>; author draft <path>; independent evidence audit <path>; independent adversarial review <path>; gate report <path>. Scope: <exact corpus/item count/schema>. This is a Codex team result, not an external Opus-role decision.
<touched> Codex/OMX created or modified this round: <measured path list>. No canonical catalog, ledger, corpus, official verify log, ruling, or release artifact was changed.
<executor> <external Claude Code Opus role> (external Claude Code CLI / Opus; source instruction: <path>). Rationale: <one line from the inspected role definition>. One main session only; no subagents, background agents, parallel dispatch, or automatic retry.
<requests> 1) Verdict: accept-as-advisory | revise | blocked. 2) Independently recheck the frozen evidence before relying on the Codex reports. 3) For every material Codex claim/finding, state agree | disagree | missed-defect with source evidence. 4) Score the author, audit, critic, and gate artifacts separately for evidence fidelity, defect detection, schema completeness, and governance compliance. 5) List every critical defect and whether the team structure caught it. 6) State whether the package is useful advisory input only; do not issue an Opus-replacement or release approval.
<reply> Create one Korean evaluation report at <bundle root>/external/<YYMMDD_NN>_opus_evaluation.md. Include frontmatter status (complete | partial | blocked), input-hash verification, independent-check order, per-artifact scorecard, material-claim cross-judgment, critical-defect register, bounded recommendation, and `NEXT:`. Do not modify any Codex team artifact.
<constraints> Advisory evaluation only. Do not modify canonicals, catalogs, ledgers, corpus, official verify logs, rulings, release state, or Codex team artifacts; do not commit. Verify rather than trust. Do not fabricate citations, IDs, claims, counts, or equivalence. Stop at the declared usage threshold and leave a precise resume point; no automatic continuation.
```

## Opus evaluation acceptance check

Codex/OMX may read the return only when the report exists at the declared path and includes all six requested evaluation elements. The return remains advisory unless the normal external operational workflow separately grants authority.
