# Remaining Manuscript Gaps

**Audit date:** 2026-06-11  
**After non-result-dependent reframing pass**

---

## Blockers before COAP submission

| ID | Gap | Owner | Depends on |
|----|-----|-------|------------|
| G-01 | ~~EXP10 stochastic robustness integration~~ | **Done 2026-06-12** | `docs/coap_exp10_manuscript_integration_20260611/` |
| G-02 | Online Resource 1 supplementary archive (proofs, full artifact bundle) | Author build | **OR1 package** |
| G-03 | Cover letter predecessor IDs/outcomes (JOCO, DAM, CAIE, EJCO) | Author records | **Author information** |
| G-04 | Full cover letter (draft disclosure paragraph only exists) | Author | G-03 |
| G-05 | Smoke/regression tests for submission readiness (per rejection audit) | Code QA | Separate task |

---

## Non-blocking but recommended

| ID | Gap | Notes |
|----|-----|-------|
| G-06 | Holdout results narrative in §6 | Holdout mentioned in §5; dedicated results subsection/table may strengthen parameter claims if not already summarized elsewhere |
| G-07 | Side-by-side overlap note vs arXiv:2412.16181 full PDF | Recommended in rejection audit; not required for this reframing pass |
| G-08 | Proof appendix in OR1 | Main text correctly defers detailed proofs |
| G-09 | sfas baseline / EXP2 traceability (from rejection audit) | Outside this manuscript-only task |

---

## Completed in this pass

- IPSNS-first framing (title, abstract, contributions, algorithm section, conclusion).
- Prior-work disclosure subsection and declarations text.
- LR-TA / WMSF / IPSNS positioning corrections.
- Supporting (non-headline) formal analysis.
- Scoped empirical language outside EXP10 areas.
- Expanded limitations (10 items).
- Qualified reproducibility wording.
- Key bibliography additions (`VahidiKoutis2024arxiv`, `HuangfuHall2018`, `CCP24`).
- Pre-edit backup and audit deliverables.

---

## Immediate next task after EXP10 finalizes

1. Run `experiments/exp10_stochastic_robustness/wait_and_finalize_exp10.py` (or equivalent finalize pipeline) without altering in-flight checkpoints.
2. Integrate finalized repeated-run median/summary at all `% EXP10-INTEGRATION` locations (abstract, §1, §5, §7 limitation item 8, §8).
3. Add §5 subsection and/or table for EXP10 if warranted by finalized summaries.
4. Rebuild PDF; verify no placeholder comments; update post-edit claim register.
5. Proceed to Online Resource 1 build and cover letter completion.
