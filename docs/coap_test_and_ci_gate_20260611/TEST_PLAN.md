# Test Plan — COAP Reproducibility Gate

## Scope

Canonical modules under test:

- `src/mwfas/lrta.py`
- `src/mwfas/wmsf.py`
- `src/mwfas/ipsns.py`
- `src/mwfas/exact.py`
- `src/mwfas/evaluation.py`
- `src/mwfas/io.py`

CLI scripts (smoke only): `scripts/run_{lrta,wmsf,ipsns,exact}.py`

## Architecture

```
tests/
├── conftest.py
├── helpers/          # graph_builders, brute_force, assertions
├── unit/             # per-module correctness
├── property/         # seeded random invariants
├── regression/       # fixtures, CLI, infra, EXP10 read-only
└── data/
    ├── tiny_graphs/  # 3 DIMACS fixtures
    └── expected_results/
```

## Principles

1. Independent `brute_force_min_backward` for expected objectives.
2. Tiny synthetic graphs only; no large benchmark copies.
3. No writes to active EXP10 directories.
4. Production defects preserved as failing tests + bug register (none found).
5. No production code changes in this gate.

## Categories implemented

| Category | Module(s) | Count (approx.) |
|----------|-----------|---------------|
| Evaluation | `test_evaluation.py`, property | 13 |
| I/O | `test_io.py` | 8 |
| LR-TA | `test_lrta.py`, property | 17 |
| WMSF | `test_wmsf.py`, `test_wmsf_safe_edge.py` | 9 |
| IPSNS | `test_ipsns.py`, `test_ipsns_rollback.py` | 7 |
| Exact DP | `test_exact.py`, fixture derivation | 10 |
| CLI smoke | `test_cli_smoke.py` | 4 |
| Regression fixtures | `test_known_instances.py` | 3 |
| Experiment infra | `test_experiment_infrastructure.py` | 5 |
| EXP10 namespace | `test_exp10_namespace.py` | 7 |

## Out of scope

- Full benchmark reruns
- DRMacIver binary builds
- Manuscript table regeneration
- Formal proof verification
- `baselines.py` (not canonical COAP core)
