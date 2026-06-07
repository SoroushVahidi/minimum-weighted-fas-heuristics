# Anonymous Artifact Plan

Recommended artifact name: `mwfas_caie_anonymous_reproducibility_artifact_v1.zip`

## Purpose

This artifact is intended for double-anonymized review support. It should let a reviewer inspect the implementation, reproduce the committed manuscript tables and figures from stored summaries, and understand how the public benchmark inputs are obtained and converted without exposing author identity.

## Source files to include

- `src/` implementation files needed to run LR-TA, WMSF-style seeding, IPSNS, and the exact small-instance solver
- `scripts/` files required to run manuscript-facing workflows and benchmark conversions
- `paper/scripts/build_paper_results_assets.py`
- `paper/scripts/audit_manuscript_text.py`
- environment/dependency manifests needed to recreate the runtime
- anonymous top-level `README.md` with setup, run order, and artifact map
- an artifact manifest listing included files and their roles

## Result summaries to include

- committed processed summaries used for EXP1b--EXP5 manuscript assets
- postprocessed tables used by the paper
- figure-generation inputs used by the manuscript plots
- provenance notes that map each paper table and figure to its summary source
- any compact validation logs needed to show that manuscript values came from committed summaries rather than reruns

## Public dataset links to cite

- graph-benchmarks collection cited in the manuscript for sparse DIMACS-style directed instances
- LOLIB / Linear Ordering Problem Library sources cited in the manuscript for dense ordering instances
- any public documentation pages needed for third-party benchmark provenance

The artifact should prefer download instructions and checksums over redistributing third-party benchmark bundles unless redistribution rights are clear.

## Files to exclude

- `.git/`
- manuscript PDFs and TeX auxiliary files
- raw `results/` trees and large intermediate logs
- local caches, virtual environments, `__pycache__`, and `.pyc` files
- predecessor archive extracts and downloaded ZIP files
- author names, affiliations, emails, usernames, ORCID identifiers, and personal URLs
- GitHub repository URLs or metadata that reveal the maintainer identity
- acknowledgments and acceptance-stage release notes

## Anonymization checks

- scan all included text files for author names, affiliation names, usernames, emails, and known repository URLs
- scan scripts for absolute paths such as `/home/...`
- confirm that README text uses anonymous phrasing such as ``anonymous artifact'' and does not mention institutional infrastructure
- confirm that generated provenance files do not embed local machine paths
- verify that `main_anonymized.tex` and shared manuscript sources remain identity-clean

## Expected artifact structure

- `README.md`
- `MANIFEST.md`
- `environment/`
- `src/`
- `scripts/`
- `paper_assets/`
- `summaries/`
- `provenance/`
- `dataset_instructions/`

## Data and Code Availability wording

Anonymous review version:

`An anonymized reproducibility artifact containing the implementation, benchmark-preparation utilities, processed summaries, and manuscript-support files is provided as supplementary material for review. Public benchmark instances are available from the cited sources.`

Post-acceptance public version:

`The code, processed result summaries, and manuscript-support files will be released in a public versioned repository and archival package upon acceptance. Public benchmark instances remain available from the cited sources.`

## Release checklist for the later artifact pass

- freeze the exact source snapshot used for submission
- export only the committed manuscript-support summaries, not raw exploratory outputs
- regenerate manuscript tables and figures from included summaries
- rerun the anonymity scan on the artifact tree
- verify that the artifact README reproduces the paper assets without requiring hidden files
- create checksum list for all included summaries and figures
