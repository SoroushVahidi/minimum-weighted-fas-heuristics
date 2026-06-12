# Current Framing Risk Audit

**Audit date:** 2026-06-11  
**Files inspected:** `paper_coap/main.tex`, `sections/01–08`, contribution list, abstract, related work.

Do **not** rewrite in this audit — recommended changes only.

---

## Title

**Current:** “Local-Ratio Seeding and SCC-Based Refinement for the Minimum Weighted Feedback Arc Set Problem”

| Check | Result |
|-------|--------|
| Overemphasizes LR-TA? | **Mild risk** — “Local-Ratio Seeding” leads; IPSNS not in title |
| Implies WMSF new? | No |
| Hype words? | No |
| Scope accurate? | Yes — MWFAS explicit |

**Recommended change (optional):** Consider “Incumbent-Protected SCC Refinement for the Minimum Weighted Feedback Arc Set Problem: Local-Ratio Seeding and Engineered Baselines” — IPSNS-forward while keeping LR-TA. **Not mandatory** if contribution list and abstract are fixed.

---

## Abstract (~220 words)

| Check | Result |
|-------|--------|
| IPSNS understated? | No — IPSNS defined with monotonicity guarantee |
| LR-TA overemphasized? | Balanced — three components listed |
| “Novel/first/SOTA”? | **None** — safe |
| Dense limitation? | **Yes** — explicit |
| Predecessor disclosure? | **Absent** — cover letter/§2 must carry this |
| Reproducibility claim? | “Fully reproducible artifact” — **risk if OR1 absent at submission** |

**Recommended changes:**
1. Add clause: “DRMacIver comparisons use repeated runs where noted (EXP10)” after EXP10 completes.
2. Soften to “reproducibility package” until OR1 + tests exist, OR complete OR1 before submission.

---

## Introduction and contribution list

### Safe language already present

- L8: “We do not claim local-ratio as new.”
- L10: IPSNS incumbent protection; not approximation guarantee.
- L14–17: Bounded sparse claims; LOLIB as scope boundary.

### Framing risks

| Issue | Location | Severity |
|-------|----------|----------|
| Contribution bullet 1 is LR-TA not IPSNS | §1 L20 | Moderate |
| Bullet 2 WMSF without “CC25-derived seed” | §1 L21 | Low |
| No author predecessor sentence | §1 entire | **High (disclosure)** |
| “best observed backward weight among all tested methods” | abstract L46 | Low — scoped to tested methods |

**Recommended changes:**

1. **Insert after L17 (before contributions):** One paragraph disclosing that LR-TA and IPSNS appeared in prior author manuscripts and arXiv:2412.16181 treats related ranking-as-MWFAS work; state COAP’s new elements (unification, Props 1–4, expanded experiments, EXP10, holdout).

2. **Reorder contribution bullets:**
   - First: IPSNS (main new algorithmic contribution; formal Props 3–4 new).
   - Second: Unified framework + reproducible artifact.
   - Third: LR-TA as engineered seed (prior JOCO manuscript).
   - Fourth: WMSF as CC25-derived seed (not novel).
   - Fifth–seventh: Formal analysis, complexity, experimental program.

3. **Replace any “first unified treatment”** only after predecessor disclosure paragraph — otherwise triggers desk review.

---

## Related work (§2)

| Check | Result |
|-------|--------|
| DF03/BYGR98 attribution | Correct |
| CC25 WMSF | Correct |
| GNNRank excluded | Correct with rationale |
| arXiv:2412.16181 | **Missing — mandatory add** |
| JOCO/DAM predecessors | **Missing — mandatory add** |
| “state of the art” for calibration baselines | L20: “not intended to represent state of the art” — **good** |

**Recommended changes:**
- New subsection: “Author predecessor work” citing arXiv:2412.16181, JOCO LR-TA manuscript, DAM IPSNS manuscript (as unpublished/previously submitted), with bullet list of COAP additions.

---

## Algorithmic framework (§4)

| Phrase | Risk |
|--------|------|
| “LR-TA is the first constructive component” | Low — ordering not novelty claim |
| “IPSNS is the main refinement contribution” | **Good** |
| Missing topological non-uniqueness | Moderate |

**Recommended change:** Add paragraph after topological order definition: linear extensions of a DAG are not unique; paper uses one deterministic extraction rule; backward weight depends on chosen extension; engineering choice not optimality claim.

---

## Experimental design and results (§5–§6)

| Issue | Status |
|-------|--------|
| DRMacIver single-run undisclosed | **High — add sentence** |
| “best observed” language | Acceptable with “tested methods” |
| EXP5 transparent | Good |
| Statistical tests | Present in paired table |

**Recommended §5 addition:**
> “DRMacIver/FAS initializes its random seed from the system clock and process identifier; EXP4 records one run per instance. Experiment EXP10 repeats DRMacIver and IPSNS with controlled seeds to assess robustness of paired comparisons.”

---

## Discussion and conclusion

| Check | Result |
|-------|--------|
| Repeats LR-TA-as-main-story? | No — emphasizes IPSNS safety + sparse regime |
| Overbroad conclusions? | Bounded — “within stated boundaries” |
| Predecessor omission? | Yes — add one sentence on unified extension |

---

## Prohibited phrases for final pass

Do not introduce:
- “novel local-ratio algorithm”
- “first approximation algorithm for MWFAS”
- “state of the art on all benchmarks”
- “globally optimal” (except EXP3/EXP8 certified subsets)
- “not published previously” (cover letter — false)

---

## Repeated previously criticized framing?

| Prior criticism | Still present? |
|-----------------|----------------|
| Local-ratio as novelty | **No** in prose |
| Universal SOTA | **No** |
| Hidden LOLIB weakness | **No** |
| WMSF as contribution | **No** |
| LR-TA leading narrative | **Partially** (title + bullet order) |
| Missing predecessor disclosure | **Yes** |
