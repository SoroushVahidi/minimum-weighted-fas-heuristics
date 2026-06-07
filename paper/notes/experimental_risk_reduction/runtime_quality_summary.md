# Runtime-Quality Summary — Sparse External Benchmark

Based on EXP4 raw results (standard 97-instance sparse benchmark, status=ok completed instances only). Lower BW = better.

| Algorithm | n completed | Mean BW | Median BW | Mean RT (s) | Median RT (s) |
|---|---:|---:|---:|---:|---:|
| IPSNS | 115 | 33,898.7 | 5,118.0 | 18.5439 | 0.0216 |
| LR-TA | 115 | 34,434.4 | 5,118.0 | 0.0685 | 0.0015 |
| WMSF | 115 | 35,916.3 | 5,118.0 | 1.1082 | 0.0012 |
| DRMacIver/FAS | 111 | 50,401.4 | 9,374.0 | 4.0023 | 0.1575 |
| igraph Eades | 115 | 85,354.9 | 12,414.0 | 0.0053 | 0.0007 |
| Weighted Eades | 115 | 88,641.4 | 12,414.0 | 0.0953 | 0.0007 |

**Note:** A true quality-vs-budget curve (varying IPSNS iteration limit) is not available from existing committed outputs and requires a dedicated future experiment.
