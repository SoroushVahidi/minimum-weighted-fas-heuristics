# DRMacIver Smoke-Test Archive (EXP10)

**Quarantine date:** 2026-06-11T22:47:15Z
**Branch:** main
**HEAD:** 80b3144d5fdbbe250faed8a4fe671dde2da76c89
**Script:** `scripts/quarantine_drmaciver_smoke_artifacts.py`

## Purpose

These are preflight/smoke-test outputs from `run_drmaciver_repetitions.py --smoke`
(3 instances × 3 repetitions = 9 runs). They were written to the production
namespace (`raw/drmaciver/`, `checkpoints/`) during environment validation and
would collide with production run keys (run00–run02 on stg, r20_60, s27).

**They are excluded from production analysis.**

## Why quarantined

DRMacIver preflight requires a clean production namespace before the full
93 × 20 = 1860 run phase. Smoke outputs share filenames with the first three
production repetitions on the smoke trio instances.

## Original paths

- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_r20_60_run00.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_r20_60_run00.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_r20_60_run00.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_r20_60_run00.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_r20_60_run01.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_r20_60_run01.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_r20_60_run01.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_r20_60_run01.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_r20_60_run02.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_r20_60_run02.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_r20_60_run02.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_r20_60_run02.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_s27_run00.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_s27_run00.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_s27_run00.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_s27_run00.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_s27_run01.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_s27_run01.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_s27_run01.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_s27_run01.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_s27_run02.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_s27_run02.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_s27_run02.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_s27_run02.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_stg_run00.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_stg_run00.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_stg_run00.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_stg_run00.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_stg_run01.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_stg_run01.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_stg_run01.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_stg_run01.done`
- `experiments/exp10_stochastic_robustness/raw/drmaciver/drmaciver_stg_run02.json` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/raw/drmaciver_stg_run02.json`
- `experiments/exp10_stochastic_robustness/checkpoints/drmaciver_stg_run02.done` → `experiments/exp10_stochastic_robustness/smoke_archive/drmaciver/checkpoints/drmaciver_stg_run02.done`

## Scientific note

No scientific result was deleted. All artifacts were moved with SHA-256
verification before and after transfer.
