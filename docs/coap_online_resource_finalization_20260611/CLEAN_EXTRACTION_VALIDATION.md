# Clean Extraction Validation

**Temp directory:** `/tmp/or1_validate_wQBXVF` (representative run)

## Procedure

1. Extract `Vahidi_Online_Resource_1_MWFAS.zip` outside repository.
2. `cd online_resource_1`
3. Run validation and reproduction scripts.

## Results

| Step | Result |
|---|---|
| `validate_artifact.sh` | **PASSED** |
| `reproduce_smoke.sh` | **PASSED** |
| `reproduce_tests.sh` | **PASSED** (79 passed, 7 skipped) |
| `reproduce_principal_tables.sh` | **PASSED** |

## Portability

- No reliance on `/home/soroush/` paths.
- No writes outside extracted directory required.
- Logs preserved in `docs/coap_online_resource_finalization_20260611/logs/clean_*.log`.

## Status

**Clean-extraction validation passed.**
