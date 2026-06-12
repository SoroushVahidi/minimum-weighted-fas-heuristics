# Executive Summary — COAP Test and CI Gate

**Audit date:** 2026-06-11  
**Branch:** `main` / **HEAD:** `80b3144d5fdbbe250faed8a4fe671dde2da76c89`  
**EXP10 modified:** No

---

## Interrupted work resolved

The prior session left a **mostly complete** `tests/` tree (64 passing tests) but **no documentation** and a few **test-only defects** (wrong tuple unpack, wrong manual expectations, broken imports, 12 accidental CSV artifacts). This resume pass:

- Audited and inventoried all partial files
- Deleted accidental CSV outputs from `tests/data/tiny_graphs/`
- Added EXP10 read-only namespace tests, fixture brute-force derivation, WMSF safe-edge regression, IPSNS rollback tests
- Ran full suite with coverage
- Produced all required `docs/coap_test_and_ci_gate_20260611/` deliverables

---

## Final test results

| Metric | Value |
|--------|-------|
| Collected | **78** |
| Passed | **77** |
| Failed | **0** |
| Skipped | **1** |
| Errors | **0** |

**Command:** `PYTHONPATH=src python3 -m pytest --ignore=experiments/exp4_external_baselines/external_tools -q`

---

## Required conclusions (30 questions)

| # | Question | Answer |
|---|----------|--------|
| 1 | Partial files found? | `tests/*` (mostly complete), `pytest.ini`, `requirements-dev.txt`, `.github/workflows/tests.yml`, 12 accidental CSVs, missing docs |
| 2 | Repaired/replaced? | CSVs deleted; 5 test-expectation fixes; 4 new test modules; docs created |
| 3 | Tests collected? | **78** |
| 4 | Pass/fail/skip/error? | **77 / 0 / 1 / 0** |
| 5 | LR-TA valid FAS on tested inputs? | **Yes** |
| 6 | LR-TA add-back inclusion-minimal? | **Yes** on tested graphs |
| 7 | WMSF safe-edge propagation correct? | **Yes** on tested regression graphs |
| 8 | WMSF restoration correct? | **Yes** (safe_tmp edges restored) |
| 9 | WMSF stabilization can worsen objective? | **Allowed by scope**; not a failing defect |
| 10 | WMSF feasible FAS on tested inputs? | **Yes** |
| 11 | IPSNS rollback restores state? | **Yes** on repair-failure path tested |
| 12 | IPSNS ≤ both seeds? | **Yes** on tested instances |
| 13 | Seeded IPSNS reproducible? | **Yes** |
| 14 | IPSNS alters global RNG? | **Yes** — calls `random.seed(rng_seed)` (documented) |
| 15 | Exact DP = brute force? | **Yes** for tested n |
| 16 | Objectives mutually consistent? | **Yes** |
| 17 | Parser contracts tested? | **Yes**; negative weights accepted at parse level |
| 18 | Checkpoint/resume utilities correct? | **Yes** in isolated temp-dir tests |
| 19 | EXP10 isolation without touching EXP10? | **Yes** — read-only pytest tests |
| 20 | Coverage per module? | eval 100%, io 97%, exact 92%, lrta 87%, wmsf 85%, ipsns 66% |
| 21 | Source defects found? | **None** |
| 22 | Result-affecting defects? | **None** |
| 23 | Experiments rerun required? | **No** |
| 24 | No-tests blocker resolved? | **Yes** |
| 25 | CI locally valid? | **Yes** (remote not run) |
| 26 | Suitable for OR1? | **Yes** as regression gate; expand IPSNS coverage recommended |
| 27 | Remains untested? | Legacy IPSNS seed path, baselines, full benchmarks, remote CI |
| 28 | Fix before submission? | Run GitHub Actions once; add OR1 test command to supplement |
| 29 | May defer? | Hypothesis tests, baselines coverage, table-regen integration |
| 30 | Next task? | **Integrate finalized EXP10 results into manuscript (§5–§6), then build Online Resource 1 including this test suite** |

---

## Files created/modified (test gate only)

**Created:** `tests/` (full tree), `pytest.ini`, `requirements-dev.txt`, `.github/workflows/tests.yml`, `docs/coap_test_and_ci_gate_20260611/*`

**Not modified:** `src/mwfas/*` (production), EXP10 directories, manuscript, experiment outputs

**Pre-existing unrelated modification:** `src/mwfas/ipsns.py` in working tree (not touched by this task)
