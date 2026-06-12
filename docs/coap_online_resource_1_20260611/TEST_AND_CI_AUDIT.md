# Test and CI Audit

## OR1 artifact test run

```
PYTHONPATH=src python3 -m pytest tests/ -ra
76 passed, 2 skipped, 0 failed (78 collected)
```

Skips:
1. `test_no_stale_tmp_during_active_run` — runner inactive
2. `test_production_checkpoint_count_when_complete` — 1860 checkpoints not bundled in OR1

## Full repository (reference)

77 passed, 1 skipped, 0 failed

## CI workflow (`.github/workflows/tests.yml`)

| Check | Status |
|-------|--------|
| Python 3.11 + 3.12 | Configured |
| `requirements-dev.txt` install | Yes |
| `pytest tests/ --cov=mwfas` | Yes |
| EXP4 external_tools ignored | Via `testpaths=tests` in pytest.ini |
| Remote execution | **Pending** |
