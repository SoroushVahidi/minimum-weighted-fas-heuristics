# Reproduce

## Quick checks

```bash
python -m compileall src/mwfas scripts
```

These checks confirm that the bundled implementation modules and command-line
wrappers load cleanly in a fresh environment.

## Inspect the committed summary tables

- `experiments/combined/tables/`
- `experiments/exp1b_core_benchmark_full_wmsf_seed/summary/`
- `experiments/exp2_ablation/summary/`
- `experiments/exp3_exact_small/summary/`
- `experiments/exp4_external_baselines/summary/`
- `experiments/exp5_lolib_dense/summary/`
- `experiments/exp6_ipsns_budget_curve/summary/`
- `experiments/exp7_plain_local_search/summary/`
- `experiments/exp8_medium_mip_baseline/summary/`
- `experiments/exp9_application_case/summary/`

## Optional reruns

The following commands are time-consuming and may require datasets or external tools that are not bundled in this artifact:

```bash
python scripts/run_lrta.py --help
python scripts/run_wmsf.py --help
python scripts/run_ipsns.py --help
python scripts/run_exact.py --help
python scripts/run_drmaciver_fas.py --help
python scripts/run_exp6_ipsns_budget_curve.py --help
python scripts/run_exp7_plain_local_search.py --help
python scripts/run_exp8_medium_mip_baseline.py --help
python scripts/run_exp9_application_case.py --help
```

Exact reproduction of runtimes or external-baseline behavior may vary by machine,
dependency versions, and availability of third-party tools.
