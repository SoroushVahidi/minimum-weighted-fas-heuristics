# Final Scientific Narrative (COAP-Oriented)

**Audit date:** 2026-06-11

---

## Recommended narrative (single paragraph)

This paper is a **computational optimization and algorithm-engineering study** of the minimum weighted feedback arc set problem on **nonnegative sparse weighted directed graphs**. The **primary new algorithmic contribution is IPSNS** (incumbent-protected SCC neighborhood search): SCC-local destroy-and-repair refinement with a proved non-worsening invariant relative to the best internal seed. **LR-TA** is an **inherited, engineered constructive seed** (developed in a prior author manuscript targeting JOCO) implementing local-ratio cycle reduction and original-weight topological add-back. **WMSF** is a **Cavallaro–Cutello (2025) reimplementation** used as a complementary seed, not a new method. The **principal empirical result** is that IPSNS achieves the **best observed backward weight among all tested methods on 96/97 standard sparse instances**, with exact and MIP validation supporting near-optimality on small and medium subsets, while **Experiment EXP10** (upon completion) certifies that the advantage over the strongest external heuristic DRMacIver/FAS is **robust under repeated stochastic runs**. A **dense LOLIB transfer test** establishes an explicit **limitation**: matrix-based pairwise-ordering methods dominate on complete dense tournaments. **Formal Propositions 1–4** provide supporting correctness and complexity statements—they do **not** constitute a new approximation-ratio theorem. A **reproducible artifact** documents all experiments.

---

## Assessment: is this narrative fully supported?

| Element | Supported? | Caveat |
|---------|------------|--------|
| IPSNS primary new | Yes | Disclose Elsevier/DAM predecessor |
| LR-TA inherited | Yes | Disclose JOCO predecessor |
| WMSF CC25 seed | Yes | — |
| 96/97 sparse best observed | Yes | Verified in final_branch audit |
| Near-optimal EXP3/EXP8 | Yes | Wording: empirical certification only |
| EXP10 robustness | **Pending** | Do not submit until integrated |
| LOLIB limitation | Yes | — |
| Props supporting only | Yes | — |
| Reproducible artifact | **Partial** | OR1 + tests incomplete |

**Narrative modification needed:** None to core science; **add disclosure layer** and **EXP10 clause**.

---

## Final hierarchy of contributions

### 1. Primary contribution
**IPSNS** with incumbent-protection invariant (Prop 3) and SCC-local LNS design; formal termination (Prop 4).

### 2. Secondary algorithmic contributions
Unified **dual-seed framework** integrating LR-TA + WMSF; deterministic engineering choices documented in code.

### 3. Empirical contributions
- Sparse benchmark dominance among tested methods (EXP1b, EXP4)
- Exact DP validation (EXP3) and MIP medium validation (EXP8)
- Ablation (EXP2), budget curve (EXP6), plain LS negative control (EXP7)
- Application case (EXP9)
- Stochastic robustness (EXP10, pending)
- Parameter holdout study (1290 runs, postprocess pending)

### 4. Supporting correctness results
Propositions 1–2 (LR-TA/add-back); complexity §4; algorithm invariants table.

### 5. Reproducibility contribution
Scripts, manifests, summaries — **completion pending OR1 + tests**.

### 6. Limitations
- Nonnegative sparse digraphs primary regime
- LOLIB dense: DRMacIver stronger
- No approximation ratio
- Training-free baseline scope (no GNNRank)
- DRMacIver wrapper timeouts on 4 sparse instances
- Parameter claims subset-validated (EXP2 + holdout)

---

## What this narrative avoids (rejection history)

- Leading with LR-TA novelty
- Claiming WMSF as new
- Hiding dense weakness
- Single-run DRMacIver without EXP10
- “Not published previously” falsehood
- Approximation theorem implications

---

## COAP reviewer one-liner (for cover letter)

“We submit a unified computational optimization study whose new algorithmic content is incumbent-protected SCC refinement (IPSNS), supported by extensive validation including exact and MIP certification, explicit dense-regime limitations, and repeated-run robustness checks, with full predecessor disclosure.”
