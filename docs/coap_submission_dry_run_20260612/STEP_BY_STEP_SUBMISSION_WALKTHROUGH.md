# Step-by-Step COAP Submission Walkthrough

**Date:** 2026-06-12  
**Journal:** Computational Optimization and Applications (COAP), Springer  
**Portal:** https://www.editorialmanager.com/coap  
**Author:** Soroush Vahidi (sv96@njit.edu)

---

## Before You Begin

Complete all items in this pre-flight checklist before opening the portal:

- [ ] Confirm JOCO-D-26-00099 status (withdrawn / rejected / still under review?) — **BLOCKER**
- [ ] Confirm DA19469 status (withdrawn / rejected / still under review?) — **BLOCKER**
- [ ] If either is still under review: amend `Vahidi_COAP_Cover_Letter.pdf` before proceeding
- [ ] Verify all 6 upload files are physically present in `paper_coap/submission/final_upload/`
- [ ] Verify SHA-256 checksums match (see `UPLOAD_FILE_REGISTER.csv`)
- [ ] Close other journal tabs to avoid accidental cross-submission
- [ ] Prepare the ORCID: `0000-0003-1934-6282`
- [ ] Open `EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md` in a separate window for copy-paste

---

## Phase 1 — Portal Login and Account Setup

**Step 1.** Navigate to https://www.editorialmanager.com/coap

**Step 2.** Log in with your existing account, or create a new account if this is your first submission to COAP.
- Email: sv96@njit.edu
- If prompted for ORCID during registration: `0000-0003-1934-6282`

**Step 3.** On the author dashboard, click **"Submit New Manuscript"** (exact label may differ: "New Submission", "Submit a Paper", "Author Login → Submit New Manuscript").

---

## Phase 2 — Article Type and Basic Information

**Step 4.** Select article type.
- Choose: **"Original Research Article"** or the closest equivalent ("Full Length Paper", "Research Article")
- Do NOT choose: review articles, notes, corrections, letters

**Step 5.** Enter the title.
- **Paste exactly:** `SCC-Local Destroy-and-Repair Heuristics for Minimum Weighted Feedback Arc Set on Sparse Digraphs`
- If a running title field appears: `SCC-Local Heuristics for MWFAS on Sparse Digraphs`

**Step 6.** Enter the abstract.
- **Paste exactly** the 238-word abstract from `EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md`
- Do not include LaTeX commands (`\textit`, `\emph`, etc.)
- Plain text only

**Step 7.** Enter keywords.
- `Minimum weighted feedback arc set; Combinatorial optimization; Local-ratio algorithm; Strongly connected components; Heuristic search; Algorithm engineering`
- If the portal requires one keyword per field, enter each separately
- If it requires a comma separator, replace semicolons with commas

---

## Phase 3 — Author Information

**Step 8.** Enter author details.
- Given name: `Soroush`
- Family name: `Vahidi`
- Email: `sv96@njit.edu`
- Institution: `New Jersey Institute of Technology`
- Department: `Department of Computer Science`
- City: `Newark` | State/Province: `NJ` | Postal: `07102` | Country: `USA`
- ORCID: `0000-0003-1934-6282`
- Corresponding author: **Yes** (sole author)

---

## Phase 4 — Statements and Declarations

**Step 9.** Enter funding statement.
- `This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.`

**Step 10.** Enter competing interests.
- `The author declares that there are no known competing financial or non-financial interests that could have appeared to influence the work reported in this paper.`

**Step 11.** Enter author contributions (CRediT).
- `Soroush Vahidi: Conceptualization, Methodology, Software, Formal analysis, Investigation, Validation, Data curation, Visualization, Writing – original draft, Writing – review & editing.`

**Step 12.** Enter data availability.
- `Online Resource 1 (supplementary PDF and artifact archive) accompanies this submission. It contains code, configurations, summary outputs, and reproduction scripts. The public benchmark instances are cited in the manuscript and available at https://github.com/alidasdan/graph-benchmarks.`

**Step 13.** Enter code availability.
- `Included in Online Resource 1 (Vahidi_Online_Resource_1_MWFAS.zip).`

**Step 14.** Enter AI/Generative AI disclosure.
- `During the preparation of this work, the author used AI-assisted tools, including ChatGPT, Codex, Claude, and Perplexity AI, to support literature exploration, organization of material, language editing, and coding assistance. The author reviewed and edited all outputs, verified the relevant sources and experimental results, and takes full responsibility for the content of the submitted manuscript.`

**Step 15.** If a preprint/arXiv field appears:
- `arXiv:2412.16181 (December 2024) — Vahidi and Koutis. The COAP submission substantially extends and supersedes that preprint.`

**Step 16.** If a "Comments to the Editor" or related-manuscripts free-text field appears:
- `A public preprint (arXiv:2412.16181) and previously submitted author manuscripts (JOCO-D-26-00099; DA19469) are disclosed. Prepared CAIE/EJCO packages are described in the enclosed related-manuscript statement. This COAP submission integrates and extends those strands; IPSNS is the primary new integrated contribution.`

