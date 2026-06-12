# Repository Cleanup Executive Summary

**Starting SHA (first pass):** `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a`  
**Starting SHA (second pass):** `3b51476fb2a6815fd566f09c7a79d931f1d99dda`  
**Final SHA:** `04ba2c3` (see `git log --oneline -1`)  
**Purpose:** Final organization pass before COAP Editorial Manager submission.

## First-pass outcomes (6c04ff1 → 3b51476)

1. **Canonical paths clarified** — `paper_coap/`, `final_upload/`, `src/mwfas/`, `online_resource_1/`.
2. **Stale EJCO and legacy `paper/` archived** under `docs/archive/`.
3. **Internal editorial material** moved to `docs/archive/internal/`.
4. **EXP10 metadata** finalized; **holdout** summarized from existing runs.
5. **Navigation layer** — root README, `docs/INDEX.md`, experiment registry.
6. **Portal abstract** corrected to 238 words in copy-ready text.
7. **Full branch audit** committed with cleanup preface.

## Second-pass outcomes (3b51476 → 04ba2c3)

8. **EXP11 summary reconciled** — README, RESULTS.md, and registry row corrected to 6 nonneg instances / 0 improved (was inconsistently showing 12 or 8 from a partial re-run).
9. **EXP10 registry** updated from COMPLETE_NONFINAL_MARKER → COMPLETE; holdout row updated.
10. **Experiment READMEs added** for EXP1b, EXP3, EXP4, EXP10, seedfix_full_wmsf.
11. **Checkpoint/raw-output policy** documented in experiments/README.md.
12. **Phase 31 maintenance docs added** — STARTING_STATE.md, SECURITY_AND_PRIVACY_RESULT.md, NUMERICAL_CONSISTENCY_CHECK.md.

## Not changed

- Algorithm behavior, experiment numbers, manuscript scientific content, upload PDF checksums.

## Tests

90 passed, 1 skipped (DRMacIver namespace).

## Author action remaining

Submit six files from `paper_coap/submission/final_upload/` via Editorial Manager; confirm CAIE/EJCO related-manuscript disclosures.
