# COAP Reference Cleanup Report (Pass 2)

**Date:** 2026-06-10  
**Bibliography style:** `sn-mathphys-num.bst` via `\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}`

## Problem

The compiled PDF rendered `\blocation{???}` for three in-proceedings entries because `sn-mathphys-num.bst` requires a BibTeX `address` field for publisher location when a `publisher` field is present. The `.bib` entries listed publishers but omitted verified locations.

## Corrections

| Bib key | Entry type | Missing field | Correction | Evidence |
|---|---|---|---|---|
| `BH13` | `@inproceedings` | `address` | Added `address = {Berlin, Heidelberg}` | WALCOM 2013, LNCS 7748, Springer Berlin Heidelberg (publisher field already present; standard Springer LNCS location) |
| `ALS09` | `@inproceedings` | `address` | Added `address = {Berlin, Heidelberg}` | ICALP 2009, Springer LNCS; cross-checked via Springer chapter citation format and DBLP/BibSLEIGH metadata for ICALP 2009 |
| `LHK10WikiVote` | `@inproceedings` | `address` | Added `address = {New York, NY, USA}` | ACM proceedings metadata for DOI `10.1145/1772690.1772756` lists publisher location New York, NY, United States |

## Verification

After rebuild:

- `main.bbl` lines now contain `\blocation{Berlin, Heidelberg}` (BH13, ALS09) and `\blocation{New York, NY, USA}` (LHK10WikiVote).
- PDF text extract contains no `???`.
- All 26 cited references render with readable publisher locations.
- No citation keys unresolved; no `??` in-text markers.

## Fields intentionally not added

No volume, page, editor, or DOI fields were invented for these three entries beyond the verified `address` additions. Existing factual metadata in `references.bib` was otherwise preserved.
