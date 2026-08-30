---
lane: verifier
grade: advisory
configured_model: gpt-5.6-sol
configured_reasoning: high
observed_model: unavailable
independence: fork_turns=none
verdict: approve
qualified_unit_count: 1
required_test_count: 8
required_cli_case_count: 8
frozen_inputs:
  - path: .claude/agents/item-writer.md
    bytes: 10818
    sha256: b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2
  - path: analysis/catalog/AUTHORING_GUIDE.md
    bytes: 10369
    sha256: 737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea
  - path: tools/check_novelty_ledger.py
    bytes: 8333
    sha256: 7ecb8c0acbb83cd25ce399b3365efb0389b1773d46f41a38d9b82c586dc1ed7d
  - path: tests/test_check_novelty_ledger.py
    bytes: 6305
    sha256: d380f0fc40c6b225778b97df973cff070d804bcd2cef6737fbf26d59c738e3c3
---

# Math-item novelty gate — independent requalification round 3

## Summary

**Advisory verdict: `approve`.** The round-3 frozen inputs matched 4/4. The unit suite
passed 8/8 (`OK`, exit 0). The eight prescribed direct-CLI cases matched the exact expected
exit sequence `0,1,1,1,1,1,1,0`, printed exact identifier diagnostics, printed
`warnings=0`, and ended with the correct `novelty-gate: PASS|FAIL` marker.

A1 ninth-field and A2 wrong-stem remain fail-closed. M1 is closed: a canonical main-plus-
auxiliary body tag keeps `SM2-09` as the main type and passes against ledger type `SM2-09`.
No critical regression or new fail-open behavior was established in the frozen revision.
No source/gate/test/canonical file was edited, and no 40-item candidate was read or qualified.

## Frozen-input verification

Command:

```powershell
$files=@('.claude/agents/item-writer.md','analysis/catalog/AUTHORING_GUIDE.md','tools/check_novelty_ledger.py','tests/test_check_novelty_ledger.py'); foreach($f in $files){$i=Get-Item -LiteralPath $f; $h=(Get-FileHash -Algorithm SHA256 -LiteralPath $f).Hash.ToLowerInvariant(); "{0}`t{1}`t{2}" -f $f,$i.Length,$h}
```

Literal output:

```text
.claude/agents/item-writer.md	10818	b715460c8ed3a40d57558329b8e5caf001d40587dd9dae0c6408d39c673565b2
analysis/catalog/AUTHORING_GUIDE.md	10369	737e72b8539a7bce6b0dca2bd36c51c579b2d0e0338afde04b52e45710fd84ea
tools/check_novelty_ledger.py	8333	7ecb8c0acbb83cd25ce399b3365efb0389b1773d46f41a38d9b82c586dc1ed7d
tests/test_check_novelty_ledger.py	6305	d380f0fc40c6b225778b97df973cff070d804bcd2cef6737fbf26d59c738e3c3
```

Result: all four byte counts and SHA-256 values exactly matched the round-3 freeze.

## Commands and literal outputs

### Unit suite — 8/8

Command:

```powershell
python -X utf8 -m unittest tests.test_check_novelty_ledger -v
```

Literal output (`EXIT_CODE` was emitted by the qualification wrapper):

```text
test_auxiliary_type_does_not_replace_main_type (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_auxiliary_type_does_not_replace_main_type) ... ok
test_duplicate_id_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_duplicate_id_fails) ... ok
test_extra_data_column_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_extra_data_column_fails) ... ok
test_missing_id_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_missing_id_fails) ... ok
test_numeric_only_axis_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_numeric_only_axis_fails) ... ok
test_type_mismatch_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_type_mismatch_fails) ... ok
test_valid_exact_cover_passes (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_valid_exact_cover_passes) ... ok
test_wrong_stem_ledger_fails (tests.test_check_novelty_ledger.NoveltyLedgerTest.test_wrong_stem_ledger_fails) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.019s

OK
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
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
FAIL: ledger_path_mismatch expected=C:\Users\Park\AppData\Local\Temp\tmpcpn0zod5\set.novelty.tsv observed=C:\Users\Park\AppData\Local\Temp\tmpcpn0zod5\unrelated.novelty.tsv
novelty-gate: FAIL
EXIT_CODE=0
```

