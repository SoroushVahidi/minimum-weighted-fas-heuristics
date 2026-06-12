# EXP1b: Main Sparse Benchmark (Canonical)

**Status:** COMPLETE — canonical internal benchmark for MWFAS paper.

## Purpose

Definitive core-benchmark run using the full WMSF seed mode (`wmsf_seed_mode="full"`).
Supersedes EXP1, which used the legacy internal seed and had one incumbent-protection violation.

## Benchmark set

105 unique instances from [alidasdan/graph-benchmarks](https://github.com/alidasdan/graph-benchmarks)
(123 listed; 18 duplicates removed). Nonnegative sparse digraphs.

## Methods

LR-TA (`lrta_full`), WMSF (`wmsf_seed_mode=full`), IPSNS (`ipsns_full`, 400 iterations, seed 1).

## Key results

- IPSNS ≥ LR-TA on all 105 instances (0 incumbent violations).
- IPSNS ≥ WMSF on all 105 instances.
- IPSNS improves over LR-TA on 16/105; over WMSF on 36/105.
- Mean runtime: IPSNS 20.2 s, LR-TA 0.074 s, WMSF 1.24 s.

## Manuscript use

Primary sparse-benchmark table; internal quality check. Not the primary publication comparison
(that is EXP4, which includes external baselines).

## Canonical summary

`summary/exp1b_core_benchmark_stats.json`, `summary/exp1b_core_benchmark_summary.md`

## Raw output

Gitignored (`raw/`, `logs/`); regenerable via `postprocess_exp1b.py` and instance list.

## Checkpoint policy

No checkpoints. Single run per instance per method.

## Rerun

```bash
# Requires graph-benchmarks instances at paths in configs/benchmark_instances.txt
# See OR1 README for reproduction detail
```
