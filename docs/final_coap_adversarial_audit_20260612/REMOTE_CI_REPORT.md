# GitHub Actions CI Report

**Audit date:** 2026-06-12  
**Branch:** `main`  
**Trigger commit:** `f306c15259132c564f981316872cfc63e94e2f80`

## Classification: **PASSED**

## Primary workflow run

| Field | Value |
|---|---|
| Workflow name | Tests |
| Run ID | 27392696517 |
| Trigger | `push` to `main` |
| Commit message | Finalize COAP manuscript, Online Resource 1, and submission package. |
| Status | **success** |
| Duration | ~31 s |
| URL | https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics/actions/runs/27392696517 |

## Jobs

| Job | Python | Status | Duration |
|---|---|---|---|
| `test (3.11)` | 3.11 | success | ~28 s |
| `test (3.12)` | 3.12 | success | ~28 s |

## Test result (remote, inferred from workflow success)

Matches local gate: **90 passed, 1 skipped, 2 warnings**  
Command: `PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools`

Skipped test: `tests/regression/test_exp10_namespace.py` — DRMacIver runner not active (expected).

## Artifacts

No workflow artifacts uploaded (test-only workflow).

## Secondary runs (same push window)

| Run ID | Workflow | Status |
|---|---|---|
| 27392697566 | Dependency Graph (pip) | success |

## Failure analysis

Not applicable — CI passed.

## Post-correction CI

A new commit correcting abstract length and related-work wording will trigger a fresh CI run. Local pytest after corrections: **90 passed, 1 skipped**.

## Answers

4. **Did GitHub Actions run?** Yes (run 27392696517 on f306c15).
5. **Did GitHub Actions pass?** Yes.
