# DRMacIver Preflight Report
**Date:** 2026-06-11T22:47:17Z
**Result:** PASS — DRMacIver phase may proceed

## Checks

| Check | Status | Detail |
|-------|--------|--------|
| ipsns_complete | ✓ PASS | 1860/1860 |
| ipsns_validated | ✓ PASS |  |
| binary_ok | ✓ PASS | Binary OK: experiments/exp4_extern |
| smoke_tests | ✓ PASS | 9/9 OK |
| instances_accessible | ✓ PASS |  |
| disk_space | ✓ PASS | 643.59 GB free |
| no_competing_process | ✓ PASS | none running |
| dr_output_namespace_clean | ✓ PASS | raw=0 ckpt=0 |
| dr_existing_runs | ✓ PASS | 0 pre-existing drmaciver_* records |
| git_commit | ✓ PASS | 80b3144d5fdbbe25... |

## DRMacIver Run Parameters

- Binary: `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas`
- Binary SHA256: `907b7abe96ff8fb54d8b70910eb3068744f765e72da5520f2c7aacf70ba996bd`
- Expected commit: `16ff24a92fde886e58819180a9fe686e60991c5c`
- Repetitions: 20 per instance
- Instances: 93 (common_93_instances.txt)
- Total runs: 1860
- Existing drmaciver_* artifacts in full namespace: 0
- Min inter-launch gap: 0.12s (for distinct time-based seeds)
- Timeout per run: 300s
- Stochasticity: `srand(time(NULL)|getpid())` — uncontrollable

## Launch Command (if preflight passes)

```bash
cd /home/soroush/minimum-weighted-fas-heuristics
python3 experiments/exp10_stochastic_robustness/scripts/run_drmaciver_repetitions.py \
  > experiments/exp10_stochastic_robustness/logs/drmaciver_runner.log 2>&1
```
