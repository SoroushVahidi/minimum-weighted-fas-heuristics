# Current repository state

| Item | Value |
|------|-------|
| Branch | `main` |
| HEAD | `80b3144d5fdbbe250faed8a4fe671dde2da76c89` |
| Main PDF pages | 45 |
| Main PDF SHA-256 | `4e6c2a3e7bfede24ec852027fa6e1b3f7a5ab7d396cb922ba3e9a9e1ab2ad9c6` |
| Tests | 90 collected; 90 passed; 1 skipped; 0 failed |
| Online Resource 1 | Present (`online_resource_1/`) |
| Manuscript backup | `paper_coap_pre_topo_audit_backup/` in this audit folder |

## Implementation map

| Function | File | Role |
|----------|------|------|
| `topo_order_active` | `src/mwfas/lrta.py` | Kahn + min-heap vertex id |
| `topo_order_active_restricted` | `src/mwfas/ipsns.py` | SCC-restricted Kahn |
| `compute_forward_backward` | `src/mwfas/evaluation.py` | Common objective |
| `exact_min_fas_dp` | `src/mwfas/exact.py` | Direct order optimization |
| Baseline order builders | `src/mwfas/baselines.py` | Direct orders |
| EXP4/5 runners | `experiments/exp4_*/run_exp4_benchmark.py` | Recompute bw from scores |
| EXP10 validators | `experiments/exp10_*/scripts/validate_*.py` | `objective_match` checks |
| Post-hoc extraction | `src/mwfas/topo_extraction.py` | EXP11 utilities (new) |

## Stored experiment artifacts

- Ranking CSVs per method/instance (EXP4 raw)
- Summary CSVs with `backward_weight`
- **Active/removed sets not stored** in committed summaries; reconstructible by rerunning FAS constructors
