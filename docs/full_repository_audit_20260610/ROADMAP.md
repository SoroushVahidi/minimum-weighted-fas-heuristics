# Project Roadmap (Post-Audit)

**Audit date:** 2026-06-10  
**Principle:** Do not disturb active holdout until `COMPLETED.ok`.

---

## Phase 0 — Predecessor disclosure (NEW — from 2026-06-11 novelty audit)

**This phase should be completed in parallel with Phase 1, not after it.**

| Field | Detail |
|---|---|
| **Objective** | Disclose the three known author predecessors and correct four algorithm-description errors in the manuscript |
| **Prerequisites** | None — independent of holdout |
| **Priority issues** | N-01 (arXiv:2412.16181), N-02 (JOCO-V), N-03 (Elsevier-V), N-04 (add-back ordering), N-05 (topo shortcut iff), N-06 (destroy causal language) |
| **Files** | `paper_coap/bibliography/references.bib`, `paper_coap/sections/02_related_work.tex`, `paper_coap/sections/04_algorithmic_framework.tex` |
| **Step 1** | Obtain full text of arXiv:2412.16181 and assess algorithmic overlap with COAP |
| **Step 2** | Add arXiv:2412.16181 to bibliography and cite in §2 related work |
| **Step 3** | Add JOCO-V and Elsevier-V as author-predecessor citations |
| **Step 4** | Draft cover letter disclosure paragraph (template in `MANUSCRIPT_POSITIONING_RECOMMENDATIONS.md`) |
| **Step 5** | Audit §4 for add-back ordering language, topo shortcut iff, and destroy causal language; apply fixes |
| **Effort** | 1–3 days depending on arXiv:2412.16181 content assessment |
| **Done when** | All N-01–N-06 issues resolved; cover letter drafted |

---

## Phase 1 — Freeze and finish holdout

| Field | Detail |
|---|---|
| **Objective** | Complete 1286 pending holdout runs |
| **Prerequisites** | None — experiment running |
| **Files** | `experiments/coap_ipsns_holdout/`, `logs/coap_ipsns_holdout/` |
| **Experiments** | Resume only if crash: `run_coap_ipsns_holdout.py --resume` |
| **tmux** | Session `coap_ipsns_holdout` — do not send keys |
| **Effort** | ~1–2 h wall time remaining (estimate) |
| **Done when** | `logs/coap_ipsns_holdout/COMPLETED.ok` exists; 1286+ successes |

---

## Phase 2 — Post-process parameter results

| Field | Detail |
|---|---|
| **Objective** | Apply pre-registered selection rules; decide default changes |
| **Prerequisites** | Phase 1 |
| **Files** | New `scripts/postprocess_coap_ipsns_holdout.py`; `paper_coap/notes/`; optional `configs/ipsns_default.yaml` |
| **Experiments** | Analysis only |
| **tmux** | No |
| **Effort** | 4–8 hours |
| **Done when** | Decision record updated; holdout summary committed |

---

## Phase 3 — Manuscript parameter + wording integration

| Field | Detail |
|---|---|
| **Objective** | Update §5 defaults if holdout confirms; fix destroy-fraction wording |
| **Prerequisites** | Phase 2 decision |
| **Files** | `paper_coap/sections/05_experimental_design.tex`, `04_algorithmic_framework.tex`, `tables/table_algorithm_invariants.tex` |
| **Effort** | 2–4 hours |
| **Done when** | Manuscript consistent with holdout evidence or explicit limitation |

---

## Phase 4 — Verify approximation / formal analysis gaps

| Field | Detail |
|---|---|
| **Objective** | Resolve Prop. 2 scope (Stabilize); decide on DF03 partial theorem |
| **Prerequisites** | None (parallel) |
| **Files** | `paper_coap/sections/04_formal_analysis.tex` |
| **Stop rule** | If DF03 transfer needs >1 week, keep disclaimer only |
| **Effort** | 2 hours – 5 days |
| **Done when** | No contradictory formal claims |

---

## Phase 5 — External baselines (sfas identity resolution; DRMacIver disclosures)

