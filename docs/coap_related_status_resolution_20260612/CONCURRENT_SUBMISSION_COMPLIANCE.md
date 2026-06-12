# Concurrent Submission Compliance Analysis

**Date:** 2026-06-12  
**Standard applied:** Springer Nature / COAP publication-ethics policy on concurrent submission  
**Evidence standard:** See EVIDENCE_METHOD.md

---

## Overlap component analysis

### Against JOCO-D-26-00099 (LR-TA manuscript)

| Component | Overlap classification | Notes |
|---|---|---|
| Problem formulation | SUBSTANTIAL | Both address MWFAS on directed graphs |
| LR-TA algorithm | SUBSTANTIAL | Same lrta.py implementation |
| WMSF | NONE | Not in JOCO predecessor |
| IPSNS | NONE | Not in JOCO predecessor |
| Formal proofs | NONE | Props 1–4 not in predecessor |
| Dataset (33 instances) | LIMITED_BACKGROUND | Predecessor 33-instance subset is a strict subset of current 105; results recomputed |
| Experiment tables | LIMITED_BACKGROUND | Predecessor EXP values superseded by EXP1b |
| Figures | NONE | Framework figure new for COAP |
| Code | SUBSTANTIAL | lrta.py code shared |
| Textual overlap | MODERATE_EXTENSION | LR-TA description paragraphs partially reused |
| Conclusions | MODERATE_EXTENSION | LR-TA conclusions are a subset of COAP conclusions |

**Overall JOCO overlap: SUBSTANTIAL** (LR-TA algorithm and code are directly reused; but IPSNS, formal analysis, and 80%+ of experiments are new).

### Against DA19469 (IPSNS/DAM manuscript)

| Component | Overlap classification | Notes |
|---|---|---|
| Problem formulation | SUBSTANTIAL | Both address MWFAS |
| LR-TA algorithm | LIMITED_BACKGROUND | Not primary in DAM; LR-TA appears as background only |
| WMSF seed | SUBSTANTIAL | Same wmsf.py |
| IPSNS | SUBSTANTIAL | Same ipsns.py — primary current contribution |
| Formal proofs | NONE | Props 1–4 not in predecessor |
| Dataset | MODERATE_EXTENSION | DAM had 33 instances; COAP has 105 + external baselines |
| Experiment tables | MODERATE_EXTENSION | Some IPSNS vs WMSF rows overlap; all results recomputed |
| Figures | NONE | Framework figure new for COAP |
| Code | SUBSTANTIAL | ipsns.py and wmsf.py shared |
| Textual overlap | SUBSTANTIAL | IPSNS description paragraphs partially reused |
| Conclusions | MODERATE_EXTENSION | IPSNS non-degradation guarantee is shared |

**Overall DAM overlap: SUBSTANTIAL** (IPSNS algorithm, code, and core narrative are directly shared; this is the higher-risk item because IPSNS is the primary current contribution).

---

## Per-item concurrent-submission risk assessment

### arXiv:2412.16181

| Question | Answer |
|---|---|
| Is it active? | NOT APPLICABLE — public preprint, not a journal submission |
| Is overlap substantial? | LIMITED_BACKGROUND (ranking formulation differs from sparse-digraph framing) |
| Is editor disclosure sufficient? | YES — already disclosed in cover letter, §2, statement |
| Is withdrawal required? | NO — preprints are not journal submissions |
| Is explicit permission required? | NO |
| Must the preprint PDF be uploaded? | NO — already cited in bibliography; preprint upload is not required |
| May COAP submission proceed now? | YES — arXiv creates no barrier |

### JOCO-D-26-00099

| Question | Answer |
|---|---|
| Is it active? | STATUS_UNVERIFIED — inferred inactive from internal notes; not confirmed by decision letter |
| Is overlap substantial? | YES — LR-TA component is substantially shared |
| Is editor disclosure sufficient? | YES IF INACTIVE — JOCO predecessor is disclosed in cover letter and §2; if inactive, disclosure is complete |
| Is withdrawal required? | YES IF ACTIVE — active simultaneous submission of a substantially overlapping manuscript is not permitted under Springer Nature policy |
| Is explicit permission required? | YES IF ACTIVE (edge case B) — if JOCO is still under review but overlap is primarily LR-TA while COAP primary contribution is IPSNS, author would need to consult both journal editors about concurrent submission of a partially overlapping work |
| Must the JOCO manuscript PDF be uploaded? | The related-manuscript statement describes the overlap; no separate JOCO PDF upload is required by standard Springer portal practice |
| May COAP submission proceed now? | CONDITIONAL — yes if JOCO is confirmed inactive; no if JOCO is still under active peer review without editor permission |

