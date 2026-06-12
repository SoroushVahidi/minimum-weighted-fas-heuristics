# Reproduction Script Audit

| Script | Purpose | Status |
|---|---|---|
| `scripts/reproduce_smoke.sh` | Level A — LR-TA, WMSF, IPSNS, exact, topo extraction | **PASS** |
| `scripts/reproduce_tests.sh` | Level B — full suite with gate | **PASS** (79/7 OR1; 90/1 full repo) |
| `scripts/reproduce_principal_tables.sh` | Level C — principal tables from summaries | **PASS** |
| `scripts/validate_artifact.sh` | Integrity, paths, secrets scan, smoke, tests, tables | **PASS** |
| `scripts/optional_full_reproduction.sh` | Level D commands documented | not executed |
| `scripts/finalize_or1.py` | Maintainer sync from repo root | operational |

## Portability

- All scripts use `$(cd "$(dirname "$0")/.." && pwd)` — no hard-coded home paths in execution paths.
- Clean-extraction validation in `/tmp/or1_validate_*` passed all gates.

## Status

**All required reproduction scripts validated.**
