---
lane: verifier
grade: advisory
configured_model: gpt-5.6-sol
configured_reasoning: high
observed_model: unavailable
independence: fork_turns=none
verdict: revise-required
qualified_unit_count: 1
required_test_count: 7
required_cli_case_count: 7
frozen_inputs:
  - path: .claude/agents/item-writer.md
    bytes: 10818
    sha256: b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2
  - path: analysis/catalog/AUTHORING_GUIDE.md
    bytes: 10369
    sha256: 737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea
  - path: tools/check_novelty_ledger.py
    bytes: 8157
    sha256: dec2eec7f5324e25e19b24f96f7ca99e9ef588697d653184119cdf7204856835
  - path: tests/test_check_novelty_ledger.py
    bytes: 5865
    sha256: 4a244863492834a9693278ac06c96cf35386aed3b8ed7142ff7e8394fa0df0d1
---

# Math-item novelty gate — independent requalification round 2

## Summary

**Advisory verdict: `revise-required`.** The new frozen inputs matched 4/4. The revised
unit suite passed 7/7 (`OK`, exit 0). The seven prescribed direct-CLI cases also matched
exactly: the original five exited `0,1,1,1,1`, and the A1 ninth-field and A2 wrong-stem
closures both printed their named failure, `novelty-gate: FAIL`, and exited 1. Every case
printed `warnings=0`.

Requalification still fails because the required auxiliary-tag probe found a critical
main-type parsing defect. For a valid body tag `[SM2-09(+SM2-16) ...]`, the parser takes the
last `SM2-xx` match and binds the ledger to auxiliary `SM2-16`, falsely rejecting ledger main
type `SM2-09`. No source/gate/test/canonical file was edited, and no 40-item set was read.

## Frozen-input verification

Command:

```powershell
$files=@('.claude/agents/item-writer.md','analysis/catalog/AUTHORING_GUIDE.md','tools/check_novelty_ledger.py','tests/test_check_novelty_ledger.py'); foreach($f in $files){$i=Get-Item -LiteralPath $f; $h=(Get-FileHash -Algorithm SHA256 -LiteralPath $f).Hash.ToLowerInvariant(); "{0}`t{1}`t{2}" -f $f,$i.Length,$h}
```

Literal output:

```text
.claude/agents/item-writer.md	10818	b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2
analysis/catalog/AUTHORING_GUIDE.md	10369	737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea
tools/check_novelty_ledger.py	8157	dec2eec7f5324e25e19b24f96f7ca99e9ef588697d653184119cdf7204856835
tests/test_check_novelty_ledger.py	5865	4a244863492834a9693278ac06c96cf35386aed3b8ed7142ff7e8394fa0df0d1
```

Result: all byte counts and SHA-256 values exactly matched the round-2 frozen request.

## Commands and literal outputs

### Unit suite — 7/7

Command:

```powershell
python -X utf8 -m unittest tests.test_check_novelty_ledger -v
```

Literal output (`EXIT_CODE` was emitted by the qualification wrapper):

```text
test_duplicate_id_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_duplicate_id_fails) ... ok
test_extra_data_column_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_extra_data_column_fails) ... ok
test_missing_id_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_missing_id_fails) ... ok
test_numeric_only_axis_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_numeric_only_axis_fails) ... ok
test_type_mismatch_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_type_mismatch_fails) ... ok
test_valid_exact_cover_passes (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_valid_exact_cover_passes) ... ok
test_wrong_stem_ledger_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_wrong_stem_ledger_fails) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.021s

OK
expected_ids=['1']
observed_ids=['1']
duplicate_ids=['1']
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: duplicate_ledger_ids=['1']
novelty-gate: FAIL
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: row=2 field_count=9 expected=8
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
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: ledger_path_mismatch expected=C:\Users\Park\AppData\Local\Temp\tmp2m8zs1hl\set.novelty.tsv observed=C:\Users\Park\AppData\Local\Temp\tmp2m8zs1hl\unrelated.novelty.tsv
novelty-gate: FAIL
EXIT_CODE=0
```

