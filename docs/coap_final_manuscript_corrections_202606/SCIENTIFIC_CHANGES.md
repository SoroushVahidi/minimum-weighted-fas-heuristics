# Scientific Changes — COAP Final Manuscript Corrections

## Title page and author metadata

- ORCID rendered as a linked identifier under affiliation (`0000-0003-1934-6282`).
- Correspondence line simplified to “Corresponding author:” with email `sv96@njit.edu` (no trailing semicolon).
- Affiliation formatted as NJIT Department of Computer Science, Newark, NJ 07102, USA.

## Tables and layout

- **Table 1 (baseline provenance):** replaced with concise Method / Role / Origin / Problem model / Execution behavior / Evaluation setting columns; detailed provenance moved to OR1.
- **Table 2 (study accounting):** replaced with Study / Purpose / Instances / Repetitions / Reference rule / Primary analysis; internal EXP labels demoted.
- **Primary sparse comparison:** split into Panel A (common 93-instance subset) and Panel B (completion availability); DAG interface failures and timeouts disclosed explicitly.
- **Table 6 (dense LOLIB):** widened to `\textwidth`, centered, with readable method column; interpretive scope claims moved to Section 6.5.
- **New tables:** IPSNS engineering defaults; benchmark structural characteristics; IPSNS-versus-best-seed contribution on 97 instances.

## Metrics and claims

- **96-of-97 result:** retained with explicit tie-credit wording; added unique-best / strict-win context.
- **Seed contribution (97 instances):** 14 strict improvements, 83 ties, 0 regressions from tracked EXP1b summaries.
- **Exact-validation gap:** reported as mean optimum-normalized gap (0.003% on 57 standard instances); zero-optimum cases handled separately.
- **Relative performance:** renamed to comparator-normalized reduction (%); formula and zero handling defined consistently.
- **Repeated-run statistics:** comparison-level Wilcoxon/sign-test presentation; SciPy 1.17.1 call details recorded.

## Algorithm description corrections

- Randomness limited to score-weighted SCC selection; destroy prefixes deterministic under tie-breaking.
- Integer rounding of destroy fractions documented as an implementation detail.
- Residual-weight notation corrected in formal analysis; Proposition 3 relabeled as incumbent non-worsening invariant.
- DRMacIver/FAS baseline described algorithmically from source inspection.

## Scope and disclosure

- Dense LOLIB claims narrowed to single-run transfer evidence.
- Data/code availability includes GitHub URL, commit, OR1 location, and benchmark sources.
- AI-use disclosure refined to separate authoring responsibility from tool assistance.
- Reference 23 (CCP24) article-number formatting corrected.

## Online Resource 1

Synchronized for all metric, table, parameter, preprocessing, statistical, and bibliography changes above.
