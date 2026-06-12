# Test and CI Infrastructure Audit

**HEAD:** `6c04ff1`  
**Audit date:** 2026-06-12

## Configuration

| File | Role |
|---|---|
| `pytest.ini` | `testpaths=tests`, `pythonpath=src`, strict markers |
| `requirements-dev.txt` | pytest, coverage deps |
| `.github/workflows/tests.yml` | CI on push; Python 3.11 + 3.12 |
| `online_resource_1/pytest.ini` | OR1 packaged test config |

## Local test result (this audit)

```
Collected: 91
Passed:    90
Skipped:   1
Failed:    0
Warnings:  2 (DeprecationWarning in exp10 update_progress.py via infrastructure test)
Duration:  ~1.7 s
```

**Skipped test:** `tests/regression/test_exp10_namespace.py::…` — `DRMacIver runner not active` (checks for live DRMacIver PID; expected in dev environment).

## Remote CI

| Run | Commit | Result |
|---|---|---|
| 27393186733 | 6c04ff1 | **success** (3.11 + 3.12) |
| 27392696517 | f306c15 | success |

Local and remote gates are **aligned**.

## Test inventory summary

See `TEST_INVENTORY.csv` (91 rows including parametrized cases).

| Category | Count (approx.) | Location |
|---|---|---|
| Unit | ~40 | `tests/unit/` |
| Regression | ~15 | `tests/regression/` |
| Property | ~5 | `tests/property/` |
| Helpers | 3 modules | `tests/helpers/` |

## OR1 vs full repository

| Gate | Full repo | OR1 package |
|---|---|---|
| Collected | 91 | 86 (5 infrastructure tests omitted) |
| Passed | 90 | 79 |
| Skipped | 1 | 7 (EXP10 namespace suite when live tree absent) |

Declarations correctly distinguish 90/1 (full) vs OR1 packaged counts.

## Coverage

Coverage artifact upload on failure only; no committed coverage report in repo. Core modules (lrta, wmsf, ipsns, exact, io, evaluation, topo_extraction) have dedicated unit/regression tests.

## Untested / fragile paths

| Path | Risk | Mitigation |
|---|---|---|
| DRMacIver subprocess integration | External binary | EXP4 scripts; skipped namespace test without runner |
| Full EXP10 rerun | Compute + raw data | Summaries committed; raw gitignored |
| `experiments/*/scripts/` | Not unit-tested directly | `test_experiment_infrastructure.py` imports EXP10 helpers |
| HiGHS MIP in EXP8 | Optional scipy | Separate experiment; not in pytest |

## Warnings

`update_progress.py` uses deprecated `datetime.utcnow()` — cosmetic; triggered only when infrastructure test imports EXP10 dashboard.

## Recommendations (future, not this task)

1. Set EXP10 progress `status` to `COMPLETE` when `completed_ok` and no PIDs.
2. Replace `utcnow()` in `update_progress.py`.
3. Keep single pytest entry point documented in README.

## Verdict

**CI and test gate are submission-ready.** No failing tests; skip behavior is documented and intentional.
