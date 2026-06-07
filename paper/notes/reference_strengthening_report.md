# Reference Strengthening Report

Pre-CAIE pass to increase curated bibliography coverage from 11 to 23 unique cited keys.

## Starting point

- **Unique keys cited:** 11
- **Total citation commands:** 29
- **Bib entries:** 13

## Added references (verified from predecessor `.bib` files and existing audit notes)

| Key | Source | Topic | Integrated in | Decision |
|---|---|---|---|---|
| `K72` | Karp (1972), DOI verified | NP-hardness foundation | Introduction, Problem definition, Related work | add |
| `F90` | Flood (1990), DOI verified | Early weighted FAS literature | Introduction, Related work, Problem definition | add |
| `ENSS98` | Even et al. (1998), DOI verified | Directed feedback approximation | Related work | add |
| `ACN08` | Ailon et al. (2008), DOI verified | Rank aggregation from inconsistent pairwise data | Introduction, Related work | add |
| `CFR10` | Coppersmith et al. (2010), DOI verified | Win-based tournament ranking / Borda context | Related work, Experimental design | add |
| `HGH21` | Hecht et al. (2021), DOI verified | Feedback-set localization | Related work | add |
| `ALS09` | Alon et al. (2009), Springer proceedings | Fast tournament FAS approximation | Related work | add |
| `FLRS10` | Fomin et al. (2010), DOI verified | Weighted tournament FAS local search | Related work, Results, Discussion | add |
| `CC25` | Cavallaro & Cutello (2025), DOI verified | Minimal/stable weighted FAS heuristic | Related work, Experimental design | add |
| `OZ24` | Ostovari & Zarei (2024), DOI verified | Recent tournament FAS approximation | Results, Discussion | add |
| `anonymous_artifact_2026` | Local placeholder | Anonymized reproducibility artifact | Data availability (anonymized) | add |
| `lop_ma_edm_repo` | Existing repo entry | Excluded LOP memetic baseline | Experimental design | add |

## Rejected candidates

| Candidate | Reason |
|---|---|
| `V25`, `V25-2` | Author-identifying arXiv preprints; incompatible with double-anonymized review |
| `GNYZ25` | Not already used in manuscript notes; omitted to avoid unverified expansion |
| `Pavone` standalone entry | No verified standalone bibliographic entry beyond `CC25` in local files |
| Additional scatter-search LOLIB references | `MRD12` and `lolib_library` already cover LOLIB provenance sufficiently |

## Ending point (post-integration target)

- **Unique keys cited:** 23
- **Bib entries:** 24
- **Unused bib keys:** none expected after integration

## Integration summary

- **Introduction:** `ACN08`, `K72`, `F90`, `BSNA21`
- **Related work:** `F90`, `K72`, `ENSS98`, `HGH21`, `CFR10`, `CC25`, `FLRS10`, `ALS09`, `ACN08`, `CFR10`, expanded positioning cites
- **Problem definition:** `F90`, `K72`
- **Experimental design:** `CFR10`, `GNNRank22`, `lop_ma_edm_repo`, `CC25`
- **Results / Discussion:** `FLRS10`, `OZ24`
- **Data availability (anonymized):** `anonymous_artifact_2026`

## Citation discipline

- No sentence ends with more than four keys.
- New cites support specific statements rather than decorative padding.
- Manuscript scientific claims unchanged.
