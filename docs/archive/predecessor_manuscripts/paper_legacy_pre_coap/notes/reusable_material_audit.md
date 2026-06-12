# Reusable Material Audit from Predecessor Manuscripts

This file identifies candidate material only. Do not copy blindly; update all claims, notation, experiments, and citations for the new merged manuscript.

## 1. Section: Example Section

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num.tex`
- Length: 201 chars
- Recommendation: Review

Snippet:

```tex
\section{Example Section}
\label{sec1}
%% Labels are used to cross-reference an item using \ref command.

Section text. See Subsection \ref{subsec1}.

%% Use \subsection commands to start a subsection.
```

## 2. Subsection: Example Subsection

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num.tex`
- Length: 290 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Example Subsection}
\label{subsec1}

Subsection text.

%% Use \subsubsection, \paragraph, \subparagraph commands to
%% start 3rd, 4th and 5th level sections.
%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Document_Structure#Sectioning_commands
```

## 3. Subsubsection: Mathematics

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num.tex`
- Length: 2643 chars
- Recommendation: Review

Snippet:

```tex
\subsubsection{Mathematics}
%% Inline mathematics is tagged between $ symbols.
This is an example for the symbol $\alpha$ tagged as inline mathematics.

%% Displayed equations can be tagged using various environments.
%% Single line equations can be tagged using the equation environment.
\begin{equation}
f(x) = (x+a)(x+b)
\end{equation}

%% Unnumbered equations are tagged using starred versions of the environment.
%% amsmath package needs to be loaded for the starred version of equation environment.
\begin{equation*}
f(x) = (x+a)(x+b)
\end{equation*}

%% align or eqnarray environments can be used for multi line equations.
%% & is used to mark alignment points in equations.
%% \\ is used to end a row in a multiline equation.
\begin{align}
 f(x) &= (x+a)(x+b) \\
      &= x^2 + (a+b)x + ab
\end{align}

\begin{eqnarray}
 f(x) &=& (x+a)(x+b) \nonumber\\ %% If equation numbering is not needed for a row use \nonumber.
      &=& x^2 + (a+b)x + ab
\end{eqnarray}

%% Unnumbered versions of align and eqnarray
\begin{align*}
 f(x) &= (x+a)(x+b) \\
      &= x^2 + (a+b)x + ab
\end{align*}

\begin{eqnarray*}
 f(x)&=& (x+a)(x+b) \\
     &=& x^2 + (a+b)x + ab
\end{eqnarray*}

%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Mathematics
%% https://en.wikibooks.org/wiki/LaTeX/Advanced_Mathematics

%% Use a table environment to create tables.
%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Tables
\begin{table}[t]%% placement specifier
%% Use tabular environment to tag the tabular data.
%% https://en.wikibooks.org/wiki/LaTeX/Tables#The_tabular_environment
\centering%% For centre alignment of tabular.
\begin{tabular}{l c r}%% Table column specifiers
%% Tabular cells are separated by &
  1 & 2 & 3 \\ %% A tabular row ends with \\
  4 & 5 & 6 \\
  7 & 8 & 9 \\
\end{tabular}
%% Use \caption command for table caption and label.
\caption{Table Caption}\label{fig1}
\end{table}


%% Use figure environment to create figures
%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions
\begin{figure}[t]%% placement specifier
%% Use \includegraphics command to insert graphic files. Place graphics files in
%% working directory.
\centering%% For centre alignment of image.
\includegraphics{example-image-a}
%% Use \caption command for figure caption and label.
\caption{Figure Caption}\label{fig1}
%% https://en.wikibooks.org/wiki/LaTeX/Importing_Graphics#Importing_external_graphi
```

## 4. Section: Example Appendix Section

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num.tex`
- Length: 912 chars
- Recommendation: Review

Snippet:

```tex
\section{Example Appendix Section}
\label{app1}

Appendix text.

%% For citations use:
%%       \cite{<label>} ==> [1]

%%
Example citation, See \cite{lamport94}.

%% If you have bib database file and want bibtex to generate the
%% bibitems, please use
%%
%%  \bibliographystyle{elsarticle-num}
%%  \bibliography{<your bibdatabase>}

%% else use the following coding to input the bibitems directly in the
%% TeX file.

%% Refer following link for more details about bibliography and citations.
%% https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management

\begin{thebibliography}{00}

%% For numbered reference style
%% \bibitem{label}
%% Text of bibliographic item

\bibitem{lamport94}
  Leslie Lamport,
  \textit{\LaTeX: a document preparation system},
  Addison Wesley, Massachusetts,
  2nd edition,
  1994.

\end{thebibliography}
\end{document}

\endinput
%%
%% End of file `elsarticle-template-num.tex'.
```

## 5. Section: Introduction

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 22 chars
- Recommendation: Potentially reusable after claim/citation verification.

Snippet:

```tex
\section{Introduction}
```

## 6. Subsection: Problem statement

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 2001 chars
- Recommendation: Potentially reusable after claim/citation verification.

Snippet:

```tex
\subsection{Problem statement}
\label{sec:intro-problem}

Let $G=(V,A,w_0)$ be a directed graph with nonnegative arc weights $w_0:A\to\mathbb{R}_{\ge 0}$. The
\emph{weighted feedback arc set} (WFAS) problem asks for a minimum-weight set of arcs whose removal
makes $G$ acyclic. We work with the equivalent \emph{ordering} formulation: a bijection (ranking)
$\pi:V\to\{1,\dots,|V|\}$ classifies each arc $(u,v)\in A$ as \emph{forward} if $\pi(u)<\pi(v)$ and
\emph{backward} otherwise. The quality of an ordering is measured by the total weight of backward
arcs,
\begin{equation}\label{eq:intro-bw}
\mathrm{BW}(\pi)\;=\;\sum_{(u,v)\in A:\,\pi(u)>\pi(v)} w_0(u,v).
\end{equation}
Removing the backward arcs of $\pi$ produces a directed acyclic graph (DAG). Conversely, any acyclic
subgraph admits a topological ordering whose backward-arc set is exactly the removed set. Hence,
WFAS can be viewed as finding an ordering that minimizes~\eqref{eq:intro-bw}.

WFAS is NP-hard, so on large sparse instances one typically relies on heuristics. In this paper we
focus on \emph{refinement} heuristics: we start from strong global seeds and then apply local
improvement steps that are inexpensive and easy to reproduce. Two constraints guide our design.
First, improvements should be \emph{safe}: a refinement procedure that occasionally damages a good
seed can be hard to trust and hard to tune. Second, the method should be \emph{reproducible}: given
the same input, it should yield the same result up to an explicitly controlled random seed and
deterministic tie-breaking. These goals lead to an \emph{incumbent-protected} search strategy: we
keep the best solution seen so far and accept a proposed move only when it strictly decreases
$\mathrm{BW}(\pi)$.

Our computational evaluation uses the 33 standard DIMACS-style benchmark instances reported by
Cavallaro and Cutello~\cite{CC25}, and we measure solution quality exclusively by the backward
weight on the original input weights via~\eqref{eq:intro-bw}.
```

## 7. Subsection: Related work and positioning

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 5327 chars
- Recommendation: Potentially reusable after claim/citation verification.

Snippet:

```tex
\subsection{Related work and positioning}
\label{sec:related}

The (minimum) feedback arc set (FAS) problem is NP-hard even in restricted settings~\cite{K72},
which has motivated a broad literature spanning approximation algorithms, exact and parameterized
methods, and scalable heuristics.

\paragraph{Approximation frameworks and cycle-reduction primitives.}
Even, Naor, Schieber, and Sudan~\cite{ENSS98} develop approximation algorithms for minimum-weight
feedback sets in directed graphs (including feedback vertex/edge set and related subset variants),
via connections to directed multicut and fractional relaxations. Demetrescu and Finocchi~\cite{DF03}
introduce a local-ratio framework for WFAS that repeatedly identifies a directed cycle, subtracts
the minimum arc weight on the cycle, removes newly tight arcs, and then applies an add-back step to
obtain an inclusion-minimal solution. We use this \emph{cycle-reduction} idea as an ingredient
rather than the main contribution: in IPSNS it serves (i) as one of two \emph{global seeds} and (ii)
as a \emph{repair primitive} restricted to a chosen SCC during refinement. Our focus is not on
deriving an approximation ratio, but on designing a refinement framework that is simple, effective
on large sparse graphs, and easy to reproduce end-to-end.

\paragraph{Greedy baselines and modern scalable heuristics.}
A classical baseline is the greedy heuristic \textsc{GR} of Eades, Lin, and Smyth~\cite{ELS93},
which builds an ordering by repeatedly removing sinks/sources and otherwise selecting a vertex that
maximizes outdegree minus indegree. Hecht, Gonciarz, and Horv\'at~\cite{HGH21} propose
\textsc{TIGHT}, which improves upon \textsc{GR} using localized operations that target cyclic
structures. Cavallaro and Cutello~\cite{CC25} propose \textsc{WMSF}, which removes arcs according to
weight-based orderings and then applies add-back minimization (with stabilization), obtaining
solutions competitive with \textsc{TIGHT} on their benchmark suite. IPSNS sits in this empirical
line, but adds a structural refinement layer: we start from strong global constructions (WMSF and a
cycle-reduction seed) and then apply \emph{SCC-neighborhood} destroy--repair moves that explicitly
target the cyclic ``core'' of the instance. Crucially, IPSNS is \emph{incumbent-protected}: a move
is accepted only if it strictly decreases backward weight, and the algorithm outputs the best
incumbent encountered. This yields a guarantee that is directly useful i
```

