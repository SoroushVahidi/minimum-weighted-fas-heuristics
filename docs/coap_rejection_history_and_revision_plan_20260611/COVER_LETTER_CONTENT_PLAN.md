# Cover Letter Content Plan (COAP)

**Audit date:** 2026-06-11  
**Deliverable:** Content plan only — not the final letter.

---

## Opening

- Address: Editor-in-Chief, *Computational Optimization and Applications*
- Manuscript title: “Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem”
- Article type: Original research / algorithm engineering with computational validation

---

## Paragraph 1 — Why COAP (not prior venues)

State explicitly:

- Problem is **NP-hard combinatorial optimization** with **algorithm engineering** and **extensive computational validation** — core COAP scope.
- Unlike **CAIE** (industrial engineering emphasis) or **EJCO** (OR practice), COAP fits the **formal analysis + optimization** combination added in this version (Propositions 1–4, complexity, MIP validation).
- Prior venue attempts focused on engineering heuristics; **this version adds unified formal treatment and stochastic robustness (EXP10)** not present in earlier packages.

**Do not say:** “CAIE/EJCO rejected because…” unless author inserts **exact documented outcomes**.

---

## Paragraph 2 — Optimization contribution

- Primary new algorithm: **IPSNS** — incumbent-protected SCC-local LNS with proved non-worsening relative to best seed (Prop 3).
- **Not** a new approximation-ratio result.
- Principal empirical finding: best **observed** performance among **tested** methods on standard sparse nonnegative benchmarks (96/97), with **EXP10** confirming paired comparison robustness vs DRMacIver.

---

## Paragraph 3 — Empirical evidence summary

Bullet mentally:
- EXP3 exact DP: 56/57 optimal
- EXP8 MIP: 7/15 optimal; IPSNS matches 6/7
- EXP4 external baselines including DRMacIver
- EXP2 ablation, EXP6 budget, EXP7 plain LS negative control
- EXP5 LOLIB scope boundary (DRMacIver stronger on dense)
- Holdout parameter validation (1290 runs)
- EXP10 stochastic repetitions (20 seeds × 93 instances)

---

## Paragraph 4 — Relation to arXiv:2412.16181

Mandatory content:

- Authors: Vahidi & Koutis (Dec 2024).
- Relationship: ranking-from-pairwise-comparisons as MWFAS; overlapping motivation and partial benchmark overlap **[author must confirm extent]**.
- COAP adds: unified LR-TA+WMSF+IPSNS framework, formal Props, expanded experiments, LOLIB boundary, holdout, EXP10.
- **Attached/uploaded** to COAP portal per policy.

---

## Paragraph 5 — Relation to prior CAIE / EJCO / JOCO / DAM manuscripts

Mandatory content:

| Predecessor | Venue | What it contained | COAP extension |
|-------------|-------|-------------------|----------------|
| JOCO LR-TA ms | JOCO | LR-TA only, 33 instances | Unified + IPSNS + formal analysis |
| DAM IPSNS ms | Discrete Applied Mathematics | IPSNS+WMSF | Unified + LR-TA + formal analysis |
| CAIE package | CAIE | Merged framework EXP1–5+ | EXP6–10, formal analysis, COAP template |
| EJCO package | EJCO | Near-identical to pre-COAP | Holdout, EXP10, Springer COAP format |

State:
- **Exact submission outcomes** (rejected / withdrawn / never submitted) — **author must supply**
- **No simultaneous submission** of predecessors with COAP version
- Predecessor PDFs uploaded for editorial review

---

## Paragraph 6 — Inherited vs new components

| Component | Status |
|-----------|--------|
| LR-TA Phase I/II | Inherited from JOCO predecessor; formalized in Props 1–2 |
| WMSF | CC25 reimplementation; seed only |
| IPSNS | From DAM predecessor; **Prop 3–4 new**; unified dual-seed new |
| Experiments EXP1–5 | Evolved from CAIE/EJCO track |
| EXP6–10, holdout | **New in COAP track** |
| Formal analysis | **New in COAP** |

---

## Paragraph 7 — Why substantial extension (not redundant publication)

- Split predecessors covered **disjoint algorithm subsets** with smaller experiments.
- COAP unifies with **first joint formal analysis** and **nine experiment types**.
- **Salami-slicing concern addressed** by transparent uploads and unified narrative.

---

## Paragraph 8 — Prior concerns resolved

Reference themes (not fake quotes):

- Local-ratio prior art acknowledged
- Exact/MIP validation added (EXP3, EXP8)
- External baselines strengthened (EXP4, EXP7)
- Dense scope bounded (EXP5)
- Stochastic comparison added (EXP10)
- Reproducibility package (Online Resource 1) + public code

---

## Paragraph 9 — Artifact and reproducibility

- Online Resource 1: code, scripts, summaries, DRMacIver binary SHA256, EXP10 outputs
- Public GitHub + DOI at submission
- Smoke tests included **[when ready]**

---

## Paragraph 10 — Closing

- Suggested reviewers (3–5 names — prepare separately)
- No competing interests; funding; AI disclosure references manuscript declarations
- Corresponding author: Soroush Vahidi, sv96@njit.edu, ORCID

---

## Statements that must NOT appear

| Prohibited statement | Why |
|---------------------|-----|
| “This work has not been published previously” | False — arXiv + predecessors |
| “Not under consideration elsewhere” without qualification | May be false for predecessor venues |
| “First algorithm for MWFAS” | False |
| “State of the art on all benchmarks” | False — LOLIB |
| “Novel local-ratio method” | Prior art |
| “Guaranteed near-optimal in general” | Only on certified subsets |
| Omitting arXiv / JOCO / DAM | Desk-rejection at COAP |

---

## Attachments checklist for editor

1. Cover letter (this document finalized)
2. Manuscript PDF + LaTeX source
3. Title page (if required separately)
4. Online Resource 1 ZIP
5. Highlights (if required)
6. Related manuscripts: arXiv PDF, JOCO PDF, DAM PDF, EJCO PDF, overlap statement
7. Suggested reviewers list
