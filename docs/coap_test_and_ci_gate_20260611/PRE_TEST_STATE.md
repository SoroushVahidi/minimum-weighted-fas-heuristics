# Pre-Test State (Repository Baseline)

**Audit date:** 2026-06-11

| Item | Value |
|------|-------|
| Branch | `main` |
| HEAD | `80b3144d5fdbbe250faed8a4fe671dde2da76c89` |
| Python | 3.12.3 |
| Runtime deps | numpy 2.4.4, pandas 3.0.2, networkx 3.6.1 (`requirements.txt`) |
| Prior automated tests | 10 tests in `experiments/exp10_stochastic_robustness/scripts/test_drmaciver_namespace.py` (script-style, not in `tests/`) |
| Prior CI | None (`.github/` absent before interrupted task) |
| Prior `tests/` directory | Absent before interrupted task |
| Initial collection (repo-wide, pre-completion) | 10 tests (EXP10 namespace script only) |
| Packaging | No root `pyproject.toml`; import via `PYTHONPATH=src` / `pytest.ini pythonpath` |

## Safe baseline command (original)

```bash
python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q
```

Result before new suite: **10 passed**.