## 8. Subsection: Contributions and organization

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 3073 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Contributions and organization}
\label{sec:intro-contrib}

\paragraph{Contributions.}
We propose \textbf{IPSNS}, an \emph{incumbent-protected} refinement framework for the weighted feedback arc set
problem. IPSNS is designed for large sparse weighted digraphs and is built around a simple idea: start from strong
global seeds, focus improvement effort on SCC neighborhoods where backward weight concentrates, and accept a move
only when it strictly improves the best solution seen so far. Concretely, IPSNS consists of the following parts.

\smallskip
\noindent\textbf{(1) Best-of-two global seeding.}
We compute two complementary initial solutions: (i) a seed produced by the \textsc{WMSF} heuristic of Cavallaro and
Cutello~\cite{CC25} and (ii) a seed produced by local-ratio cycle reduction in the spirit of~\cite{DF03}. Each seed is
post-processed by a heavy-first topological add-back routine that restores acyclicity while attempting to keep the
removed weight small, and we evaluate a seed by the backward weight of the topological ordering it induces
(Eq.~\eqref{eq:intro-bw}).

\smallskip
\noindent\textbf{(2) SCC-neighborhood destroy--repair refinement.}
Starting from the better seed, IPSNS performs large-neighborhood search moves restricted to strongly connected
components (SCCs) of the original graph. At each iteration, IPSNS selects an SCC that contributes substantial backward
weight under the current ordering, applies a localized \emph{destroy} perturbation inside that SCC, and then
\emph{repairs} feasibility using SCC-restricted cycle reduction followed by SCC-restricted heavy-first add-back. Global
feasibility is checked by recomputing a topological ordering of the current active subgraph.

\smallskip
\noindent\textbf{(3) Incumbent protection (a non-degradation guarantee).}
IPSNS maintains a best-so-far incumbent snapshot and commits a proposed move only upon strict improvement in backward
weight. As a result, IPSNS is \emph{provably non-degrading}: the algorithm always returns an ordering whose backward
weight is no worse than the better of its two initial seeds.

\smallskip
\noindent\textbf{(4) Reproducible evaluation and artifacts.}
We evaluate IPSNS on the 33 standard benchmark instances reported in~\cite{CC25} and measure solution quality by
backward weight (Eq.~\eqref{eq:intro-bw}). Our implementation uses deterministic parsing (including aggregation of
parallel arcs), deterministic tie-breaking, and explicit random seeds. To facilitate rep
```

## 9. Section: Method: Incumbent-Protected SCC-Neighborhood LNS

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 58 chars
- Recommendation: Potentially reusable, but must be synchronized with current repository code.

Snippet:

```tex
\section{Method: Incumbent-Protected SCC-Neighborhood LNS}
```

## 10. Subsection: Definitions and notation

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 4649 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Definitions and notation}
\label{sec:defs-notation}

We consider a directed weighted graph $G=(V,A,w_0)$, where $V$ is the vertex set,
$A\subseteq V\times V$ is the arc set, and $w_0:A\to\mathbb{R}_{\ge 0}$ assigns a nonnegative
\emph{original} weight to each arc. If the input contains multiple arcs with the same ordered pair
$(u,v)$, we aggregate them into a single arc with weight equal to the sum of their weights; this
aggregation preserves $\mathrm{BW}(\pi)$ for every ordering $\pi$. We write an arc $e\in A$ as
$e=(u,v)$ with tail $u$ and head $v$.

\paragraph{Vertex orderings and backward weight.}
A (total) vertex ordering is a bijection $\pi:V\to\{1,\dots,|V|\}$, where $\pi(v)$ denotes the
position of vertex $v$. An arc $(u,v)$ is \emph{forward} under $\pi$ if $\pi(u)<\pi(v)$ and
\emph{backward} otherwise. The backward weight of $\pi$ (always evaluated under the original weights)
is
\begin{equation}\label{eq:backward-weight}
\mathrm{BW}(\pi)\;=\;\sum_{(u,v)\in A:\,\pi(u)>\pi(v)} w_0(u,v),
\end{equation}
and the forward weight is
\begin{equation}\label{eq:forward-weight}
\mathrm{FW}(\pi)\;=\;\sum_{(u,v)\in A:\,\pi(u)<\pi(v)} w_0(u,v).
\end{equation}
Let $W_{\mathrm{tot}}=\sum_{(u,v)\in A} w_0(u,v)$ denote the total weight; then
\begin{equation}\label{eq:bw-fw-total}
\mathrm{BW}(\pi)=W_{\mathrm{tot}}-\mathrm{FW}(\pi).
\end{equation}

\paragraph{Weighted feedback arc set (WFAS).}
A set of arcs $F\subseteq A$ is a \emph{feedback arc set} if removing $F$ makes the graph acyclic, i.e.,
$(V,A\setminus F)$ is a DAG. Its weight is $w_0(F)=\sum_{e\in F} w_0(e)$, and WFAS asks for a
minimum-weight feedback arc set. The feedback-set and ordering views coincide: for any ordering $\pi$,
the set of backward arcs
\begin{equation}\label{eq:backward-arc-set}
F_\pi=\{(u,v)\in A:\pi(u)>\pi(v)\}
\end{equation}
is a feedback arc set and satisfies
\begin{equation}\label{eq:wfas-eq-bw}
w_0(F_\pi)=\mathrm{BW}(\pi).
\end{equation}

\paragraph{Acyclic active states and extracted orderings.}
IPSNS maintains a subset of \emph{active} arcs $A_{\mathrm{act}}\subseteq A$ and its complement
$F_{\mathrm{inact}}=A\setminus A_{\mathrm{act}}$. The feasibility invariant is that the active subgraph
$(V,A_{\mathrm{act}})$ is a DAG. Whenever an ordering is needed, we compute a topological ordering of
$(V,A_{\mathrm{act}})$ and use it as the produced ranking $\pi$.

\medskip
\noindent\textbf{Inactive arcs vs.\ backward arcs.}
Every active arc is forward under any topological order
```

## 11. Subsection: Framework overview

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 4074 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Framework overview}\label{sec:framework}

We seek a low-cost weighted feedback arc set (WFAS), i.e., a subset $F\subseteq A$ whose removal makes $G$
acyclic while minimizing
\begin{equation}\label{eq:framework-wfas}
w_0(F)=\sum_{e\in F} w_0(e).
\end{equation}
We work with the equivalent ordering formulation: a ranking $\pi:V\to\{1,\dots,|V|\}$ induces forward arcs
$(u,v)$ with $\pi(u)<\pi(v)$ and backward arcs with $\pi(u)>\pi(v)$, and the objective is to minimize the
backward weight $\mathrm{BW}(\pi)$ (Eq.~\eqref{eq:backward-weight}). Throughout, solution quality is evaluated
by $\mathrm{BW}(\pi)$ computed under the original weights $w_0$.

\medskip
\noindent\textbf{Overview.}
IPSNS is a two-phase heuristic built around a practical promise: refinement should not be allowed to damage a
good seed. We therefore construct two complementary global seeds, keep the better one as an \emph{incumbent},
and then attempt improvements through localized large-neighborhood moves. The central mechanism is
\emph{incumbent protection}: we store the best acyclic state encountered and commit a proposed move only if it
strictly reduces the incumbent backward weight. This makes the refinement phase a safe add-on---if no improving
move is found, IPSNS still returns the best seed.

\paragraph{Phase I: best-of-two global seeding.}
We first construct two candidate acyclic states using established templates from the literature.
\begin{itemize}
\item \textbf{WMSF seed (Cavallaro--Cutello~\cite{CC25}).}
We implement the \textsc{WMSF} pipeline described in~\cite{CC25}: arcs are removed according to a prescribed
weight-based ordering until the remaining subgraph becomes acyclic, followed by a heavy-first topological
add-back procedure that reinstates as many removed arcs as possible without creating a directed cycle.
\item \textbf{Local-ratio seed (Demetrescu--Finocchi~\cite{DF03}).}
We apply local-ratio cycle reduction in the spirit of~\cite{DF03} to deactivate tight arcs until the active
subgraph becomes acyclic, and then apply the same heavy-first add-back procedure.
\end{itemize}
Each seed yields an acyclic active subgraph and an induced topological ordering $\pi$; we evaluate both by
$\mathrm{BW}(\pi)$ and initialize the incumbent to the better of the two.

