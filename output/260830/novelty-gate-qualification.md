---
lane: verifier
configured_model: gpt-5.6-sol
configured_reasoning: high
observed_model: unavailable
independence: fork_turns=none
verdict: revise-required
qualified_unit_count: 1
required_test_count: 5
required_cli_case_count: 5
frozen_inputs:
  - path: .claude/agents/item-writer.md
    bytes: 10818
    sha256: b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2
  - path: analysis/catalog/AUTHORING_GUIDE.md
    bytes: 10369
    sha256: 737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea
  - path: tools/check_novelty_ledger.py
    bytes: 7461
    sha256: 5094b5332adaa51c6a3e21656adc6846fee58293aa7a4d178f96f099e7ed222a
  - path: tests/test_check_novelty_ledger.py
    bytes: 4683
    sha256: 77bd5cae9ac13fdf45c0f007ae5da409f540e9ec4c7383681988614116bc17ae
---

# Math-item novelty gate — independent pilot qualification

## Summary

**Verdict: `revise-required`.** The frozen inputs matched, the required unit suite passed
5/5, and the required direct-CLI matrix behaved correctly in all 5/5 cases. Qualification
nevertheless fails because two additional direct-CLI probes demonstrate fail-open behavior
against explicit authoring contracts:

1. a ledger row with nine TSV fields passes although the schema is exactly eight columns;
2. a ledger whose filename/stem is unrelated to the set passes although the canonical rule
   requires the same stem and `.novelty.tsv` suffix.

No source, gate, test, documentation, catalog, candidate set, or shared ledger was modified.
No 40-item set was read or qualified.

## Frozen-input verification

Command:

```powershell
$files=@('.claude/agents/item-writer.md','analysis/catalog/AUTHORING_GUIDE.md','tools/check_novelty_ledger.py','tests/test_check_novelty_ledger.py'); foreach($f in $files){$i=Get-Item -LiteralPath $f; $h=(Get-FileHash -Algorithm SHA256 -LiteralPath $f).Hash.ToLowerInvariant(); "{0}`t{1}`t{2}" -f $f,$i.Length,$h}
```

Literal output:

```text
.claude/agents/item-writer.md	10818	b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2
analysis/catalog/AUTHORING_GUIDE.md	10369	737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea
tools/check_novelty_ledger.py	7461	5094b5332adaa51c6a3e21656adc6846fee58293aa7a4d178f96f099e7ed222a
tests/test_check_novelty_ledger.py	4683	77bd5cae9ac13fdf45c0f007ae5da409f540e9ec4c7383681988614116bc17ae
```

Result: all four byte counts and SHA-256 values exactly match the frozen request.

## Commands and literal outputs

### Required unit suite

Command:

```powershell
python -X utf8 -m unittest tests.test_check_novelty_ledger -v
```

Literal output (the final `EXIT_CODE` was emitted by the qualification wrapper):

```text
test_duplicate_id_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_duplicate_id_fails) ... ok
test_missing_id_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_missing_id_fails) ... ok
test_numeric_only_axis_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_numeric_only_axis_fails) ... ok
test_type_mismatch_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_type_mismatch_fails) ... ok
test_valid_exact_cover_passes (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_valid_exact_cover_passes) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.017s

OK
expected_ids=['1']
observed_ids=['1']
duplicate_ids=['1']
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: duplicate_ledger_ids=['1']
novelty-gate: FAIL
expected_ids=['1', '2']
observed_ids=['1']
duplicate_ids=[]
missing_ids=['2']
extra_ids=[]
warnings=0
FAIL: missing_ledger_ids=['2']
novelty-gate: FAIL
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: item=1 axis_1_numeric_or_cosmetic='좌표 변경 2→3'
novelty-gate: FAIL
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: item=1 type_mismatch set=SM2-09 ledger=SM2-16
novelty-gate: FAIL
expected_ids=['1', '2']
observed_ids=['1', '2']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
EXIT_CODE=0
```

### Required direct-CLI matrix

Each case was written under a fresh `tempfile.TemporaryDirectory`, executed via
`python -X utf8 tools/check_novelty_ledger.py --set ... --ledger ... --required-count ...`,
and removed after the matrix. Literal output:

