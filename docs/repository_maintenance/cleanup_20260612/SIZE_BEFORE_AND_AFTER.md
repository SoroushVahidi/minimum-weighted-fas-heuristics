# Size Before and After

| Metric | Before (6c04ff1) | After first pass (3b51476) | After second pass (04ba2c3) |
|---|---|---|---|
| Tracked files (`git ls-files`) | 6336 | 6410 | 6418 |
| Working tree size | ~333 MB | ~213 MB | ~213 MB |
| Top-level `submission_package/` | present | removed (archived) | removed |
| Top-level `paper/` | present | removed (archived) | removed |

First pass removed large legacy binary PDFs and ZIPs from active branch, reducing tree size.
Second pass added 8 experiment READMEs and 3 maintenance docs (+8 tracked files).

Large ignored trees (EXP10 raw, checkpoints) unchanged by policy. No aggressive checkpoint deletion.
