# IPSNS Novelty Audit

**Audit date:** 2026-06-11  
**Authoritative sources:** `src/mwfas/ipsns.py` (canonical code); `src/mwfas/wmsf.py`; COAP
`sections/04_algorithmic_framework.tex`; `sections/04_formal_analysis.tex`; COAP
`bibliography/references.bib`; predecessor project manifest; Elsevier ZIP contents.

---

## 1. Exact IPSNS mechanism from code (not from analogy)

The following is derived entirely from `ipsns.py` (`lns_merge_wmsf_lr_best_incumbent`).

### 1.1 Initialization

1. **SCC computation:** Kosaraju's algorithm run once on the full original graph
   (`kosaraju_scc`, lines 50–104 of `wmsf.py`). SCCs are computed from the original
   input edge set and remain fixed throughout the entire IPSNS run (no dynamic SCC recomputation).
   
2. **WMSF seed:** `wmsf_seed_solution_full` — runs the per-SCC pipeline
   (removeArcs → MinimizeFas → StabilizeFas → MinimizeFas) for each nontrivial SCC.
   For single-SCC graphs, tries both L1 and L2 orderings and keeps the one with lower backward
   weight. This exactly matches the standalone `wmsf.py` entry point.
   
3. **LR seed:** `lr_seed_solution` — global cycle reduction (`lr_cycle_reduction_global`) using
   reduced weights, followed by global heavy-first add-back (`wmsf_minimize_global`) using
   original weights W0 for sorting.
   
4. **Incumbent initialization:** The better-backward-weight seed is selected as the initial
   incumbent. The `best_snapshot` stores `(bytearray(active), set(F))` — a full copy of the
   active-flag array and the removed-edge set.

### 1.2 SCC scoring

```python
def score_scc_backward_weight(edges_in_scc, rank):
    return sum(w for u, v, w, _ in edges_in_scc if rank[u] > rank[v])
```

