---
tags:
  - reference
index: "[Methods for taxonomies](_index.md)"
aliases:
  - Taxonomic construction procedure
---
# Taxonomic construction procedure

> [!QUESTION] Goal: designing a systematic methodology to construct taxonomies, regardless of the domain.

Specifically, a qualitative taxonomy of a set of objects is adequate when it delivers a set of attributes ("conceptual dimensions") that satisfy the following requirements:

- every pair of objects that must be distinguished differs on at least one attribute,
- no retained attribute is determined by the others,
- the dependencies among the retained attributes are stated explicitly.

## Operationalizing the problem

### Objects, attributes, values

To apply systematic methods, the verbal description of the domain must first take a formal shape:

- the **objects** that the taxonomy must distinguish are collected into a **universe** $U$ (e.g. species of birds);
- the **attributes** describing these objects are collected into a set $A$ (e.g. plumage color and beak shape);
- the available **values** for each attribute $a$ are collected in a set $V_a$ (e.g. "red", "blue", "green" for plumage color).

Each attribute $a$ is a *function* assigning a value to every object:
$$a:U\rightarrow V_a$$
*Example*: The distinction *robust beak* becomes an attribute once the rule fixes, for instance, that a beak deeper than half its length counts as robust. Without such a rule, two observers describing the same bird could record different values. 

Any subset of attributes $B\subseteq A$ induces an **indiscernibility relation**. ^def-indiscernibility
Two objects are indiscernible whenever every attribute in $B$ assigns them identical values:
$$\operatorname{IND}(B)=\{(x,y)\in U\times U: \forall a\in B, a(x)=a(y)\}$$
The relation is an equivalence, so it partitions the universe into classes of objects that the attributes of $B$ cannot separate.

### Two types of attributes

> [!IMPORTANT] Two forms feed different reduction methods

An attribute can be either:

- **many-valued**, when its value set holds more than two values (e.g. the color of a bird ranges over a set of colors), 
- **one-valued** when it either holds of an object or does not (e.g. the attribute "being red" is boolean).

A description with *many-valued attributes* is an **information system**, written as the pair of the universe and the attribute set: ^def-information-system
$$\mathcal{A} = (U, A)$$

A description with *one-valued attributes* is a **formal context**, written as a triple: ^def-formal-context
$$\mathbb{K} = (U, A, I)$$
The the incidence $I \subseteq U \times A$ is the set of pairs $(x,a)$ such that object $x$ has attribute $a$.

> [!NOTE] Differences between both structures
> The two structures differ in how they carry the values: 
> - an attribute of an information system returns a value from its set $V_a$, 
> - the incidence of a context records only the pairs on which the attribute holds.

### Tabulating the attributes

The reduction methods operate on an **object × attribute matrix**: ^def-object-attribute-matrix

- its *rows* are the *objects*, 
- its *columns* are the *attributes*, 
- each cell the value that the attribute assigns to that object, carried by the attribute function itself.

