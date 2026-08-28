# Exam Forecast Procedure (Canonical)

> The type catalogs (`catalog/*.md`) answer **"which types exist."**
> This document defines the procedure for extracting **"what will appear on THIS round"**
> (e.g., 2026 semester-2 midterm) by combining past papers and the companion workbook.
>
> Related: [`../CLAUDE.md`](../CLAUDE.md) principles 6–7 · [`TYPE_CATALOG.md`](TYPE_CATALOG.md) ·
> [`EXTRACTION_LOG.md`](EXTRACTION_LOG.md) · [`REV_GUIDE.md`](REV_GUIDE.md) §1·§3·§6 ·
> [`../docs/DATA_STANDARD.md`](../docs/DATA_STANDARD.md) §2 (file naming)

## 0. Pipeline & actors (260825)

```
[1 scope-fix]──▶[2 grading A~E]──▶[3 report]──▶[4 review]──▶[5 handoff]   ⟲ post-scoring loop
   forecast-writer authors ──▶ differential review ──▶ item-writer consumes grades
```

| Stage | Actor | Governance |
|---|---|---|
| Authoring (stages 1–3) | `forecast-writer` | proposal-class artifact under `analysis/forecast/` |
| Review — scope CONFIRMED (notice-based) | `forecast-reviewer`, one pass | light tier-1 gate |
| Review — scope UNCONFIRMED (⚠️ pattern-inferred) | `forecast-reviewer` ⇄ `forecast-auditor`, ≤5 rounds | full loop; unresolved disputes escalate to `forecast-arbiter` |
| Handoff (stage 5) | Codex/OMX coordinator | grades feed item-writer distribution |

- These four are **dedicated forecast-chain sub-agents** — separate instances from the
  `rev-*` chain; one file is never written by two agents.
- Protocol mechanics (handoff ledger `_index.md`, round rules, decision request package)
  inherit REV_GUIDE §1·§3·§6. Each forecast agent definition adds only its
  forecast-specific checklist on top.
- Every agent return opens with a progress map of the pipeline above (REV_GUIDE §3 rule 5).

## 1. Data grades — evidence does not carry equal weight

| Grade | Source | Catalog status wording | What you may claim |
|:---:|------|------------------|----------------|
| **Primary** | This school's **past papers** (exam scans) | `verified` | **it was actually tested** |
| **Secondary** | This school's **companion workbook / drill prints** | `verified(workbook)` | the school **drilled it**; tested-or-not unknown |
| **Tertiary** | Curriculum · achievement standards · other schools' material | `demonstration` | scope-judgment aid only |

**Rule: primary outranks secondary.** On conflict, follow the past paper.
Types found only in the workbook are described as **"drilled"**, never "will be tested".
A term with zero primary sources gets reliability stated explicitly as **"unmeasured"**.

## 2. Round-scope determination — first, and most important

A wrong scope invalidates even a perfect type analysis. Attempt in order:

1. **School notice · pacing schedule · exam briefing wins if present.** Ask the user for it.
2. Otherwise infer from **the same school's historical split pattern**.
   - **Measured (2026 S1 Common Math 1):** midterm = **Polynomials (unit I) entire +
     front part of Equations & Inequalities (II)** (complex numbers · quadratic equations ·
     quadratic functions) / final = II remainder + Counting (III) + Matrices (IV).
   - → **This school does NOT cut midterms at unit boundaries.** The next unit bleeds in.
     Use this as the default inference pattern for new terms.
3. When proceeding on inference, attach **⚠️ scope UNCONFIRMED — school notice pending**
   to line 1 of both the question-set frontmatter area and the forecast report.
   No definitive phrasing until confirmed.

> **Workbook coverage is NOT exam scope.** Even if the workbook covers only one unit,
> the exam can reach beyond it. Treating workbook range as exam range is this project's
> signature misjudgment.

## 3. Hit-rate measurement — when both past papers and workbook exist for the term

Running this contrast turns forecast reliability into numbers. Do it whenever possible.

| Metric | Definition | How to read |
|------|------|--------|
| **Reflect rate** | share of workbook types that actually appeared in the past paper | how much to trust the workbook |
| **Cover rate** | share of past-paper types that existed in the workbook | how far the workbook alone carries you |
| **Blindspot** | **types in the past paper with NO workbook counterpart** | **most important** — the axis workbook-only students lose wholesale |

- Record computed figures BOTH in the corresponding `analysis/forecast/` report AND in the
  subject catalog preamble.
- With no contrast source available, write **"reliability unmeasured — workbook-only evidence"**.
  Never fabricate estimates.

## 4. Per-type probability grades

Combine catalog importance (★) with data grade into a **per-round grade**. This table is
the forecast's final deliverable.

| Grade | Condition | Set reflection |
|:---:|------|--------------|
| **A near-certain** | past papers **≥2 appearances** AND workbook-drilled | mandatory, **multiple items** |
| **B likely** | 1 past appearance OR workbook ★★★ | include |
| **C possible** | workbook ★★ | include if room |
| **D peripheral** | workbook ★ single-shot | safe to omit |
| **E blindspot** | **in past papers, absent from workbook** | **mandatory** — the axis students never trained |

> Never skip grade E. It is the structural blind spot of workbook-based forecasting, and
> actual point loss happens here.

## 5. Deliverable format

Save to `analysis/forecast/<YYMMDD>_<term-code>-<subject_code>.md`
(term codes M/F/Pnn — DATA_STANDARD §4.6; e.g., `260915_2026-2M-math2.md`).

```markdown
# <Year> <Semester> <Midterm|Final> Type Forecast — <subject>
> Scope: <confirmed | ⚠️ inferred> / basis: <school notice | historical split pattern>
> Reliability: reflect __% · cover __% (or "unmeasured — workbook-only evidence")
> Sources used: <past papers> + <workbook>

## 1. Scope determination evidence
## 2. Per-type grade table (A~E)
| Type ID | Name | Grade | Evidence (rounds / workbook items) | Recommended items |
## 3. Blindspot (E) list — always its own section
## 4. Distribution advice (items per unit · Tier spread)
## 5. Open questions — confirm requested
```

**Downstream obligations (260825):** any set built FROM this forecast records in its
frontmatter `intended_use: practice|exam` and passes the solve-back pre-gate before
anyone sees it; release requires arbiter approval plus user confirmation for exam sets
(REV_GUIDE §3-b). The forecast report itself states these obligations in §4 advice.

## 6. Post-scoring — every forecast gets graded (append-only)

When new past papers arrive, **reopen the report and compare against reality.**

1. Record hit/miss per grade at the END of the report — additions only, deletions forbidden.
2. One line per missed type: why it missed (scope error / grade criterion / missing source).
3. A repeatedly failing axis triggers a **correction of §4 criteria**, logged in history.

> This loop is what makes forecasts sharpen each round. An unscored forecast accumulates nothing.

# History
- 260823 신설. 자료 등급(1~3차), 회차 범위 추정 패턴(2026 1학기 실측), 적중률 3지표,
  유형 등급 A~E, 사후 검증 루프 정의. 계기: 공통수학2가 **부교재 단독 근거**라
  신뢰도를 측정할 대조군이 없다는 점이 드러남(1학기 부교재 미확보).
- 260825 Full English rewrite (language policy); added §0 pipeline & dedicated actor chain
  (forecast-writer/reviewer/auditor/arbiter) with differential governance by scope certainty;
  filename aligned to term-code convention; downstream obligations wired (intended_use,
  pre-gate, release rule). Persona made two-layer across all judgment-side agents
  (fixed teacher/item-expert layer + variable target-cohort line).
