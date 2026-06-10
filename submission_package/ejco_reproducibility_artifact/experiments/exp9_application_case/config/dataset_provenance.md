# EXP9 Dataset Provenance

## Dataset
**Wikipedia Adminship Vote Network** (SNAP)

## Citation
J. Leskovec, D. Huttenlocher, J. Kleinberg. 'Predicting Positive and Negative Links in Online Social Networks.' Proc. WWW 2010.

## URL
https://snap.stanford.edu/data/wiki-Vote.txt.gz

## Application framing
Find a hierarchical prestige ranking of Wikipedia users that minimizes reverse endorsements (backward arcs). Each arc u->v has weight = number of times user u voted in support of user v's adminship candidacy. A minimum-BW ordering extracts the best-fitting hierarchical structure from the endorsement vote graph.

## Conversion rule
Restrict to top-N users by total edge degree; w_uv = total vote count from u to v across all elections.

## Full instance (`experiments/exp9_application_case/converted/wiki_vote_top50.d`)
- n = 50 nodes, m = 752 arcs
- Total weight = 752
- Density = 0.306939

## Smoke instance (`experiments/exp9_application_case/converted/wiki_vote_top10.d`)
- n = 10 nodes, m = 26 arcs
- Total weight = 26
- Density = 0.288889

## Anonymization
Original SNAP integer node IDs are used (no names).
