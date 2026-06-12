# Metric Reconciliation

## Table 3 (sparse Panel A): mean instance-level IPSNS reduction

**Formula:** mean over common 93 instances of \((X-\mathrm{IPSNS})/X\times 100\), with \(X>0\); zero-zero pairs contribute 0%.

| Comparator | Recomputed mean (%) |
|---|---:|
| LR-TA | 0.70 |
| WMSF seed | 1.96 |
| DRMacIver/FAS | 21.14 |
| igraph Eades | 28.97 |

**Not** computed from ratio of displayed aggregate mean BW values.

## Repeated-run 21.6%

**Formula:** mean of per-instance median \((\mathrm{DR}-\mathrm{IPSNS})/\mathrm{DR}\times 100\) on 93 instances with DR median \(>0\).

**Recomputed value:** 21.6018% (reported as 21.6%).

## LOLIB 3.88% (corrected wording)

**Previous text:** “3.88% lower mean BW” — misleading (ratio of aggregate means is −1.83%).

**Correct formula (EXP5):** mean of \((\mathrm{BW}_{\mathrm{DR}}-\mathrm{BW}_{\mathrm{IPSNS}})/\mathrm{BW}_{\mathrm{IPSNS}}\times 100\) over instances with \(\mathrm{BW}_{\mathrm{IPSNS}}>0\).

**Recomputed value:** **−3.88%** (DRMacIver/FAS lower under this convention).

Aggregate means: DR 571,687; IPSNS 582,354.

## Exact-validation gaps

| Metric | IPSNS recomputed mean |
|---|---:|
| Optimum-normalized \((\mathrm{BW}-\mathrm{BW}_{\mathrm{opt}})/\mathrm{BW}_{\mathrm{opt}}\times 100\) on 57 standard instances | 0.0031% |
| Total-weight-normalized on same set | 0.00057% |

**r20_60:** absolute gap 3 BW; optimum-normalized gap 0.178%; total-weight-normalized gap 0.032%.

Main text uses optimum-normalized gap; legacy 0.0006% total-weight figure appears only in status docs, not main manuscript.

## Ablation subset (10 instances)

| Claim | Method | Recomputed |
|---|---|---:|
| LR no add-back vs LR-TA | ratio of subset means | +5.94% |
| IPSNS vs best seed | ratio of subset means | −0.76% |

Mean-of-instance-ratio values differ; manuscript now states ratio-of-means explicitly.
