# Manuscript Integration Guide (EXP10)

### Abstract [required]

Add one sentence: repeated-run robustness on 93 instances confirms IPSNS median advantage (38/55/0 win/tie/loss vs DRMacIver).

### Contributions [strongly recommended]

Cite EXP10 as confirmatory stochastic robustness study.

### Experimental protocol [required]

Document 20 IPSNS seeds and 20 DRMacIver repetitions; note DRMacIver non-determinism.

### Sparse benchmark results [required]

Report median-based 38/55/0; retain EXP4 single-run as historical.

### Robustness subsection [required]

New subsection referencing EXP10 tables/figures.

### Statistical analysis [required]

Wilcoxon p=7.739732463297963e-08; bootstrap CI in effect_sizes JSON.

### Limitations [required]

DRMacIver seed uncontrollable; IPSNS zero variance ≠ proof of determinism.

### Conclusion [optional]

Qualify 'robust across repeated executions' on common subset.

