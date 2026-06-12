# Related-Manuscript Contribution Matrix

**Audit date:** 2026-06-11  
**Purpose:** Map each algorithmic and experimental component to its origin across the manuscript
family, assess overlap, and identify required disclosure items.

**Notation:**
- ✓ = clearly present
- ~ = partially or inferably present
- ? = cannot confirm without full-text access
- ✗ = absent

**Manuscripts:**
- **arXiv-VK** = arXiv:2412.16181, Vahidi & Koutis (Dec 2024) — author predecessor
- **JOCO-V** = JOCO predecessor ZIP, Vahidi alone (archive/predecessor_projects/Fast_LR…)
- **Elsevier-V** = Elsevier predecessor ZIP, Vahidi (Incumbent_Protected_SCC…)
- **COAP** = current manuscript (paper_coap/), Vahidi

---

## Table 1 — Component-level contribution matrix

| Component | arXiv-VK | JOCO-V | Elsevier-V | COAP | Degree of alg. overlap | New evidence/analysis in COAP | Required disclosure |
|---|---|---|---|---|---|---|---|
| **Local-ratio peeling (Phase I)** | ? | ✓ | ~ | ✓ | High vs. JOCO-V | Same algorithm; formal Prop. 1 is new | Cite JOCO-V as predecessor |
| **Zero-edge deletion** | ? | ✓ | ~ | ✓ | Exact vs. JOCO-V | None beyond Prop. 1 | Same |
| **Heavy-first add-back (original weights)** | ? | ✓ | ~ | ✓ | Exact vs. JOCO-V | Prop. 2 correctness statement | Cite JOCO-V |
| **Topological fast path (rank shortcut)** | ? | ✓ | ~ | ✓ | Exact vs. JOCO-V | Same, Prop. 2 | Cite JOCO-V |
| **Reachability fallback (rank-pruned)** | ? | ✓ | ~ | ✓ | Exact vs. JOCO-V | Same, Prop. 2 | Cite JOCO-V |
| **Topo recompute after backward accept** | ? | ✓ | ~ | ✓ | Exact vs. JOCO-V | Prop. 2(3) | Cite JOCO-V |
| **WMSF (CC25 reimplementation)** | ? | ✗ | ✓ | ✓ | Exact vs. Elsevier-V | WMSF formal analysis is new | Cite CC25 (done); cite Elsevier-V predecessor |
| **SCC decomposition (Kosaraju)** | ? | ~ | ✓ | ✓ | Standard algorithm | None new | Cite as standard |
| **IPSNS full algorithm** | ? | ✗ | ✓ | ✓ | High vs. Elsevier-V | Prop. 3, 4; unified complexity | Cite Elsevier-V predecessor |
| **SCC backward-weight scoring** | ? | ✗ | ✓ | ✓ | High vs. Elsevier-V | None new | Same |
| **Weighted top-K SCC selection** | ? | ✗ | ? | ✓ | Unknown vs. Elsevier-V | None new | Same |
| **Destroy A (heavy reactivate)** | ? | ✗ | ? | ✓ | Likely overlap | None new | Same |
| **Destroy B (light remove)** | ? | ✗ | ? | ✓ | Likely overlap | None new | Same |
| **SCC-local LR repair (original-wt reset)** | ? | ✗ | ? | ✓ | Likely overlap | None new | Same |
| **SCC-local minimize add-back** | ? | ✗ | ? | ✓ | Likely overlap | None new | Same |
| **Rollback on degenerate repair** | ? | ✗ | ? | ✓ | Likely overlap | None new | Same |
| **Strict-improvement acceptance** | ? | ✗ | ✓ | ✓ | High vs. Elsevier-V | Prop. 3 formalizes this | Cite Elsevier-V |
| **Incumbent protection invariant** | ? | ✗ | ~ | ✓ | Partially in Elsevier-V | **Prop. 3 proof is new in COAP** | Cite Elsevier-V, note Prop. 3 is new |
| **Dual-seed initialization (WMSF+LR best)** | ? | ✗ | ~ | ✓ | Partially | Formally described in COAP | Cite Elsevier-V |
| **Exact DP validation (EXP3)** | ? | ✗ | ? | ✓ | Unknown | Newly reported in COAP | Disclose if in arXiv-VK |
| **EXP1b core benchmark (105 instances)** | ? | ~ (33 inst) | ? | ✓ | Expanded | Expanded from 33 to 105 | Cite JOCO-V (33-instance version) |
| **EXP2 ablation** | ? | ✗ | ? | ✓ | Unknown | New in COAP | — |
| **EXP4 external baselines** | ? | ~ | ? | ✓ | Partially | More baselines in COAP | — |
| **EXP5 LOLIB transfer test** | ? | ✗ | ? | ✓ | Unknown | **New scope boundary — COAP** | — |
| **EXP6 budget curve** | ? | ✗ | ? | ✓ | Unknown | New in COAP | — |
| **EXP7 plain LS comparison** | ? | ✗ | ? | ✓ | Unknown | New in COAP | — |
| **EXP8 MIP validation** | ? | ✗ | ? | ✓ | Unknown | New in COAP | — |
| **EXP9 application case** | ? | ✗ | ? | ✓ | Unknown | New in COAP | — |
| **Formal Prop. 1 (LR-TA feasibility)** | ✗ | ✗ | ✗ | ✓ | None | **New in COAP** | — |
| **Formal Prop. 2 (add-back correctness)** | ✗ | ✗ | ✗ | ✓ | None | **New in COAP** | — |
| **Formal Prop. 3 (IPSNS monotonicity)** | ✗ | ✗ | ✗ | ✓ | None | **New in COAP** | — |
| **Formal Prop. 4 (IPSNS termination)** | ✗ | ✗ | ✗ | ✓ | None | **New in COAP** | — |
| **Complexity analysis (COAP §4)** | ✗ | ~ (partial) | ✗ | ✓ | Partial vs. JOCO-V | Unified, all three algorithms | Cite JOCO-V for LR-TA complexity |
| **Holdout parameter study (EXP stage-2)** | ✗ | ✗ | ✗ | ~ | None | **New in COAP** (pending) | — |

