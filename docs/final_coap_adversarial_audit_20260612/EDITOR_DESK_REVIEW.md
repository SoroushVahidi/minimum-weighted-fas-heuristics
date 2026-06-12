# Simulated COAP Handling Editor Desk Review

**Perspective:** Skeptical handling editor, first-pass materials only.

## Materials reviewed

Cover letter, title, abstract, introduction (pp. 1–2), contribution list, related-work disclosure (§2.1), Table sparse external baselines, declarations, related-manuscript statement.

## Scoring key

`no concern` | `minor concern` | `moderate concern` | `major concern` | `desk-rejection risk`

---

### Scope — **no concern**

| Question | Assessment |
|---|---|
| Clearly computational optimization? | Yes — MWFAS heuristics, formal supporting analysis, extensive computational evidence |
| Problem important for COAP? | Yes — graph optimization, feedback arc set, algorithm engineering |
| Algorithm development + evidence vs. domain-only? | Yes — IPSNS framework, ablations, exact/MIP validation |
| Sparse-graph focus explained? | Yes — introduction and problem definition distinguish sparse digraphs from dense LOLIB |

### Novelty visibility — **no concern** (post-trim)

| Question | Assessment |
|---|---|
| IPSNS primary new contribution? | Yes — title, abstract, contribution bullet 1, introduction |
| LR-TA and WMSF attributed correctly? | Yes — “not claimed as new,” Demetrescu–Finocchi and Cavallaro–Cutello cited |
| Integration clear without 20 pages? | Yes — framework figure and §4 overview |
| Contribution list leads with new element? | Yes — IPSNS first |
| Title matches central contribution? | Yes — SCC-local destroy-and-repair on sparse MWFAS |

### Incremental-publication risk — **minor concern**

| Question | Assessment |
|---|---|
| arXiv:2412.16181 disclosed? | Yes — cover letter, related-work §2.1, related-manuscript statement |
| JOCO and DAM disclosed? | Yes — JOCO-D-26-00099, DA19469 |
| CAIE/EJCO accurate? | **Author confirmation needed** — packages prepared; submission history not verified in repo |
| Overlap vs. new content distinguished? | Yes |
| Double claiming avoided? | Yes |
| Substantial integrated advance? | Yes — unified framework, expanded validation, EXP10/EXP11, OR1 |

**Desk-rejection risk:** low. Related-manuscript volume is high but transparently disclosed.

### Evidence strength — **no concern**

Abstract and introduction communicate bounded sparse-benchmark advantage, exact/MIP checks, LOLIB scope boundary, EXP10 medians (38/55/0). Qualifications are proportionate (“best observed among evaluated methods”). Length is substantial but organized.

### Reproducibility — **minor concern**

| Question | Assessment |
|---|---|
| OR1 described accurately? | Yes |
| GitHub identified? | Not in main declarations as public URL (appropriate while private) |
| Data-deposition claims match public state? | OR1 bundle is submission artifact; benchmarks cited, not bundled |
| “Fully reproducible” avoided? | Yes |

**Note:** Private GitHub during review is acceptable if OR1 is complete; author should confirm release plan.

---

## Area scores

| Area | Score |
|---|---|
| Scope | no concern |
| Novelty visibility | no concern |
| Incremental-publication risk | minor concern |
| Evidence strength | no concern |
| Reproducibility | minor concern |

## Overall desk assessment

**Proceed to review.** No desk-rejection trigger identified. Editor may flag related-manuscript history and length at assignment, not at triage.
