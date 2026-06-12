# EXP8 Status Check — 2026-06-07

## Repository state
- **HEAD**: c9e7e56d07957fa3398eea390a442f4d9e6f2cf3
- **Branch**: main (up to date with origin/main)
- **Dirty files**: `experiments/exp8_medium_mip_baseline/summary/` (untracked)

## tmux session
- `mwfas_exp8_mip`: **NOT RUNNING** (experiment finished and session closed)

## EXP8 overall status: COMPLETED (EXP8_DONE_EXIT=0)

## Solver availability
- `scipy.optimize.milp (HiGHS)` v1.17.1: **available**
- All other solvers (highspy, pulp, ortools, gurobipy, python-mip): not available

## Selected instances
- 15 instances selected, all files found
- Size range: n=20–318, m=30–576

## Experiment results
- Completed: **15/15**
- Proven optimal: **7** (instances with n ≤ 170, MIP mode, all solved within time limit)
- Time-limit reached: **8** (instances with n ≥ 273, LP_relaxation mode, all hit 120s limit)
- Errors/skipped: **0**
- IPSNS matches MIP on: **6/7** proven optimal instances

### Result files (all present, not yet committed)
| File | Exists | Size |
|---|---|---|
| `summary/exp8_mip_raw_summary.csv` | YES | 3380 bytes, 15 rows |
| `summary/exp8_mip_summary.json` | YES | 2159 bytes |
| `summary/exp8_final_report.md` | YES | 1162 bytes |
| `summary/exp8_final_report_smoke.md` | YES | 701 bytes |
| `summary/exp8_mip_raw_summary_smoke.csv` | YES | 430 bytes |
| `summary/exp8_mip_summary_smoke.json` | YES | 541 bytes |
| `logs/exp8_tmux.log` | YES | 3655 bytes |
| `config/selected_instances.csv` | YES | 2314 bytes |

### Tracked vs untracked
- **Tracked (committed)**: README.md, config/solver_availability.{json,md}, all 4 scripts
- **Untracked (not yet committed)**: entire `summary/` directory, `logs/`, `config/selected_instances.csv`

## Next action
EXP8 is complete. Run the **EXP8 postprocessing/integration query** next to:
1. Commit results (summary/, logs/, selected_instances.csv)
2. Integrate MIP baseline findings into the manuscript