\paragraph{Phase II: SCC-neighborhood refinement.}
Every directed cycle lies entirely within a strongly connected component (SCC). IPSNS uses this structural fact
as a locality principle: SCCs are computed once on t
```

## 12. Subsection: Phase I: Best-of-two global seeding (WMSF and local-ratio)

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 4265 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Phase I: Best-of-two global seeding (WMSF and local-ratio)}\label{sec:phase1}

Phase~I constructs two global candidate solutions using complementary templates from prior work: the \textsc{WMSF}
heuristic of Cavallaro and Cutello~\cite{CC25} and local-ratio cycle reduction in the spirit of Demetrescu and
Finocchi~\cite{DF03}. Each seed produces an acyclic active subgraph and an induced topological ordering $\pi$. We
evaluate both seeds by backward weight $\mathrm{BW}(\pi)$ under the original weights $w_0$ and initialize the
incumbent to the better one. This best-of-two initialization is the starting point for the incumbent-protection
guarantee used in Phase~II.

\paragraph{Seed A: WMSF seeding pipeline (Cavallaro--Cutello~\cite{CC25}).}
We follow the template described in~\cite{CC25}. Starting from the full graph, arcs are removed according to a
prescribed ordering until the remaining subgraph becomes acyclic. The removed set is then minimized by a
heavy-first topological add-back procedure that restores as many removed arcs as possible without creating a
directed cycle. As in~\cite{CC25}, we consider two arc orderings:
\begin{itemize}
\item \textbf{L1:} nondecreasing original weight $w_0(e)$;
\item \textbf{L2:} nondecreasing ratio
\begin{equation}\label{eq:wmsf-l2}
\frac{w_0(u,v)}{W^{\mathrm{in}}(u)+W^{\mathrm{out}}(v)},
\end{equation}
where
\begin{equation}\label{eq:wmsf-inout}
W^{\mathrm{in}}(x)=\sum_{(y,x)\in A} w_0(y,x)
\qquad\text{and}\qquad
W^{\mathrm{out}}(x)=\sum_{(x,y)\in A} w_0(x,y)
\end{equation}
are computed from the original input graph.
\end{itemize}
We refer to the resulting ordering as $\pi_{\mathrm{WMSF}}$ and its backward weight as
$\mathrm{BW}_{\mathrm{WMSF}}=\mathrm{BW}(\pi_{\mathrm{WMSF}})$.

\paragraph{Seed B: Local-ratio cycle reduction (Demetrescu--Finocchi~\cite{DF03}).}
Our second seed applies local-ratio cycle reduction in the spirit of~\cite{DF03}. Starting from the full graph,
we maintain reduced weights $\tilde w(\cdot)$ initialized as $\tilde w(e)\leftarrow w_0(e)$. We repeatedly identify
a directed cycle $C$ in the current active subgraph, set
\begin{equation}\label{eq:lr-eps}
\varepsilon=\min_{e\in C}\tilde w(e),
\end{equation}
and reduce the cycle weights by
\begin{equation}\label{eq:lr-update}
\tilde w(e)\leftarrow \tilde w(e)-\varepsilon \qquad \text{for all } e\in C.
\end{equation}
Any arc whose reduced weight becomes (near) zero is declared \emph{tight} and deactivated. The process terminates
once the remai
```

## 13. Subsection: Phase II: SCC-neighborhood LNS refinement

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 4249 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Phase II: SCC-neighborhood LNS refinement}\label{sec:phase2}

Phase~II refines the Phase~I incumbent via a large-neighborhood search (LNS) that operates inside strongly
connected components (SCCs) of the \emph{original} graph. Since every directed cycle is contained within a
single SCC, SCCs provide fixed neighborhoods in which we can make substantial local changes while preserving
global feasibility by maintaining an acyclic active subgraph and extracting orderings via topological sorting.

\paragraph{SCC selection by backward-weight contribution.}
Given the current incumbent state, we compute a topological ordering $\pi$ of the maintained acyclic subgraph
and use it to identify where the current backward weight concentrates. For an SCC $S\subseteq V$, let
\begin{equation}\label{eq:scc-internal-arcs}
A(S)=\{(u,v)\in A:\,u\in S,\; v\in S\}
\end{equation}
denote the set of arcs internal to $S$ (with SCCs computed once on the input graph). We score SCCs by their
\emph{backward contribution} under $\pi$,
\begin{equation}\label{eq:scc-bw}
\mathrm{BW}_S(\pi)\;=\;\sum_{(u,v)\in A(S):\,\pi(u)>\pi(v)} w_0(u,v),
\end{equation}
and consider only SCCs with $\mathrm{BW}_S(\pi)>0$. At each iteration we form a pool of the top-$K$ SCCs by
$\mathrm{BW}_S(\pi)$ and sample one SCC from this pool with probability proportional to $\mathrm{BW}_S(\pi)$.
This biases the search toward neighborhoods that currently explain a larger portion of the objective.

\paragraph{Destroy--repair move inside an SCC.}
Let $S$ be the selected SCC. A single LNS iteration applies a destroy--repair move that modifies only arcs in
$A(S)$, leaving the state outside $S$ unchanged.
\begin{itemize}
\item \textbf{Destroy (localized perturbation).}
We temporarily perturb the incumbent within $S$ by two complementary edits:
(i) we reactivate a fraction of currently inactive SCC-internal arcs, processed in nonincreasing order of
$w_0(e)$ (heavy-first), and
(ii) we deactivate a small fraction of currently active SCC-internal arcs, processed in nondecreasing order of
$w_0(e)$ (light-first). This ``swap-style'' perturbation increases flexibility inside the SCC while keeping the
rest of the instance fixed.

\item \textbf{Repair (SCC-restricted cycle reduction + add-back).}
The destroy step may create directed cycles within the SCC-induced subgraph. We restore acyclicity using two
subroutines restricted to $A(S)$:
(i) SCC-restricted local-ratio cycle reduction in the spirit of~\cite{DF03}, where redu
```

## 14. Subsection: Complexity and implementation notes

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 5894 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Complexity and implementation notes}\label{sec:complexity}

This section summarizes the main computational costs of IPSNS and records the implementation choices that most
strongly influence practical performance. Phase~I uses two established templates---\textsc{WMSF} seeding as in
\cite{CC25} and local-ratio cycle reduction in the spirit of~\cite{DF03}---while Phase~II adds SCC-local
destroy--repair refinement together with repeated global evaluation and incumbent protection.

\paragraph{Preprocessing and representation.}
Input parsing (including aggregation of parallel arcs) and construction of adjacency lists take $O(n+m)$ time.
We represent arcs by integer IDs and store outgoing/incoming adjacency lists of arc IDs; the current state is
maintained by a Boolean \texttt{active} flag per arc. Adjacency lists are built once and reused across all phases,
so local modifications are implemented by toggling flags rather than rebuilding subgraphs. A topological ordering
of the current active subgraph is computed by a standard linear-time scan,
\begin{equation}\label{eq:toposort-cost}
T_{\mathrm{topo}}=O(n+m).
\end{equation}

\paragraph{Phase I seeding costs.}
\emph{WMSF seed.}
Following~\cite{CC25}, WMSF orders arcs by a weight-based key (L1 or L2) and removes arcs until the remaining
subgraph is acyclic, followed by heavy-first add-back minimization. Sorting $m$ arcs costs $O(m\log m)$. The
subsequent removals interleave with acyclicity checks based on topological sorting; each such check costs
$O(n+m)$.

\emph{Local-ratio seed.}
Local-ratio cycle reduction~\cite{DF03} iterates: find a directed cycle in the current subgraph, subtract the
minimum reduced weight on that cycle, and deactivate arcs that become tight. A DFS-based cycle search has
worst-case cost $O(n+m)$, and a single cycle update costs $O(|C|)$. In the worst case, the number of reductions
can be $O(m)$, yielding the conservative bound $O(m(n+m))$ for the full cycle-reduction stage. In practice,
multiple arcs may become tight per reduction, and the active graph shrinks quickly.

\paragraph{Heavy-first topological add-back (global or SCC-restricted).}
Both seeds and the Phase~II repair stage use the same add-back pattern that mirrors the post-processing step in
\cite{DF03} and the minimization step in~\cite{CC25}: inactive arcs are processed in nonincreasing $w_0(e)$ order
and reactivated whenever doing so preserves acyclicity. Sorting $r$ candidate arcs costs $O(r\log r)$. Each
reactivati
```

## 15. Section: Computational Experiments

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 35 chars
- Recommendation: Likely obsolete except wording/structure; experiments must be replaced by EXP1b-EXP5.

Snippet:

```tex
\section{Computational Experiments}
```

## 16. Subsection: Experimental setup

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 3812 chars
- Recommendation: Likely obsolete except wording/structure; experiments must be replaced by EXP1b-EXP5.

Snippet:

