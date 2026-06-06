# Paper Status — 2026-06-06

**Repository:** `SoroushVahidi/minimum-weighted-fas-heuristics` (private)  
**Current HEAD:** `a934037`

---

## Experimental Evidence (Complete)

| Experiment | Instances | Key finding | Status |
|---|---|---|---|
| **EXP1b** main benchmark | 105 | IPSNS ≥ LR-TA, IPSNS ≥ WMSF on all 105; 0 incumbent violations | ✅ Done |
| **EXP2** ablation | 10 | Add-back −5.9% BW; LNS −0.8% further; `ipsns_no_scc_priority` included | ✅ Done |
| **EXP3** exact small-instance | 57 standard | IPSNS 98.2% optimal; LR-TA 96.5%; WMSF 89.5% | ✅ Done |
| **EXP4** external baselines | 97 standard | IPSNS beats all: closest is DRMaciver (+21.6% mean BW) | ✅ Done |

---

## Remaining Before Manuscript

### Required

| Item | Notes |
|---|---|
| **EXP5 LOLIB benchmark** | ✅ Complete. 50 instances, 0 errors. DRMaciver wins 45/50; IPSNS wins 5/50 (competitive on IO family). Incumbent protection holds. See `experiments/exp5_lolib_dense/summary/exp5_final_report.md`. |
| **Final table consolidation** | Merge EXP1b, EXP2, EXP3, EXP4 into clean manuscript tables. Pending EXP5. |
| **Make repo public** | Must be done before or upon submission. |

### Optional / Nice-to-have

| Item | Notes |
|---|---|
| GNNRank comparison | GNN-based FAS baseline; requires setup. Low priority if EXP5 is strong. |
| Zenodo/GitHub release | Create a DOI-tagged release for citation. |

---

## Venue Direction

| Venue | Notes |
|---|---|
| **CAOR (primary)** | Computers & Operations Research — good fit for heuristic + computational study |
| **CAIE (secondary)** | Computers & Industrial Engineering — broader audience |

---

## Claim Boundaries

### What the paper claims
- **LR-TA** with Topological Add-Back achieves near-optimal solutions efficiently.
  The add-back phase is the novel contribution (prior work: local-ratio framework).
- **IPSNS** achieves guaranteed no-worsening against both seeds (incumbent protection)
  and finds high-quality solutions competitive with external tools.
- Experimental superiority over standard FAS baselines on the alidasdan benchmark set.

### What the paper does NOT claim
- Do **not** claim local-ratio as a novel contribution — it is prior art.
- Do **not** claim a new approximation ratio — IPSNS has no ratio guarantee.
- Do **not** claim exact optimality in general — only near-optimality on small instances (EXP3).
- Do **not** claim external baselines are official implementations — several are wrappers
  or adaptations (see `experiments/exp4_external_baselines/summary/external_access_report.md`).

### Scope constraint
- All standard claims apply to **non-negative-weight instances only**.
- Negative-weight instances (`k3_3`, `ku`, `peterson*`, `gerez`, `howard-max`, `stg0`)
  are **excluded** from all standard analysis and paper comparisons.
- WMSF is used as a seed and baseline — it is a reimplementation of paper049's pipeline,
  not a novel contribution.

---

## Pre-submission Checklist

- [x] EXP5 LOLIB completed
- [ ] Manuscript tables finalized
- [ ] Repo made public
- [ ] GitHub release/Zenodo DOI created
- [ ] Code and data availability statement added to manuscript
- [ ] All claim boundaries checked against the above

---

## EXP4 Key Numbers for Manuscript (97 Standard Instances)

| Algorithm | Mean BW | Median BW | Mean RT (s) | Global Best |
|---|---|---|---|---|
| **IPSNS** | **37,698** | 5,118 | 21.9 | **96/97** |
| LR-TA | 38,327 | 5,118 | 0.08 | 80/97 |
| WMSF | 40,005 | 5,118 | 1.31 | 61/97 |
| DRMaciver | 53,173 | 5,649 | 4.00 | 56/97 |
| igraph Eades | 95,920 | 6,120 | 0.006 | 40/97 |
| Weighted Eades | 99,689 | 6,343 | 0.11 | 42/97 |
| Borda | 512,277 | 12,394 | 0.003 | 27/97 |
| Random (100 restarts) | 1,075,258 | 8,860 | 0.027 | 42/97 |

Source: `experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv`