### Required direct-CLI matrix — 8/8

Each case was created under `tempfile.TemporaryDirectory` and invoked as:

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
FAIL: ledger_path_mismatch expected=C:\Users\Park\AppData\Local\Temp\novelty-gate-r3-ia76aow1\A2-wrong-stem\set.novelty.tsv observed=C:\Users\Park\AppData\Local\Temp\novelty-gate-r3-ia76aow1\A2-wrong-stem\unrelated.novelty.tsv
novelty-gate: FAIL
EXIT_CODE=1
===== CASE M1-main-plus-auxiliary =====
expected_ids=['1']
observed_ids=['1']
duplicate_ids=[]
missing_ids=[]
extra_ids=[]
warnings=0
novelty-gate: PASS
EXIT_CODE=0
CASE_EXIT_CODES=0,1,1,1,1,1,1,0
TEMP_REMOVED=True
```

All eight cases printed exact expected/observed IDs, duplicate/missing/extra lists,
`warnings=0`, the correct final marker, and the required exit code.

## Closure matrix

| unit | acceptance behavior | observed | disposition |
|---|---|---|---|
| original valid | PASS, exit 0 | exact | pass |
| numeric-only | named cosmetic-axis failure, exit 1 | exact | pass |
| missing ID | `missing_ledger_ids=['2']`, exit 1 | exact | pass |
| duplicate ID | `duplicate_ledger_ids=['1']`, exit 1 | exact | pass |
| type mismatch | named main-type mismatch, exit 1 | exact | pass |
| A1 ninth field | `field_count=9 expected=8`, exit 1 | exact | closed |
| A2 wrong stem | `ledger_path_mismatch`, exit 1 | exact | closed |
| M1 main + auxiliary | PASS with ledger main `SM2-09`, exit 0 | exact | closed |

## Regression and fail-open inspection

- `parse_items()` now selects `type_matches[0]`; in the canonical item footer the main type
  precedes explicit auxiliaries such as `(+SM2-16)`. The direct CLI and unit fixture both
  prove the M1 valid form no longer binds to the auxiliary.
- Plain mismatched ledger type remains rejected, so the M1 repair does not fail open on the
  original type-mismatch case.
- Exact eight-field row enforcement and same-stem path enforcement remain active and pass
  their direct closure fixtures.
- Expected/observed/duplicate/missing/extra identifier diagnostics remain stable; all warning
  counts are zero.
- Exact header comparison and fail-closed `OSError`/`UnicodeError`/`csv.Error` handling remain.
- The parser relies on the canonical footer ordering in which main type is the first type token
  in the item block. That is consistent with the frozen item-writer output contract; no
  conflicting supported tag form was observed in the permitted inputs.
- No critical regression or new fail-open behavior was established.

## Contract consistency

The frozen canonicals remain consistent: item-writer rule 1 and AUTHORING_GUIDE check 8 require
at least two non-numeric axes; item-writer rule 8 and AUTHORING_GUIDE check 9 require the same
exact eight-column, same-stem, exact-ID-cover novelty ledger. The implementation now enforces
the tested coverage/schema/path/main-type portions without contradicting those rules.

## Semantic-claim boundary

`novelty-gate: PASS` means **evidence-contract compliance only**. The tool expressly cannot
prove mathematical originality, does not compare the mathematical structure against the named
prior, and cannot establish that ledger prose is substantively true. Those remain reviewer
judgments. This advisory approval does not broaden the gate's semantic claim.

## Stop/resume

Stop condition reached in one round-3 qualification turn: hashes 4/4, unit tests 8/8, direct
CLI cases 8/8, warnings zero, and no critical defect. The gate implementation is qualified for
leader integration of the next author-pilot stage. This report does not qualify any generated
40-item set. `NEXT` is leader integration only; this verifier performs no source fix.