```tex
\subsection{Experimental setup}
\label{sec:exp-setup}

\paragraph{Benchmark instances.}
We evaluate on weighted directed graph instances from the \texttt{graph-benchmarks} collection.\footnote{Repository:
\url{https://github.com/alidasdan/graph-benchmarks}.}
This is the same suite (families and instance names) used by Cavallaro and Cutello~\cite{CC25}; we use the
corresponding DIMACS-style \texttt{.d} input files. Following~\cite{CC25}, we exclude the \texttt{arwiki} family
from the main tables and report it separately. We also follow~\cite{CC25} in splitting the suite into
(i) instances whose full input graph is a single SCC and (ii) instances with multiple SCCs.

\paragraph{Objective and reporting.}
Given an ordering $\pi:V\to\{1,\dots,|V|\}$, we report solution quality by the backward weight
$\mathrm{BW}(\pi)$ (Eq.~\eqref{eq:backward-weight}); lower is better. For every method, we compute
$\mathrm{BW}(\pi)$ from the \emph{returned ordering} under the original weights~$w_0$. This produces a uniform
evaluation that is independent of internal representations (e.g., an explicitly maintained removed-arc set) and
matches the WFAS objective.

\paragraph{Reproducibility and preprocessing.}
All code, scripts, and configuration files used to generate the reported results are publicly available; see the
\emph{Data and code availability} section. As a deterministic preprocessing step, we aggregate parallel arcs so that
each ordered pair $(u,v)$ appears at most once with weight equal to the sum of its parallel weights; this preserves
$\mathrm{BW}(\pi)$ for every ordering~$\pi$ and removes redundancy from subsequent procedures. We additionally use
deterministic tie-breaking (by arc endpoints and a fixed arc ID) whenever ordering ties arise. Randomization is
confined to SCC selection in Phase~II and is controlled by an explicit seed.

\paragraph{Methods compared.}
We compare the following approaches.
\begin{itemize}
    \item \textbf{TIGHT}: The heuristic of Hecht, Gonciarz, and Horv\'at~\cite{HGH21}. We report \textsc{TIGHT}
    values as reported in~\cite{CC25}.
    \item \textbf{WMSF (reported)}: The \textsc{WMSF} values reported by Cavallaro and Cutello~\cite{CC25}.
    \item \textbf{WMSF (ours)}: Our independent implementation of the \textsc{WMSF} seeding pipeline described
    in~\cite{CC25} (remove-arcs followed by heavy-first topological add-back minimization with deterministic
    tie-breaking).\footnote{Minor implementation choices (e.g., tie-breaking and cy
```

## 17. Subsection: Results on standard benchmarks

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 9550 chars
- Recommendation: Likely obsolete except wording/structure; experiments must be replaced by EXP1b-EXP5.

Snippet:

```tex
\subsection{Results on standard benchmarks}
\label{sec:results-standard}

Tables~\ref{tab:results_scc} and~\ref{tab:results_multiscc} report backward-weight (BW) values on the
33 benchmark instances used by Cavallaro and Cutello~\cite{CC25}. Following~\cite{CC25}, we split the suite into
(i) instances whose full input graph is a single strongly connected component (Table~\ref{tab:results_scc}) and
(ii) instances with multiple SCCs (Table~\ref{tab:results_multiscc}). For each dataset (\textbf{Code}), the column
$|V|$--$|A|$ gives the number of vertices and arcs after deterministic parsing, and each numeric entry is the total
weight of backward arcs induced by the returned ordering (Eq.~\eqref{eq:backward-weight}); lower is better.

\paragraph{Meaning of the columns.}
\textbf{TIGHT} denotes the BW achieved by \textsc{TIGHT}~\cite{HGH21} as reported in~\cite{CC25}.
\textbf{WMSF (reported)} denotes the \textsc{WMSF} values reported by Cavallaro and Cutello~\cite{CC25}.
\textbf{WMSF (ours)} denotes our independent implementation of the \textsc{WMSF} seeding pipeline described
in~\cite{CC25} (remove-arcs followed by heavy-first topological add-back minimization, with deterministic
tie-breaking).\footnote{Independent implementations can differ from reported values due to choices not fully
specified in~\cite{CC25} (e.g., tie-breaking and cycle-check frequency). We therefore report both columns. When
we run multiple arc-ordering variants (L1/L2), we report the best BW obtained.}
\textbf{Local-ratio (ours)} denotes our instantiation of local-ratio cycle reduction in the spirit of
Demetrescu and Finocchi~\cite{DF03}, followed by the same heavy-first topological add-back minimization.
Finally, \textbf{IPSNS (ours)} is our incumbent-protected SCC-neighborhood LNS
(Sections~\ref{sec:framework}--\ref{sec:phase2}), initialized from the better of the two seeds and refined via
SCC-local destroy--repair moves.

\paragraph{Incumbent protection and improvements beyond seeding.}
IPSNS maintains a best-so-far incumbent and updates it only upon strict improvement in backward weight (up to
tolerance), as in~\eqref{eq:phase2-accept}. Consequently, for every instance in the tables, IPSNS satisfies the
non-degradation guarantee
\begin{equation}\label{eq:results-nondegradation}
\mathrm{BW}(\text{IPSNS}) \;\le\; \min\{\mathrm{BW}(\text{WMSF (ours)}),\,\mathrm{BW}(\text{Local-ratio (ours)})\}.
\end{equation}
On this suite, IPSNS improves upon \textbf{WMSF (ours)} on 26 instances and tie
```

## 18. Section: Conclusions and Future Work

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 61 chars
- Recommendation: Review

Snippet:

```tex
\section{Conclusions and Future Work}
\label{sec:conclusions}
```

## 19. Subsection: Summary of findings

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 1785 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Summary of findings}
\label{sec:conclusion-summary}

This paper introduced \textbf{IPSNS}, an incumbent-protected hybrid heuristic for the weighted feedback arc set
(WFAS) problem in weighted directed graphs. IPSNS combines two complementary global constructions---the
\textsc{WMSF} seeding pipeline of Cavallaro and Cutello~\cite{CC25} (implemented independently from the description
in~\cite{CC25}) and local-ratio cycle reduction in the spirit of Demetrescu and Finocchi~\cite{DF03}---with an
SCC-neighborhood large-neighborhood search (LNS) refinement. In Phase~II, IPSNS applies destroy--repair moves
restricted to SCC neighborhoods computed on the original input graph and commits a move only upon strict
improvement in backward weight (Eq.~\eqref{eq:phase2-accept}). This yields the central non-degradation guarantee:
the final ordering returned by IPSNS has backward weight no larger than the better of the two Phase~I seeds
(Eq.~\eqref{eq:framework-nondegradation}).

On the 33 benchmark instances used by Cavallaro and Cutello~\cite{CC25}
(Tables~\ref{tab:results_scc}--\ref{tab:results_multiscc}), IPSNS is consistently competitive with the published
baselines reproduced in~\cite{CC25} (\textsc{TIGHT}~\cite{HGH21} and \textsc{WMSF}~\cite{CC25}). In particular,
IPSNS improves upon \textsc{WMSF (reported)} on 18 instances (ties on 13 and losses on 2) and improves upon
\textsc{TIGHT} on 9 instances (ties on 17 and losses on 7). Beyond these comparisons, IPSNS yields strict
improvements beyond \emph{both} internal seeds on 9 instances (Eq.~\eqref{eq:results-beyond-both}), indicating
that SCC-local destroy--repair refinement can extract additional gains even when starting from strong global
initializations, while incumbent protection prevents regressions.
```

## 20. Subsection: Limitations

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 1420 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Limitations}
\label{sec:conclusion-limitations}

Our evaluation is centered on the benchmark suite used in~\cite{CC25}. While this suite provides a standardized
testbed for WFAS heuristics on sparse instances, it does not cover the full range of graph structures encountered
in other applications. In particular, the suite does not directly isolate which structural features---such as the
distribution of SCC sizes, the concentration of weight on inter-SCC versus intra-SCC arcs, or the density of short
cycles inside large SCCs---best predict when SCC-neighborhood refinement yields substantial gains.

A second limitation concerns comparisons to published baselines. For \textsc{TIGHT} and \textsc{WMSF (reported)},
we use the values reported in~\cite{CC25}. We also provide an independent implementation of the \textsc{WMSF}
pipeline described in~\cite{CC25}, but some implementation details are not fully specified (e.g., tie-breaking and
the frequency of cycle/acyclicity checks), and these choices can affect outcomes on a subset of instances. For this
reason, our strongest and most reproducible conclusions are those that rely on explicitly defined components in
our pipeline---namely, IPSNS relative to its two internal seeds and the non-degradation guarantee
(Eq.~\eqref{eq:framework-nondegradation})---together with comparisons to published numbers interpreted strictly as
reported in~\cite{CC25}.
```

## 21. Subsection: Future directions

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 2222 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Future directions}
\label{sec:conclusion-future}

Several directions appear promising for extending incumbent-protected refinement for WFAS while preserving the
central strict-improvement acceptance rule (Eq.~\eqref{eq:phase2-accept}) and the non-degradation guarantee
(Eq.~\eqref{eq:framework-nondegradation}).

\paragraph{Broader benchmarks and structural diagnostics.}
A natural next step is to evaluate IPSNS on substantially larger and more diverse datasets, including additional
families from the same benchmark repository and other public directed graph collections. Beyond aggregate BW
values, it would be valuable to connect improvements to structural predictors, such as SCC size distributions,
the fraction of total weight carried by inter-SCC versus intra-SCC arcs, and the prevalence of short cycles within
large SCCs. Such diagnostics could clarify when SCC-local destroy--repair refinement is most effective and guide
instance-aware parameter choices.

\paragraph{Stronger neighborhoods and adaptive policies.}
The SCC-neighborhood LNS can be enriched without changing the incumbent-protected acceptance rule. Examples include
alternative SCC scoring functions (beyond $\mathrm{BW}_S(\pi)$), adaptive choices of the candidate pool size $K$,
and mixed selection policies that occasionally explore lower-ranked SCCs to avoid over-focusing on a single region.
More expressive destroy--repair operators---for instance, weight-aware perturbations that target arcs with high
marginal contribution to local backward weight, or cycle-selection heuristics inside the repair routine---may
increase the frequency of improvements beyond both seeds while preserving the same non-degradation guarantee.

