# Computational Environment — Notes

## Manuscript wording added

Added to `paper/sections/05_experimental_design.tex` (§5 Implementation and reproducibility, final paragraph):

> "Runtime values are wall-clock times on a Linux workstation (Intel Core i7-12700K,
> 62 GiB RAM, Ubuntu 24.04, Python 3.12) and are used mainly for within-study
> comparison; external tools were invoked via their documented interfaces."

## Source of hardware/software details

Collected 2026-06-07 via `lscpu`, `free -h`, `/etc/os-release`, and `python3 --version`.
See `system_info_raw.txt` for full output; `system_info_sanitized.md` for the clean summary.

## Intentionally excluded for anonymization

- **Hostname**: `al-khwarizmi` — removed (not in manuscript)
- **Username / home path**: `/home/soroush` — removed (not in manuscript)
- **Core count**: omitted from manuscript sentence (kept in sanitized notes only)
- **Package versions**: omitted from manuscript sentence; recorded in sanitized notes

## Consistency check

EXP3 log (`experiments/exp3_exact_small/logs/exp3_exact.log`) records Python 3.12.3,
consistent with the current environment. No conflicting hardware statements found in
any experiment log.

## Uncertainty

All final runs (EXP1b–EXP9) were executed on this machine. Wall-clock times depend
on hardware and external tool implementations, so the manuscript correctly limits
their interpretation to within-study comparisons.
