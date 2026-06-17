# SNCS Rejection-Risk Audit — Pass 2A

**Date:** 2026-06-17
**Branch audited:** `sncs-retargeting`
**Starting commit:** `d7b0316`
**Pass scope:** diagnosis only for the current SN Computer Science manuscript. No manuscript text, experiments, references, or submission-bundle files were edited in this pass.

## Scope and audited files

The prompt's requested filenames do not exactly match the current `paper_sncs/` layout. The audit used the actual current files below:

| Requested in prompt | Actual file audited |
|---|---|
| `paper_sncs/main.tex` | `paper_sncs/main.tex` |
| `paper_sncs/sections/01_introduction.tex` | `paper_sncs/sections/01_introduction.tex` |
| `paper_sncs/sections/02_related_work.tex` | `paper_sncs/sections/02_related_work.tex` |
| `paper_sncs/sections/03_preliminaries.tex` | `paper_sncs/sections/03_problem_definition.tex` |
| `paper_sncs/sections/04_algorithms.tex` | `paper_sncs/sections/04_algorithmic_framework.tex` and `paper_sncs/sections/04_formal_analysis.tex` |
| `paper_sncs/sections/05_experiments.tex` | `paper_sncs/sections/05_experimental_design.tex` and `paper_sncs/sections/06_results.tex` |
| `paper_sncs/sections/06_discussion.tex` | `paper_sncs/sections/07_discussion.tex` |
| `paper_sncs/declarations/statements_and_declarations.tex` | `paper_sncs/declarations/statements_and_declarations.tex` |
| `paper_sncs/references.bib` | `paper_sncs/bibliography/references.bib` |
| `paper_sncs/main.pdf` | `paper_sncs/main.pdf` |

Supporting evidence also came from:

- `paper_sncs/tables/table_baseline_provenance.tex`
- `paper_sncs/tables/table_sparse_external_baselines.tex`
- `paper_sncs/tables/table_comparison_accounting.tex`
- `paper_sncs/tables/table_ipsns_parameters.tex`
- `paper_sncs/tables/table_exact_validation.tex`
- `paper_sncs/tables/table_lolib_scope.tex`
- `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md`
- `docs/sncs_preparation_202606/README.md`
- `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md`

PDF text was extracted with:

```bash
pdftotext paper_sncs/main.pdf /tmp/sncs_current.txt
```

## Executive summary

The current SNCS manuscript is materially better aligned with a computer-science algorithms audience than the earlier COAP-facing versions. The sparse-digraph scope is explicit, the dense LOLIB boundary is explicit, the seeds are attributed rather than claimed as novel, and the declarations are now low-risk.

The main remaining rejection risks are not overlap or compliance issues. They are manuscript-quality risks:

1. the novelty/significance case is still vulnerable because the post-seed gains are modest and the paper does not yet fully preempt the obvious "incremental over a strong seed" objection;
2. the related-work / recent-reference layer is still too thin for a 2026 SN Computer Science submission;
3. the first-page readability still carries the acronym-density and terminology risk that COAP explicitly flagged.

No new experiments are required to complete the immediate next pass. The next pass should be a manuscript-editing pass that strengthens framing, baseline-justification language, and related-work coverage before any decision about extra comparator implementation is made.

## Risk matrix

