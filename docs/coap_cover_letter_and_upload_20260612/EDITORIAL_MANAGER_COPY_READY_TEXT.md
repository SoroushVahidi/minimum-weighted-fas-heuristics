# Editorial Manager Copy-Ready Text

## Manuscript title

SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs

## Running title

SCC-Local Heuristics for MWFAS on Sparse Digraphs

## Article type

Original Research / Research Article

## Abstract

*(Matches `paper_coap/main.tex`; 238 words — within COAP 150–250 guideline)*

The minimum weighted feedback arc set (MWFAS) problem asks for a minimum-weight set of arcs whose removal makes a nonnegative weighted directed graph acyclic, equivalently a vertex ordering minimizing backward arc weight on sparse digraphs. Despite its NP-hardness, scalable heuristics are needed where exact solvers are too expensive and dense tournament methods are structurally mismatched.

We introduce IPSNS (incumbent-protected SCC neighborhood search), an SCC-local destroy-and-repair heuristic that scores strongly connected components by backward contribution, applies weighted top-K neighborhood selection, performs two-sided perturbations and repairs within fixed original-graph SCC neighborhoods, and accepts moves only under strict incumbent protection. IPSNS uses an integrated framework with a refined LR-TA seed from the Demetrescu–Finocchi local-ratio lineage and an engineered WMSF-style seed from Cavallaro and Cutello's weighted feedback arc set method.

This study is not an approximation-ratio theorem. On the evaluated sparse nonnegative weighted-digraph benchmark, IPSNS attains the best observed backward weight among compared methods on 96 of 97 standard instances. A repeated-run study on the 93-instance common sparse subset (20 IPSNS seeds and 20 DRMacIver/FAS repetitions) compares per-instance medians and corroborates the IPSNS advantage (38 wins, 55 ties, 0 losses). Exact validation on 57 small instances matches the bitmask dynamic-programming optimum on 56 cases; time-capped mixed-integer validation on medium instances adds certified reference points. A dense LOLIB transfer study identifies a scope boundary where matrix-based pairwise-ordering methods are stronger. Online Resource 1 supplies code, configurations, summary outputs, and reproduction scripts (see Data Availability).

## Keywords

Minimum weighted feedback arc set; Combinatorial optimization; Local-ratio algorithm; Strongly connected components; Heuristic search; Algorithm engineering

## Competing interests

The author declares that there are no known competing financial or non-financial interests that could have appeared to influence the work reported in this paper.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Author contributions

Soroush Vahidi: Conceptualization, Methodology, Software, Formal analysis, Investigation, Validation, Data curation, Visualization, Writing – original draft, Writing – review & editing.

## Data availability

Online Resource 1 (supplementary PDF and artifact archive) accompanies this submission. It contains proofs, extended tables, EXP10/EXP11 materials, implementation, tests, and reproduction scripts. Public benchmark instances are cited in the manuscript.

## Code availability

Included in Online Resource 1 (`Vahidi_Online_Resource_1_MWFAS.zip`).

## Generative AI disclosure

During the preparation of this work, the author used AI-assisted tools, including ChatGPT, Codex, Claude, and Perplexity AI, to support literature exploration, organization of material, language editing, and coding assistance. The author reviewed and edited all outputs, verified the relevant sources and experimental results, and takes full responsibility for the content of the submitted manuscript.

## Related-work / originality (portal free text)

A public preprint (arXiv:2412.16181) and previously submitted author manuscripts (JOCO-D-26-00099; DA19469) are disclosed. Prepared CAIE/EJCO packages are described in the related-manuscript statement. This COAP submission integrates and extends those strands; IPSNS is the primary new integrated contribution.

## Suggested reviewers (top 5)

1. Kathrin Hanauer, University of Vienna, kathrin.hanauer@univie.ac.at  
2. Petra Mutzel, University of Bonn, petra.mutzel@cs.uni-bonn.de  
3. Giuseppe Lancia, University of Udine, giuseppe.lancia@uniud.it  
4. Eduardo Uchoa, Universidade Federal Fluminense, eduardo_uchoa@id.uff.br  
5. Ivana Ljubic, ESSEC Business School, ljubic@essec.edu  

## Opposed reviewers

None unless author documents a specific conflict.
