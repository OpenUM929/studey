# Candidate fixture catalog

All fixtures are synthetic and remain inside this directory.  They are never appended to a ledger.

| fixture | planted defect | expected detector |
|---|---|---|
| `split_generator*` | two singleton rows carry the same `generator_id` | generator-equivalence maximality failure |
| `selftest.candidate.py` temporary `report_mojibake` case | corrupt report body | report content-integrity failure |
| `selftest.candidate.py` temporary `ruler_edit` case | generated expected span changed by hand | transcript-regeneration mismatch |
| `selftest.candidate.py` temporary `schema_ruler_edit` case | candidate acceptance schema replaced | acceptance-schema integrity/marker failure |

The remaining eight planted defects are also created in temporary copies by `selftest.candidate.py`.
The frozen 260828 sources are hashed before and after the run.
