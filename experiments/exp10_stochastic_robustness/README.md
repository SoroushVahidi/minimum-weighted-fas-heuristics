# EXP10: Stochastic Robustness Study

**Status:** COMPLETE — 1860/1860 IPSNS runs, 1860/1860 DRMacIver runs validated.

## Purpose

Validates that EXP4 results are robust under repeated runs: 20 IPSNS seeds and
20 DRMacIver/FAS repetitions per instance on the 93-instance common sparse subset.

## Benchmark set

93 instances: EXP4 standard nonnegative instances where DRMacIver completed (97 − 4 incomplete).

## Protocol

- IPSNS: 20 seeds (0–19), frozen configuration (400 iterations, topK=15).
- DRMacIver/FAS: 20 independent runs per instance.
- Quality-focused; not an equal-time comparison.

## Key results

- IPSNS: 0 objective variance across 20 seeds; seed 0 = best on all 93 instances.
- DRMacIver: 53/93 instances zero variance; 40/93 with variance.
- Per-instance median comparison: IPSNS wins 38, ties 55, loses 0.
- EXP4 sole DRMacIver win (r20_60) does NOT persist: IPSNS median 1688 vs DR median 1698.
- Mean relative excess (DR − IPSNS)/DR: 21.60% (matches EXP4 single-run result).
- Wilcoxon and sign tests: p < 0.001.

## Manuscript use

Stochastic-robustness section; corroborates primary EXP4 sparse comparison.
Reports 38/55/0 win/tie/loss and 21.60% mean relative excess.

## Canonical summary

`summary/FINAL_CONCLUSIONS.md`, `summary/experiment_metadata.json`,
`summary/paired_median_comparison.csv`, `summary/statistical_tests.json`.

Completion marker: `summary/COMPLETED.ok`

## Raw output

1860 IPSNS checkpoint files and 1860 DRMacIver checkpoint files. Raw data is local-only
(gitignored); summaries are committed and authoritative.

## Checkpoint policy

Checkpoints committed in `checkpoints/` namespace are production records.
9 smoke/preflight checkpoints quarantined in `drmaciver_smoke_archive/`.
Do not delete production checkpoints without external backup.

## Rerun

Expensive (~6 hours). Requires DRMacIver binary.
Not needed; summaries are validated and frozen.
