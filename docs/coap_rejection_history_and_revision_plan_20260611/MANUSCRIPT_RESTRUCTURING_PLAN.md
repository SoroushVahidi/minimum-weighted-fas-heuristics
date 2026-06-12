# Manuscript Restructuring Plan

**Audit date:** 2026-06-11  
**Goal:** Avoid prior rejection patterns (LR-TA-led novelty, hidden scope, theory overload, table sprawl).  
**Do not edit files in this task** — ordered plan only.

---

## Target section structure (main paper)

1. **Introduction** — Problem → sparse vs dense → IPSNS-centered contributions → **predecessor disclosure paragraph** → paper outline
2. **Related work** — External literature + **Author predecessor work** subsection (arXiv, JOCO, DAM)
3. **Problem definition** — MWFAS, backward weight, sparse primary / dense transfer notation
4. **Algorithmic framework**
   - 4.1 LR-TA seed (background-level: “inherited engineered seed”)
   - 4.2 WMSF seed (baseline seed, CC25-derived)
   - 4.3 IPSNS refinement (**primary algorithmic section** — longest subsection)
   - 4.4 Formal analysis — **Proposition statements only** (1 page)
5. **Experimental design** — Questions, datasets, baselines, fairness, EXP10/holdout mention
6. **Results** — Ordered evidence stream (sparse main → exact → ablation → external → LOLIB → supplementary EXP6–9 → EXP10)
7. **Discussion** — IPSNS interpretation, limitations, runtime tradeoff, predecessor unified extension
8. **Conclusion** — Bounded summary
9. **Declarations** — unchanged
10. **Appendix (optional in main PDF)** — Full proofs OR defer proofs to Online Resource 1

---

## Ordered restructuring actions

### Phase A — Disclosure and framing (before EXP10 integration)

1. Add **§2.x Author predecessor work** (arXiv:2412.16181, JOCO LR-TA, DAM IPSNS, CAIE/EJCO attempts).
2. Reorder **introduction contribution bullets** — IPSNS first.
3. Add **topological non-uniqueness** paragraph in §4.1 or §4.3.
4. Add **DRMacIver seeding** sentence in §5 (placeholder for EXP10 numbers).

### Phase B — After EXP10 finalize

5. Insert **§6.x Stochastic robustness (EXP10)** with win/tie/loss distributions.
6. Update abstract final sentence on repeated-run validation.
7. Reconcile any claim if DRMacIver win record shifts under repetitions.

### Phase C — Holdout integration

8. Add **§5 parameter selection** paragraph citing holdout tuning on held-out instances (conservative wording).
9. Cross-reference holdout chosen defaults with code constants in OR1 README.

### Phase D — Length control

10. **Move to Online Resource 1:**
    - Full proofs of Props 1–4
    - Per-instance EXP4 table
    - EXP10 diagnostic CSVs (seed improvement, accepted/rejected counts)
    - Holdout full run log summary
    - Extended ablation tables
11. **Consolidate main-text tables** to ≤8–10:
    - Algorithm components + invariants (merge or keep both — high value for rigor objections)
    - Experiment overview
    - Sparse external baselines (EXP4)
    - Paired tests
    - Exact small (EXP3)
    - MIP medium (EXP8) — or merge with exact subsection
    - Ablation (EXP2)
    - LOLIB scope (EXP5)
    - Budget curve (EXP6) — consider figure-only with key numbers in text
12. Target **25–35 PDF pages** (COAP compliance audit guidance).

---

## Component placement decisions

| Component | Placement | Rationale |
|-----------|-----------|-------------|
| LR-TA | Methods §4.1, not intro novelty hook | Prior JOCO paper; avoids novelty rejection |
| WMSF | Methods §4.2 as seed | CC25 attribution |
| IPSNS | Methods §4.3 + intro lead | Main new content |
| Props | §4.4 statements; proofs in OR1 | Addresses rigor without theory-paper misclassification |
| EXP7/EXP9 | Results subsubsection or OR1 if space tight | Supporting not headline |

---

## Dense LOLIB framing (do not change scientifically)

Keep as **§6.x Scope boundary experiment** — title table caption must retain “not evidence for universal dominance.” This directly answers prior RR-004 criticism and **helps** COAP submission.

---

## Predecessor disclosure placement

| Location | Content |
|----------|---------|
| Cover letter | Full lineage + outcomes (author-supplied) |
| §2 new subsection | Scholarly citation-style disclosure |
| Online Resource 1 | Overlap matrix (algorithm × manuscript table from RELATED_MANUSCRIPT_CONTRIBUTION_MATRIX.md) |
| Portal uploads | PDFs of predecessors + EJCO + arXiv |

---

## Limitations placement

Keep consolidated in **§7 Discussion** with bullet list:
- Sparse nonnegative regime
- LOLIB dense boundary
- No approximation ratio
- Training-free baseline scope
- DRMacIver wrapper incompletions
- Parameter tuning scope (holdout + EXP2)

Do not bury limitations only in conclusion.

---

## 40-page assessment

CAIE anonymized PDF was **44 pages** — flagged as excessive. COAP target shorter. **Recommendation:** 30±5 pages main text + Online Resource 1 for extended material. Not a rejection reason if supplement holds overflow, but reviewer fatigue is real (taxonomy E).