| Risk category | Present? | Severity | Evidence/location | Why it matters | Recommended fix | Fix priority |
|---|---|---|---|---|---|---|
| A. Scope and audience mismatch | Partly | Medium | `paper_sncs/main.tex:57-64`; `paper_sncs/sections/01_introduction.tex:4-14`; `paper_sncs/sections/02_related_work.tex:16-20`; `paper_sncs/sections/06_results.tex:52-54` | The paper is now CS-facing, but the front page still opens with some application language that can read broader than the sparse-graph algorithm-engineering core. | Reframe title/abstract/introduction opening around sparse digraph algorithm engineering first, applications second. | P1 |
| B. Acronym overload and readability | Yes | High | `paper_sncs/main.tex:57-64`; `paper_sncs/sections/01_introduction.tex:6-14`; PDF pp. 1-3 (`/tmp/sncs_current.txt`) | COAP explicitly objected to acronym/terminology density. The current abstract still introduces `SCC` before definition and quickly stacks `IPSNS`, `DRMacIver/FAS`, `LOLIB`, `MWFAS`, `LR-TA`, and `WMSF-style`. | Simplify the abstract and first two introduction paragraphs; define concepts before acronyms; expand or rename `WMSF-style`; delay seed acronyms until after the reader has the sparse-digraph picture. | P0 |
| C. Novelty / significance risk | Partly | High | `paper_sncs/sections/01_introduction.tex:10-21`; `paper_sncs/sections/06_results.tex:14,26,39,43`; `paper_sncs/sections/08_conclusion.tex:4-8` | Several prior rejections cited insufficient novelty/significance. The manuscript now states the novelty clearly, but the evidence also admits that only 14 of 97 instances are strict wins over the best seed, only 12 of 93 repeated-run instances ever improve over the seed, and the ablation gain after seeding is 0.76\%. That leaves an obvious reviewer line of attack: "interesting engineering, but too incremental." | Strengthen the contribution framing around what is new and why selective, non-worsening sparse-local refinement is scientifically meaningful even when the deltas are concentrated rather than uniform. | P0 |
| D. Related work and recent references | Yes | High | `paper_sncs/bibliography/references.bib`; `paper_sncs/sections/02_related_work.tex:8-20,26-35`; `paper_sncs/sections/05_experimental_design.tex:23-25` | Prior rejections flagged dated or incomplete baseline context. The bibliography has only 29 entries total, only 11 entries from 2020-2026, and only 6 of those 11 are recent research rather than software/docs. Several reviewer-expected references are still missing. | Add the missing recent and comparison-critical citations, then thread them into related work and baseline-selection paragraphs. | P0 |
| E. External baseline sufficiency | Partly | Medium | `paper_sncs/tables/table_baseline_provenance.tex:8-19`; `paper_sncs/tables/table_sparse_external_baselines.tex:9-33`; `paper_sncs/sections/05_experimental_design.tex:23-25`; `paper_sncs/sections/06_results.tex:12-16` | The current paper has one strong external executable (`DRMacIver/FAS`) and one generic library baseline (`igraph Eades`), but it does not yet explicitly justify why other cited comparator families were not implemented. Reviewers may ask for one more external baseline or at least a stronger omission rationale. | Add a short baseline-selection / omitted-baselines paragraph. Optionally consider one more sparse-graph external comparator, but do not block the immediate editing pass on that. | P1 |
| F. Methodological maturity and reproducibility | Partly | Medium | `paper_sncs/sections/04_algorithmic_framework.tex:47,54,100`; `paper_sncs/sections/04_formal_analysis.tex:4,52`; `paper_sncs/sections/05_experimental_design.tex:39-56`; `paper_sncs/tables/table_ipsns_parameters.tex:4-17` | The paper is substantially reproducible, but several implementation and proof details are deferred to Online Resource 1. That is acceptable, though some reviewers may still want a more self-contained explanation of parameter choices, seed mechanics, and the role of randomness. | Tighten one paragraph in methods and one in experiments so the main paper itself carries the essential parameter/randomness story without forcing the reviewer into the supplement. | P1 |
| G. Overclaiming / scope creep | Partly | Low | `paper_sncs/main.tex:62-64`; `paper_sncs/sections/01_introduction.tex:14`; `paper_sncs/sections/08_conclusion.tex:6-8` | The paper is mostly careful, but the opening result sentences still foreground the 96/97 figure before the reader reaches the later explanation that only 14 are strict wins and that the dense boundary is unfavorable. | Slightly rebalance the abstract and conclusion so the scoped claim and the "consistent refinement layer" interpretation arrive earlier. | P2 |
| H. Dense-vs-sparse confusion | Partly | Low | `paper_sncs/sections/01_introduction.tex:6-14`; `paper_sncs/sections/02_related_work.tex:16-20`; `paper_sncs/sections/03_problem_definition.tex:31-46`; `paper_sncs/sections/06_results.tex:45-54` | The sparse-vs-dense distinction is present and generally strong. The residual risk is only that the ranking/pairwise-comparison lineage remains visible enough that some readers may still infer a closer connection to dense ordering than intended. | Keep the sparse-digraph target sentence at the top of the abstract/introduction and explicitly label dense ordering as a different problem model in one more short sentence. | P2 |
| I. Declarations and submission-risk issues | No | Low | `paper_sncs/declarations/statements_and_declarations.tex:21-30` | The current declaration language is factual, concise, and non-alarming. It no longer sounds blocked or unresolved. | No substantive change needed; only preserve the concise style in later edits. | P2 |
| J. Editorial Manager upload compliance | Partly | Low | `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md:42-52`; `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md:17-27,40`; `docs/sncs_preparation_202606/README.md:15-25` | The current documentation correctly recommends PDF-only initial upload and warns against using the current source ZIP as the main manuscript. The residual risk is procedural: the existing ZIP still contains subfolders, so an inattentive upload would be wrong if the portal later demands source. | No manuscript edit needed. Keep the warning prominent and prepare a flattened source package only if the portal later requires it. | P2 |

