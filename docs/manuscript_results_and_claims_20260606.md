# Manuscript Results and Claim Boundaries

**Date:** 2026-06-06  
**Repository:** `SoroushVahidi/minimum-weighted-fas-heuristics` (private)  
**Final HEAD:** `e5b5b96`

---

## Current Repository State

| Field | Value |
|-------|-------|
| HEAD commit | `e5b5b96` |
| Branch | `main` |
| Completed experiments | EXP1b, EXP2, EXP3, EXP4, EXP5 |
| Clean working tree | Yes (as of 2026-06-06) |
| Reproducibility | All committed CSVs/JSONs are generated from committed scripts + committed DIMACS/LOLIB data |
| Repo visibility | **Private** — must be made public before or upon submission |
| Large/raw files | Gitignored (`raw/`, `logs/`, `downloads/`, `external_tools/`) |

---

## Experimental Pillars

### Pillar 1: Sparse Weighted Graph-Benchmarks

**Experiments:** EXP1b (3-algorithm internal), EXP4 (8-algorithm external comparison)  
**Dataset:** `alidasdan/graph-benchmarks` — 105 unique DIMACS `.d` instances  
**Standard subset:** 97 non-negative-weight instances (8 negative-weight excluded)

This is the **primary benchmark** and supports the paper's main claim. The instances
are real-world weighted directed graphs (circuits, dependency graphs, combinatorial
instances) — not synthetic random graphs.

**EXP1b key numbers (105 instances, internal):**
- IPSNS ≥ LR-TA on all 105 (0 incumbent violations vs LR-TA)
- IPSNS ≥ WMSF on all 105 (0 incumbent violations vs WMSF)
- IPSNS strictly improves over LR-TA on 16/105 instances
- IPSNS strictly improves over WMSF on 36/105 instances
- Mean relative gain over best seed: 0.42%
- Mean IPSNS runtime: 20.2s; mean LR-TA: 0.074s; mean WMSF: 1.24s

**EXP4 key numbers (97 standard instances, 8 algorithms):**

| Algorithm | Mean BW | Median BW | n_best | vs IPSNS mean BW |
|-----------|---------|-----------|--------|-----------------|
| **IPSNS** | **37,698** | 5,118 | **96/97** | — |
| LR-TA | 38,327 | 5,118 | 80/97 | +0.71% |
| WMSF | 40,005 | 5,118 | 61/97 | +2.06% |
| DRMaciver | 53,173 | 5,649 | 56/97 | +21.6% |
| igraph Eades | 95,920 | 6,120 | 40/97 | +30.5% |
| Weighted Eades | 99,689 | 6,343 | 42/97 | +30.5% |
| Borda | 512,277 | 12,394 | 27/97 | +55.5% |
| Random (100) | 1,075,258 | 8,860 | 42/97 | +49.8% |

Only loss for IPSNS: `r20_60` — DRMaciver wins by 3 units (0.18%).

**Allowed claim:**
> On standard non-negative sparse weighted graph-benchmarks, IPSNS outperforms all
> tested internal and external baselines and achieves the global minimum backward
> weight on 96/97 standard instances, with 0 incumbent-protection violations guaranteed.

**Not allowed:**
> IPSNS is universally state-of-the-art for all FAS/LOP instances.

---

### Pillar 2: Exact Small-Instance Validation

**Experiment:** EXP3  
**Dataset:** `alidasdan/graph-benchmarks`, n ≤ 20 subset  
**Standard subset:** 57 non-negative-weight instances

**Key numbers:**

| Algorithm | n_optimal / 57 | % optimal | Mean gap from optimal |
|-----------|---------------|-----------|----------------------|
| **IPSNS** | **56/57** | **98.2%** | **0.0006%** |
| LR-TA | 55/57 | 96.5% | 0.059% |
| WMSF | 51/57 | 89.5% | 0.096% |

Only near-miss for IPSNS: `r20_60` (n=20, gap 0.03%).  
This is the same instance DRMaciver beats IPSNS on in EXP4.

Exact solver: bitmask DP (n ≤ 20); validated against exact optimal.

**Allowed claim:**
> On small non-negative instances where exact optimization is feasible, IPSNS is
> near-optimal: optimal on 56/57 standard instances with a mean gap of 0.0006%.

**Not allowed:**
> IPSNS has an approximation guarantee or is always optimal.

---

### Pillar 3: Ablation Study

**Experiment:** EXP2  
**Dataset:** 10 representative instances from `alidasdan/graph-benchmarks`  
**Variants:** 8 (lr_no_addback, lrta_full, wmsf_seed, best_seed_no_lns,
ipsns_50iters, ipsns_100iters, ipsns_full, ipsns_no_scc_priority)

**Key numbers (mean BW over 10 instances):**

