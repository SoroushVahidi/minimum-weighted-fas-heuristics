# SNCS Submission Metadata

## Manuscript title

An Incumbent-Protected Component-Local Heuristic for Minimum Weighted Feedback Arc Set on Sparse Digraphs

## Short title / running title

Component-Local Heuristic for MWFAS

## Article type

Original Research

Source: `docs/sncs_preparation_202606/SNCS_GUIDELINE_CHECK.md`

## Author

Soroush Vahidi  
Department of Computer Science, New Jersey Institute of Technology  
Newark, NJ 07102, USA  
Email: `sv96@njit.edu`  
ORCID: `0000-0003-1934-6282`

## Corresponding author

Soroush Vahidi

## Keywords

- Feedback arc set
- Graph algorithms
- Combinatorial optimization
- Heuristic search
- Strongly connected components
- Algorithm engineering

## Abstract

**Purpose:** The minimum weighted feedback arc set problem seeks a minimum-weight arc set whose removal makes a directed graph acyclic, equivalently a vertex ordering of minimum backward-arc weight. It is NP-hard and arises in precedence aggregation, scheduling, and ranking from directed evidence. We target sparse nonnegative weighted digraphs, where exact methods do not scale broadly and dense ordering heuristics are not always well aligned.

**Methods:** We propose an incumbent-protected, component-local destroy-and-repair heuristic. It scores strongly connected components (SCCs) by backward-weight contribution, perturbs a randomly selected component neighborhood, repairs it with local-ratio reduction and heavy-first add-back, and accepts only strict global improvements. We refer to this refinement method as incumbent-protected SCC neighborhood search (IPSNS). It refines the better of two attributed constructive seeds and is evaluated against exact, mixed-integer, graph-library, external-tool, and dense-transfer baselines.

**Results:** Among the evaluated methods, the refinement attains the minimum observed backward weight on 96 of 97 standard nonnegative sparse instances, with ties credited to every tied method (14 strict improvements, 83 ties, 0 regressions versus the better seed). On a 57-instance exact-validation subset, the mean optimum-normalized gap is 0.0031\%. Repeated-run per-instance medians over 20 runs on a 93-instance common subset give 38 wins, 55 ties, and 0 losses against DRMacIver/FAS, with a mean comparator-normalized reduction of 21.60\%. On 50 dense LOLIB instances, the comparator was favored on 45.

**Conclusion:** Incumbent-protected, component-local refinement is an effective sparse-digraph algorithm-engineering strategy among the evaluated methods, though it does not dominate dense complete-ordering benchmarks, where matrix-based heuristics remain preferable.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Competing interests

The author declares that there are no known competing financial or non-financial interests that could have appeared to influence the work reported in this paper.

## Data and code availability

The source code, experiment outputs, Online Resource~1, and submission bundle are publicly available from the GitHub repository `https://github.com/SoroushVahidi/minimum-weighted-fas-heuristics`, which is public at the time of submission. The SN Computer Science manuscript PDF, source snapshot, and upload bundle are served from `paper_sncs/submission/sncs_initial/` on the repository main branch; the scientific source snapshot recorded in `online_resource_1/provenance/source_commit.txt` identifies the exact commit used to build the accompanying artifact. Online Resource~1 is provided as `online_resource_1/Online_Resource_1.pdf` and as the upload ZIP in the same `sncs_initial/` directory. Public benchmark families are cited in the manuscript: sparse instances from `graph-benchmarks` and dense LOLIB 2010 instances. External-tool versions and acquisition procedures are documented in Online Resource~1 (§ S5, S8--S9). No Zenodo DOI is assigned at the time of submission.

Reproducing the full benchmark runs additionally requires the documented external data, third-party tools, and computational resources described in Online Resource~1. The package is intended to make the reported evidence traceable without requiring every reader to rerun the most expensive computations.

## Ethics / consent

**Ethics approval:** Not applicable. This study involves no human participants, human data, or animal subjects; it is a computational study on public graph benchmark instances.

**Consent to participate:** Not applicable.

**Consent for publication:** Not applicable.

## AI disclosure

During the preparation of this work, the author used AI-assisted tools, including ChatGPT, Codex, Claude, and Perplexity AI, to support literature exploration, organization of material, language editing, and coding assistance. These tools did not independently select scientific conclusions, create experimental observations, fabricate or alter data, certify proofs, determine acceptance or rejection decisions, or supply unverified references as final citations. The author reviewed and edited all outputs, checked references against primary sources, reviewed and tested code changes, and recomputed or validated numerical claims. The author assumes full responsibility for the content of the submitted manuscript.

## Related manuscript disclosure

An earlier version of this manuscript was submitted to Computational Optimization and Applications and was declined on journal-audience/fit grounds. The present version retargets the same scientific contribution for a broader computer-science algorithms audience. Section~\ref{subsec:prior-work} describes the relationship to the public preprint \cite{VahidiKoutis2024arxiv} and explains how the LR-TA and WMSF-style components are attributed. No substantially overlapping manuscript is currently under consideration elsewhere. A related but distinct manuscript concerning learning-free ranking from pairwise comparisons via feedback-arc-set pruning and add-back is being handled separately; it does not substantially overlap with the present sparse-digraph SCC-local refinement study.

## Recommended files to upload

**Main Manuscript:**  
`paper_sncs/submission/sncs_initial/Vahidi_SNCS_Manuscript.pdf`

**Backup only, do not upload unless required:**  
`paper_sncs/submission/sncs_initial/Vahidi_SNCS_Source.zip`

## Editorial Manager note

For initial submission, upload the PDF manuscript as the main Manuscript file. Do not upload the source ZIP unless the portal explicitly requires LaTeX source. If source upload becomes required, prepare a separate flattened no-subfolder LaTeX package.