## Detailed findings by category

### A. Scope and audience mismatch

**Present?** Partly

**Seriousness for SN Computer Science:** Medium

**Likely effect if uncorrected:** reviewer criticism, with mild desk-risk only when combined with readability issues.

**Evidence**

- The manuscript now clearly aims at a CS graph-algorithms audience in the title and introduction: `paper_sncs/main.tex:50`, `paper_sncs/sections/01_introduction.tex:6-14`.
- The sparse target is explicit early and repeatedly: `paper_sncs/main.tex:58-64`, `paper_sncs/sections/01_introduction.tex:6-8`, `paper_sncs/sections/03_problem_definition.tex:31-46`, `paper_sncs/sections/06_results.tex:52-54`.
- The dense boundary is treated honestly rather than hidden: `paper_sncs/main.tex:62-64`, `paper_sncs/sections/06_results.tex:52-54`, `paper_sncs/tables/table_lolib_scope.tex:4-18`.
- The remaining scope risk is front-page emphasis. The abstract and first introduction paragraph still lead with a general weighted-FAS problem statement and a broad application list including precedence aggregation, scheduling, and ranking, before they fully settle into the sparse-digraph algorithm-engineering frame: `paper_sncs/main.tex:57-60`, `paper_sncs/sections/01_introduction.tex:4-8`.

**Assessment**

- `1. Does the manuscript read as a CS graph-algorithm / algorithm-engineering paper?` Yes, substantially more than the COAP version.
- `2. Does it avoid sounding OR-only or industrial-engineering-only?` Mostly yes.
- `3. Is the title/abstract/first page understandable to a broad CS reader?` Partly; the topic is understandable, but the abstract is still jargon-heavy.
- `4. Does it explicitly explain why sparse digraphs are the target?` Yes; this is one of the better-developed parts of the manuscript.
- `5. Does it clearly distinguish sparse digraphs from dense LOLIB/ranking settings?` Yes.

**What should change in Pass 2B**

- Tighten the opening abstract sentence so sparse digraphs appear as the primary object, not as a later qualifier.
- Reduce the application-list emphasis on page 1 and replace it with one sentence of algorithm-engineering motivation for sparse cyclic structure.
- Keep the dense-ordering contrast, because it is doing useful audience-fit work.

### B. Acronym overload and readability

**Present?** Yes

**Seriousness for SN Computer Science:** High

**Likely effect if uncorrected:** desk-rejection risk on readability/presentation grounds, and clear reviewer criticism.

**Evidence**

- Title: no acronym problem. Good.
- Abstract: at least four meaningful acronym or identifier-like technical labels appear on page 1 alone: `SCC`, `IPSNS`, `DRMacIver/FAS`, `LOLIB`; page 2 adds `MWFAS` in the introduction. If `NP-hard` is counted as acronym-like terminology, that total rises by one. See `paper_sncs/main.tex:57-64` and PDF pp. 1-2.
- `SCC` is used before being defined in the abstract: `paper_sncs/main.tex:60`.
- `IPSNS` is introduced in the same sentence as the unexplained phrase "incumbent-protected SCC neighborhood search": `paper_sncs/main.tex:60`.
- The first three introduction paragraphs are readable, but page 3 immediately adds `LR-TA` and `WMSF-style` on top of `MWFAS`, `SCC`, and `IPSNS`: `paper_sncs/sections/01_introduction.tex:10-14`.
- `WMSF-style` is never properly expanded into a stable readable phrase beyond its provenance discussion. The manuscript explains the line of work but does not give the acronym itself a clean first-definition sentence: `paper_sncs/sections/01_introduction.tex:12`, `paper_sncs/sections/02_related_work.tex:26-28`, `paper_sncs/sections/04_algorithmic_framework.tex:49-54`.

**Assessment**