| Variant | Mean BW | Notes |
|---------|---------|-------|
| lr_no_addback | 4525.1 | No add-back phase |
| lrta_full | 4271.5 | Add-back: **−5.9%** vs no add-back |
| wmsf_seed | 4332.5 | WMSF only |
| best_seed_no_lns | 4271.5 | Best of LR-TA/WMSF, no LNS |
| ipsns_50iters | 4239.2 | **−0.75%** vs lrta_full |
| ipsns_100iters | 4239.2 | Converged at 50 iters |
| ipsns_full (200) | 4239.2 | Converged at 50 iters |
| ipsns_no_scc_priority | 4239.1 | Negligible SCC priority effect |

The add-back phase is the dominant contributor (−5.9%).
IPSNS LNS provides an additional −0.75% gain.
SCC priority has negligible effect on this 10-instance subset.

**Allowed claim:**
> EXP2 supports the contribution of the topological add-back phase (−5.9% mean BW
> reduction) and the incumbent-protected refinement step (additional −0.75%).

**Not allowed:**
> All design choices are universally optimal or generalize beyond this 10-instance subset.
> SCC priority is definitively unnecessary.

---

### Pillar 4: Dense LOLIB Transfer Test

**Experiment:** EXP5  
**Dataset:** LOLIB 2010 — 25 SGB (n=75), 10 IO (n=44–79), 15 RandA1 (n=100/150/200)  
**Note:** LOLIB instances are **dense complete tournaments**, fundamentally different from
the sparse DIMACS benchmark. EXP5 is a transfer/generalization test, not the primary claim.

**Key numbers (50 instances, 8 algorithms):**

| Algorithm | Mean BW | n_best / 50 | Notes |
|-----------|---------|------------|-------|
| **DRMaciver** | 571,688 | **45/50** | Tournament-native; −3.88% vs IPSNS |
| **IPSNS** | 582,354 | 5/50 | 4 IO + 1 SGB |
| LR-TA | ~582,948 | 2/50 | — |
| WMSF | ~585,926 | 1/50 | — |

Per-family breakdown:

| Family | n | IPSNS best | DRMaciver best |
|--------|---|-----------|----------------|
| SGB (n=75) | 25 | 1/25 | 24/25 |
| IO (n=44–79) | 10 | 4/10 | 6/10 |
| RandA1 (n=100–200) | 15 | 0/15 | 15/15 |

IPSNS has 0 incumbent violations (0 vs LR-TA, 0 vs WMSF) on all 50 instances.
400/400 algorithm runs completed, 0 errors.

**Why DRMaciver wins:** DRMaciver uses a tournament-specialized algorithm. IPSNS
uses LNS over the full SCC graph, which does not exploit tournament structure and
converges near the LR-TA seed on complete dense graphs.

**Allowed claim:**
> LOLIB shows IPSNS transfers reasonably as a general weighted digraph heuristic but
> is not a dense-native LOP state-of-the-art method. Incumbent protection holds
> (0 violations). IPSNS is competitive on structured IO instances (4/10 best).

**Not allowed:**
> IPSNS beats dense-native ordering solvers on complete dense LOP benchmarks.

---

## Final Paper Positioning

### Option A: Computers & Industrial Engineering (CAIE)

**Fit:** Strong. CAIE publishes computational heuristic studies for combinatorial
optimization in industrial/engineering contexts. Weighted ordering, precedence-conflict
repair, and sparse directed decision structures are directly relevant application areas.

**Required framing:** Emphasize practical applications — scheduling, circuit layout,
dependency resolution, tournament seeding. The methodology is the contribution; the
experimental validation is sufficient for CAIE standards.

**Risk:** Lower reviewer expectations for approximation theory. Likely reviewers from
OR/IE with practical focus.

### Option B: Computers & Operations Research (C&OR)

**Fit:** Moderate-to-strong. C&OR publishes heuristic + computational studies for
combinatorial problems, but reviewers may request stronger baseline comparison,
theoretical analysis, or more diverse benchmarks.

**Required framing:** Emphasize the mathematical structure (local-ratio, SCC
decomposition, LNS) and the framework's reproducibility. Would benefit from
DRMaciver multi-restart comparison or GNNRank inclusion.

**Recommendation:** **CAIE as primary target.** The experimental portfolio is solid
for CAIE. Switch to C&OR only if:
- GNNRank comparison is added, OR
- A theoretical gap bound is derived for LR-TA, OR
- The LOLIB/dense generalization story becomes substantially stronger.

---

## Recommended Titles

1. **"A Reproducible Local-Ratio and SCC-Refinement Framework for Weighted Ordering Problems in Directed Graphs"**
   — CAIE-compatible; emphasizes framework and reproducibility; avoids overclaiming.

2. **"Incumbent-Protected SCC Refinement for Minimum Weighted Feedback Arc Set and Weighted Ordering"**
   — More technical; highlights the algorithmic guarantee; good for C&OR if theory is added.

