# Executive Summary — Rejection History and COAP Revision Plan

**Audit date:** 2026-06-11  
**Branch:** `main`  
**HEAD:** `80b3144d5fdbbe250faed8a4fe671dde2da76c89`  
**Target journal:** Computational Optimization and Applications (COAP), Springer Nature  
**Audit mode:** Read-only (no experiment, code, or manuscript modifications)

---

## Critical evidence limitation

**No referee reports, decision letters, desk-rejection notices, or editorial emails are stored in this repository.** The prior audit at `paper/notes/rejection_audit/extracted_review_text/README.txt` confirms this explicitly. Rejection history is therefore reconstructed from:

- Predecessor manuscripts (JOCO, DAM) and arXiv preprint metadata
- Internal planning documents (`docs/manuscript_results_and_claims_20260606.md`, `docs/venue_decision_notes_20260606.md`)
- Experiment READMEs attributing EXP7/EXP8 to “reviewer” or “external reviewer” requests (CAIE revision track)
- Git history (CAIE package → CAIE revision commits → EJCO package → COAP retargeting)
- Internal notes (`paper/notes/reuse_risk_report.md`: “rejected JOCO or DAM manuscripts”)

**Do not treat planning-register “Reviewer notes …” lines as verbatim referee quotes unless corroborated by a stored report.**

---

## Submission lineage (documented)

| # | Work | Venue | Status in repo evidence |
|---|------|-------|-------------------------|
| 1 | arXiv:2412.16181 (Vahidi & Koutis) | arXiv | Public author predecessor; not cited in COAP |
| 2 | Fast Local-Ratio… (LR-TA) | Journal of Combinatorial Optimization | Archived predecessor; internal note: rejected |
| 3 | Incumbent-Protected SCC… (IPSNS) | **Discrete Applied Mathematics** | Full predecessor TeX in archive; internal note: rejected |
| 4 | Reproducible Local-Ratio and SCC-Refinement… | **Computers & Industrial Engineering** | Submission package prepared 2026-06-06; outcome unknown |
| 5 | Local-Ratio Seeding and SCC-Based Refinement… | **EURO Journal on Computational Optimization** | Submission package in repo; outcome unknown |
| 6 | Same title as (5) | **COAP** (current target) | In preparation |

**Not documented as submitted in this repository:** EAAI, Applied Intelligence, Digital Engineering, MLJ, KBS, COR, OPSEARCH (listed as audit-needed only).

---

## Documented criticism themes (32 items in master register)

| Taxonomy | Count | Most serious for COAP |
|----------|-------|------------------------|
| A Novelty | 7 | Local-ratio prior art; undisclosed author predecessors |
| B Experimental | 11 | DRMacIver single-run; benchmark breadth |
| C Technical | 5 | Approximation bounds; topological extraction semantics |
| D Positioning | 4 | Venue fit; sparse-vs-dense scope |
| E Writing | 5 | Length; contribution ordering |
| F Reproducibility | 6 | No tests; no COAP artifact; private repo |
| G Ethics/disclosure | 5 | arXiv undisclosed; salami-slicing risk |
| H Editorial | 4 | Cover letter accuracy; portal uploads |

---

## Answers to required final conclusions

1. **Documented rejection reasons?** No verbatim decision letters. Reconstructible concerns: insufficient novelty (local-ratio prior art), weak theory, baseline/exact-validation gaps, dense-scope overclaiming, reproducibility, undisclosed predecessor overlap, parameter justification, manuscript length. JOCO/DAM labeled “rejected” only in `paper/notes/reuse_risk_report.md`.

2. **Most serious rejection reason?** **Undisclosed overlap with author predecessors (arXiv:2412.16181, JOCO LR-TA paper, DAM IPSNS paper) combined with salami-slicing perception** — a desk-rejection / ethics issue at COAP if not addressed in cover letter and portal uploads.

3. **Unresolved criticisms?** arXiv disclosure; predecessor portal uploads; EXP10 integration; COAP Online Resource 1; automated tests; cover letter rewrite; holdout final summary in manuscript; sfas baseline resolution.

4. **Fully resolved?** WMSF/CC25 attribution; LOLIB scope boundary; GNNRank scoping; EXP7/EXP8/EXP3 exact validation; negative-weight exclusions; local-ratio prior-art language in related work; paired statistical tests; formal Props 1–4.

5. **Novelty positioned correctly?** **Substantially yes in prose** (IPSNS as main new element; LR-TA inherited). **Not yet in disclosure or contribution bullet order.**