**Step 17.** If subject classifications (MSC codes) are requested:
- 90C27 (Combinatorial optimization)
- 68W25 (Approximation algorithms)
- 05C85 (Graph algorithms)

---

## Phase 5 — File Upload

Upload files in this order. All files are in `paper_coap/submission/final_upload/`.

**Step 18.** Upload `Vahidi_COAP_Manuscript.pdf`
- Designation: **Manuscript**
- This is the primary document

**Step 19.** Upload `Vahidi_COAP_Cover_Letter.pdf`
- Designation: **Cover Letter**
- Verify it is marked editor-only (should not appear in reviewer PDF)

**Step 20.** Upload `Vahidi_COAP_Manuscript_Source.zip`
- Designation: **LaTeX Source Files** (or "Source Files", "Supplementary Material — Source")
- Not reviewer-visible; for production use

**Step 21.** Upload `Vahidi_Online_Resource_1_MWFAS.pdf`
- Designation: **Supplementary Information** or **Electronic Supplementary Material**
- Reviewer-visible; this is Online Resource 1

**Step 22.** Upload `Vahidi_Online_Resource_1_MWFAS.zip`
- Designation: **Supplementary Material** or **Data/Code Archive**
- Reviewer-visible; this is the reproducibility artifact

**Step 23.** Upload `Vahidi_Related_Manuscripts_Statement.pdf`
- Designation: **Cover Letter** (secondary), **Other**, or **Author Statement**
- Verify editor-only visibility

---

## Phase 6 — Suggested Reviewers

**Step 24.** Enter suggested reviewers (see `SUGGESTED_REVIEWER_REGISTER.csv`).

| Name | Institution | Email |
|---|---|---|
| Kathrin Hanauer | University of Vienna | kathrin.hanauer@univie.ac.at |
| Petra Mutzel | University of Bonn | petra.mutzel@cs.uni-bonn.de |
| Giuseppe Lancia | University of Udine | giuseppe.lancia@uniud.it |
| Eduardo Uchoa | Universidade Federal Fluminense | eduardo_uchoa@id.uff.br |
| Ivana Ljubic | ESSEC Business School | ljubic@essec.edu |

**Step 25.** Opposed reviewers: enter any conflict-of-interest exclusions. If none, leave blank.

---

## Phase 7 — Generate and Verify Review PDF

**Step 26.** Click **"Build PDF"** or **"Generate PDF"**.

Wait for the portal to generate the review PDF (may take 1–3 minutes).

**Step 27.** Open and verify the generated PDF:

- [ ] First page: correct title, author, affiliation
- [ ] Abstract on title page: 238-word abstract present
- [ ] Cover letter is NOT included in the reviewer PDF
- [ ] Online Resource 1 PDF appears as supplementary section (or is linked)
- [ ] No garbled pages or encoding artifacts
- [ ] Page count is plausible (~45 pp manuscript)
- [ ] All sections present (Introduction through Declarations)
- [ ] All figures render correctly

**Step 28.** If the generated PDF is correct: click **"Approve PDF"**.  
If incorrect: click **"Edit Submission"**, fix the issue, and regenerate.

---

## Phase 8 — Final Review and Submit

**Step 29.** On the final review screen, verify:
- All required fields are complete (no error indicators)
- Files are all uploaded and designated correctly
- Author information is complete with ORCID
- Declarations are all filled

**Step 30.** Re-confirm the concurrent submission statement:
> "I confirm that no substantially overlapping manuscript by me is under consideration elsewhere at the time of submission."

**This statement must be true at the moment you click Submit.** If JOCO or DAM is still under active review, stop here and amend the cover letter first.

**Step 31.** Click **"Submit"** (or **"Submit Manuscript"**).

**Step 32.** Record:
- Submission date and time
- COAP manuscript number assigned by the portal
- Confirmation email received at sv96@njit.edu

---

## After Submission

- Monitor sv96@njit.edu for acknowledgment email (typically same day)
- The portal will send status updates: Under Editorial Review → Under Review → Decision
- Do not submit substantially overlapping work elsewhere while this is under review
- The repository and OR1 should remain private during peer review unless the editor requests otherwise
- Keep this walkthrough file with the submission record

---

## Files referenced in this walkthrough

| File | Location |
|---|---|
| Upload files | `paper_coap/submission/final_upload/` |
| Copy-ready text | `paper_coap/submission/EDITORIAL_MANAGER_FINAL_COPY_READY_TEXT.md` |
| Suggested reviewers | `docs/coap_submission_dry_run_20260612/SUGGESTED_REVIEWER_REGISTER.csv` |
| Author confirmations | `docs/coap_submission_dry_run_20260612/AUTHOR_CONFIRMATIONS_REQUIRED.md` |
| Issue register | `docs/coap_submission_dry_run_20260612/FINAL_PORTAL_ISSUE_REGISTER.csv` |
| File designations | `docs/coap_submission_dry_run_20260612/FILE_DESIGNATION_MAP.csv` |
| PDF order plan | `docs/coap_submission_dry_run_20260612/GENERATED_PDF_ORDER_PLAN.md` |
