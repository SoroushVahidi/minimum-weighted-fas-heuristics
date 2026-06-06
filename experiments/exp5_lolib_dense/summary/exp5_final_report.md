# EXP5 LOLIB Dense Benchmark — Final Report

**Generated:** 2026-06-06  
**Run time:** ~33 min (tmux session `mwfas_exp5_lolib`, 18:44–19:16 EDT)

---

## Repository

| Milestone | Commit |
|-----------|--------|
| Organization + cleanup | `fffa2dc` |
| EXP5 framework + converted instances | `5800d8e` |
| README status update | `86cb10b` |
| EXP5 results + audit (this commit) | _see below_ |

---

## Dataset

- **Archive:** LOLIB 2010 (`lolib_2010.zip`, 10.7 MB, from Marti's Dropbox)
- **Primary URL returned 404:** `grafo.etsii.urjc.es/optsicom/lolib.html` is GitHub Pages; ZIP files were never committed to the repo. See `summary/exp5_lolib_access_report.md`.
- **50 instances** converted to complete weighted DIMACS digraphs:

| Family | n | Count | Arc range |
|--------|---|-------|-----------|
| SGB | 75 | 25 | 2432–2550 arcs/instance |
| IO | 44–79 | 10 | 759–2705 arcs/instance |
| RandA1 | 100 | 5 | ~4900 arcs/instance |
| RandA1 | 150 | 5 | ~11050 arcs/instance |
| RandA1 | 200 | 5 | ~19700 arcs/instance |

**Conversion:** arc i→j has weight C[i,j]; diagonal ignored. Forward + backward = total off-diagonal weight.

---

## Baselines

| Algorithm | Type | Status |
|-----------|------|--------|
| lrta_full | Ours | ✅ Ran on all 50 |
| wmsf_seed | Ours | ✅ Ran on all 50 |
| ipsns_full | Ours | ✅ Ran on all 50 (200 iters) |
| borda_net_score | External | ✅ Ran on all 50 |
| weighted_eades | External | ✅ Ran on all 50 |
| random_multistart | External | ✅ Ran on all 50 (100 trials) |
| drmaciver_fas | External | ✅ Ran on all 50 |
| igraph_approx_eades | External | ✅ Ran on all 50 |
| LOP_MA-EDM | External | ⏭ Checked, not built — DRMaciver used instead |

---

## Validation

| Check | Result |
|-------|--------|
| Total rows | 400 (50 × 8) |
| Unique instances | 50 |
| Algorithms | 8 |
| Status OK | **400/400** |
| Errors | **0** |
| Timeouts | **0** |
| BW + FW = total_weight | **400/400 pass** (0 arithmetic failures) |
| Incumbent violations vs LR-TA | **0** |
| Incumbent violations vs WMSF | **0** |

---

## Main Results

### Overall (50 instances)

| Algorithm | Global Best | Mean BW | Mean Forward Ratio | Mean RT (s) |
|-----------|-------------|---------|-------------------|-------------|
| **drmaciver_fas** | **45/50** | **571,688** | **0.7373** | 1.01 |
| ipsns_full | 5/50 | 582,354 | 0.7255 | 37.9 |
| lrta_full | 2/50 | 582,948 | 0.7248 | 0.22 |
| wmsf_seed | 1/50 | 585,926 | 0.7180 | 0.19 |
| igraph_approx_eades | 0/50 | 659,570 | 0.6911 | 0.008 |
| weighted_eades | 0/50 | 675,235 | 0.6854 | 0.006 |
| random_multistart | 0/50 | 883,664 | 0.5782 | 0.023 |
| borda_net_score | 0/50 | 1,066,045 | 0.5659 | 0.004 |

**DRMaciver mean BW gap vs IPSNS: −3.88%** (DRMaciver has lower backward weight).

### Per-Family Breakdown

| Family | n | IPSNS best | DRMaciver best | IPSNS mean BW | DRMaciver mean BW |
|--------|---|-----------|----------------|---------------|-------------------|
| SGB | 75 | 1/25 | **24/25** | 1,048,056 | 1,036,085 |
| IO | 44–79 | **4/10** | 6/10 | 36,996 | 32,860 |
| RandA1 | 100–200 | 0/15 | **15/15** | 169,755 | 156,909 |

### IPSNS vs LR-TA (Incumbent Protection)

| Metric | Count |
|--------|-------|
| IPSNS strictly improves over LR-TA | 19/50 |
| IPSNS ties LR-TA | 31/50 |
| IPSNS violates LR-TA | **0/50** ✅ |
| IPSNS violates WMSF | **0/50** ✅ |

---

## Key Findings

1. **DRMaciver dominates LOLIB.** On all three families, DRMaciver wins more instances
   than any other algorithm. It wins 45/50 overall, achieving lower backward weight than
   IPSNS by 3.88% on average.

2. **IPSNS is competitive on IO.** On the 10 real-world IO instances (parliamentary votes,
   sports, trade data), IPSNS achieves global best on 4/10 compared to DRMaciver's 6/10.
   IPSNS mean BW on IO = 36,996 vs DRMaciver = 32,860 (~12% gap).

3. **IPSNS is not competitive on random dense instances (RandA1).** On all 15 n=100/150/200
   random instances, DRMaciver wins. IPSNS mean BW = 169,755 vs DRMaciver = 156,909 (~8% gap).

4. **IPSNS improves over LR-TA on 19/50 instances (38%).** The LNS phase does add value,
   particularly on IO instances. Incumbent protection holds on all 50 instances.

5. **IPSNS runtime on dense instances is high.** n=200: ~245s per instance with 200 iters,
   vs DRMaciver ~1.7s. For dense complete graphs, IPSNS is computationally expensive
   and does not improve proportionally over LR-TA.

---

## Manuscript Interpretation

LOLIB is a **dense complete weighted ordering** benchmark, not a sparse general-digraph
benchmark. DRMaciver's algorithm is tournament-native — it operates directly on score
differences in complete pairwise comparisons, which is exactly the LOLIB structure.
IPSNS's neighborhood search is designed for sparse directed graphs where SCC decomposition
gives a useful search structure.

**If DRMaciver beats IPSNS on LOLIB, this is a scope boundary, not a failure.**
The appropriate framing for the paper:

- **Primary claim (remains strong):** IPSNS dominates external baselines on sparse weighted
  DIMACS instances (EXP4: IPSNS best on 96/97, DRMaciver +21.6% mean BW).
- **Transfer test (EXP5):** On dense complete LOLIB instances, a tournament-native algorithm
  (DRMaciver) is stronger. IPSNS remains competitive on structured IO instances (4/10 best).
- **Scope statement for the paper:** "Our method is designed for weighted directed graphs and
  achieves near-optimal results on the sparse DIMACS benchmark. On dense complete tournament
  instances (LOLIB), algorithms specialized for the linear ordering problem structure outperform
  our approach, which reflects the different structural properties of these benchmarks."

This honest framing prevents overclaiming and strengthens the credibility of the paper.

---

## Next Step

1. Create `docs/baselines_and_datasets_references.md` — **done** in this audit pass.
2. Decide whether GNNRank is needed. Given EXP5's finding (DRMaciver is already a strong
   external baseline; GNNRank is a GNN-based method), GNNRank is optional. The paper's
   primary claim is for sparse DIMACS.
3. Finalize manuscript tables using EXP1b–EXP5 results.
