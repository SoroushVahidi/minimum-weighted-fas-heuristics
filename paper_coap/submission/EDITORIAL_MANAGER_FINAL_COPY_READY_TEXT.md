# Editorial Manager — Final Copy-Ready Text

**Canonical location:** `paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`  
**Date prepared:** 2026-06-12  
**Purpose:** Exact text to paste field-by-field into the COAP Editorial Manager portal. Do not paraphrase — paste verbatim.

---

> **PRE-SUBMISSION GATE — AUTHOR CONFIRMATION REQUIRED BEFORE PASTING ANY TEXT**
>
> The cover letter contains the declaration: "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission."
>
> This file does **not** assert that JOCO-D-26-00099 or DA19469 are currently inactive. Their statuses are documented in author submission records, not in repository files. Before opening the portal and pasting any text below:
>
> 1. Check whether JOCO-D-26-00099 (LR-TA, Journal of Combinatorial Optimization) is currently under active peer review.
> 2. Check whether DA19469 (IPSNS, Discrete Applied Mathematics) is currently under active peer review.
> 3. If either is still under active peer review, do not paste the cover-letter statement as written — consult the CONCURRENT_SUBMISSION_DECISION_TREE.md for required action.
> 4. If both are inactive (withdrawn, rejected, or accepted), the cover-letter statement is accurate and submission may proceed.
>
> Fields below are organized as: **PASTE VERBATIM** (safe without confirmation) and **CONFIRM BEFORE PASTING** (depends on JOCO/DAM status).

---

## Manuscript title

SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs

---

## Running title / Short title

SCC-Local Heuristics for MWFAS on Sparse Digraphs

---

## Article type

Original Research Article

*(If the portal does not list "Original Research Article", choose "Full Length Paper", "Research Article", or the closest equivalent for a novel methods + computational study.)*

---

## Abstract

*(238 words — within COAP 150–250 guideline. Paste as plain text; do not include LaTeX commands.)*

The minimum weighted feedback arc set (MWFAS) problem asks for a minimum-weight set of arcs whose removal makes a nonnegative weighted directed graph acyclic, equivalently a vertex ordering minimizing backward arc weight on sparse digraphs. Despite its NP-hardness, scalable heuristics are needed where exact solvers are too expensive and dense tournament methods are structurally mismatched.

We introduce IPSNS (incumbent-protected SCC neighborhood search), an SCC-local destroy-and-repair heuristic that scores strongly connected components by backward contribution, applies weighted top-K neighborhood selection, performs two-sided perturbations and repairs within fixed original-graph SCC neighborhoods, and accepts moves only under strict incumbent protection. IPSNS uses an integrated framework with a refined LR-TA seed from the Demetrescu–Finocchi local-ratio lineage and an engineered WMSF-style seed from Cavallaro and Cutello's weighted feedback arc set method.

This study is not an approximation-ratio theorem. On the evaluated sparse nonnegative weighted-digraph benchmark, IPSNS attains the best observed backward weight among compared methods on 96 of 97 standard instances. A repeated-run study on the 93-instance common sparse subset (20 IPSNS seeds and 20 DRMacIver/FAS repetitions) compares per-instance medians and corroborates the IPSNS advantage (38 wins, 55 ties, 0 losses). Exact validation on 57 small instances matches the bitmask dynamic-programming optimum on 56 cases; time-capped mixed-integer validation on medium instances adds certified reference points. A dense LOLIB transfer study identifies a scope boundary where matrix-based pairwise-ordering methods are stronger. Online Resource 1 supplies code, configurations, summary outputs, and reproduction scripts (see Data Availability).

---

## Keywords

*(6 keywords; verify the portal separator — use semicolons if no specific guidance, or enter each in a separate field.)*

Minimum weighted feedback arc set; Combinatorial optimization; Local-ratio algorithm; Strongly connected components; Heuristic search; Algorithm engineering

---

## Subject classifications / MSC codes

*(Enter if the portal requests AMS subject classifications.)*

- 90C27 — Combinatorial optimization
- 68W25 — Approximation algorithms
- 05C85 — Graph algorithms

---

## Author information

**Family name:** Vahidi  
**Given name:** Soroush  
**Email:** sv96@njit.edu  
**Institution:** New Jersey Institute of Technology  
**Department:** Department of Computer Science  
**City:** Newark  
**State/Province:** NJ  
**Postal code:** 07102  
**Country:** USA  
**ORCID:** 0000-0003-1934-6282  
**Corresponding author:** Yes (sole author)

---

## Statements and Declarations

### Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

### Competing interests

The author declares that there are no known competing financial or non-financial interests that could have appeared to influence the work reported in this paper.

### Author contributions

