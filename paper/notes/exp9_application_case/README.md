# EXP9 Application Case Study — Final Report

## Dataset

**Wikipedia Adminship Vote Network**

Source: J. Leskovec, D. Huttenlocher, J. Kleinberg. 'Predicting Positive and Negative Links in Online Social Networks.' Proc. WWW 2010.

Application framing: Find a hierarchical prestige ranking of Wikipedia users that minimizes reverse endorsements (backward arcs). Each arc u->v has weight = number of times user u voted in support of user v's adminship candidacy. A minimum-BW ordering extracts the best-fitting hierarchical structure from the endorsement vote graph.

## Algorithm results by instance

### wiki_vote_top50
n=50, m=752, density=0.306939, total_weight=752.0

| Algorithm | BW | Runtime (s) | Status |
|---|---|---|---|
| DRMacIver/FAS | 135.0000 | 0.7925 | ok |
| LR-TA | 141.0000 | 0.2302 | ok |
| IPSNS | 141.0000 | 0.7151 | ok |
| WMSF | 142.0000 | 0.2386 | ok |
| igraph_eades | 153.0000 | 0.3058 | ok |
| weighted_eades | 157.0000 | 0.0217 | ok |

## Error summary

No errors.
