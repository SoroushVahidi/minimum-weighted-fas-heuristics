# Section Change Log

**Audit date:** 2026-06-11  
**Scope:** Non-result-dependent COAP manuscript reframing (`paper_coap/`). Numerical tables unchanged.

---

## Global

| File | Change |
|------|--------|
| `main.tex` | New IPSNS-first title and running head; abstract rewritten (IPSNS → seeds → validation → scoped sparse result → LOLIB boundary → qualified reproducibility); `% EXP10-INTEGRATION` comment in abstract source only |
| `declarations/statements_and_declarations.tex` | Added **Related manuscripts and prior author work**; qualified data/code availability (OR1 pending) |
| `bibliography/references.bib` | Added `VahidiKoutis2024arxiv`, `HuangfuHall2018`, `CCP24`; retained verified `CC25`, `DF03`, etc. |
| `tables/table_algorithm_components.tex` | LR-TA = inherited seed; WMSF = CC25 engineered variant; IPSNS = primary new integrated heuristic |

---

## §1 Introduction (`sections/01_introduction.tex`)

- IPSNS presented as **primary new algorithmic contribution** with narrow integration novelty.
- LR-TA positioned as inherited/refined from DF03 and arXiv VK; WMSF as CC25 engineered variant.
- Contribution list reordered: (1) IPSNS, (2) integrated framework, (3) computational evidence, (4) supporting correctness + reproducibility infrastructure.
- Stochastic robustness explicitly pending EXP10; `% EXP10-INTEGRATION` comments at paragraph and contribution bullet.
- Empirical language scoped to **best observed among the evaluated methods**.

---

## §2 Related work (`sections/02_related_work.tex`)

- New **§2.1 Relationship to our prior work** (`\label{subsec:prior-work}`): arXiv:2412.16181, JOCO LR-TA archive, DAM IPSNS archive, CAIE/EJCO packages (neutral on submission outcomes); `% AUTHOR-STATUS` comments for cover letter only.
- arXiv predecessor content enumerated (MWFAS ranking framing, cycle peeling, reinsertion, topological extraction, pairwise experiments).
- COAP incremental additions listed explicitly.
- LR-TA paragraph softened: engineering pipeline, not new local-ratio theory.
- WMSF/CC25 + CCP24 lineage noted in heuristic literature paragraph.

---

## §4 Algorithmic framework (`sections/04_algorithmic_framework.tex`)

- LR-TA: inherited DF03 + VK lineage; floating-point qualification; add-back inclusion-minimal ≠ global minimum.
- WMSF: CC25 engineered variant extending CCP24; not a new paper contribution; pipeline deviations disclosed.
- IPSNS: primary contribution; standard LNS/SCC/rollback ingredients not claimed novel individually.

---

## §4 Formal analysis (`sections/04_formal_analysis.tex`)

- Retitled **Supporting correctness properties**; proofs removed from main text (deferred to OR1).
- Proposition on budgeted termination merged into incumbent monotonicity; labeled supporting, not headline theory.

---

## §5 Experimental design (`sections/05_experimental_design.tex`)

- IPSNS as method of interest; LR-TA/WMSF as seeds only.
- HiGHS cite via `HuangfuHall2018`; holdout study described conservatively.
- Reproducibility qualified; `% EXP10-INTEGRATION` anchor for future subsection.

---

## §6 Results (`sections/06_results.tex`)

- **Wording only** (tables untouched): “tested methods” → “evaluated methods”; removed “fully reproducible” closing phrasing.

---

## §7 Discussion (`sections/07_discussion.tex`)

- Expanded limitations enumerate all 10 required scope items.
- EXP10 pending language in limitation item 8 with `% EXP10-INTEGRATION` comment.
- Opening/closing sparse claims scoped to evaluated methods.

---

## §8 Conclusion (`sections/08_conclusion.tex`)

- IPSNS-first conclusion; LR-TA/WMSF as supporting seeds; LOLIB boundary explicit; `% EXP10-INTEGRATION` comment.

---

## Unchanged by design

- All numerical tables (`tables/table_*.tex` except algorithm components).
- `sections/03_problem_definition.tex`.
- Experiment outputs, checkpoints, logs, and source code under `src/` and `experiments/`.
