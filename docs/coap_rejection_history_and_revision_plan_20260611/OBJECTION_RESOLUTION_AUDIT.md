# Objection Resolution Audit

**Audit date:** 2026-06-11  
**Comparison baseline:** `paper_coap/`, `docs/final_branch_audit_20260611/`, `docs/full_repository_audit_20260610/`, experiment directories.

Resolution statuses: **Fully resolved | Substantially resolved | Partially resolved | Unresolved | Worsened | N/A | Impossible until EXP10**

---

## Explicit assessment of 15 required questions

### 1. Is novelty now centered correctly on IPSNS?

**Substantially resolved.**  
- Evidence: `paper_coap/sections/02_related_work.tex` L50: “IPSNS is the main algorithmic contribution beyond the engineered LR-TA seed.”  
- Gap: `paper_coap/sections/01_introduction.tex` contribution bullets still list LR-TA first (L20).  
- Action: Reorder bullets; add predecessor citation for LR-TA/WMSF lines.

### 2. Is LR-TA properly described as inherited/refined?

**Fully resolved in prose.**  
- Evidence: Intro L8: “We do not claim local-ratio as new”; §2 cites DF03 as antecedent.  
- Gap: No explicit citation to JOCO predecessor manuscript (only DF03/CC25).

### 3. Is WMSF properly attributed to Cavallaro–Cutello?

**Fully resolved.**  
- Evidence: `paper_coap/sections/02_related_work.tex` L24; EXP design notes CC25 not rerun.

### 4. Are predecessor manuscripts disclosed?

**Unresolved.**  
- No mention of JOCO, DAM, CAIE, EJCO, or arXiv in manuscript or declarations.  
- Evidence gap: `docs/final_branch_audit_20260611/RELATED_WORK_AND_DISCLOSURE_AUDIT.md` N-03.

### 5. Is the benchmark suite now broad enough?

**Substantially resolved.**  
- 105 sparse + 97 standard + 50 LOLIB + EXP9 application + holdout tuning instances.  
- Evidence: `experiments/exp1b_*`, `exp4_*`, `exp5_*`, `exp9_*`, `coap_ipsns_holdout/results/runs.jsonl` (1290 lines).

### 6. Are external baselines adequate?

**Substantially resolved.**  
- DRMacIver, igraph Eades, weighted Eades, Borda, random multistart.  
- Gap: sfas identity unresolved (`POST_HOLDOUT_BASELINE_PLAN.md` P-01).

### 7. Is exact validation adequate?

**Fully resolved for submission scope.**  
- EXP3: 56/57 DP optimal; EXP8: 7/15 MIP optimal, IPSNS matches 6/7.  
- Evidence: `docs/final_branch_audit_20260611/EXACT_SOLVER_AUDIT.md`.

### 8. Are stochastic limitations addressed by EXP10?

**Impossible until EXP10 completes.**  
- IPSNS phase: zero variance across 20 seeds on all 93 instances (validated).  
- DRMacIver phase: ~21% complete at audit; manuscript lacks EXP10 integration.

### 9. Are ablation, sensitivity, and holdout studies complete?

**Substantially resolved.**  
- EXP2 ablation: complete.  
- EXP6 budget: complete.  
- Holdout: 1290/1290 runs in `runs.jsonl`; postprocess/summary for manuscript **partially pending**.

### 10. Are theoretical claims properly limited?

**Fully resolved.**  
- Abstract: “computational and algorithmic rather than a new approximation-ratio theorem.”  
- Prop 3 framed as monotonicity not optimality gap.

### 11. Is sparse-versus-dense scope clearly stated?

**Fully resolved.**  
- Abstract, intro L16–17, results, discussion all state LOLIB boundary.

### 12. Is the paper still too long or unfocused?

**Partially resolved.**  
- ~13k words TeX; many tables. Consolidation recommended before submission.

### 13. Is the supplementary artifact adequate?

**Unresolved.**  
- EJCO artifact stale; COAP OR1 not created (`COAP_COMPLIANCE_AUDIT.md`).

### 14. Are tests still missing?

**Unresolved.**  
- Zero test files (`TEST_AND_CI_AUDIT.md` BLOCKER).

---

## Master resolution table (by reason ID)

| ID | Status | Supporting evidence path |
|----|--------|------------------------|
| RR-001 | Substantially | paper_coap/sections/01_introduction.tex, 02_related_work.tex |
| RR-002 | Substantially | paper_coap/sections/04_formal_analysis.tex; abstract |
| RR-003 | Fully | paper_coap/sections/02_related_work.tex L24 |
| RR-004 | Fully | paper_coap/sections/06_results.tex; table_lolib_scope.tex |
| RR-005 | Substantially | paper_coap/sections/05_experimental_design.tex |
| RR-006 | Partially | declarations promise OR1; repo private |
| RR-007 | Fully | CC25 citations; WMSF_AUDIT.md |
| RR-008 | Substantially | EXP6–EXP9 + EXP10 pending |
| RR-009 | Substantially | COAP framing vs venue_decision_notes |
| RR-010 | Substantially | EXP5 + expanded sparse suite |
| RR-011 | Fully | experiments/exp8_*; paper_coap results |
| RR-012 | Fully | experiments/exp7_*; paper_coap §5–§6 |
| RR-013 | Partially | Code deterministic; prose gap |
| RR-014 | Substantially | Formal analysis section added |
| RR-015 | Fully | All numbers from EXP recomputation |
| RR-016 | Partially | Unified narrative; disclosure missing |
| RR-017 | **Unresolved** | No arXiv cite in paper_coap/bibliography |
| RR-018 | Partially | EXP10 running; §5 disclosure missing |
| RR-019 | **Unresolved** | TEST_AND_CI_AUDIT.md |
| RR-020 | **Unresolved** | COAP_COMPLIANCE_AUDIT.md |
| RR-021 | **Unresolved** | cover_letter_draft.tex |
| RR-022 | Partially | COAP shorter than CAIE 44pp draft |
| RR-023 | Substantially | holdout runs.jsonl 1290; manuscript pending |
| RR-025 | Partially | MISSING_BASELINE_REGISTER.csv |
| RR-026 | Fully | COAP bounded language vs DAM abstract |
| RR-027 | N/A | COAP target replaces CAIE/COR debate |
| RR-028 | Impossible until EXP10 | exp10_stochastic_robustness/ |
| RR-029 | Partially | requirements.txt unpinned |
| RR-030 | Partially | Needs author-confirmed withdrawal status |
| RR-031 | Partially | Intro bullet order |
| RR-032 | **Unresolved** | No upload bundle prepared |

---

## Items that worsened relative to predecessors

| Issue | Note |
|-------|------|
| Disclosure debt | More predecessors + venues than early CAIE draft acknowledged |
| Artifact complexity | Nine experiment types increase OR1 burden |
| Cover letter liability | EJCO draft “not under consideration elsewhere” is inaccurate if predecessors public |

No scientific claim was found to be **worsened** vs CAIE/EJCO — COAP adds formal analysis and holdout/EXP10.
