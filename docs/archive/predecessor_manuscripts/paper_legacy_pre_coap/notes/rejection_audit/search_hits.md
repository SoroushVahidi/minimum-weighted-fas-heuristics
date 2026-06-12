# Rejection-Audit Search Hits

This file records the highest-signal local hits used in the rejection audit. It is intentionally curated; the raw broad grep was much noisier than the useful evidence.

## `docs/manuscript_results_and_claims_20260606.md`

- L261: `Reviewer notes local-ratio is prior art (Bar-Yehuda et al.)`
- L262: `Reviewer asks for approximation ratio or formal bound`
- L263: `Reviewer requests GNNRank or more recent learning-based methods`
- L264: `Reviewer points to EXP5 where DRMaciver beats IPSNS`
- L265: `Reviewer asks for synthetic or larger-scale instances`
- L266: `Reviewer cannot verify code`
- L267: `WMSF is a reimplementation of paper049`

## `docs/venue_decision_notes_20260606.md`

- L47: `Feedback has been on experimental completeness and framing, not theoretical novelty.`
- L61: `Reviewer expectations align with the current experimental portfolio (5 experiments, clean baselines).`
- L62: `Lower risk of "insufficient novelty" rejection given focus on computational methodology.`
- L64: `The LOLIB transfer test (EXP5) broadens scope without requiring deep theory.`

## `docs/paper_status_20260606.md`

- L51: `The add-back phase is the novel contribution (prior work: local-ratio framework).`
- L57: `Do not claim local-ratio as a novel contribution — it is prior art.`
- L58: `Do not claim a new approximation ratio — IPSNS has no ratio guarantee.`
- L59: `Do not claim exact optimality in general — only near-optimality on small instances (EXP3).`
- L64-L67: standard claims apply only to non-negative-weight instances; negative-weight instances are excluded.

## `docs/baselines_and_datasets_references.md`

- L161: `Key parameter | --wmsf-seed-mode full (required for incumbent protection)`
- L166-L168: IPSNS guarantee is enforced algorithmically by initializing from the better seed and accepting only strict improvements.

## `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`

- L591-L607: predecessor JOCO manuscript summarized itself as a heuristic paper centered on empirical quality/runtime tradeoff.
- L612-L618: predecessor JOCO limitations state that the benchmark coverage did not include broader structural families such as dense graphs and application-specific networks.

## `paper/sections/02_related_work.tex`

- Current draft already states that local-ratio is inherited, not newly invented here.
- Current draft already frames the paper as an integrated computational heuristic study rather than a new approximation-theory result.

## `paper/sections/04_algorithmic_framework.tex`

- Current draft already states the monotone non-degradation invariant for IPSNS.
- Current draft does not yet explicitly discuss non-uniqueness of extracted topological orders; this remains a writing action item rather than an experimental gap.
