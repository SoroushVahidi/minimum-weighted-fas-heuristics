# Rejection Reason Taxonomy

**Audit date:** 2026-06-11  
**Source register:** `REJECTION_REASON_MASTER_REGISTER.csv` (32 items)

Each item is mapped to taxonomy categories A–H. Items marked **[INFER]** are editorial-risk inferences, not documented referee quotes.

---

## A. Novelty (7 items)

| ID | Summary | Source type |
|----|---------|-------------|
| RR-001 | Local-ratio is prior art (Bar-Yehuda / DF03 lineage) | Planning register |
| RR-007 | WMSF is CC25 reimplementation, not novel | Claim boundaries |
| RR-009 | Insufficient novelty if framed as theorem paper | Venue note [INFER] |
| RR-016 | Salami slicing between LR-TA and IPSNS split papers | Audit inference |
| RR-017 | arXiv:2412.16181 undisclosed author predecessor | Audit finding |
| RR-026 | Predecessor DAM abstract overclaims vs prior published results | Predecessor text |
| RR-031 | Contribution list leads with LR-TA not IPSNS | Framing audit |

**COAP mitigation:** Center IPSNS; cite predecessors; formal Props as new unified analysis; disclose arXiv.

---

## B. Experimental evidence (11 items)

| ID | Summary |
|----|---------|
| RR-003 | Missing learning baselines (GNNRank) |
| RR-004 | Dense LOLIB: DRMacIver beats IPSNS |
| RR-005 | Need synthetic/larger-scale instances |
| RR-008 | Experimental completeness and framing |
| RR-010 | JOCO benchmark breadth limitation |
| RR-011 | Need stronger exact/ILP on medium instances → EXP8 |
| RR-012 | IPSNS vs generic local search → EXP7 |
| RR-018 | DRMacIver single-run limitation |
| RR-023 | IPSNS parameter sensitivity |
| RR-025 | sfas baseline unresolved |
| RR-028 | No stochastic repetitions → EXP10 |

**COAP mitigation:** EXP6–EXP10 + holdout; transparent LOLIB; scoped baseline set with rationale.

---

## C. Technical correctness (5 items)

| ID | Summary |
|----|---------|
| RR-002 | No approximation ratio / formal bound |
| RR-013 | Topological linear extension non-uniqueness [INFER/unverified] |
| RR-024 | Terminology: minimum weighted FAS consistency |
| RR-014 | Insufficient mathematical backbone (addressed by Props) |
| RR-029 | EXP2 ablation numbers need raw recomputation |

---

## D. Positioning and scope (4 items)

| ID | Summary |
|----|---------|
| RR-004 | Dense vs sparse scope (also B) |
| RR-027 | C&OR vs CAIE scope mismatch [INFER] |
| RR-009 | Venue fit for computational vs theory paper |
| RR-008 | Framing vs ranking generality |

**COAP fit:** Strong for algorithm engineering + computational validation; weaker if sold as approximation theory.

---

## E. Writing and presentation (5 items)

| ID | Summary |
|----|---------|
| RR-022 | Manuscript length / table density |
| RR-031 | Contribution ordering |
| RR-014 | Algorithm description vs formalism balance |
| RR-008 | Framing clarity |
| RR-026 | Predecessor hype language contrast |

---

## F. Reproducibility and artifact (6 items)

| ID | Summary |
|----|---------|
| RR-006 | Code not verifiable / private repo |
| RR-019 | No automated tests |
| RR-020 | No COAP Online Resource 1 |
| RR-029 | Dependency pinning / clean-machine gap |
| RR-018 | DRMacIver binary checksum missing |
| RR-006 | Supplement weak vs “fully reproducible” claim |

---

## G. Publication ethics and disclosure (5 items)

| ID | Summary |
|----|---------|
| RR-017 | arXiv undisclosed |
| RR-016 | Salami slicing |
| RR-030 | Simultaneous submission concern |
| RR-015 | Reuse predecessor result numbers |
| RR-032 | COAP portal related-manuscript uploads missing |

---

## H. Editorial and formatting (4 items)

| ID | Summary |
|----|---------|
| RR-021 | Cover letter false originality |
| RR-032 | Portal compliance |
| RR-028 | HiGHS citation (MIN-04) |
| RR-022 | Page length vs COAP norms |

---

## Editorial-risk inferences (not documented rejections)

These structural weaknesses **[INFER]** may have contributed to prior rejection even without stored reports:

1. Manuscript historically led with LR-TA rather than IPSNS (JOCO/DAM split).
2. Claiming novelty in standard mechanisms (local-ratio peeling, Kosaraju SCC).
3. Weak differentiation from arXiv:2412.16181 without citation.
4. External baseline breadth questioned until EXP4/EXP8/EXP7 added.
5. Single-run DRMacIver comparisons until EXP10.
6. Ranking framing vs general MWFAS claims without sparse/dense boundary.
7. Elementary propositions presented as if they were approximation theorems (mitigated in COAP).
8. No authoritative best-known benchmark claim (COAP correctly avoids this).
9. Overly broad conclusions in predecessor DAM abstract.
10. WMSF provenance ambiguity (resolved in COAP).
11. Missing reproducibility package at submission time.
12. Manuscript length and table density (CAIE 44 pp).
13. Cover letter “not published previously” incompatible with arXiv + predecessors.
14. COAP is better venue fit than CAIE for formal analysis + optimization framing **[INFER]**.

---

## Severity ranking (for revision priority)

| Rank | Issue | Category |
|------|-------|----------|
| 1 | Undisclosed author predecessors + portal uploads | G, H |
| 2 | EXP10 incomplete — DRMacIver stochastic claim | B |
| 3 | No COAP Online Resource 1 / tests | F |
| 4 | Cover letter accuracy | G, H |
| 5 | Novelty framing (IPSNS first) | A, E |
| 6 | Holdout integration for parameters | B |
| 7 | Manuscript length consolidation | E |
| 8 | Topological non-uniqueness paragraph | C, E |