```text
===== CASE valid =====
expected_ids=['1', '2']
observed_ids=['1', '2']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
EXIT_CODE=0
===== CASE numeric-only =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: item=1 axis_1_numeric_or_cosmetic='좌표 변경 2→3'
novelty-gate: FAIL
EXIT_CODE=1
===== CASE missing-id =====
expected_ids=['1', '2']
observed_ids=['1']
duplicate_ids=[]
missing_ids=['2']
extra_ids=[]
warnings=0
FAIL: missing_ledger_ids=['2']
novelty-gate: FAIL
EXIT_CODE=1
===== CASE duplicate-id =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=['1']
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: duplicate_ledger_ids=['1']
novelty-gate: FAIL
EXIT_CODE=1
===== CASE type-mismatch =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: item=1 type_mismatch set=SM2-09 ledger=SM2-16
novelty-gate: FAIL
EXIT_CODE=1
CASE_EXIT_CODES=0,1,1,1,1
TEMP_REMOVED=True
```

Required result: 5/5 cases matched the prescribed behavior; exits were `0,1,1,1,1`.

## Positive case

The valid two-item fixture printed exact `expected_ids=['1', '2']` and
`observed_ids=['1', '2']`; all duplicate/missing/extra lists were `[]`, `warnings=0`,
`novelty-gate: PASS`, exit 0. No false failure was observed.

## Negative cases (4/4)

| case | required named failure | observed gate | exit | result |
|---|---|---:|---:|---|
| numeric-only axis | `axis_1_numeric_or_cosmetic` | FAIL | 1 | PASS |
| missing ID | `missing_ledger_ids=['2']` | FAIL | 1 | PASS |
| duplicate ID | `duplicate_ledger_ids=['1']` | FAIL | 1 | PASS |
| type mismatch | `type_mismatch set=SM2-09 ledger=SM2-16` | FAIL | 1 | PASS |

## Contract consistency

- `.claude/agents/item-writer.md` rule 1 requires at least two changed **non-numeric**
  variation axes; rule 8 requires one matching novelty-ledger row per item and fixes the
  eight field names.
- `analysis/catalog/AUTHORING_GUIDE.md` §1-B contains exactly 9 checks. Checks 8 and 9 repeat
  the same two-axis requirement, exact eight-column ledger schema, exact ID cover, and
  `FAIL=0` requirement.
- The two canonical texts do not contradict each other.
- The implementation is inconsistent with two parts of that shared contract: it checks the
  eight-name header but not each row's exact field count, and it does not check the required
  same-stem set/ledger relationship.

## Adversarial findings

### A1 — Critical: extra TSV data columns fail open

`csv.DictReader` stores surplus row fields under a `None` key. The validator ignores that key,
so an exact eight-name header followed by a nine-field data row passes. This violates the
canonical **exact 8-column schema** and makes malformed rows indistinguishable from conforming
rows at the gate.

Direct CLI proof:

```text
===== ADVERSARIAL extra-data-column =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
EXIT_CODE=0
```

Required closure before requalification: reject every ledger row whose physical TSV field
count is not exactly 8, and add a direct-CLI or unit regression fixture for a ninth field.

### A2 — Critical: same-stem ledger binding is not enforced

The authoring guide requires `SET-STEM.md` and `SET-STEM.novelty.tsv`. The CLI accepts any
ledger pathname and validates only its contents. An unrelated ledger can therefore pass when
its numeric item IDs and type IDs happen to match the set, which is plausible across fixed-size
sets and breaks the canonical set-to-evidence binding.

Direct CLI proof:

```text
===== ADVERSARIAL wrong-stem-ledger =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
EXIT_CODE=0
TEMP_REMOVED=True
```

Required closure before requalification: fail unless the ledger is the set path's same-stem
`.novelty.tsv`, and add a wrong-stem regression fixture.

### Semantic-claim boundary

The module explicitly says it **cannot prove mathematical originality**. That limitation is
correct: it verifies completeness and a narrow cosmetic-token heuristic, but does not compare
the authored mathematics with `nearest_prior` or prove that ledger prose is true. The required
numeric-only self-disclosing fixture is caught, but a gate PASS must continue to be described
only as evidence-contract compliance, never as proof of originality.

### Encoding and header behavior

- Both set and ledger use `utf-8-sig`, so UTF-8 with or without BOM is accepted intentionally.
- `OSError`, `UnicodeError`, and `csv.Error` are caught by `main()` and produce a FAIL exit;
  those read/encoding failures are fail-closed.
- Header names and order are compared exactly. The critical header-adjacent gap is row width,
  described in A1.

## Stop/resume

Stop condition reached: one representative implementation was qualified, the full required
5-test/5-CLI matrix ran, and critical fail-open defects were proven. Do not dispatch or qualify
the 40-item authoring set under this gate. Resume only after the implementation owner fixes A1
and A2, updates regression tests, and the leader supplies a newly frozen four-input table; then
rerun the same required matrix plus both adversarial closures. `NEXT` belongs to leader
integration only.
