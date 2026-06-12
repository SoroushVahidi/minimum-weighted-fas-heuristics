# Final Pre-Submission Sequence

**Audit date:** 2026-06-11  
**Prerequisite:** Do not submit until all P1 items complete.

---

## Sequence (ordered)

### Stage 0 — Author documentary completion (parallel to EXP10)

| Step | Action | Owner | Output |
|------|--------|-------|--------|
| 0.1 | Locate CAIE/EJCO/JOCO/DAM decision letters and manuscript IDs | Author | Update `PRIOR_DECISION_AND_REVIEW_REGISTER.csv` |
| 0.2 | Download full arXiv:2412.16181 PDF; side-by-side overlap note | Author | Overlap paragraph for §2 |
| 0.3 | Confirm no parallel submission of predecessor manuscripts | Author | Cover letter statement |

### Stage 1 — Wait for EXP10 (no manual intervention on runner)

| Step | Action | Verification |
|------|--------|--------------|
| 1.1 | Allow `run_drmaciver_repetitions.py` → 1860/1860 | Checkpoint count |
| 1.2 | `wait_and_finalize_exp10.py` completes pipeline | `finalize_exp10.py` exit 0 |
| 1.3 | Review EXP10 summary: IPSNS deterministic; DRMacIver distribution | `experiments/exp10_stochastic_robustness/summary/` |

### Stage 2 — Holdout finalization (parallel)

| Step | Action | Verification |
|------|--------|--------------|
| 2.1 | Run holdout postprocess if not done | Summary JSON/MD in holdout dir |
| 2.2 | Document chosen defaults vs tuning grid | Match `ipsns.py` constants |
| 2.3 | Add conservative §5 paragraph | Parameter claims subset-scoped |

### Stage 3 — Code and tests

| Step | Action | Verification |
|------|--------|--------------|
| 3.1 | Commit `ipsns.py` diagnostics + EXP10 infrastructure | git clean for experiment dirs |
| 3.2 | Create `tests/` smoke: io, exact small, lrta/wmsf/ipsns feasibility | pytest pass |
| 3.3 | Pin `requirements.txt` | Document Python 3.10.x tested |
| 3.4 | Add DRMacIver SHA256 file | Hash matches binary |

### Stage 4 — Manuscript revision

| Step | Action | File |
|------|--------|------|
| 4.1 | Add §2 predecessor subsection + arXiv bib entry | `02_related_work.tex`, `references.bib` |
| 4.2 | Reorder contribution bullets (IPSNS first) | `01_introduction.tex` |
| 4.3 | Add topological non-uniqueness paragraph | `04_algorithmic_framework.tex` |
| 4.4 | Add DRMacIver seeding + EXP10 subsection | `05_experimental_design.tex`, `06_results.tex` |
| 4.5 | Integrate holdout parameter paragraph | `05_experimental_design.tex` |
| 4.6 | Recompute EXP2 ablation numbers from raw | `MANUSCRIPT_NUMERICAL_TRACEABILITY.csv` |
| 4.7 | Verify HiGHS citation | `references.bib` |
| 4.8 | Consolidate tables / move proofs to OR1 | `MANUSCRIPT_RESTRUCTURING_PLAN.md` |
| 4.9 | Rebuild PDF; check page count 25–35 | `main.pdf` |

### Stage 5 — Online Resource 1

| Step | Action | Verification |
|------|--------|--------------|
| 5.1 | Build COAP OR1 ZIP from template in gap analysis | MANIFEST complete |
| 5.2 | Clean-machine reproduction test | Independent pass |
| 5.3 | Sanitize absolute paths in EXP10 JSON for artifact | No `/home/soroush/` in OR1 |

### Stage 6 — Cover letter and portal uploads

| Step | Action | Verification |
|------|--------|--------------|
| 6.1 | Write COAP cover letter from content plan | No prohibited statements |
| 6.2 | Prepare related PDFs: arXiv, JOCO, DAM, EJCO | Portal checklist |
| 6.3 | Prepare overlap matrix PDF | Attached |
| 6.4 | Suggested reviewers list | 3–5 names with emails/institutions |
| 6.5 | Regenerate title page + highlights for COAP | Match abstract |

### Stage 7 — Final gates

| Gate | Criterion |
|------|-----------|
| G1 | EXP10 integrated; claims match summary |
| G2 | All predecessor disclosures in letter + §2 + uploads |
| G3 | OR1 + tests exist; reproducibility claim defensible |
| G4 | `REJECTION_PROOFING_REVISION_MATRIX.csv` all P1 rows = resolved |
| G5 | Author visual PDF review |
| G6 | Public GitHub + Zenodo DOI (if policy requires at submission) |

### Stage 8 — Submit to COAP

- Upload via Springer submission system
- Retain local copy of exact upload manifest
- Do **not** submit EJCO/CAIE packages

---

## Parallel work allowed during EXP10

- Stage 0 documentary search
- Stage 2 holdout postprocess
- Stage 3 tests and dependency pinning (avoid modifying `ipsns.py` logic beyond committed diagnostics)
- Stage 5 OR1 scaffolding (exclude EXP10 until finalized)
- Draft cover letter text (without final EXP10 numbers)

## Work forbidden until EXP10 completes

- Final §6 stochastic claims
- Final abstract sentence on DRMacIver robustness
- OR1 EXP10 data inclusion
- Submission G1 sign-off

---

## Estimated timeline (after EXP10)

| Stage | Duration estimate |
|-------|-------------------|
| EXP10 completion | Hours (in progress at audit) |
| Manuscript edits | 2–4 days |
| OR1 + clean-machine test | 2–3 days |
| Tests + commits | 1 day |
| Cover letter + uploads | 1 day |
| **Total post-EXP10** | **~1 week focused work** |

---

## Single next task (immediate)

**Allow EXP10 to finish** via existing `wait_and_finalize_exp10.py` monitor — then execute Stage 4.4 (manuscript EXP10 integration) as the first authoring action.