- `1. Count the acronyms in title, abstract, and first two pages.` Title: 0. Abstract/page 1: 4-5 meaningful technical acronym-like terms (`SCC`, `IPSNS`, `DRMacIver/FAS`, `LOLIB`, optionally `NP-hard`). First two PDF pages together: at least 5 distinct terms, adding `MWFAS`. Page 3 then adds `LR-TA` and `WMSF-style`.
- `2. Paragraphs where acronyms hurt readability.` Abstract methods/results (`paper_sncs/main.tex:60-64`), introduction novelty framing (`paper_sncs/sections/01_introduction.tex:10-14`).
- `3. Is SCC defined before use?` No, not in the abstract. Yes, in the introduction.
- `4. Is IPSNS introduced after the idea is explained?` Partly; the idea and acronym are introduced almost simultaneously.
- `5. Are LR-TA and WMSF delayed until the reader has context?` Partly; they are delayed until page 3, which is acceptable, but they still arrive in a dense burst.
- `6. Exact paragraphs needing simplification.` Abstract methods/results (`paper_sncs/main.tex:60-64`), introduction paragraphs 4-5 (`paper_sncs/sections/01_introduction.tex:10-14`).

**What should change in Pass 2B**

- Define "strongly connected components" before any `SCC` usage in the abstract, or avoid the acronym there entirely.
- Introduce IPSNS after a one-sentence plain-language description of the move.
- Expand or rename `WMSF-style` so it is readable without prior local project context.
- Reduce acronym density on the first three PDF pages even if later technical sections remain unchanged.

### C. Novelty / significance risk

**Present?** Partly

**Seriousness for SN Computer Science:** High

**Likely effect if uncorrected:** reviewer rejection or major-revision pressure on significance grounds.

**Evidence**

- The manuscript does state novelty clearly: `paper_sncs/sections/01_introduction.tex:10-21`, `paper_sncs/sections/02_related_work.tex:33-35`, `paper_sncs/sections/04_algorithmic_framework.tex:56-65`.
- It also carefully disclaims novelty for inherited components: `paper_sncs/sections/01_introduction.tex:12,19-20`; `paper_sncs/sections/04_algorithmic_framework.tex:11,52,59`.
- The vulnerability is not "unclear novelty"; it is "is the improvement scientifically large enough?" The paper itself records:
  - only 14 strict improvements over the better seed on 97 standard instances: `paper_sncs/sections/06_results.tex:14`;
  - only 12 of 93 common sparse instances ever improve over the best seed across 20 IPSNS runs: `paper_sncs/sections/06_results.tex:39`;
  - a 0.76% ablation gain after strong seeding on the 10-instance subset: `paper_sncs/sections/06_results.tex:43`;
  - a 0.42% relative mean improvement over the better seed: `paper_sncs/sections/06_results.tex:14`.

**Assessment**

- `1. Does the introduction state the novelty in a way that is impossible to miss?` Yes.
- `2. Does the paper distinguish inherited seeds from the new contribution?` Yes.
- `3. Does it say exactly what is new?` Yes: fixed original-graph neighborhoods, contribution-based SCC scoring, two-sided perturbation, SCC-restricted repair, strict incumbent protection, and the integrated evaluation.
- `4. Does it avoid claiming LR-TA/WMSF as new?` Yes.
- `5. Is there a clear contributions list?` Yes.
- `6. Is the contribution significant enough for SNCS as currently framed?` Partly. The scientific idea is defensible, but the current framing still leaves reviewers room to say "incremental refinement over strong seeds."

**What should change in Pass 2B**

- Reframe the significance argument around consistency, non-worsening protection, sparse-local targeting, and near-optimality on validated subsets, not just raw best counts.
- Explicitly explain why a concentrated improvement profile is expected and still important in weighted cycle-breaking heuristics.
- Put the "14 strict wins / 83 ties / 0 regressions" story into a more reviewer-proof interpretation early in the introduction or discussion.

### D. Related work and recent references

**Present?** Yes

**Seriousness for SN Computer Science:** High

**Likely effect if uncorrected:** reviewer criticism with real rejection risk if the paper is judged too isolated from current comparator literature.

**Evidence**

- `paper_sncs/bibliography/references.bib` contains **29 total references**.
- Of those, **11** are dated 2020-2026, but only **6** are recent research entries; the other **5** are software/documentation/data-page `@misc` entries.
- Already present from the requested list:
  - Hecht, Gonciarz, Horvát 2021: yes (`HGH21`)
  - Simpson, Srinivasan, Thomo 2016: yes (`SST16`)
  - Baharev, Schichl, Neumaier, Achterberg 2021: yes (`BSNA21`)
  - Brandenburg and Hanauer, "Sorting Heuristics for the Feedback Arc Set Problem": yes (`BH13`)
  - Vahidi and Koutis 2024: yes (`VahidiKoutis2024arxiv`)
