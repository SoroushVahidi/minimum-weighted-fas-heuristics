# Manuscript Positioning Recommendations

**Audit date:** 2026-06-11  
**Based on:** NOVELTY_AND_PRIOR_WORK_AUDIT.md, DF_VS_LRTA_OPERATIONAL_COMPARISON.md,
IPSNS_NOVELTY_AUDIT.md, RELATED_MANUSCRIPT_CONTRIBUTION_MATRIX.md, and code reading.

---

## 1. Disclosure language for the manuscript and cover letter

### 1.1 Cover letter — recommended disclosure paragraph

The following is recommended as a disclosure paragraph in the COAP cover letter:

---

*This manuscript unifies and extends three prior lines of work by the first author. An
earlier single-author manuscript, "Fast Local-Ratio Cycle Reduction with Topological Add-Back
for Weighted Feedback Arc Sets" (target: Journal of Combinatorial Optimization), presents the
LR-TA algorithm (Phase I local-ratio cycle reduction and Phase II topological add-back) with
a 33-instance experimental evaluation. A separate earlier manuscript, "Incumbent Protected SCC
Neighborhood Search for the Weighted Feedback Arc Set Problem" (target: Elsevier journal),
presents the IPSNS and WMSF-style algorithms with their own experimental evaluation.
A related preprint, Vahidi and Koutis (arXiv:2412.16181, December 2024), formulates ranking
from pairwise comparisons as a minimum weighted feedback arc set problem and proposes
combinatorial heuristics; its experimental results partially overlap with the benchmark suite
used here.*

*The present submission is distinguished from these predecessors by: (1) the unified framework
combining all three components under one theoretically grounded treatment; (2) four formal
propositions establishing feasibility, correctness, monotonicity, and termination (absent from
all predecessors); (3) a substantially expanded computational study comprising nine experiment
types including exact DP validation, a five-method external baseline comparison, a LOLIB dense
transfer test establishing explicit scope boundaries, a budget curve analysis, and an
application case study; and (4) a holdout parameter sensitivity study. Copies of the prior
manuscripts are attached as supplementary uploads per COAP editorial policy.*

---

### 1.2 Related work section — recommended positioning paragraph

The following can be inserted in §2 related work, replacing or augmenting the current
"Positioning relative to our prior work" note (if present):

---

*The present work builds on two predecessor manuscripts by the first author. The LR-TA
algorithm was previously presented in [REF-JOCO] in a single-algorithm study focusing on
Phase I local-ratio cycle reduction and Phase II topological add-back, evaluated on a 33-instance
benchmark. The IPSNS and WMSF-style seed algorithms were presented in [REF-ELSEVIER].
The present manuscript is the first unified treatment of all three components, and is the
first to provide formal correctness and complexity results (Propositions 1–4) for the
combined framework. arXiv:2412.16181 [REF-VK] treats ranking from pairwise comparisons as
MWFAS and is related in problem motivation; the present work targets general sparse weighted
directed graphs with a broader experimental scope and an explicit dense-ordering scope boundary.*

---

### 1.3 Contribution list — recommended revised paragraph

Replace the current contribution list item for LR-TA:

**Current (problematic if read as claiming novelty to COAP):**
> LR-TA is an engineered local-ratio seed with topological add-back...

**Recommended:**
> LR-TA, presented in a prior manuscript and here unified with formal guarantees, is an
> engineered local-ratio seed with topological add-back: iterative cycle-weight reductions
> build a feasible ordering, and a heavy-first arc-recovery phase using original arc weights
> reduces unnecessary deletions.

Replace the current IPSNS contribution item:

**Current:**
> IPSNS is an incumbent-protected SCC-local destroy-and-repair refinement...

**Recommended:**
> IPSNS, introduced in a prior manuscript and here formally analyzed for the first time,
> is an incumbent-protected SCC-local destroy-and-repair refinement that concentrates search
> on strongly connected components with positive backward contribution and accepts a candidate
> ordering only when the global backward weight strictly decreases.

Add a new contribution item for the formal analysis:

> This paper provides the first formal treatment of the unified framework: Propositions 1–4
> establish LR-TA feasibility and termination, correctness of the topological add-back
> shortcut, IPSNS incumbent monotonicity (no worsening relative to both seeds), and IPSNS
> termination. These are the primary new theoretical contributions.

---

## 2. Algorithm description corrections

### 2.1 Add-back ordering — required fix

In any algorithm description (pseudocode, theorem statement, or prose) referring to Phase II
add-back ordering:

**Must say:** "sorted by original arc weight, heaviest first"
**Must not say:** "sorted by residual weight" or "sorted by reduced weight"

Manuscript location to check: `sections/04_algorithmic_framework.tex` add-back description.

### 2.2 Topological-rank shortcut — required fix

**Must say (or equivalent):**
*"If rank(u) < rank(v), reinserting (u,v) cannot create a cycle and is accepted immediately.
Otherwise, a reachability test from v to u is performed; if v cannot reach u, the arc is
reinstated and the topological order is recomputed."*

**Must not say (or equivalent):**
- "if and only if rank(u) < rank(v)" (the iff is false)
- "(u→v) preserves acyclicity iff it is forward in the topological order" (false; forward
  is sufficient but backward may also be acyclic)

### 2.3 Destroy operation description — required fix

**Must say:** "two independent perturbations"
**Must not say:** "reactivates heavy backward arcs via the light edges blocking them"
or any language implying that Destroy A and Destroy B are causally linked.

---

## 3. Experimental claim language