Soroush Vahidi: Conceptualization, Methodology, Software, Formal analysis, Investigation, Validation, Data curation, Visualization, Writing – original draft, Writing – review & editing.

### Data availability

Online Resource 1 (supplementary PDF and artifact archive) accompanies this submission. It contains code, configurations, summary outputs, and reproduction scripts. The public benchmark instances are cited in the manuscript and available at https://github.com/alidasdan/graph-benchmarks.

### Code availability

Included in Online Resource 1 (Vahidi_Online_Resource_1_MWFAS.zip).

### AI / Generative AI disclosure

During the preparation of this work, the author used AI-assisted tools, including ChatGPT, Codex, Claude, and Perplexity AI, to support literature exploration, organization of material, language editing, and coding assistance. The author reviewed and edited all outputs, verified the relevant sources and experimental results, and takes full responsibility for the content of the submitted manuscript.

---

## Related work / originality statement

*(Paste in the portal's "Comments to the editor" or "Related manuscripts" free-text field if present, or reference the uploaded related-manuscript statement.)*

**PASTE VERBATIM — does not assert JOCO/DAM status; discloses prior work accurately regardless of status:**

A public preprint (arXiv:2412.16181) and previously submitted author manuscripts (JOCO-D-26-00099; DA19469) are disclosed. Prepared CAIE/EJCO packages are described in the enclosed related-manuscript statement. This COAP submission integrates and extends those strands; IPSNS is the primary new integrated contribution.

---

## Suggested reviewers

*(Enter in the portal's suggested reviewers step. List verified candidates only.)*

1. Kathrin Hanauer, University of Vienna — kathrin.hanauer@univie.ac.at  
   Expertise: graph algorithms, feedback arc sets, competitive algorithm design
2. Petra Mutzel, University of Bonn — petra.mutzel@cs.uni-bonn.de  
   Expertise: combinatorial optimization, graph drawing, algorithm engineering
3. Giuseppe Lancia, University of Udine — giuseppe.lancia@uniud.it  
   Expertise: combinatorial optimization, integer programming, bioinformatics scheduling
4. Eduardo Uchoa, Universidade Federal Fluminense — eduardo_uchoa@id.uff.br  
   Expertise: branch-and-cut, vehicle routing, exact and heuristic methods
5. Ivana Ljubic, ESSEC Business School — ljubic@essec.edu  
   Expertise: network design, combinatorial optimization, MIP

*(See `SUGGESTED_REVIEWER_REGISTER.csv` for verification notes.)*

---

## Opposed reviewers

None unless the author documents a specific conflict of interest before submission.

---

## Preprint disclosure

*(If the portal has a dedicated arXiv/preprint field:)*

arXiv:2412.16181 (December 2024) — "Minimum Weighted Feedback Arc Sets for Ranking from Pairwise Comparisons" (Vahidi and Koutis). The COAP submission substantially extends and supersedes that preprint.

---

## Upload file checklist

| Order | File | Designation |
|---|---|---|
| 1 | Vahidi_COAP_Manuscript.pdf | Manuscript |
| 2 | Vahidi_COAP_Cover_Letter.pdf | Cover Letter (editor-only) |
| 3 | Vahidi_COAP_Manuscript_Source.zip | LaTeX Source Files |
| 4 | Vahidi_Online_Resource_1_MWFAS.pdf | Supplementary Information / Online Resource |
| 5 | Vahidi_Online_Resource_1_MWFAS.zip | Supplementary Material (Data/Code) |
| 6 | Vahidi_Related_Manuscripts_Statement.pdf | Cover Letter (Other — editor-only) |

---

## Notes for author at portal time

- Complete the PRE-SUBMISSION GATE at the top of this file before opening the portal
- Verify the generated PDF preview before approving: check title page, abstract, keyword section, all supplementary entries
- Reviewer email addresses were drawn from public faculty pages as of 2026-06-12; verify they are current before entering
- The cover letter statement "no substantially overlapping manuscript by me is under consideration elsewhere" must be accurate at the moment of clicking Submit — see CONCURRENT_SUBMISSION_DECISION_TREE.md
- Do not submit if either JOCO or DAM is still under peer review without first amending the cover letter
- Complete AUTHOR_PRE_SUBMISSION_CONFIRMATION.md and sign off all checkboxes before clicking Submit

## Field classification legend

**PASTE VERBATIM** — text is factually correct independent of JOCO/DAM status; safe to paste as written.

**CONFIRM BEFORE PASTING** — text depends on JOCO/DAM status or other author-only facts; verify first.

**PORTAL SELECTION** — not text to paste; describes which portal option to choose.

**UNVERIFIED PORTAL BEHAVIOR** — behavior not confirmed from a logged-in session; may vary.
