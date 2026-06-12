# Test results

**Command:** `PYTHONPATH=src python3 -m pytest tests/ -q`

| Metric | Before audit | After audit |
|--------|--------------|-------------|
| Collected | 78 | 91 |
| Passed | 77 | 90 |
| Skipped | 1 | 1 |
| Failed | 0 | 0 |

**New file:** `tests/unit/test_topo_extraction_math.py` (13 tests)

**Skipped test:** `test_no_stale_tmp_during_active_run` (EXP10 runner inactive)

**Production algorithms:** Unchanged behavior.
