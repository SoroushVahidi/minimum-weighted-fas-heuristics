# Commit Plan — COAP Submission Branch
**Date:** 2026-06-11  
**Current HEAD:** 80b3144d5fdbbe250faed8a4fe671dde2da76c89  
**Branch:** main

---

## Current Uncommitted State

| File | Status | Description |
|------|--------|-------------|
| `src/mwfas/ipsns.py` | Modified (unstaged) | 7 diagnostic counter variables, all gated on `return_info=True` |
| `docs/full_repository_audit_20260610/` | Untracked | Prior session audit documents |
| `experiments/coap_ipsns_holdout/checkpoints/` | Untracked | Holdout checkpoint files |
| `experiments/coap_ipsns_holdout/results/` | Untracked | Holdout result files |
| `experiments/exp10_stochastic_robustness/` | Untracked | EXP10 full infrastructure + in-progress outputs |
| `logs/coap_ipsns_holdout/` | Untracked | Holdout logs |
| `docs/final_branch_audit_20260611/` | Untracked | This audit (25 files being created) |

---

## Proposed Commit Sequence

### Commit 1: IPSNS diagnostic counters
**When:** Immediately (changes are safe and complete)  
**Files:**
```bash
git add src/mwfas/ipsns.py
```
**Message:**
```
Add EXP10 diagnostic counters to IPSNS

Seven counters (_n_accepted, _n_rejected, _n_failed_repair,
_n_topo_failed, _n_noop, _best_iter, _time_to_best) added to
lns_merge_wmsf_lr_best_incumbent. All gated on return_info=True;
zero impact on production runs or experiment results.
```

### Commit 2: COAP sensitivity holdout outputs
**When:** After Commit 1  
**Files:**
```bash
git add experiments/coap_ipsns_holdout/checkpoints/
git add experiments/coap_ipsns_holdout/results/
git add logs/coap_ipsns_holdout/
```
**Message:**
```
Add completed COAP IPSNS sensitivity holdout outputs

1290/1290 runs complete across 65 instances × varied seed configurations.
Results support sensitivity analysis in §6. COMPLETED.ok sentinel present.
```
**Note:** Check size before adding — checkpoint directories can be large.

### Commit 3: EXP10 infrastructure (scripts and config only)
**When:** After EXP10 begins but before results are complete  
**Files:**
```bash
git add experiments/exp10_stochastic_robustness/scripts/
git add experiments/exp10_stochastic_robustness/config/
```
**Message:**
```
Add EXP10 stochastic robustness experiment infrastructure

Scripts and configuration for 20-seed IPSNS × 20-rep DRMacIver
comparison across 93 common instances. Checkpoint-based, fully
resumable. Validates robustness of EXP4 37/55/1 result.
```

### Commit 4: EXP10 results and completed outputs
**When:** After EXP10 fully complete (IPSNS + DRMacIver + postprocessing)  
**Files:**
```bash
git add experiments/exp10_stochastic_robustness/checkpoints/
git add experiments/exp10_stochastic_robustness/results/
git add experiments/exp10_stochastic_robustness/logs/
```
**Message:**
```
Add EXP10 stochastic robustness results

1860 IPSNS runs (93 instances × 20 seeds) and 1860 DRMacIver runs
(93 instances × 20 reps) complete. Summary statistics in results/.
```

### Commit 5: Manuscript EXP10 integration
**When:** After EXP10 results analyzed and manuscript updated  
**Files:**
```bash
git add paper_coap/sections/05_experimental_design.tex
git add paper_coap/sections/06_results.tex
git add paper_coap/sections/07_discussion.tex
git add paper_coap/main.pdf
# Also any new tables/figures
```
**Message:**
```
Integrate EXP10 stochastic robustness analysis into manuscript

Add §5 DRMacIver single-run disclosure, §6 robustness subsection,
§7 discussion of variability across repeated randomized runs.
```

### Commit 6: Repository maintenance
**When:** Before final submission, after all other commits  
**Files:**
```bash
git add requirements.txt          # version pins
git add scripts/drmaciver_fas.sha256  # binary checksum
git add README.md                 # if updated with run instructions
```
**Message:**
```
Add dependency version pins and DRMacIver binary checksum

Pin numpy/pandas/networkx/pyyaml/tqdm to tested versions.
Add SHA-256 checksum for drmaciver_fas binary (commit 16ff24a).
```

### Commit 7: Audit documents
**When:** After all other commits; audit documents are informational  
**Files:**
```bash
git add docs/full_repository_audit_20260610/
git add docs/final_branch_audit_20260611/
```
**Message:**
```
Add pre-submission audit documents (2026-06-10, 2026-06-11)

Repository-wide audit covering algorithm correctness, manuscript
claim verification, COAP compliance, and submission readiness.
All principal claims verified; issues catalogued with action plan.
```

### Commit 8: COAP submission artifact
**When:** Last commit before submission  
**Files:**
```bash
git add submission_package/coap_artifact/  # new COAP artifact
git add submission_files_for_download/     # updated cover letter, highlights
```
**Message:**
```
Add COAP submission package (Online Resource 1 + cover letter)

Supplementary artifact includes src/, experiment scripts, result
summaries, DRMacIver binary, README with run instructions.
Cover letter updated for COAP; prior submission history disclosed.
```

---

## Constraints

- **Never amend already-pushed commits** (main branch; shared with remote)
- **Never force-push to main**
- **Stage only specific files** — do not use `git add -A` or `git add .` (risk of including checkpoints/logs inadvertently)
- **Verify checkpoint directory sizes** before staging — large binary directories should be excluded or gitignored if too large

---

## Suggested .gitignore Additions

Consider adding to `.gitignore` to avoid accidentally staging checkpoint JSON records (which can be large and machine-specific):
```
experiments/*/checkpoints/runs/
experiments/exp10_stochastic_robustness/checkpoints/
experiments/exp10_stochastic_robustness/logs/
```
If these are explicitly intended to be committed, confirm before staging.
