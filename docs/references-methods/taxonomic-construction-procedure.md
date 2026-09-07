---
tags:
  - reference
index: "[References and methods](_index.md)"
aliases:
  - Taxonomic construction procedure
---
# Taxonomic construction procedure

> [!QUESTION] Goal: Is there a systematic domain-independent methodology to construct taxonomies?

## Overview

For qualitative taxonomies, the goal is to achieve:

> complete discernibility + minimality + explicit dependency structure

> [!WARNING] Minimality alone is vacuous
> To discriminate all pairs among $|U| = n$ objects, it is sufficient to have $\lceil \log_2 n \rceil$ _arbitrary_ binary attributes. Discrimination with minimal cardinality is therefore trivially achievable and carries no epistemic content. The operative desideratum is not minimality but **projectibility** — the capacity of the attributes to classify objects not yet in the universe $U$. This is Goodman's problem (_Fact, Fiction and Forecast_, 1955) and is demonstrably underdetermined by any finite universe $U$.

Once a sufficiently rich **candidate vocabulary of distinctions** has been elicited, there exist rigorous algorithmic procedures for:

1. determining which attributes actually discriminate objects;
2. removing redundant attributes;
3. finding minimal subsets preserving the distinctions induced by the full set;
4. identifying dependencies between attributes;
5. deriving non-retained attributes from retained ones when the dependency is logically supported.

The irreducibly domain-dependent component is deciding **which distinctions count as meaningful**. No mathematical reduction can determine that without an externally supplied semantic objective.

However, there is no domain-independent algorithm for:

- generating the initial set of candidate attributes ("conceptual dimensions") — which is provably not determined by the items alone and their arbitrary verbal descriptions;
- recovering a *unique*, *canonical* minimal "basis of attributes" under the discrimination invariant — which is possible only under the

## Operational pipeline

Thus, the desired methodology exists, but it is naturally **hybrid**:

> **qualitative elicitation of candidate distinctions → formal representation → mathematical reduction and dependency analysis.**