For an [information system](#^def-information-system), each cell holds a value drawn from the set $V_a$. For a [formal context](#^def-formal-context), each cell states records only whether the object carries the attribute, so the matrix is **binary**.

*Example*: four species of birds described by three many-valued attributes give the following *information system* table:

| species | beak depth | plumage color | diet    |
| ------- | ---------- | ------------- | ------- |
| $s_1$   | shallow    | red           | insects |
| $s_2$   | deep       | red           | seeds   |
| $s_3$   | deep       | blue          | seeds   |
| $s_4$   | shallow    | blue          | nectar  |

> [!TIP] Conversion
> The table of an [information system](#^def-information-system) can be turned into the table of a a [formal context](#^def-formal-context) by [scaling the many-valued attributes](#^conceptual-scaling), i.e. replacing each column with binary ones.

## Division of labour

### Domain-dependent vs. -independent steps

The methodology is **hybrid**: ^hybrid-methodology

- The initial and terminal stages *depend on the domain*. They demand knowledge of which differences between the objects matter for the purpose the taxonomy serves:

	- which candidate attributes to consider in the first place, since the objects alone and their arbitrary verbal descriptions provably do not determine them;
	- which set of attributes to retain, since several sets are typically admissible (by different methods, and by one method).
	
- The intermediate phases are *independent* of the domain and proceed mechanically. Rigorous algorithmic procedures settle the questions of:

	- which attributes actually discriminate the objects;
	- which attributes are redundant;
	- which minimal subsets of attributes preserve the distinctions the full set induces;
	- which dependencies hold between attributes;
	- how a discarded attribute is derived from the retained ones, where the dependency is logically supported.

> [!IMPORTANT] Need of external criteria
> The domain enters irreducibly at one point: deciding **which distinctions count as meaningful**, since the [two reduction methods](#^two-reduction-routes) together provide *multiple candidate sets of attributes*.

### Two reduction routes

Two reduction methods answer different questions and achieve distinct constraints: ^two-reduction-routes

| Method                                               | Constraint                                       | Output                                                                                                          |
| ---------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| [Rough Set reduction](#^rough-set-theory)            | preserving only discriminability between objects | distinct sets of attributes that still distinguish the objects, generally of different sizes                    |
| [Formal Concept Analysis](#^formal-concept-analysis) | preserving the structure of the conceptual space | *canonical* set of attributes (unique up to isomorphism) + *canonical* basis of dependencies holding among them |

So, each method provides at least one set of candidate attributes. Selecting the appropriate vocabulary among these candidates still requires a **criterion from outside the description**, such as an external semantic objective.

*Example*: A set of birds can be partitioned by both plumage color and beak shape. The second distinction becomes the meaningful one when the objective is predicting what each species eats.

## Pipeline

> [!NOTE] Hybrid methodology
> The phases follow the [division of labour](#^hybrid-methodology): eliciting the distinctions and selecting the final vocabulary demand domain judgment, whereas formalizing the description and reducing it proceed mechanically.

### Designing the description

1. **Define the universe $U$.** Specify which objects the taxonomy must distinguish and for what purpose.
2. **Elicit candidate distinctions.** Compare maximally diverse objects and name the property that carries each relevant difference (*method*: [Kelly's triadic elicitation](#^kelly-triadic-elicitation)).
3. **Structure the descriptive space.** Declare the design of the description as a whole as a template sentence, from the objects, the attributes, and the values (*method*: [Guttman's mapping sentence](#^guttman-mapping-sentence)). Determine all the admissible profiles by the Cartesian product of the template sentence.

### Formalizing the description

4. **Operationalize attributes.** Turn each attribute into a rule that assigns a value to any object, the admissible values being Boolean, categorical, or ordinal. 
5. **Construct the [object × attribute matrix](#^def-object-attribute-matrix).** Evaluate every attribute on every object. The table is the [information system](#^def-information-system) on which every later reduction operates.
6. **Test coverage.** Check that every pair of objects to distinguish differs on at least one attribute. When a pair does not differ, the vocabulary is incomplete, and the procedure must return to eliciting distinctions.

### Reducing and deriving dependencies

> [!NOTE] Two reduction routes
> At this stage, the pipeline divides in [two routes that answer distinct questions](#^two-reduction-routes): a taxonomy that needs only a small vocabulary takes the Rough Sets route, whereas one that needs only the dependency structure takes the FCA route.
> Both routes rejoin when a single vocabulary must be selected among the candidate sets.

**By preserving discernibility**:

7. **Compute [reducts](#^def-reduct).** From the many-valued [object × attribute matrix](#^def-object-attribute-matrix), identify the attribute subsets that preserve the indiscernibility relation of the full vocabulary and are minimal for set inclusion (*method*: [rough-set reduction](#^rough-set-theory)). The step ends with a *family* of candidate attribute sets, rather than a single solution.

**By preserving the conceptual structure**:

8. **Scale the many-valued attributes.** Obtain the [one-valued formal context](#^def-formal-context) by replacing each attribute carrying more than two values by the binary columns of a scale (*method*: [conceptual scaling](#^conceptual-scaling)).
9. **Clarify and reduce the context.** First merge the duplicate rows and columns of the cross-table of the context, then delete every attribute whose extent (i.e. set of objects carrying it), is an intersection of other extents (*method*: [Formal Concept Analysis](#^formal-concept-analysis)). The surviving attributes are the *meet-irreducible* ones, and the reduced context is unique up to isomorphism.
10. **Compute the canonical basis of implications.** An implication is a dependency between two sets of attributes, that holds when every object carrying all attributes of one set also carries those of the other. Construct the [canonical "basis" of implications](#^duquenne-guigues-canonical-basis), that generates every implication valid in the context (*method*:  [Ganter's Next-Closure algorithm](#^next-closure)).

> [!NOTE] Multiple candidate solutions
> The reduction leaves several attribute sets with equal discriminatory power, and the canonical basis fixes the dependencies without ranking those sets. 

### Selecting and validating the vocabulary

11. **Select one [reduct](#^def-reduct).** Define a criterion that the vocabulary itself cannot supply, and score each candidate set. For instance, measure [accuracy on new objects](#^crit-predictive-accuracy), or [count the total length of the description](#^crit-minimum-description-length).
12. **Validate the vocabulary.** Add to the universe new objects that were not used in the construction — in particular the pairs that the retained attributes are most likely to conflate — and check that those attributes still discriminate them. If discrimination fails, then the procedure must return to eliciting distinctions.
13. **Validate dependencies.** If the objects collected so far form a *sample* rather than the whole domain, check whether the implication basis computed on those objects is complete, or enlarge the context with new objects and update the basis (*method*: [Attribute Exploration](#^attribute-exploration)).

> [!NOTE]
> The two validation tests differ in what they test:
> - the first test confronts the declared *vocabulary* with new objects and repairs the *vocabulary* (selection of attributes);
> - the second test ("Attribute Exploration") submits an *implication* to an expert and repairs the *dependencies*.

### Explaining a designated outcome

14. **Minimize the conditions for an outcome.** If one attribute records a *result* to be explained rather than a *description* of an object, single out that attribute and compute the smallest combinations of the remaining attributes whose presence suffices for the result (*method*: [Quine–McCluskey minimization](#^quine-mccluskey-qca)). 

## Formal references

Each step of the pipeline draws on one formal framework:

- [Repertory-grid and contrastive elicitation](#^kelly-triadic-elicitation) identifies the candidate attributes from contrasts observed among the objects themselves.
- [Facet theory (mapping sentence)](#^guttman-mapping-sentence) declares the objects, the attributes and the values, and determines the admissible profiles.
- [Conceptual scaling](#^conceptual-scaling) replaces each many-valued attribute with binary columns, producing the one-valued context.
- [Rough sets](#^rough-set-theory) return the "minimal" attribute subsets that discriminate the objects as the full vocabulary does.
- [Formal Concept Analysis](#^formal-concept-analysis) exposes the logical dependencies among attributes and the derivations that recover the discarded ones.
- [Minimum description length](#^crit-minimum-description-length) ranks the competing reducts by the length of the description each of them yields.
- [Attribute exploration](#^attribute-exploration) completes a universe of objects that holds no counterexample to a false law.
- [Quine–McCluskey minimization](#^quine-mccluskey-qca) returns the minimal conjunctions of conditions sufficient for a designated outcome.

### Eliciting initial attributes

> [!QUOTE] Kelly's **repertory grid** and **triadic elicitation** (1955)
> This procedure is established in Personal Construct Theory, and then used across various domains, from [measuring how participants' self-identity shifted over a youth development program](https://pmc.ncbi.nlm.nih.gov/articles/PMC3349140/) to [eliciting the constructs listeners apply in sound design](https://dl.acm.org/doi/10.1145/1859799.1859807) and [mapping the design space of aesthetics](https://arxiv.org/abs/2008.07862).

This technique identifies the initial attributes ("conceptual dimensions") that discriminate the objects. It proceeds systematically, thereby replacing an unconstrained brainstorming.

The procedure consists of a series of **triadic comparisons**: ^kelly-triadic-elicitation

> Present three representative objects, name the property distinguishing one from the other two. Concretely, ask: _In what relevant respect are two alike and different from the third?_

The answer produces a **bipolar** attribute: the property that the pair shares provides one pole, and the contrasting property of the third object provides the other pole. All the remaining objects will then be placed in between these two ends, so the attribute may take more than two values.

The comparison is repeated across strategically chosen triads to form a vocabulary of attributes.

> [!CHECK] Non-trivial discrimination
> By construction, the property groups as well as separates:
> -  The contrast among two objects guarantees that the attribute actually discriminates.
> - The third object forces the named property to hold of two objects, while a mere *pair* could yield a arbitrary difference. 

### Structuring the descriptive space

> [!QUOTE] **Mapping sentence** (Guttman's facet theory; Borg & Shye, 1995)

The **mapping sentence** is a template used to describe the whole design. ^guttman-mapping-sentence

Each slot of the template sentence is a **facet**, a set whose elements are the values admissible in that slot: 

- the **population facet** fixes the *universe* — which objects are observed;
- the **content facets** fix the *attributes* — the respects in which each object is described;
- the **range facet** fixes the *values* an observation may take, together with the unit and the resolution recorded.

*Example*: For a taxonomy of finch species, one template reads:

> Species (*x*) of the Galápagos finches has a beak of depth {shallow / intermediate / deep} and plumage of color {red / blue / green}, and feeds mainly on {seeds / insects / nectar}.

The mapping sentence plays several roles:

- It **commits the declared attributes** to be all the respects that the description covers.
	
- It fixes, a priori, all the **admissible profiles**, obtained by the Cartesian product of facets that the objects are expected to populate. By contrast, the [object × attribute table](#^def-object-attribute-matrix) records only the **realized profiles**. Comparing the realized profiles against the admissible ones exposes the **unrealized profiles**, that are never observed. Those unrealized profiles are probed by [attribute exploration](#^attribute-exploration) and treated as remainders by [Boolean minimization](#^quine-mccluskey-qca).
	
- It **prevents errors** that a completed table cannot expose: 
	
	- naming a value where an attribute is intended (a class of "red objects" instead of a facet of color), 
	- leaving a facet implicit because every object collected so far shares one of its elements.

### Scaling many-valued attributes

> [!QUOTE] **Conceptual scaling** (Ganter & Wille)

To convert an [information system](#^def-information-system) into a [formal context](#^def-formal-context), each many-valued attribute is replaced by the **binary attributes of a scale**. 

> [!NOTE] The one-valued formal context is required only by the [Formal Concept Analysis](#^formal-concept-analysis).

**Deriving the one-valued formal context**: ^conceptual-scaling

1. For each many-valued attribute $a$, define its **scale**. The scale is itself a [formal context](#^def-formal-context): $$\mathbb{S}_a = (V_a, M_a, I_a)$$
	- the objects are the values of $a$ from the set $V_a$, 
	- the attributes $M_a$ are the binary predicates that represent those values.
	
2. In the [information-system table](#^def-information-system), replace the single column $a$ by the columns $M_a$.
	
3. Assign the scale attribute $m$ to the object $x$ whenever the pair $(a(x), m)$ belongs to the incidence $I_a$.

**Standard scales**:

- **nominal**, $(V_a, V_a, =)$: one mutually exclusive column per value, for unordered categories;
- **ordinal**, $(V_a, V_a, \leq)$: one column per value $v$, holding for the objects whose value is at most $v$, so that the order is retained;
- **interordinal**: columns for both "at most $v$" and "at least $v$", so that intervals of values become concepts;
- **dichotomic**: two complementary columns, for a binary split.

*Example*: a nominal scale on plumage color keeps the values mutually exclusive:

| value | is red | is blue | is green |
| ----- | ------ | ------- | -------- |
| red   | ×      |         |          |
| blue  |        | ×       |          |
| green |        |         | ×        |

*Example*: on beak depth, ordered as shallow $<$ intermediate $<$ deep, the ordinal scale keeps the three left columns, while the interordinal scale keeps all six:

| value        | at most shallow | at most intermediate | at most deep | at least shallow | at least intermediate | at least deep |
| ------------ | --------------- | -------------------- | ------------ | ---------------- | --------------------- | ------------- |
| shallow      | ×               | ×                    | ×            | ×                |                       |               |
| intermediate |                 | ×                    | ×            | ×                | ×                     |               |
| deep         |                 |                      | ×            | ×                | ×                     | ×             |

An interval is recovered as a conjunction: intermediate is "at most intermediate" together with "at least intermediate". 

*Example*: a dichotomic scale on the same attribute keeps two complementary columns instead, splitting the values at "deep":

| value        | deep | not deep |
| ------------ | ---- | -------- |
| shallow      |      | ×        |
| intermediate |      | ×        |
| deep         | ×    |          |

> [!IMPORTANT] Modelling decisions
> The scale determines which distinctions reach the lattice. For instance, a nominal scale applied to an ordered attribute discards the order, while a coarse ordinal scale merges values that the objects genuinely separate. Each scale must therefore be documented with the attribute it replaces and must justify which of its distinctions matter.

### Reducing by preserving discernibility

> [!QUOTE] **Rough Set Theory** (RST), introduced by Zdzisław Pawlak (1982)

This reduction method aims at a "minimal" non-redundant set of attributes sufficient to discriminate the objects. ^rough-set-theory

#### Definitions

A **reduct** is a subset of attributes $R\subseteq A$ that satisfies two conditions: ^def-reduct

1. it preserves the [indiscernibility relation](#^def-indiscernibility), i.e. merges none of the classes the full vocabulary distinguishes: $$\operatorname{IND}(R)=\operatorname{IND}(A)$$
2. it is *minimal for set inclusion*, i.e. no proper subset of $R$ still discriminates the objects.

> [!WARNING] Non-uniqueness: reducts are generally **multiple and non-isomorphic**.

The intersection of all reducts is the **core**: it contains the attributes that cannot be removed in _any_ reduct.

> [!IMPORTANT] Notion of minimality
> A [reduct](#^def-reduct) is minimal for *set inclusion*, not for *cardinality*: no proper subset of a reduct still discriminates the objects, but another reduct may be strictly smaller.

> [!WARNING] Minimal cardinality alone is vacuous
> To discriminate all pairs among $n$ objects, $\lceil \log_2 n \rceil$ _arbitrary_ binary attributes suffice. Discrimination with minimal cardinality is therefore *trivially achievable* and carries *no epistemic content*.
> The operative desideratum is not minimality but **projectibility** — the capacity of the attributes to classify objects that the universe does not yet contain. Projectibility is demonstrably underdetermined by any finite universe (Goodman, _Fact, Fiction, and Forecast_, 1955).

#### Procedure

The process operates on the [object × attribute matrix](#^def-object-attribute-matrix) of an [information system](#^def-information-system) $\mathcal{A}$.

Reducts are identified mechanically by the **Skowron–Rauszer procedure**. ^skowron-rauszer-procedure

1. Construct the *discernibility matrix* $M(\mathcal{A})$, whose entry $c_{ij}$ holds the attributes that separate the objects $x_i$ and $x_j$: $$c_{ij} = \{a \in A : a(x_i) \neq a(x_j)\}$$
	
2. Form the *discernibility function* $f_{\mathcal{A}}$, a Boolean function whose variables are the attributes. Each non-empty entry of the matrix $M(\mathcal{A})$ contributes the disjunction of the attributes it holds, and the function is the conjunction of those disjunctions: $$f_{\mathcal{A}} = \bigwedge_{c_{ij} \in M(\mathcal{A}),\; c_{ij} \neq \emptyset} \ \bigvee_{a \in c_{ij}} a$$A candidate subset $B$ is evaluated by setting the variables of $B$ to true and the remaining variables to false. One disjunction is then true whenever $B$ holds at least one attribute separating that pair, so $f$ is true exactly when $B$ separates every pair that the full vocabulary separates.
	
3. Convert the discernibility function $f_{\mathcal{A}}$ into a disjunction of conjunctions of attributes: distribute the conjunction $\wedge$ over the disjunctions $\vee$, and then absorb every term that contains another (since, by idempotence, $a \vee (a \wedge b) = a$). 
	
4. Extract the surviving conjunctions: each is a set of attributes that corresponds to a candidate reduct.
	
5. The reducts are the **prime implicants** of the discernibility function $f$: ^prime-implicants
	
	- an *implicant* is a conjunction of attributes whose presence makes $f$ true — which means separating every pair of objects;
	- it is *prime* when dropping any of its conjuncts destroys that entailment — which means retaining no removable attribute.

> [!WARNING]
> So, the *value* of the discernibility function only reports that a set of attributes is *sufficient* to discriminate the objects (half of the [definition](#^def-reduct)). Minimality is the further condition that isolates the reducts.

*Example*: on the [four-species table](#^def-information-system), the attributes beak depth, plumage color and diet are written $b$, $c$ and $d$.

- The *discernibility matrix* $M(\mathcal{A})$ gives the attributes that separate each pair (only the non-empty entries of the matrix are presented below):

| pair       | discriminant attributes |
| ---------- | ----------------------- |
| $s_1, s_2$ | $b$, $d$                |
| $s_1, s_3$ | $b$, $c$, $d$           |
| $s_1, s_4$ | $c$, $d$                |
| $s_2, s_3$ | $c$                     |
| $s_2, s_4$ | $b$, $c$, $d$           |
| $s_3, s_4$ | $b$, $d$                |

- Discarding the repeated entries, the function is:
$$f_{\mathcal{A}} = (b \vee d) \wedge (b \vee c \vee d) \wedge (c \vee d) \wedge c$$
- The single-attribute clause $c$ (last term) absorbs every clause containing $c$, so $f_{\mathcal{A}}$ reduces to $c \wedge (b \vee d)$.
- Distributing gives $(c \wedge b) \vee (c \wedge d)$. 
- The reducts are therefore $\{b, c\}$ and $\{c, d\}$, that is, beak depth with color, and color with diet.
- The core is $\{c\}$ alone: no vocabulary separates $s_2$ from $s_3$ without the color, since the two species differ on no other property. 

> [!WARNING] Complexity
> Obtaining _one reduct_ costs a **polynomial** removal of attributes (one at a time).
> Obtaining one of *minimum cardinality* is **NP-hard** (Wong & Ziarko, 1985): no polynomial-time algorithm is known, and none exists unless $P = NP$. 
> Singling out the smallest set is therefore a further step, and not what the route delivers.

### Reducing by preserving the conceptual structure

> [!QUOTE] **Formal Concept Analysis (FCA)**, introduced by Rudolf Wille (1982) and developed with Bernhard Ganter

This reduction method aims to preserve the concept lattice $\underline{\mathfrak{B}}(\mathbb{K})$ up to isomorphism. ^formal-concept-analysis

#### Definitions

The theory introduces two **derivation operators** that read the incidence in opposite directions:

- The **extent** of a set of *attributes* $B \subseteq A$ is the set of *objects* that share all attributes in $B$: 
$$B' = \{x \in U : \forall a \in B,\ (x,a) \in I\}$$
	For a single attribute $a$, the extent $\{a\}'$ is its *column* in the [cross-table](#^def-object-attribute-matrix).
	
- The **intent** of a set of *objects* $X \subseteq U$ is the set of *attributes* shared by all objects in $X$:
$$X' = \{a \in A : \forall x \in X,\ (x,a) \in I\}$$

These operators define the constructs that reduction manipulates:

- The **concept lattice** is the family of extents, that is, the sets of objects of the form $B'$ for some set of attributes $B$, ordered by inclusion. The family is a lattice because any two extents have a greatest extent below both, their intersection, and a least extent above both, the smallest extent containing them.
	
- The composites $X \mapsto X''$ and $B \mapsto B''$ are **closure operators**: each sends a set to its smallest closed superset. Applied to a set, the word names the result: $B''$ is *the closure of* $B$, which contains every attribute carried by all the objects that carry $B$. 
	
- A set is **closed** when it equals its own closure, $B = B''$: every further attribute would drop an object from its extent. A set is **unclosed** when its closure exceeds it, $B \neq B''$: the closure holds an attribute outside $B$ that every object carrying $B$ carries anyway, so adding it leaves the extent unchanged.

Two sets of attributes $B, C \subseteq A$ are related by an **attribute implication** $B\rightarrow C$ whenever every object possessing all attributes in $B$ also possesses those in $C$. The implication is determined by the closure $B''$ of $B$:
$$B \to C \iff C \subseteq B''$$

An attribute $a$ is **reducible** when *some* set of other attributes has the same extent: the reducible attribute can be *defined* from the others, and its column carries no distinction that the columns of these other attributes do not already carry jointly. Formally,  $a$ is reducible iff there exists a set $B \subseteq A \setminus \{a\}$ such that:
$$\{a\}' = \bigcap_{b \in B} \{b\}' = B'$$
The intersection is the set of objects that carry every attribute in $B$. Since $a$ and $B$ have the same extent, both implications $B \to a$ and $a \to B$ are valid (mutual implication).

Conversely, an attribute is **irreducible** when no intersection of the others recovers it. In other words, dropping such an attribute removes an extent that no intersection of the remaining columns reproduces. ^def-irreducible-attribute

The extent $\{a\}'$ of an irreducible attribute is then a **meet-irreducible** element of the concept lattice: no intersection of extents strictly larger than it returns it. The irreducible attributes generate the whole lattice: every extent is an intersection of theirs. They are exactly the attributes that the reduction retains.

*Example*: the four finches, described by three attributes scaled nominally: ^scaled-bird-context

| species | shallow | deep | red | blue | insects | seeds | nectar |
| ------- | ------- | ---- | --- | ---- | ------- | ----- | ------ |
| $s_1$   | ×       |      | ×   |      | ×       |       |        |
| $s_2$   |         | ×    | ×   |      |         | ×     |        |
| $s_3$   |         | ×    |     | ×    |         | ×     |        |
| $s_4$   | ×       |      |     | ×    |         |       | ×      |

The column *insects* holds of $s_1$ alone, and so does the intersection of *shallow* and *red*. The attribute *insects* is therefore reducible: a finch with a shallow beak and red plumage eats insects, and conversely.

An **implication basis** is a set of valid implications entailing every valid implication of the context.

The **premises** of the basis are the left-hand sides of the implications, hence a set of attributes. ^def-premice

The **Duquenne–Guigues canonical basis** (1986) is the unique implication basis that: ^duquenne-guigues-canonical-basis

- is *irredundant*: no member follows from the others;
- has *minimum cardinality* among all bases of the implication theory. 

These two characteristic properties are guaranteed by a recursive definition:

- The **premises** $P$ of the basis are the **pseudo-closed** sets of attributes, each contributing exactly one implication, $P \to P''$.
	
- A set $P$ is **pseudo-closed** when it meets two conditions: ^def-pseudo-closed
	
	1. $P$ is unclosed (i.e. $P \neq P''$ ), so its implication forces attributes *outside* $P$ and is not vacuous.
	2. For every pseudo-closed set $Q$ strictly contained in $P$ (i.e. $Q \subsetneq P$), then $Q'' \subseteq P$. This makes $P$ absorb the consequences of every pseudo-closed set strictly inside it, so its implication does not follow from theirs. 
	
- The base case is the sets with no pseudo-closed proper subset, for which the second condition holds vacuously.

*Example*: on the context of the [four finches](#^scaled-bird-context), the canonical basis holds six implications:
$$\text{insects} \to \text{shallow},\ \text{red} \qquad\qquad \text{shallow},\ \text{red} \to \text{insects}$$
$$\text{nectar} \to \text{shallow},\ \text{blue} \qquad\qquad \text{shallow},\ \text{blue} \to \text{nectar}$$
$$\text{red},\ \text{blue} \to \text{every attribute} \qquad\qquad \text{shallow},\ \text{deep} \to \text{every attribute}$$
The first two pairs state that *insect* and the pair (*shallow*, *red*) determine one another, and likewise for *nectar* and (*shallow*, *blue*). The last pair records impossibility (a premise that no object realizes forces every attribute): no finch of the table is both *red* and *blue*, or both *shallow* and *deep*.

#### Procedures

> [!TIP] Two procedures
> The reduction of the context precedes the computation of the basis for two reasons:
> - Constructing the basis proceeds by an enumeration that is exponential in the number of attributes, so it must run on the smallest attribute set carrying the concept lattice.
> - On an unreduced context, most of the implications produced only record that the removable columns are derivable — the information that the reduction has already extracted, and that [the closure derivation](#^context-reduction) restores on demand.

**Reducing the context**: ^context-reduction

This procedure operates on the [cross-table](#^def-object-attribute-matrix) of a [formal context](#^def-formal-context) $\mathbb{K}$.

1. *Clarification step*. Merge the duplicate rows and columns of the cross-table of the context, that is, objects carrying identical attribute sets, and attributes whose extents coincide.
	
2. *Identification step*. For each attribute in turn, collect the attributes whose column contains its own column, and intersect those columns: the attribute is *reducible* exactly when that intersection is its own column.
	
3. *Reduction step*. Delete every reducible attribute, and dually every reducible object. The surviving attributes, the irreducible ones, correspond to the **meet-irreducible** elements of the concept lattice.

*Example*: on the [scaled table of the four finches](#^scaled-bird-context):

- *Clarification*: the columns *deep* and *seeds* hold of $s_2$ and $s_3$ and of no other object, so they are duplicates and merge into one.
- *Identification*: *insects* is the intersection of *shallow* and *red*, and *nectar* the intersection of *shallow* and *blue*. Applying the test to the remaining four columns returns no reducible attribute.
- *Reduction*: after deleting *insects* and *nectar*, the reduced context retains *shallow*, *deep*, *red* and *blue*.

> [!IMPORTANT] Order of the steps
> The *Clarification step* must run *before* the *Reduction step*. Indeed, two attributes sharing an extent are each *reducible* with respect to the other: deleting reducible attributes on an unclarified table could remove both and lose the extent they share. In the table above, *deep* and *seeds* are exactly such a pair.
> In the *Clarification step*, merging duplicate rows and merging duplicate columns are independent, since objects with identical rows agree on every attribute and removing one cannot separate two columns, and dually.

> [!CHECK] Canonicity
> The result is *unique* up to isomorphism for finite context $\mathbb{K}$: no other reduced context carries the same lattice.
> Deleting any retained attribute changes the lattice, so the retained set is minimal for *set inclusion*, not for cardinality. 
> *Warning*: minimality by inclusion holds for the *lattice* rather than the indiscernibility relation for the [reducts](#^def-reduct). The retained set is therefore not the smallest a taxonomy could use, since [a reduct is generally smaller](#^reduced-set-versus-reduct).

**Computing the implication basis** (Ganter's **Next-Closure** algorithm): ^next-closure

1. Order the attributes once and for all, and then derive the *lectic order* of the sets of attributes: of two distinct sets, the smaller is the one that omits the first attribute on which they differ.
	
2. Start from the empty set of attributes and an empty list of implications.
	
3. Compute the closure $B''$ of the current set $B$ in the context. When $B'' \neq B$, record the implication $B \to B''$: the set $B$ is pseudo-closed.
	
4. Move to the lectically next set that is closed under the implications recorded so far, and return to step 3.
	
5. Stop once the set of all attributes is reached. The recorded implications are the canonical basis.

Each set is obtained from its predecessor, so that no set is generated twice and none is stored for comparison.

*Example*: on the clarified table of the four finches, with *seeds* merged into *deep*:

| species | shallow | deep | red | blue | insects | nectar |
| ------- | ------- | ---- | --- | ---- | ------- | ------ |
| $s_1$   | ×       |      | ×   |      | ×       |        |
| $s_2$   |         | ×    | ×   |      |         |        |
| $s_3$   |         | ×    |     | ×    |         |        |
| $s_4$   | ×       |      |     | ×    |         | ×      |

Order the attributes *shallow* $<$ *deep* $<$ *red* $<$ *blue* $<$ *insects* $<$ *nectar*, abbreviated $s$, $d$, $r$, $b$, $i$, $n$. The enumeration then visits 16 sets, and records an implication at each set that its closure exceeds:

| visit | set                    | closure                | verdict                                     |
| ----- | ---------------------- | ---------------------- | ------------------------------------------- |
| 1     | $\{\ \}$               | $\{\ \}$               | closed                                      |
| 2     | $\{n\}$                | $\{s, b, n\}$          | pseudo-closed, records $n \to s, b$         |
| 3     | $\{i\}$                | $\{s, r, i\}$          | pseudo-closed, records $i \to s, r$         |
| 4     | $\{b\}$                | $\{b\}$                | closed                                      |
| 5     | $\{r\}$                | $\{r\}$                | closed                                      |
| 6     | $\{r, b\}$             | $\{s, d, r, b, i, n\}$ | pseudo-closed, records $r, b \to s, d, i, n$ |
| 7     | $\{d\}$                | $\{d\}$                | closed                                      |
| 8     | $\{d, b\}$             | $\{d, b\}$             | closed                                      |
| 9     | $\{d, r\}$             | $\{d, r\}$             | closed                                      |
| 10    | $\{s\}$                | $\{s\}$                | closed                                      |
| 11    | $\{s, b\}$             | $\{s, b, n\}$          | pseudo-closed, records $s, b \to n$         |
| 12    | $\{s, b, n\}$          | $\{s, b, n\}$          | closed                                      |
| 13    | $\{s, r\}$             | $\{s, r, i\}$          | pseudo-closed, records $s, r \to i$         |
| 14    | $\{s, r, i\}$          | $\{s, r, i\}$          | closed                                      |
| 15    | $\{s, d\}$             | $\{s, d, r, b, i, n\}$ | pseudo-closed, records $s, d \to r, b, i, n$ |
| 16    | $\{s, d, r, b, i, n\}$ | $\{s, d, r, b, i, n\}$ | closed, and the run stops                   |

The 6 implications recorded are those given with the [definition of the basis](#^duquenne-guigues-canonical-basis). Four of them concern the two columns that the reduction removes, so the same run on the reduced context therefore returns two implications only.

**Expressing the dependencies between attributes**:

Write $B$ for the set of attributes retained, that is, the [irreducible ones](#^def-irreducible-attribute) after [context reduction](#^context-reduction), or the [reduct](#^def-reduct) that the [Rough Sets route](#^rough-set-theory) selects.

The derivation $B \to B''$ then accounts for the discarded attributes, and for any attribute proposed later: when an attribute lies in the closure $B''$ of the retained set $B$, then every object carrying $B$ carries that attribute too, so the implication recovers it. In other words, $B''$ holds the attributes that $B$ forces. So, an attribute in $B''$ is entailed by the retained ones and needs no column of its own: it can be deleted without loss.

*Example*: with *shallow*, *deep*, *red* and *blue* retained, the closure of $\{\text{shallow}, \text{red}\}$ contains *insects*, and the closure of $\{\text{shallow}, \text{blue}\}$ contains *nectar*. Both discarded columns are recovered by an implication, and neither is stored.

> [!WARNING] Complexity
> Each individual closure $B \mapsto B''$ runs in time **polynomial** in the size of the context $\mathbb{K}$. 
> However, the basis itself carries no polynomial bound: its cardinality can grow **exponentially** with the size of the context, so enumerating the pseudo-closed sets is the expensive step.

### Selecting among competing reducts

> [!QUOTE] **Minimum description length** (Rissanen, 1978)

Every [reduct](#^def-reduct) separates the objects exactly as the full vocabulary does, so no criterion internal to the description distinguishes one from another. The canonical basis of implications does not rank them either: it fixes the dependencies holding in the context, whatever attribute set is taken as primitive.

Multiple criteria can be considered, and several may be applied together. The two criteria below can be used depending on what is available: predictive accuracy needs objects held out of the construction, whereas minimum description length scores each candidate against the corpus already collected.

**Criterion of predictive accuracy**: ^crit-predictive-accuracy

The criterion measures projectibility directly, on objects the construction never used:

1. withhold part of the objects, compute the candidate sets on the rest,
2. score each candidate by how well it still separates and classifies the withheld objects
3. retrain the set retained that generalizes best.

**Criterion of minimum description length**: ^crit-minimum-description-length

This criterion retains is the candidate that compresses the description best. The description length of a candidate set counts:

- *the corpus encoded with that set* — every object written as its values on the retained attributes. With $|V_a|$ values available for the attribute $a$, one value costs $\log_2 |V_a|$ bits, so an object costs the sum of those over the retained attributes, and the corpus costs that sum across objects.
- *the definitions of its attributes* — the rule that operationalizes each retained attribute, written in the description language fixed beforehand, and its length is the length of that rule. The term forbids an attribute encoding the identity of each object: such an attribute does not shorten the corpus, and its own definition then costs as much as the corpus it spares.
- *the implications recovering the attributes it discards* — one implication $R \to a$ per discarded attribute, each costing the attributes that the premise and the conclusion name. When no implication recovers a discarded attribute, its column is stored instead, at the price of the corpus term.

> [!NOTE] Requirements
> That last term (implications) needs the closure of the candidate attribute set, computed in time polynomial in the size of the context.
> It does *not* require the canonical basis from [Formal Concept Analysis](#^formal-concept-analysis): that basis is only a *convenient* way of supplying these derivations.
> However, closures are computed in the [one-valued context](#^def-formal-context), whereas the reducts being scored come from the [many-valued information system](#^def-information-system). So computing the description length requires the scaled context. 

### Exploring attributes

> [!QUOTE] **Attribute exploration** (Ganter, 1987)

If the universe is taken as complete, the basis is computed directly and is complete. However, when the objects already collected form an *unrepresentative sample of the domain*, then the basis computed on them might incorrectly elevate a locally valid implication as a law of the domain.

*Example*: The implication "no bird with a deep beak feeds on nectar" may be a law of the domain, or it may hold only because no deep-beaked nectar feeder was ever collected. 

**Domain expert**: ^def-domain-expert

The method relies on an oracle in the *formal sense* — usually a human specialist, or any effective substitute such as a decision procedure, a simulation, a query against a larger corpus.

**Procedure**: ^attribute-exploration

This algorithm progresses iteratively, starting from the [canonical basis](#^duquenne-guigues-canonical-basis) of a sample context:

1. Each candidate implication of the current basis is presented to the domain expert.
2. The expert either validates it or supplies a counterexample.
3. Each counterexample adds an object to the context, after which the basis is recomputed on the enlarged context.

For a finite attribute set, the process *provably terminates* with a context whose implication theory is complete for the domain.

> [!NOTE]
> The initial basis is a function of a *fixed* context, obtained by enumerating the pseudo-closed sets of that context. The exploration instead *builds* the context whose basis is sought.

### Minimizing conditions for an outcome

> [!QUOTE] **Quine–McCluskey minimization** (Quine, 1952; McCluskey, 1956), applied to comparative research as **qualitative comparative analysis** (Ragin, 1987)

#### Definitions

Specific designs split their vocabulary in two:

- one attribute is designated as an **outcome**, recording a result to be explained,
- the remaining **condition attributes** describe each object.

The information system thereby becomes a **decision system**. The question asked of the vocabulary becomes:

> *Which combinations of condition values suffice for the outcome?*

Sufficiency is meant in its logical sense, and in one direction only: a combination suffices for the outcome when every object exhibiting that combination exhibits the outcome, with no counterexample. The combination is sufficient without being necessary: the outcome may arise from other combinations too.

#### Procedures

 The minimal sufficient conjunctions of the attributes is identified by **Boolean minimization**: ^quine-mccluskey-qca

1. Group the objects into **configurations**, one per combination of values of the condition attributes, each configuration carrying the outcome observed for the objects it holds.
	
2. This truth table defines the **outcome function**, a Boolean function of the condition attributes. 
	
3. Compute the [prime implicants](#^prime-implicants) of the outcome function by **Quine–McCluskey minimization**. It yields the minimal conjunctions of conditions that entail the outcome.
	
4. Select a minimal cover of the positive configurations by prime implicants: the shortest expression that is sufficient for the outcome and accounts for every configuration in which the outcome is observed. Each disjunct of that cover is read as one path to the outcome. 

> [!WARNING] Contradictory configurations
> Two objects may share every condition value and still differ on the outcome. The outcome function is then undefined on that configuration: the pair belongs to $\operatorname{IND}$ of the condition attributes, while the outcome separates it, so the decision system is *inconsistent*. The repairs available:
> - add a condition attribute separating the two objects, and return to eliciting distinctions;
> - or accept the configuration under a consistency threshold, coding it positive when the proportion of objects showing the outcome exceeds a stated level.

> [!WARNING] Limited diversity
> Where no object realizes a configuration, the outcome function stays undefined on that part of the table, and each way of filling the gap yields a different solution:
> - the *complex* solution treats those remainders as negative;
> - the *parsimonious* solution admits them as unconstrained terms;
> - an *intermediate* solution rests on explicit counterfactual assumptions about which remainders would produce the outcome.

#### Comparison with reduction methods

Both reduction and minimization approaches extract the prime implicants of a function. However, they differ on the function and the algorithm.

|           | Reduction methods                                                                                                                            | Minimization method                                                                                                                                               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Question  | Which attributes suffice to distinguish the objects?                                                                                         | Which combinations of condition values suffice for the outcome?                                                                                                   |
| Function  | Discernibility function                                                                                                                      | Outcome function                                                                                                                                                  |
| Algorithm | [Skowron–Rauszer procedure](#^skowron-rauszer-procedure) arrives as a conjunction of clauses and is converted by distribution and absorption | Quine–McCluskey minimization: arrives as a truth table, and its prime implicants are obtained by repeatedly combining configurations that differ on one condition |
| Outcome   | The reducts are the prime implicants of the discernibility function.                                                                         | The minimal sufficient conditions are the prime implicants of the outcome function.                                                                               |

## Comparison between reductions methods

The *canonical* set of attributes returned by [Formal Concept Analysis](#^formal-concept-analysis) is generally **not** a [reduct](#^def-reduct) returned by [Rough Set reduction](#^rough-set-theory). ^reduced-set-versus-reduct

The relation holds in one direction only: 

- The canonical  preserves [discernibility](#^def-indiscernibility) between objects (i.e. it satisfies half of the [reduct's definition](#^def-reduct)). Indeed, every attribute extent is an intersection of irreducible extents, so two objects that the full context separates are still separated by the irreducible attributes alone. Therefore, the reduced attribute set *contains at least one reduct*.
	
- The converse fails (i.e. the minimality clause fails). An irreducible attribute can be removed without merging any two objects, so the reduced set is generally *larger than a reduct*, and a reduct may keep an attribute that this reduction deletes as reducible. The smallest reduct is therefore never larger than the reduced set, and is usually smaller.

This departure is due to the distinct constraints of the methods: 

- the canonical attribute set keeps every attribute whose extent is not recovered by any intersection of the others, 
- a reduct keeps only enough columns to hold the rows apart. 

*Example*: three attributes $a$, $b$, $c$ over four objects, with the extents $\{g_1,g_2\}$, $\{g_2,g_3\}$ and $\{g_1,g_2,g_3\}$:

| object | $a$ | $b$ | $c$ |
| ------ | --- | --- | --- |
| $g_1$  | ×   |     | ×   |
| $g_2$  | ×   | ×   | ×   |
| $g_3$  |     | ×   | ×   |
| $g_4$  |     |     |     |

- Formal Concept Analysis retains the three attributes, since all are irreducible: no intersection of $\{g_2,g_3\}$ and $\{g_1,g_2,g_3\}$ gives $\{g_1,g_2\}$, none of $\{g_1,g_2\}$ and $\{g_1,g_2,g_3\}$ gives $\{g_2,g_3\}$, and none of $\{g_1,g_2\}$ and $\{g_2,g_3\}$ gives $\{g_1,g_2,g_3\}$.
- Rough Set reduction retains two attributes, since the only reduct is the pair $\{a,b\}$: the rows restricted to $a$ and $b$ read $\{a\}$, $\{a,b\}$, $\{b\}$ and the empty set, four distinct rows in all; dropping $a$ merges $g_1$ with $g_2$, and dropping $b$ merges $g_2$ with $g_3$.

Therefore, deleting the attribute $c$ does not costs to discrimination, since no two objects are merged, whereas it changes the lattice, since the extent $\{g_1,g_2,g_3\}$ disappears.

> [!WARNING]
> "Canonicity" is therefore a property of the reduction, and evidence neither that the surviving attributes are the fewest a taxonomy needs, nor that they are the ones its purpose requires.

## Comparison with linear algebra

### Partial analogy

Both conceptual decomposition and linear decomposition (e.g. Principal Component Analysis) pursue a *similar aim*: finding a small set of elements from which every object can be reconstructed. 

However, the structures they operate on differ throughout:

| Linear algebra, PCA                                                                                       | Conceptual spaces                                                                                                 |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Predefined ambient vector space: coordinates already exist numerically                                    | No coordinate system a priori                                                                                     |
| Inner product on the ambient space, where covariance defines "importance" and "orthogonality"             | No canonical metric, no inner product, hence no notion of orthogonality                                           |
| Orthonormal eigenbasis of the covariance, fixed (canonical) up to sign where the eigenvalues are distinct | *Implication basis* (i.e. a basis of the _dependencies_), but multiple *attribute sets* preserve discriminability |
| Bases with invariant cardinality                                                                          | Minimal attribute sets of different cardinalities coexist                                                         |
| Linear independence                                                                                       | Irreducibility                                                                                                    |
| Linear combination                                                                                        | Intersection of extents                                                                                           |
| Subspace lattices are complemented in addition                                                            | Concept lattices need not admit complements, so no attribute set can be projected out of another                  |

Dimensions are treated in the theory of conceptual spaces as respects in which objects are judged similar or different, and they are not required to be independent: some are _integral_, others _separable_, and empirical dimensions co-vary within a domain, itself a set of integral dimensions separable from all others ([Gärdenfors, 2000](https://www.lucs.lu.se/fileadmin/user_upload/project/lucs/PG/pg-2014r.pdf)).

### Closure system versus Vector space

The concept lattice is the qualitative counterpart of the linear span:

- The closed attribute sets are stable under intersection, and the whole set $A$ is one of them, so they form a **closure system** (also called a *Moore family*): every set of attributes has a smallest closed superset, its closure.
- The linear subspaces of a vector space form a closure system of the same kind, with the span as closure operator. 

However, the invariant cardinality of a linear basis rests on a lattice property that a closure system does not inherit:

- The *lattice of linear subspaces* is **modular**: whenever $a \le b$, the identity $a \vee (x \wedge b) = (a \vee x) \wedge b$ holds. Modularity makes a finite lattice graded, so all maximal chains between two comparable elements have equal length, and that common length defines the dimension. Every basis of a subspace therefore has the same number of elements. 
- A *concept lattice* carries no such constraint, since every complete lattice is isomorphic to the concept lattice of some context. No rank function assigns a common length to its chains.

### Additive representation in a qualitative structure

Formally, an additive representation is a relation $\phi(a_1,\dots,a_k) = \sum_i \phi_i(a_i)$, unique up to a common positive multiplier and separate additive constants.

In a qualitative structure, such an additive representation exists under specific conditions, stated by **additive conjoint measurement** (Krantz, Luce, Suppes & Tversky, _Foundations of Measurement_, vol. I, 1971): independence, the Thomsen condition, restricted solvability, the Archimedean axiom. 

Each is an ordinal condition that observations can falsify. So, a numerical decomposition of a qualitative structure rests on **axioms that must be tested rather than assumed**. 

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
