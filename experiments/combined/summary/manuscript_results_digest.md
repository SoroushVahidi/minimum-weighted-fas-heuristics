# Manuscript Results Digest

**Generated:** 2026-06-06  
**HEAD commit:** e5b5b96  
**Experiments complete:** EXP1b, EXP2, EXP3, EXP4, EXP5

---

## Experimental Pillars

### Pillar 1: Sparse weighted graph-benchmarks

**Experiments:** EXP1b, EXP4  
**Dataset:** alidasdan/graph-benchmarks (DIMACS .d)  
**N instances:** {'EXP1b': 105, 'EXP4': 97}  

**Main result:** IPSNS achieves global minimum BW on 96/97 standard non-negative instances. DRMaciver (external) is closest competitor at +21.6% mean BW. IPSNS has 0 incumbent-protection violations on 105 EXP1b instances.

**Allowed claim:** On standard non-negative sparse weighted graph-benchmarks, IPSNS outperforms all tested internal and external baselines and achieves the global minimum backward weight on 96/97 standard instances.

**Not allowed:** IPSNS is universally state-of-the-art for all FAS/LOP instances.

### Pillar 2: Exact small-instance validation

**Experiments:** EXP3  
**Dataset:** alidasdan/graph-benchmarks, n<=20 subset  
**N instances:** {'EXP3': 57}  

**Main result:** IPSNS achieves exact optimality on 56/57 (98.2%) standard non-negative instances. Only near-miss: r20_60 (n=20), 0.0006% mean relative gap. LR-TA: 55/57 (96.5%), WMSF: 51/57 (89.5%).

**Allowed claim:** On small non-negative instances where exact optimization is feasible, IPSNS is near-optimal (98.2% exact, mean gap 0.0006%).

**Not allowed:** IPSNS has an approximation guarantee or always reaches optimum.

### Pillar 3: Ablation study

**Experiments:** EXP2  
**Dataset:** alidasdan/graph-benchmarks (10 representative instances)  
**N instances:** {'EXP2': 10}  

**Main result:** Add-back phase reduces mean BW by 5.9% (lr_no_addback 4525.1 -> lrta_full 4271.5). IPSNS full reduces further by 0.75% (lrta_full 4271.5 -> ipsns_full 4239.2). Convergence reached at 50 iterations (ipsns_50iters == ipsns_full on this subset). SCC priority has negligible effect on 10-instance subset.

**Allowed claim:** EXP2 supports the contribution of the add-back phase (−5.9% BW) and incumbent-protected refinement (−0.75% further).

**Not allowed:** All design choices are universally optimal or generalize beyond the 10-instance subset.

### Pillar 4: Dense LOLIB transfer test

**Experiments:** EXP5  
**Dataset:** LOLIB 2010 (SGB n=75, IO n=44-79, RandA1 n=100/150/200)  
**N instances:** {'EXP5': 50}  

**Main result:** DRMaciver (tournament-native) achieves global best on 45/50 instances. IPSNS best on 5/50 (4 IO + 1 SGB). DRMaciver mean BW 571,688 vs IPSNS 582,354 (−3.88% advantage for DRMaciver). IPSNS retains 0 incumbent violations. Per-family: SGB DRMaciver 24/25, IO IPSNS 4/10 vs DRMaciver 6/10, RandA1 DRMaciver 15/15. Scope boundary: IPSNS is not a dense-native LOP algorithm.

**Allowed claim:** LOLIB shows IPSNS transfers reasonably as a general weighted digraph heuristic but is not a dense-native LOP state-of-the-art method. Incumbent protection holds. IPSNS is competitive on structured IO instances (4/10).

**Not allowed:** IPSNS beats dense-native ordering solvers on complete dense LOP benchmarks.

---

## Strongest Allowed Claim

> On standard non-negative sparse weighted directed graph benchmarks (alidasdan/graph-benchmarks), IPSNS achieves the global minimum backward weight on 96/97 instances, surpassing all tested external baselines including DRMaciver (+21.6% mean BW), with guaranteed non-worsening against both LR-TA and WMSF seeds.

## Strongest Not-Allowed Claim

> IPSNS is universally state-of-the-art for all weighted feedback arc set or linear ordering problem instances, including dense tournament benchmarks.

## Scope Boundary

> All claims apply to non-negative-weight instances only. On dense LOLIB tournaments (EXP5), DRMaciver (tournament-native) outperforms IPSNS overall. IPSNS is designed for sparse directed graphs; EXP5 is a scope test, not the primary claim.

---

## Source Files

- `experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json` [✓]
- `experiments/exp1b_core_benchmark_full_wmsf_seed/tables/exp1b_core_benchmark_paper_summary.csv` [✓]
- `experiments/exp2_ablation/summary/exp2_ablation_stats.json` [✓]
- `experiments/exp2_ablation/tables/exp2_ablation_summary.csv` [✓]
- `experiments/exp3_exact_small/summary/exp3_exact_stats.json` [✓]
- `experiments/exp3_exact_small/tables/exp3_exact_summary.csv` [✓]
- `experiments/exp4_external_baselines/summary/exp4_external_stats.json` [✓]
- `experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv` [✓]
- `experiments/exp5_lolib_dense/summary/exp5_lolib_stats.json` [✓]
- `experiments/exp5_lolib_dense/tables/exp5_lolib_paper_summary.csv` [✓]
