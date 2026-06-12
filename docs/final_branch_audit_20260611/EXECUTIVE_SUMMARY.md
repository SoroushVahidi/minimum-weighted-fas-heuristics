# Executive Summary — Final Branch Audit
**Date:** 2026-06-11  
**Branch:** main  
**HEAD:** 80b3144d5fdbbe250faed8a4fe671dde2da76c89  
**Target:** Computational Optimization and Applications (COAP), Springer Nature

---

## 1. Branch State at Audit Time

| Item | Status |
|------|--------|
| Branch | `main`, up to date with `origin/main` |
| Uncommitted changes | `src/mwfas/ipsns.py` (EXP10 diagnostic instrumentation — intentional, safe) |
| Untracked | `docs/full_repository_audit_20260610/`, `experiments/coap_ipsns_holdout/checkpoints/`, `experiments/coap_ipsns_holdout/results/`, `experiments/exp10_stochastic_robustness/`, `logs/coap_ipsns_holdout/` |
| Merge conflicts | None |
| Active process | EXP10 IPSNS runner (PID 24482, 65% complete at audit time) |

## 2. Running Experiment

**EXP10 Stochastic Robustness (IPSNS phase):** 1215/1860 IPSNS runs complete at audit time. PID 24482 actively consuming ~100% of one CPU core. DRMacIver phase not yet started. EXP10 is designed to answer whether IPSNS's 37/55/1 advantage over DRMacIver is robust across repeated randomized runs.

## 3. Science Verdict

The principal empirical claims are **verified**:

| Claim | Source | Status |
|-------|--------|--------|
| IPSNS best on 96/97 sparse instances | `exp4_raw_summary.csv` direct recompute | **VERIFIED** |
| 37/55/1 vs DRMacIver on 93 common instances | Same data | **VERIFIED** |
| 21.61% mean relative excess (DRMacIver) | `exp4_external_stats.json` + direct calc | **VERIFIED** |
| 56/57 exact optimal (IPSNS) | `exp3_exact_report.md` | **VERIFIED** |
| Zero incumbent violations (105 instances) | `exp1b_raw_summary.csv` direct recompute | **VERIFIED** |
| EXP8: 7/15 proven optimal, IPSNS matches 6/7 | `exp8_final_report.md` | **VERIFIED** |
| Holdout complete (1290/1290 runs) | `logs/coap_ipsns_holdout/COMPLETED.ok` | **VERIFIED** |

All six canonical source files (`lrta.py`, `wmsf.py`, `ipsns.py`, `exact.py`, `evaluation.py`, `io.py`) have been audited. All algorithms are correctly implemented. Formal propositions in the manuscript accurately reflect the code behavior.

## 4. Open Issues Summary

| Severity | Count | Summary |
|----------|-------|---------|
| BLOCKER | 2 | EXP10 not yet complete; no test suite |
| CRITICAL | 3 | Stale EJCO submission package; ipsns.py instrumentation uncommitted; EXP10 results not yet available for manuscript integration |
| MAJOR | 4 | DRMacIver single-run limitation; absolute paths in EXP10 config; no validation script for EXP10 output; DRMacIver non-determinism underqualified in §5 |
| MODERATE | 5 | sfas identity unresolved (audit-only); supplementary artifact not COAP-targeted; EXP10 data has machine-local paths in JSON records; EXP5 best-known comparison absent; igraph Eades weight semantics note |
| MINOR | 5 | Various disclosure and wording items |
| INFORMATIONAL | 4 | Observations without required action |

## 5. Algorithm Correctness

All principal algorithms are correctly implemented:
- **LR-TA**: correct cycle detection, correct add-back using original weights (W0), deterministic topo-sort via min-heap, no global random state, correct termination
- **WMSF**: correct three-phase pipeline; stabilization swap guard is correct (rank check prevents cycle introduction); safe-edge propagation is correct
- **IPSNS**: correct rollback; incumbent guarantee enforced code-level (snapshot preserved); random.seed(rng_seed) isolates runs; `return_info=True` counters are additive-only and cannot change outcomes
- **Exact DP**: correct recurrence; handles self-loops (correctly excluded from forward weight); handles parallel arcs via adj accumulation
- **evaluation.py**: correct forward/backward definition; self-loops correctly counted as backward
- **io.py**: correct parallel-arc aggregation; deterministic sorted output

## 6. Manuscript Verdict

The COAP manuscript (paper_coap/) is scientifically accurate and well-positioned. Related-work disclosure is comprehensive and accurate (DF03, CC25, DRMacIver, BSNA21, SST16, GNNRank all addressed). Contribution claims are appropriately bounded. Formal propositions are accurate. All headline numbers are traceable to experiment outputs.

**One DRMacIver disclosure gap**: §5 does not explicitly state that DRMacIver/FAS was run only once per instance (single deterministic run under `srand(time|pid)`). While the discussion acknowledges DRMacIver is deterministic in documentation, the manuscript does not state that the 37/55/1 result rests on single runs. This is Moderate severity.

## 7. What Must Happen Before Submission

1. **EXP10 must complete** (IPSNS + DRMacIver phases + postprocessing) — results must be integrated into manuscript
2. **ipsns.py and EXP10 infrastructure must be committed**
3. **COAP submission package** must be created (ejco_source is stale)
4. **DRMacIver single-run qualification** should be added to §5 (one sentence)
5. **Absolute paths in EXP10 config** should be documented as machine-local
6. **Test suite** should exist; currently zero tests
7. **Declarations** are complete and appropriate; no changes needed there

## 8. What Must NOT Be Changed

- Any experiment outputs in EXP1–EXP9 (already reported in manuscript)
- Any experiment outputs in `coap_ipsns_holdout/` (frozen)
- Any experiment outputs in `coap_ipsns_sensitivity/` (completed, cited)
- The ipsns.py algorithm behavior (only diagnostic counters added, not algorithm)
- Any table or figure generated from EXP1–EXP9

## 9. Final Readiness Verdict

**NOT YET READY for final submission branch** — blocked by EXP10 incompleteness. The manuscript and code are otherwise near submission-ready. Once EXP10 completes and its results are integrated, the branch requires only minor text edits and package updates to reach final submission quality.

**Scientific validity: CONFIRMED.** All principal claims are verified. Code is correct. Related work is honest. Scope boundaries are clearly stated.
