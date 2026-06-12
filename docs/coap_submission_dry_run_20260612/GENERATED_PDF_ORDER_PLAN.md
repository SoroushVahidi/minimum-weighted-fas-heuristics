# Generated PDF Order Plan

**Date:** 2026-06-12  
**Purpose:** Specify how Editorial Manager assembles the review PDF and document the expected page order so the author can verify the generated proof before approving.

---

## How Editorial Manager assembles the review PDF

Editorial Manager concatenates uploaded files in the order the author specifies or in a default order based on designation. The typical assembly for a Springer COAP submission is:

1. **Manuscript** — the primary PDF (all pages)
2. **Supplementary Information / ESM** — appended after main manuscript (in upload order if multiple)
3. **Cover letter** — typically excluded from the reviewer PDF (editor-only designation)
4. **LaTeX source** — excluded from the reviewer PDF (production use only)

The reviewer PDF is generated from designations 1 and 4 in the table below.

---

## Planned page order in reviewer-visible generated PDF

| Position | File | Designation | Pages (approx.) | Notes |
|---|---|---|---|---|
| 1 | Vahidi_COAP_Manuscript.pdf | Manuscript | ~45 pp | Title page, abstract, body, references, declarations |
| 2 | Vahidi_Online_Resource_1_MWFAS.pdf | Supplementary Information | ~60–80 pp | OR1 supplement; may appear as ESM_1 in generated PDF |
| 3 | Vahidi_Online_Resource_1_MWFAS.zip | Supplementary Material | (not rendered as pages — download link) | ZIP is linked separately, not concatenated into PDF |

**Cover letter and source ZIP are editor-only and must NOT appear in the reviewer PDF.**

---

## Required verification steps before approving the generated PDF

When the portal displays the generated review PDF, verify ALL of the following:

| Check | Expected result | Action if wrong |
|---|---|---|
| First page is manuscript title page | Title: "SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs"; Author: Soroush Vahidi; Affiliation: NJIT | Reject and re-upload correct manuscript |
| Abstract on title page | 238-word abstract present and complete | Reject and fix |
| No cover letter pages in reviewer PDF | Cover letter content absent from any position | Change cover letter designation to "Cover Letter" (editor-only) |
| Supplementary section present | OR1 PDF appended or linked after manuscript | Verify supplementary upload designation |
| No garbled pages | No encoding artifacts, missing fonts, or OCR failure | Rebuild PDF and re-upload |
| Page count plausible | Manuscript ~45 pp + supplement ~60–80 pp | Flag discrepancy |
| All sections present | Introduction through Declarations sections all appear | Re-upload if truncated |
| Figures render correctly | All figures appear (framework_overview, exp6, exp10 figures) | Re-upload |
| References are complete | Reference list appears at end of manuscript section | Verify |

---

## If the generated PDF fails verification

1. Click "Edit Submission" (do not approve).
2. Identify which file caused the issue (manuscript PDF vs. OR1 PDF vs. upload order).
3. Re-upload the correct file and re-generate the proof.
4. Repeat verification before approving.

**Do not click "Approve PDF" unless all checks above pass.**

---

## Upload order recommendation

Upload in this sequence to control the assembly order:

1. `Vahidi_COAP_Manuscript.pdf` (Manuscript)
2. `Vahidi_COAP_Cover_Letter.pdf` (Cover Letter — editor-only)
3. `Vahidi_COAP_Manuscript_Source.zip` (LaTeX Source)
4. `Vahidi_Online_Resource_1_MWFAS.pdf` (Supplementary Information)
5. `Vahidi_Online_Resource_1_MWFAS.zip` (Supplementary Material)
6. `Vahidi_Related_Manuscripts_Statement.pdf` (Cover Letter / Author Statement — editor-only)