\paragraph{Parallel and multi-start variants under controlled randomness.}
The framework naturally supports parallelism through independent multi-start runs and, more cautiously, through
parallel evaluation of candidate neighborhood moves. With deterministic tie-breaking and controlled randomness
(e.g., fixed seeds per worker), parallel variants can remain reproducible while improving solution quality by
exploring a wider portion of the search space and retaining the best incumbent found across runs.
```

## 22. Section: Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 538 chars
- Recommendation: Review

Snippet:

```tex
\section*{Declaration of generative AI and AI-assisted technologies in the manuscript preparation process}
During the preparation of this work, the author(s) used ChatGPT (OpenAI) to support the
organization and editing of the manuscript text and to assist with drafting small portions of
implementation code. After using this tool, the author(s) reviewed and edited the content as needed,
verified the correctness of any code incorporated into the implementation, and take(s) full
responsibility for the content of the published article.
```

## 23. Section: Data and code availability

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-harv.tex`
- Length: 574 chars
- Recommendation: Review

Snippet:

```tex
\section*{Data and code availability}
The benchmark instances used in our experiments are publicly available as part of the
\texttt{graph-benchmarks} collection.\footnote{\url{https://github.com/alidasdan/graph-benchmarks}}
Our implementation of IPSNS, together with scripts and configuration files used to produce the
reported results, is publicly available at
\url{https://github.com/SoroushVahidi/weighted-minfas-codes/tree/main}.

\bibliographystyle{elsarticle-harv}
\bibliography{references}


\end{document}

\endinput
%%
%% End of file `elsarticle-template-harv.tex'.
```

## 24. Section: Example Section

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num-names.tex`
- Length: 201 chars
- Recommendation: Review

Snippet:

```tex
\section{Example Section}
\label{sec1}
%% Labels are used to cross-reference an item using \ref command.

Section text. See Subsection \ref{subsec1}.

%% Use \subsection commands to start a subsection.
```

## 25. Subsection: Example Subsection

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num-names.tex`
- Length: 290 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Example Subsection}
\label{subsec1}

Subsection text.

%% Use \subsubsection, \paragraph, \subparagraph commands to
%% start 3rd, 4th and 5th level sections.
%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Document_Structure#Sectioning_commands
```

## 26. Subsubsection: Mathematics

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num-names.tex`
- Length: 2643 chars
- Recommendation: Review

Snippet:

```tex
\subsubsection{Mathematics}
%% Inline mathematics is tagged between $ symbols.
This is an example for the symbol $\alpha$ tagged as inline mathematics.

%% Displayed equations can be tagged using various environments.
%% Single line equations can be tagged using the equation environment.
\begin{equation}
f(x) = (x+a)(x+b)
\end{equation}

%% Unnumbered equations are tagged using starred versions of the environment.
%% amsmath package needs to be loaded for the starred version of equation environment.
\begin{equation*}
f(x) = (x+a)(x+b)
\end{equation*}

%% align or eqnarray environments can be used for multi line equations.
%% & is used to mark alignment points in equations.
%% \\ is used to end a row in a multiline equation.
\begin{align}
 f(x) &= (x+a)(x+b) \\
      &= x^2 + (a+b)x + ab
\end{align}

\begin{eqnarray}
 f(x) &=& (x+a)(x+b) \nonumber\\ %% If equation numbering is not needed for a row use \nonumber.
      &=& x^2 + (a+b)x + ab
\end{eqnarray}

%% Unnumbered versions of align and eqnarray
\begin{align*}
 f(x) &= (x+a)(x+b) \\
      &= x^2 + (a+b)x + ab
\end{align*}

\begin{eqnarray*}
 f(x)&=& (x+a)(x+b) \\
     &=& x^2 + (a+b)x + ab
\end{eqnarray*}

%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Mathematics
%% https://en.wikibooks.org/wiki/LaTeX/Advanced_Mathematics

%% Use a table environment to create tables.
%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Tables
\begin{table}[t]%% placement specifier
%% Use tabular environment to tag the tabular data.
%% https://en.wikibooks.org/wiki/LaTeX/Tables#The_tabular_environment
\centering%% For centre alignment of tabular.
\begin{tabular}{l c r}%% Table column specifiers
%% Tabular cells are separated by &
  1 & 2 & 3 \\ %% A tabular row ends with \\
  4 & 5 & 6 \\
  7 & 8 & 9 \\
\end{tabular}
%% Use \caption command for table caption and label.
\caption{Table Caption}\label{fig1}
\end{table}


%% Use figure environment to create figures
%% Refer following link for more details.
%% https://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions
\begin{figure}[t]%% placement specifier
%% Use \includegraphics command to insert graphic files. Place graphics files in
%% working directory.
\centering%% For centre alignment of image.
\includegraphics{example-image-a}
%% Use \caption command for figure caption and label.
\caption{Figure Caption}\label{fig1}
%% https://en.wikibooks.org/wiki/LaTeX/Importing_Graphics#Importing_external_graphi
```

## 27. Section: Example Appendix Section

- Source: `paper/source_material/extracted_archives/Incumbent_Protected_SCC_Neighborhood_Search_for_the_Weighted_Feedback_Arc_Set_Problem/elsarticle-template-num-names.tex`
- Length: 999 chars
- Recommendation: Review

Snippet:

```tex
\section{Example Appendix Section}
\label{app1}

Appendix text.

%% For citations use:
%%       \citet{<label>} ==> Lamport [21]
%%       \citep{<label>} ==> [21]
%%
Example citation, See \citet{lamport94}.

%% If you have bib database file and want bibtex to generate the
%% bibitems, please use
%%
%%  \bibliographystyle{elsarticle-num-names}
%%  \bibliography{<your bibdatabase>}

%% else use the following coding to input the bibitems directly in the
%% TeX file.

%% Refer following link for more details about bibliography and citations.
%% https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management

\begin{thebibliography}{00}

%% For authoryear reference style
%% \bibitem[Author(year)]{label}
%% Text of bibliographic item

\bibitem[Lamport(1994)]{lamport94}
  Leslie Lamport,
  \textit{\LaTeX: a document preparation system},
  Addison Wesley, Massachusetts,
  2nd edition,
  1994.

\end{thebibliography}
\end{document}

\endinput
%%
%% End of file `elsarticle-template-num-names.tex'.
```

## 28. Section: Introduction

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 22 chars
- Recommendation: Potentially reusable after claim/citation verification.

Snippet:

```tex
\section{Introduction}
```

## 29. Subsection: Problem statement

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 1206 chars
- Recommendation: Potentially reusable after claim/citation verification.

Snippet:

```tex
\subsection{Problem statement}
\label{sec:intro-problem}

Given a directed weighted graph $G=(V,A,w)$, the \emph{weighted feedback arc set} (WFAS) problem asks
for a minimum-total-weight set of arcs whose removal makes $G$ acyclic. An equivalent and convenient
view is in terms of vertex orderings: a bijection (ranking) $\pi:V\rightarrow\{1,\dots,|V|\}$ induces
a partition of arcs into \emph{forward} arcs $(u,v)$ with $\pi(u)<\pi(v)$ and \emph{backward} arcs with
$\pi(u)>\pi(v)$. The objective is to minimize the total weight of backward arcs,
\begin{equation}
\mathrm{BW}(\pi)\;=\;\sum_{(u,v)\in A:\,\pi(u)>\pi(v)} w(u,v),
\end{equation}
since removing all backward arcs of any ordering yields a directed acyclic graph (DAG).

Computing an optimal WFAS is NP-hard, and exact methods become impractical on large sparse instances.
This work focuses on fast, scalable heuristics that return high-quality orderings (low backward
weight) together with an explicit feedback arc set, while remaining simple enough to implement and
reproduce. We target the standard DIMACS-like benchmark instances used in recent experimental studies,
and measure performance by backward weight and end-to-end wall-clock time.
```

## 30. Subsection: Related work and positioning

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 6872 chars
- Recommendation: Potentially reusable after claim/citation verification.

Snippet:

```tex
\subsection{Related work and positioning}
\label{sec:related}

The (minimum) feedback arc set (FAS) problem is NP-hard, even in restricted settings \cite{K72},
which has motivated a large body of approximation algorithms, exact/parameterized methods, and
scalable heuristics for large instances.

\paragraph{Approximation frameworks.}
Even, Naor, Schieber, and Sudan \cite{ENSS98} develop approximation algorithms for minimum-weight
feedback sets in directed graphs (feedback vertex/edge set and related subset variants), obtaining
polynomial-time guarantees via reductions to directed multicut formulations and techniques based on
fractional relaxations. Demetrescu and Finocchi \cite{DF03} propose a local-ratio framework for
weighted feedback arc set (WFAS) that repeatedly selects a directed cycle, subtracts the minimum
cycle-edge weight from all edges on the cycle, deletes newly zero-weight edges, and then applies an
add-back/minimization step to obtain an inclusion-minimal feedback arc set. Our LR-TA method follows
this local-ratio template, but emphasizes an implementation engineered for speed and reproducibility
on large sparse instances.

\paragraph{Fast greedy baselines and modern heuristics.}
A classical baseline is the greedy heuristic \textsc{GR} of Eades, Lin, and Smyth \cite{ELS93}, which
constructs an ordering by repeatedly removing sinks/sources and otherwise removing a vertex
maximizing outdegree minus indegree; it runs in $O(m)$ time and is widely used as a fast reference.
More recently, Hecht, Gonciarz, and Horv\'at \cite{HGH21} introduce \textsc{TIGHT}, a universal
heuristic for (weighted) FAS based on \emph{tight localizations} that target nearly isolated cyclic
structures; empirically, \textsc{TIGHT} substantially improves upon \textsc{GR} while remaining
practical on large sparse graphs. Cavallaro and Cutello \cite{CC25} propose \textsc{WMSF}, which
removes arcs according to two weight-based orderings and then applies add-back minimization and a
stabilization step; they report that \textsc{WMSF} improves over \textsc{GR} and is competitive with
\textsc{TIGHT} on their benchmark suite, with all instances finishing in seconds except
\texttt{s38584}, which required on the order of tens of minutes.

\paragraph{Tournament-specific approximation, local improvement, and parameterized algorithms.}
In the dense tournament setting, several works study WFAS via approximation guarantees and local
improvement under probability constraints ($w_{uv}+w_{vu}=1
```

## 31. Subsection: Contributions and organization

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 1490 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Contributions and organization}
\label{sec:intro-contrib}

\paragraph{Contributions.}
We introduce \textbf{LR-TA} (Local-Ratio with Topological Add-Back), a practical two-phase heuristic for
computing low-weight feedback arc sets and high-quality vertex orderings on large directed weighted
graphs. The method (i) performs local-ratio cycle reductions on an \emph{active-edge} subgraph until it
becomes acyclic, and (ii) minimizes the removed set via a heavy-first add-back procedure guided by a
maintained topological order with rank-window reachability tests. We further describe an
engineering-oriented implementation that avoids adjacency rebuilds and keeps updates $O(1)$ per edge
deactivation.

For empirical comparison, we evaluate on the 33 benchmark instances used in \cite{CC25}, reporting
backward weight and end-to-end runtime, and we provide an independent implementation of WMSF from
\cite{CC25} (since no code is publicly available) to support reproducibility. Our code and scripts are
available at \url{https://github.com/SoroushVahidi/weighted-minfas-local-ratio}.

\paragraph{Organization.}
Section~\ref{sec:framework} presents LR-TA and its implementation details. Section~\ref{sec:exp-setup}
describes the experimental setup, and Section~\ref{sec:results-standard} reports results on standard
benchmarks. Section~\ref{sec:conclusions} concludes and discusses limitations and future directions.


% ============================================================
```

## 32. Section: Proposed Method: Local-Ratio with Topological Add-Back (LR-TA)

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 72 chars
- Recommendation: Potentially reusable, but must be synchronized with current repository code.

Snippet:

```tex
\section{Proposed Method: Local-Ratio with Topological Add-Back (LR-TA)}
```

## 33. Subsection: Definitions and notation

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 2996 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Definitions and notation}
\label{sec:defs-notation}

We consider a directed weighted graph $G=(V,A,w)$, where $V$ is the set of vertices, $A\subseteq V\times V$
is the set of directed arcs, and $w:A\to\mathbb{R}_{>0}$ assigns a positive weight to each arc.\footnote{If
the input contains parallel arcs with the same ordered pair $(u,v)$, we optionally aggregate them into a
single arc with weight equal to the sum of their weights; see Section~\ref{sec:exp-setup}.}
We write an arc $e\in A$ as $e=(u,v)$ with tail $u$ and head $v$.

\paragraph{Vertex orderings and backward weight.}
A (total) vertex ordering is a bijection $\pi:V\to\{1,\dots,|V|\}$. For an arc $(u,v)$, we say it is
\emph{forward} under $\pi$ if $\pi(u)<\pi(v)$ and \emph{backward} otherwise. The \emph{backward weight}
of $\pi$ is
\begin{equation}\label{eq:BW-def}
\mathrm{BW}(\pi)\;=\;\sum_{(u,v)\in A:\,\pi(u)>\pi(v)} w(u,v),
\end{equation}
which is the objective minimized by the weighted feedback arc set problem.

\paragraph{Weighted feedback arc set (WFAS).}
A set of arcs $F\subseteq A$ is a \emph{feedback arc set} if removing $F$ makes the graph acyclic, i.e.,
the subgraph $(V,A\setminus F)$ is a DAG. In the weighted setting, the cost of $F$ is
\[
w(F)=\sum_{e\in F} w(e),
\]
and the \emph{weighted feedback arc set (WFAS)} problem asks for a feedback arc set of minimum cost.
Equivalently, the problem can be expressed as finding an ordering $\pi$ minimizing $\mathrm{BW}(\pi)$
in \eqref{eq:BW-def}; for any ordering $\pi$, the set of backward arcs
$F_\pi=\{(u,v)\in A:\pi(u)>\pi(v)\}$ is a feedback arc set and has weight $w(F_\pi)=\mathrm{BW}(\pi)$.
Conversely, any DAG admits a topological ordering whose backward weight equals the weight of the arcs
removed to obtain the DAG.

\paragraph{Directed cycles, SCCs, and DAGs.}
A (simple) directed cycle is a sequence of distinct vertices
$v_0,v_1,\dots,v_{k-1}$ with $k\ge 2$ such that $(v_i,v_{(i+1)\bmod k})\in A$ for all $i$.
A directed graph is acyclic if it contains no directed cycle; such a graph is a directed acyclic graph
(DAG) and admits a topological ordering. A \emph{strongly connected component} (SCC) is a maximal vertex
subset $S\subseteq V$ such that every pair of vertices in $S$ is mutually reachable by directed paths.
The SCC condensation of $G$ is always a DAG.

\paragraph{Weights and originals.}
When an algorithm performs weight reductions, we distinguish between the original input weights
$w_0(e)$ and the current (possibly reduc
```

## 34. Subsection: Framework overview

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 3487 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Framework overview}\label{sec:framework}

We consider a directed weighted graph $G=(V,A,w)$ and seek a low-cost weighted feedback arc set (WFAS), i.e., a subset $F\subseteq A$ whose removal makes the graph acyclic while minimizing $\sum_{e\in F} w(e)$. Equivalently, we aim to compute a vertex ordering (ranking) $\pi:V\to\{1,\dots,|V|\}$ that minimizes the total weight of \emph{backward} arcs,
\begin{equation}\label{eq:backward-weight}
\mathrm{BW}(\pi)\;=\;\sum_{(u,v)\in A:\;\pi(u)>\pi(v)} w(u,v),
\end{equation}
since removing the backward arcs of any ordering yields an acyclic subgraph.

Our method follows a two-phase template inspired by the local-ratio approach for feedback arc set problems \cite{DF03}, but is engineered to be practical on large sparse instances. The algorithm maintains an \emph{active} subgraph using an edge-ID representation with an ``active'' indicator per arc. Parallel arcs (if present in the input) are aggregated so that each ordered pair $(u,v)$ appears at most once with weight equal to the sum of its parallel weights; this reduces both memory and redundant work in subsequent phases.

\paragraph{Phase I: Local-ratio cycle reduction.}
Starting from the full graph, we repeatedly identify a directed cycle $C$ in the current active subgraph. Let
\begin{equation}\label{eq:epsilon-cycle}
\varepsilon \;=\; \min_{e\in C} w(e).
\end{equation}
We decrease the weight of every arc on the cycle by $\varepsilon$, i.e., $w(e)\leftarrow w(e)-\varepsilon$ for all $e\in C$. At least one arc on $C$ becomes \emph{tight} (weight $0$) and is removed from the active subgraph and recorded in a candidate set $R$ of removed arcs. This is the characteristic local-ratio step: by charging the same $\varepsilon$ across all edges of a cycle, the algorithm forces progress by eliminating at least one edge per iteration while preserving a decomposition that supports approximation-style reasoning \cite{DF03}. Phase~I terminates when the active subgraph contains no directed cycle, i.e., when it is a DAG.

