# Rejection Concern Action Items

Date: 2026-06-06

## A. Must fix in manuscript text

- Explicitly say that local-ratio is prior work and that the manuscript's contribution is the engineered LR-TA plus IPSNS framework.
- Use "minimum weighted feedback arc set" consistently when the optimization objective is meant.
- Add one short explanation that IPSNS's monotone non-degradation invariant is a guarantee about refinement quality, not an approximation ratio.
- Discuss deterministic topological extraction as an implementation choice and note that linear extensions of a DAG are not unique.
- State plainly that the paper targets sparse nonnegative weighted digraphs and that dense LOLIB is included as a transfer test and scope boundary.
- Make the parameter-justification paragraph conservative: EXP2 supports the chosen defaults on the ablation subset, not universal optimal tuning.

## B. Must fix in tables / figures

- In the EXP4 sparse baseline table narrative, explicitly identify DRMaciver as the strongest external baseline on the primary benchmark.
- In the EXP3 exact-validation narrative, label the result as empirical near-optimality only.
- In the EXP5 LOLIB table narrative, state that DRMaciver is stronger on dense tournaments and that this bounds the claim surface.
- Keep the algorithm invariants table visible in the main paper; it directly addresses rigor concerns.

## C. Already fixed by EXP1b--EXP5

- EXP1b: incumbent protection never worsens LR-TA or WMSF on the 105-instance internal benchmark.
- EXP2: supports the topological add-back phase, IPSNS refinement increment, and limited parameter rationale.
- EXP3: answers the "heuristic without any exact reference point" concern on small instances.
- EXP4: answers baseline-strength concerns for classical weighted-digraph heuristics on the standard sparse benchmark.
- EXP5: prevents overclaiming by showing the dense linear-ordering boundary explicitly.

## D. Optional if space permits

- Mention GNNRank and similar learned ranking methods in Related Work as out-of-scope comparators.
- Add a sentence about runtime and reproducibility tradeoffs using existing reports, without opening a new profiling campaign.
- Add a short note that the repository must be public at submission and that DOI creation is pending.

## E. Not recommended

- Do not start a new graph-family benchmark campaign before the manuscript draft is complete.
- Do not add a learned baseline or commercial exact solver now; the setup burden is too high relative to the verified concern record.
- Do not claim a new approximation guarantee, theoretical dominance, or dense LOP competitiveness.
- Do not fabricate direct reviewer wording where only memory or planning notes exist.
