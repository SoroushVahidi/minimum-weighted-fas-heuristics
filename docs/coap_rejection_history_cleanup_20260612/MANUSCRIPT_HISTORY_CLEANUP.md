# Manuscript History Cleanup

**Date:** 2026-06-12  
**Files changed:** `paper_coap/sections/02_related_work.tex`, `paper_coap/declarations/statements_and_declarations.tex`

---

## What was removed

### `sections/02_related_work.tex` — §2 prior-work subsection

**Removed from LR-TA paragraph:**
```
(submitted to the Journal of Combinatorial Optimization as JOCO-D-26-00099; rejected)
```
The paragraph now reads: `An earlier author manuscript, ``Fast Local-Ratio Cycle Reduction...''` — the scientific description of the predecessor is fully retained; only the venue name, manuscript ID, and rejection outcome were removed.

**Removed from IPSNS predecessor paragraph:**
```
(submitted to Discrete Applied Mathematics as DA19469; rejected)
```
Same treatment: scientific description retained, editorial history removed.

**Removed entire CAIE/EJCO paragraph:**
```
Related manuscripts were also submitted to Computers & Industrial Engineering and the 
EURO Journal on Computational Optimization; both were rejected and are no longer under 
consideration. Those manuscripts share much of the merged experimental narrative now 
retargeted to COAP, but predate the consolidated formal-analysis section, the holdout 
study, and the completed stochastic-robustness study (EXP10).
```
This paragraph mentioned venues and rejection outcomes only. The scientific content it contained (what those manuscripts predate) is already covered by the contribution-increment list that follows the predecessor paragraphs.

### `declarations/statements_and_declarations.tex` — Related manuscripts subsection

**Replaced:**
```
JOCO-D-26-00099 (Journal of Combinatorial Optimization; rejected), DA19469 (Discrete 
Applied Mathematics; rejected), a related submission to Computers & Industrial 
Engineering (rejected), and a related submission to the EURO Journal on Computational 
Optimization (rejected). None of these prior submissions is currently under consideration.
```

**With:**
```
the unpublished predecessor manuscripts that share the LR-TA, WMSF, and IPSNS components 
with the present study. No substantially overlapping manuscript is currently under 
consideration elsewhere.
```

This declaration is reviewer-visible. The revised wording conveys the same essential fact (there are predecessor manuscripts, none is active) without listing venues, IDs, or rejection outcomes.

---

## What was retained

- Citation to arXiv:2412.16181 and full description of its content (§2 paragraph 1)
- Statement that LR-TA code matches the predecessor at the code level
- Statement that IPSNS core is preserved from the predecessor manuscript
- All scientific distinctions between inherited and new components
- Full contribution-increment list (§2 final paragraph of the prior-work subsection)
- All other §2 content (algorithmic foundations, heuristics, exact methods, dense ordering)
- All algorithmic uses of "rejected" (IPSNS move rejection in §4, wrapper behavior in §6)

---

## Scientific attribution check

| Attribution | Still present? |
|---|---|
| arXiv:2412.16181 preprint | YES — paragraph 1 of §2.1 |
| LR-TA lineage (Demetrescu–Finocchi) | YES — §2.2 |
| WMSF attribution (Cavallaro–Cutello) | YES — §2.3 |
| LR-TA predecessor manuscript description | YES — paragraph 2 of §2.1 |
| IPSNS predecessor manuscript description | YES — paragraph 3 of §2.1 |
| IPSNS novelty positioning | YES — §2.4 and contribution list |
| New components listed | YES — (i)–(vi) in §2.1 |
