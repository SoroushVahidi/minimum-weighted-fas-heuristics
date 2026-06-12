# Online Resource 1

**Title:** Algorithms, Proofs, Reproducibility Materials, and Extended Computational Results

**Companion manuscript:** *SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs* (Computational Optimization and Applications, Springer Nature)

**Author:** Soroush Vahidi (sv96@njit.edu), New Jersey Institute of Technology

**Frozen:** 2026-06-12 — see `provenance/source_commit.txt`

## Quick start

```bash
./scripts/validate_artifact.sh          # full validation
./scripts/reproduce_smoke.sh            # Level A
./scripts/reproduce_tests.sh            # Level B (OR1: 79 passed, 7 skipped; full repo: 90/1)
./scripts/reproduce_principal_tables.sh # Level C
```

## Contents

| Path | Description |
|------|-------------|
| `supplement/online_resource_1.pdf` | Supplementary PDF |
| `src/mwfas/` | Implementation including `topo_extraction.py` (EXP11 utilities) |
| `tests/` | Pytest gate (91 collected) |
| `results/` | Committed summaries EXP1--EXP11 |
| `scripts/` | Reproduction and validation |
| `provenance/` | Claim map, manifests, limitations |

## Reproducibility classification

The artifact is **computationally reproducible from validated summaries** for all headline tables (Level C). Full benchmark reruns (Level D) require external datasets and are optional. Smoke and test validation (Levels A--B) run from included source only.

## What is not bundled

EXP10 production raw JSON (3720 files) and checkpoints remain in the full repository; OR1 includes validated summaries and validation JSON sufficient to verify headline EXP10 claims.