- Missing from the requested list:
  - Geladaris, Lionakis, Tollis, "Effective Computation of a Feedback Arc Set Using PageRank," JGAA 2023
  - Cavallaro, Cutello, Pavone, 2023 ITADATA/CEUR version
  - a Jünger / Grötschel / Reinelt weighted-MFAS cutting-plane / dicycle-inequality reference
  - Hanauer, "Linear Orderings of Sparse Graphs"

**Assessment**

- `1. Reference count.` 29 total.
- `2. How many references from 2020-2026?` 11 total; only 6 are recent research papers/proceedings rather than software/docs.
- `3. Requested works already cited?`
  - Hecht/Gonciarz/Horvát 2021: Yes.
  - Cavallaro/Cutello/Pavone 2023 CEUR: No.
  - Geladaris/Lionakis/Tollis 2023: No.
  - Simpson/Srinivasan/Thomo 2016: Yes.
  - Baharev et al. 2021: Yes.
  - Jünger/Grötschel/Reinelt weighted-MFAS discussion: No.
  - Brandenburg and Hanauer sorting heuristics: Yes.
  - Hanauer sparse linear-orderings work: No.
  - Vahidi and Koutis 2024: Yes.
- `4. Where should missing references be cited?`
  - Geladaris/Lionakis/Tollis 2023: `paper_sncs/sections/02_related_work.tex:16-20` and `paper_sncs/sections/05_experimental_design.tex:23-25`
  - Cavallaro/Cutello/Pavone 2023 CEUR: `paper_sncs/sections/02_related_work.tex:26-28` and `paper_sncs/sections/04_algorithmic_framework.tex:49-54`
  - Jünger/Grötschel/Reinelt weighted-MFAS / cutting-plane discussion: `paper_sncs/sections/02_related_work.tex:8-12` or `16-20`, depending on whether framed as exact/linear-ordering context
  - Hanauer sparse-graph ordering work: `paper_sncs/sections/02_related_work.tex:12` or `16-20`
- `5. Serious rejection risk or just improvement?` Serious enough to fix before submission. This is a P0 text-and-citation pass, not a cosmetic improvement.

**What should change in Pass 2B**

- Add the missing references.
- Rewrite two related-work paragraphs so the paper is visibly connected to sparse-graph heuristics, dense-ordering comparators, and recent feedback-set engineering work.
- Add one short baseline-selection paragraph in experiments that cites omitted comparator families even when they are not implemented.

### E. External baseline sufficiency

**Present?** Partly

**Seriousness for SN Computer Science:** Medium

**Likely effect if uncorrected:** reviewer criticism; possible rejection if the paper is judged under-compared.

**Evidence**

- Current baselines in the paper:
  - `internal / proposed`: IPSNS
  - `internal seeds`: LR-TA, WMSF-style seed
  - `library / heuristic calibrators`: igraph Eades, Weighted Eades, Borda/net score, Random multistart
  - `external executable baseline`: DRMacIver/FAS
  - `exact / validation`: Exact DP, HiGHS MIP
  - Source: `paper_sncs/tables/table_baseline_provenance.tex:8-19`
- DRMacIver/FAS is clearly described as external and matrix-based: `paper_sncs/sections/02_related_work.tex:18`; `paper_sncs/sections/05_experimental_design.tex:25`.
- igraph Eades is clearly described as a graph-library baseline: `paper_sncs/tables/table_baseline_provenance.tex:16`; `paper_sncs/sections/05_experimental_design.tex:25`.
- DP and MIP validation are clearly explained: `paper_sncs/sections/05_experimental_design.tex:17,25,31-37`; `paper_sncs/sections/06_results.tex:20-30`.
- What is missing is not raw clarity but omission rationale. The manuscript does not yet explicitly explain why cited families such as TIGHT-CUT*, minOFAS, SortFAS/GreedyFAS variants, or PageRank-style FAS methods were not implemented.

**Assessment**

- `1. List current baselines.` See list above.
- `2. Separate them by class.` Done above.
- `3. Is DRMacIver/FAS clearly described as external?` Yes.
- `4. Is igraph Eades clearly described as external library baseline?` Yes.
- `5. Are DP and MIP validation clearly explained?` Yes.
- `6. Does the paper justify why TIGHT-CUT*, minOFAS, GreedyFAS/SortFAS, and PageRankFAS are cited but not implemented?` No, not yet.
- `7. Risk that reviewers demand one more external baseline?` Yes, moderate.
- `8. Single most useful optional baseline?` If one more external baseline is added later, the most useful one would be a sparse-graph-targeted sorting-heuristic family in the Brandenburg/Hanauer line rather than another dense-ordering comparator. That would answer the most natural reviewer question. It is useful, but not important enough to delay the immediate Pass 2B editing work.

