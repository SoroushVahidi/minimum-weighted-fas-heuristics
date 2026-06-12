# Mathematical analysis

## Setup

\(G=(V,A,w)\) with \(w:A\to\mathbb{R}_{\ge 0}\).

\(F\subseteq A\) removed; \(H=(V,A\setminus F)\) active.

For topological order \(\pi\) of \(H\):

\[
B_\pi=\{(u,v)\in A:\ \pi(v)<\pi(u)\}.
\tag{3}
\]

## Proofs

**Lemma (backward subset).** If \(\pi\) is a topological order of \(H\), then every arc of \(H\) is forward under \(\pi\). Any backward arc of \(G\) under \(\pi\) cannot belong to \(A\setminus F\), hence \(B_\pi\subseteq F\). \(\square\)

**Proposition (weight inequality).** For nonnegative weights, \(w(B_\pi)\le w(F)\). \(\square\)

**Equality (general).** \(w(B_\pi)=w(F)\iff w(F\setminus B_\pi)=0\).

**Equality (strictly positive removed weights).** If \(w(a)>0\) for all \(a\in F\), then \(w(B_\pi)=w(F)\iff B_\pi=F\).

## Parallel arcs and self-loops

- Parallel arcs are aggregated before algorithms run; \(B_\pi\) and \(F\) are sets of aggregated arcs.
- Self-loops are deactivated at tolerance and excluded from active graphs; they contribute to \(F\) when removed.

## Four objectives distinguished

| Concept | Meaning in repo |
|---------|-----------------|
| Explicit FAS weight | \(w(F)\) |
| Active-DAG construction | Feasibility of \(H\) |
| Final linear extension | \(\pi\) from Kahn min-id |
| Reported objective | \(\mathrm{bw}(\pi)=w(B_\pi)\) |

Add-back minimizes \(|F|\) on the active state but does **not** force every remaining removed arc to be backward; forward reinsertions are allowed when acyclic.