| Benchmark result | Safe version | Version to avoid |
|---|---|---|
| 96/97 sparse instances best | "best observed backward weight among the evaluated methods on 96 of 97 standard nonneg sparse instances" | "state of the art"; "best known solution" |
| DRMacIver 21.6% worse | "DRMacIver is approximately 21.6% worse in mean backward weight on the evaluated sparse benchmark" | "DRMacIver represents the leading external method" |
| LOLIB: DRMacIver wins 45/50 | "on 50 dense LOLIB instances, DRMacIver/FAS obtains best observed backward weight on 45; proposed method on 5" | "performs comparably on dense ordering instances" |
| 56/57 exact optimal | "matches DP optimum on 56 of 57 small instances (n ≤ 20)" | "optimal on small instances" |
| Ablation: add-back reduces BW by 5.9% | "on the ablation subset, topological add-back reduces mean backward weight by 5.9% relative to Phase I alone" | "add-back is essential" or "5.9% improvement generalizes to all instances" |

---

## 4. Formal analysis — scope recommendations

### 4.1 Proposition 2 scope

The current Prop. 2 (add-back correctness) is stated for LR-TA Phase II, WMSF-style
minimization, and IPSNS SCC-local add-back. The WMSF stabilization step
(`wmsf_stabilizeFas_scc`) is NOT covered by Prop. 2 — it uses a swap rule different from
the reachability-based add-back. The manuscript should:

**Option A (recommended):** Scope Prop. 2 to "minimize steps" (add-back) and add a
brief separate note that the stabilization step uses a different swap rule.

**Option B:** Expand Prop. 2 to cover the stabilization swap, with a separate case in the proof.

### 4.2 Numerical tolerance

Prop. 3 (IPSNS monotonicity) uses threshold `1e-12` for improvement detection. The proof
should note that BW comparisons use a tolerance of `1e-12`, meaning acceptance requires
`bw < best_bw - 1e-12`. This is consistent with the code and mathematically defensible for
nonneg integer or bounded rational weights.

### 4.3 DF03 gap — no action required

The current disclaimer ("no new approximation theorem") in the introduction is correct and
sufficient. Do not attempt to prove DF03 inheritance unless a complete argument is available.
The LOLIB evidence further supports limiting performance claims to the sparse nonneg setting.

---

## 5. Bibliography additions required

| Entry | Key | Action |
|---|---|---|
| arXiv:2412.16181 | Add as VK24 or VK25 | Add to `bibliography/references.bib`; cite in §2 related work and §9 disclosure |
| JOCO predecessor | Add as author-predecessor citation | Add stub citation; cite in §2 positioning paragraph |
| Elsevier predecessor | Add as author-predecessor citation | Add stub citation; cite in §2 positioning paragraph |
| lop_ma_edm_repo | Remove | Not cited in text; remove from bibliography |

---

## 6. What is safe to claim as COAP contributions

The following is the defensible contribution list after corrections:

1. **Formal Propositions 1–4:** First formal correctness, add-back, monotonicity, and
   termination results for the unified framework. Genuinely new in COAP.

2. **Unified treatment:** First unified presentation of LR-TA + WMSF + IPSNS under one
   complexity framework and one experimental program. New in COAP.

3. **LOLIB scope boundary:** First characterization that the framework is explicitly limited
   on dense complete ordering instances, with DRMacIver dominating. New in COAP.

4. **Expanded experimental program:** Nine experiment types; exact DP validation; five-method
   external baseline comparison; holdout parameter sensitivity; application case study.
   Substantially new in COAP vs. predecessors.

5. **Engineering validation of LR-TA (inherited and refined):** The specific engineering
   choices (original-weight add-back ordering, O(1) forward shortcut, rank-bounded reachability,
   deterministic Kahn sort, edge-ID active-flag representation) are validated in the expanded
   experimental program and are well-described here with correctness analysis.

---

## 7. Actions checklist (manuscript-editing phase)

| Action | Priority | File | Notes |
|---|---|---|---|
| Add arXiv:2412.16181 to bibliography and related work | **Blocker** | `bibliography/references.bib`, `sections/02_related_work.tex` | Cannot submit without this |
| Add JOCO-V and Elsevier-V as author predecessors | **Blocker** | Same | COAP portal policy requires it |
| Fix add-back ordering description if "residual" anywhere | High | `sections/04_algorithmic_framework.tex` | Verify no "residual" wording for add-back sort |
| Fix topological shortcut description (sufficient, not iff) | High | Same | Check for iff language |
| Fix destroy operation description (not causally linked) | High | Same | Remove any "blocking" language |
| Fix destroy-fraction reproducibility wording (deterministic, not random) | Medium | Same | Already flagged as M-01 |
| Scope Prop. 2 to exclude WMSF stabilize step | Medium | `sections/04_formal_analysis.tex` | Or add separate stabilize invariant |
| Remove lop_ma_edm_repo from bibliography if uncited | Low | `bibliography/references.bib` | Clean up |
| Replace "state of the art" with "best observed among evaluated methods" | High | `sections/06_results.tex`, `sections/01_introduction.tex` | Verify wording everywhere |
| Add DRMacIver non-determinism disclosure | Medium | `sections/05_experimental_design.tex` | "uses internal time/PID-based random seed; results from single run per instance" — see B-07 |
| Add igraph Eades weight-guarantee clarification | Low | `sections/05_experimental_design.tex` | "accepts arc weights but does not carry a weight-minimization guarantee" — see B-08 |
| Label borda_net_score as "in-repo adaptation" | Low | `sections/05_experimental_design.tex` | Consistent with weighted_eades "adaptation" label — see B-09 |
| Resolve sfas identity and update §5 baseline description | Medium | `sections/05_experimental_design.tex` | Either run CC25 external code (if available) or add explicit documented exclusion — see B-06 |