Score = total weight of SCC-internal arcs that are backward in the current incumbent ranking.
This uses the current global rank vector (from the incumbent's topological sort).

### 1.3 SCC selection

Each iteration:
1. Score every nontrivial SCC by backward weight against the current incumbent rank.
2. Filter to SCCs with score > 0.
3. Sort descending by score; take top-K (default K=15).
4. Weighted random choice from the pool, with weights proportional to SCC backward weight.
   (Ablation mode: uniform random from all non-zero-BW SCCs.)

### 1.4 Destroy operations (two independent perturbations)

**Destroy A — reactivate heavy removed edges:**
```python
removed_in_scc = sorted([eid for eid in internal_eids if eid in F],
                         key=lambda eid: (-W0[eid], U[eid], V[eid], eid))
k_add = int(destroy_addback_frac * len(removed_in_scc))
for eid in removed_in_scc[:k_add]:
    active[eid] = 1; F.discard(eid)
```
Reactivates the heaviest `destroy_addback_frac` fraction of edges currently in the FAS for
this SCC. Ordered by original weight W0 descending.

**Destroy B — remove light active edges:**
```python
active_in_scc = sorted([eid for eid in internal_eids if active[eid]],
                        key=lambda eid: (W0[eid], U[eid], V[eid], eid))
k_rem = int(destroy_remove_frac * len(active_in_scc))
for eid in active_in_scc[:k_rem]:
    active[eid] = 0; F.add(eid)
```
Removes the lightest `destroy_remove_frac` fraction of currently active SCC edges. Ordered
by original weight W0 ascending.

**Causal relationship:** NONE. Destroy A and Destroy B are applied sequentially but are
**not causally linked**. Destroy A adds heavy edges back to the active graph;
Destroy B removes light active edges from the active graph. There is no mechanism in the code
by which the reactivated heavy edges "depend on" the light edges removed, or vice versa. The
framing "reactivates heavy backward arcs via the light edges blocking them" is INCORRECT and
must not appear in manuscript prose.

### 1.5 Repair — LR cycle reduction inside SCC

`local_ratio_repair_inside_scc` runs local-ratio cycle reduction restricted to nodes/edges
in the selected SCC. Critical detail:

```python
W = {eid: W0[eid] for eid in range(len(U)) if allowed_eids[eid]}
```

**The local weight dictionary is reset from original weights W0 at the start of every repair.**
It does NOT carry over reduced weights from the initial global LR phase. This is correct
behavior (it avoids accumulated floating-point residues interfering with SCC-local reduction),
but it means each repair is an independent local-ratio pass on the SCC, not a continuation of
the global Phase I.

### 1.6 Repair — add-back inside SCC

`minimize_addback_inside_scc`:
- Same heavy-first mechanism as LR-TA Phase II, restricted to allowed SCC nodes/edges.
- Sort key: `(-W0[eid], U[eid], V[eid], eid)` — original weight descending with eid tiebreak.
- Same topological fast path + reachability fallback + recompute-on-accept.

### 1.7 Rollback

If `minimize_addback_inside_scc` raises `RuntimeError` (SCC subgraph cyclic — indicates
degenerate repair state), the pre-move `(active, F)` state is restored from `old_states`.
Additionally, if global `topo_order_active` raises after a repair, the incumbent is restored
from `active_before`/`F_before`.

### 1.8 Acceptance criterion

```python
if _bw < best_bw - 1e-12:
    best_bw = _bw
    best_snapshot = (bytearray(active), set(F))
```

**Strict improvement required.** If the repaired candidate is feasible but its backward weight
≥ current best minus tolerance, the incumbent is restored exactly (no plateau acceptance).

### 1.9 Incumbent guarantee

Output comes from `best_snapshot`, which was updated only on strict improvement.
The final backward weight is ≤ both seed backward weights.

---

## 2. External prior work comparison

### 2.1 General LNS for combinatorial optimization

Large Neighborhood Search (LNS) is a general metaheuristic (Shaw 1998). Applying it to
feedback arc set via SCC decomposition is a natural combination but not previously published
for weighted FAS in the literature reviewed for this audit.

**Key prior work surveyed:**
- Brandenburg & Hanauer (2013) — sorting heuristics for FAS, no LNS
- Eades, Lin, Smyth (1993) — greedy, no LNS
- Hecht, Gonciarz, Horváth (2021) TIGHT — tight localizations, not SCC-LNS
- Cavallaro & Cutello (2025) WMSF — stabilize+minimize pipeline, not iterative LNS
- Baharev et al. (2021) — exact method, ILP, not LNS
- Simpson, Srinivasan, Thomo (2016) — web-scale greedy, not LNS
- Fomin et al. (2010) — tournament local search (k-exchange), different problem structure
- DRMacIver/FAS — matrix-based, no SCC neighborhood

None of the above use SCC-restricted destroy-repair LNS with incumbent protection for
weighted FAS. Based on the literature accessible in this audit, IPSNS appears to be a
**potentially novel algorithm design** for this problem class.

**Caveat:** arXiv and conference preprints not yet in this bibliography may contain similar
approaches. Specifically, arXiv:2412.16181 (Vahidi & Koutis, see §3) must be examined to
determine whether a similar IPSNS was already proposed there.

### 2.2 DFVS literature and LNS

The Directed Feedback Vertex Set problem has attracted LNS-style approaches (e.g., in
parameterized algorithm engineering). However, DFVS and WFAS are distinct problems with
different neighborhood structures.

---

## 3. Author-predecessor assessment

### 3.1 Elsevier predecessor (Predecessor 2)

The Elsevier predecessor ZIP (`Incumbent_Protected_SCC_Neighborhood_Search...zip`) contains
only template files, `cas-refs.bib`, `references.bib`, and `grabs.pdf` — no manuscript body
text. The manuscript body was either not included in this ZIP or exists separately.

**Consequence:** The exact content of the Elsevier predecessor cannot be verified from the
repository alone. Given the ZIP title explicitly names "Incumbent Protected SCC Neighborhood
Search," IPSNS clearly appears in this predecessor manuscript.

**Status:** IPSNS is an **author-predecessor contribution** from the Elsevier predecessor.
The COAP manuscript refines it within a unified framework.

### 3.2 arXiv:2412.16181 (Vahidi & Koutis)

Per the JOCO predecessor manuscript (which cites arXiv:2412.16181 as [V25-2]):
> "Vahidi and Koutis [V25-2] formulate ranking from pairwise comparisons as a minimum weighted
> feedback arc set problem and propose combinatorial heuristics with strong empirical performance
> and fast runtimes on standard benchmarks."

This description does not specify whether IPSNS appears in arXiv:2412.16181. The JOCO paper
treats arXiv:2412.16181 as a different but related work, not as the same manuscript.

**Status:** Cannot confirm or deny IPSNS presence in arXiv:2412.16181 without full-text access.

### 3.3 JOCO predecessor (Predecessor 1, Vahidi alone)

No IPSNS content. The JOCO predecessor is entirely about LR-TA (Phase I + Phase II). IPSNS
does not appear.

---

## 4. Novelty classification

| IPSNS component | Prior art (external) | Author predecessor | Novelty class |
|---|---|---|---|
| LNS metaheuristic framework | Shaw 1998 (general LNS) | Elsevier predecessor | Standard engineering adaptation |
| SCC decomposition for FAS | Standard technique; used in BH13, HGH21 | Both predecessors | Standard engineering adaptation |
| Dual-seed initialization (WMSF+LR, take best) | Not found in surveyed literature | COAP manuscript may be first formal description | Nontrivial problem-specific integration |
| SCC backward-weight scoring | Not in surveyed heuristic literature | Likely Elsevier predecessor | Potentially novel |
| Weighted top-K SCC selection | Not in surveyed FAS literature | Likely Elsevier predecessor | Potentially novel |
| Destroy A (heavy edge reactivation) | General LNS destroy patterns | Likely Elsevier predecessor | Standard engineering adaptation |
| Destroy B (light edge removal) | General LNS destroy patterns | Likely Elsevier predecessor | Standard engineering adaptation |
| Combined destroy A+B (independent) | Not specifically found | Likely Elsevier predecessor | Nontrivial combination |
| LR repair with original-weight reset | Not in surveyed literature | Likely Elsevier predecessor | Potentially novel |
| Strict-improvement acceptance (no plateau) | Standard LNS improvement-only | Elsevier predecessor | Standard engineering adaptation |
| Incumbent monotonicity guarantee (Prop. 3) | Not in surveyed FAS literature | COAP formal analysis (new) | **Genuinely new in COAP** |
| Rollback on degenerate repair state | Standard defensive coding | — | Standard engineering |

---

## 5. What is genuinely new in COAP vs. predecessors

Based on code analysis and available predecessor content:

1. **Incumbent monotonicity proposition (Prop. 3):** Formally proved for the first time in the
   COAP formal analysis section. Not in JOCO predecessor. Not evidenced in Elsevier predecessor
   (whose body text is unavailable). This is COAP's clearest new formal contribution.

2. **Unified framework with dual-seed initialization:** WMSF seed + LR seed + IPSNS under one
   proof-supported complexity analysis. The unified presentation under one complexity framework
   (§4 formal analysis, Prop. 1–4) is new relative to the split-manuscript predecessors.

3. **Formal complexity characterization:** Conservative O(m(n+m)) for LR-TA and similar for
   WMSF and IPSNS. While derivable, these are stated formally for the first time in COAP.

4. **Expanded experimental program:** EXP1b-9 (105 instances, ablation, exact DP, LOLIB, etc.)
   vs. 33 instances in JOCO predecessor. The LOLIB scope-boundary finding is new.

5. **LOLIB dense transfer test:** The characterization that the method is deliberately limited
   on dense ordering instances, with DRMacIver dominating on LOLIB, is a new scope-boundary
   contribution.

---

## 6. What is NOT new to COAP (already in predecessors)

| Component | Where it first appears |
|---|---|
| LR-TA Phase I (cycle reduction) | arXiv:2412.16181 and/or JOCO predecessor |
| LR-TA Phase II (topological add-back) | JOCO predecessor (fully described) |
| IPSNS destroy-repair structure | Elsevier predecessor |
| WMSF reimplementation | Cavallaro-Cutello 2025 (external prior art, reimplemented) |
| Benchmark results on 33 core instances | JOCO predecessor (different subset) |

---

## 7. What the manuscript must disclose

1. IPSNS first appears in an author predecessor manuscript (Elsevier submission), predating COAP.
   Disclose the Elsevier predecessor as "author predecessor" and explain what COAP adds.
2. The JOCO predecessor (LR-TA only) contains Phase I and Phase II as implemented in current
   code. Disclose.
3. arXiv:2412.16181 (Vahidi & Koutis) must be cited and its relationship to COAP clarified.
   If it contains IPSNS, the disclosure is stronger; if not, mention it as complementary prior work.
4. WMSF is a reimplementation of CC25 (external). This is already visible in the manuscript
   through citations.

---

## 8. Conclusion on IPSNS novelty

**Working conclusion (cautious):**

IPSNS as a specific algorithm design — SCC-decomposed LNS with backward-weight priority scoring,
weighted top-K selection, two-phase independent destroy, LR repair with original-weight reset,
and strict-improvement acceptance — does not appear in the external literature surveyed.
It represents a **nontrivial problem-specific integration** that is plausibly novel relative
to published external work.

However:
- The algorithm first appears in an author predecessor manuscript (Elsevier), not in COAP.
- Whether arXiv:2412.16181 contains a similar algorithm is unknown without full-text access.
- The incumbent monotonicity guarantee (Prop. 3) is the clearest **new formal contribution**
  first appearing in COAP.

**Permissible COAP claim:** "IPSNS was introduced in a predecessor manuscript and is here
presented with formal correctness guarantees, a unified complexity analysis, and an expanded
experimental validation."

**Prohibited claim:** "IPSNS is a new algorithm introduced in this paper" (without disclosing
the predecessor manuscript).
