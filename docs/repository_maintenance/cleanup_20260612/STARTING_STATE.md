# Starting State Snapshot

**Starting commit (first pass):** `6c04ff1cc19d1887bd5b1b2bd1d1f31dc2b6924a`

**Starting commit (second pass, this session):** `3b51476fb2a6815fd566f09c7a79d931f1d99dda`

**Date:** 2026-06-12

## Repository structure at 6c04ff1 (pre-first-pass)

```
minimum-weighted-fas-heuristics/
├── src/mwfas/               ← canonical algorithms
├── scripts/                 ← CLI runners
├── tests/                   ← pytest suite (91 collected)
├── configs/                 ← benchmark instance lists
├── experiments/             ← EXP1b–EXP11 + COAP sensitivity/holdout
├── paper_coap/              ← COAP manuscript (45 pages)
├── online_resource_1/       ← OR1 source + packaged mirror
├── paper/                   ← LEGACY manuscript tree (pre-COAP) — ARCHIVED in first pass
├── submission_package/      ← EJCO historical package — ARCHIVED in first pass
├── submission_files_for_download/  ← anonymized files for download
├── archive/predecessor_projects/  ← predecessor ZIPs
├── docs/                    ← 12+ dated audit directories
├── logs/                    ← local experiment logs
├── results/                 ← processed/raw/tables outputs
├── notebooks/               ← exploratory notebooks
├── CITATION.cff
├── README.md
├── requirements.txt / requirements-dev.txt
├── pytest.ini
├── setup.py
├── Vahidi_Online_Resource_1_MWFAS.{pdf,zip}  ← root mirrors
└── .github/workflows/       ← CI
```

**Issues present at 6c04ff1:**
- `paper/` and `submission_package/` at root level (confusable with COAP canonical)
- EXP10 `experiment_progress.json` status field said NONFINAL despite completion
- No `coap_ipsns_holdout/summary/` (only checkpoints)
- No `docs/INDEX.md` or living registries
- EDITORIAL_MANAGER abstract was 271 words (stale)
- `experiments/combined/` had no deprecation notice
- EXP1 had no ARCHIVED label

## Repository structure at 3b51476 (start of second pass)

All first-pass actions completed:
- `paper/` archived to `docs/archive/predecessor_manuscripts/paper_legacy_pre_coap/`
- `submission_package/` archived to `docs/archive/legacy_submission_packages/ejco_submission_package/`
- `docs/INDEX.md`, `docs/CANONICAL_SOURCE_MAP.md`, `docs/EXPERIMENT_REGISTRY.csv` created
- `docs/REPOSITORY_DOCUMENTATION_POLICY.md`, `docs/KNOWN_LIMITATIONS.md` created
- EXP10 progress.json updated to `status: COMPLETE`
- Holdout summary created (`coap_ipsns_holdout/summary/holdout_aggregate.json`)
- Portal abstract updated to 238 words
- Root README rewritten

**Issues present at 3b51476 (addressed in second pass):**
- EXP11 README says "12-instance calibration subset" (should be 6)
- EXP11_RESULTS.md says "8 instances, 2 improved" (inconsistent with aggregate.json: 6, 0 improved)
- Missing READMEs for EXP1b, EXP3, EXP4, EXP10, seedfix_full_wmsf
- Missing Phase 31 docs: STARTING_STATE.md, SECURITY_AND_PRIVACY_RESULT.md, NUMERICAL_CONSISTENCY_CHECK.md
- experiments/README.md missing checkpoint/raw-output policy
- EXPERIMENT_REGISTRY.csv EXP11 row noted inconsistencies (cleaned up in this pass)

## Tracked file counts

- At 6c04ff1: ~6350 tracked files
- At 3b51476: ~6410 tracked files (navigation docs added)
- After second pass: see SIZE_BEFORE_AND_AFTER.md update
