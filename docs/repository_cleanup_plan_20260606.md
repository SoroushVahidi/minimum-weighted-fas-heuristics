# Repository Cleanup Plan — 2026-06-06

**Current HEAD:** `a934037`  
**Purpose:** Pre-EXP5 cleanup and organization pass.

---

## Predecessor ZIP/Archive Files Found

| File | Location | Size | Type |
|---|---|---|---|
| `Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO.zip` | root → `archive/predecessor_projects/` | 198 KB | LaTeX manuscript (JOCO/Springer) |
| `Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem.zip` | root → `archive/predecessor_projects/` | 74 KB | LaTeX manuscript (Elsevier) |

Both ZIPs were previously at the repository root. They contain **LaTeX source for the two predecessor paper submissions**, not code. Moved to `archive/predecessor_projects/` with `git mv`.

## Predecessor README/Doc Files Found

| File | Location | Type |
|---|---|---|
| `docs/README_weighted-minfas-codes.md` | `docs/` → `docs/provenance/` | Predecessor repo README (provenance) |
| `docs/README_weighted-minfas-local-ratio.md` | `docs/` → `docs/provenance/` | Predecessor repo README (provenance) |

Moved to `docs/provenance/` to separate active documentation from historical provenance.

## Original Notebooks

Preserved in place — no move needed:
- `notebooks/local_ratio_original/feeback-arc-set-codes.ipynb` — from `weighted-minfas-local-ratio`
- `notebooks/ipsns_original/feeback-arc-set-codes.ipynb` — from `weighted-minfas-codes`

## Large/Untracked Items

| Path | Status | Action |
|---|---|---|
| `experiments/exp4_external_baselines/external_tools/` | Gitignored (by `experiments/*/external_tools/`) | No action — correctly excluded |
| `experiments/exp4_external_baselines/external_tools/fas-smartAE/snap/*.txt` | 11 MB each, gitignored | No action |
| `results/` | Untracked, gitignored | No action — regenerable |
| `scripts/__pycache__/`, `src/mwfas/__pycache__/`, `src/mwfas.egg-info/` | Untracked, gitignored | Cleaned with `find . -type d -name __pycache__ ...` |

## Documentation Updates

| File | Action |
|---|---|
| `README.md` | Rewritten to reflect current state (EXP1b–EXP4 complete, new scripts, experiments layout) |
| `experiments/README.md` | Created — table of all experiments EXP1b–EXP5 |
| `docs/paper_status_20260606.md` | Created — manuscript readiness and next actions |
| `archive/predecessor_projects/README.md` | Created — archive index |
| `docs/provenance/predecessor_project_manifest.md` | Created — full provenance record |

## .gitignore Status

Reviewed — no changes needed. Current rules correctly:
- Exclude `__pycache__/`, `*.pyc`, `*.egg-info/`, `*.log`, `venv/`, `.venv/`
- Exclude `experiments/*/external_tools/`
- Exclude `experiments/*/raw/`, `results/raw/`, `results/processed/`
- Whitelist `experiments/*/summary/*.csv`, `experiments/*/summary/*.json`,
  `experiments/*/summary/*.md`, `experiments/*/tables/*.csv`

## Remaining Hygiene Issues (Post-Cleanup)

1. **Top-level run scripts** (`run_exp1_core_benchmark_tmux.sh`, `run_exp1b_full_wmsf_seed_tmux.sh`, `run_repro_tmux.sh`) live at the root. These are functional but cluttering. Consider moving to `experiments/exp1*/` in a future pass — not done here to avoid breaking documented paths.
2. **`results/` untracked** — intentional; regenerable from scripts.
3. **`experiments/seedfix_full_wmsf/`** — diagnostic archive from EXP1 investigation. No standard layout. Low priority cleanup.
4. **EXP1 (legacy)** — superseded by EXP1b; preserved for historical completeness.
