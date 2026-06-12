# Manuscript Writing Plan

## Target Journal

Primary target: Computers & Industrial Engineering. The manuscript should emphasize weighted cyclic-ordering problems in engineering systems, practical heuristic design, reproducible computation, and scope-aware empirical validation.

Alternative adaptation: Computers & Operations Research. A C&OR version should strengthen mathematical framing, add more theoretical discussion, and possibly add newer or learning-based baselines before submission.

## Thesis

The paper argues that a reproducible combination of engineered local-ratio cycle reduction, topological add-back, weighted seeding, and incumbent-protected strongly connected component refinement is an effective heuristic framework for nonnegative sparse weighted directed graphs. The main contribution is not a new approximation guarantee or a universal ordering solver; it is a carefully bounded algorithm-engineering study with exact validation, ablation evidence, external baselines, and a dense linear-ordering transfer test that exposes the method's limits.

## Final Contributions

- Engineered local-ratio topological add-back for nonnegative weighted feedback arc set instances.
- Incumbent-protected SCC neighborhood refinement with an auditable non-worsening invariant relative to the best internal seed.
- Computational validation spanning sparse public benchmarks, exact small instances, ablations, external baselines, and dense LOLIB transfer tests.
- Explicit claim boundaries for negative weights, dense complete ordering instances, weighted Eades adaptation, and absence of a new approximation theorem.

## Section Plan

- Introduction: motivate weighted cyclic ordering, define the evidence-backed scope, state bounded contributions, and preview the dense LOLIB limitation.
- Related work: feedback arc set, local-ratio methods, Eades-style heuristics, exact methods, linear ordering, and ranking from pairwise comparisons.
- Problem definition: directed graph notation, backward weight, feedback arc set equivalence, and dense LOLIB forward/backward relation.
- Algorithmic framework: LR-TA, WMSF seed, IPSNS, invariant, and implementation details.
- Experimental design: datasets, exclusions, baselines, parameters, metrics, reproducibility.
- Results: compact manuscript tables for sparse baselines, exact validation, ablation, and LOLIB scope.
- Discussion: why sparse graphs favor SCC-local refinement, why dense complete tournaments favor tournament-native solvers, limitations, and reviewer-risk mitigation.
- Conclusion: bounded summary and reproducibility statement.

## Reuse From Predecessor Manuscripts

- Basic problem motivation and notation, rewritten and verified.
- Prior local-ratio and heuristic context, with original citations checked.
- High-level method organization where it matches current code.
- Declarations/data-availability structure if consistent with Elsevier requirements.

## Do Not Reuse

- Any predecessor experimental results.
- Any novelty wording that implies local-ratio itself is new.
- Any universal state-of-the-art claim.
- Any dense-LOP dominance claim.
- Any text that assumes the repository is already public.
- Any claims involving negative-weight instances as standard MWFAS evidence.

## Claim Boundaries

- Standard claims apply to nonnegative weighted directed graphs.
- Negative-weight instances are excluded from standard comparisons.
- IPSNS provides incumbent non-worsening relative to internal seeds, not an approximation ratio.
- WMSF is a seed/baseline, not a central novelty claim.
- Weighted Eades is an in-repository weighted adaptation of Eades et al. (1993).
- LOLIB is a dense complete linear-ordering transfer test and shows a scope boundary.
- Repository-public and DOI claims remain TODO until release.

## Expected Main Tables

- Sparse external baselines: `paper/tables/table_sparse_external_baselines.tex`.
- Exact small validation: `paper/tables/table_exact_validation.tex`.
- Ablation: `paper/tables/table_ablation.tex`.
- Dense LOLIB scope: `paper/tables/table_lolib_scope.tex`.
- Optional later table: algorithm components and invariants.

## Expected Figures

- Relative mean backward weight on sparse external baselines.
- Win-count chart for sparse external baselines.
- Exact-gap distribution for small instances.
- LOLIB per-family comparison between IPSNS and DRMaciver.
- Ablation or convergence figure showing add-back and refinement effects.

## Citation TODOs

- Verify and add the foundational local-ratio reference from Bar-Yehuda et al.
- Add official citations or stable references for DRMaciver/Feedback-Arc-Set and python-igraph.
- Verify LOLIB references and add Marti, Reinelt, Duarte, Laguna, and Glover entries if missing.
- Verify dataset provenance for alidasdan/graph-benchmarks.
- Decide whether GNNRank, LOP_MA-EDM, Baharev exact MWFAS, Simpson--Srinivasan, and Cavallaro--Cutello--Pavone belong in related work.

## Journal Guideline TODOs

- Verify current Computers & Industrial Engineering aims and scope.
- Verify current Elsevier author-guide requirements for article type, word limits, figures, data availability, declarations, and highlights.
- Verify whether graphical abstract, highlights, or credit author statement are required.
- Verify current editor and area fit before writing the cover letter.