---

## Table 2 — Textual and algorithmic overlap characterization

| Manuscript pair | Algorithmic overlap | Textual overlap | Assessment |
|---|---|---|---|
| COAP ↔ JOCO-V | High for LR-TA components (same code, same algorithm) | Likely high for §3 problem def, §4 Phase I/II; COAP adds formal analysis | Must disclose; not duplicate because COAP adds IPSNS, WMSF, formal analysis, 3× more experiments |
| COAP ↔ Elsevier-V | High for IPSNS, WMSF | Unknown (body text not in ZIP) | Must disclose; extent of text overlap needs manual side-by-side |
| COAP ↔ arXiv-VK | Unknown | Unknown | Must obtain full text; cannot assess without it |
| COAP ↔ EJCO/CAIE | High (COAP is EJCO + Springer template + formal analysis) | High | Must disclose; EJCO and CAIE are prior submission attempts |

---

## Table 3 — Disclosure action items

| Predecessor | Nature | Action |
|---|---|---|
| **arXiv:2412.16181** (Vahidi & Koutis) | Author predecessor; formulation and heuristics overlapping unknown | **Must cite in COAP related work**; must be uploaded to COAP portal if algorithms overlap substantially; clarify what COAP adds beyond this preprint |
| **JOCO predecessor** (Vahidi alone) | Author predecessor; LR-TA is fully present | **Must cite** or disclose in cover letter; clarify single-author vs. unified COAP |
| **Elsevier predecessor** (Vahidi) | Author predecessor; IPSNS/WMSF present | **Must cite** or disclose in cover letter; upload to COAP portal |
| **EJCO submission** | Prior submission of same work to different venue | Disclose in cover letter; upload EJCO manuscript to portal if still under consideration or rejected; note COAP additions |
| **CAIE submission** | Prior submission attempt | Disclose in cover letter if substantially the same |

---

## Table 4 — Degree-of-novelty by component for COAP

| Component | Classification | Confidence |
|---|---|---|
| LR-TA Phase I | Author-predecessor contribution (JOCO-V) | High — exact overlap |
| LR-TA Phase II | Author-predecessor contribution (JOCO-V) | High — exact overlap |
| WMSF | External prior art reimplemented (CC25) | High — manuscript acknowledges |
| IPSNS structure | Author-predecessor contribution (Elsevier-V) | High — ZIP title confirms |
| Formal Prop. 1–4 | Genuinely new in COAP | High — not in any predecessor |
| Unified complexity analysis | New in COAP (partial precedent in JOCO-V for LR-TA) | Medium |
| Incumbent monotonicity proof | New in COAP | High |
| EXP2 ablation | Likely new in COAP | Medium |
| EXP3 exact DP | Unknown vs. arXiv-VK; likely new vs. JOCO-V and Elsevier-V | Medium |
| EXP5 LOLIB scope boundary | New in COAP | High |
| EXP6–9 | Likely new in COAP | Medium |
| Holdout parameter study | New in COAP | High |

---

## 5. Salami-slicing risk assessment

**Definition used:** Salami slicing is the unjustified splitting of a single body of work into
multiple publications to artificially inflate the publication record.

**Current situation:**
- The JOCO predecessor covers LR-TA only (no IPSNS, no WMSF, 33 instances).
- The Elsevier predecessor covers IPSNS + WMSF (no formal analysis, smaller experiments).
- COAP unifies both, adds formal analysis (4 propositions), expands to 9 experiment types,
  includes LOLIB scope boundary, adds holdout parameter study, and substantially expands the
  experimental program.
- The split between LR-TA and IPSNS manuscripts may reflect an originally separate development
  path that is now legitimately unified.

**Risk level:** Moderate. The split could be questioned if JOCO and COAP are in parallel
submission or if JOCO is under review while COAP is submitted. The concern is manageable if:
1. COAP transparently discloses both predecessors.
2. The cover letter explains that the predecessors were separate development efforts now
   unified with new formal analysis and expanded experiments.
3. The predecessor manuscripts are uploaded to the COAP portal per COAP guidelines.
4. The JOCO submission and COAP submission are not simultaneous (or COAP explicitly acknowledges
   JOCO as a predecessor available for reviewer review).

**Key mitigating factor:** The formal analysis section (Prop. 1–4) and the unified complexity
characterization are genuinely new material that justifies the unified COAP submission as
an advance beyond the split predecessors taken together.
