# COAP Testing Statement (draft for Online Resource 1 / cover letter)

We provide an automated regression and correctness test suite for the canonical minimum weighted feedback arc set implementation (`src/mwfas/`). As of 2026-06-11, the suite contains **78 tests** (77 passing, 1 skipped when EXP10 runner inactive), executed in approximately 2 seconds on a standard Linux workstation with Python 3.12.

**Categories covered:** objective consistency (independent brute-force reference), DIMACS I/O parsing, LR-TA feasibility and add-back inclusion-minimality, WMSF safe-edge handling and minimization, IPSNS incumbent protection and seeded reproducibility, exact dynamic programming cross-checked against brute force for \(n \le 8\), CLI smoke tests on tiny fixtures, isolated experiment-infrastructure patterns, and read-only EXP10 smoke-archive integrity checks.

**Exact validation:** `exact_min_fas_dp` is compared to an independent brute-force enumerator on hand-crafted and seeded random tiny graphs; committed regression fixtures cross-check `exact_bw` independently.

**Reproducibility command:**

```bash
pip install -r requirements-dev.txt
PYTHONPATH=src python3 -m pytest tests/ -q
```

**CI:** GitHub Actions workflow `.github/workflows/tests.yml` runs the same suite on Python 3.11 and 3.12 (workflow validated locally; remote pass not claimed here).

**Limitations:** Tests use tiny synthetic graphs only; they do not certify approximation ratios, formal proofs, or full-benchmark optimality. WMSF stabilization is not asserted to be non-worsening. Coverage of `ipsns.py` remains partial (~66%) because legacy seed paths and long LNS branches are not exhaustively exercised.
