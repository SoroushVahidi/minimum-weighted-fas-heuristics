# seedfix_full_wmsf: IPSNS WMSF Seed Alignment Diagnostic

**Status:** COMPLETE DIAGNOSTIC — not a benchmark experiment; no publishable results.

## Purpose

Documents and validates the fix to the IPSNS internal WMSF seed, ensuring it matches
the standalone WMSF pipeline (`wmsf_seed_mode="full"`).

## What was fixed

The legacy IPSNS internal seed used a simplified global algorithm that differed from
standalone WMSF (different SCC handling, no Stabilize step). The `gr10` instance exposed
this: legacy internal seed = 58,839 BW vs. standalone WMSF = 58,481 BW.

Fix: IPSNS now calls `wmsf_seed_solution_full()`, which matches the standalone pipeline
exactly. Guarantee `IPSNS_BW ≤ min(LR-TA, WMSF)` holds on all tested instances post-fix.

## Why EXP1 was superseded by EXP1b

EXP1 was run with the legacy seed and contained 1 incumbent-protection violation artifact.
EXP1b was re-run post-fix (0 violations).

## Canonical report

`seedfix_report.md`

## Smoke test

10 diagnostic instances (gr10, gr00, gr7, others); 10/10 pass post-fix.
