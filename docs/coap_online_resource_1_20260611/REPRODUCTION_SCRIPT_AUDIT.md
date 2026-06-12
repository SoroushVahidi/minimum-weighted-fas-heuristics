# Reproduction Script Audit

| Script | Status | Notes |
|--------|--------|-------|
| `reproduce_smoke.sh` | **PASS** | 3 tiny fixtures validated |
| `reproduce_tests.sh` | **PASS** | 76 passed, 2 skipped in OR1 |
| `reproduce_principal_tables.sh` | **PASS** | 8 numerical checks |
| `validate_artifact.sh` | **PASS** | structure + smoke + tests |
| `optional_full_reproduction.sh` | **DOC only** | does not launch reruns |

All scripts use relative paths from artifact root; no `/home/soroush/` paths.
