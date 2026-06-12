# EXP4 External Baseline Access Report

Generated: 2026-06-06  
Host: linux (Ubuntu 22.04+, x86_64)  
Python: checked via `python3 -c "import <pkg>"`  
R: checked via `which R`

---

## Python Package Availability

| Package | Check Command | Status | Version/Notes |
|---------|--------------|--------|---------------|
| igraph | `import igraph` | **Available** | 1.0.0 (python-igraph) |
| networkx | `import networkx` | Available | (standard install) |
| pandas | `import pandas` | Available | (standard install) |
| numpy | `import numpy` | Available | (standard install) |
| scipy | `import scipy` | Available | (standard install) |
| networkit | `import networkit` | **Not installed** | `ModuleNotFoundError` |

---

## R igraph

```
which R  →  (empty / not found)
```

**Status: R not installed on this machine.**  
R igraph (`feedback_arc_set(..., algo="approx_eades")`) cannot be used.  
This path is documented-only for EXP4.

---

## igraph (Python, python-igraph v1.0.0)

**URL:** https://github.com/igraph/python-igraph  
**Access command:** `pip install python-igraph` (already installed)  
**Version:** 1.0.0  
**Commit/tag:** v1.0.0  
**Weighted directed support:** Yes — `Graph.feedback_arc_set(weights=es["weight"], method="eades")`  
**Test performed:**

```python
import igraph as ig
g = ig.Graph(n=3, directed=True)
g.add_edges([(0,1),(1,2),(2,0)])
g.es["weight"] = [5.0, 4.0, 3.0]
fas_ids = g.feedback_arc_set(weights=g.es["weight"], method="eades")
# Returns [2]  (edge 2→0 with weight 3 — correct minimum FAS)
g2 = g.copy()
g2.delete_edges(fas_ids)
order = g2.topological_sorting()
# Returns [0, 1, 2] — optimal ordering
```

**Result:** PASS. Returns correct FAS for 3-cycle.  
**EXP4 usage:** Yes — `igraph_approx_eades` baseline via `run_igraph_eades.py`.  
**Notes:** Only `method="eades"` tested. The `method="ip"` (exact ILP) is available but
belongs to exact comparisons (EXP3-style), not heuristic EXP4.

---

## DRMacIver / Feedback-Arc-Set

**URL:** https://github.com/DRMacIver/Feedback-Arc-Set  
**Clone target:** `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/`  
**Commit:** `16ff24a92fde886e58819180a9fe686e60991c5c`  
**License:** Not explicitly stated in repo (source available, "use as-is").  
**Build command:** `make fas`  
**Build result:** SUCCESS — compiled `fas` binary (36 KB)  
**Access command:** `echo "3\n0 1 5\n1 2 4\n2 0 3" | ./fas`  
**Test output:**
```
Score: 9.000000
Optimal ordering: 0 1 2
```
**Weighted directed support:** Yes — input is a weighted matrix W[i][j] = "evidence i < j",
exactly matching MWFAS arc weight convention.  
**Input format:** `n` on first line, then `i j x` triples (0-indexed, x ≥ 0).  
**Output format:** `Score: X\nOptimal ordering: a b c [d e] || ...`
(brackets = ties, `||` = condorcet partition separator)  
**EXP4 usage:** Yes — `drmaciver_fas` baseline via `run_drmaciver_fas.py`.  
**Notes:**  
- Binary is deterministic (fixed random seed at each run via `srand(time|pid)`? No:
  source uses `srand(time(NULL) ^ getpid())` — technically non-deterministic across runs
  but the algorithm appears to be deterministic in practice for typical instances).
- Algorithm is O(n²) in number of items; practical for all EXP4 instances.
- Result is locally optimal (no single-element move improves it).

---

## fas-smartAE

**URL:** https://github.com/jurepustos/fas-smartAE/  
**Clone target:** `experiments/exp4_external_baselines/external_tools/fas-smartAE/`  
**Commit:** `e6b998f321a5040c3615a2410ca786fe01ad7af3`  
**License:** MIT (LICENSE file present)  
**Requirements:** `networkit` Python package  
**networkit status:** **Not installed** (`ModuleNotFoundError: No module named 'networkit'`)  
**Weight support inspection:**  
- `main.py` uses `NetworkitGraph` (from `networkit_fas.py`) and `FASGraph`  
- The main algorithm in `feedback_arc_set.py` uses `SortedList`; no weight parameter  
  visible in the primary API  
- Appears to be an **unweighted** FAS heuristic (minimizes arc count, not arc weight)  
**EXP4 usage:** **Not used for weighted EXP4.**  
**Reason:**  
  1. `networkit` is not installed  
  2. The algorithm appears unweighted; forcing it on our weighted problem would be unfair  
**Documentation note:** Listed in baseline registry as "documentation-only" for EXP4.
  Could be used as a future unweighted-projection baseline with `networkit` installed.

---

## Summary Table

| Resource | URL | Status | Weighted | Used in EXP4 | Reason if Not Used |
|----------|-----|--------|----------|--------------|--------------------|
| python-igraph | https://github.com/igraph/python-igraph | Available v1.0.0 | Yes | **Yes** | — |
| R igraph | https://r.igraph.org/ | R not installed | N/A | No | R not present |
| DRMacIver/FAS | https://github.com/DRMacIver/Feedback-Arc-Set | Built, tested | Yes | **Yes** | — |
| fas-smartAE | https://github.com/jurepustos/fas-smartAE/ | Cloned, networkit missing | No | No | Unweighted; networkit unavailable |

---

## Manual Setup Needed (if future use required)

- **R igraph**: Install R (`sudo apt install r-base`) then `install.packages("igraph")` in R.
- **fas-smartAE**: `pip install networkit` (requires C++ build tools, may need `cmake`).
- **fas-smartAE weighted**: Would require significant modification to the codebase.
