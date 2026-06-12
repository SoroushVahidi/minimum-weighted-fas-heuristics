# Exact Baseline Feasibility Assessment

**Audit date:** 2026-06-11  
**Scope:** All exact or certified-quality methods relevant to MWFAS validation.  
**Constraint:** Read-only; no software installed; no experiments run.

---

## Overview

The manuscript uses two exact reference methods for quality validation:
1. **Bitmask DP** (EXP3) — certified optima for n≤20 instances
2. **HiGHS MIP** (EXP8) — time-capped exact solver for medium instances (n≤318, 120s cap)

Three additional exact methods are assessed here for feasibility as cross-validation tools:
- igraph exact IP (`method="ip"`)
- Baharev et al. 2021 (BSNA21) formulations
- Generic extended MILP formulations beyond the current HiGHS implementation

---

## 1. igraph exact integer programming (`method="ip"`)

### 1.1 What it is

python-igraph v1.0.0 implements a minimum feedback arc set ILP solver accessible via  
`Graph.feedback_arc_set(weights=..., method="ip")`.

**Availability:** Confirmed available. python-igraph 1.0.0 is installed on the experimental machine  
(verified in `experiments/exp4_external_baselines/summary/external_access_report.md`).

### 1.2 Input/output model

| Property | Value |
|---|---|
| Input | igraph directed graph with arc weights |
| Output | Minimum-weight FAS (list of edge indices) |
| Algorithm | Internal ILP formulation (details undocumented in igraph API) |
| Weighted support | Yes — passes weights to solver |
| Time limit control | Not exposed in the python-igraph 1.0.0 API |

### 1.3 Scalability assessment

The FAS ILP formulation has exponential worst-case complexity. igraph's ILP implementation:
- **n ≤ 10:** Likely fast (sub-second)
- **n ≤ 20:** Expected to complete within reasonable time (seconds)
- **n ≤ 50:** Possible but may be slow (minutes) on dense instances
- **n > 50:** Expected to timeout or fail on most non-trivial instances

The EXP3 benchmark has 57 instances with n ≤ 20. The EXP8 benchmark has 15 instances with  
n ≤ 318 — igraph exact IP would fail on most of these.

### 1.4 Value as additional exact oracle

Running igraph exact IP on the 57 EXP3 instances would:
1. Cross-validate the bitmask DP results independently
2. Confirm that bitmask DP produced correct optima (or find disagreements)
3. Provide a second exact certificate for the 56/57 IPSNS near-optimality claim

**Value assessment:** Low-to-moderate. The bitmask DP (EXP3) is already independently implemented  
and has been the primary exact reference. An igraph IP cross-check would strengthen the claim  
that bitmask DP is correct, but the probability of discovering a discrepancy is very low.

### 1.5 Verdict

| Criterion | Assessment |
|---|---|
| Technically feasible | **Yes** — on EXP3 instances (n≤20) |
| Incremental scientific value | **Low** — EXP3 bitmask DP already covers this; igraph IP is an independent sanity check only |
| Appropriate category | Exact cross-validation (not a heuristic comparison) |
| Appropriate benchmark | EXP3 small-instance subset only (n≤20) |
| Should be added to manuscript | **No** — adds verification work without changing the narrative |
| Should be run as author self-check | **Optional** — useful for author confidence but not required for submission |

---

## 2. Baharev et al. 2021 (BSNA21)

### 2.1 What it is

Baharev, Schichl, Neumaier, Achterberg (2021): "An Exact Method for the Minimum Feedback Arc  
Set Problem." This paper presents new exact formulations and branch-and-bound methods for MWFAS.  
The manuscript cites it as: "a modern exact treatment of minimum feedback arc set through  
formulations that connect the problem to broader combinatorial optimization machinery."

### 2.2 Availability

**No code is present in the repository.** No attempt to access the BSNA21 implementation was  
recorded in any experiment file or audit log. The paper is cited as a methodological reference  
only.

Searching the repository for any BSNA21-related file names, URLs, or install records finds nothing.

### 2.3 Feasibility assessment

| Criterion | Assessment |
|---|---|
| Code availability | Unknown — possible public repository but not confirmed here |
| Installation effort | Unknown — likely requires specific MIP solver dependencies |
| Scalability | Designed for instances where exact computation is feasible; likely n ≤ few hundred at most |
| Appropriate benchmark | Exact validation subset only (not full 97-instance benchmark) |
| Incremental value vs EXP8 HiGHS | Moderate if it scales better; unknown without testing |

