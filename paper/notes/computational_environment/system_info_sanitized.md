# Computational Environment — Sanitized Summary

**Date collected:** 2026-06-07

## CPU
- Model: Intel Core i7-12700K (12th Gen)
- Cores: 12 physical / 20 logical (hyperthreading enabled)
- Max frequency: 5.0 GHz
- Architecture: x86_64

## Memory
- RAM: 62 GiB

## Operating system
- Ubuntu 24.04.4 LTS (Noble Numbat)
- Kernel: Linux 6.17.0-23-generic

## Python and packages
- Python 3.12.3
- numpy 2.4.4
- pandas 3.0.2
- scipy 1.17.1
- networkx 3.6.1
- matplotlib 3.10.9
- igraph 1.0.0

## Intentionally excluded
- Hostname (removed for anonymization)
- Username / home directory path
- Institution or cluster identifiers

## Consistency check
- EXP3 log (`experiments/exp3_exact_small/logs/exp3_exact.log`) records Python 3.12.3,
  consistent with current system. No conflicting environment statements found in any
  experiment log.

## Uncertainty
- All final experiment runs (EXP1b–EXP9) were executed on this machine under the same
  Python environment. Wall-clock times should be compared within each experiment, not
  across machines, as external tools (DRMacIver/FAS, igraph) were invoked via subprocess
  and their implementations differ in CPU utilization patterns.
