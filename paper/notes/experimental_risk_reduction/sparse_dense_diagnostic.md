# Sparse vs Dense Structural Diagnostic

## Sparse benchmark (EXP4 standard set)

- Instances: 101
- IPSNS wins / DRMacIver wins / Ties: 37 / 8 / 56
- Mean BW — IPSNS: 27,206.10, DRMacIver: 48,613.72
- Mean RT — IPSNS: 1.8270 s, DRMacIver: 3.6830 s

## Dense LOLIB benchmark (EXP5, 50 instances)

- Instances: 50
- IPSNS wins / DRMacIver wins / Ties: 5 / 45 / 0
- Mean BW — IPSNS: 582,353.56, DRMacIver: 571,687.14
- Mean RT — IPSNS: 37.9224 s, DRMacIver: 1.0122 s

### Per-family breakdown

| Family | n | IPSNS wins | DRM wins | Ties | Mean BW IPSNS | Mean BW DRM |
|---|---:|---:|---:|---:|---:|---:|
| SGB | 25 | 1 | 24 | 0 | 1,048,055.68 | 1,036,084.64 |
| RandA1 | 15 | 0 | 15 | 0 | 169,755.07 | 156,909.40 |
| IO | 10 | 4 | 6 | 0 | 36,996.00 | 32,860.00 |

**Interpretation:** On the sparse benchmark IPSNS wins more instances than DRMacIver/FAS. On dense LOLIB DRMacIver/FAS wins more instances. This supports the structural narrative: IPSNS is SCC-refinement oriented (sparse), DRMacIver/FAS is matrix-based pairwise-ordering (dense-friendly).