| Field | Detail |
|---|---|
| **Objective** | Resolve sfas identity; add DRMacIver non-determinism and igraph Eades weight disclosures; optionally run CC25 external code if available |
| **Prerequisites** | Phase 0 (novelty/disclosure) should be complete first — sfas resolution interacts with CC25 disclosure |
| **Files** | `paper_coap/sections/05_experimental_design.tex`; optionally `scripts/`, `experiments/exp4_*` extension |
| **Step 1** | Author confirms sfas identity (P-01 in POST_HOLDOUT_BASELINE_PLAN.md) |
| **Step 2** | Add DRMacIver non-determinism sentence to §5 (P-02, 30 min) |
| **Step 3** | If CC25 code publicly available and weighted: run on EXP4 instances (2–5 days); otherwise document exclusion (1 hour) |
| **Step 4** | Optional: DRMacIver 3–5-run reproducibility check on 20 instances (P-03, 2–4h) |
| **Stop rule** | If sfas = CC25 code: stop if weighted support absent or install fails. If sfas = something else: document exclusion immediately. |
| **igraph exact_ip** | Classified as exact validation (not heuristic comparison); run on EXP3 instances as optional sanity check only (P-04) |
| **Effort** | 30 min (text) to 5 days (if CC25 code run) |
| **Done when** | sfas identity resolved and documented; DRMacIver/Eades disclosures in §5 |

**2026-06-11 audit findings:**
- sfas has no established identity in the repository (B-06)
- igraph exact_ip should go to EXP3-scope exact validation, NOT EXP4 heuristic comparison (EXACT_BASELINE_FEASIBILITY.md)
- fas-smartAE doubly disqualified: unweighted + networkit unavailable
- See `BASELINE_EXECUTION_READINESS_AUDIT.md`, `MISSING_BASELINE_REGISTER.csv`, `POST_HOLDOUT_BASELINE_PLAN.md`

---

## Phase 6 — Related-manuscript disclosure

| Field | Detail |
|---|---|
| **Objective** | COAP-compliant overlap documentation |
| **Prerequisites** | Manual review of predecessor ZIPs and EJCO/CAIE PDFs |
| **Files** | Cover letter, portal uploads, `paper_coap/notes/` |
| **Effort** | 2–4 days |
| **Done when** | Cover letter + uploaded related manuscripts |

---

## Phase 7 — Build Springer ESM_1.zip

| Field | Detail |
|---|---|
| **Objective** | COAP Online Resource 1 |
| **Prerequisites** | Phases 2, 6 |
| **Files** | New `submission_coap/` or `paper_coap/supplementary/` |
| **Effort** | 1–2 days |
| **Done when** | ZIP matches manuscript citation; no path leaks |

---

## Phase 8 — Tests and CI

| Field | Detail |
|---|---|
| **Objective** | Theorem-critical pytest + GitHub Actions |
| **Prerequisites** | None |
| **Files** | `tests/`, `.github/workflows/` |
| **Effort** | 2–3 days |
| **Done when** | CI green on push |

---

## Phase 9 — Final PDF and compliance audit

| Field | Detail |
|---|---|
| **Objective** | Human visual PDF review; COAP checklist |
| **Prerequisites** | Phases 3, 7 |
| **Files** | `paper_coap/main.pdf` |
| **Effort** | 4 hours |
| **Done when** | Checklist in `COAP_TEMPLATE_AND_GUIDELINES_AUDIT.md` all verified |

---

## Phase 10 — COAP submission package

| Field | Detail |
|---|---|
| **Objective** | Editorial Manager upload bundle |
| **Prerequisites** | Phases 6–9 |
| **Contents** | PDF, LaTeX source, title page (if required), cover letter, ESM_1.zip, related PDFs, reviewer suggestions |
| **Effort** | 1 day |
| **Done when** | Successful portal submission |

---

## Phase 11 — Optional historical ideas

| Field | Detail |
|---|---|
| **Objective** | Test expanded seeds / parallel SCC only if scientifically motivated |
| **Stop rule** | Abandon if holdout already supports 50-iter default with zero violations |
| **Priority** | **Low** pre-submission |

---

## Recommended stopping rules

- **Holdout:** If zero violations and clear 50-iter winner on holdout, do not run expanded seed portfolio
- **sfas/exact_ip:** If install blocked, document exclusion rather than delay submission >2 weeks
- **DF03 theorem:** Defer if not essential to acceptance — disclaimer is already honest
- **Refactoring duplicated code:** Post-acceptance only
