# LOP Baseline Feasibility Assessment

**Audit date:** 2026-06-11  
**Scope:** Assessment of Linear Ordering Problem (LOP) and dense pairwise-ordering baselines  
relevant to the COAP manuscript's LOLIB transfer test (EXP5).  
**Constraint:** Read-only; no software installed; no experiments run.

---

## Background: LOP vs MWFAS structural distinction

The manuscript makes an explicit structural distinction between two problem regimes:

1. **Sparse weighted digraph (MWFAS):** Most vertex pairs have no arc between them. Backward  
   weight is concentrated in a relatively small fraction of possible arcs. The IPSNS framework  
   is designed for this regime.

2. **Dense complete ordering (LOP):** Every ordered pair (i,j) carries a non-negative weight  
   representing evidence that i should precede j. All n(n-1) pairs are present. This is the  
   LOLIB benchmark format.

The MWFAS and LOP objectives are equivalent in principle (both minimize total backward arc  
weight in an ordering) but the input models are structurally different. Applying a LOP solver  
to a sparse DIMACS instance requires "completing" the missing pairs with weight 0, which  
changes the algorithmic landscape. Applying a sparse MWFAS heuristic to a complete pairwise  
matrix effectively ignores the dense coupling structure.

---

## 1. DRMacIver/FAS as LOLIB proxy (current EXP5)

### 1.1 What it does

DRMacIver/FAS is a matrix-based pairwise-ordering heuristic: its input model is a weight matrix  
W[i][j] representing the weight of placing i before j. This is structurally equivalent to the  
LOP input. EXP5 runs DRMacIver on 50 LOLIB instances and compares against IPSNS.

### 1.2 EXP5 results summary

| Method | N instances | N times best | Mean BW |
|---|---|---|---|
| DRMacIver/FAS | 50 | 45 | 571,687 |
| IPSNS | 50 | 5 | 582,354 |
| Mean gap (DRMacIver advantage) | — | — | 3.88% |

DRMacIver wins 45/50, IPSNS wins 5/50. Family breakdown: DRMacIver wins 24/25 SGB, 15/15 RandA1,  
6/10 IO. IPSNS wins 4/10 IO.

### 1.3 Assessment of DRMacIver as LOP proxy

**Appropriate but not ideal.** DRMacIver is not a purpose-built LOP solver; it is a general  
pairwise ordering heuristic. Purpose-built LOP solvers (LOP_MA-EDM, the methods in MRD12) may  
achieve substantially lower backward weights on LOLIB instances than DRMacIver. If DRMacIver  
can beat IPSNS by 3.88% on LOLIB, a purpose-built LOP solver might beat IPSNS by significantly  
more, strengthening the manuscript's scope-boundary claim without changing its direction.

**The manuscript correctly notes this limitation:**  
> "dedicated linear-ordering solvers such as LOP\_MA-EDM and the methods surveyed in [MRD12]  
> may achieve lower backward weights than DRMacIver/FAS on LOLIB"

This caveat is appropriately honest but may be insufficient if reviewers expect an actual  
LOP-native comparison for the LOLIB claims.

---

## 2. LOP_MA-EDM (memetic algorithm for LOP)

### 2.1 What it is

LOP_MA-EDM is a memetic algorithm designed specifically for the Linear Ordering Problem  
(referenced as `lop_ma_edm_repo` in the predecessor manuscript's bibliography, but **NOT in  
the COAP bibliography**). It uses a permutation representation with estimation of distribution  
and a memetic search.

