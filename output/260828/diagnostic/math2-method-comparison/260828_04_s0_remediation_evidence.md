# S0 전사 복구 증거 — EX-math2-20252M (260828)

- Pipeline: `[1 refine] -> [2 propose] -> [3 review] -> [4 arbiter] -> [5 apply]`; this work is **S1 REFINE remediation only**, not a formal proposal.
- Stage: `S0 partial-pass / formal-proposal blocked`.
- Team: `mode=solo`; `corpus-refine = Codex/OMX Sol` (persona: factual-transcription owner; no type, tier, answer, or catalog judgment); source instruction: `.claude/agents/type-extractor.md`.
- Authority: `output/260826/260826_01_operations_cycle_prd.md` S1; canonical change surface restricted to this corpus unit and its append-only `verify_log.tsv`.

## 1. Trigger and root cause

The external diagnostic reply `opus/OPUS_MATH2_PERSONA_ROLE_METHOD_EVALUATION_260828.md` found S-15 and S-17 transcription gaps. Local re-check established a broader S1 gate failure: the prior transcript and ledger claimed `corpus/_images/EX-math2-20252M/bindata` existed, but the directory did not exist.

This was not treated as a type-analysis defect. The source HWP was read again through `hwp5proc`; no catalog, ledger outside the corpus unit, proposal, or answer claim was modified.

## 2. Bounded slice and applied factual corrections

Slice: one five-page subject unit (`EX-math2-20252M`), within the type-extractor limit of one subject unit / <=10 pages.

1. Restored three embedded source streams into `corpus/EX-math2-20252M/_images/bindata/`: `BIN0001.jpg`, `BIN0002.bmp`, `BIN0003.jpg`.
2. Recovered S-15's five `<보기>` expressions from source `ViewText/Section1` EQED sequence numbers 1384, 1386, 1392, 1394, 1400; added the existing `BIN0002.bmp` marker and only factual diagram description.
3. Checked S-17 source EQED records: sequence 1668 contains `f(a)` and 1672 contains `f(k)`; no defining equation for `f` occurs in the item record chain. Added an explicit `[unreadable: source defect]` marker and append-only ledger row. No value was inferred.
4. Corrected `meta.yml` `answer_key` to `null`: the shared answer PDF exists under `origin_data/2025_2학기_1학년_중간/`, but is not an `answers.*` file in this corpus unit, as required by `docs/DATA_STANDARD.md` 5.7.

## 3. Validation evidence

| Check | Expected | Result |
|---|---:|---:|
| restored source-image SHA-256 | 3/3 match | 3/3 match; mismatch 0 |
| S-15 choice expressions | 5 | 5 |
| S-15 BIN0002 marker | 1 | 1 |
| S-17 explicit source-defect marker | true | true |
| `answer_key` semantic validity | `null` | `null` |
| appended verify-log rows | 4 | 4 (prior 3 rows preserved) |
| unreadable ledger row | >=1 | 1 |
| `git diff --check -- corpus/EX-math2-20252M` | exit 0 | exit 0 |

## 4. Remaining blockers and invalidation boundary

- **B remains blocked:** no `pNN.png` rendering exists for this HWP corpus unit, and `analysis/catalog/_README.md` was not part of the prior frozen diagnostic input.
- **C remains blocked:** the shared answer PDF must be explicitly frozen for a later answer-comparison operation; this remediation does not use it.
- **D remains blocked:** the ten type-boundary disagreements require external `rev-arbiter` judgment. They are not resolved by transcription.
- The prior 260828 diagnostic and Opus reply are immutable evidence of the earlier frozen input. This corrected corpus changes the input state; any renewed diagnostic or formal proposal must create a new manifest and must not overwrite those artifacts.

## 5. Stop condition

No formal `type_analysis`, `catalog_update`, type ID, star, answer, cluster decision, or canonical catalog mutation has been produced here. Proceed only through a newly frozen input set and the required external role gates.