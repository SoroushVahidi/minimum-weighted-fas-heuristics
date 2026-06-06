# Reuse Risk Report

This workspace should not copy predecessor manuscript text directly into the new paper. The predecessor archives are useful for structure, notation, citations, and cautionary context, but all claims need to be revalidated against current HEAD.

## High-Risk Material

- Any experimental claims from the rejected JOCO or DAM manuscripts. These are superseded by EXP1b--EXP5.
- Any statement implying a new approximation guarantee. The new manuscript should not claim one unless a separate proof is added.
- Any broad state-of-the-art claim. EXP5 shows that dense LOLIB is a scope boundary where DRMacIver/FAS is stronger.
- Any claim that the repository is public. The current scaffold marks this as a TODO.
- Any statement that ignores negative-weight exclusions. Nonnegative MWFAS claims should not be generalized to excluded negative-weight instances.

## Lower-Risk Material

- General problem motivation, after citation checks.
- Basic MWFAS definitions and ordering/backward-edge equivalence, after notation is harmonized.
- High-level descriptions of local-ratio background, if attributed to original sources.
- The idea of SCC-local refinement, if rewritten to match current IPSNS code and current terminology.

## Required Before Drafting Full Text

- Reconcile algorithm descriptions with current code behavior.
- Replace all predecessor result numbers with the combined EXP1b--EXP5 digest and tables.
- Verify every BibTeX entry used in prose.
- Decide target Elsevier journal and final frontmatter metadata.
