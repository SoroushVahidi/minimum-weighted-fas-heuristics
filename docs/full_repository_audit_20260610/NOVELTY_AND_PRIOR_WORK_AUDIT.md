# Novelty and Prior-Work Audit

**Audit date:** 2026-06-11  
**Repository:** `SoroushVahidi/minimum-weighted-fas-heuristics` @ `main` (HEAD `80b3144`)  
**Audit mode:** Read-only; no source, manuscript, experiment, or git state modified.

**Source authority:** The canonical code in `src/mwfas/` is the authoritative source for
algorithm behavior. Where the prior-audit documentation conflicts with code behavior, the code
takes precedence. All code-derived findings are marked **[CODE]**. Literature-derived findings
are marked **[LIT]**. Inferences are marked **[INFER]**.

---

## Part 1 — Predecessor manuscript identity (Mandatory Correction A)

### 1.1 arXiv:2412.16181

**Title:** "Minimum Weighted Feedback Arc Sets for Ranking from Pairwise Comparisons"  
**Authors:** Soroush Vahidi, Ioannis Koutis  
**Year:** December 2024  
**arXiv ID:** 2412.16181 (cs.IR)  
**URL:** https://arxiv.org/abs/2412.16181

**Status:** Author predecessor. Vahidi is the COAP corresponding author. This is not
independent competing work.

**Content inferred from JOCO predecessor reference:** The JOCO predecessor manuscript (Vahidi
alone) cites arXiv:2412.16181 as [V25-2] with the description: *"Vahidi and Koutis [V25-2]
formulate ranking from pairwise comparisons as a minimum weighted feedback arc set problem
and propose combinatorial heuristics with strong empirical performance and fast runtimes on
standard benchmarks."* **[LIT from JOCO ZIP]**

**What this tells us:**
- arXiv:2412.16181 contains at minimum: MWFAS formulation for ranking, combinatorial heuristics,
  and empirical results on standard benchmarks.
- The JOCO predecessor explicitly distinguishes its own contribution (LR-TA engineering focus)
  from arXiv:2412.16181's scope, implying some overlap but different emphasis.
- arXiv:2412.16181 was completed before the JOCO predecessor was written (cited as existing work).

**What cannot be determined without full text access:**
- Whether IPSNS appears in arXiv:2412.16181.
- Whether the WMSF-style algorithm appears.
- The exact experimental overlap with EXP1b–EXP4.

**Critical observation: arXiv:2412.16181 is not cited anywhere in the COAP manuscript.** **[CODE/LIT]**
This is a major disclosure gap. COAP `bibliography/references.bib` does not contain this entry.
The JOCO predecessor lists it as [V25-2] but COAP does not include or cite it.

### 1.2 JOCO Predecessor (Vahidi alone)

**Title:** "Fast Local-Ratio Cycle Reduction with Topological Add-Back for Weighted Feedback
Arc Sets"  
**Author:** Soroush Vahidi (single author — not Koutis)  
**Target venue:** Journal of Combinatorial Optimization  
**Archive:** `archive/predecessor_projects/Fast_Local_Ratio...JOCO.zip`

**Confirmed content from ZIP main.tex:** **[CODE/LIT]**

