# Coverage Report

**Tool:** pytest-cov 7.1.0  
**Command:** `PYTHONPATH=src python3 -m pytest tests/ --cov=mwfas --cov-report=term-missing`  
**Artifact:** `coverage.xml`

## Per canonical module

| Module | Statements | Miss | Cover |
|--------|------------|------|-------|
| `evaluation.py` | 9 | 0 | **100%** |
| `io.py` | 31 | 1 | **97%** |
| `exact.py` | 63 | 5 | **92%** |
| `lrta.py` | 193 | 26 | **87%** |
| `wmsf.py` | 306 | 47 | **85%** |
| `ipsns.py` | 586 | 201 | **66%** |
| **TOTAL (mwfas)** | **1299** | **390** | **70%** |

`baselines.py` (110 stmts) excluded from gate target — not canonical COAP core.

## Untested / low-coverage paths (priority)

### `ipsns.py` (~34% of statements missed)

- Legacy global WMSF seed path (`wmsf_removeArcs_global`, lines ~273–371)
- Restricted repair failure branches in some SCC shapes
- Verbose logging branches
- `wmsf_seed_mode="legacy"` CLI path

### `wmsf.py`

- Full end-to-end `wmsf_ranking_from_dimacs_fast` multi-SCC L1/L2 selection branches
- Stabilization swap branches (312–338) partially covered
- Fallback deletion loop (232–239)

### `lrta.py`

- DIMACS entry points `paper_fas_ranking_from_dimacs_fast` (329–346)
- Rare DFS parent-break paths (111, 115)

### `exact.py`

- Empty-graph DIMACS wrapper branch (125–130)
- DP reconstruction break (98)

### `io.py`

- Line 29: non-`a`/`c`/`p` line skip path

## Interpretation

Coverage is **diagnostic**. The gate prioritizes correctness-critical observable behavior on tiny graphs rather than line-percentage targets.
