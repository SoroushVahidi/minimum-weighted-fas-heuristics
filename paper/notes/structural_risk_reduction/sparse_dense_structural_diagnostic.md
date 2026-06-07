# Sparse vs Dense Structural Diagnostic

## Sparse benchmark

- Instances: 95
- Mean n: 868.9, Mean m: 1521.8
- Mean density: 0.347740, Median density: 0.122222
- Mean largest-SCC fraction: 0.6437
- Mean fraction of vertices in nontrivial SCCs: 0.7796
- Mean number of nontrivial SCCs: 11.17
- Acyclic instances (no nontrivial SCCs): 4

## LOLIB dense benchmark

- Instances: 50
- Mean n: 93.9, Mean m: 5082.6
- Mean density: 0.454233, Median density: 0.450991
- Mean largest-SCC fraction: 0.9867
- Mean fraction of vertices in nontrivial SCCs: 0.9867
- Mean number of nontrivial SCCs: 1.00

## Interpretation

Sparse benchmark instances have low density (mean ~0.3477) and localized cyclic substructures (mean fraction of vertices in nontrivial SCCs: ~77.96%). LOLIB instances, by contrast, have near-complete density (mean ~0.4542) with essentially all vertices in one large SCC (mean fraction: ~98.67%). This structural contrast is consistent with the observed performance: SCC-local refinement (IPSNS) targets isolated cyclic subgraphs effectively on sparse instances, while matrix-based pairwise-ordering (DRMacIver/FAS) aligns naturally with fully dense complete-ordering instances.
