# SNCS Pass 2B Changelog

**Date:** 2026-06-17
**Branch:** `sncs-retargeting`
**Purpose:** targeted manuscript edits responding to `docs/sncs_preparation_202606/REJECTION_RISK_AUDIT_PASS2A.md`

## Files edited

- `paper_sncs/main.tex`
- `paper_sncs/sections/01_introduction.tex`
- `paper_sncs/sections/02_related_work.tex`
- `paper_sncs/sections/04_algorithmic_framework.tex`
- `paper_sncs/sections/05_experimental_design.tex`
- `paper_sncs/sections/07_discussion.tex`
- `paper_sncs/bibliography/references.bib`
- `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md`
- `docs/sncs_preparation_202606/CHANGELOG_SNCS_PASS2B.md`

## References added

New BibTeX entries added in this pass:

- `GJR22` — Gr{\"o}tschel, J{\"u}nger, Reinelt, comment on the Baharev et al. exact MFAS method
- `BH11TR` — Brandenburg and Hanauer technical report on sorting heuristics for FAS
- `CCP23CEUR` — Cavallaro, Cutello, Pavone, ITADATA / CEUR minimal-FAS heuristics paper
- `GLT23` — Geladaris, Lionakis, Tollis, PageRank-based FAS heuristic
- `Hanauer2017thesis` — Hanauer dissertation on sparse linear orderings

Verified references already present and therefore not duplicated:

- `HGH21`
- `BSNA21`
- `SST16`
- `BH13`
- `CCP24`
- `CC25`
- `VahidiKoutis2024arxiv`

## References considered but not added

- No separate older dicycle-inequality / cutting-plane reference beyond `GJR22` was added in this pass because exact metadata was not harvested during this run and the requested exact-method comment already covers the immediate formulation discussion needed for the manuscript edit.

## Abstract and acronym readability changes

- Rewrote the abstract methods sentence so the method idea appears before `IPSNS`.
- Introduced “strongly connected components” before `SCC` in the abstract.
- Removed early abstract naming of `LR-TA` and `WMSF-style`; the abstract now refers to “two attributed constructive seeds.”
- Replaced repeated early acronym emphasis with “the refinement” / “this refinement method” wording where appropriate.

## Novelty and contribution changes

- Reframed the introduction around sparse nonnegative weighted digraphs as the target regime.
- Made the novelty claim explicit: the new contribution is the incumbent-protected SCC-local refinement layer, not the attributed seeds.
- Added a clearer contribution list covering problem focus, algorithmic novelty, attribution/supporting analysis, and computational contribution.
- Added explicit non-worsening language: only strict global improvements are accepted, so the method cannot return a worse solution than its incumbent.
- Added the reviewer-facing significance sentence explaining that the value lies in selective strengthening without regressions, not universal improvement on every instance.

## Related-work changes

- Expanded the exact-method context to cite `BSNA21` together with `GJR22`.
- Added modern sparse/general heuristic context for TIGHT-CUT / TIGHT-CUT*, web-scale heuristic engineering, PageRankFAS, and the minimal-feedback line.
- Added sparse-versus-dense ordering context using `Hanauer2017thesis` and the prior ranking-oriented `VahidiKoutis2024arxiv` reference.
- Clarified that the present paper is about sparse weighted digraphs, while dense ranking / LOLIB work is related but distinct context.

## Baseline-selection rationale added

- Added a paragraph in `paper_sncs/sections/05_experimental_design.tex` separating:
  - internal constructive baselines,
  - transparent weighted calibrators,
  - external library baseline,
  - external executable comparator,
  - exact / certifying validation tools.
- Added explicit why-not-implemented language for TIGHT-CUT*, minimal-FAS heuristics, web-scale ordering heuristics, and PageRankFAS.
- Recorded that TIGHT-CUT* is the closest future additional sparse FAS baseline, but not required for the current scoped claim.

## Method and parameter self-containedness improvements

- Brought the essential LR-TA and WMSF-style behavior more clearly into the main text instead of leaving the reader dependent on Online Resource 1.
- Added main-text wording that IPSNS neighborhoods are restricted to cyclic SCCs.
- Added main-text wording that repair reruns local-ratio reduction and heavy-first add-back only inside the selected neighborhood.
- Added main-text wording that repeated runs vary only by explicit seeds and that the reported defaults are fixed across instances once selected by holdout.
- Added explicit “no instance-specific tuning” language for the reported comparisons.

## Scope and limitation changes

- Tightened the discussion so the claim is explicitly “among the evaluated methods.”
- Added an explicit sparse-regime limitation.
- Strengthened the LOLIB dense-boundary statement: dense complete-ordering benchmarks are better aligned with dense matrix-based methods.
- Added a comparator-scope limitation stating that the comparison set is broad but not exhaustive.
- Preserved the paper’s non-universal claim language.

## Build and bundle refresh

- `latexmk -pdf main.tex`: succeeded.
- `paper_sncs/main.pdf` page count: **27**.
- `paper_sncs/main.pdf` SHA-256: `38159c605baf63f7150560fa45287505f08073b3eab17aa845201727932a46e8`
- Refreshed `paper_sncs/submission/sncs_initial/Vahidi_SNCS_Manuscript.pdf`.
- Rebuilt `paper_sncs/submission/sncs_initial/Vahidi_SNCS_Source.zip` as the backup source package using the repository’s existing packaging convention.
- Regenerated `paper_sncs/submission/sncs_initial/MANIFEST.sha256`.

## Remaining risks

- Pass 2C still needs a careful human read of the edited SNCS manuscript for overall flow, claim balance, and line-level polish.
- No new experiments were run in this pass, and no new baseline implementation was attempted.
- A future additional sparse comparator such as TIGHT-CUT* remains optional follow-up work, not a blocker for the current scoped manuscript.
- The submission bundle still correctly recommends PDF-only initial upload; the source ZIP remains backup only and is not flattened for portal-source upload.