**Availability in repository:**  
- No code present in the repository.  
- No install attempt recorded.  
- The `lop_ma_edm_repo` bibliography entry appears in the JOCO predecessor's `references.bib`  
  but NOT in `paper_coap/bibliography/references.bib`.  
  (See `VERIFIED_REFERENCE_REGISTER.csv` entry: "lop_ma_edm_repo — remove if not cited in  
  COAP text, minor cleanup")

### 2.2 Input/output model

LOP_MA-EDM is designed for LOP format: a complete weighted tournament matrix. Running it on  
sparse DIMACS instances requires completing the matrix with zeros for absent arcs.

### 2.3 Feasibility assessment

| Criterion | Assessment |
|---|---|
| Code availability | Unknown — possible public repository; not confirmed |
| Input format compatibility | Requires complete matrix; sparse instances need format conversion |
| Applicability to sparse benchmark | Structurally mismatched — adding zero-weight arcs to sparse instances changes the ordering problem |
| Applicability to LOLIB benchmark | High — LOLIB is the exact format LOP_MA-EDM was designed for |
| Required for submission | No — explicitly excluded in §5 with correct rationale |

### 2.4 Verdict

**Not feasible as a primary baseline** for the sparse benchmark due to structural mismatch.  
**Feasible but not required** for LOLIB. The manuscript's stated exclusion rationale is correct  
and defensible. If a reviewer specifically requests a LOP-native comparison on LOLIB, LOP_MA-EDM  
would be the appropriate response — but this would be a post-review addition, not pre-submission.

---

## 3. MRD12 methods (survey of linear ordering heuristics)

### 3.1 What it is

MRD12 (Marti, Reinelt, Duarte 2012) surveys local search, metaheuristic, and exact methods  
for the LOP. It references multiple implementations including tabu search, scatter search, and  
iterated greedy for LOP.

### 3.2 Assessment

| Criterion | Assessment |
|---|---|
| Code availability | Survey paper — individual implementations referenced but not bundled |
| Primary purpose | Dense complete ordering (LOP-native) |
| Applicability to sparse benchmark | Same structural mismatch as LOP_MA-EDM |
| Required for COAP | No |

### 3.3 Verdict

**Not required.** The manuscript correctly characterizes MRD12 as the reference class for dense  
linear ordering, not as a peer baseline on the sparse benchmark.

---

## 4. FLRS10 tournament local search

### 4.1 What it is

FLRS10 (Fernandez-Lapique-Rocha-Solis 2010) provides local search for weighted tournament  
feedback arc set. Designed for tournament graphs (every ordered pair present with non-negative  
weight), which overlaps with the LOLIB input model.

### 4.2 Assessment

| Criterion | Assessment |
|---|---|
| Code availability | Unknown — no code in repository |
| Weighted support | Yes (tournament weights) |
| Input format | Tournament (all pairs present) |
| Applicability to LOLIB | Yes — LOLIB instances are tournaments |
| Applicability to sparse benchmark | Structurally mismatched |
| Required for COAP | No |

### 4.3 Verdict

**Not required.** Cited correctly in §2 as related tournament method. If added to LOLIB  
comparison, it would strengthen the scope-boundary claim by showing another method that  
outperforms IPSNS on dense complete ordering. This is a post-submission enhancement only.

---

## 5. R igraph (R package)

### 5.1 What it is

R's igraph package provides `feedback_arc_set(graph, algo="approx_eades")`. It would provide  
an independent implementation of the Eades algorithm, similar to python-igraph.

### 5.2 Availability

R is not installed on the experimental machine (confirmed in `external_access_report.md`).

### 5.3 Verdict

**Not feasible.** Would require R installation. Incremental value is minimal — python-igraph  
Eades is already tested; R igraph Eades would provide similar results with different tie-breaking.

---

## 6. Summary: LOLIB comparison coverage

| Method | Dense-native? | Currently in EXP5? | Action |
|---|---|---|---|
| DRMacIver/FAS | Partial (matrix-based, not LOP-specialized) | Yes | Already used; note limitation in manuscript |
| IPSNS | No (sparse-native) | Yes | Already used; results show expected scope boundary |
| LOP_MA-EDM | Yes (LOP-specialized) | No | Optional post-submission addition for LOLIB only |
| MRD12 methods | Yes (LOP-specialized) | No | Cite as reference class; not required to run |
| FLRS10 | Yes (tournament-based) | No | Cite as related work; optional LOLIB addition |

---

## 7. Manuscript wording assessment

The following manuscript statement about LOLIB coverage is assessed:

> "dedicated linear-ordering solvers such as LOP_MA-EDM and the methods surveyed in [MRD12]  
> were not rerun for this study; they may achieve lower backward weights than DRMacIver/FAS on  
> LOLIB, reinforcing the conclusion that dense complete ordering instances favor methods  
> specialized for that regime."

**Assessment: SAFE.** This wording:
- Honestly acknowledges the gap
- Correctly predicts the direction of any future comparison (LOP-native methods would likely  
  beat DRMacIver, which already beats IPSNS)
- Does not overclaim on the LOLIB result
- Frames the result as a scope boundary rather than a failure

**One concern:** `lop_ma_edm_repo` is cited in this passage in the manuscript's §7 discussion.  
If `lop_ma_edm_repo` is NOT in the COAP bibliography (as indicated by the novelty audit), this  
is a citation error. Verify that the COAP bibliography contains the correct LOP_MA-EDM entry  
before submission. (See VERIFIED_REFERENCE_REGISTER.csv N-08.)

---

## 8. Overall verdict for LOP baselines

The current LOLIB treatment is **adequately scoped but explicitly limited**. The manuscript  
correctly:
- Uses DRMacIver as a practical dense-comparison proxy
- Acknowledges that purpose-built LOP solvers likely dominate
- Does not claim IPSNS is competitive on the dense LOP problem

**No new LOP baselines are required for submission.** If a reviewer requests one, LOP_MA-EDM  
on the 50 LOLIB instances would be the appropriate response.
