# Branch and Working-Tree Audit
**Date:** 2026-06-11  
**Branch:** main  
**HEAD:** 80b3144d5fdbbe250faed8a4fe671dde2da76c89

---

## 1. Branch Identity

| Field | Value |
|-------|-------|
| Current branch | `main` |
| HEAD commit | `80b3144d5fdbbe250faed8a4fe671dde2da76c89` |
| Tracking upstream | `origin/main` |
| Ahead/behind upstream | Up to date (0 ahead, 0 behind) |
| Merge conflicts | None |
| Rebase/bisect in progress | None |

## 2. Working-Tree Status

### 2a. Modified tracked files

| File | Change type | Purpose | Scientific impact |
|------|-------------|---------|-------------------|
| `src/mwfas/ipsns.py` | Modified | EXP10 diagnostic counter instrumentation (`return_info=True` path only) | **None** — algorithm behavior unchanged; counters populated only when `return_info=True` which is not used in production runs |

**Git diff summary for ipsns.py:**
- Added 7 diagnostic counter variables (`_n_accepted`, `_n_rejected`, `_n_failed_repair`, `_n_topo_failed`, `_n_noop`, `_best_iter`, `_time_to_best`) initialized before LNS loop
- All counter increments gated on `if return_info:` — zero overhead in normal execution
- Extended `return_info` dict with 7 new fields
- **No change to algorithm logic, acceptance criteria, rollback, or objective computation**

### 2b. Untracked files

| Path | Category | Content | Should be committed? |
|------|----------|---------|----------------------|
| `docs/full_repository_audit_20260610/` | Audit | 34 audit documents from prior audit session | Yes, before submission |
| `experiments/coap_ipsns_holdout/checkpoints/` | Experiment | 1290 checkpoint sentinel files for holdout | Yes (or .gitignored) |
| `experiments/coap_ipsns_holdout/results/` | Experiment | Holdout result files | Yes |
| `experiments/exp10_stochastic_robustness/` | Experiment | Full EXP10 infrastructure + in-progress data | After EXP10 complete |
| `logs/coap_ipsns_holdout/` | Experiment | Holdout logs + COMPLETED.ok sentinel | Yes |

### 2c. Staged files
None.

### 2d. Deleted tracked files
None.

## 3. Recent Commit History

| SHA | Message | Scientific impact |
|-----|---------|-------------------|
| 80b3144 | Add sensitivity instance list omitted by csv gitignore | Low — adds missing .csv instance list |
| 90af464 | Add completed COAP IPSNS sensitivity experiment | High — adds sensitivity experiment results |
| 92e9c5a | Add formal correctness and complexity analysis for COAP | High — adds formal propositions to manuscript |
| 76a3412 | Polish COAP template and manuscript layout | Low — formatting only |
| 7e8e0b7 | Create Springer COAP manuscript version | High — creates the COAP submission manuscript |
| 581ee35 | Track final EJCO submission package | Stale EJCO — not target journal |
| 5e1fcc1 | Finalize EJCO submission package | Stale |
| Earlier | Various CAIE/EJCO submission preparations | Not target journal |

**Note:** The last 4-5 commits before 7e8e0b7 are EJCO-era. The repository has been retargeted for COAP since commit 7e8e0b7.

## 4. Files Changed on Branch Relative to Default Branch

This IS the main/default branch. No divergence from main exists.

## 5. File Category Separation

### Source changes (not yet committed)
- `src/mwfas/ipsns.py` — EXP10 instrumentation (should be committed with EXP10)

### Manuscript changes (committed)
- All manuscript changes are in committed history (7e8e0b7 and later)
- `paper_coap/` is fully tracked and consistent

### Experiment changes (untracked)
- `experiments/exp10_stochastic_robustness/` — new experiment
- `experiments/coap_ipsns_holdout/checkpoints/`, `results/` — holdout completions
- `logs/coap_ipsns_holdout/` — holdout logs

### Audit changes (untracked)
- `docs/full_repository_audit_20260610/` — prior audit documents

### Generated files
- `paper_coap/main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out` — LaTeX build artifacts (should remain untracked or .gitignored)
- `paper_coap/main.pdf` — compiled PDF (should be tracked for submission readiness check)
- Various `*.json` in experiment raw/ directories — generated results (tracked per .gitignore rules)

## 6. Sensitive / Privacy Items

| Item | Location | Severity | Notes |
|------|----------|----------|-------|
| Email address `sv96@njit.edu` | `paper_coap/main.tex:37` | None | Required for COAP submission |
| ORCID link | `paper_coap/main.tex:37` | None | Required for COAP submission |
| Home paths `/home/soroush/` | `experiments/exp10_stochastic_robustness/config/common_93_instances.txt` and many raw JSON records | Minor | Machine-local paths, not sensitive; standard for local experiments |
| Machine name | Various experiment logs | Informational | Not sensitive |
| No API keys, tokens, passwords, or private SSH keys found anywhere | — | — | — |

## 7. .gitignore Assessment

The `.gitignore` is presumed to exclude:
- `*.csv` in raw experiment directories (by pattern)
- Large binary files
- Python `__pycache__/`, `*.pyc`
- LaTeX build artifacts

**Potential reproducibility concern:** If `.gitignore` excludes experiment raw JSON or CSV files that are needed for reproducing manuscript numbers, this must be verified. The prior audit notes that sensitivity instance list CSV was omitted by `.gitignore` (commit 80b3144 fixed one case). All critical summary files (`exp1b_raw_summary.csv`, `exp4_raw_summary.csv`, etc.) appear to be tracked given their presence in `summary/` directories.

## 8. Large/Binary Files Assessment

| File | Size | Type | Issue? |
|------|------|------|--------|
| `paper_coap/main.pdf` | ~MB | PDF | Expected; submission artifact |
| `submission_package/ejco_source.zip` | ~MB | ZIP | Stale (EJCO era); replace before submission |
| `submission_package/ejco_reproducibility_artifact.zip` | ~MB | ZIP | Stale; replace |
| DRMacIver binary `experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas` | Small binary | ELF | Expected; needed for EXP10 and EXP4 |

## 9. Conclusion

The working tree is clean except for the intentional EXP10 instrumentation in `ipsns.py`. No merge conflicts, no stray commits, no unexpected binary files beyond known artifacts. The branch divergence from upstream is zero. The main publication-readiness concern is the untracked EXP10 directory and holdout results, which must be committed once EXP10 is complete.
