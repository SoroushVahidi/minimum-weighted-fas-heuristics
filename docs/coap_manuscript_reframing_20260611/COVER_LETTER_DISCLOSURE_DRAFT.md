# Cover Letter Disclosure Draft (paragraph only)

**Not a full cover letter.** Use in COAP submission letter after author fills `% AUTHOR-STATUS` placeholders.

---

## Draft disclosure paragraph

This manuscript extends several related lines of work by the author rather than presenting every algorithmic ingredient as newly invented. A public preprint with Ioannis Koutis (arXiv:2412.16181, December 2024) formulates ranking from pairwise comparisons as minimum weighted feedback arc set and reports combinatorial heuristics including local-ratio-inspired cycle reduction, feasible reinsertion, and topological ranking extraction; the present paper does not claim those foundations as new and cites that preprint explicitly.

The LR-TA seed inherits directed local-ratio cycle reduction from Demetrescu and Finocchi (2003) and was developed further in an earlier author manuscript archived in our repository (“Fast Local-Ratio Cycle Reduction with Topological Add-Back for Weighted Feedback Arc Sets”); the Phase I/Phase II implementation in the current study matches that predecessor at code level and is refined here as an engineered sparse-graph seed rather than as a new approximation theorem. IPSNS appeared in a separate archived author manuscript targeting Discrete Applied Mathematics together with a WMSF-style seed; the COAP submission preserves IPSNS as the primary new integrated contribution while adding LR-TA as an additional seed, unified formal supporting properties, and an expanded experimental program.

The WMSF-style seed is an engineered implementation variant of the weighted minimal-and-stable feedback arc set method of Cavallaro and Cutello (SEKE 2025, paper 049), extending the earlier minimal-and-stable line of Cavallaro, Cutello, and Pavone (Journal of Combinatorial Optimization, 2024); it is not introduced here as a separate new algorithm. Relative to all of the above, the incremental contribution of this COAP submission is IPSNS with incumbent-protected SCC-local destroy-and-repair; unification of LR-TA and the WMSF-style seed under one evaluation pipeline; exact and mixed-integer validation; expanded sparse benchmarks with external baselines; holdout-supported parameter interpretation; a dense LOLIB scope boundary; and supporting correctness analysis.

The repository also contains manuscript packages prepared for *Computers & Industrial Engineering* and the *EURO Journal on Computational Optimization*; preparation of a package in the repository does not by itself establish submission history. [AUTHOR: insert exact prior submission dates, manuscript IDs, and outcomes for JOCO LR-TA, DAM IPSNS, CAIE, and EJCO where applicable.]

Code, configurations, and committed summary outputs accompany the submission; Online Resource 1 will consolidate the final supplementary archive at submission.

---

## Phrases to avoid in the cover letter

- “This work has not been published in any form.”
- “No related manuscript exists.”
- “All algorithms are new.”
- “The submission is entirely independent of prior work.”
