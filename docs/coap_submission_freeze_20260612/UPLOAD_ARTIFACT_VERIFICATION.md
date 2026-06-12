# Upload Artifact Verification

**Date:** 2026-06-12  
**Directory:** `paper_coap/submission/final_upload/`  
**Verification method:** `sha256sum -c MANIFEST.sha256`

---

## SHA-256 verification result

```
sha256sum -c MANIFEST.sha256
Vahidi_COAP_Cover_Letter.pdf: OK
Vahidi_COAP_Manuscript.pdf: OK
Vahidi_COAP_Manuscript_Source.zip: OK
Vahidi_Online_Resource_1_MWFAS.pdf: OK
Vahidi_Online_Resource_1_MWFAS.zip: OK
Vahidi_Related_Manuscripts_Statement.pdf: OK
```

**Result: ALL 6 FILES VERIFIED — no byte-level changes since last confirmed build**

---

## File register

| Filename | SHA-256 | Size (bytes) | Designation | Reviewer-visible | Verified |
|---|---|---|---|---|---|
| Vahidi_COAP_Manuscript.pdf | 97eb61238a81e12e2597a6963926f0f092ad994f3f369b89715f36e9e06d0898 | 333,157 | Manuscript | YES | OK |
| Vahidi_COAP_Cover_Letter.pdf | df6622bd7b19f2ed73e5d54c38e953a2092f9436f574db4da86b374efe6496f8 | 24,732 | Cover Letter | NO (editor-only) | OK |
| Vahidi_COAP_Manuscript_Source.zip | 0fd2b2c138c31798ff334a47f7d5c917fd32ec83aa5b05b932c82c20a32f7b38 | 145,760 | LaTeX Source Files | NO (production) | OK |
| Vahidi_Online_Resource_1_MWFAS.pdf | 8cc1479fb7aebe9e8b4c219aada0bf87f6c0383f53345a2d851b776b581aa0ea | 130,236 | Supplementary Information | YES | OK |
| Vahidi_Online_Resource_1_MWFAS.zip | 5dc3875acad386f992266a43d1406b96787c95fa1d3acde7124be327ee29495e | 1,116,197 | Supplementary Material (Data/Code) | YES | OK |
| Vahidi_Related_Manuscripts_Statement.pdf | 7e5ee12c4200ff0a006f350b379d63a1dc38dccbc588ab7dbb62e241a08b519e | 22,804 | Cover Letter (Other) | NO (editor-only) | OK |

---

## Additional files in final_upload/

| Filename | Purpose | Upload to portal? |
|---|---|---|
| MANIFEST.sha256 | SHA-256 verification manifest for the 6 upload files | NO |
| README.txt | Human-readable notes about the upload bundle | NO |
| SUBMISSION_FREEZE.json | Machine-readable freeze manifest | NO |
| SUBMISSION_FREEZE.sha256 | SHA-256 of SUBMISSION_FREEZE.json | NO |

These 4 additional files are repository documentation. They must NOT be uploaded to Editorial Manager — only the 6 named PDFs/ZIPs above are upload files.

---

## No additional upload files

Confirmed: no unexpected PDF or ZIP was found in the directory. The upload bundle is exactly 6 files.

---

## No artifacts regenerated

All 6 upload files were verified byte-for-byte against the manifest. No file was regenerated, modified, or replaced during this freeze pass. The checksums match those originally recorded at submission preparation (commit 04ca3ad) and confirmed in the dry-run (2026-06-12).