1. **Define the universe $U$.** Specify precisely which objects the taxonomy must distinguish and for what purpose.
2. **Elicit candidate distinctions.** Systematically compare pairs/triads of maximally diverse objects and formulate the properties responsible for relevant differences ([Kelly's *triadic elicitation*](#^kelly-triadic-elicitation)).

==TODO: Complete the procedure by adding from point 3 a uniform sequence from the two versions below. Merge the steps that are identical, preserving the details from both versions. Include at the correct position the steps that are unique to one version.==
VC:
3. **Structure the descriptive space** with a Guttman **mapping sentence** (facet theory) to make facets and their ranges explicit before tabulation. ==TODO: if this is a distinct step, create a subsection in the "Formal references" section==
4. **Scale** many-valued attributes into a formal context, documenting each scale. ==TODO: if this is a distinct step, create a subsection in the "Formal references" section==
5. **Clarify and reduce** the context (via the method that preserves conceptual structure). Retain the *meet-irreducible* attributes.
6. **Compute the Duquenne–Guigues basis.** Each implication is either an accepted conceptual law or the signal of a missing counterexample item.
7. **Run attribute exploration.** ==TODO: is it a distinct process than the Duquenne–Guigues basis, or the only way to compute it?== The process is interactive, and the expert either validates each implication or supplies a counterexample.
8. **Arbitrate residual competing reducts** by an *external* criterion — minimum description length of corpus plus criterion definitions (Rissanen, 1978), or predictive accuracy on held-out items. Purely internal criteria cannot decide.
9. Where outcomes are at stake rather than mere descriptions, **Quine–McCluskey minimization** over the truth table (Ragin's QCA, 1987) yields the minimal sufficient conjunctions.

VG:
3. **Operationalize attributes.** Convert each distinction into a Boolean, categorical, ordinal, or otherwise explicitly evaluable attribute $a:U\to V_a$.
4. **Construct the object × attribute matrix.** This transforms verbal knowledge into an information system.
5. **Test coverage.** Every pair that should be distinguishable must differ on at least one attribute. Failure means that further elicitation is required.
6. **Compute reducts.** Use Rough Set attribute reduction to find minimal subsets preserving the desired discernibility relation.
7. **Compute dependencies.** Use FCA/attribute exploration to identify implications among attributes and obtain an irredundant implication basis.
8. **Validate externally.** Add difficult/new objects and determine whether the taxonomy still discriminates them. Counterexamples trigger another elicitation–reduction iteration.

## Formal references

- Repertory-grid/contrastive elicitation provides a disciplined mechanism for _discovering candidate attributes_.
- Rough sets provide the formal criterion for _minimal discriminatory attributes_.
- Formal Context Aanalysis provides _logical dependency and derivability_; r

### Discovering initial attributes

^kelly-triadic-elicitation

> [!QUOTE] Kelly's **Repertory Grid / triadic elicitation** (repertory grid, 1955)
> There exists a systematic elicitation technique generates the initial dimensions, to move from un unstructured qualitative description to a formal context. 

The procedure consists of a series of triadic comparisons:

> Present three representative objects, name the property distinguishing one from the other two. Concretely, ask: _In what relevant respect are two alike and different from the third?_

The answer produces a bipolar attribute that is is guaranteed to be discriminating, since it is grounded in actual contrasts among the objects rather than in unconstrained brainstorming. 

Repeating this across strategically chosen triads generates candidate dimensions. 

> [!INFO] Origin and usage
> This procedure is established in Personal Construct Theory and has been used well beyond personality research, including music and complex design spaces (e.g. ["Evaluation of a Positive Youth Development Program Based on the Repertory Grid Test"](https://pmc.ncbi.nlm.nih.gov/articles/PMC3349140/))

For many-valued attributes, the passage to a formal context requires **conceptual scaling** (Ganter & Wille), where every substantive modelling decision is concentrated. No algorithm generates this step. ==TODO: explain==

### Formalizing the context

==FIX: note that G must be replaced by U, M must be replaced by A, so the initial symbols A/A' must change to X, X'==

The framework starts from **collection of objects** $U$ (universe) is described by **attributes** $A$. 

Each attribute $a$ is formally a *function* that maps objects to values in a value set $V_a$:
$$a:U\rightarrow V_a$$

The problem corresponds to a **formal context**:
$$\mathbb{K} = (U, A, I)$$
where:
- $U$ is the set of items, 
- $A$ is the set of candidate attributes, 
- $I \subseteq U \times A$ is the incidence, that is, the set of pairs $(x,a)$ such that object $x$ has attribute $a$.

Any subset of attributes $B\subseteq A$ induces an **indiscernibility relation**: two objects are indistinguishable with respect to the set of attributes $B$ whenever all attributes in $B$ assign them identical values. Formally, the indiscernibility relation is defined as:
$$ 
\operatorname{IND}(B)=\{(x,y)\in U\times U: \forall a\in B, a(x)=a(y)\}
$$
$\operatorname{IND}(B)$ is the set of all pairs of objects that are indiscernible with respect to the attributes in $B$.

Two **derivation operators** are defined: ==TODO: what do they serve to in the process, concretely?==

- For a set of objects $X \subseteq U$, the set of attributes shared by all objects in $X$ is:
$$X' = \{a \in A : \forall x \in X,\ (x,a) \in I\}$$
- For a set of attributes $B \subseteq A$, the set of objects that share all attributes in $B$ is:
$$B' = \{x \in U : \forall a \in B,\ (g,a) \in I\}$$
The pair $(X', B')$ forms a Galois connection; the composites $X \mapsto X''$ and $B \mapsto B''$ are closure operators, and the concept lattice $\underline{\mathfrak{B}}(\mathbb{K})$ is the complete invariant of the description. ==TODO: explain these objets simply and what they serve to.==

> [!WARNING]
> This lattice-theoretic structure ==TODO: what is it, simply?== — a Moore family ==TODO: what is it, simply?== — is the qualitative counterpart of the linear span.
> It is strictly weaker: closure systems are not modular ==TODO: what is modular here, simply?==, admit no complements in general, and support no notion of angle.

Then, two distinct invariants may be preserved, each yielding a reduction method.

### Preserving discernibility (non-unique, NP hard)

^rough-set-theory

> [!QUOTE] **Rough Set Theory** (RST), introduced by Zdzisław Pawlak
> This decomposition method aims to a "minimal" non-redundant set of attributes sufficient to discriminate the items.

The central notion is that of **reduct**:

> A reduct is a **minimal collection of attributes having the same discriminatory power as the complete attribute vocabulary**. 

Formally, a reduct is a subset of attributes $R\subseteq A$, that satisfies:
$$\operatorname{IND}(R)=\operatorname{IND}(A)$$
while no proper subset of $R$ does.
 
> [!WARNING] Non-uniqueness: reducts are generally **multiple and non-isomorphic**.

The intersection of all reducts is the **core**: it contains the attributes that cannot be removed in _any_ reduct. 

Reducts can be identified mechanically by the **Skowron–Rauszer procedure**: ^skowron-rauszer-procedure

1. Construct the discernibility matrix $c_{ij} = \{a \in A : a \text{ separates } x_i, x_j\}$. Each entry $c_{ij}$ contains a set of attributes that discern between objects $x_i$ and $x_j$.
2. Form the discernibility function, a Boolean function over the attributes. It takes in arguments the attributes and outputs whether they form a reduct: ==TODO: explain the steps to compute the value from the arguments.==
$$f = \bigwedge_{i<j} \ \bigvee_{a \in c_{ij}} a$$
3. Convert the discernibility function $f$ into a disjunction of conjunctions of attributes. ==TODO: explain how to construct this disjunction of conjunctions.== Each conjunction is a set of attributes that corresponds to a candidate reduct.
4. The reducts are the prime implicants. ==TODO: what are they?==

> [!WARNING] Complexity
> Computing a minimum-cardinality reduct is **NP-hard** (Wong & Ziarko, 1985): it is not polynomial in the number of attributes, and that the result is not unique. The best that can be done is to enumerate all reducts and select one according to an external criterion.

### Preserving the conceptual structure (canonical)

^formal-concept-analysis

> [!QUOTE] **Formal Concept Analysis (FCA)**, developed by Rudolf Wille and Bernhard Ganter
> This alternative decomposition method aims to preserve the concept lattice $\underline{\mathfrak{B}}(\mathbb{K})$ up to isomorphism. 

The framework starts from objects and attributes and studies their logical structure. It defines **attribute implications**:
$$A\rightarrow B$$
meaning that whenever an object possesses all attributes in $A$, it necessarily possesses those in $B$.

An attribute $a$ is **reducible** iff its extent is an intersection of other attribute extents:
$$\{a\}' = \bigcap_{n \in N} \{n\}', \qquad N \subseteq A \setminus \{a\}$$
==TODO: how does it relate to the implication relations?==

The **reduced context** is obtained by deleting all reducible attributes (after clarification, i.e. merging duplicate rows and columns ==TODO: in what table?==). This reduced context is *unique* up to isomorphism for finite $\mathbb{K}$. The surviving attributes correspond to the **meet-irreducible** elements of the lattice.

> [!WARNING] This method restores canonicity, but "minimality" is with respect to *set inclusion*, not cardinality.

The analysis then constructs an **irredundant implication basis** from which all valid attribute implications can be derived.

The classical **Duquenne–Guigues canonical basis** (1986) provides such a representation. ^duquenne-guigues-canonical-basis
==TODO: how to construct this basis?==
This basis, indexed by pseudo-closed sets, is the **unique basis of minimum cardinality** for the implication theory of $\mathbb{K}$. Every discarded or subsequently proposed attribute $a$ is then accounted for by the derivation $B \to B''$ that entails it.  ==TODO: what does it mean?==

> [!CHECK] Complexity
> This procedure is deterministic, polynomial in $|G|\cdot|M|^2$, and interpretable.

### Exploring attributes

> [!QUOTE] **Attribute Exploration** (Ganter and Obiedkov, 1986)
> This procedure can be seen as a general methodology for acquiring structured conceptual knowledge from qualitative information.

This algorithm is an **interactive procedure**: 

- Candidate implications are systematically presented to a domain expert.
- The expert either validates them or supplies a counterexample.

==TODO: who is the "expert"? does it refer to a human specialist or is it a metaphoric denomination for some oracle / test data set ?==

The process *provably terminates* with a context whose implication theory is complete for the domain. Its guarantee is genuine though relative to the oracle.

## Analogy with decomposition in linear algrebra

> [!WARNING] Analogy with linear algebra is only *partial*

Standard decomposition methods in *linear algebra* (e.g. PCA) differ from *conceptual decomposition* in several respects. The following table summarizes the key differences and structural analogies:

| Linear algebra, PCA                                                                       | Conceptual spaces                                                                      |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Predefined ambient vector space: coordinates already exist numerically                    | No coordinate system a priori                                                          |
| Inner product based on variance, defining the notions of "importance" and "orthogonality" | No canonical metric, no inner product, hence no notion of orthogonality                |
| Canonical basis ==TODO: complete==                                                        | *Implication basis* (i.e. a basis of the _dependencies_) rather than *attribute basis* |
| Linear independence                                                                       | Irreducibility                                                                         |
| Linear combination                                                                        | Intersection of extents                                                                |

**Gärdenfors' theory of conceptual spaces** explicitly treats dimensions as ways in which objects can be judged similar or different, while also emphasizing that dimensions need not be independent: some are _integral_, others _separable_, and empirical dimensions can covary. [Lund University Cognitive Science](https://www.lucs.lu.se/fileadmin/user_upload/project/lucs/PG/pg-2014r.pdf?utm_source=chatgpt.com)

**Numerical decomposition requires axioms that must be tested, not assumed.** The conditions under which a qualitative structure admits an additive representation $\phi(a_1,\dots,a_k) = \sum_i \phi_i(a_i)$, unique up to positive affine transformation, are stated by **additive conjoint measurement** (Krantz, Luce, Suppes & Tversky, _Foundations of Measurement_, vol. I, 1971): independence, the Thomsen condition, restricted solvability, Archimedean axiom. These are empirically falsifiable ordinal conditions. Where they hold, a genuine PCA-like uniqueness obtains; where they fail, no amount of methodological care produces one.

## Principal references

- Kelly, _The Psychology of Personal Constructs_ (1955)
- Pawlak, _Rough Sets_ (Kluwer, 1991) — supplies the complementary theory of reducts and indiscernibility. 
- Andrzej Skowron & Soma Dutta, [*Rough sets: past, present, and future*](https://link.springer.com/article/10.1007/s11047-018-9700-3?)
- Piotr Hońk, [*Attribute reduction: a horizontal data decomposition approach*](https://link.springer.com/article/10.1007/s00500-014-1554-8?)
- Zaineb Chelly Dagdia, Christine Zarges, Gaël Beck, Mustapha Lebbah, [A scalable and effective rough set theory-based approach for big data pre-processing](https://link.springer.com/article/10.1007/s10115-020-01467-y?)
- Ganter & Wille, _[Formal Concept Analysis: Mathematical Foundations](https://www.sciencedirect.com/topics/computer-science/formal-concept-analysis)_ (Springer, 1999)
- Ganter & Obiedkov, _[Conceptual Exploration](https://link.springer.com/book/10.1007/978-3-662-49291-8?)_ — explicitly develops algorithms for conceptual knowledge acquisition and attribute exploration.
- Guigues & Duquenne, _Math. Sci. Hum._ 95 (1986)
- Skowron & Rauszer, in _Intelligent Decision Support_ (1992)
- Krantz, Luce, Suppes & Tversky, _Foundations of Measurement_ I (1971)
- Borg & Shye, _Facet Theory_ (1995)
- Ragin, _The Comparative Method_ (1987)