**What should change in Pass 2B**

- Add a short paragraph in `paper_sncs/sections/05_experimental_design.tex` explaining that the current comparison set covers internal seeds, graph-library heuristics, one strong external executable, and exact/certified validators, while some other cited families are referenced for context but were not used due to implementation availability, interface mismatch, or scope.
- Mention explicitly that the paper is not claiming to exhaust all FAS heuristics.

### F. Methodological maturity and reproducibility

**Present?** Partly

**Seriousness for SN Computer Science:** Medium

**Likely effect if uncorrected:** reviewer criticism, not likely desk rejection.

**Evidence**

- Algorithms are presented with pseudocode for LR-TA and IPSNS: `paper_sncs/sections/04_algorithmic_framework.tex:22-45,67-98`.
- Non-worsening and feasibility properties are stated in the paper: `paper_sncs/sections/04_formal_analysis.tex:6-34`.
- Parameters are tabulated: `paper_sncs/tables/table_ipsns_parameters.tex:4-17`.
- Randomness, repeated runs, medians, tests, and bootstrap intervals are documented: `paper_sncs/sections/05_experimental_design.tex:39-56`; `paper_sncs/sections/06_results.tex:35-39`.
- Strict global-improvement acceptance is stated clearly in both abstract and methods: `paper_sncs/main.tex:60`; `paper_sncs/sections/04_algorithmic_framework.tex:65,89-94`.
- Artifact/repository availability is good: `paper_sncs/declarations/statements_and_declarations.tex:24-27`.
- Remaining weakness: several important details are repeatedly deferred to Online Resource 1 rather than summarized concisely in the main paper: `paper_sncs/sections/04_algorithmic_framework.tex:47,54,100`; `paper_sncs/sections/04_formal_analysis.tex:4,52`.

**Assessment**

- `1. Are algorithms specified clearly enough to be reproducible?` Mostly yes.
- `2. Are parameters justified or at least documented?` Yes, documented; justification is modest but acceptable.
- `3. Does the paper include enough pseudocode?` Yes for the main story.
- `4. Does it explain randomness, seeds, repeated runs, and acceptance criteria?` Yes.
- `5. Does it clearly state strict global improvements only?` Yes.
- `6. Does it provide enough artifact/repository information?` Yes.
- `7. Are statistical tests and repeated-run summaries clearly reported?` Yes.
- `8. Are there claims based on too few instances?` Partly. The ablation subset (10 instances) and MIP study (15 instances, 7 certified) are small, but the manuscript already treats them as supporting rather than primary evidence.

**What should change in Pass 2B**

- Add one sentence in methods clarifying the seed mechanics and one sentence in experiments clarifying that parameter defaults are documented in the main paper and expanded in Online Resource 1.
- Keep the main empirical claims tied to the 97-instance sparse benchmark and 93-instance repeated-run subset, not to the small ablation or MIP subsets.

### G. Overclaiming / scope creep

**Present?** Partly

**Seriousness for SN Computer Science:** Low

**Likely effect if uncorrected:** reviewer criticism only.

**Evidence**

- The abstract and conclusion already use "among the evaluated methods": `paper_sncs/main.tex:62-64`; `paper_sncs/sections/08_conclusion.tex:6`.
- The dense boundary is explicit and negative where appropriate: `paper_sncs/main.tex:64`; `paper_sncs/sections/06_results.tex:52-54`; `paper_sncs/sections/07_discussion.tex:10-17`.
- The main residual overclaim risk is rhetorical ordering: the 96/97 result is foregrounded before the later explanation that strict wins are only 14 and that improvements over the better seed are concentrated.

**Assessment**

- `1. Does the abstract overclaim?` Not seriously, but it could still be more conservative in the order of emphasis.
- `2. Does the conclusion overclaim?` No.
- `3. Does the paper say "among the evaluated methods" where needed?` Yes, in the most important places.
- `4. Does it clearly say dense LOLIB is a scope boundary?` Yes.
- `5. Does it avoid implying superiority over all FAS methods?` Mostly yes.
- `6. Are limitations explicit enough?` Yes.

