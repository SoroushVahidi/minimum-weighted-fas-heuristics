# IPSNS Gain-Feature Correlation

- Sparse instances with features: 95
- Instances with IPSNS vs LR-TA gain: 95
- Instances with IPSNS vs DRMacIver/FAS gain: 93

All improvements are IPSNS BW minus baseline BW (sign-flipped: positive = IPSNS achieves lower backward weight).

## Spearman correlations with IPSNS gain over LR-TA

| Feature | n | Spearman r | p |
|---|---:|---:|---:|
| n (vertices) | 95 | 0.5413 | <0.001 |
| m (arcs) | 95 | 0.5426 | <0.001 |
| density | 95 | -0.5104 | <0.001 |
| largest SCC fraction | 95 | -0.1452 | 0.1605 |
| fraction in nontrivial SCCs | 95 | -0.1211 | 0.2425 |
| fraction arcs internal to SCCs | 95 | -0.0999 | 0.3353 |
| n nontrivial SCCs | 95 | 0.2423 | 0.0180 |

## Spearman correlations with IPSNS gain over DRMacIver/FAS

| Feature | n | Spearman r | p |
|---|---:|---:|---:|
| n (vertices) | 93 | 0.8495 | <0.001 |
| m (arcs) | 93 | 0.8446 | <0.001 |
| density | 93 | -0.8262 | <0.001 |
| largest SCC fraction | 93 | -0.5229 | <0.001 |
| fraction in nontrivial SCCs | 93 | -0.5687 | <0.001 |
| fraction arcs internal to SCCs | 93 | -0.5628 | <0.001 |
| n nontrivial SCCs | 93 | 0.6100 | <0.001 |

## IPSNS gain over LR-TA by SCC fraction quartile

| Group | n | Mean SCC frac | Mean gain | Median gain |
|---|---:|---:|---:|---:|
| Q1 (low SCC frac) | 23 | 0.1263 | 358.52 | 0.00 |
| Q2 | 23 | 0.4725 | 125.65 | 0.00 |
| Q3 | 23 | 0.9294 | 2,170.35 | 0.00 |
| Q4 (high SCC frac) | 26 | 1.0000 | 0.04 | 0.00 |
