# Test and CI Audit
**Date:** 2026-06-11

---

## 1. Test Discovery

```
$ python3 -m pytest tests/ -v --tb=short -q
ERROR: file or directory not found: tests/
collected 0 items
```

**Result: ZERO tests in the repository.** `pytest` finds no test files when run from the repository root.

The only test-like file found: `experiments/exp4_external_baselines/external_tools/fas-smartAE/test_reductions.py` — this is part of an external tool, not a repository test suite.

## 2. CI/CD Workflows

No `.github/workflows/` directory exists. No CI configuration found (no `.travis.yml`, `.circleci/`, `Makefile` targets for tests). **No automated testing or CI pipeline.**

## 3. Required Tests vs. Actual Tests

| Category | Required | Exists |
|----------|---------|--------|
| Cycle-peeling feasibility (LR-TA Phase 1 produces acyclic graph) | Yes | **No** |
| Simple-cycle extraction (DFS returns correct cycle) | Yes | **No** |
| Add-back acyclicity (LR-TA Phase 2 preserves acyclicity) | Yes | **No** |
| One-pass inclusion minimality (MinimizeFas) | Yes | **No** |
| WMSF safe-edge propagation correctness | Yes | **No** |
| WMSF stabilization non-worsening (conditional) | Yes | **No** |
| IPSNS rollback (state correctly reverted on failure) | Yes | **No** |
| IPSNS incumbent guarantee (output ≤ best seed) | Yes | **No** |
| Random-seed reproducibility (same seed → same result) | Yes | **No** |
| Objective equivalence (compute_forward_backward consistent with FAS set) | Yes | **No** |
| Exact DP versus brute force (small instances) | Yes | **No** |
| Negative-weight rejection in EXP exclusion | Yes | **No** |
| Zero-weight edge handling | Yes | **No** |
| Parallel-arc aggregation | Yes | **No** |
| Self-loop handling | Yes | **No** |
| Checkpoint atomicity (os.replace atomicity) | Yes | **No** |
| Duplicate-run prevention (checkpoint sentinel) | Yes | **No** |
| Output-schema validation (required JSON fields present) | Yes | **No** |

**Score: 0/18 required test categories have tests.**

## 4. Severity Assessment

The absence of a test suite is a **BLOCKER** for a reproducibility-first submission to COAP. The manuscript explicitly states: "A fully reproducible artifact accompanies the paper." An artifact with no tests provides no automated correctness guarantee. Reviewers and artifact evaluators will note this gap.

## 5. What Tests Would Catch

The code audit (see CODE_CORRECTNESS_AUDIT.md) found no bugs. However, without tests:
- Any future refactoring could silently break correctness properties
- The EXP10 instrumentation change to `ipsns.py` has no automated verification that it doesn't affect algorithm behavior
- The incumbent guarantee cannot be automatically regression-tested

## 6. Minimum Test Suite Recommendation

Priority 1 (before submission):
```
test_lrta.py:
  - test_lrta_produces_acyclic_output()  # compute_forward_backward + DAG check
  - test_lrta_add_back_non_worsening()  # BW(LR-TA) ≤ BW(LR no add-back)
  - test_lrta_small_known_instance()    # r20_60: BW=1688, stg: BW=5

test_ipsns.py:
  - test_ipsns_incumbent_guarantee()    # BW(IPSNS) ≤ min(BW(WMSF), BW(LR))
  - test_ipsns_reproducibility()        # same seed → same BW
  - test_ipsns_iters_zero_equals_seed() # iters=0 → returns best seed

test_exact.py:
  - test_exact_dp_small()               # known small instance
  - test_exact_dp_vs_ipsns()            # IPSNS ≥ exact on all n≤10 instances
  
test_io.py:
  - test_parallel_arc_aggregation()
  - test_self_loop_handling()
```

## 7. Linting / Type Checking

No `mypy`, `pylint`, `flake8`, or `ruff` configuration found. No formatting enforcement (no `black` or `isort` config). Code style is consistent but not enforced programmatically.

## 8. Packaging

`setup.py` present in `submission_package/ejco_reproducibility_artifact/setup.py` (stale). No `pyproject.toml` or current `setup.py` in repository root. Package is importable from `src/mwfas/` via `sys.path.insert(0, "src")` pattern used in scripts.

## 9. Summary

| Check | Status |
|-------|--------|
| Test suite exists | ❌ NO |
| Tests pass | N/A (no tests) |
| CI pipeline | ❌ NO |
| Linting | ❌ Not enforced |
| Type checking | ❌ Not enforced |
| Packaging | ⚠️ Stale |
| Manuscript build | ✓ Manual (LaTeX) |

**Test gap is the single largest engineering quality concern in this repository.**