**What should change in Pass 2B**

- Move one scoped-claim sentence earlier in the abstract and conclusion.
- Keep the "consistent refinement layer" framing more prominent than the raw best-count figure.

### H. Dense-vs-sparse confusion

**Present?** Partly

**Seriousness for SN Computer Science:** Low

**Likely effect if uncorrected:** reviewer criticism only.

**Evidence**

- Sparse target is explicit in title, abstract, introduction, problem definition, experiments, results, discussion, and conclusion: `paper_sncs/main.tex:50,58-64`; `paper_sncs/sections/01_introduction.tex:6-14`; `paper_sncs/sections/03_problem_definition.tex:31-46`; `paper_sncs/sections/05_experimental_design.tex:4,19-20`; `paper_sncs/sections/06_results.tex:52-54`; `paper_sncs/sections/08_conclusion.tex:4-8`.
- LOLIB is treated as transfer/boundary, not as the main claim-bearing benchmark: `paper_sncs/sections/05_experimental_design.tex:19-20`; `paper_sncs/sections/06_results.tex:45-54`.
- The residual confusion risk is only that the manuscript still visibly traces back to ranking/pairwise-comparison literature and uses a matrix-ordering external comparator prominently: `paper_sncs/sections/02_related_work.tex:16-20`; `paper_sncs/sections/05_experimental_design.tex:25`.

**Assessment**

- `1. Is the sparse-digraph target clear across the manuscript?` Yes.
- `2. Is LOLIB treated as transfer/scope boundary only?` Yes.
- `3. Does the paper distinguish dense linear ordering methods from the target setting?` Yes.
- `4. Does it avoid mixing claims from the prior ranking manuscript into the sparse-digraph manuscript?` Mostly yes.

**What should change in Pass 2B**

- Only minor reinforcement needed. Keep one short sentence separating sparse-digraph cycle breaking from dense pairwise-comparison ranking early in the introduction and experiments.

### I. Declarations and submission-risk issues

**Present?** No

**Seriousness for SN Computer Science:** Low

**Likely effect if uncorrected:** none likely.

**Evidence**

- No substantially overlapping manuscript under consideration elsewhere is stated clearly: `paper_sncs/declarations/statements_and_declarations.tex:21-22`.
- The COAP declined-submission disclosure is factual and not melodramatic: `paper_sncs/declarations/statements_and_declarations.tex:22`.
- The related Supercomputing manuscript is described as related but distinct and non-overlapping in a concise way: `paper_sncs/declarations/statements_and_declarations.tex:22`.
- The AI disclosure is detailed and responsibility-preserving: `paper_sncs/declarations/statements_and_declarations.tex:29-30`.

**Assessment**

- `1. No substantially overlapping manuscript under consideration elsewhere?` Yes.
- `2. COAP disclosure factual and non-alarming?` Yes.
- `3. Supercomputing wording non-alarming?` Yes.
- `4. AI disclosure acceptable and responsible?` Yes.
- `5. Any unresolved-overlap signal likely to spook an editor?` No.

**What should change in Pass 2B**

- No substantive change is required.

### J. Editorial Manager upload compliance

**Present?** Partly

**Seriousness for SN Computer Science:** Low

**Likely effect if uncorrected:** procedural error only, not scientific rejection.

**Evidence**

- The active SNCS docs correctly recommend PDF-only initial upload: `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md:42-52`; `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md:17-27`; `docs/sncs_preparation_202606/README.md:15-25`.
- The source ZIP is explicitly marked as backup only: `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md:46,52`; `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md:21,27,40`.
- The docs explicitly warn that a flattened source package must be prepared only if source upload becomes necessary: `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md:48`; `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md:23`; `docs/sncs_preparation_202606/README.md:21`.
- The residual risk remains because the existing `Vahidi_SNCS_Source.zip` is a repository-style backup archive with subfolders, so it should not be uploaded unchanged if the portal later requests source.

**Assessment**

- `1. Does the package recommend PDF-only initial upload?` Yes.
- `2. Is the source ZIP marked as backup, not recommended main upload?` Yes.
- `3. Is there risk that the current ZIP could be uploaded incorrectly?` Yes, but the docs warn against it.
- `4. Is there a clear note that flattened LaTeX source should be prepared only if required?` Yes.

**What should change in Pass 2B**

- No manuscript edit needed. Preserve the current warning language in docs.

## Missing-reference checklist for Pass 2B