\paragraph{Phase II: Topological add-back minimization.}
Phase~I may remove arcs that are not strictly necessary to break all cycles. In Phase~II we therefore attempt to \emph{reinsert} arcs from $R$ back into the current DAG while maintaining acyclicity, producing a smaller final WFAS. We process removed arcs in nonincreasing order of their \emph{original} weights (heavy-first). For each candidate arc $e=(u,v)$, we test whether adding $e$ would create a
```

## 35. Subsection: Phase I: Local-ratio cycle reduction

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 2996 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Phase I: Local-ratio cycle reduction}\label{sec:phase1}

Phase~I iteratively reduces arc weights along directed cycles until the active subgraph becomes acyclic. The procedure is based on the local-ratio framework for feedback arc set problems \cite{DF03}, but we implement it using an explicit \emph{active-edge} representation to avoid expensive graph rebuilds.

\paragraph{Active-edge representation.}
Each arc $e\in A$ is assigned an edge identifier $\mathrm{id}(e)\in\{1,\dots,m\}$, and we store its endpoints and weights in arrays. We maintain a Boolean flag $\mathrm{active}[e]$ indicating whether $e$ is currently present in the active subgraph. Adjacency lists are built once as lists of outgoing edge-IDs per tail vertex. During the algorithm we never delete items from adjacency lists; instead, we skip inactive edges when scanning outgoing edges. This design keeps updates $O(1)$ per edge deactivation and makes the main cost dominated by cycle detection.

\paragraph{Cycle detection.}
At each iteration we search the active subgraph for any directed cycle. We use a depth-first search (DFS) over vertices restricted to active edges. Let $\mathrm{parV}[v]$ denote the parent vertex of $v$ in the DFS tree and $\mathrm{parE}[v]$ the parent edge that discovered $v$. We also maintain a tri-color visitation scheme:
\[
\mathrm{state}(v)\in\{0,1,2\}
\]
for unvisited, in-progress (on recursion stack), and finished vertices, respectively. When exploring an active edge $(x,y)$, if $\mathrm{state}(y)=1$ then we have found a back-edge and can reconstruct a directed cycle $C$ by following parent pointers from $x$ back to $y$ and adding $(x,y)$. The search stops immediately upon finding one cycle; Phase~I does not require a minimum-weight cycle.

\paragraph{Local-ratio reduction and edge elimination.}
Given a detected directed cycle $C$, we compute
\begin{equation}\label{eq:phase1-eps}
\varepsilon \;=\; \min_{e\in C} w(e).
\end{equation}
We then apply the local-ratio reduction
\begin{equation}\label{eq:phase1-reduce}
w(e)\;\leftarrow\;w(e)-\varepsilon \qquad \forall\, e\in C.
\end{equation}
At least one edge in $C$ becomes tight. Due to floating-point arithmetic (and aggregated weights), we treat an edge as tight if $w(e)\le \tau$ for a small tolerance $\tau>0$. Every tight edge is deactivated (set $\mathrm{active}[e]=\texttt{false}$) and appended to a list $R$ of removed edges, which forms a \emph{candidate} WFAS to be minimized later in Phase~II. We emphasize tha
```

## 36. Subsection: Phase II: Topological add-back minimization

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 3609 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Phase II: Topological add-back minimization}\label{sec:phase2}

Phase~I produces a set $R$ of removed arcs whose deletion makes the remaining active subgraph acyclic. However, $R$ is not necessarily minimal (or near-minimal) with respect to total removed weight, because some removed arcs may be redundant once other arcs have been removed. Phase~II therefore attempts to \emph{reinsert} arcs from $R$ back into the current DAG while preserving acyclicity. The final WFAS is the subset of $R$ that cannot be reinserted.

\paragraph{Reinsertion order.}
Let $w_0(e)$ denote the \emph{original} weight of arc $e$ before any local-ratio reductions. We process arcs in $R$ in nonincreasing order of $w_0(e)$ (heavy-first). Intuitively, this prioritizes reinserting high-weight arcs and keeping low-weight arcs in the WFAS, which tends to reduce the total removed weight. A similar principle (ordering by weight in minimization/reinsertion) is suggested within the local-ratio framework \cite{DF03}.

\paragraph{Topological order and constant-time acceptance.}
Let $G_{\mathrm{DAG}}=(V,A_{\mathrm{act}})$ be the current active subgraph after Phase~I and after any accepted reinsertions so far. Since $G_{\mathrm{DAG}}$ is acyclic, it admits a topological ordering. We maintain a topological order $\pi$ and its rank array $\mathrm{rank}(\cdot)$ such that
\begin{equation}\label{eq:topo-property}
(u,v)\in A_{\mathrm{act}} \;\Longrightarrow\; \mathrm{rank}(u) < \mathrm{rank}(v).
\end{equation}
Consider a candidate arc $e=(u,v)\in R$ to be reinserted. If $\mathrm{rank}(u) < \mathrm{rank}(v)$, then adding $(u,v)$ is consistent with the current topological order and cannot create a directed cycle; therefore we accept the reinsertion immediately in $O(1)$ time.

\paragraph{Cycle test for backward candidates.}
If $\mathrm{rank}(u) \ge \mathrm{rank}(v)$, adding $(u,v)$ \emph{may} create a cycle. In a DAG, adding $(u,v)$ creates a cycle if and only if there is already a directed path from $v$ to $u$ in $G_{\mathrm{DAG}}$. Thus we perform a reachability test:
\begin{equation}\label{eq:reachability-condition}
(u,v)\ \text{creates a cycle} \;\Longleftrightarrow\; v \leadsto u \ \text{in}\ G_{\mathrm{DAG}}.
\end{equation}
We implement this test using a DFS/BFS from $v$ over currently active edges. To reduce work, we exploit the current topological ranks: any path from $v$ to $u$ must move forward in rank, hence it must stay within the rank interval $[\mathrm{rank}(v),\,\mathrm{rank}(u)
```

## 37. Subsection: Complexity and implementation notes

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 3733 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Complexity and implementation notes}\label{sec:complexity}

We summarize the main computational costs of the proposed LR-TA framework and highlight the implementation choices that determine practical performance.

\paragraph{Preprocessing and representation.}
After reading the input, we optionally aggregate parallel arcs so that each ordered pair $(u,v)$ appears at most once with weight equal to the sum of its parallel weights. Building the edge-ID arrays and outgoing adjacency lists takes
\begin{equation}\label{eq:prep-time}
O(|V|+|A|).
\end{equation}
Throughout the algorithm, adjacency lists are never rebuilt; deactivating an arc is implemented by flipping a Boolean flag $\mathrm{active}[e]$ in $O(1)$ time.

\paragraph{Phase I complexity.}
Each iteration of Phase~I consists of (i) finding a directed cycle in the current active subgraph and (ii) applying a local-ratio weight reduction on the cycle and deactivating newly tight arcs. A DFS that scans outgoing adjacency lists and skips inactive arcs runs in
\begin{equation}\label{eq:phase1-dfs}
O(|V|+|A|)\quad\text{time in the worst case}.
\end{equation}
The local-ratio update on a cycle $C$ requires scanning the edges of $C$ to compute $\varepsilon$ and then reducing weights, which costs
\begin{equation}\label{eq:phase1-cycle-update}
O(|C|).
\end{equation}
At least one arc becomes tight and is deactivated per iteration. Thus, the number of iterations is at most $|A|$, yielding the conservative upper bound
\begin{equation}\label{eq:phase1-worst}
O\!\bigl(|A|\,(|V|+|A|)\bigr)
\end{equation}
for Phase~I. In practice, multiple arcs can become tight in one iteration and the active graph shrinks quickly, so the observed running time is typically much smaller than the worst-case bound.

\paragraph{Phase II complexity.}
Let $r=|R|$ be the number of arcs removed in Phase~I. Phase~II processes these arcs in sorted order, which costs
\begin{equation}\label{eq:sort-removed}
O(r\log r).
\end{equation}
For each candidate arc $(u,v)$, if it is forward with respect to the current topological ranks, reinsertion is accepted in $O(1)$. Otherwise, we perform a reachability search from $v$ restricted to the rank window up to $\mathrm{rank}(u)$, which in the worst case costs
\begin{equation}\label{eq:reachability-cost}
O(|V|+|A|).
\end{equation}
Whenever a backward candidate is accepted, we recompute a topological ordering, which also costs
\begin{equation}\label{eq:toposort-cost}
O(|V|+|A|).
\end{equation}
Consequen
```

## 38. Section: Computational Experiments

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 35 chars
- Recommendation: Likely obsolete except wording/structure; experiments must be replaced by EXP1b-EXP5.

Snippet:

```tex
\section{Computational Experiments}
```

## 39. Subsection: Experimental setup

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 3091 chars
- Recommendation: Likely obsolete except wording/structure; experiments must be replaced by EXP1b-EXP5.

Snippet:

```tex
\subsection{Experimental setup}
\label{sec:exp-setup}

\paragraph{Benchmark instances.}
We evaluate our method on the weighted directed graph instances from the \texttt{graph-benchmarks} repository.\footnote{\texttt{https://github.com/alidasdan/graph-benchmarks}} To ensure strictly deterministic behavior, we preprocess each instance by aggregating parallel arcs: multiple arcs $(u,v)$ are replaced by a single arc with weight equal to the sum of their weights. Vertices are mapped to indices deterministically by sorting their string identifiers lexicographically, and arcs are processed in lexicographic order of their endpoints.

\paragraph{Objective and reporting.}
For each instance, we report (i) the \emph{backward weight} (BW) of the computed ranking (Eq.~\ref{eq:backward-weight}), and (ii) the end-to-end wall-clock runtime in seconds.

\paragraph{Methods compared.}
We compare the following approaches:
\begin{itemize}
    \item \textbf{TIGHT}: The best-known heuristic from \cite{HGH21}, which iteratively resolves "tight" cycles. We list the backward weights reported for this method in \cite{CC25}.
    \item \textbf{WMSF-reported}: The Weighted Minimal Stable Feedback (WMSF) heuristic proposed by Cavallaro and Cutello \cite{CC25}. We list the results as reported in their paper.
    \item \textbf{WMSF-impl}: Our independent, faithful implementation of the WMSF heuristic \cite{CC25}. Since the authors did not provide code, we implemented the full pipeline described in their work: \textsc{RemoveArcs} $\to$ \textsc{Minimize} $\to$ \textsc{Stabilize} $\to$ \textsc{Minimize}. In the \textsc{Stabilize} phase, we enforce the limit of $\log_2|V|$ iterations as specified in \cite{CC25}. For the arc removal order, we implement both strategies defined in \cite{CC25}:
    \begin{itemize}
        \item \emph{L1}: Increasing order of weight $w(u,v)$.
        \item \emph{L2}: Increasing order of the ratio $w(u,v) / (W_{in}(u) + W_{out}(v))$, where $W_{in}$ and $W_{out}$ are total weighted degrees.
    \end{itemize}
    For instances forming a single strongly connected component (SCC), we run both L1 and L2 and report the result with the lower backward weight.
    \item \textbf{Ours (LR-TA)}: The proposed Local-Ratio with Topological Add-Back method.
\end{itemize}

\paragraph{Runtime measurement and implementation details.}
All algorithms (WMSF-impl and LR-TA) are implemented in Python 3.11.14 using NumPy 2.3.5. To handle large sparse graphs efficiently without hitting recur
```

## 40. Subsection: Results on standard benchmarks

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 7970 chars
- Recommendation: Likely obsolete except wording/structure; experiments must be replaced by EXP1b-EXP5.

Snippet:

```tex
\subsection{Results on standard benchmarks}
\label{sec:results-standard}

Tables~\ref{tab:results_scc} and~\ref{tab:results_multiscc} summarize results on the 33 benchmark
instances used in \cite{CC25}. Following \cite{CC25}, we split the suite into (i) instances whose full
graph is strongly connected (Table~\ref{tab:results_scc}) and (ii) instances with more than one SCC
(Table~\ref{tab:results_multiscc}). Each row corresponds to one dataset (\textbf{Code}), and the
column $|V|-|A|$ reports the number of vertices $|V|$ and arcs $|A|$ after our deterministic
preprocessing (including aggregation of parallel arcs). All objective values shown are the backward
weight (BW) of the returned ordering (Eq.~\eqref{eq:backward-weight}); lower is better.

\paragraph{Meaning of the columns.}
\textbf{Tight} is the BW for \textsc{TIGHT} originally from \cite{HGH21}, as reported in \cite{CC25}.
\textbf{WMSF} is the BW reported for the WMSF heuristic in \cite{CC25}. Since the authors of \cite{CC25}
have not provided code, we additionally report \textbf{WMSF-impl}, our independent implementation of
their described pipeline, along with its runtime (\textbf{WMSF-impl time}). \textbf{Ours} and
\textbf{Ours time} are the BW and end-to-end runtime of our LR-TA implementation. All code (LR-TA and
our WMSF reimplementation) and scripts to reproduce the tables are available at
\url{https://github.com/SoroushVahidi/weighted-minfas-local-ratio}.

\paragraph{About the GR baseline.}
In addition to \textsc{TIGHT} and WMSF, \cite{CC25} also compares against the greedy heuristic
\textsc{GR} of Eades, Lin, and Smyth~\cite{ELS93}. We do not include GR in our tables because its
solutions are consistently much worse than both \textsc{TIGHT} and WMSF on this benchmark suite, and
therefore it is not a competitive reference point for the accuracy regime targeted here.

\paragraph{Quality relative to reported baselines.}
Against the strongest reported baseline (\textbf{Tight}), LR-TA improves BW on 6 instances, ties on
16, and is worse on 11. Over the full suite, the average ratio
$\mathrm{BW}(\text{Ours})/\mathrm{BW}(\text{Tight})$ is $0.997$ (geometric mean $0.996$), indicating
that LR-TA is slightly better than \textsc{TIGHT} overall. The largest improvement over \textsc{TIGHT}
occurs on \texttt{parker1986} (ratio $0.918$), while the largest degradation occurs on \texttt{mm9a}
(ratio $1.050$).

Comparing to \textbf{WMSF} as reported in \cite{CC25}, LR-TA is better on 17 instances, ties on 9, a
```

## 41. Subsection: Ablations and sensitivity analysis

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 49 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Ablations and sensitivity analysis}
%
```

## 42. Subsection: Scalability and large-instance study

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 113 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Scalability and large-instance study}

% ============================================================
```