6. **Distinct from arXiv:2412.16181?** **Cannot fully verify without full preprint text.** COAP adds unified framework, formal analysis, expanded experiments, LOLIB boundary — but **must cite and disclose**.

7. **WMSF provenance?** **Yes** — CC25 cited; labeled seed/baseline.

8. **IPSNS sufficient as main new algorithm?** **Yes for COAP computational paper**, provided predecessors disclosed and EXP10 confirms external-comparison robustness.

9. **Experiments sufficient after EXP10?** **Yes for initial submission**, with holdout postprocess integrated; no mandatory new baseline campaigns.

10. **Another exact solver required?** **No** — EXP3 DP + EXP8 HiGHS MIP sufficient; Baharev/igraph exact-IP optional P3.

11. **Another external heuristic required?** **No** — DRMacIver + Eades + EXP10 repetitions adequate; sfas/CC25 external code optional.

12. **Too long/unfocused?** **Moderate risk** — consolidate tables; move proof details to Online Resource 1.

13. **Theory reduced/moved?** **Recommended:** keep Prop statements in main text; move full proofs to appendix/OR1.

14. **Dense LOLIB limitation help or hurt?** **Helps** — proactively bounds claims; essential given EXP5.

15. **Title appropriate?** **Yes** — technical, no hype; MWFAS-focused.

16. **Abstract appropriate?** **Yes** — bounded claims; states computational contribution; mentions LOLIB boundary.

17. **Contribution list appropriate?** **Needs reorder** — IPSNS should be first bullet; LR-TA/WMSF labeled inherited.

18. **Greatest desk-rejection risk?** **Incomplete related-manuscript disclosure + inaccurate cover letter originality statement.**

19. **Greatest reviewer-rejection risk?** **Perceived incremental novelty (LR-TA/WMSF from prior author work) if IPSNS/EXP10 story not foregrounded.**

20. **Mandatory before submission?** EXP10 complete + integrated; COAP cover letter with full disclosure; Online Resource 1; arXiv citation; DRMacIver single-run + EXP10 text in §5–§6; predecessor PDF uploads; smoke tests; rewrite cover letter.

21. **Strongly recommended?** Holdout summary in §5; contribution reorder; topological non-uniqueness paragraph; table consolidation; pin dependencies; HiGHS citation check.

22. **Can safely omit?** GNNRank experiments; Baharev comparison; sfas if documented; additional dense benchmarks; memory scaling study.

23. **Must wait for EXP10?** DRMacIver stochastic robustness paragraph; finalize §6–§7 comparison language; Online Resource 1 packaging; final pre-submission verdict.

24. **Must wait for holdout?** Final default-parameter justification paragraph (1290 runs exist; postprocess pending).

25. **Final narrative?** Computational optimization/engineering paper: **IPSNS** is primary new contribution; LR-TA and WMSF are inherited seeds; best observed performance among tested methods on sparse nonnegative digraphs; exact/MIP certification; EXP10 stochastic robustness; LOLIB defines limitation.

26. **Main paper?** Intro, related work (with predecessor disclosure), problem, algorithms + Prop statements, experimental design, core results (EXP1b/4/3/2/5/6–9 summary), discussion, conclusion.

27. **Online Resource 1?** Full reproduction scripts, pinned env, DRMacIver binary+SHA256, EXP10 raw summaries, holdout logs, proof details, extended tables, predecessor overlap matrix.

28. **Cover letter must disclose?** All prior venues; arXiv; JOCO/DAM predecessors; CAIE/EJCO attempts and outcomes (author must supply exact outcomes); what is new in COAP; no parallel submission.

29. **Editor files?** Predecessor PDFs, overlap statement, suggested reviewers, declarations, title page, anonymized PDF, OR1 ZIP.

30. **Credible COAP path?** **Yes, conditional** — science and experiments are strong; **editorial/disclosure/artifact gaps are the remaining blockers.**

---

## EXP10 safety confirmation

Passive inspection only at audit time: DRMacIver production runner active; ~394/1860 checkpoints; **no EXP10 files, processes, or production code were modified during this audit.**

---

## Single next task after EXP10 completes

Run `experiments/exp10_stochastic_robustness/scripts/wait_and_finalize_exp10.py` pipeline to completion (validate → summarize → finalize), then integrate EXP10 results into `paper_coap/sections/05_experimental_design.tex` and `06_results.tex` before building COAP Online Resource 1.