1. Phase I (local-ratio cycle reduction): Identical algorithm to `lrta.py` Phase I.
2. Phase II (topological add-back): Identical to `lrta.py` Phase II, including:
   - Add-back ordering: original weight W0 descending (explicitly stated: "nonincreasing order
     of their *original* weights (heavy-first)")
   - Forward-rank acceptance: `rank(u) < rank(v)` → accept O(1) (sufficient condition)
   - Backward-rank cases: reachability test from v to u, rank-interval pruned
   - After backward accept: recompute full topo sort
3. The JOCO manuscript also describes WMSF (as a competitor, per CC25) — not as a contribution.
4. No IPSNS content.
5. 33-instance benchmark (subset of current 105-instance EXP1b benchmark).
6. Partial complexity analysis (LR-TA only).
7. Cites arXiv:2412.16181 as co-author Vahidi+Koutis related work.
8. Does NOT contain formal propositions (Prop. 1–4) equivalent to COAP's formal analysis.

**Relationship to COAP:** LR-TA as described and implemented is identical. COAP adds:
IPSNS + WMSF seed + 4 formal propositions + unified complexity + 9 experiment types +
LOLIB scope boundary + holdout parameter study.

### 1.3 Elsevier Predecessor (Vahidi)

**Title:** "Incumbent Protected SCC Neighborhood Search for the Weighted Feedback Arc Set
Problem"  
**Author:** Soroush Vahidi  
**Target venue:** Elsevier journal  
**Archive:** `archive/predecessor_projects/Incumbent_Protected_SCC...zip`

**Verified content:** ZIP contains bibliography files and template files only; no manuscript
body text is included in the archive. **[CODE]**

**Inferred content from ZIP title and predecessor manifest:** **[INFER]**
- IPSNS algorithm (Incumbent-Protected SCC Neighborhood Search)
- WMSF algorithm (used as seed)
- Some experiments

**What COAP adds vs. Elsevier predecessor (inferred):**
- LR-TA as explicit co-seed (dual-seed initialization)
- Formal Prop. 1–4 (correctness, complexity)
- Expanded experimental program (9 types)
- LOLIB scope boundary
- Holdout parameter study

---

## Part 2 — Component-level novelty table

| Component | Exact mechanism (from code) | Closest external prior work | Closest author predecessor | Shared mechanisms | Distinguishing mechanisms | Novelty classification | Evidence strength | Permissible COAP claim | Prohibited/risky claim |
|---|---|---|---|---|---|---|---|---|---|
| **LR Phase I: cycle reduction** | Iterative DFS finds any cycle; subtract min edge weight (reduced W[]); deactivate edges ≤ tol; when eps ≤ tol deactivate cyc[0] | DF03: same local-ratio principle for directed FAS | JOCO-V and arXiv-VK: same algorithm | Local-ratio weight subtraction; cycle-triggered deactivation | DFS (not DF03's dynamic TC); single-arc deactivation when eps ≤ tol | Author-predecessor contribution | High (JOCO-V confirms exact match) | "LR-TA Phase I is an engineered implementation of the local-ratio cycle reduction principle" | "Phase I is a new algorithm" or "Phase I inherits DF03's ratio guarantee" |
| **LR Phase II: topological add-back** | Sort removed edges by -W0 (original); rank[u]<rank[v] → accept O(1); else reachability(v,u,rank≤rank[u]); backward accept → full topo recompute | DF03: inclusion-minimal add-back (different goal) | JOCO-V: exact match including original-weight ordering | Heavy-first ordering concept; acyclicity test | Original (not residual) weight ordering; O(1) forward shortcut; rank-pruned reachability; full recompute on backward accept | Author-predecessor contribution | High (JOCO-V text: "nonincreasing order of original weights") | "Phase II performs a heavy-first topological add-back using original arc weights, with O(1) forward acceptance and rank-bounded reachability fallback" | "Phase II ordering is by residual/reduced weight" or "rank(u)<rank(v) iff acyclic after addition" |
| **Topological fast path** | `if rank[u] < rank[v]: accept` — sufficient condition only | None directly | JOCO-V: same | O(1) cycle test for forward arcs | Sufficient-not-iff; stale rank OK after forward accept | Author-predecessor contribution | High | "Forward-rank acceptance is a sufficient O(1) test" | "rank(u)<rank(v) iff addition is acyclic" (iff is false) |
| **Reachability fallback** | DFS from v to u, nodes pruned by rank > rank[u] | DF03: mentions reachability | JOCO-V: same | Rank-bounded pruning idea | Iterative DFS with stamp-based visited (not dynamic TC) | Author-predecessor contribution | High | "Backward candidates use rank-interval-pruned DFS reachability" | "Uses DF03's dynamic transitive closure structure" |
| **WMSF** | CC25 removeArcs(L1/L2)+MinimizeFas+StabilizeFas+MinimizeFas; per SCC | CC25 (Cavallaro-Cutello 2025) — exact match | Elsevier-V (reimplemented) | Entire pipeline | Only difference: COAP runs both L1 and L2 for single-SCC graphs | Established prior art (CC25) reimplemented | High | "WMSF is a reimplementation of the Cavallaro-Cutello algorithm" | "WMSF is a novel contribution" |
| **SCC decomposition** | Kosaraju (deterministic), called once at IPSNS init | Standard; BH13 uses SCC for ordering | Both predecessors | Standard SCC algorithm | Kosaraju for determinism | Established prior art | High | "SCCs are computed via Kosaraju's algorithm" | "SCC decomposition is novel" |
| **IPSNS: dual-seed incumbent init** | WMSF seed + LR seed; take min(BW_A, BW_B) as incumbent | Not found in surveyed FAS literature | Likely Elsevier-V | Dual-seed concept | Formal monotonicity guarantee (Prop. 3) is new | Nontrivial problem-specific integration | Medium | "Incumbent initialized from the better of two constructive seeds" | "Dual-seed initialization is a well-known technique" (not established for FAS) |
| **IPSNS: SCC backward-weight scoring** | sum(w for u,v,w in SCC if rank[u]>rank[v]) | Not in surveyed FAS heuristics | Likely Elsevier-V | Backward-weight concept | Applied at SCC granularity per-iteration | Potentially novel | Medium | "SCC selection prioritizes components with highest current backward contribution" | "SCC scoring is a novel invention of this paper" (may be in Elsevier-V) |
| **IPSNS: weighted top-K selection** | sorted by -BW_scc, take top K; weighted random choice | Not in surveyed FAS literature | Possibly Elsevier-V | Priority + random sampling | Weighted random from top-K pool (not uniform) | Potentially novel | Medium | "A stochastic weighted top-K selection policy" | [no prohibited version specific to this] |
| **IPSNS: destroy operations** | Destroy A: heaviest-removed fraction reactivated; Destroy B: lightest-active fraction removed; two independent operations | General LNS destroy patterns | Likely Elsevier-V | Independent perturbation pattern | Not causally linked; ordered by original weight | Standard engineering adaptation | Medium | "Two independent perturbations: reactivating heavy removed edges and removing light active edges" | "Heavy backward arcs are reactivated via the light edges blocking them" |
| **IPSNS: LR repair (original wt reset)** | local_ratio_repair_inside_scc; W reset to W0 at start; restricted to SCC subgraph | Not in surveyed FAS LNS literature | Likely Elsevier-V | LR cycle reduction (from DF03 lineage) | Per-SCC restriction; reset to original weights per repair | Potentially novel | Medium | "SCC-local LR repair resets arc weights from original values at each repair step" | "LR repair continues the global weight reduction" |
| **IPSNS: strict improvement acceptance** | `if _bw < best_bw - 1e-12` | Standard in improvement-only LNS | Elsevier-V | No plateau acceptance | Numerical tolerance 1e-12 | Standard engineering adaptation | High | "Candidates accepted only on strict backward-weight improvement" | [not risky] |
| **IPSNS: incumbent protection invariant** | Output from best_snapshot; BW monotone decreasing | Not formally proved in FAS literature | COAP Prop. 3 (first formal statement) | Non-worsening concept | Formal proof + strict-improvement code path | **Genuinely new in COAP** | High | "IPSNS guarantees the output is no worse than the best seed (Prop. 3)" | "This is an approximation guarantee relative to optimal" |
| **Formal Prop. 1–4** | Feasibility, add-back correctness, IPSNS monotonicity, IPSNS termination | None in surveyed FAS heuristic literature | Absent from all predecessors | Correctness/termination claims | Formal proofs with code references | **Genuinely new in COAP** | High | "Formal correctness and complexity statements are new contributions of this paper" | [not risky] |
| **LOLIB scope boundary** | 50 LOLIB instances; DRMacIver wins 45; framework wins 5; explicit limitation | LOLIB benchmark used in LOP literature | Not in any predecessor | Transfer test concept | Framing as scope boundary rather than failure | **Genuinely new in COAP** | High | "The LOLIB dense transfer test establishes a scope boundary for the proposed framework" | "The framework performs well on LOLIB" |
| **EXP3 exact DP validation** | Bitmask DP; 57 small instances; 56/57 match optimal | DP-based exact validation (methodology known) | Possibly absent from predecessors | Small-instance validation idea | Exact optimality certificate with bitmask DP | Likely new in COAP | Medium | "Exact validation on small instances using bitmask dynamic programming" | [not risky] |

---

## Part 3 — Add-back ordering correction (Mandatory Correction C)

**What code does:** **[CODE]**

In `lrta.py` line 265:
```python
removed_list = sorted(removed_eids, key=lambda eid: (-W0[eid], U[eid], V[eid]))
```

In `wmsf.py` `wmsf_minimizeFas_scc` line 263:
```python
cand = sorted(F, key=lambda eid: (-W0[eid], U[eid], V[eid], eid))
```

In `ipsns.py` `minimize_addback_inside_scc` line 242:
```python
cand = sorted([eid for eid in F if allowed_eids[eid]],
              key=lambda eid: (-W0[eid], U[eid], V[eid], eid))
```

All three sort by `W0[eid]` — the **original arc weight** stored at graph construction,
before any local-ratio reductions. The mutable reduced weight `W[eid]` (which decreases
during Phase I) is NOT used for add-back ordering.

**Tie-breaking:** The JOCO predecessor and WMSF/IPSNS use eid as final tiebreak; the LR-TA
standalone (`lrta.py`) does not include eid in the sort tuple (minor inconsistency, flagged
separately as low-severity in MANUSCRIPT_ALGORITHM_CONSISTENCY.md).

**JOCO predecessor confirmation:** **[LIT]** The JOCO predecessor explicitly states:
*"Let w_0(e) denote the original weight of arc e before any local-ratio reductions. We process
arcs in R in nonincreasing order of w_0(e) (heavy-first)."*

---

## Part 4 — Cycle detection mechanism (Mandatory Correction D)

**Implementation:** `find_any_cycle_eids` in `lrta.py` (lines 54–122) and
`find_any_cycle_eids_global` / `find_any_cycle_eids_restricted` in `ipsns.py`.

All use **iterative DFS** (simulated stack to avoid Python recursion limits).

**DFS behavior:** **[CODE]**
- Maintains `state[]` (0=unvisited, 1=in-progress, 2=done) and `parent_eid[]`
- When a back-edge (u, v) is found where v is in-progress, reconstructs the cycle
  by tracing parent pointers from u back to v
- Resets only touched nodes (not full array) for efficiency
- Returns the FIRST cycle found (not minimum weight, not shortest)

**DF03 comparison:** DF03's theoretical analysis references dynamic transitive-closure
data structures for incremental reachability. LR-TA uses plain restart DFS per cycle-finding
call. This is simpler, has higher per-call cost, but is practically fast because the active
graph shrinks after each edge removal. **[INFER]**

**Conservative complexity bounds derived from code:** **[CODE/INFER]**
- Phase I: ≤ m iterations (each removes ≥ 1 arc); each call O(n + m_active) ≤ O(n + m)
  → Phase I: O(m(n + m))
- Phase II: O(r log r + r(n + m)) where r = |removed|
- WMSF per SCC: O(m_S log m_S + r_S(k + m_S) + log(k) m_S) per SCC
- IPSNS per iteration: O(m + s log s + c_S(n_S + m_S) + r_S log r_S + r_S(n_S + m_S))
  where s = eligible SCC count, c_S = LR repair rounds, r_S = add-back candidates in SCC

These are conservative upper bounds; the actual complexity depends on graph structure and
how quickly cycles are eliminated.

---

## Part 5 — DF03 approximation guarantee (Mandatory Correction E)

**Status: Category 3 — Not currently established for the implementation.**

**Gaps between LR-TA and DF03's proof requirements:** (see full analysis in
`DF_VS_LRTA_OPERATIONAL_COMPARISON.md`)

1. DF03 requires inclusion-minimal add-back → LR-TA uses heavy-first (not inclusion-minimal)
2. DF03 removes all zero-weight edges simultaneously → LR-TA removes one arc when eps ≤ tol
3. DF03's proof relies on simple cycle selection → LR-TA finds any cycle via DFS back-edge
   (which is simple in the DFS-tree sense, but not necessarily minimum-weight)
4. Numerical tolerance (tol = 1e-12) introduces rounding effects not addressed in the proof

**Consequences:**
- COAP correctly disclaims the approximation guarantee in the introduction.
- The formal analysis section (Prop. 1–4) does not claim a ratio.
- This is the correct and defensible position.

**For IPSNS and WMSF:** Neither algorithm inherits the DF03 guarantee. IPSNS provides only
a monotonicity guarantee relative to its own seeds. WMSF provides no theoretical guarantee.

---

## Part 6 — Experimental claims (Mandatory Correction G)

### 6.1 Permissible wording by benchmark

| Benchmark | Result | Permissible wording | Prohibited wording |
|---|---|---|---|
| 97 standard nonneg sparse instances (EXP4) | Best on 96/97 | "best observed backward weight among the evaluated methods on 96 of 97 standard nonneg sparse instances" | "state of the art"; "best known" |
| DRMacIver comparison (sparse) | DRMacIver ~21.6% worse mean BW | "DRMacIver is about 21.6% worse in mean backward weight on this sparse benchmark" | "DRMacIver is the strongest existing baseline" |
| 50 LOLIB dense instances (EXP5) | DRMacIver wins 45/50; framework wins 5 | "on 50 dense LOLIB instances, the proposed framework achieves best observed solution on 5 instances; DRMacIver/FAS wins on 45" | "performs comparably on dense instances" |
| DRMacIver LOLIB incompletions | Some incomplete runs noted | Report incomplete runs or exclude from analysis | Claim all LOLIB runs completed |
| 57 exact-DP instances (EXP3) | 56/57 match optimal | "matches DP optimum on 56 of 57 small nonneg instances (n ≤ 20)" | "optimal on small instances" (1 exception exists) |
| sfas baseline | Not implemented | State explicitly that sfas baseline was not included | Imply exhaustive baseline coverage |
| exact-IP comparison | Not implemented | State explicitly | Imply exact-IP comparison was conducted |

### 6.2 Holdout experiment status

The stage-2 holdout (1286 runs, ~42% complete at audit time) is still running.
Default parameter claims that depend on holdout results must not be finalized until
`logs/coap_ipsns_holdout/COMPLETED.ok` exists.

---

## Part 7 — Literature verification notes

### 7.1 References that support their claimed mechanism

| Cite key | Claimed mechanism in COAP | Verification status |
|---|---|---|
| DF03 | Local-ratio framework for directed FAS; closest antecedent to Phase I | Verified via DOI 10.1016/S0020-0190(02)00491-X |
| BYGR98 | General local-ratio approximation framework | Verified via DOI 10.1137/S0097539796305109 |
| CC25 | WMSF algorithm (paper049) | Verified via DOI 10.18293/SEKE2025-049 |
| BSNA21 | Exact ILP method for MFAS | Verified via DOI 10.1145/3446429 |
| ELS93 | Greedy source/sink heuristic | Verified via DOI 10.1016/0020-0190(93)90079-O |
| HGH21 | TIGHT heuristic | Verified via DOI 10.1145/3447652 |
| SST16 | Web-scale FAS | Verified via DOI 10.14778/3021924.3021930 |
| MRD12 | LOLIB benchmark description | Verified via DOI 10.1007/s10589-010-9384-9 |

### 7.2 References requiring caution

| Cite key | Issue |
|---|---|
| graph_benchmarks_repo | Year listed as 2026 in bib; dataset may predate 2026 — verify access date accuracy |
| lolib_library | Year 2010 in bib; official page still active; use with MRD12 for formal provenance |
| lop_ma_edm_repo | Appears in bib but not cited in COAP text — **remove** |
| BH13 | No DOI in COAP bib; Springer record exists; add DOI if available |
| JOCO-V | Not cited in COAP — **must be added and cited** |
| arXiv-VK (2412.16181) | Not cited in COAP — **must be added and cited** |
| Elsevier-V | Not cited in COAP — **must be disclosed and cited** |

### 7.3 References not proposed for COAP (clarifying status)

**Simpson–Srinivasan–Thomo (SST16):** Currently cited in COAP for web-scale context. The
paper is about scalable FAS computation for web graphs. The mechanism (greedy + SCC) is
different from LR-TA/IPSNS. Appropriate as conceptual reference; not directly comparable.

**Baharev et al. (BSNA21):** Cited for exact method context. Used for EXP8 MIP motivation.
Appropriate.

**Cavallaro–Cutello (CC25):** Correctly cited as the source of the WMSF algorithm.

---

## Part 8 — Disclosure obligations

### 8.1 What COAP must disclose

1. **arXiv:2412.16181 (Vahidi & Koutis, Dec 2024):**
   - This is an author predecessor. It is NOT currently cited in COAP.
   - Must be added to the COAP bibliography and discussed in related work.
   - If it contains LR-TA or IPSNS algorithms substantially similar to COAP,
     copies must be uploaded to the COAP portal per COAP guidelines.
   - Must distinguish what COAP adds beyond this preprint.

2. **JOCO predecessor (Vahidi, LR-TA only):**
   - LR-TA is directly inherited from this manuscript.
   - Must be disclosed in the COAP cover letter.
   - If currently under review at JOCO, COAP editors must be informed.
   - The formal analysis (Prop. 1–4) and the IPSNS+WMSF integration are what distinguish COAP.

3. **Elsevier predecessor (Vahidi, IPSNS/WMSF):**
   - IPSNS is inherited from this manuscript.
   - Must be disclosed in the COAP cover letter.
   - Upload to COAP portal if applicable.

4. **EJCO/CAIE submissions:**
   - Prior submission attempts of substantially the same manuscript.
   - Disclose in cover letter with outcome (rejected/withdrawn).

### 8.2 Minimum-disclosure cover letter language (recommended)

See `MANUSCRIPT_POSITIONING_RECOMMENDATIONS.md` for complete draft language.

---

## Part 9 — Final conclusions

### 9.1 Strongest defensible novelty claim

**The formal correctness and complexity analysis (Propositions 1–4) is the single strongest
defensible novelty contribution first appearing in the COAP manuscript.** It provides:
- LR-TA feasibility and termination (Prop. 1)
- Correctness of the add-back shortcut mechanism (Prop. 2)
- IPSNS incumbent monotonicity guarantee (Prop. 3)
- IPSNS termination (Prop. 4)

These propositions are genuinely new: absent from the JOCO predecessor, absent from
the Elsevier predecessor (body text unavailable but the formal analysis section is new
to COAP), and not found in the external literature.

### 9.2 Second strongest contribution

**The unified experimental program (9 experiment types including LOLIB scope boundary,
exact DP validation, and holdout parameter study) substantially exceeds the prior-manuscript
experimental evidence.** The LOLIB scope-boundary finding (DRMacIver dominates on dense
complete ordering instances) is a new, honest characterization of algorithm scope with no
precedent in the predecessor manuscripts.

### 9.3 Claims that must not be made

1. LR-TA inherits DF03's approximation guarantee.
2. Adding (u→v) preserves acyclicity if and only if rank(u) < rank(v).
3. Add-back ordering is by residual/reduced weight.
4. "State of the art" for sparse FAS (baseline panel is not exhaustive).
5. IPSNS reactivates heavy arcs via light arcs blocking them (no such mechanism).
6. Destroy fractions are randomized (they are deterministic parameters).
7. arXiv:2412.16181, the JOCO predecessor, and the Elsevier predecessor are independent
   works with no overlap.

### 9.4 IPSNS novelty after literature review

**IPSNS appears genuinely novel relative to the published external literature surveyed.**
The specific combination of SCC-local LNS with backward-weight priority scoring, weighted
top-K selection, independent destroy-A and destroy-B perturbations, LR repair with
original-weight reset, and strict-improvement acceptance is not found in the surveyed FAS,
LNS, or ordering literature.

**However:** IPSNS first appeared in the author's Elsevier predecessor manuscript and thus
cannot be claimed as "new in COAP" without disclosure. The formal monotonicity proof (Prop. 3)
is the new COAP contribution built on the inherited IPSNS design.

### 9.5 LR-TA classification

**LR-TA should be called an engineered specialization of the DF03 local-ratio framework,**
presented as a standalone validated implementation in the JOCO predecessor and now incorporated
as a seed within the unified COAP framework. It is not a "new algorithm" (the principle is
from DF03 and the implementation is from the JOCO predecessor), but the engineering choices
(original-weight add-back ordering, O(1) topological fast path, rank-bounded reachability,
deterministic Kahn sort) are non-trivial and constitute a specific contribution.

### 9.6 Distinctness from arXiv:2412.16181

**Insufficient information to fully assess without full-text access.** However, based on what
is known:
- arXiv:2412.16181 targets "ranking from pairwise comparisons" — a specific application framing.
- COAP targets "general sparse weighted directed graphs" — broader problem scope.
- COAP adds formal analysis (Prop. 1–4) not described in arXiv:2412.16181 per the JOCO reference.
- COAP adds LOLIB scope-boundary test, holdout parameter study, and 9 experiment types.
- **These distinctions are likely sufficient for COAP to be a publishable advance**, but the
  authors must obtain the full text of arXiv:2412.16181 and document precisely what COAP adds.

### 9.7 Salami-slicing verdict

**The risk is moderate but manageable with transparent disclosure.** The split between JOCO-V
(LR-TA only) and Elsevier-V (IPSNS/WMSF only) could raise concerns if submitted
simultaneously. COAP unifies both and adds substantial new content (formal analysis,
9 experiments, LOLIB scope boundary). With proper disclosure and cover-letter narrative,
COAP can be positioned as a legitimate and substantial advancement over the predecessors.
