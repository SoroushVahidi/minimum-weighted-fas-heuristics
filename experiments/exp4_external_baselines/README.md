# EXP4: External Baseline Comparison (Primary Sparse Comparison)

**Status:** COMPLETE

## Purpose

Compares IPSNS against strong external FAS heuristics on the full sparse benchmark.
This is the primary sparse-comparison experiment in the paper.

## Benchmark set

105 instances; 97 standard nonnegative (8 negative-weight excluded: gerez, howard-max,
k3_3, ku, peterson, peterson1, peterson2, stg0).

## Methods

IPSNS, LR-TA, WMSF, Borda-net-score, Weighted-Eades, Random-multistart, iGraph-Eades, DRMacIver/FAS.
DRMacIver binary vendored in `external_tools/` (excluded from CI via pytest ignore).

## Key results (97 standard instances)

- IPSNS mean BW: 37,698 — best among all methods.
- IPSNS best on **96/97** instances (ties DRMacIver on 1: r20_60).
- DRMacIver/FAS mean BW: 53,173 (~21.6% excess over IPSNS).
- DRMacIver: 93/97 complete (2 DAG rejections, 2 timeouts on large instances).

## Manuscript use

Main sparse-comparison table; primary claim supporting IPSNS effectiveness.
Stochastic robustness of these results validated in EXP10.

## Canonical summary

`summary/exp4_external_stats.json`

## Raw output

Gitignored; regenerable with external binaries and graph-benchmarks instances.

## Checkpoint policy

No checkpoints. Single run per instance per algorithm.

## External dependency

DRMacIver/FAS binary required for full reproduction. Excluded from pytest CI:
`--ignore=experiments/exp4_external_baselines/external_tools`

## Rerun

```bash
# Requires external binaries and benchmark instances
# See online_resource_1/scripts/run_exp4_repro.py
```
