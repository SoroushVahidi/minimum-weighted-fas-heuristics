# Remote CI Readiness

## Workflow

File: `.github/workflows/tests.yml`

| Check | Status |
|---|---|
| Test path `tests/` | consistent |
| PYTHONPATH via pytest from repo root | implicit via package layout |
| Dependencies `requirements-dev.txt` | present |
| External binaries in CI | none required for unit tests |
| Benchmark downloads | none |
| Stale expected counts in workflow | none (no hard-coded pass count) |
| Python matrix 3.11, 3.12 | configured |
| Coverage on failure | configured |

## Remote execution

**Workflow locally validated; remote execution remains pending until the branch is pushed.**

Per instruction, no push was performed. This is a submission-quality recommendation, not a scientific blocker given local 90/1 gate.
