# Runtime-Quality Summary — Sparse External Benchmark

Based on EXP4 raw results (standard 97-instance sparse benchmark, status=ok completed instances only). Lower BW = better.

| Algorithm | n completed | Mean BW | Median BW | Mean RT (s) | Median RT (s) |
|---|---:|---:|---:|---:|---:|
| IPSNS | 123 | 31,663.8 | 5,118.0 | 17.3378 | 0.0186 |
| LR-TA | 123 | 32,164.6 | 5,118.0 | 0.0641 | 0.0011 |
| WMSF | 123 | 33,550.1 | 5,118.0 | 1.0361 | 0.0012 |
| DRMacIver/FAS | 119 | 46,875.0 | 6,216.0 | 3.7334 | 0.1225 |
| igraph Eades | 123 | 79,740.8 | 7,114.0 | 0.0050 | 0.0007 |
| Weighted Eades | 115 | 88,641.4 | 12,414.0 | 0.0953 | 0.0007 |

**Note:** A true quality-vs-budget curve (varying IPSNS iteration limit) is not available from existing committed outputs and requires a dedicated future experiment.
