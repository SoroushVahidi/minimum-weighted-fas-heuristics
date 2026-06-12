# Title Options and Decision

**Audit date:** 2026-06-11  
**Previous title:** Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem

---

## Evaluation criteria

Scientific accuracy, COAP fit, distinction from arXiv:2412.16181 (ranking/pairwise framing), IPSNS prominence, searchability, manageable length.

---

## Five candidates

| # | Title | Pros | Cons |
|---|-------|------|------|
| T1 | **SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs** | IPSNS-forward; sparse scope explicit; no local-ratio novelty trap; distinct from ranking preprint title | Long; omits seed framework |
| T2 | Incumbent-Protected SCC Refinement for Minimum Weighted Feedback Arc Set on Sparse Weighted Digraphs | Highlights IPSNS invariant | Less searchable; long |
| T3 | Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem | Current; accurate components | **LR-TA leads**; indistinguishable from EJCO package; underplays IPSNS |
| T4 | Computational Heuristics for Minimum Weighted Feedback Arc Set: SCC-Local Refinement on Sparse Digraphs | COAP computational framing | Generic; weak IPSNS signal |
| T5 | Minimum Weighted Feedback Arc Set on Sparse Digraphs: An SCC-Local Destroy-and-Repair Framework | Problem-first | Colon title; still long |

---

## Selected title

**T1:** SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs

**Running head:** SCC-Local Heuristics for MWFAS on Sparse Digraphs

**Rationale:** The prior title foregrounded local-ratio seeding, repeating a framing pattern associated with earlier rejections and with the JOCO predecessor. The selected title states the primary algorithmic mechanism (SCC-local destroy-and-repair = IPSNS), the optimization problem (MWFAS), and the empirical scope (sparse digraphs) without implying a new local-ratio theory or universal FAS dominance. It is clearly distinct from arXiv:2412.16181’s ranking-from-pairwise-comparisons title while remaining searchable under MWFAS and feedback arc set keywords.

**Manuscript updated:** `paper_coap/main.tex` `\title[...]{...}`
