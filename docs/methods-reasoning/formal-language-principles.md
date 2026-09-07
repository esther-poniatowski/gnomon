---
tags:
  - reference
index: "[References and methods](_index.md)"
aliases:
  - Formal reasoning language principles
---
# Design Principles for a Formal Research Reasoning Language

> A structured dialogue on the epistemological and formal foundations of a research-reasoning language, covering adequacy criteria, ontological commitments, operation taxonomies, execution semantics, and the unification of typed objects with atomic moves.

---

## Table of Contents

1. [Initial Question: Design Principles for a Fully Formal Research Reasoning Language](#^design-principles)
2. [Clarifications on Language, Grammar, Ontology, and the Status of Relations](#^vocabulary-clarifications)
3. [Beyond Deduction: A Calculus of Constructive Epistemic Operations](#^operations-calculus)
4. [Extending the Operation Inventory](#^operation-inventory)
5. [From Operation Inventory to Concrete Execution](#^execution-semantics)
6. [Reasoning as Explicit Stepwise Construction](#^stepwise-construction)
7. [Two Foundational Clarifications: Objects-as-Moves and the Rule Catalog](#^objects-as-moves)

---

## 1. Initial Question: Design Principles for a Fully Formal Research Reasoning Language ^design-principles

### Context

A research framework is being designed to formally encode research reasoning. The target language must represent both:

1. **Knowledge contents:**
   - concepts / definitions
   - claims
   - assumptions
   - scope
   - models / frameworks
   - observations / evidence
   - explanations / mechanisms / interpretations
   - uncertainties
   - comparisons / contrasts / correspondences / mappings / analogies
   - taxonomies / classifications
   - examples / counter-examples

2. **Inquiry processes:**
   - epistemic gaps / problems / questions / paradoxes
   - success conditions / admissibility conditions
   - question decomposition / problem analysis
   - case distinctions
   - syntheses / reconstructions
   - resolution plans / proof strategies
   - reusable methods / procedures / heuristics
   - derivations at the finest level (each atomic operation or transformation with its effect)
   - abductive moves
   - revisions
   - alternative approaches
   - rationale
   - transfer affordances
   - potential misconceptions

### Central Constraint

No free-form prose is allowed inside semantic content fields. Every content must be expressed in a fully formal syntax. Natural language may appear only as external comments, labels, or documentation, never as the semantic content of claims, gaps, arguments, explanations, or strategies.

### Preliminary: Reframing the Task

The request conflates two design problems that must be separated before any principle can be stated. The first is the design of a *content language* $\mathcal{L}_C$ adequate for representing scientific knowledge (claims, models, evidence, uncertainties). The second is the design of an *inquiry language* $\mathcal{L}_I$ adequate for representing the dynamics of research (gaps, strategies, derivations, revisions). These are not strata of a single formalism; they obey different logics. $\mathcal{L}_C$ is largely *alethic* and *modal* (truth, possibility, support); $\mathcal{L}_I$ is largely *erotetic*, *deontic*, and *procedural* (questions, admissibility, operations on epistemic states). A unified language is possible only as a controlled coupling of the two via reflection mechanisms — never by collapsing them. Failing to separate them is the first and most pervasive error, because it leads designers to encode questions as propositions and strategies as proofs, destroying the very distinctions the language is meant to make legible.

With that separation in place, the following principles apply.

### Principle 1 — Adequacy is Defined Against a Formal Reconstruction Test, Not Against Coverage

**Principle.** A grammar $G$ is adequate iff there exists a reconstruction function $\rho : \text{ResearchArtifact} \to G$ such that, for any pair of competent reconstructors, $\rho_1(a)$ and $\rho_2(a)$ are *operationally equivalent* under the language's inference rules — i.e., they license the same derivations, support the same queries, and yield the same revisions under the same evidence. Adequacy is thus *behavioral*, not *expressive*.

**Motivation.** "Coverage" — the ability to *write down* something for every artifact in the corpus — is necessary but trivially achievable by allowing opaque tokens. What matters is whether the encoded form *acts* like the artifact under the operations the system supports.

**Consequence.** Every category in the inventory (gaps, abductive moves, rationale, etc.) must be associated, *before* grammar design, with: (i) the inferences it must license, (ii) the queries it must answer, (iii) the transformations it must undergo. The grammar is then a residual: the minimal structure supporting those operations.

**Risk if ignored.** The language becomes a *taxonomic notation* — a structured way to label prose — rather than a calculus. This is the dominant failure mode of ontology-heavy frameworks (cf. much of OBO, parts of CIDOC-CRM): rich vocabulary, negligible inferential yield.

### Principle 2 — The Syntax / Semantics / Ontology / Pragmatics Stratification Must Be Enforced as Independence, Not Layering

**Principle.** The four strata are not a stack; they are *orthogonal commitments* whose intersections must be explicitly governed.

- *Syntax*: the well-formedness conditions on expressions, defined purely combinatorially.
- *Semantics*: the interpretation function $\llbracket \cdot \rrbracket : \mathcal{L} \to \mathcal{M}$ into a model class $\mathcal{M}$ — and the consequence relation $\vDash$ it induces.
- *Ontology*: the commitments about *what exists* in $\mathcal{M}$ (entities, processes, dispositions, events, magnitudes, types). This is a property of $\mathcal{M}$, not of $\mathcal{L}$.
- *Pragmatics*: the conditions under which utterances in $\mathcal{L}$ count as appropriate research moves (assertion, conjecture, retraction, challenge). This is a property of the *use* relation, governed by deontic rules.

**Motivation.** Each stratum has its own failure modes and its own validation criteria. Conflating semantics with ontology produces languages whose meaning shifts when the domain changes; conflating semantics with pragmatics produces languages where logical consequence depends on social context; conflating syntax with semantics produces languages where well-formedness drifts as interpretation is refined.

**Consequence.** The design must produce, as separate artifacts: a formal grammar, a model-theoretic semantics, a domain ontology (or a parameterized family of them), and a pragmatic rule set (an inference-and-commitment calculus in the Brandom–Lance sense, or an update semantics in the DEL sense). Coupling between strata occurs only at named, auditable interfaces.

**Risk if ignored.** Semantic drift: the "same" expression means different things to different users, and disagreements about content become indistinguishable from disagreements about logic or about norms of inquiry.

### Principle 3 — Primitives Must Be Chosen by Closure Under the Required Operations, Not by Ontological Intuition

**Principle.** A category $C$ deserves primitive status iff (i) the required operations on $\mathcal{L}$ are not closed without it, or (ii) defining $C$ from other primitives forces structurally unstable encodings.

**Motivation.** Primitive selection is the most consequential decision in language design and the most often made on aesthetic or intuitive grounds. The correct criterion is operational closure: if revising a claim requires identifying *which sub-claim* was retracted and *what dependencies* fall, then claims must be structured objects with addressable parts and an explicit dependency relation — not strings, not opaque atoms.

**Consequence.** The candidate primitives derive from the operations enumerated in the task, not from the content categories. A non-exhaustive list:

- *Propositions* with internal structure (predicate–argument, with terms drawn from a typed signature).
- *Judgments* — propositions under an epistemic modality and an agent index: $a :_{\text{conj}}^{t} \varphi$ (agent $a$ conjectures $\varphi$ at stage $t$).
- *Questions* as partitions of a possibility space (à la Hamblin / Groenendijk–Stokhof) or as sets of direct answers with a presupposition lattice (à la Wiśniewski's IEL).
- *Dependency edges* — typed relations between judgments (evidential support, presupposition, refutation, decomposition, abductive jump).
- *Epistemic states* — finite structures over judgments and questions, closed under the calculus's update operations.
- *Derivations* — proof-theoretic objects whose nodes are inference-rule applications, not whose labels are strings.
- *Plans* — partially ordered sets of intended operations on epistemic states, with preconditions and postconditions (the STRIPS/HTN framing already engaged with).
- *Schemas* — second-order objects abstracting over the above to support reuse and transfer.

Concepts, taxonomies, examples, and analogies are *not* primitives at this level; they are constructions over the primitives (a taxonomy is a relation on predicate symbols; an analogy is a partial homomorphism between sub-models).

**Risk if ignored.** A bloated primitive layer whose categories overlap and whose operations are partial — the system can represent everything and reason about nothing.

### Principle 4 — Full Formalization Is Not Equivalent to Typed Field Schemas, and the Test Is Compositional Substitution

**Principle.** A field is genuinely formal iff its content can be substituted, in any expression where it occurs, by any other content of the same type *salva congruentia* — i.e., the well-formedness, semantics, and inferential behavior of the enclosing expression depend only on the type and structure of the substituted content, never on its prose.

**Motivation.** This is the operational version of Frege's context principle and the categorial-grammar discipline. Typed fields containing prose (`claim: "All swans are white"`) fail the test: the enclosing system cannot detect that swapping in `"Some swans are white"` changes the entailment structure. The string is type-correct but semantically opaque.

**Consequence.** Every semantic field must contain an expression of $\mathcal{L}_C$ or $\mathcal{L}_I$, where these languages are themselves defined by a formal grammar with a model-theoretic interpretation. Natural-language strings are permitted *only* as values of fields explicitly typed `Annotation`, `Label`, or `Documentation`, which by construction play no role in the calculus. This means uncertainties cannot be `"high"` or `"moderate"`; they must be elements of a formally defined uncertainty algebra (an imprecise-probability structure, a possibility measure, a ranking function, a Dempster–Shafer mass function — the choice itself being a deliberate semantic commitment).

**Sufficiency question.** Can a sufficiently refined typed system eliminate prose entirely? *In principle, yes — provided the type system is dependent and the signatures are open.* A dependent type theory in the Martin-Löf or HoTT tradition can encode propositions, proofs, equivalences, and revisions uniformly; an open signature allows domain vocabulary to be introduced as needed without polluting the core. *In practice, the bottleneck is not expressive power but the cost of axiomatizing the domain* — every predicate introduced demands inference rules, or it remains an opaque atom (Principle 1 violation in microcosm). Eliminating prose is therefore not a binary achievement but a *gradient* parameterized by the depth of domain axiomatization the project can afford.

**Risk if ignored.** *Cosmetic formalism* — the most insidious failure. The artifact looks like a knowledge graph; its nodes contain English; the surrounding tooling cannot tell the difference between a valid inference and a non-sequitur because the inferential content lives in the prose, not in the structure.

### Principle 5 — The Quadrilemma of Expressivity, Manipulability, Rigor, and Usability Has No Global Optimum and Must Be Resolved Per Layer

**Principle.** Expressivity (what can be said), manipulability (what computations are tractable), rigor (what guarantees hold), and usability (what humans can produce and read) are pairwise in tension. They cannot be jointly maximized; they must be *allocated* across the language's strata.

**Motivation.** Lindström's theorem and the standard expressivity–decidability trade-offs in description logic make the formal version of this point: every gain in one dimension is paid elsewhere. Pretending otherwise produces languages that are simultaneously too weak to encode interesting science and too rich to support automated checking.

**Consequence.** The design must explicitly stratify:

- A *core* language with strong rigor and tractable manipulability (e.g., a fragment with decidable consequence — perhaps a guarded fragment or a description-logic-like core for the static content layer).
- An *extended* language with higher expressivity (full first-order, modal, or dependently typed) for content that exceeds the core, with explicit markers at the boundary.
- A *surface* layer optimized for usability — controlled natural language, structured editors, projectional syntax — provably compiled to the core/extended layers.

Each layer has its own adequacy criterion (Principle 1). Usability is *not* a property of the core grammar; it is the responsibility of the surface layer, and the two must not be conflated.

**Risk if ignored.** Either an unusable formalism that no researcher will adopt, or a usable notation that licenses no real inferences — both common, both fatal.

### Principle 6 — Methodological Path: Bottom-Up Calibration on Hard Cases, Not Top-Down Axiomatization

**Principle.** The language must be designed by iteratively reconstructing *paradigmatic difficult artifacts* — not by elaborating an a priori ontology of research.

**Motivation.** Top-down designs encode the designer's epistemology, not the epistemology of the practice being formalized. Bottom-up calibration exposes which distinctions actually do work and which are decorative.

**Consequence — a concrete methodology.**

1. *Corpus selection.* Assemble a small, heterogeneous set of canonical research episodes spanning the categories in the inventory — episodes where the distinctions matter (e.g., a paradox-resolution case, a reanalysis-after-evidence case, a successful analogy transfer, a failed abductive move corrected by a reviewer). Ten to twenty episodes is enough; representativeness matters more than volume.
2. *Operation specification.* For each episode, list the operations the language must support: which inferences must be drawable, which queries answerable, which revisions reconstructible.
3. *Primitive distillation.* From the union of required operations, derive the minimal primitive set (Principle 3).
4. *Semantics first, then syntax.* Specify the model class $\mathcal{M}$ and the consequence relation $\vDash$ before fixing concrete syntax. Syntax should be a *presentation* of the semantics, not its source.
5. *Stratified grammar.* Construct the core grammar to be sound and complete w.r.t. a tractable fragment of $\vDash$; specify the extensions and their boundary conditions.
6. *Reconstruction test.* Re-encode the corpus episodes. Where reconstruction is forced into `Annotation` fields, the language is incomplete: extend or refine. Where two encodings of the same episode behave differently under the calculus, the semantics is ambiguous: refine.
7. *Adversarial cases.* Construct cases the language *should not* express (category errors, ill-typed analogies, vacuous abductions). Verify the type system rejects them.
8. *Pragmatic calibration.* Specify the commitment-and-entitlement rules governing assertion, retraction, and challenge. Verify that ordinary research moves (peer critique, revision after evidence) are reconstructible as sequences of these rules.
9. *Surface layer.* Only now design the human-facing syntax and tooling.

**Risk if ignored.** A language that elegantly handles the cases its designer imagined and silently mutilates everything else.

### Principle 7 — Catalog of Design Errors That Produce Only Superficial Formalism

The principles above can be summarized negatively, as a checklist of errors each of which suffices to reduce a formalism to decoration:

1. *Prose-in-typed-fields.* Semantic content carried by strings inside structurally typed records. Defeats Principle 4.
2. *Taxonomic inflation.* Multiplying categories without specifying operations on them. Defeats Principle 1.
3. *Stratum confusion.* Encoding pragmatic moves (assertion, retraction) as semantic content, or encoding ontological commitments as syntactic conventions. Defeats Principle 2.
4. *Question-as-proposition.* Representing $?\varphi$ as a proposition asserting that $\varphi$ is unknown, rather than as an erotetic object with its own admissibility and resolution conditions. Collapses $\mathcal{L}_I$ into $\mathcal{L}_C$.
5. *Strategy-as-derivation.* Conflating *plans to prove* with *proofs*, losing the distinction between intended and achieved inference, and thereby making revisions and abandoned approaches inexpressible.
6. *Uncertainty-as-label.* Treating epistemic statuses as enumerated tags rather than as elements of a formal uncertainty calculus. Makes aggregation, propagation, and revision incoherent.
7. *Opaque atoms.* Predicates introduced without inference rules. The system cannot reason about their content; they function as prose in disguise.
8. *Closed-world ontology.* Fixing the domain vocabulary in advance, forcing every new scientific concept to be smuggled in as an annotation.
9. *Single-layer ambition.* Attempting a single grammar that is simultaneously expressive, decidable, and writable by humans. Violates Principle 5; produces a language that fails at all three.
10. *Validation by example.* Declaring the language adequate because example encodings "look right," rather than because they pass the reconstruction test (Principle 1) and the substitution test (Principle 4).
11. *Designer-as-oracle.* Resolving ambiguities by the designer's intuition rather than by appeal to the semantics. Indicates the semantics is underspecified.
12. *Surface-syntax-first.* Designing the human-facing notation before the model theory, then retrofitting semantics. Guarantees that the formal layer is a rationalization rather than a foundation.

### Synthesis

The deepest commitment is this: a formal research-reasoning language is a *calculus on epistemic states*, not a *notation for research artifacts*. Its primitives are chosen by the operations it must support; its semantics fixes a class of models and a consequence relation; its syntax is a presentation of that semantics; its pragmatics governs the use of expressions as research moves; and its surface form is engineered separately for human production and inspection. The categories in the original inventory — concepts, claims, gaps, strategies, revisions — are *not* the units of design; they are the *test cases* against which the calculus is calibrated. Designing in the reverse direction — starting from the inventory and reaching for grammar — is the standard path to a system that is formal in appearance and informal in substance.

---

## 2. Clarifications on Language, Grammar, Ontology, and the Status of Relations ^vocabulary-clarifications

### Questions

1. The framework was initially presented as providing a "language" based on typed "objects", "relations" and "operations". The answer emphasized the notion of "content language", "inquiry language", "formal grammar", "model", "expressions", "domain ontology". What are the differences between these notions? Are some of them synonyms or overlapping? How are "relations" and "operations" represented or expressed?
2. Any relation seems reducible to a typed tuple of objects and thus reifiable as a composite (non-primitive) object. Is that correct? Does it have consequences? Is there a tension between ontology size and language power?

### 2.1 Disentangling the Vocabulary

The terms in question are not synonymous, but they are systematically related, and the temptation to identify them is the source of much confusion. The clearest way to disentangle them is to recognize that they live at *different levels of the design* and answer *different questions*.

#### The Four Levels and What Each Answers

| Level | Question it answers | Artifact at this level |
|---|---|---|
| **Syntactic** | What strings (or trees, or graphs) count as well-formed? | A **formal grammar** generating a set of **expressions** |
| **Semantic** | What do well-formed expressions mean? | A **model class** $\mathcal{M}$ and an interpretation $\llbracket \cdot \rrbracket$ |
| **Ontological** | What exists in the models? | A **domain ontology** — the signature and axioms fixing the inhabitants of $\mathcal{M}$ |
| **Pragmatic** | What does it mean to *use* an expression? | A **commitment calculus** governing assertion, retraction, challenge |

A **formal language** $\mathcal{L}$ is the whole stack: a grammar, plus an interpretation into a model class whose inhabitants are fixed by an ontology, plus rules of use. To call $\mathcal{L}$ a "language" is shorthand for this entire apparatus. When the previous response distinguished a *content language* $\mathcal{L}_C$ from an *inquiry language* $\mathcal{L}_I$, the distinction was at this whole-stack level: two different calculi, each with its own grammar, semantics, ontology, and pragmatics, designed to handle different kinds of objects (propositions about the world vs. questions and operations on epistemic states).

#### Where "Typed Objects, Relations, Operations" Fits

The original framing — "typed objects, relations, operations" — is a description at the *ontological* level. It specifies what the models contain:

- **Objects** are the inhabitants of the domain (or rather, of typed sub-domains $D_\tau$ indexed by types $\tau$).
- **Relations** are subsets $R \subseteq D_{\tau_1} \times \cdots \times D_{\tau_n}$ — that is, sets of tuples of typed objects, picked out by relation symbols in the signature.
- **Operations** are functions $f : D_{\tau_1} \times \cdots \times D_{\tau_n} \to D_{\tau_0}$ — picked out by function symbols in the signature.

This is the standard structure of a *many-sorted first-order signature* $\Sigma = (\mathcal{T}, \mathcal{F}, \mathcal{R})$ comprising types, function symbols, and relation symbols. The signature is the syntactic skeleton of the ontology; the ontology proper is the signature plus the *axioms* constraining how its symbols may be jointly interpreted.

The grammar is then a presentation device that lets one *write* expressions — terms $t$ built from function symbols, atomic formulas $R(t_1, \ldots, t_n)$ built from relation symbols, and compound formulas built by logical connectives and binders. The model interprets each symbol of $\Sigma$ as an actual set, function, or relation in some structure $\mathfrak{A}$.

#### The Correspondence

Schematically:

$$
\underbrace{\text{Objects, Relations, Operations}}_{\text{ontology}} \;\xrightarrow{\text{symbolized by}}\; \underbrace{\Sigma = (\mathcal{T}, \mathcal{F}, \mathcal{R})}_{\text{signature}} \;\xrightarrow{\text{generates}}\; \underbrace{\text{Expressions}}_{\text{syntax via grammar}} \;\xrightarrow{\llbracket \cdot \rrbracket}\; \underbrace{\mathfrak{A} \in \mathcal{M}}_{\text{semantics}}
$$

The original formulation was not wrong; it was *one slice* through the design — the ontological slice, which fixes what the language talks *about*. The previous response added the slices that fix how the language talks *at all* (grammar), what its talk *means* (model theory), and what its talk *does* in inquiry (pragmatics).

#### How Relations and Operations Are Represented in Expressions

In the syntax of the language, relations and operations are not themselves first-class objects (by default); they appear as *symbols* applied to argument expressions. If $R$ is a binary relation symbol of type $\tau_1 \times \tau_2$, then $R(t_1, t_2)$ — where $t_1$ has type $\tau_1$ and $t_2$ has type $\tau_2$ — is an atomic formula. If $f$ is a function symbol of type $\tau_1 \times \tau_2 \to \tau_0$, then $f(t_1, t_2)$ is a term of type $\tau_0$.

This is the default. *Whether relations and operations can also be treated as objects* — argument positions, quantified over, manipulated — is precisely the question of section 2.2 below.

### 2.2 Reification of Relations: Is It Always Possible, and What Does It Cost?

The question — "can any relation be reduced to a typed tuple of objects and thus reified as a composite non-primitive object?" — is sharp and the answer is *yes in principle, but with structural costs that govern the central design tension*.

#### The Reification Operation

Given a relation $R \subseteq D_{\tau_1} \times \cdots \times D_{\tau_n}$, one can introduce a new type $\tau_R$ and a bijection between the extension of $R$ and a subdomain of $\tau_R$. Each tuple $(a_1, \ldots, a_n) \in R$ becomes an object $r \in \tau_R$, equipped with projection functions $\pi_i(r) = a_i$ recovering the components, and a discrimination predicate marking $r$ as an $R$-instance.

Concretely, the atomic formula $\mathrm{supports}(e, c)$ (a relation between an evidence item $e$ and a claim $c$) can be replaced by:

$$
\exists s : \mathrm{Support}.\; \mathrm{evidence}(s) = e \;\wedge\; \mathrm{claim}(s) = c
$$

where $\mathrm{Support}$ is a new type whose inhabitants are support-events, with two projection functions. The relation has been *reified*: it is no longer a fact relating two objects but an object in its own right, about which further facts can be stated (its strength, its provenance, its date, whether it has been retracted).

This is the standard *Davidsonian* or *neo-Davidsonian* move (events as first-class entities), and it is the technique behind RDF reification, named graphs, and the property-graph model.

#### Yes, It Is Always Possible — At a Cost

Formally, reification is always available: for any relation symbol $R$ of arity $n$, one can introduce $\tau_R$ with $n$ projections and an axiom

$$
\forall r : \tau_R.\; R(\pi_1(r), \ldots, \pi_n(r))
$$

plus existence axioms enforcing the bijection. The reified theory and the original theory are *mutually interpretable*; they say the same things in the same models, modulo renaming.

The costs are real and shape the design:

**(a) Quantifier complexity.** Each reification introduces an existential quantifier in the unfolded form. Aggressive reification can push expressions out of decidable fragments.

**(b) Identity criteria.** Once a relation is reified into a type, one must specify *when two instances are equal*. The answer is not given by reification itself; it must be added as an axiom (extensional vs. intensional identity).

**(c) Schema proliferation.** Every reified relation is a new type, with its own well-formedness rules, its own axioms, and its own tooling support. The ontology grows.

**(d) Loss of structural cues.** When `supports(e, c)` is a relation symbol, the grammar enforces that exactly two arguments of the right types appear. When it is a reified type with projections, the structural enforcement must be carried by axioms or by the type system.

#### The Real Consequence: A Design Knob, Not a Trap

Reification is best viewed as a *design knob* one turns deliberately, not a universal solvent. The criterion for turning it is whether the relation must itself become an *object of discourse* — something one quantifies over, attaches further predicates to, or operates upon.

- Keep $R$ as a relation symbol when $R$-facts are *terminal*: they participate in formulas but no further facts are stated *about them*.
- Reify $R$ to type $\tau_R$ when one must state facts *about $R$-instances themselves* — their provenance, strength, temporal extent, revision history, the rationale that produced them.

For a research-reasoning language, relations representing *epistemic links* (evidential support, presupposition, refutation, decomposition, abductive jump) almost always need reification, because the language must talk *about* those links — annotate them with strength, retract them, compare alternative supports for the same claim. Relations representing *typing or membership* typically should not be reified — they are terminal.

#### The Tension With Ontology Size: Diagnosis and Resolution

The previous warning about "ontology-heavy frameworks" was not against having many objects but against a specific failure pattern:

> *Adding categories (types, relation symbols, reified relations) without adding the inference rules, axioms, and operations that give those categories computational content.*

OBO and CIDOC-CRM accumulate hundreds of classes and relations — many of them reifications — but the *axiomatic content* per category is thin. The result is that the ontology can *label* a claim as "Support" or "Causes" or "Influences," but the calculus cannot do much *with* that label.

The resolution principle:

> **Reification is justified iff the axioms governing the reified type license inferences that were unavailable without it.**

#### A Concrete Heuristic

For each candidate category, the designer should answer three questions before granting it primitive (or reified-type) status:

1. *What new expressions become well-formed because this category exists?*
2. *What new inferences does the calculus license once axioms governing this category are added?*
3. *What operations on epistemic states does this category make tractable that were intractable without it?*

A category that scores zero on all three is a labeling convention masquerading as ontology.

### Synthesis

The terms are arranged thus: *objects, relations, operations* describe the **ontology**; the **signature** symbolizes them; the **grammar** uses the signature to generate **expressions**; the **semantics** interprets expressions in **models** built from the ontology; the **pragmatics** governs the use of expressions in inquiry. All of these together compose a **formal language**.

Relations are reducible to reified objects via the standard construction, and this reduction is always available in principle, but it is a *tool with costs* — quantifier complexity, identity-criterion debt, schema growth, weakened structural enforcement — and its use should be governed by a single criterion: reify exactly when the relation must become an object of further discourse.

---

## 3. Beyond Deduction: A Calculus of Constructive Epistemic Operations ^operations-calculus

### Question

The previous analysis seems strongly focused on deductive moves. In real research, many operations are not deductions: constructing concepts, taxonomies, comparing, contrasting, illustrating, generalizing, transferring, questioning. How should such activities be handled?

### Preliminary Diagnosis

The observation is correct and identifies a real bias. The bias has a specific source: model-theoretic semantics and proof-theoretic adequacy criteria were developed for *truth-preserving* inference, and importing them wholesale produces a language in which the only operations that "count" are those that preserve truth from premises to conclusions. Most research activity is not of this kind. Concept construction, taxonomic carving, analogical transfer, generalization, and the very act of asking a question are not truth-preserving — they are *structure-producing*, *structure-modifying*, or *structure-relating* operations on epistemic states.

The error to avoid, however, is the opposite one: concluding that non-deductive moves are *informal* and must therefore be left to prose. They are not informal; they are *differently formal*. Each has a precise structure, and the literature already contains substantial formal accounts.

### 3.1 The Right Generalization: From Inference to Update

The unifying abstraction is not *inference* but *update on epistemic states*. A research operation is, in general, a partial function

$$
\mathrm{op} : \mathcal{S} \rightharpoonup \mathcal{S}
$$

where $\mathcal{S}$ is the space of admissible epistemic states. Deduction is the special case where (i) the state is a set of judgments, (ii) the update only adds judgments, and (iii) the addition preserves a truth-functional invariant.

The state space $\mathcal{S}$ must include at least:

- a **signature** $\Sigma$ (current vocabulary: types, predicates, functions);
- a **theory** $T$ over $\Sigma$ (current axioms, definitions, observations);
- a **question agenda** $Q$ (open inquiries, partitions, presupposition lattices);
- a **construction history** $H$ (provenance: which moves produced which elements);
- a set of **commitments** $\Pi$ (endorsement status of each item: asserted, conjectured, suspended);
- an **uncertainty assignment** $U$ over $T$;
- a set of **schemas** $\mathcal{X}$ (reusable structures available for transfer);
- a set of **structural mappings** $M$ (recognized correspondences with other states or sub-states).

An epistemic state is a tuple $s = \langle \Sigma, T, Q, H, \Pi, U, \mathcal{X}, M \rangle$.

### 3.2 Concept Construction

Concept construction enlarges $\Sigma$. Several discrete species:

**Explicit definition.** $P(\bar{x}) \;\stackrel{\mathrm{def}}{=}\; \varphi(\bar{x})$ where $\varphi$ is already in $\Sigma$. Conservative.

**Implicit definition.** A new symbol constrained by axioms but not eliminable. The Beth definability theorem governs when implicit definitions can be made explicit.

**Abstraction principle.** A new sort introduced via an equivalence relation: $\#x = \#y \leftrightarrow x \sim y$.

**Inductive / coinductive specification.** A type constructed by generators and recursors, or by observers and corecursors.

**Quotient construction.** A new type as the quotient of an existing one by an equivalence relation.

The state transition is:

$$
s = \langle \Sigma, T, \ldots \rangle \;\longmapsto\; s' = \langle \Sigma \cup \{P\}, T \cup \mathrm{Ax}(P), \ldots \rangle
$$

### 3.3 Taxonomy and Classification

Taxonomies are *structured relations on predicate symbols*. A taxonomy over a domain is a (typically partial) order on a set of predicates, plus coherence axioms (subsumption, disjointness, covering).

Two formal moves: **Carving** (introducing children with subsumption, pairwise disjointness, and covering axioms) and **Rearrangement** (restructuring an existing taxonomy).

A taxonomy is *admissible* iff its axioms are jointly satisfiable and its carving criterion is recorded.

### 3.4 Comparison, Contrast, Correspondence, Analogy

These four are formally cognate and best treated as variants of a single construction: a *structural mapping* between sub-states.

A structural mapping is a partial homomorphism

$$
\mu : \langle \Sigma_1, T_1 \rangle \rightharpoonup \langle \Sigma_2, T_2 \rangle
$$

that sends symbols of $\Sigma_1$ to symbols (or compound expressions) of $\Sigma_2$ and that preserves a designated subset of $T_1$.

- **Comparison** = construction of $\mu$ with record of preserved and non-preserved axioms.
- **Contrast** = comparison where salient content is non-preserved axioms.
- **Correspondence / mapping** = comparison where $\mu$ preserves the full relevant structure.
- **Analogy** = comparison where $\mu$ preserves relational structure but underlying objects differ in type, aimed at *transfer*.

### 3.5 Generalization and Specialization

A generalization of theory $T$ is a theory $T^*$ together with an interpretation $\iota : T^* \to T$ — a translation of $T^*$'s symbols into $T$'s vocabulary under which $T^*$'s axioms are theorems of $T$.

Several distinct moves cluster here: **parametric**, **schematic**, **axiomatic**, and **concept** generalization. Specialization is the inverse construction.

### 3.6 Transfer

Given a mapping $\mu : \langle \Sigma_1, T_1 \rangle \rightharpoonup \langle \Sigma_2, T_2 \rangle$ and a statement $\varphi$ true in $T_1$, the *transfer of $\varphi$ along $\mu$* is the conjecture $\mu(\varphi)$ in $T_2$.

$$
\frac{T_1 \vdash \varphi \qquad \mu : T_1 \rightharpoonup T_2}{T_2 \;?\vdash\; \mu(\varphi)}
$$

The conjecture enters $T_2$ tagged as transferred, with $\mu$ and $\varphi$ as its provenance.

### 3.7 Illustration and Exemplification

Three moves: **witness construction** (from existence proof to witnessing term), **model exhibition** (exhibiting $\mathfrak{A} \models T$), **counter-example construction**.

### 3.8 Questioning

Adopting Wiśniewski's *Inferential Erotetic Logic* or the partition semantics of Groenendijk–Stokhof, a question $?\Phi$ is determined by its *set of direct answers* and its *presuppositions*. Operations include:

- **Posing**, **Decomposition**, **Reformulation**, **Refinement**, **Dissolution**, **Resolution**.

### 3.9 Revision and Retraction

AGM revision operations: **Expansion**, **Contraction**, **Revision**. Governed by an *entrenchment* ordering — itself an object in $\Pi$.

### 3.10 Abduction

Abduction is the inference from $\varphi$ and a candidate explanation $\psi$ (such that $T \cup \{\psi\} \vdash \varphi$ and $T \not\vdash \varphi$) to the *conjecture* of $\psi$.

### 3.11 The Integrating Framework

The shape that emerges is a *dynamic logic of inquiry* — a calculus whose objects include not only judgments but signatures, questions, mappings, schemas, and commitment structures. Each operation has a formal type:

$$
\mathrm{op} : \mathrm{Pre} \to \mathrm{Post}, \quad \mathrm{Pre}, \mathrm{Post} \subseteq \mathcal{S}
$$

with a precondition, an effect, and an invariant. The invariants differ: deduction preserves truth-in-models; concept construction preserves prior content (under conservativity); revision preserves maximal coherence; transfer preserves structural homomorphism. *No single invariant governs all moves* — and demanding one is the deep mistake that produces the deductive bias.

### 3.12 What This Means for Language Design

**(a) The state space must be rich.** $\Sigma, Q, H, \Pi, U, \mathcal{X}, M$ as enumerated, each a typed object with its own operations.

**(b) Operations must be first-class.** Each operation type (`construct-concept`, `carve-taxonomy`, `pose-question`, `decompose-question`, `compare`, `transfer`, `revise`, `abduce`, etc.) is a typed object in the language.

**(c) Commitment must be orthogonal to content.** The same content $\varphi$ can be asserted, conjectured, suspended, transferred, or abductively introduced. These differ not in $\varphi$ but in its tag in $\Pi$.

### Synthesis

Once $\mathcal{S}$ is enlarged to include signatures, questions, mappings, schemas, and commitments, the non-deductive moves become formal operations of the same kind as deduction — partial functions on $\mathcal{S}$ with preconditions, effects, and invariants. The framework is therefore a *calculus of epistemic state dynamics*, of which deductive proof theory is one component among several.

---

## 4. Extending the Operation Inventory ^operation-inventory

### Question

Are there other operations to include in a research and reasoning framework beyond concept construction, taxonomic carving, comparison, generalization, transfer, exemplification, questioning, revision, and abduction?

### Methodological Note

Three filters for primitive status:

1. **Irreducibility.** Not a derived combination of operations already in the inventory.
2. **Distinctive type signature.** Precondition, effect, or invariant not shared by any existing primitive.
3. **Inferential or organizational yield.** Recording the operation enables queries, revisions, or transfers that would be unavailable otherwise.

### 4.1 Operations on the Question Space

**Presupposition extraction.** Isolate $\mathrm{pres}(?\Phi)$ — the propositions that must hold for $?\Phi$ to admit any direct answer.

**Question composition.** $?\Phi_1 \wedge ?\Phi_2$ (joint question) or $?\Phi_1 ; ?\Phi_2$ (sequential question).

**Question relativization.** $?\Phi \mid \psi$ — the conditional question asked under the assumption $\psi$.

**Erotetic search.** Identify which axioms or observations in $T$ are *erotetically relevant* to $?\Phi$.

### 4.2 Observation and Measurement

**Observation.** Adding $\langle d, c, p \rangle$ to $T$, where $d$ is data, $c$ is conditions of production, $p$ is precision/uncertainty.

**Measurement.** Specialization with operational definition.

**Selection / sampling.** Choice of which entities to observe, with sampling frame recorded.

**Instrument calibration.** Meta-operation that adjusts measurement procedure parameters.

### 4.3 Idealization, Abstraction, and Approximation

**Idealization.** Deliberate counterfactual simplification with explicit distortion relation.

**Abstraction.** Truth-preserving suppression of detail by quotienting or projection.

**Approximation.** Replacement of exact statement by tractable one with recorded error bound.

Their *revision profiles* differ: idealizations are revised by *de-idealization*; abstractions by *refinement*; approximations by *tightening the bound*.

### 4.4 Decomposition and Composition of Content

**Theory factorization.** Decomposition into modules with inter-module dependency structure.

**Mechanism decomposition.** Identify components, activities, organizational features (Glennan / MDC sense).

**Compositional construction.** Building larger theories with explicit *bridge axioms*.

### 4.5 Operations on Commitments and Their Sources

**Endorsement.** Promote from `conjectured` to `asserted` with recorded grounds.

**Suspension.** Move to neither endorsed nor denied — distinct from contraction.

**Provenance attribution.** Attach source: who produced it, by what operation, under what conditions.

**Source credibility revision.** Update credibility weight on a source.

**Disagreement registration.** Record incompatible commitments without immediate revision.

### 4.6 Operations on the Schema Repository

**Schema extraction.** From successful local construction, abstract a reusable pattern with applicability conditions.

**Schema instantiation.** Apply $X \in \mathcal{X}$ to a new situation.

**Schema refinement.** Update applicability conditions based on accumulated successes and failures.

### 4.7 Evaluation, Diagnosis, and Calibration

**Adequacy assessment.** Produce a structured judgment of whether $T$ is adequate for a target.

**Anomaly identification.** Recognize a tension between $T$ and an observation that does not yet warrant revision.

**Coherence check.** Audit $T$ for internal coherence.

**Robustness analysis.** Identify which axioms of $T$ are essential for the derivation of $\varphi$.

### 4.8 Communicative and Coordinative Operations

**Translation.** Restate content in target vocabulary while preserving commitments.

**Explication.** Replace informal concept with precise one (Carnap).

**Convention establishment.** Fix notation, default interpretation, or measurement unit.

**Default establishment.** Specify behavior in absence of specific information.

### 4.9 Planning, Strategy, and Meta-Reasoning

**Plan construction**, **Plan execution**, **Plan revision**, **Strategy selection**, **Reflection**.

### 4.10 Anticipation and Counterfactual Operations

**Prediction**, **Retrodiction**, **Counterfactual exploration**, **Intervention simulation** (Pearl sense).

### 4.11 Boundary Operations: Scope and Domain

**Scope specification**, **Domain extension**, **Scope restriction**.

### 4.12 The Updated Inventory

- **Content construction:** concept construction, taxonomic carving, explication, convention establishment, default establishment.
- **Empirical input:** observation, measurement, selection, instrument calibration.
- **Inferential and explanatory:** deduction, abduction, prediction, retrodiction.
- **Structural and relational:** comparison, contrast, correspondence, analogy, generalization, specialization, transfer.
- **Decompositional and compositional:** theory factorization, mechanism decomposition, compositional construction, schema extraction, schema instantiation, schema refinement.
- **Modificatory:** idealization, abstraction, approximation, scope specification, scope extension, scope restriction.
- **Exemplificatory:** witness construction, model exhibition, counter-example construction.
- **Erotetic:** posing, decomposition, reformulation, refinement, dissolution, resolution, presupposition extraction, question composition, question relativization, erotetic search.
- **Doxastic:** expansion, contraction, revision, endorsement, suspension, provenance attribution, source credibility revision, disagreement registration.
- **Evaluative:** adequacy assessment, anomaly identification, coherence check, robustness analysis.
- **Meta-strategic:** plan construction, plan execution, plan revision, strategy selection, reflection.
- **Counterfactual:** counterfactual exploration, intervention simulation.
- **Communicative:** translation.

### 4.13 Caveat About Completeness

This inventory is not closed by fiat. The corpus method of Principle 6 applies. Two qualifications:

First, certain operations may be *domain-relative* (experimental design, mathematical proof normalization). The core inventory is the genus; domain-specific specializations are species added as needed.

Second, certain operations are emerging or contested (computational simulation as an epistemic operation). Operations not yet philosophically settled should be included with provisional signatures and explicit flags.

The right disposition: *open-ended but principled*.

---

## 5. From Operation Inventory to Concrete Execution ^execution-semantics

### Question

Once the objects and operations are defined, how should a user manipulate them? It is not sufficient to "call" a "function" that represents an operation for it to be concretely executed, in the sense of creating outputs that advance the epistemic state.

### The Core Problem

An inventory of operations defines a *type system* but not an execution semantics. Writing `compare(T_1, T_2)` no more produces a comparison than writing `integrate(f, a, b)` produces an integral.

**Note: this section's framing was substantively revised in §6 below.** The execution-mode stratification (algorithmic / constructive / recorded) presented here treats some reasoning as happening *to* the state through opaque mechanisms — only the result enters the formal record. This reintroduces, at the level of operations, the prose-in-fields failure the framework was designed to eliminate. The corrected position is presented in §6. The original draft is retained here for completeness and to make the revision visible.

### 5.1 The Execution Model: Three Modes (Original Draft, Superseded)

**Mode A — Algorithmic.** The operation is fully computable: deductive inference in a decidable fragment, AGM revision under specified entrenchment, taxonomic restructuring under stated criteria, conservativity checking, robustness analysis, coherence checking, schema instantiation.

**Mode B — Constructive with System Support.** The operation requires content that the system cannot generate but can *constrain*, *propose candidates for*, and *verify*: concept construction, abduction, structural mapping construction, counter-example construction, idealization, explication, measurement.

**Mode C — Recorded, with Coherence Maintenance.** The operation's content is essentially outside the system: observation, sampling decisions, instrument calibration, source credibility judgments, endorsement, disagreement registration, scope specification, convention establishment, anomaly identification, strategy selection.

### 5.2 The Invocation Interface

Operation selection (direct or goal-driven), input specification (selection for Mode A, content authoring for Mode B, record completeness for Mode C), parameter specification, output integration (transactional with previewed consequences).

### 5.3 The Constraint and Verification Layer

Three layers of constraint:

- *Type constraints*: structural shape.
- *Axiomatic constraints*: logical conditions (conservativity, abductive vetting, preservation).
- *Pragmatic constraints*: recorded grounds, conditions of production, source mappings.

Verification strategies stratify: decide what is decidable, automate what is automatable, demand user-supplied certificates where automation is infeasible.

**Verification debt as first-class.** When an operation result is accepted without full verification, the state records this as a *verification debt* — the unverified claim, the constraint that should have been checked, the reason verification was not completed, the conditions for retry.

### 5.4 Workflow Architecture: Operations in Sequence

**The inquiry trace.** Every executed operation recorded as a typed event with type, inputs, parameters, output, state delta, verification status, agent, time, rationale.

**Plans as pre-operations.** Plans are *anticipated* operation sequences with preconditions and expected effects.

**Dependency tracking and reactive updates.** Truth maintenance (downgrade items downstream of retracted content) and change propagation (re-derive items downstream of modified content).

**Views and projections.** Filtered, structured projections of the state suited to specific tasks.

### 5.5 What Concretely Advances the Epistemic State

An operation advances the state when its output is integrated in a way that changes what the state can answer, support, or derive. Five forms:

1. **Content addition** — non-redundant, consequence-bearing.
2. **Content removal or modification** — resolves tracked tension, eliminates vulnerability.
3. **Structural enrichment** — new mapping, schema, or dependency edge.
4. **Agenda modification** — finer-grained or better-directed open questions.
5. **Commitment refinement** — status shifts tracking the underlying evidential situation.

An invocation producing none of these is *vacuous* and should be flagged.

---

## 6. Reasoning as Explicit Stepwise Construction ^stepwise-construction

### Disagreement and Correction

The previous section implied that some operations are carried out outside the system ("system computes, user supplies," "content essentially outside the system"). Instead, the language must represent all reasoning operations at the finest operational grain. Algorithmic computations must be written explicitly so the user can read them step by step. User constructions must be derived step by step to track reasoning and rationale.

### Acknowledging the Correction

The objection is correct. The execution-mode stratification reintroduced, at the operation level, the prose-in-fields failure. An observation whose *constitution as an observation* — the reasoning that warrants treating this data as evidence for that claim — is opaque, is still cosmetically formal. A deductive step performed by an SMT solver and entered as "verified" is a sealed black box.

The corrected requirement: every operation must be decomposable into atomic moves, each fully expressed in the formal language. The trace of a reasoning episode must be a continuous chain in which every transition is locally readable, with no step requiring appeal to extra-systemic content or extra-systemic procedures.

### 6.1 The Principle of Operational Atomicity

Every operation must be expressible as a finite composition of *atomic moves*, where an atomic move is a transition $s \to s'$ that:

1. has a fully formal precondition statement;
2. has a fully formal effect statement;
3. is justified by a formal rule of the calculus;
4. carries no internal opacity.

The atomic moves are the *instructions* of the calculus. Compound operations are *programs* built from these instructions. Compound forms are *recognized macros* — expanded for the trace, not stored as opaque calls.

### 6.2 The Vocabulary of Atomic Moves

#### Structural Moves

**`introduce-symbol(\sigma, \tau, \alpha)`.** Add new symbol $\sigma$ of type $\tau$ to $\Sigma$, governed by axiom set $\alpha$.

**`retire-symbol(\sigma)`.** Remove $\sigma$ from $\Sigma$.

**`assert-axiom(\varphi, \rho)`.** Add formula $\varphi$ to $T$ with commitment status $\rho$.

**`retract-axiom(\varphi)`.** Remove $\varphi$ from $T$.

**`set-commitment(\varphi, \rho)`.** Change commitment status.

#### Inferential Moves

**`apply-rule(R, \langle \varphi_1, \ldots, \varphi_n \rangle, \psi)`.** Apply named inference rule $R$ to premises, producing conclusion.

**`unfold-definition(\sigma, \varphi)`.** Replace occurrences of $\sigma$ by its definiens.

**`fold-definition(\sigma, \varphi)`.** The inverse.

#### Erotetic Moves

**`pose-question(?\Phi)`.** Add $?\Phi$ to agenda $Q$.

**`refine-question(?\Phi, ?\Phi')`.** Replace by strictly finer question.

**`bind-answer(?\Phi, \varphi)`.** Mark $\varphi$ as resolution.

#### Mapping Moves

**`declare-mapping(\mu, \text{src}, \text{tgt}, \text{symbol-map})`.** Introduce structural mapping.

**`record-preservation(\mu, \varphi)`.** Assert that $\mu$ preserves $\varphi$.

**`record-divergence(\mu, \varphi)`.** Assert that $\mu$ fails to preserve $\varphi$.

#### Provenance and Trace Moves

**`record-source(\varphi, \pi)`.** Attach provenance object.

**`set-entrenchment(\varphi, e)`.** Place $\varphi$ at entrenchment level $e$.

### 6.3 How Compound Operations Decompose

#### Deductive Inference as a Sequence of `apply-rule`

```
apply-rule(R_1, premises_1, intermediate_1)
apply-rule(R_2, premises_2, intermediate_2)
...
apply-rule(R_n, premises_n, \psi)
```

When an automated procedure is invoked, it does not enter the trace as "applied SMT solver" — it produces a sequence of `apply-rule` calls. If the procedure cannot produce such a derivation, its result enters as conjectural with explicit verification debt.

#### Observation as a Sequence of Recorded Reasoning Moves

```
introduce-symbol(d, \text{Datum}, \emptyset)
assert-axiom(\text{produced-by}(d, c), asserted)
assert-axiom(\text{calibrated}(i, t), asserted)
apply-rule(R_{\text{instrument-reliability}}, [...], \text{indicates}(d, \varphi))
apply-rule(R_{\text{evidence-uptake}}, [\text{indicates}(d, \varphi), \neg\text{defeater}(\varphi)], \varphi)
assert-axiom(\varphi, asserted)
record-source(\varphi, \pi_{\text{observation}}(d, c, i, t))
```

The *raw datum* is one thing; the *interpretation of the datum as evidence for $\varphi$* is a chain of rule applications.

#### Concept Construction as Stepwise Definition

```
introduce-symbol(P, \tau, \emptyset)
assert-axiom(\forall \bar{x}. P(\bar{x}) \leftrightarrow \varphi(\bar{x}), asserted)
apply-rule(R_{\text{conservativity-check}}, [\text{definitional-form}(P, \varphi)], \text{conservative}(P))
assert-axiom(\text{conservative}(P), asserted)
record-source(P, \pi_{\text{construction}}(\text{motivating question}, \text{rationale}))
```

#### Abduction as Explicit Hypothesis Generation and Vetting

```
pose-question(?\text{explain}(\varphi))
apply-rule(R_{\text{abductive-schema-instantiation}}, [\varphi, T, \mathcal{X}], [\psi_1, \psi_2, \psi_3])
assert-axiom(\psi_1, conjectured)
...
apply-rule(R_{\text{entailment-check}}, [T \cup \{\psi_1\}, \varphi], \text{entails}(...))
apply-rule(R_{\text{novelty-check}}, [T, \varphi], \neg\text{entails}(...))
apply-rule(R_{\text{plausibility-ordering}}, [\psi_1, \psi_2, \psi_3, \text{criteria}], [\psi_2 \succ \psi_1 \succ \psi_3])
```

The abductive move is creative in the *selection of the schema* and in the *generation of candidates*, but every link is locally inspectable.

### 6.4 The Status of Automation

*No computation is opaque.* Automated procedures are permitted, but their output must be the same kind of thing a user would produce — a sequence of atomic moves.

**Provers must produce certificates.** When a procedure establishes $T \vdash \psi$, it must emit a derivation. If it cannot, the result is a conjecture supported by an *external testimony* with explicit verification debt.

**Macros must expand.** No "system performs revision" black box; only explicit kernel-selection followed by explicit retractions and additions, all visible.

**Search must be explicit.** The result of search is not an opaque "best candidate" but a vetted and ordered list with explicit trace.

Procedures like modern SMT solvers, ML-based hypothesis generators, or LLM-style suggestion engines are admissible *only as oracle sources* whose outputs enter as conjectures, never as verified results. The line: *whether the procedure produces inspectable derivations*.

### 6.5 What the User Actually Manipulates

The user does not invoke `compare(T_1, T_2)` and receive a comparison object. The user *constructs* the comparison by executing atomic moves: declaring the mapping, recording preservation claims one axiom at a time, recording divergence claims one axiom at a time.

The user does not invoke `revise(T, \varphi)` and receive a revised theory. The user *executes* the revision: applying the AGM contraction kernel rule (with selection criterion named), retracting kernel members one at a time, asserting $\varphi$.

The user does not observe; the user *records an observation trace* of the kind shown in §6.3, each step a separate, inspectable move.

### 6.6 The Cost and Its Justification

This discipline is expensive. Mitigations:

**Stable macros.** Recurring patterns named as macros; the expansion is automatic; the trace records the expansion with macro identity as metadata.

**Granularity views.** The trace, always recorded at atomic granularity, can be *viewed* at coarser granularities.

**Scoped suspension of atomicity.** For exploratory work, *sketch mode* records compound operations as macros without immediate expansion, with *expansion debt* tracked.

The justification: this is what it means to have a framework in which reasoning is fully formal. The alternative — opaque steps, sealed certificates, prose-in-fields-by-another-name — is the failure mode.

### 6.7 The Revised Architecture

The framework consists of:

1. a *signature* and *theory* together with $Q, H, \Pi, U, \mathcal{X}, M$;
2. a *catalog of atomic moves*;
3. a *catalog of inference rules*;
4. a *macro library* with faithfulness proofs;
5. a *trace*, queryable at multiple granularities;
6. a *view system*;
7. an *authoring environment* with scaffolding;
8. an *oracle interface* for external procedures.

### Synthesis

The corrected design takes the operational discipline of proof assistants and generalizes it from deductive proof to the entire space of research operations. Every reasoning episode — deductive, observational, constructive, strategic — is a finite sequence of atomic moves, each fully expressed, each licensed by a named rule, each contributing inspectably to the state. Automation is permitted but never opaque.

---

## 7. Two Foundational Clarifications: Objects-as-Moves and the Rule Catalog ^objects-as-moves

### Questions

1. Are most atomic moves equivalent to introducing a new object? For instance, `introduce-symbol` creates a concept object, `assert-axiom` creates a claim object, `declare-mapping` creates a mapping object. Can all atomic moves be encoded by creating an object? Otherwise, what makes them irreducible? Or are the two encodings equivalent — two presentation choices analogous to function application vs. declarative syntax in Python?

2. Rules are named, formally specified objects — modus ponens, ∧-introduction, AGM contraction kernel selection. How to choose the catalog?

### Part 1 — Are Atomic Moves Just Object Introductions?

#### The Observation Is Largely Correct

The intuition is right: in a properly designed system, most atomic moves *can* be encoded as the introduction of a typed object. The state delta produced by `introduce-symbol(\sigma, \tau, \alpha)` is the addition of a new symbol-record to $\Sigma$; the state delta of `assert-axiom(\varphi, \rho)` is the addition of an axiom-record to $T$; the state delta of `declare-mapping(\mu, \ldots)` is the addition of a mapping-record to $M$.

This reflects a deep principle: *the state is the totality of recorded objects, and changes to the state are changes to that totality*. The atomic moves *are* the elementary state changes; the typed objects *are* the elementary state contents; the two are dual presentations of the same underlying fact.

The distinction is analogous to function-application / declarative-syntax in Python or to the Curry-Howard correspondence: a proof step *is* the construction of a proof term; a derivation *is* a tree of such terms.

#### Where the Equivalence Holds Cleanly

For moves whose effect is purely *additive*:

- `introduce-symbol` ↔ creation of a `Symbol` object with fields type, governing-axioms, provenance.
- `assert-axiom` ↔ creation of an `Axiom` object with fields formula, commitment-status, provenance.
- `pose-question` ↔ creation of a `Question` object with fields answer-set, presupposition, provenance.
- `declare-mapping` ↔ creation of a `Mapping` object.
- `record-preservation` ↔ creation of a `PreservationClaim` object.
- `record-source` ↔ creation of a `Provenance` object.

#### Where the Equivalence Requires Care

**Moves with non-additive effects.** `retract-axiom`, `retire-symbol`, `set-commitment`, `set-entrenchment` remove or modify state. The framework's commitment to *trace persistence* forces an *event-sourcing* discipline: nothing is ever truly removed; a `Retraction` object is introduced that points to the retracted axiom and marks it as no longer active. The state at any time is the *interpretation* of accumulated event-objects. Under this discipline, *every* atomic move is the creation of an object.

**Moves whose content is the application of a rule.** The legitimacy of a `RuleApplication` object requires that the rule's preconditions actually hold of the cited premises. Object construction is gated by type-checking with substantive content — the same discipline as *dependent typing*. An object of type `RuleApplication(R, [\varphi_1, \ldots, \varphi_n])` is well-typed only if there exists a unification proving that $R$ applies to those premises.

**Moves that express relationships between other objects.** `record-preservation`, `record-divergence`, `bind-answer` link existing objects. The linkage is content: that mapping $\mu$ preserves axiom $\varphi$ is a claim distinct from the existence of $\mu$ and the existence of $\varphi$. The linkage object is a typed relationship-record — every relation worth tracking should be reified.

#### The Reformulated Position

> *Every atomic move is the introduction of a typed object into the state record. The object's type encodes the move's preconditions and effects; the object's fields encode the move's parameters and results; the object's provenance encodes the rationale. The trace is the accumulating list of such objects, ordered by their creation, and the current state is the interpretation of the accumulated trace.*

Moves and objects are two presentations of the same content. Function-application style emphasizes the dynamics; declarative style emphasizes the result. Both are needed: function-application for authoring, declarative for inspection and queries.

#### The Two Encodings Are Equivalent — With One Substantive Constraint

The two encodings are equivalent provided that *object types are rich enough to capture the substantive content of the moves they reify*:

1. Object types must include the move's preconditions as type constraints.
2. Object types must include provenance as a structural field.
3. Object construction must be *transactional*: proposing an object triggers type-checking, consequence-preview, and integration only on acceptance.

Under these constraints, the duality is exact. The choice between encodings is *pragmatic* — about authoring ergonomics, tooling, and exposition — not foundational. The user's intuition that this is "like Python's distinction between function application and declarative syntax" is precisely correct.

#### Practical Consequence for Design

- **Declarative core, imperative surface.** The formal substance is the typed object catalog and the constraints on object construction. The "atomic move" vocabulary is a *surface presentation*.
- **Trace as object database.** The trace is a typed database of objects with relationships, supporting standard database disciplines.
- **Move catalog and object catalog are isomorphic.** The framework specifies one and derives the other automatically.

The earlier presentation, which spoke of atomic moves as a separate primitive vocabulary, was over-stated. The atomic moves *are* the object types of the typed record, viewed dynamically.

### Part 2 — How to Choose the Rule Catalog

#### Why the Question Is Hard

Rule catalogs are determined by the interaction of several factors:

- The *target consequence relation*: which entailments the calculus must license.
- The *granularity discipline*: how fine-grained the derivations must be.
- The *meta-theoretic properties* desired: soundness, completeness, normalization, cut-elimination, decidability.
- The *coverage* of the operation inventory.
- The *extensibility discipline*.

The catalog is a *negotiated equilibrium*, not a discoverable fact.

#### Principles That Constrain the Choice

**R1 — Semantic Anchoring.** Every rule must be *sound* with respect to the framework's semantics. For non-deductive rules, soundness is generalized: each rule specifies its preserved invariant (consistency, maximal coherence, structural homomorphism) and proves that it respects it.

**R2 — Compositional Completeness.** Deductive completeness for the deductive sub-calculus; operational completeness for each compound operation in the inventory.

**R3 — Granularity Discipline.** The operational test: can a reader verify the rule's application by inspecting the premises and conclusion alone? If verification requires further unstated reasoning, the rule conceals content and must be decomposed.

**R4 — Conservativity of Extension.** When a new rule is added, no previously valid derivation becomes invalid, and no previously invalid derivation becomes valid in the un-extended portion. Enforced by *signature scoping*.

**R5 — Symmetry Between Introduction and Elimination.** For each compound logical structure, both introduction and elimination rules — Gentzen-style balance ensuring cut-elimination.

**R6 — Coverage of Modal and Epistemic Dimensions.** Rules governing commitment propagation, provenance composition, dependency propagation, entrenchment update. These are framework-specific and must be designed alongside the framework.

#### A Practical Methodology

**Step 1 — Fix the target semantics.** Choose $\mathcal{M}$, $\vDash$, the update semantics.

**Step 2 — Identify the deductive core.** Propositional, first-order, modal, dependently typed? Governed by the operation inventory.

**Step 3 — Adopt a standard rule system for the deductive core.** Import decades of well-validated rule sets.

**Step 4 — Design the framework-specific modal-epistemic rules.** Original work. Validate against pragmatic semantics.

**Step 5 — Design rules for non-deductive operations.** Abductive, revisionary, erotetic, comparative, generalization, transfer rules — each validated against its preserved invariant.

**Step 6 — Test against the corpus.** Reconstruct paradigmatic episodes; each unreconstructible move signals a missing rule.

**Step 7 — Audit for redundancy.** When two rules license the same derivations, one is redundant.

**Step 8 — Document admissibility conditions for future rules.** Specify conditions under which users may propose new rules.

#### Primitive and Derived Rules

Not every rule in the catalog need be primitive. Many useful rules are *derived* — theorems of the calculus packaged for convenient use. Double-negation elimination, for example, is derivable and included as a *derived rule*.

The discipline: every rule is either primitive (axiomatic) or derived (proved from primitives). Derived rules expand to primitive derivations in user traces, preserving operational atomicity even though authoring used the derived rule directly.

This keeps the primitive catalog *small* and *well-understood* while providing a large *effective catalog* of derived rules.

#### Synthesis on Catalog Choice

The catalog is determined by:

- the semantics chosen;
- the operation inventory the framework must support;
- the granularity required by operational atomicity;
- the meta-theoretic properties the framework must satisfy;
- the corpus of research episodes the framework must reconstruct.

Two well-designed catalogs for the same framework should differ only in surface presentation — in which rules are chosen as primitive versus derived — but should be equivalent in the derivations they license.

The risk: treating the catalog as a *menu* from which the designer picks. The catalog is *forced* by the framework's other commitments. The designer's freedom is in choosing those commitments.

### Concluding Remark Connecting the Two Clarifications

The two clarifications converge on a single deeper point: the framework's content lives entirely in its *typed object catalog* and its *rule catalog*, with the two related by a tight constraint — every rule licenses the construction of objects of certain types, and every object of certain types is constructible only by application of certain rules.

The object catalog tells us *what can exist*; the rule catalog tells us *how things come into existence and propagate*. The atomic moves are the dynamic view of object construction; the typed objects are the static view of the trace. The catalogs together constitute the framework's formal apparatus, and their joint design is the primary task of foundation-laying.

The user's intuition that atomic moves "are just object introductions" is therefore not a simplification but a recognition of the framework's deep structure. The intuition is correct, with the caveat that object types must encode the substantive content of the moves they reify, including dependent-type constraints capturing rule-application correctness and event-sourcing discipline capturing non-additive effects. Under these conditions, the framework has *one* primary catalog — typed objects — with rules as the constraints on how objects of certain types may come into being.
