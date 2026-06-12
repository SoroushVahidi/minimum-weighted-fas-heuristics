# EXP11: Topological-extraction sensitivity

Frozen post-hoc study comparing alternative linear extensions of the **same**
final active DAG produced by LR-TA and IPSNS. Does not modify core algorithms or
prior experiment outputs.

## Scope

- Methods: LR-TA and IPSNS final active graphs on a 12-instance calibration subset.
- Rules: `current_min_id` (repository default), `max_id`, `weighted_net`, insertion refinement.
- Metric: backward weight `w(B_pi)` and extraction gap `w(F)-w(B_pi)`.

## Run

```bash
PYTHONPATH=src python3 experiments/exp11_topological_extraction_sensitivity/scripts/run_exp11.py
```

## Outputs

- `summary/exp11_per_instance.csv`
- `summary/exp11_aggregate.json`
- `summary/EXP11_RESULTS.md`
