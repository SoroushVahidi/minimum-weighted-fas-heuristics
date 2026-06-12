# Git Provenance Reconciliation

**Date:** 2026-06-12  
**Repository:** /home/soroush/minimum-weighted-fas-heuristics  
**Remote:** https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics

---

## Actual state at freeze-phase start

| Item | Value |
|---|---|
| Local HEAD (before any freeze commit) | `af34d57d3a921c1be50a61f990c2d85ff8d97df3` |
| origin/main | `af34d57d3a921c1be50a61f990c2d85ff8d97df3` |
| Local = Remote | **YES — fully synchronized** |
| Diverged branches | None |
| Uncommitted tracked changes | None |
| Untracked files | `docs/coap_submission_dry_run_20260612/` (directory), `paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md` |

Commands run to verify:
```
git fetch origin --prune
git rev-parse HEAD        # af34d57d3a921c1be50a61f990c2d85ff8d97df3
git rev-parse origin/main # af34d57d3a921c1be50a61f990c2d85ff8d97df3
git status --short        # ?? docs/coap_submission_dry_run_20260612/
                          # ?? paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md
```

---

## Reconciliation: af34d57 vs 04ba2c3

The dry-run report from the prior session cited repository commit `04ba2c3` while the prior cleanup summary report identified final commit `af34d57`. This was not a discrepancy indicating lost work — the two commits are related as follows:

| Relationship | Result |
|---|---|
| Is 04ba2c3 an ancestor of af34d57? | **YES** (exit code 0) |
| Is af34d57 an ancestor of 04ba2c3? | **NO** (exit code 1) |
| Conclusion | `af34d57` is the later commit; `04ba2c3` is its ancestor |

The correct commit history (most recent last):

```
04ba2c3  experiments: reconcile documentation and EXP completion metadata
af34d57  docs: update maintenance summary for second cleanup pass  ← HEAD, origin/main
```

`04ba2c3` was the HEAD at the start of the dry run. `af34d57` was committed during the same cleanup session (updating the maintenance summary for the second cleanup pass). The dry-run session ran after `04ba2c3` was committed but before the summary referenced `af34d57` had been pushed; the dry-run report cited the then-current HEAD. This is consistent and correct.

**No commits are missing, lost, reset, amended, or superseded. Git history is intact.**

---

## Full recent history

```
* af34d57 (HEAD -> main, origin/main) docs: update maintenance summary for second cleanup pass
* 04ba2c3 experiments: reconcile documentation and EXP completion metadata
* 3b51476 docs: record post-cleanup repository size metrics
* 04ca3ad chore: sync manuscript PDF with submission upload bundle
* 938c32d docs: add navigation layer, full branch audit, and experiment reconciliation
* 4d1c657 chore: archive legacy manuscript and EJCO submission packages
* 6c04ff1 paper: address final COAP submission audit
* f306c15 Finalize COAP manuscript, Online Resource 1, and submission package.
```

No force-push indicators; no non-linear history; no reset markers.

---

## Conclusion

The repository history is intact. The local branch and origin/main are synchronized at `af34d57`. The `04ba2c3` reference in the dry-run report was accurate at the time the dry run was conducted and represents an ancestor commit in the normal linear history.
