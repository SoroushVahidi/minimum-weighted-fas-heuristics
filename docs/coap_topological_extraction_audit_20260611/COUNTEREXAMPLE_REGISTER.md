# Counterexample register

All examples verified in `tests/unit/test_topo_extraction_math.py` with independent `reference_backward_weight`.

| ID | Phenomenon | Graph / state | Orders | Result |
|----|------------|---------------|--------|--------|
| CE1 | Two topo orders, different bw | DAG 0→1,0→2,1→2 | [0,1,2] vs [0,2,1] | bw 0 vs 1 |
| CE2 | Removed edge forward | Active 0→2,1→2; removed (1,0) w=10 | [1,0,2] | (1,0) forward, bw=0 |
| CE3 | \(B_\pi\subsetneq F\) | Same | [1,0,2] | \(w(F)=5\), bw=0 |
| CE4 | Min-id worse than max-id | Same active DAG | min-id vs max-id | bw 10 vs 0 |
| CE5 | Insertion refine improves (active-respecting) | Same | refine from [0,1,2] | bw 10→0 |
| CE6 | Zero-weight removed, weight tie, set unequal | removed (1,0) w=0 | [1,0,2] | \(B_\pi=\emptyset\), \(F=\{(1,0)\}\), both weights 0 |
