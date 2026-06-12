# Cleanup and Reorganization Recommendations

**Audit-only — no actions taken in this task.**

Prioritized for **post-submission** or **post-acceptance** maintenance.

## Priority 1 — Low risk, high clarity

| # | Action | Rationale |
|---|---|---|
| 1 | Add `docs/INDEX.md` with canonical audit pointers | Reduces confusion across 12+ audit dirs |
| 2 | Update `EDITORIAL_MANAGER_COPY_READY_TEXT.md` abstract to 238 words | Prevents portal paste error |
| 3 | Add `submission_package/README_STALE_EJCO.md` | Warns against COAP misuse |
| 4 | Set EXP10 `update_progress.py` to emit `COMPLETE` when `completed_ok` | Fixes misleading NONFINAL |
| 5 | Replace `datetime.utcnow()` in `update_progress.py` | Removes deprecation warnings |

## Priority 2 — Repository hygiene

| # | Action | Rationale |
|---|---|---|
| 6 | Commit `coap_ipsns_holdout/summary/` or document checkpoint-only state | Closes holdout traceability gap |
| 7 | Regenerate `experiments/combined/manuscript_results_digest.json` incl. EXP6–11 | Internal claim guardrail |
| 8 | Remove or relocate `table_runtime_quality_tradeoff.tex` | Orphan table file |
| 9 | Align EXP11 README instance count with `exp11_aggregate.json` (6) | Doc consistency |
| 10 | Add `.gitignore` exception pattern for `docs/full_branch_repository_audit_20260612/*.csv` | If committing this audit |

## Priority 3 — Structural (post-acceptance)

| # | Action | Rationale |
|---|---|---|
| 11 | Archive `submission_package/` to `archive/ejco_submission_2026/` | Reduces duplication risk |
| 12 | Archive `paper/` legacy tree similarly | Clear COAP-only canonical path |
| 13 | External archive of EXP10 raw JSON (optional) | Disk space; not needed in git |
| 14 | Public GitHub release with OR1 ZIP + citation DOI | After acceptance / author decision |
| 15 | Sync OR1 `src/mwfas/` from `src/mwfas/` via scripted freeze | On next code change |

## Do NOT do (without strong reason)

- Delete EXP1 directory (documents supersession history)
- Delete audit directories (decision trail)
- Remove EXP10 local checkpoints before external backup
- Weaken pytest skips for CI cosmetics
- Force-push or rewrite Git history

## Reorganization sketch (optional future)

```
archive/
  ejco_submission_package/
  legacy_paper_tree/
docs/
  INDEX.md
  audits/   ← symlinks or moves of dated dirs (cosmetic only)
```

No reorganization is **required** for submission.
