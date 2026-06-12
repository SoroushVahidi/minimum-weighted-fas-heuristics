# CI Workflow Audit

**File:** `.github/workflows/tests.yml`

## Validation performed locally

| Check | Result |
|-------|--------|
| YAML structure (basic parse) | Pass |
| Triggers `push`/`pull_request` on `main` | Present |
| Python matrix 3.11 + 3.12 | Present |
| Installs `requirements-dev.txt` | Present |
| Runs `pytest tests/ --cov=mwfas` | Present |
| No benchmark downloads | Pass |
| No DRMacIver build | Pass |
| No EXP10 execution | Pass |
| Upload artifact on failure | Present |

## Notes

- Workflow uses `pytest tests/` which respects `pytest.ini` (`pythonpath = src`).
- **Remote GitHub Actions execution not verified in this task.** Status: *workflow syntax and local command validated*.
- `pytest.ini` sets `testpaths = tests` — EXP10 script tests under `experiments/` are excluded from CI (namespace coverage moved to `tests/regression/test_exp10_namespace.py`).

## Recommended CI command (matches local gate)

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/ --cov=mwfas --cov-report=term-missing --cov-report=xml -q
```
