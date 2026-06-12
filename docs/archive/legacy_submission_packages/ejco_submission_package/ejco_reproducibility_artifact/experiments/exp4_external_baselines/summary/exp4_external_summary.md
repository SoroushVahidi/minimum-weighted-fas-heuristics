# EXP4 External Baselines Summary

Generated from: `exp4_raw_summary.csv`  
Total instances: 105  
Standard (non-negative): 97  
Negative-weight (excluded): peterson2, howard-max, stg0, gerez, peterson1, k3_3, ku, peterson  

## Availability

- **ipsns_full**: Available
- **lrta_full**: Available
- **wmsf_seed**: Available
- **borda_net_score**: Available
- **weighted_eades**: Available
- **random_multistart**: Available
- **igraph_approx_eades**: Available
- **drmaciver_fas**: Available

## Per-Algorithm Results (Standard Instances)

| Algorithm | Complete | Mean BW | Median BW | Mean FW Ratio | Mean RT (s) | N Best | IPSNS Improves | Mean Rel Gain (%) |
|-----------|----------|---------|-----------|---------------|-------------|--------|----------------|-------------------|
| ipsns_full | 97/97 | 37697.5052 | 5118.0 | 0.840773 | 21.9243 | 96 | 0 | 0.0 |
| lrta_full | 97/97 | 38326.9381 | 5118.0 | 0.840198 | 0.08 | 80 | 16 | 0.7133 |
| wmsf_seed | 97/97 | 40005.0619 | 5118.0 | 0.839857 | 1.3118 | 61 | 36 | 2.059 |
| borda_net_score | 97/97 | 512276.8144 | 12394.0 | 0.709586 | 0.0027 | 27 | 70 | 55.548 |
| weighted_eades | 97/97 | 99689.2784 | 6343.0 | 0.821114 | 0.1122 | 42 | 55 | 30.4783 |
| random_multistart | 97/97 | 1075258.4124 | 8860.0 | 0.65322 | 0.0269 | 42 | 55 | 49.7646 |
| igraph_approx_eades | 97/97 | 95920.1856 | 6120.0 | 0.818669 | 0.0059 | 40 | 57 | 30.5445 |
| drmaciver_fas | 93/97 | 53173.3763 | 5649.0 | 0.827824 | 3.9985 | 56 | 37 | 21.6076 |

## Notes

- **IPSNS improves**: number of instances where IPSNS backward weight < algorithm backward weight.
- **Mean rel gain**: mean (alg_bw - ipsns_bw) / alg_bw × 100% (only where alg_bw > 0).
- **N Best**: number of instances where this algorithm achieves the minimum backward weight.
- Negative-weight instances excluded from all statistics above.
- `fas_smartAE` and `R_igraph_eades` not run: see external_access_report.md.