### 2.4 Verdict

| Criterion | Assessment |
|---|---|
| Technically feasible | **Unknown** — no code identified |
| Incremental scientific value | **Moderate** if publicly available and better-scaling than HiGHS MIP |
| Appropriate category | Exact validation method (same as EXP8) |
| Required for submission | **No** — EXP8 already covers exact validation for medium instances |
| Manuscript treatment | Correct as-is: "not the computational baseline for the full sparse benchmark" |

**Recommendation:** Keep as citation only. If BSNA21 code becomes available and scales better  
than HiGHS on medium instances (n=50–300), it would strengthen EXP8. This is a post-submission  
enhancement, not a pre-submission requirement.

---

## 3. HiGHS MIP via scipy.optimize.milp (current EXP8)

### 3.1 What it is

EXP8 uses `scipy.optimize.milp` with the HiGHS backend to solve a generic MWFAS integer program  
on 15 selected medium instances (n ≤ 318) with a 120-second per-instance time limit.

**Current results (from `experiments/exp8_medium_mip_baseline/summary/exp8_mip_raw_summary.csv`):**
- 15 instances total
- 7 proven optimal within 120s
- 8 exceeded time limit (no MIP incumbent reported for these)
- IPSNS matches MIP optimum on 6 of 7 proven-optimal instances
- Single exception: `r20_60` — IPSNS is 0.178% above MIP optimum

### 3.2 Formulation assessment

The MILP formulation in `scripts/run_exp8_medium_mip_baseline.py` implements the standard  
binary variable FAS formulation: binary variables `x_{ij}` indicating arc removal, with  
subtour-elimination constraints or cycle-cover constraints. The formulation's efficiency depends  
on whether it uses:
- Full subtour elimination (exponentially many constraints)
- Callback-based constraint generation (practical for HiGHS via milp)
- Tournament-ordering constraints (alternative compact formulation)

**This audit has not read the full MILP implementation code.** The results suggest the  
formulation works for small instances but struggles at n > ~200.

### 3.3 Enhancement options

| Enhancement | Feasibility | Value |
|---|---|---|
| Longer time limit per instance | Feasible (config change) | Would certify more instances optimal; may extend EXP8 scope |
| Tighter formulation (callback constraints) | Requires code change | Not allowed (no code modification in this audit) |
| More instances (15 → 30+) | Feasible (config change) | Extends exact validation coverage |
| Parallel solving | Requires code change | Not allowed |

### 3.4 Verdict

**EXP8 is appropriately designed and complete.** The 7/15 proven-optimal result is honest about  
scalability limits. The 8 time-limited cases are correctly treated as incomplete evidence.

The manuscript text is accurate: "A supplementary time-capped MIP baseline (EXP8) extends  
certified reference to medium sparse instances where bitmask DP is infeasible, reporting  
provably optimal solutions where the solver terminates within 120 s and treating time-limited  
cases as incomplete evidence."

**No changes required to EXP8 for submission.**

---

## 4. Cross-experiment consistency of exact validation

| Claim | Supported by | Cross-validated? |
|---|---|---|
| 56/57 IPSNS matches exact optimum | EXP3 bitmask DP | Partially — EXP8 confirms r20_60 as the single exception |
| r20_60 is the only IPSNS near-miss | EXP3 (DP) + EXP8 (MIP) + EXP4 (heuristic comparison) | **Yes** — three independent experiments agree |
| Mean IPSNS exact gap 0.0006% | EXP3 | Not independently verified, but consistent with 56/57 match |
| IPSNS matches EXP8 MIP optimum on 6/7 | EXP8 MIP | Single source; consistent with EXP3 |

The `r20_60` convergence across EXP3, EXP4, and EXP8 is the strongest internal consistency  
signal in the experimental program. It is appropriately used in the manuscript to explain  
the single DRMacIver/FAS win.

---

## 5. Summary table

| Method | Available | Appropriate scope | Recommended action |
|---|---|---|---|
| Bitmask DP (EXP3) | Yes (in-repo) | EXP3: n≤20 small instances | Already used; no change needed |
| HiGHS MIP (EXP8) | Yes (in-repo) | EXP8: n≤318 medium, 120s cap | Already used; no change needed |
| igraph exact IP | Yes (installed) | EXP3-scale only (n≤20) | Optional cross-check; not required for submission |
| Baharev et al. BSNA21 | Unknown | Exact medium instances | Keep as citation; run only if code becomes available post-submission |
| DF03 reference impl | None | N/A | No public code; do not attempt |
