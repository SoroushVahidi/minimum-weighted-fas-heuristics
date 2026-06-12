# EXP10 Final Validation

## Phase 1 state (2026-06-12)

| # | Item | Value |
|---|------|-------|
| 1 | Branch | `main` |
| 2 | HEAD | `80b3144d5fdbbe250faed8a4fe671dde2da76c89` |
| 3 | DRMacIver runner active | No |
| 4 | wait_and_finalize active | No (completed with script fixes) |
| 5 | DRMacIver completed | 1860 |
| 6 | Expected | 1860 |
| 7 | Valid (PASS) | 1860 |
| 8 | Failed | 0 |
| 9 | Timeout | 0 |
| 10 | Crash | 0 |
| 11 | Malformed | 0 |
| 12 | Duplicate keys | 0 |
| 13 | Missing keys | 0 |
| 14 | .tmp files | 0 |
| 15 | Last log update | 2026-06-12T02:24:19Z |
| 16 | Unique PIDs | 1860/1860 |
| 17 | Smoke excluded | Yes (9 archived) |
| 18 | IPSNS valid | 1860/1860 |

## Validation artifacts

- `summary/drmaciver_validation_report.csv`
- `summary/drmaciver_validation_summary.json` (`validation_passed: true`)
- `summary/drmaciver_per_instance_summary.csv`
- `summary/drmaciver_variability_summary.csv`
- `summary/drmaciver_phase_conclusions.md`
- `summary/ipsns_validation_summary.json` (pre-existing, passed)
- `summary/COMPLETED.ok`

## IPSNS limitation (retained)

Validated IPSNS records support objective-level repeated-seed analysis. They do **not** preserve every search trajectory or ordering for post-hoc trajectory comparison.

## Script repairs (infrastructure only)

1. `validate_drmaciver_runs.py`: fixed `smoke_shas` variable shadowing (`UnboundLocalError`).
2. `finalize_exp10.py`: fixed EXP4 WTL tuple index in `write_final_conclusions`.

Production algorithm source was **not** modified.