3. **"Computational Heuristics for Weighted Directed Ordering via Local Ratio and SCC-Based Refinement"**
   — Descriptive; broad audience; CAIE-friendly.

4. **"A Reproducible Framework for Resolving Cyclic Weighted Ordering Constraints in Directed Graphs"**
   — Application-framed; highlights precedence-conflict interpretation; strong for CAIE.

5. **"Engineering Local-Ratio and SCC-Local Search for Minimum Weighted Feedback Arc Set"**
   — Engineering-focused; CAIE fit; "engineering" signals implementation-heavy contribution.

---

## Main Manuscript Tables

| # | Table | Source | Caption suggestion |
|---|-------|--------|--------------------|
| 1 | Algorithm components and guarantees | (manual) | "Overview of algorithm components, runtime complexity, and guaranteed invariants" |
| 2 | External baseline comparison (EXP4) | `experiments/combined/tables/manuscript_table_external_sparse.csv` | "Comparison on 97 standard non-negative sparse instances (EXP4)" |
| 3 | Exact small-instance validation (EXP3) | `experiments/combined/tables/manuscript_table_exact_small.csv` | "Near-optimality on 57 small instances validated against exact DP (EXP3)" |
| 4 | Ablation study (EXP2) | `experiments/combined/tables/manuscript_table_ablation.csv` | "Component ablation on 10 representative instances (EXP2)" |
| 5 | LOLIB dense scope test (EXP5) | `experiments/combined/tables/manuscript_table_lolib_dense.csv` | "Transfer test on 50 LOLIB dense tournament instances (EXP5)" |

**Appendix tables (optional):**
- Per-instance raw results (EXP4)
- Full EXP1b per-instance IPSNS gain table

---

## Figures to Create Later

1. **Bar chart:** Mean BW relative to IPSNS on EXP4 (8 algorithms, 97 instances)
   — log scale if needed; shows dominance of IPSNS.

2. **Win count chart:** EXP4 n_best per algorithm (bar chart or stacked).

3. **Exact gap histogram (EXP3):** Distribution of IPSNS gap from optimal across 57 instances
   — nearly all at zero, one small outlier (r20_60).

4. **LOLIB per-family comparison:** DRMaciver vs IPSNS mean BW by family (SGB/IO/RandA1).
   — makes scope boundary visually clear.

5. **Convergence/iteration plot (EXP2):** IPSNS mean BW vs number of iterations
   — shows convergence at ~50 iterations; justifies iteration count choice.

---

## Reviewer Risk Register

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Local-ratio novelty** | Reviewer notes local-ratio is prior art (Bar-Yehuda et al.) | Clearly state local-ratio is prior art; claim novelty in the topological add-back phase and IPSNS framework. Cite Bar-Yehuda explicitly. |
| **Heuristic without theory** | Reviewer asks for approximation ratio or formal bound | Acknowledge heuristic nature; cite IPSNS incumbent protection as the formal guarantee provided. Note exact bitmask DP is used for empirical validation (EXP3). |
| **Baseline sufficiency** | Reviewer requests GNNRank or more recent learning-based methods | Add optional GNNRank comparison as supplementary, or explicitly scope the paper to classical heuristics and note neural methods as future work. |
| **Dense LOLIB weakness** | Reviewer points to EXP5 where DRMaciver beats IPSNS | Frame EXP5 proactively as a scope-defining transfer test. State clearly that IPSNS targets sparse digraphs; DRMaciver is tournament-native. Do not hide the result. |
| **Dataset scope** | Reviewer asks for synthetic or larger-scale instances | Note all instances are public, well-established benchmarks. Acknowledge scale limit (n ≤ 30K for sparse); EXP5 adds dense n=200 instances. |
| **Reproducibility/private-repo** | Reviewer cannot verify code | Make repository public upon submission. Provide DOI (Zenodo release). Include code availability statement. |
| **WMSF novelty** | WMSF is a reimplementation of paper049 | Explicitly state WMSF is a baseline/seed (not a novel contribution). Its value is as a seed for IPSNS. |

---

## Pre-Submission Checklist

- [x] EXP1b complete (105 instances, 0 violations)
- [x] EXP2 complete (ablation, 8 variants)
- [x] EXP3 complete (exact validation, 56/57 optimal)
- [x] EXP4 complete (97 standard instances, 8 algorithms)
- [x] EXP5 complete (50 LOLIB instances, 0 errors)
- [x] Consolidated tables: `experiments/combined/tables/`
- [x] Results digest: `experiments/combined/summary/`
- [ ] Manuscript draft started
- [ ] Figures generated
- [ ] Repo made public
- [ ] Zenodo/GitHub release with DOI
- [ ] Code and data availability statement added to manuscript
- [ ] Claim boundaries checked against this document