## 43. Section: Conclusions and Future Work

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 61 chars
- Recommendation: Review

Snippet:

```tex
\section{Conclusions and Future Work}
\label{sec:conclusions}
```

## 44. Subsection: Summary of findings

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 1356 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Summary of findings}
\label{sec:conclusion-summary}

This paper presented LR-TA, a simple two-phase heuristic for the weighted feedback arc set problem
that combines local-ratio cycle reductions with a topological-order--guided add-back minimization.
The key goal was practical performance: low backward weight together with fast end-to-end runtimes
on standard weighted benchmarks.

On the 33 benchmark instances used in \cite{CC25} (Tables~1--2), LR-TA is consistently competitive
with the best published results reported in \cite{CC25} and the \textsc{TIGHT} baseline from
\cite{HGH21} (as reported in \cite{CC25}). In particular, LR-TA improves or matches \textsc{TIGHT}
on the majority of instances, and improves \textbf{WMSF-reported} on more instances than it loses,
while remaining fast across the suite. The runtime profile is especially favorable on the largest
strongly-connected benchmark \texttt{s38584}: \cite{CC25} reports this as the clear outlier for WMSF,
requiring ``almost about 20 minutes,'' while LR-TA completes in seconds on the same instance under
our measurement protocol.

To the best of our knowledge, these experiments provide the strongest overall empirical performance
(backward-weight accuracy combined with end-to-end runtime) reported for this specific benchmark
suite under a reproducible single-thread setup.
```

## 45. Subsection: Limitations

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 964 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Limitations}
\label{sec:conclusion-limitations}

Our study has several limitations. First, the empirical evaluation is restricted to the benchmark set
used in \cite{CC25}; while this suite is a standard reference for recent work, it does not cover very
large graphs with millions of arcs or diverse structural families (e.g., dense graphs, heavy-tailed
degree distributions, or application-specific networks). Second, while we report results for
\textbf{WMSF-reported} from \cite{CC25} and also provide \textbf{WMSF-impl} (our independent
implementation), the absence of an official code release for \cite{CC25} means that small
implementation-level differences could affect instance-level comparisons. Third, LR-TA is a heuristic:
its Phase~I cycle selection is not optimized (we stop at the first detected cycle), and Phase~II
currently recomputes a full topological order after accepting a backward candidate, which may be
suboptimal on some graphs.
```

## 46. Subsection: Future directions

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 1768 chars
- Recommendation: Review

Snippet:

```tex
\subsection{Future directions}
\label{sec:conclusion-future}

A first direction is to evaluate LR-TA on substantially larger datasets (including the larger
instances available in the same benchmark repository and additional public graph collections) to
characterize scaling behavior and memory usage beyond the 33-instance suite.

A second direction is \textbf{parallelization}. Both phases contain opportunities for parallel work:
for example, Phase~I can potentially search for cycles (or candidate cycles) in parallel across
different start vertices or SCCs, and Phase~II reachability tests for rejected candidates could be
batched or parallelized under careful synchronization. Assessing which parts parallelize cleanly
without losing determinism is an important next step.

Finally, we plan to explore algorithmic refinements that preserve the simplicity of LR-TA while
reducing traversal overhead, such as more informative cycle selection policies in Phase~I (to trigger
more tight edges per iteration), incremental maintenance of topological order in Phase~II (to avoid
full recomputation after every accepted backward edge), and additional pruning rules for reachability
tests.




%\begin{acknowledgements}
%If you'd like to thank anyone, place your comments here
%and remove the percent signs.
%\end{acknowledgements}

% BibTeX users please use one of
%\bibliographystyle{spbasic}      % basic style, author-year citations
%\bibliographystyle{spmpsci}      % mathematics and physical sciences
%\bibliographystyle{spphys}       % APS-like style for physics
%\bibliography{}   % name your BibTeX data base

% Non-BibTeX users please use
\bibliographystyle{spbasic}   % author–year Springer style
\bibliography{references}     % your .bib file name without .bib
```

## 47. Section: Statements and Declarations

- Source: `paper/source_material/extracted_archives/Fast_Local_Ratio_Cycle_Reduction_with_Topological_Add_Back_for_Weighted_Feedback_Arc_Sets_JOCO/main.tex`
- Length: 1083 chars
- Recommendation: Review

Snippet:

```tex
\section*{Statements and Declarations}

\paragraph{Funding.}
The author declares that no funds, grants, or other support were received during the preparation of this manuscript.

\paragraph{Competing Interests.}
The author has no relevant financial or non-financial interests to disclose.

\paragraph{Data Availability.}
The datasets used in this study are publicly available at \url{https://github.com/alidasdan/graph-benchmarks}.

\paragraph{Code Availability.}
The implementation and scripts are available at \url{https://github.com/SoroushVahidi/weighted-minfas-local-ratio}.

\paragraph{Use of large language models.}
Large language models (LLMs), including ChatGPT and Google Gemini, were used to assist with improving the presentation of the manuscript (paraphrasing and rewriting selected passages) and with drafting portions of the implementation. The author verified the correctness of all technical content and software artifacts and remains fully accountable for the work, including the final text, code, and reported results.



\end{document}
% end of file template.tex
```
