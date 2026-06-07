# IPSNS Gain-Feature Correlation

- Sparse instances with features: 103
- Instances with IPSNS vs LR-TA gain: 103
- Instances with IPSNS vs DRMacIver/FAS gain: 101

All improvements are IPSNS BW minus baseline BW (sign-flipped: positive = IPSNS achieves lower backward weight).

## Spearman correlations with IPSNS gain over LR-TA

| Feature | n | Spearman r | p |
|---|---:|---:|---:|
| n (vertices) | 103 | 0.5338 | <0.001 |
| m (arcs) | 103 | 0.5346 | <0.001 |
| density | 103 | -0.5062 | <0.001 |
| largest SCC fraction | 103 | -0.0777 | 0.4355 |
| fraction in nontrivial SCCs | 103 | -0.0538 | 0.5894 |
| fraction arcs internal to SCCs | 103 | -0.0349 | 0.7265 |
| n nontrivial SCCs | 103 | 0.2694 | 0.0059 |

## Spearman correlations with IPSNS gain over DRMacIver/FAS

| Feature | n | Spearman r | p |
|---|---:|---:|---:|
| n (vertices) | 101 | 0.7689 | <0.001 |
| m (arcs) | 101 | 0.7638 | <0.001 |
| density | 101 | -0.7625 | <0.001 |
| largest SCC fraction | 101 | -0.2180 | 0.0285 |
| fraction in nontrivial SCCs | 101 | -0.2437 | 0.0141 |
| fraction arcs internal to SCCs | 101 | -0.2393 | 0.0159 |
| n nontrivial SCCs | 101 | 0.6812 | <0.001 |

## IPSNS gain over LR-TA by SCC fraction quartile

| Group | n | Mean SCC frac | Mean gain | Median gain |
|---|---:|---:|---:|---:|
| Q1 (low SCC frac) | 25 | 0.0611 | 174.24 | 0.00 |
| Q2 | 25 | 0.4117 | 271.20 | 0.00 |
| Q3 | 25 | 0.8864 | 1,996.72 | 0.00 |
| Q4 (high SCC frac) | 28 | 1.0000 | 0.04 | 0.00 |
