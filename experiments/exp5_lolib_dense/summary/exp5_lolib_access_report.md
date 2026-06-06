# EXP5 LOLIB Data Access Report

**Date:** 2026-06-06  
**Purpose:** Document access to LOLIB instance archives and related tools for EXP5.

---

## LOLIB Instance Data

### Primary Source (LOLIB website, GitHub Pages)

| URL | Command | Result |
|-----|---------|--------|
| `https://grafo.etsii.urjc.es/optsicom/lolib.html` | `wget -O - URL` | **200 OK** — HTML page accessible |
| `https://grafo.etsii.urjc.es/lolib/lop/SGB.zip` | `wget URL` | **404 Not Found** |
| `https://grafo.etsii.urjc.es/lolib/lop/IO.zip` | `wget URL` | **404 Not Found** |
| `https://grafo.etsii.urjc.es/lolib/lop/RandA1.zip` | `wget URL` | **404 Not Found** |

**Reason for 404:** The LOLIB website is hosted on GitHub Pages (`Server: GitHub.com`).
The download links on the HTML page reference ZIP files that were never committed to
the GitHub Pages repository. The HTML is live but the data files are absent.

### Alternative Source (Marti's personal page — Dropbox)

| URL | Command | Result |
|-----|---------|--------|
| `https://www.uv.es/~rmarti/paper/lop.html` | `wget -O - URL` | **200 OK** |
| `https://www.dropbox.com/s/fk105g63jmi3i1d/lolib_2010.zip?dl=1` | `wget -O lolib_2010.zip URL` | **200 OK — 10.7 MB** |

**Action:** Downloaded `lolib_2010.zip` (10,708,204 bytes) to
`experiments/exp5_lolib_dense/downloads/lolib_2010.zip` on 2026-06-06.

The archive is gitignored (large binary). It contains the following family ZIPs:
- `SGB.zip` — 135 KB (25 instances, all n=75)
- `IO.zip` — 111 KB (50 instances, n=44–79)
- `MB.zip` — 742 KB (not used in EXP5)
- `RandA1.zip` — 5.9 MB (100 instances: 25 each at n=100, 150, 200, 500)
- `RandA2.zip` — 845 KB (not used in EXP5)
- `RandB.zip` — 168 KB (not used in EXP5)
- `Spec.zip` — 82 KB (not used in EXP5)
- `xLOLIB.zip` — 2.6 MB (not used in EXP5)

**Families used:** SGB, IO, RandA1

---

## LOLIB File Format

```
Line 1: n (integer, number of objects)
Lines 2..n+1: n space-separated integer weights
  C[i][j] = weight of arc (i+1)→(j+1), 1-indexed
  Diagonal C[i][i] = 0
```

Confirmed format by inspecting:
- `SGB/N-sgb75.01` — first line `75`, then 75 rows of 75 integers
- `IO/N-be75eec` — first line `50`, then 50 rows of 50 integers
- `RandA1/N-t1d100.01` — first line `100`, then 100 rows of 100 integers

---

## Converter and Target Subset

**Converter:** `scripts/convert_lolib_to_dimacs.py`
- Writes only nonzero off-diagonal arcs (zero-weight arcs contribute 0 to objective)
- Writes metadata JSON sidecar with n, arcs written, total_weight, min/max weight

**Target subset selected (50 instances):**

| Family | n | Count | Notes |
|--------|---|-------|-------|
| SGB | 75 | 25 | All 25 instances |
| IO | 44–79 | 10 | N-be75eec/np/oi/tot, N-usa79, N-stabu70/74/75, N-tiw56n54/r54 |
| RandA1 | 100 | 5 | N-t1d100.01..05 |
| RandA1 | 150 | 5 | N-t1d150.01..05 |
| RandA1 | 200 | 5 | N-t1d200.01..05 |

n=500 RandA1 excluded (out of scope for exploratory benchmark; up to 250k arcs per instance).

**Converted DIMACS files:** `experiments/exp5_lolib_dense/converted/{SGB,IO,RandA1}/`  
Committed (gitignored pattern does not cover `converted/`).

**Tiny synthetic test:** `experiments/exp5_lolib_dense/configs/tiny_lolib_test.lop`  
4×4 matrix, all algorithms tested, smoke passed.

---

## Best-Known Solutions (BKS)

The Dropbox archive does not include BKS forward-objective values.
BKS values for LOLIB instances are published in:
- Martí, Reinelt, Duarte (2011) "A branch and cut algorithm for the LOP"
- The LOLIB website HTML mentions BKS tables but the ZIPs were not accessible

**Status:** BKS not loaded. EXP5 reports relative comparisons among algorithms only.
Gap to BKS is not computed in this run. Can be added manually if BKS values are obtained.

---

## LOP_MA-EDM

| Resource | URL | Status |
|----------|-----|--------|
| LOP_MA-EDM repo | `https://github.com/carlossegurag/LOP_MA-EDM` | **200 OK — accessible** |

**Action:** Not cloned or built. The repo provides a Memetic Algorithm for LOP
(C++ code). Build would require C++ compilation and input format investigation.
Decision: **not included in EXP5 first run** per task plan ("continue with DRMaciver
plus our existing baselines"). DRMaciver is the primary external baseline for
tournament/dense instances.

**Manual action if needed:** Clone to `experiments/exp5_lolib_dense/external_tools/LOP_MA-EDM`
and build with `make`. Expected input format: LOLIB matrix format.

---

## EJOR2015 GitHub Repo

| Resource | URL | Status |
|----------|-----|--------|
| EJOR2015 | `https://github.com/sgpceurj/EJOR2015` | **200 OK — accessible** |

Contents: `ILSr.zip`, `MAr.zip`, `xLOLIB.zip`, `xLOLIB2.zip`.
These are solver code (ILS and MA implementations) and extended LOLIB instances
(xLOLIB: n=150, 250 challenging instances from Martí et al. 2011).
**Not used in EXP5 first run.** Could extend to xLOLIB instances in a follow-up.

---

## Summary

| Item | Status |
|------|--------|
| LOLIB data downloaded | ✅ Dropbox (10.7 MB, 2026-06-06) |
| SGB instances (25) | ✅ Converted to DIMACS |
| IO instances (10 of 50) | ✅ Converted to DIMACS |
| RandA1 instances (15 of 100) | ✅ Converted to DIMACS |
| BKS values | ❌ Not loaded (no accessible source) |
| LOP_MA-EDM | ⏭ Skipped — DRMaciver used instead |
| Tiny synthetic test | ✅ All 8 algorithms passed |
| Smoke test (5 instances) | ✅ Passed |
| Full EXP5 | ✅ Launched in tmux session `mwfas_exp5_lolib` |
