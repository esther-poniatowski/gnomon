---
tags:
  - reference
index: "[Methods for taxonomies](_index.md)"
aliases:
  - Taxonomic construction procedure
---
# Taxonomic construction procedure

> [!QUESTION] Goal: Is there a systematic domain-independent methodology to construct taxonomies?

## Overview

For qualitative taxonomies, the goal is to achieve:

> complete discernibility + minimality + explicit dependency structure

Once a sufficiently rich **candidate vocabulary of distinctions** has been elicited, there exist rigorous algorithmic procedures for:

1. determining which attributes ("conceptual dimensions") actually discriminate objects;
2. removing redundant attributes;
3. finding minimal subsets preserving the distinctions induced by the full set;
4. identifying dependencies between attributes;
5. deriving non-retained attributes from retained ones when the dependency is logically supported.

However, there is no domain-independent algorithm for:

- generating the initial set of candidate attributes — which is provably not determined by the items alone and their arbitrary verbal descriptions;
- recovering a *unique*, *canonical* minimal "basis of attributes" under the requirement to preserve only discrimination — it is only possible to achieve a canonical "basis of dependencies" under the requirement to preserve the structure of the conceptual space.

> [!IMPORTANT]
> The irreducibly domain-dependent task is deciding **which distinctions count as meaningful**. No mathematical reduction can determine that without an externally supplied semantic objective.

> [!WARNING] Minimality alone is vacuous
> To discriminate all pairs among $n$ objects, it is sufficient to have $\lceil \log_2 n \rceil$ _arbitrary_ binary attributes. Discrimination with minimal cardinality is therefore *trivially achievable* and carries *no epistemic content*. 
> The operative desideratum is not minimality but **projectibility** — the capacity of the attributes to classify objects not yet in the universe (i.e. the set of objects). This is Goodman's problem (_Fact, Fiction, and Forecast_, 1955) and is demonstrably underdetermined by any finite universe.

## Operational pipeline

The methodology exists, but it is naturally **hybrid**:

> **qualitative elicitation of candidate distinctions → formal representation → mathematical reduction and dependency analysis**

