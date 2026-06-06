# Predecessor Project Manifest

**Date inspected:** 2026-06-06  
**Repository:** `SoroushVahidi/minimum-weighted-fas-heuristics`  
**Purpose:** Provenance record for files originating from the two predecessor paper
submissions that were merged into this repository.

---

## Predecessor 1 — LR-TA Paper (Local Ratio)

| Field | Value |
|---|---|
| GitHub repo | `https://github.com/SoroushVahidi/weighted-minfas-local-ratio` |
| Algorithm | LR-TA: Local-Ratio cycle reduction with Topological Add-Back |
| Venue | JOCO (Journal of Combinatorial Optimization) |
| Archive file | `archive/predecessor_projects/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO.zip` |
| Archive contents | `main.tex` (manuscript), `references.bib`, `history.txt`, `readme.txt`, Springer template files (`svjour3.cls`, etc.), `example.pdf`, `example.eps` |
| Original notebook | `notebooks/local_ratio_original/feeback-arc-set-codes.ipynb` |
| Current code | `src/mwfas/lrta.py` |
| README preserved | `docs/provenance/README_weighted-minfas-local-ratio.md` |

**What was preserved:**
- LaTeX manuscript ZIP → `archive/predecessor_projects/`
- Original notebook → `notebooks/local_ratio_original/`
- README from predecessor repo → `docs/provenance/`

**What was not copied:**
- Raw result files from the predecessor repo (not present in the ZIP; only manuscript source)
- Predecessor repo history (use GitHub URL above)

---

## Predecessor 2 — IPSNS/WMSF Paper

| Field | Value |
|---|---|
| GitHub repo | `https://github.com/SoroushVahidi/weighted-minfas-codes` |
| Algorithms | IPSNS (Incumbent-Protected SCC Neighborhood Search) + WMSF |
| Venue | Elsevier journal |
| Archive file | `archive/predecessor_projects/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem.zip` |
| Archive contents | `cas-refs.bib`, `references.bib`, `grabs.pdf`, Elsevier template class/bst files |
| Original notebook | `notebooks/ipsns_original/feeback-arc-set-codes.ipynb` |
| Current code | `src/mwfas/ipsns.py`, `src/mwfas/wmsf.py` |
| README preserved | `docs/provenance/README_weighted-minfas-codes.md` |

**What was preserved:**
- LaTeX manuscript ZIP → `archive/predecessor_projects/`
- Original notebook → `notebooks/ipsns_original/`
- README from predecessor repo → `docs/provenance/`

**What was not copied:**
- Predecessor repo history
- Raw result files (not in ZIP)

---

## Merge Notes

Both predecessor repos contained **identical notebooks** (`feeback-arc-set-codes.ipynb`)
with three algorithm cells: LR-TA, WMSF, and IPSNS side by side.

The unified `minimum-weighted-fas-heuristics` repository:
1. Preserves the original notebooks verbatim in `notebooks/`
2. Extracts and modularizes all algorithm code into `src/mwfas/`
3. Replaces hard-coded paths with `--input`/`--output` CLI arguments
4. Adds a full experimental framework (`experiments/`, `scripts/`)
5. Adds external baselines (`src/mwfas/baselines.py`, EXP4)
6. Documents all experiments (EXP1b through EXP4, with EXP5 planned)

The **current maintained implementation** is entirely in `src/mwfas/`. The predecessor
notebooks and ZIPs are archived for provenance only and should not be modified.

---

## Claim Boundaries

- **LR-TA topological add-back** is the novel contribution from the LR-TA predecessor.
  The local-ratio framework is prior art; only the add-back phase is claimed as new.
- **IPSNS** is the novel contribution from the IPSNS predecessor: SCC-local LNS with
  incumbent protection guaranteeing no-worsening against both seed solutions.
- **WMSF** is a reimplementation of the paper049 removeArcs/Minimize/Stabilize pipeline,
  used as a seed and baseline — not a novel contribution.
- Do **not** claim a new approximation ratio; IPSNS is a heuristic without ratio guarantees.
