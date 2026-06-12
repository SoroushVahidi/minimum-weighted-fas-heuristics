# Submission Lineage Timeline

**Audit date:** 2026-06-11  
**Evidence standard:** Documentary facts separated from inference (marked **[INFER]**).

---

## Timeline

```
2024-12 ── arXiv:2412.16181 posted
           Authors: Soroush Vahidi, Ioannis Koutis
           Title: Minimum Weighted Feedback Arc Sets for Ranking from Pairwise Comparisons
           Evidence: JOCO predecessor bib entry [V25-2]; NOVELTY audit
           Status: Public preprint (author predecessor)
           Decision materials: None in repo

pre-2026 ── JOCO predecessor manuscript archived
           Author: Soroush Vahidi (single author)
           Title: Fast Local-Ratio Cycle Reduction with Topological Add-Back for Weighted Feedback Arc Sets
           Target: Journal of Combinatorial Optimization
           Algorithms: LR-TA only
           Experiments: 33-instance subset
           Evidence: archive/...JOCO.zip; extracted main.tex
           Status: [INFER] rejected — paper/notes/reuse_risk_report.md only
           Decision materials: None in repo

pre-2026 ── DAM predecessor manuscript archived
           Author: Soroush Vahidi
           Title: Incumbent-Protected SCC-Neighborhood Search for the Weighted Feedback Arc Set Problem
           Target: Discrete Applied Mathematics (\\journal{Discrete Applied Mathematics} in TeX)
           Algorithms: IPSNS + WMSF-style dual seed
           Experiments: 33 benchmarks per predecessor abstract
           Evidence: archive/...Incumbent_Protected...zip; elsarticle-template-harv.tex
           Status: [INFER] rejected — reuse_risk_report.md only
           Decision materials: None in repo

2026-06-06 ── CAIE submission package prepared
           Title: A Reproducible Local-Ratio and SCC-Refinement Framework for Weighted Ordering in Directed Graphs
           Target: Computers & Industrial Engineering (Elsevier)
           Algorithms: Unified LR-TA + WMSF + IPSNS
           Experiments: EXP1b–EXP5 (+ later revision additions)
           Evidence: git d496b8a; cover_letter.txt; final_repository_status_20260606.md
           Status: Package ready; upload manual actions documented; **decision outcome not in repo**
           [INFER] Review or revision cycle suggested by commits:
             - e48b663 EXP8 for CAIE revision ("External reviewers requested...")
             - 7f16b6c EXP7 for CAIE revision
             - c847747 statistical postprocessing for CAIE revision

2026 (post-CAIE) ── EJCO submission package prepared
           Title: Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem
           Target: EURO Journal on Computational Optimization (Springer)
           Evidence: submission_package/ejco_source/; git 581ee35
           Cover letter: claims original / not under consideration elsewhere
           Status: Package in repo; **decision outcome not in repo**

2026-06 ── COAP manuscript created
           Same scientific title as EJCO
           Target: Computational Optimization and Applications (Springer Nature)
           Evidence: git 7e8e0b7; paper_coap/
           Additions vs EJCO: Springer sn-jnl template; formal analysis §4.4;
             holdout study; EXP10 stochastic robustness (in progress)
           Status: Current submission target — not yet submitted

2026-06-11 ── EXP10 running (passive audit observation)
           IPSNS phase: 1860/1860 complete (per exp10 summaries)
           DRMacIver phase: in progress (~21% at audit time)
           No modification during this audit
```

---

## Venue resolution table

| Abbreviation in user query | Resolved full name | Submitted? | Evidence |
|----------------------------|-------------------|------------|----------|
| arXiv:2412.16181 | arXiv preprint | Posted publicly | JOCO bib + novelty audit |
| JOCO | Journal of Combinatorial Optimization | Predecessor target | JOCO ZIP |
| CAIE | Computers & Industrial Engineering | Package prepared | git + cover letter |
| EJCO | EURO Journal on Computational Optimization | Package prepared | submission_package/ |
| COAP | Computational Optimization and Applications | Target (in prep) | paper_coap/ |
| DAM | Discrete Applied Mathematics | Predecessor target | DAM TeX \\journal{} |
| Elsevier (IPSNS manifest) | Resolved to DAM above | Predecessor | predecessor manifest + TeX |
| COR | Computers & Operations Research | Considered only | venue_decision_notes |
| EAAI | Engineering Applications of Artificial Intelligence | **Not found** | — |
| Applied Intelligence | Springer journal | **Not found** | — |
| Digital Engineering | **Not found** | — |
| MLJ | Machine Learning Journal | **Not found** | — |
| KBS | Knowledge-Based Systems | **Not found** | — |
| OPSEARCH | OPSEARCH journal | Listed audit-needed | RELATED_MANUSCRIPTS_AUDIT_NEEDED.md |

---

## Algorithm evolution across lineage

| Component | arXiv-VK | JOCO-V | DAM-V | CAIE/EJCO/COAP |
|-----------|----------|--------|-------|----------------|
| LR-TA Phase I/II | ? | ✓ | ~ | ✓ |
| WMSF seed | ? | ✗ (cited CC25) | ✓ | ✓ |
| IPSNS | ? | ✗ | ✓ | ✓ |
| Formal Props 1–4 | ✗ | ✗ | ✗ | ✓ (COAP) |
| EXP4 external baselines | ? | partial | ? | ✓ |
| LOLIB scope test | ? | ✗ | ? | ✓ |
| EXP10 stochastic | ✗ | ✗ | ✗ | ✓ (COAP, pending) |

---

## Relationship to current COAP manuscript

The COAP submission is a **unified extension** of:

1. JOCO LR-TA line (same implementation in `src/mwfas/lrta.py`)
2. DAM IPSNS/WMSF line (same implementation in `src/mwfas/ipsns.py`, `wmsf.py`)
3. CAIE/EJCO merged experimental manuscript (shared TeX lineage in `paper/` → `submission_package/ejco_source/` → `paper_coap/`)

It is **not** a wholly new problem formulation relative to arXiv:2412.16181 (ranking-as-MWFAS), but it **is** a substantially expanded unified treatment with formal analysis and broader validation — **provided disclosure is complete.**

---

## Missing documentary items (author action)

- [ ] CAIE decision letter / manuscript ID / outcome
- [ ] EJCO decision letter / manuscript ID / outcome
- [ ] JOCO decision letter (if submitted beyond archive)
- [ ] DAM decision letter
- [ ] Any email correspondence referenced in venue_decision_notes (“email history”)
- [ ] Full text of arXiv:2412.16181 for overlap diff
- [ ] OPSEARCH / other venue manuscripts if they exist

Store these in `docs/coap_rejection_history_and_revision_plan_20260611/` or a secure non-repo location and update `PRIOR_DECISION_AND_REVIEW_REGISTER.csv` with exact quotes.