Do not invent BibTeX in Pass 2A. The following missing items should be added and cited in Pass 2B:

- Geladaris, Lionakis, Tollis, "Effective Computation of a Feedback Arc Set Using PageRank," JGAA 2023.
  - Recommended insertion: `paper_sncs/sections/02_related_work.tex:16-20`
  - Secondary mention: `paper_sncs/sections/05_experimental_design.tex:23-25` as omitted baseline context.

- Cavallaro, Cutello, Pavone, 2023 ITADATA/CEUR version.
  - Recommended insertion: `paper_sncs/sections/02_related_work.tex:26-28`
  - Secondary mention: `paper_sncs/sections/04_algorithmic_framework.tex:49-54`

- A Jünger / Grötschel / Reinelt weighted-MFAS / dicycle-inequality / cutting-plane reference.
  - Recommended insertion: `paper_sncs/sections/02_related_work.tex:8-12` or `16-20`

- Hanauer, "Linear Orderings of Sparse Graphs."
  - Recommended insertion: `paper_sncs/sections/02_related_work.tex:12` or `16-20`

## Recommended Pass 2B edit plan

### 1. Title/abstract/conclusion claim-scope fixes

- `paper_sncs/main.tex`
  - Rewrite the abstract methods sentence to define the move before the acronym.
  - Remove or delay `SCC` in the abstract unless it is defined first.
  - Rebalance the results sentence so scoped interpretation appears as early as the 96/97 figure.
- `paper_sncs/sections/08_conclusion.tex`
  - Tighten the first two paragraphs so the "consistent sparse refinement layer" message is foregrounded over raw best-count language.

### 2. Introduction novelty/contribution fixes

- `paper_sncs/sections/01_introduction.tex`
  - Make the sparse-digraph algorithm-engineering motivation more prominent than the broad application list.
  - Add one sentence explaining why selective, non-worsening local refinement is scientifically meaningful even when improvements are concentrated.
  - Simplify the paragraph that currently introduces `IPSNS`, `LR-TA`, and `WMSF-style` in rapid succession.
  - Expand or rename `WMSF-style` so it reads cleanly.

### 3. Related-work and recent-reference fixes

- `paper_sncs/sections/02_related_work.tex`
  - Add the missing recent comparator and context references listed above.
  - Strengthen the sparse-heuristic and dense-ordering comparison context.
  - Add one explicit sentence locating this paper relative to weighted MFAS exact/ordering literature and sparse-graph heuristic literature.
- `paper_sncs/bibliography/references.bib`
  - Add the missing bibliography entries in Pass 2B.

### 4. Baseline-selection and why-not-added-baselines fixes

- `paper_sncs/sections/05_experimental_design.tex`
  - Add a concise paragraph explaining why the comparison set includes one strong external executable, one graph-library baseline, internal seeds, and exact/certified validators.
  - Add one sentence explaining why other cited families are contextual rather than implemented in this pass.
- `paper_sncs/sections/02_related_work.tex`
  - Cross-reference the omitted baseline families so the experiments section does not look arbitrary.

### 5. Experimental-method / reproducibility fixes

- `paper_sncs/sections/04_algorithmic_framework.tex`
  - Add one self-contained sentence summarizing the role of the default parameters and the reproducibility conditions.
- `paper_sncs/sections/05_experimental_design.tex`
  - Add one sentence clarifying that the defaults in Table `tab:ipsns-parameters` are documented in the main paper and expanded in Online Resource 1.
  - Keep the repeated-run and statistical-treatment wording, which is already strong.

### 6. Declarations / submission-package fixes

- `paper_sncs/declarations/statements_and_declarations.tex`
  - No substantive edit required unless the front-matter readability pass forces a terminology cleanup.
- `docs/sncs_preparation_202606/SUBMISSION_PACKAGE_STATUS.md`
  - No immediate edit required for the rejection-risk pass.
- `paper_sncs/submission/sncs_initial/README_SNCS_UPLOAD.md`
  - No immediate edit required for the rejection-risk pass.

## Final audit verdict

The current SNCS manuscript is **not** blocked by overlap, declaration, or upload-compliance issues. It **is** still exposed to avoidable reviewer-level rejection risk on three fronts:

1. acronym/readability density on the front page;
2. novelty/significance framing versus modest post-seed gains;
3. insufficiently developed related-work and omitted-baseline context for a 2026 SN Computer Science submission.

These are manuscript-edit risks, not experiment-blocking risks. They should be addressed before SNCS submission.
