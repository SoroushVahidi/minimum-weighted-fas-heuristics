# Test Expectation Change Log

| Test | Original expectation | Corrected expectation | Reason | Evidence |
|------|---------------------|----------------------|--------|----------|
| `test_integer_weights` | backward weight 3.0 | backward weight 1.0 | Only edge (1,2) is backward under scores {0:2,1:0,2:1} | Independent `reference_backward_weight` |
| `test_scc_scoring` | SCC backward contribution 3.0 | contribution 5.0 | Only (0,1) with w=5 is backward under rank {0:2,1:0,2:1} | Manual edge/rank check |
| `test_lrta_*` helpers | unpack 7 values from `local_ratio_fas_fast` | unpack 6 values | API returns `(removed, U, V, W0, active, adj)` | `src/mwfas/lrta.py` return statement |
| `test_safe_edge_closure_*` (first version) | `safe_tmp` nonempty on 4-cycle chain | acyclic FAS on source-edge graph 0→1,1↔2 | Original graph had no temporarily safe edges at start | WMSF `wmsf_removeArcs_scc` trace |
| `test_cli_smoke` env | `subprocess.os.environ` | `os.environ` | Test defect (invalid attribute) | Import error during interrupted run |

No production-code changes were made to satisfy these corrections.