### DA19469

| Question | Answer |
|---|---|
| Is it active? | STATUS_UNVERIFIED — inferred inactive from internal notes; not confirmed by decision letter |
| Is overlap substantial? | YES — IPSNS (primary COAP contribution) is substantially shared; this is the highest-risk item |
| Is editor disclosure sufficient? | YES IF INACTIVE — DAM predecessor is disclosed; if inactive, disclosure is complete |
| Is withdrawal required? | YES IF ACTIVE — active simultaneous submission of IPSNS to both COAP and DAM is a direct concurrent-submission policy violation |
| Is explicit permission required? | YES IF ACTIVE — active DAM would require written permission from both editors or withdrawal |
| Must the DAM manuscript PDF be uploaded? | No separate PDF required; disclosure statement describes the overlap |
| May COAP submission proceed now? | CONDITIONAL — yes if DAM is confirmed inactive; no if DAM is active (highest-priority confirmation) |

### CAIE

| Question | Answer |
|---|---|
| Is it active? | STATUS_UNVERIFIED — git evidence strongly suggests inactive (revision cycle completed; pivot to EJCO then COAP); not confirmed by decision or withdrawal letter |
| Is overlap substantial? | MODERATE_EXTENSION — CAIE merged experimental narrative shares core algorithms; COAP adds formal analysis and additional experiments |
| Is editor disclosure sufficient? | YES IF CONFIRMED INACTIVE — current disclosure uses "package prepared" qualifier; if CAIE was submitted and is inactive, statement should reflect actual submission history |
| Is withdrawal required? | IF ACTIVE AND SUBSTANTIALLY OVERLAPPING — yes; but inference suggests inactive |
| Is explicit permission required? | NOT LIKELY — even if CAIE was submitted and rejected, no permission needed; if still active, yes |
| Must the CAIE manuscript be uploaded? | No standard requirement; disclosure statement is sufficient |
| May COAP submission proceed now? | CONDITIONAL — requires author to confirm CAIE is inactive |

### EJCO

| Question | Answer |
|---|---|
| Is it active? | STATUS_UNVERIFIED — likely not formally submitted (no ID); package archived; inference of inactive |
| Is overlap substantial? | SUBSTANTIAL (near-identical pre-holdout core) if formally submitted |
| Is editor disclosure sufficient? | YES IF ONLY PACKAGE PREPARED — current "package prepared" language is accurate if EJCO was never formally submitted |
| Is withdrawal required? | IF FORMALLY SUBMITTED AND ACTIVE — yes; but formal submission is unconfirmed |
| Must EJCO manuscript be uploaded? | No — related-manuscript statement qualifies status appropriately |
| May COAP submission proceed now? | CONDITIONAL — requires author to confirm EJCO was not formally submitted, or if submitted that it is inactive |

---

## Bottom-line concurrent-submission risk assessment

The current cover-letter declaration "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission" is:

**CONSISTENT with repository evidence** — internal notes infer JOCO and DAM were rejected; git timeline strongly suggests CAIE became inactive before EJCO was prepared; EJCO formal submission is unconfirmed.

**NOT FORMALLY VERIFIABLE from available evidence** — no rank 1–6 documentary evidence is present in this audit.

**The author, having written this declaration, presumably has the knowledge to confirm it is accurate.** The declaration is not contradicted by any available evidence. It is blocked only by the absence of documentary confirmation in this audit pass.

---

## Publication-ethics summary

This is not a legal assessment. From a publication-ethics standpoint:

1. All five related items are disclosed — this is the primary ethics obligation.
2. The COAP manuscript is a substantive extension that adds new contributions (IPSNS-unified framework, formal analysis, expanded experiments, OR1) beyond any individual predecessor.
3. The concurrent-submission declaration in the cover letter is the author's personal attestation. The author must be able to stand behind it at submission time.
4. If JOCO and DAM were rejected and CAIE/EJCO are inactive, the submission is ethically clear.
5. If any one of JOCO, DAM, or CAIE is currently under active peer review and has substantial overlap with COAP, that item must be resolved (withdrawn or disclosed with editor permission) before COAP submission.