1. **Define the universe $U$.** Specify precisely which objects the taxonomy must distinguish and for what purpose.
2. **Elicit candidate distinctions.** Systematically compare pairs/triads of maximally diverse objects and formulate the properties responsible for relevant differences ([Kelly's *triadic elicitation*](#^kelly-triadic-elicitation)).
3. **Structure the descriptive space.** Before any item is scored, a mapping sentence declares the design of the description: its population, its content facets, and its range of values ([facets and their ranges are fixed a priori](#^guttman-mapping-sentence)). ==TODO (resolved — distinct step, documented under "Structuring the descriptive space"): if this is a distinct step, create a subsection in the "Formal references" section==
4. **Operationalize attributes.** Each elicited distinction becomes an explicitly evaluable function $a:U\to V_a$, whose value set is Boolean, categorical, or ordinal. A distinction that no procedure evaluates on a new item is not yet an attribute.
5. **Construct the object × attribute matrix.** Evaluating every attribute on every item turns the verbal descriptions into an information system, the table on which every later reduction operates.
6. **Test coverage.** Every pair of items that must be distinguishable has to differ on at least one attribute. A pair that does not differ reveals an incomplete vocabulary, and the procedure returns to eliciting distinctions.
7. **Scale the many-valued attributes.** Each attribute carrying more than two values is replaced by the binary columns of a scale, chosen and documented attribute by attribute ([the scale decides which distinctions reach the lattice](#^conceptual-scaling)). The one-valued formal context produced here is what the dependency analysis requires. ==TODO (resolved — distinct step, documented under "Scaling many-valued attributes"): if this is a distinct step, create a subsection in the "Formal references" section==
8. **Compute reducts.** Rough-set reduction returns the minimal attribute subsets preserving the indiscernibility relation of the full vocabulary ([reducts are the prime implicants of the discernibility function](#^rough-set-theory)). The step ends with a family of candidates rather than one answer, since the reducts are generally multiple and non-isomorphic.
9. **Clarify and reduce the context.** Duplicate rows and columns are merged, then every attribute whose extent is an intersection of other extents is deleted ([the reduction preserves the concept lattice](#^formal-concept-analysis)). The surviving attributes are the *meet-irreducible* ones, and the reduced context is unique up to isomorphism.
10. **Compute the Duquenne–Guigues basis.** One canonical set of implications, of minimum cardinality, generates every implication valid in the context ([the basis is indexed by the pseudo-closed sets](#^duquenne-guigues-canonical-basis)). Each implication is either an accepted conceptual law or the signal of a missing counterexample item.
11. **Run attribute exploration.** The procedure applies when the items collected so far form a sample rather than the whole domain. Each implication of the current basis is submitted to the expert, who either validates it as a law of the domain or supplies a counterexample ([the exploration builds the context whose basis is sought](#^attribute-exploration)). The counterexample item enters the context, and the basis is recomputed on the enlarged context. ==TODO (resolved — a distinct process, and not the only route to the basis): is it a distinct process than the Duquenne–Guigues basis, or the only way to compute it?==
12. **Arbitrate residual competing reducts** by an *external* criterion — minimum description length of corpus plus criterion definitions (Rissanen, 1978), or predictive accuracy on held-out items. Purely internal criteria cannot decide, since every reduct carries the same discriminatory power by construction. The criterion applies only once the implication basis exists, because the description length of a reduct includes the derivations that recover the attributes it discards.
13. **Validate externally.** Difficult and previously unseen items are added to the universe, and the retained attributes must still discriminate them. Each counterexample triggers another elicitation–reduction iteration.
14. **Minimize the conditions for an outcome.** Where outcomes are at stake rather than mere descriptions, one attribute is designated as the outcome, and Quine–McCluskey minimization over the truth table yields the minimal sufficient conjunctions ([each disjunct of the minimal cover is one path to the outcome](#^quine-mccluskey-qca)). ==TODO (resolved — distinct step, documented under "Minimizing conditions for an outcome"): if this is a distinct step, create a subsection in the "Formal references" section==

==TODO (resolved by the sequence above, pending review — the two source variants were consumed by the merge and deleted; they remain in the history at commit `a80c7d4`): Complete the procedure by adding from point 3 a uniform sequence from the two versions below. Merge the steps that are identical, preserving the details from both versions. Include at the correct position the steps that are unique to one version.==

## Formal references

The whole process involves several reference methodologies / theories:

- [Repertory-grid/contrastive elicitation](#^kelly-triadic-elicitation) provides a disciplined mechanism for _discovering candidate attributes_.
- [Facet theory's mapping sentence](#^guttman-mapping-sentence) provides the a priori _declaration of the facets and their ranges_.
- [Conceptual scaling](#^conceptual-scaling) provides the _passage from many-valued data to a one-valued context_.
- [Rough sets](#^rough-set-theory) provide the formal criterion for _minimal discriminatory attributes_.
- [Formal Concept Analysis](#^formal-concept-analysis) provides _logical dependency and derivability_.
- [Attribute exploration](#^attribute-exploration) provides the _completion of an incomplete universe of items_.
- [Quine–McCluskey minimization](#^quine-mccluskey-qca) provides the _minimal sufficient conditions for a designated outcome_.

### Discovering initial attributes

^kelly-triadic-elicitation

> [!QUOTE] Kelly's **repertory grid** and **triadic elicitation** (1955)
> A systematic elicitation technique generates the initial dimensions, moving an unstructured qualitative description toward a formal context.

The procedure consists of a series of triadic comparisons:

> Present three representative objects, name the property distinguishing one from the other two. Concretely, ask: _In what relevant respect are two alike and different from the third?_

The answer produces a bipolar attribute that is guaranteed to be discriminating, since it is grounded in actual contrasts among the objects rather than in unconstrained brainstorming. 

Repeating this across strategically chosen triads generates candidate dimensions. 

> [!INFO] Origin and usage
> This procedure is established in Personal Construct Theory and has been used well beyond personality research, from [measuring how participants' self-identity shifted over a youth development program](https://pmc.ncbi.nlm.nih.gov/articles/PMC3349140/) to [eliciting the constructs listeners apply in sound design](https://dl.acm.org/doi/10.1145/1859799.1859807) and [mapping the design space of aesthetics](https://arxiv.org/abs/2008.07862).

For many-valued attributes, the passage to a formal context requires [conceptual scaling](#^conceptual-scaling), where every substantive modelling decision is concentrated. ==TODO (resolved under "Scaling many-valued attributes"): explain==

### Structuring the descriptive space

^guttman-mapping-sentence

> [!QUOTE] **Mapping sentence** (Guttman's facet theory; Borg & Shye, 1995)
> A sentence template declares the population observed, the facets of content, and the range of admissible values, before any item is scored.

Triadic elicitation returns one construct at a time and leaves unfixed which respects the description as a whole must cover. The mapping sentence fixes them in advance: the whole descriptive design is declared in one template, ahead of any tabulation.

Each slot of the template is a **facet**, a set whose elements are the values admissible in that slot. Three kinds of facet compose the sentence:

- the **population facet** fixes which items are observed;
- the **content facets** fix the respects in which each item is described;
- the **range facet** fixes the values an observation may take, together with the unit and the resolution recorded.

Selecting one element from each facet yields one admissible profile, read off as an ordinary sentence. The mapping sentence therefore fixes, a priori, the Cartesian product of facets that the items are expected to populate, whereas the table records only the profiles actually realized. Comparing the two exposes the profiles declared admissible and never observed. Those unrealized profiles are what the interactive completion of the implication basis probes, and what Boolean minimization treats as remainders.

The mapping sentence also prevents two errors that a completed table cannot expose: naming a value where an attribute is intended (a class of "red items" instead of a facet of colour), and leaving a facet implicit because every item collected so far shares one of its elements.

The mapping sentence supplies no reduction. Which facets survive is settled downstream, by whichever invariant the analysis preserves.

### Formalizing the context

The framework starts from a **universe** $U$, the collection of objects to be distinguished, described by a set of **attributes** $A$.

Each attribute $a$ is formally a *function* that maps objects to values in a value set $V_a$:
$$a:U\rightarrow V_a$$

Many-valued attributes of this form constitute an **information system**, the structure on which rough sets operate. Formal Concept Analysis instead requires a one-valued **formal context**. Conceptual scaling derives that context from the information system:
$$\mathbb{K} = (U, A, I)$$

Three components compose the context:

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
$$B' = \{x \in U : \forall a \in B,\ (x,a) \in I\}$$
The two operators form a Galois connection between the subsets of $U$ and the subsets of $A$; the composites $X \mapsto X''$ and $B \mapsto B''$ are closure operators, and the concept lattice $\underline{\mathfrak{B}}(\mathbb{K})$ is the complete invariant of the description. ==TODO: explain these objets simply and what they serve to.==

> [!WARNING]
> This lattice-theoretic structure ==TODO: what is it, simply?== — a Moore family ==TODO: what is it, simply?== — is the qualitative counterpart of the linear span.
> It is strictly weaker: closure systems need not be modular ==TODO: what is modular here, simply?==, admit no complements in general, and support no notion of angle.

### Scaling many-valued attributes

^conceptual-scaling

> [!QUOTE] **Conceptual scaling** (Ganter & Wille)
> Each many-valued attribute is replaced by the binary attributes of a scale. The scaled columns compose the one-valued formal context derived from the information system.

Implications and the concept lattice are defined for a one-valued incidence $I \subseteq U \times A$, whereas an elicited attribute takes its values in an arbitrary set $V_a$. A **scale** bridges the two. The scale of the attribute $a$ is itself a formal context:
$$\mathbb{S}_a = (V_a, M_a, I_a)$$
Its objects are the values of $a$, and its attributes $M_a$ are the binary predicates that represent those values. In the derived context, the single column $a$ is replaced by the columns $M_a$, and an item $x$ receives the scale attribute $m$ whenever the pair $(a(x), m)$ belongs to $I_a$.

Four scales are standard:

- **nominal**, $(V_a, V_a, =)$: one mutually exclusive column per value, for unordered categories;
- **ordinal**, $(V_a, V_a, \leq)$: one column per value $v$, holding for the items whose value is at most $v$, so that the order is retained;
- **interordinal**: columns for both "at most $v$" and "at least $v$", so that intervals of values become concepts;
- **dichotomic**: two complementary columns, for a binary split.

The scale decides which distinctions reach the lattice, and no algorithm chooses it: a nominal scale applied to an ordered attribute discards the order, and a coarse ordinal scale merges values that the items genuinely separate. The value set $V_a$ carries no record of which of its distinctions matter, so every substantive modelling decision concentrates here. Each scale is therefore documented with the attribute it replaces.

Then, two distinct invariants may be preserved, each yielding a reduction method. Rough-set reduction reads the many-valued information system directly, so the reducts do not depend on the scales chosen. The reduction that preserves the concept lattice does depend on them, and so does the implication basis computed from the scaled context.

### Preserving discernibility (non-unique, NP hard)

^rough-set-theory

> [!QUOTE] **Rough Set Theory** (RST), introduced by Zdzisław Pawlak (1982)
> This decomposition method aims at a "minimal" non-redundant set of attributes sufficient to discriminate the items.

The central notion is that of **reduct**:

> A reduct is a **minimal collection of attributes having the same discriminatory power as the complete attribute vocabulary**. 

Formally, a reduct is a subset of attributes $R\subseteq A$ that satisfies:
$$\operatorname{IND}(R)=\operatorname{IND}(A)$$
while no proper subset of $R$ does.
 
> [!WARNING] Non-uniqueness: reducts are generally **multiple and non-isomorphic**.

The intersection of all reducts is the **core**: it contains the attributes that cannot be removed in _any_ reduct. 

Reducts can be identified mechanically by the **Skowron–Rauszer procedure**: ^skowron-rauszer-procedure

1. Construct the discernibility matrix $c_{ij} = \{a \in A : a \text{ separates } x_i, x_j\}$. Each entry $c_{ij}$ contains a set of attributes that discern between objects $x_i$ and $x_j$.
2. Form the discernibility function, a Boolean function over the attributes. It takes in arguments the attributes and outputs whether they form a reduct: ==TODO: explain the steps to compute the value from the arguments.== $$f = \bigwedge_{i<j} \ \bigvee_{a \in c_{ij}} a$$
3. Convert the discernibility function $f$ into a disjunction of conjunctions of attributes. ==TODO: explain how to construct this disjunction of conjunctions.== Each conjunction is a set of attributes that corresponds to a candidate reduct.
4. The reducts are the **prime implicants** of $f$. An *implicant* is a conjunction of attributes whose presence makes $f$ true, and it is *prime* when dropping any of its conjuncts destroys that entailment. Applied to the discernibility function, the first property means separating every pair of objects, and the second means retaining no removable attribute. A subset with both properties is precisely a reduct. ==TODO (resolved — the minimal conjunctions of attributes that make the discernibility function true): what are they?== ^prime-implicants

> [!WARNING] Complexity
> Computing a minimum-cardinality reduct is **NP-hard** (Wong & Ziarko, 1985): no polynomial-time algorithm is known, and none exists unless $P = NP$. The result is not unique either, so the remaining route is to enumerate all reducts and select one according to an external criterion.

### Preserving the conceptual structure (canonical)

^formal-concept-analysis

> [!QUOTE] **Formal Concept Analysis (FCA)**, introduced by Rudolf Wille (1982) and developed with Bernhard Ganter
> This alternative decomposition method aims to preserve the concept lattice $\underline{\mathfrak{B}}(\mathbb{K})$ up to isomorphism. 

The framework starts from objects and attributes and studies their logical structure. It defines **attribute implications** between two sets of attributes $B, C \subseteq A$:
$$B\rightarrow C$$
The implication means that whenever an object possesses all attributes in $B$, it necessarily possesses those in $C$.

An attribute $a$ is **reducible** iff its extent is an intersection of other attribute extents:
$$\{a\}' = \bigcap_{b \in B} \{b\}', \qquad B \subseteq A \setminus \{a\}$$
==TODO: how does it relate to the implication relations?==

The **reduced context** is obtained by deleting all reducible attributes, and dually all reducible objects, after clarification, that is, merging duplicate rows and columns ==TODO: in what table?==. This reduced context is *unique* up to isomorphism for finite $\mathbb{K}$. The surviving attributes correspond to the **meet-irreducible** elements of the lattice.

> [!WARNING] This method restores canonicity, but the "minimality" of the retained attributes is with respect to *set inclusion*, not cardinality.

The analysis then constructs an **irredundant implication basis** from which all valid attribute implications can be derived.

The classical **Duquenne–Guigues canonical basis** (1986) provides such a representation. ^duquenne-guigues-canonical-basis
==TODO: how to construct this basis?==
This basis, indexed by pseudo-closed sets, is **canonically determined** by $\mathbb{K}$ and has **minimum cardinality** among all bases of its implication theory. Every discarded or subsequently proposed attribute $a$ is then accounted for by the derivation $B \to B''$ that entails it.  ==TODO: what does it mean?==

> [!WARNING] Complexity
> The construction is deterministic and interpretable, and each individual closure $B \mapsto B''$ runs in time polynomial in the size of $\mathbb{K}$. The basis itself carries no polynomial bound: its cardinality can grow exponentially with the size of the context, so enumerating the pseudo-closed sets is the expensive step.

### Exploring attributes

^attribute-exploration

> [!QUOTE] **Attribute exploration** (Ganter, 1987)
> This procedure can be seen as a general methodology for acquiring structured conceptual knowledge from qualitative information.

This algorithm is an **interactive procedure**: 

- Candidate implications are systematically presented to a domain expert.
- The expert either validates them or supplies a counterexample.

==TODO: who is the "expert"? does it refer to a human specialist or is it a metaphoric denomination for some oracle / test data set ?==

The exploration and the [canonical basis](#^duquenne-guigues-canonical-basis) are distinct constructions, and computing the basis requires no exploration. The basis is a function of a *fixed* context, obtained by enumerating the pseudo-closed sets of that context, with no question asked. The exploration instead *builds* the context whose basis is sought: each question it asks is one implication of the basis of the context as it currently stands, and each counterexample adds an item, after which the basis is recomputed on the enlarged context.

The exploration is needed exactly when the items already collected form an unrepresentative sample of the domain. An implication that holds in the sample and fails in the domain is refuted by no available item, so the basis of the collected context asserts it as a law. The counterexample requested from the expert is precisely that missing item. Where the universe is taken as complete, the basis is computed directly and no question is asked.

For a finite attribute set, the process *provably terminates* with a context whose implication theory is complete for the domain. Its guarantee is genuine though relative to the oracle.

### Minimizing conditions for an outcome

^quine-mccluskey-qca

> [!QUOTE] **Quine–McCluskey minimization** (Quine, 1952; McCluskey, 1956), applied to comparative research as **qualitative comparative analysis** (Ragin, 1987)
> Once one attribute is designated as an outcome, Boolean minimization returns the minimal conjunctions of the remaining attributes that are sufficient for that outcome.

Designating one attribute as the **outcome** splits the vocabulary in two. The remaining **condition attributes** describe each item, while the outcome records the result to be explained, and the information system thereby becomes a *decision system*. The question asked of the vocabulary changes accordingly: reduction by discernibility and reduction by conceptual structure both ask which attributes distinguish the items, whereas this minimization asks which combinations of condition values suffice for the outcome.

The items are grouped into **configurations**, one per combination of values of the condition attributes, and each configuration carries the outcome observed for the items it holds. This truth table defines the **outcome function**, a Boolean function of the condition attributes. Quine–McCluskey minimization returns its [prime implicants](#^prime-implicants), the minimal conjunctions of conditions that entail the outcome. A minimal cover of the positive configurations by prime implicants is a minimal sufficient condition, and each disjunct of that cover is read as one path to the outcome.

One operation therefore underlies both reductions of the pipeline: the reducts are the prime implicants of the discernibility function, and the minimal sufficient conditions are the prime implicants of the outcome function. The two differ in the function minimized, not in the algorithm.

> [!WARNING] Limited diversity
> Configurations that no item realizes leave the outcome function undefined on part of the table. Treating those remainders as negative yields the *complex* solution, admitting them as unconstrained ("don't care") terms yields the *parsimonious* solution, and any intermediate solution rests on explicit counterfactual assumptions about which remainders would produce the outcome.

## Analogy with decomposition in linear algebra

> [!WARNING] Analogy with linear algebra is only *partial*

This conceptual decomposition approach echoes standard decomposition methods in *linear algebra* (e.g. Principal Component Analysis), where the basis elements are "independent" in some sense, and span the variability of the data so that each item can be reconstructed. However, *conceptual decomposition* differs in several respects. The following table summarizes the key differences and structural analogies:

| Linear algebra, PCA                                                                       | Conceptual spaces                                                                      |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Predefined ambient vector space: coordinates already exist numerically                    | No coordinate system a priori                                                          |
| Inner product on the ambient space, with the covariance defining "importance" and "orthogonality" | No canonical metric, no inner product, hence no notion of orthogonality                |
| Canonical basis ==TODO: complete==                                                        | *Implication basis* (i.e. a basis of the _dependencies_) rather than *attribute basis* |
| Linear independence                                                                       | Irreducibility                                                                         |
| Linear combination                                                                        | Intersection of extents                                                                |

**Gärdenfors' theory of conceptual spaces** explicitly treats dimensions as ways in which objects can be judged similar or different, while also emphasizing that dimensions need not be independent: some are _integral_, others _separable_, and [empirical dimensions co-vary within a domain, itself a set of integral dimensions separable from all others](https://www.lucs.lu.se/fileadmin/user_upload/project/lucs/PG/pg-2014r.pdf).

**Numerical decomposition requires axioms that must be tested, not assumed.** The conditions under which a qualitative structure admits an additive representation $\phi(a_1,\dots,a_k) = \sum_i \phi_i(a_i)$, unique up to a common positive multiplier and separate additive constants, are stated by **additive conjoint measurement** (Krantz, Luce, Suppes & Tversky, _Foundations of Measurement_, vol. I, 1971): independence, the Thomsen condition, restricted solvability, Archimedean axiom. These are empirically falsifiable ordinal conditions. Where they hold, a genuine PCA-like uniqueness obtains; where they fail, no amount of methodological care produces one.

## Main references

- Kelly, _The Psychology of Personal Constructs_ (1955)
- Goodman, _Fact, Fiction, and Forecast_ (1955) — poses the projectibility problem that minimal discrimination leaves unresolved.
- Pawlak, [_Rough sets_](https://link.springer.com/article/10.1007/BF01001956) (_International Journal of Computer and Information Sciences_ 11, 1982) — introduces approximation by indiscernibility.
- Pawlak, _Rough Sets: Theoretical Aspects of Reasoning about Data_ (Kluwer, 1991) — supplies the complementary theory of reducts and indiscernibility.
- Andrzej Skowron & Soma Dutta, [*Rough sets: past, present, and future*](https://link.springer.com/article/10.1007/s11047-018-9700-3)
- Piotr Hońko, [*Attribute reduction: a horizontal data decomposition approach*](https://link.springer.com/article/10.1007/s00500-014-1554-8)
- Zaineb Chelly Dagdia, Christine Zarges, Gaël Beck, Mustapha Lebbah, [A scalable and effective rough set theory-based approach for big data pre-processing](https://link.springer.com/article/10.1007/s10115-020-01467-y)
- Wong & Ziarko, _Bull. Polish Acad. Sci._ 33 (1985) — establishes that a minimum-cardinality reduct is NP-hard to compute.
- Wille, _Restructuring lattice theory_, in _Ordered Sets_ (Reidel, 1982) — introduces the concept lattice.
- Ganter & Wille, _[Formal Concept Analysis: Mathematical Foundations](https://link.springer.com/book/10.1007/978-3-642-59830-2)_ (Springer, 1999)
- Ganter, _Algorithmen zur Formalen Begriffsanalyse_, in _Beiträge zur Begriffsanalyse_ (1987) — introduces attribute exploration.
- Ganter & Obiedkov, _[Conceptual Exploration](https://link.springer.com/book/10.1007/978-3-662-49291-8)_ (Springer, 2016) — the textbook treatment of attribute exploration, its algorithms and generalizations.
- Guigues & Duquenne, _Math. Sci. Hum._ 95 (1986)
- Skowron & Rauszer, _The discernibility matrices and functions in information systems_, in _Intelligent Decision Support_ (Kluwer, 1992)
- Krantz, Luce, Suppes & Tversky, _Foundations of Measurement_ I (1971)
- Gärdenfors, _Conceptual Spaces: The Geometry of Thought_ (MIT Press, 2000) — treats dimensions as grounds of similarity judgment, integral or separable.
- Rissanen, _Modeling by shortest data description_, _Automatica_ 14 (1978) — supplies the external minimum-description-length criterion.
- Borg & Shye, _Facet Theory: Form and Content_ (Sage, 1995)
- Ragin, _The Comparative Method_ (1987)
- Quine, _The problem of simplifying truth functions_, _American Mathematical Monthly_ 59 (1952) — reduces a truth function to its prime implicants.
- McCluskey, _Minimization of Boolean functions_, _Bell System Technical Journal_ 35 (1956) — supplies the tabular procedure that systematizes that reduction.