### Required direct-CLI matrix — 7/7

Each case was built in `tempfile.TemporaryDirectory` and invoked as:

```text
python -X utf8 tools/check_novelty_ledger.py --set <temporary-set> --ledger <temporary-ledger> --required-count <count>
```

Literal output:

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
===== CASE A1-ninth-field =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: row=2 field_count=9 expected=8
novelty-gate: FAIL
EXIT_CODE=1
===== CASE A2-wrong-stem =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: ledger_path_mismatch expected=C:\Users\Park\AppData\Local\Temp\novelty-gate-requal-sa1nwxvc\A2-wrong-stem\set.novelty.tsv observed=C:\Users\Park\AppData\Local\Temp\novelty-gate-requal-sa1nwxvc\A2-wrong-stem\unrelated.novelty.tsv
novelty-gate: FAIL
EXIT_CODE=1
CASE_EXIT_CODES=0,1,1,1,1,1,1
TEMP_REMOVED=True
```

All seven cases printed exact expected/observed identifiers, duplicate/missing/extra lists,
`warnings=0`, a final PASS/FAIL marker, and the required exit code.

## A1/A2 closure

| closure | required behavior | observed | result |
|---|---|---|---|
| A1 ninth TSV field | named `field_count=9 expected=8`, FAIL, exit 1 | exact match | closed |
| A2 wrong ledger stem | named `ledger_path_mismatch`, FAIL, exit 1 | exact match | closed |

The prior round's two defects are fixed without regression in the original five CLI cases.

## Adversarial main-type finding

### Critical M1 — auxiliary type is incorrectly selected as the main type

`parse_items()` applies `TYPE_RE.findall(block)` and stores `type_matches[-1]`. With the
supported tag form `[SM2-09(+SM2-16) ...]`, the last match is auxiliary `SM2-16`, not main
`SM2-09`. A conforming ledger row therefore receives a false `type_mismatch` and exit 1.

Direct CLI command shape:

```text
python -X utf8 tools/check_novelty_ledger.py --set <set-containing-[SM2-09(+SM2-16)]> --ledger <same-stem-ledger-with-type-SM2-09> --required-count 1
```

Literal output:

```text
===== ADVERSARIAL main-plus-auxiliary-tag =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
FAIL: item=1 type_mismatch set=SM2-16 ledger=SM2-09
novelty-gate: FAIL
EXIT_CODE=1
TEMP_REMOVED=True
```

This is critical under the round-2 acceptance instruction. The parser must bind only the
main type in the item's canonical tag, not the last type token anywhere in the item block.
A regression fixture using the exact main-plus-auxiliary form is required before requalification.

## Regression and fail-open inspection

- A1 row-width enforcement uses `csv.reader` and rejects every physical row whose field count
  differs from 8; normalization occurs only after the failure is recorded.
- A2 compares resolved ledger and expected same-stem paths before content validation.
- The original positive, numeric-only, missing-ID, duplicate-ID, and plain type-mismatch cases
  retain their required behavior.
- Read/Unicode/CSV exceptions remain fail-closed through the `main()` exception boundary.
- Exact header comparison remains intact.
- No new fail-open defect was established in the inspected revision. M1 is instead a critical
  false failure on a contract-valid auxiliary tag and is independently sufficient for
  `revise-required`.

## Semantic-claim boundary

The module still states that it cannot prove mathematical originality. That boundary is
correct. Its PASS can establish ledger coverage, schema/path compliance, and the presence of
axis/structural/prior claims; it cannot prove those claims mathematically true or prove an item
original. Requalification does not broaden that claim.

## Stop/resume

Stop condition reached in one requalification turn. The required 7/7 unit tests and 7/7 CLI
cases completed with zero warnings, A1/A2 are closed, and critical M1 is directly reproduced.
The 40-item author pilot remains blocked. Resume only after the implementation owner repairs
main-type parsing, adds a main-plus-auxiliary regression test, and the leader supplies a new
frozen-input table. `NEXT` is leader integration only; this verifier performs no source fix.
