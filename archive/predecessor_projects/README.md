# Archive: Predecessor Project Files

This directory contains files from the two predecessor paper submissions that were
merged into this repository. They are kept for provenance and historical reference.

---

## Files

### `Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO.zip`

- **Contents:** LaTeX manuscript source (JOCO / Springer format) for the LR-TA paper
- **Includes:** `main.tex`, `references.bib`, `history.txt`, `readme.txt`,
  Springer journal class files (`svjour3.cls`, etc.), example figures
- **Algorithm covered:** LR-TA (Local-Ratio cycle reduction with Topological Add-Back)
- **Venue:** JOCO (Journal of Combinatorial Optimization) submission
- **Status:** Predecessor paper; current implementation is in `src/mwfas/lrta.py`

### `Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem.zip`

- **Contents:** LaTeX manuscript source (Elsevier format) for the IPSNS paper
- **Includes:** `cas-refs.bib`, `references.bib`, `grabs.pdf`, Elsevier template files
- **Algorithm covered:** IPSNS (Incumbent-Protected SCC Neighborhood Search)
- **Venue:** Elsevier journal submission
- **Status:** Predecessor paper; current implementation is in `src/mwfas/ipsns.py`

---

## Relationship to Current Repository

The current `minimum-weighted-fas-heuristics` repository **merges** both predecessor
works into a unified codebase. See `docs/repository_notes.md` for the merge details
and `docs/provenance/predecessor_project_manifest.md` for the full provenance record.

Code extracted from both predecessors is maintained under `src/mwfas/`. The original
notebooks from both predecessor repositories are preserved under:
- `notebooks/local_ratio_original/` — from `weighted-minfas-local-ratio`
- `notebooks/ipsns_original/` — from `weighted-minfas-codes`
