# Datasets

## graph-benchmarks sparse directed instances

- Public source: https://github.com/alidasdan/graph-benchmarks
- Redistribution in this artifact: no
- Access mode: download separately from the public source
- Selected subset: manuscript benchmark instance lists in `experiments/*/configs/`
- Conversion note: instances are used in DIMACS directed-arc format
- Scope note: standard paper claims use the nonnegative-weight subset only
- Negative-weight exclusions: `gerez`, `howard-max`, `k3_3`, `ku`, `peterson`, `peterson1`, `peterson2`, `stg0`

## LOLIB dense ordering instances

- Public source: https://grafo.etsii.urjc.es/optsicom/lolib.html
- Redistribution in this artifact: no original archive; only the small committed smoke-test `.lop` file is included
- Access mode: download from the cited public source, then convert with `scripts/convert_lolib_to_dimacs.py`
- Selected subset: SGB, IO, and RandA1 families listed in `experiments/exp5_lolib_dense/configs/exp5_lolib_instances.txt`
- Conversion note: the manuscript uses converted DIMACS digraphs derived from dense ordering matrices
- Scope note: LOLIB is used as a dense transfer test, not the primary sparse benchmark
