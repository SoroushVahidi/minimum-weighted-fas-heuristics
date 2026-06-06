# EXP1 Core Benchmark Summary (corrected)

- **n_instances**: 105
- **n_instances_with_ipsns_result**: 105
- **n_ipsns_errors**: 0
- **ipsns_error_instances**: []
- **ipsns_improves_lrta**: 16
- **ipsns_improves_wmsf**: 36
- **incumbent_protection_violations**: 1
- **mean_gain_over_best_seed_bw**: 590.6667
- **median_gain_over_best_seed_bw**: 0.0
- **mean_relative_gain_pct**: 0.398
- **median_relative_gain_pct**: 0.0
- **note_duplicates**: 18 instances appeared twice in benchmark_instances_found_all.txt (overlapping source lists); first occurrence kept.
- **note_gr10**: gr10 bw(IPSNS=58839) > bw(standalone WMSF=58481) is NOT a true violation. IPSNS internal WMSF seed=58839 (L2-only, no stabilize); standalone WMSF also tries L1 and runs full stabilize pipeline. The incumbent protection guarantee (output <= best internal seed) holds: 0 violations.
- **note_gr00_gr7**: gr00 and gr7 are empty graphs (n=0, m=0). IPSNS algorithm returned bw=0 correctly. A ZeroDivisionError in the reporting print statement (fw/total_w, ipsns.py:787) prevented the result from being recorded in EXP1. Fixed: guard added. Corrected values: bw=0 for all algorithms.

Raw summary: `experiments/exp1_core_benchmark/summary/exp1_raw_summary.csv`
Paper summary: `experiments/exp1_core_benchmark/tables/exp1_core_benchmark_paper_summary.csv`