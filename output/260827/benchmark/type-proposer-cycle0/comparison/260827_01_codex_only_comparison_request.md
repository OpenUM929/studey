---
artifact_kind: external_opus_comparison_evaluation_request
status: pending_external_review
date: 2026-08-27
requested_by: Codex/OMX coordinator
scope: non-canonical advisory benchmark
---

# Codex-only advisory track — external Opus comparison evaluation request

## Boundary

This is an evidence audit of a Codex-only advisory analysis, not a formal catalog proposal, a three-tier ruling, or an authorization to alter canonical files. No catalog, ledger, corpus, WIP, review ledger, or source file may be changed. The external reviewer may write only the reply file named below.

## Frozen evidence

- Corpus units: 11
- Total items from meta.yml: 315
- Frozen corpus-input files: 33 (	ranscript.md, meta.yml, erify_log.tsv for each unit)
- Input hashes: output/260827/benchmark/type-proposer-cycle0/comparison/INPUT_MANIFEST_260827.tsv
- Codex advisory artifact files: 49
- Artifact hashes: output/260827/benchmark/type-proposer-cycle0/comparison/CODEX_ARTIFACT_MANIFEST_260827.tsv
- Historical failed parallel Opus dispatch is incident evidence only: output/260827/benchmark/type-proposer-cycle0/opus/OPUS_EXECUTION_REPORT_260827.md

## Codex artifact coverage map

| corpus | meta items | advisory files | path |
|---|---:|---:|---|
| EX-science-20252M | 29 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-science-20252M/ |
| EX-english-20252M | 32 | 5 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-english-20252M/ |
| EX-info-20252M | 25 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-info-20252M/ |
| EX-math2-20252M | 22 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-math2-20252M/ |
| EX-social-20252M | 25 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-social-20252M/ |
| EX-history-20252M | 29 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-history-20252M/ |
| EX-korean-20252F | 31 | 5 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-korean-20252F/ |
| EX-english-20252F | 33 | 5 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-english-20252F/ |
| EX-science-20252F | 33 | 5 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-science-20252F/ |
| EX-social-20252F | 27 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-social-20252F/ |
| EX-history-20252F | 29 | 4 | output/260827/benchmark/type-proposer-cycle0/codex-only/EX-history-20252F/ |

## Required audit method — quota-safe

1. Work in **one main Opus session only**. Do not invoke subagents, background agents, parallel tasks, automatic continuation, or automatic retry.
2. Verify the two manifests before opening analytical artifacts. If a hash differs, stop and write locked with the exact path.
3. Read CLAUDE.md, nalysis/REV_GUIDE.md §2-b C and §6-b, nalysis/catalog/_README.md, nalysis/catalog/CODE_REGISTRY.md, and the relevant subject catalog(s).
4. Independently audit the reserved representative EX-science-20252M in three bounded slices (items 1–10, 11–20, 21–29). For each slice, first inspect the corpus inputs, then inspect the corresponding Codex artifact. Do not infer page evidence where no rendered page exists.
5. For the other 10 units, perform manifest/count coverage verification and a deterministic spot audit of the first item in lexical corpus-ID order: EX-english-20252F item 1 and EX-social-20252F item 1. This is sampling, not full re-analysis; state the limitation.
6. Evaluate only traceability, evidence-gap handling, scope-guard handling, existing-type match discipline, and whether the advisory boundary was preserved. Do not assert answers, invent IDs, or promote status.

## Open questions

1. **Input integrity:** Are all reviewed Codex claims tied to the frozen inputs, and are any manifest/hash/count discrepancies present? Verdict: pass | revise-required | blocked.
2. **Representative quality:** For EX-science-20252M items 1–29, are the assignments/HOLD decisions traceable and appropriately bounded by the available evidence? Verdict: pass | revise-required | blocked.
3. **Cross-unit safeguard:** Do the two deterministic spot audits and the 11-unit coverage map support the claim that this is a complete *advisory coverage track*, without treating it as a canonical type-proposer output? Verdict: pass | revise-required | blocked.
4. **Comparison readiness:** Is this track suitable as one side of a future Codex-vs-Opus benchmark, with no claim that Sol or a solo run replaces Opus? Verdict: 
eady | not-ready | blocked.

## Reply format and path

Write exactly one Korean Markdown file:
output/260827/benchmark/type-proposer-cycle0/opus/OPUS_COMPARISON_EVALUATION_260827.md

Use frontmatter with artifact_kind: external_opus_comparison_evaluation, status: pass|revise-required|blocked, and executor: external Claude Code Opus. Include: (a) manifest verification table, (b) three representative slice findings, (c) two spot-audit findings, (d) a four-question verdict table, (e) binding corrections as - [ ] only when needed, (f) explicit sampling and evidence limitations, (g) a final no canonical changes made statement. Do not append to analysis/REV_LOG.md; this is an isolated benchmark evaluation, not a formal review round.
o canonical changes made statement. Do not append to nalysis/REV_LOG.md; this is an isolated benchmark evaluation, not a formal review round.
