# Anonymous Artifact Plan

Recommended artifact name: `mwfas_reproducibility_artifact_anonymous.zip`

## Include

- Source code needed to reproduce manuscript results
- Experiment scripts and configuration files
- Selected benchmark instance lists
- Conversion utilities for benchmark preparation
- Postprocessed summaries and compact manuscript tables
- Environment file or dependency manifest
- Anonymous README with run instructions and artifact map

## Exclude

- `.git`
- Author names and affiliations
- GitHub usernames and identifying repository URLs
- NJIT references
- Predecessor ZIP archives
- Logs, caches, and huge raw outputs
- Downloaded third-party archives
- Local absolute paths
- Acknowledgements and reviewer-facing metadata

## Distribution notes

- Public benchmark datasets should be linked and cited rather than redistributed unless the license clearly permits redistribution.
- The anonymized artifact should contain enough metadata and scripts to fetch or reconstruct benchmark inputs.
- After acceptance, release the public repository and archive a DOI-backed snapshot.
