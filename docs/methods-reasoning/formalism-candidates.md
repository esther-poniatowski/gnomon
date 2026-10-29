---
tags:
  - ideas
index: "[Methods for reasoning](docs/methods-reasoning/_index.md)"
aliases:
  - Formalism candidates
---
# Formalism candidates

These candidates are formalisms and mechanisms, drawn from programming languages, logic and the study of argument, that may serve an open goal of the [project goals](../../TODO.md). Each entry states the idea, the literature that it draws on, and the goal on which it bears, with a second goal when a part of the idea bears elsewhere. The entries are grouped by goal, and an entry stays here until the work on its goal adopts or declines it. The statements cited as examples belong to the [adversarial statements](adversarial-statements.md).

The candidates that bore only on the retired design documentation, and the triage log that recorded the provenance of every candidate, remain in the git history, in the note of fleeting ideas at commit 9e138e2. The same note holds the progressive formalization of relations, which let a relation pass from a free linking phrase to a controlled type. The [decision on closed typed relations](../adr/closed-typed-relations.md#^closed-relations) settles that candidate: a relation takes its type from the closed vocabulary at every commitment and maturity, since an untyped link cannot be checked, and a prose reading carries the informal sense of a relation.

---

## Goal `research-actions`

The goal `research-actions` decides whether the activities of the registry of activities are primitive, or derive from a smaller set of constructors.

### Multiple dispatch

An operation need not belong to one of its arguments. A generic function holds several methods, and the method that applies is selected on the types of all its arguments together. Several operations on research content have no single owner:

| Operation | Arguments that select the method | Reason that no argument owns the operation |
| --- | --- | --- |
| `supports(argument, claim)` | the kind of argument, the kind of claim | support depends on both kinds |
| `contradicts(statement, statement)` | two kinds of statement | contradiction is a relation, often symmetric |
| `instantiates(example, concept)` | the structure of the example, the kind of concept | instantiation depends on both |
| `formalizes(textual_claim, formal_object)` | the informal and the formal representation | formalization depends on both representations |
| `translates(object, target_language)` | the source object, the target formalism | translation depends on both |
| `equivalent(x, y, criterion)` | two objects and a criterion | equivalence holds relative to a criterion |
| `applies(theorem, model, assumptions)` | a theorem, a model, a set of assumptions | applicability depends on all three |
| `proves(proof, proposition, formal_system)` | a proof, a proposition, a formal system | provability holds relative to a system |
| `task_relevant(representation, task, equivalence)` | a representation, a task, an equivalence | relevance holds relative to a task and a criterion |

The activities of the registry already declare the product types of their inputs. An activity could therefore be one generic operation, with one method for each tuple of input types, instead of one entry per combination.

**Literature.** The Common Lisp Object System (CLOS) and Julia.

**Bears on.** [`research-actions`](../../TODO.md).

### Moves that improve an idea

A vocabulary of moves transforms research content:

- *clarify* reduces an ambiguity;
- *distinguish* splits two conflated notions;
- *generalize* and *specialize* change the scope of a claim;
- *operationalize* and *formalize* give a notion a procedure or a formal object;
- *weaken* removes an excessive commitment, and *strengthen* adds conditions or support;
- *integrate* combines ideas, and *rise above* states a formulation of higher level that synthesizes partial ideas;
- *problematize* exposes a hidden assumption or a limitation;
- *metadiscourse* reasons about the state of the inquiry itself.

These moves are finer than the activities of the registry, so they are candidate constructors from which the activities could derive. Revisionary relations, such as *refines*, *weakens* and *splits into*, name the same changes as relations between two states of the content. The moves and the relations must therefore be reconciled into one vocabulary, not adopted as two.

**Literature.** Knowledge Building theory.

**Bears on.** [`research-actions`](../../TODO.md), and `relation-registry` for the revisionary relations.

---

## Goal `relation-registry`

The goal `relation-registry` declares, in one registry, the relations between research units and between exposition units and research units, each with a warrant kind, and decides which relations transmit a revision. The [decision on answers, models and bindings](../adr/answers-models-bindings.md) already fixes the relations between answers: `supports`, `presupposes`, `tests`, `defeats`, and `revises` for the lineage of an answer.

### Typed-relation discipline

Description Logics provide three disciplines for relations, each of which a check can apply when a record is written:

- **Domain and range.** Each relation declares the kind of its source and the kind of its target: `proves` relates a proof to a mathematical statement, `defines` a definition to a concept, `supports` an argument to a claim, and `cites` any record to a source.
- **Structural properties.** Each relation declares whether it is transitive or symmetric, and names its inverse: `dependsOn` is transitive, `proves` has the inverse `isProvedBy`, and `attacks` is directed, not symmetric.
- **Reification.** A relation that needs a provenance, a strength or a status becomes a record of its own, such as a support relation that holds its supporter, its supported claim, its strength, its context and its source.

Declaring that a relation is transitive differs from computing its transitive closure. The declaration is a property of the relation, whereas the closure would add relations that no author wrote.

**Literature.** Description Logics, restricted to their static modelling discipline.

**Bears on.** [`relation-registry`](../../TODO.md).

### Source-qualified assertions

In RDF, each assertion belongs to a named graph, which identifies the source and the context of the assertion. The same edge, a subject, a predicate and an object, can then hold in the graph of one source and fail in the graph of another, and each relation carries a source, a context and a confidence. The decision on answers already places the acceptance of an answer in a belief base on a named corpus with a named owner. The candidate extends that qualification to each relation, so that a relation asserted in one corpus is not read as asserted in every corpus.

**Literature.** RDF named graphs.

**Bears on.** [`relation-registry`](../../TODO.md).

### Citation intent

CiTO types a citation by its intent: whether the citing work extends, disputes, uses a method from, or corroborates the cited work. A relation `cites` without an intent records only that the link exists. The goal requires the registry to stay independent of the citation vocabularies of the consumers of `gnomon`, so an intent taken from CiTO is declared in the registry of `gnomon` rather than imported from a consumer.

**Literature.** The Citation Typing Ontology (CiTO).

**Bears on.** [`relation-registry`](../../TODO.md).

### The reified relation

Two candidates of this goal describe one object by different routes: the reification of the [typed-relation discipline](#typed-relation-discipline) and the [source-qualified assertion](#source-qualified-assertions). That object is a relation record that holds its source, its target, its relation type, its context, its provenance and its status, so the two candidates are resolved together. Two fields of that record answer statements of the test set:

- **A bounded scope.** A relation holds only within a stated boundary, and fails outside it under a stated condition. An analogy holds only while both of its terms share intrinsic directions of transformation ([example 12](adversarial-statements.md#^example-argument-whose-premise-is-an-analogy-with-restricted-scope)). A model isolates a structure that a phenomenon instantiates under some conditions only, pending a mapping still to be found ([example 35](adversarial-statements.md#^example-ambiguous-relation-between-model-and-phenomenon)).
- **A status local to the relation.** A hedge can bear on one inferential link inside a statement, rather than on the whole statement: "plausible, though not yet demonstrated" bears on one link from an observation to a mechanism ([example 23](adversarial-statements.md#^example-mixed-epistemic-status-within-a-single-statement)). A statement is then asserted in part and hedged in part.

**Literature.** The literature of the two candidates that it unites.

**Bears on.** [`relation-registry`](../../TODO.md).

### Argumentation relations

Abstract and structured argumentation represent arguments together with relations of attack, support and defeat, and compute the acceptance of each argument under a semantics. Only the relations are a candidate here, since the decision on answers already excludes a network of untyped claims linked by support and attack. That decision fixes `supports` and `defeats` between answers. The statements of the test set require one further relation, between two explanations offered for one observation, neither of which attacks, supports or defeats the other:

- a separation of manifolds that is the mechanism or a trace of a routing process of lower level ([example 9](adversarial-statements.md#^example-statement-that-introduces-an-explanatory-gap-rather-than-a-claim));
- a gating mechanism or a change of the decoding basis ([example 23](adversarial-statements.md#^example-mixed-epistemic-status-within-a-single-statement));
- context as a separable axis or as a deformation of the whole space ([example 28](adversarial-statements.md#^example-statement-using-absence-as-evidence));
- decodability read as evidence of representation or of redundant statistical alignment ([example 3](adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example)).

The registry must decide whether two candidate answers to one question already state this competition, or whether a relation of competition is declared. The senses of attack, such as `rebuts`, belong to the same goal.

**Literature.** Dung-style abstract argumentation and structured argumentation, as stated in [argumentation theory](argumentation-theory.md).

**Bears on.** [`relation-registry`](../../TODO.md).

---

## Goal `derivation-framework`

The goal `derivation-framework` formalizes derivation, its results, and synthesis.

### Algebraic data types for propositional content

Propositional content is represented by a recursive algebraic data type, with the constructors `Atom`, `Not`, `And`, `Or` and `Implies`, rather than by a string or by prose. The grammar `φ ::= p | ¬φ | φ∧φ | φ∨φ | φ→φ` admits structural pattern matching, and a string does not. The [decision on expression syntax](../adr/expression-syntax.md) already gives each formula a term structure: an S-expression core, whose operators are head symbols. The open part is whether the claim of an answer admits logical connectives as operators of that core. The goal `audit-local-repairs` currently counts `and` written as an operator as a defect of the worked inquiries.

A grammar for propositional content must also state four constructs that the primitives of a programming language lack: quantification over an open domain, a condition or a regime under which a claim holds, approximate or conditional equality, and the distinction between using a claim and mentioning it.

**Literature.** None cited beyond the construct of algebraic data types.

**Bears on.** [`derivation-framework`](../../TODO.md).

### Statement modality

A statement need not assert its content. Two modalities appear in the test set:

- **A hypothetical statement.** A whole statement is conditional: "if such evidence held, it would mean Z" ([example 3](adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example), [example 4](adversarial-statements.md#^example-research-question-embedded-in-a-critique)).
- **A counterfactual claim.** A claim concerns what a computation would have been under an intervention that did not take place. "The feature contributes to the task" unpacks as a claim about the computation without the feature ([example 37](adversarial-statements.md#^example-statement-with-implicit-dependency-on-counterfactuals)). Such a claim has a meaning only relative to a family of admissible interventions.

The [attitude of a claim](../epistemology/definitions/claim-and-hypothesis.md#^attitude-support), `entertained`, `hypothesized`, `accepted` or `retracted`, already marks a claim that is not asserted. The candidate concerns the content instead: a conditional claim can be accepted as a whole while its antecedent is not asserted, and a counterfactual claim must name its family of interventions.

**Literature.** None cited; the candidate derives from the statements of the test set.

**Bears on.** [`derivation-framework`](../../TODO.md).

### Proof objects

A proof is a structured record, not a prose field attached to a proposition. It holds steps, assumptions, and dependencies on mathematical objects, and one proposition may hold several proofs and several countermodels. A proof assistant separates elaboration, which turns a semi-formal statement into a formal object, from checking, which a small trusted kernel performs. The other concepts borrowed are the context (the active assumptions, definitions and notation), the term, the tactic (an operation from a goal to subgoals), the goal state, and the dependency graph.

The [decision on expression syntax](../adr/expression-syntax.md) declines the term language of a proof assistant, because `gnomon` specifies an inquiry without proving its claims. The structure of a proof, its steps, assumptions, goal states and dependencies, therefore remains a candidate, whereas mechanical checking belongs to a later formalization.

**Literature.** Proof assistants, with the background stated in [proof theory](proof-theory.md) and [dependent type theory](dependent-type-theory.md).

**Bears on.** [`derivation-framework`](../../TODO.md).

### Term rewriting with traces

A rewrite rule `l → r` replaces an expression that matches the pattern `l` by the expression `r`, and leaves a trace that records the source, the target, the rule and its justification. The rules cover normalizing a formula, expanding a definition, applying a theorem, translating a notation, refining a concept, compressing an argument and transforming a proof. A rewrite records a transformation that an author applied; no program applies the rules to derive content.

A rewrite can preserve meaning and still change what reads as explanatory. Rewriting the function of a network as a sum over paths makes some distributed effects look local, because locality moves from the units to the paths ([example 24](adversarial-statements.md#^example-derivation-with-a-hidden-change-of-representation-language)). The trace must therefore also record this explanatory shift: what the new representation makes local, simple or salient, which the former one did not.

**Literature.** Term rewriting systems.

**Bears on.** [`derivation-framework`](../../TODO.md). The candidate first bore on the primitiveness of operations, now held by `research-actions`, as a kind of operation that transforms content.

---

## Goal `research-corrections`

The goal `research-corrections` applies the research corrections of the Mixture pilot, among them a rationale on each itinerary step.

### Grammars for the rationale of a step

The fields that state why a step of reasoning was taken are read by checks, so each of them requires a grammar rather than free prose. The candidate grammars are:

- **strategic rationale:** a record `{move_type, target_deficiency_ref, expected_gain_kind}`, or a grammar over the signatures of the operations;
- **explanatory gain:** a reference to the property of the state that the step made present, such as a newly licensed claim, a discharged assumption or a closed subgoal;
- **route selected and alternatives rejected:** references to candidate operations, each in a record `{candidate_ref, rejection_reason_kind}` whose kind is drawn from a closed list;
- **deficiency addressed:** a reference to a question or a gap.

The goal already requires the rationale of each step to name the question served and what the step acts on, which covers the deficiency addressed. The candidate adds the gain obtained and the alternatives rejected.

**Literature.** None cited.

**Bears on.** [`research-corrections`](../../TODO.md), and `inquiry-records-round-2`, which requires field paths that a program can read instead of prose.

---

## Goal `definitions-framework`

The goal `definitions-framework` formalizes definitions, and produces the full definition object to which a concept record may link.

### Legitimate mutual constraint

Two structures look circular without being vicious cycles of justification:

- **Co-definition.** Two definitions can depend on each other. "Task variable" cannot be fixed independently of "task", because what counts as a variable depends on which distinctions the task makes relevant ([example 29](adversarial-statements.md#^example-conceptual-dependence-between-two-definitions)). Such definitions are admitted together, as a cluster that records its mutual constraint as legitimate.
- **Co-determination.** Two objects can each explain an aspect of the other. The task explains the geometry, and the geometry explains which aspects of the task are treated as relevant ([example 32](adversarial-statements.md#^example-ambiguous-explanatory-priority)). A directed relation `explains` cannot state this. A distinction, here between the task and the effective task, often removes the apparent circle, because it separates the endpoints of the two relations.

The note on the [order of specification](../epistemology/specification-order.md#^iteration-circularity) already separates circularity in the order of execution from circularity in warrant, and admits cycles between questions resolved by iteration. The candidate draws the same distinction for definitions and for explanatory relations.

**Literature.** None cited; the candidate derives from the statements of the test set.

**Bears on.** [`definitions-framework`](../../TODO.md) for co-definition, and `relation-registry` for co-determination.

### Identity criterion of a concept

A concept carries an identity criterion, which decides whether two records denote the same concept, instead of serving as a label without conditions. The concept record of the [decision on concepts, glossaries and notations](../adr/concepts-glossaries-notations.md) holds a gloss, a kind, a broader concept, a source note and its confusions with other concepts, but no identity criterion. The criterion is therefore a candidate part of the full definition object to which the record may link. The same proposal held an equivalence criterion, which the decision on answers already places in the block of an exploration.

**Literature.** None cited.

**Bears on.** [`definitions-framework`](../../TODO.md).

---

## Goal `vocabulary-records`

The goal `vocabulary-records` provides the mechanisms of notations, glossaries, audiences and project specifications, and defines the concept record.

### Concept as class and concept as object

A concept is both a category, a class of things, and an object of inquiry, which carries a definition, a history, sources, variants and critiques. "Representation" is at once a class and an object about that class. The discipline keeps both readings explicit: a concept object that `denotesClass` a category. The concept record already holds both: its broader concept states an inclusion between the classes that two concepts denote, whereas its source note and its confusions describe the concept as an object of inquiry. The candidate requires the schema of the record to mark which fields bear on the class and which on the object, so that no check reads one as the other.

**Literature.** Metamodeling in Description Logics.

**Bears on.** [`vocabulary-records`](../../TODO.md), for the schema of the concept record, and `definitions-framework`.

---

## Goal `status-propagation`

The goal `status-propagation` decides which changes of the attitude or of the support of a claim mark the records resting on it for review.

### Revision operations

Belief revision names five operations on an epistemic state: expansion adds a claim without resolving a conflict, revision adds a claim while preserving consistency, contraction removes a commitment, consolidation restores consistency after a contradiction, and merge combines two epistemic states. The [note on revision](../epistemology/definitions/activities/revision.md) already adopts expansion, contraction and revision, under the AGM postulates, as the activity `belief-revision`. The candidate adds consolidation and merge, and offers the five operations as the classes of change that the goal sorts: the goal can state, for each operation, whether it marks the records resting on the changed claim for review.

**Literature.** The AGM theory of belief revision, as stated in [belief revision and dynamic epistemic logic](belief-revision-dynamic-epistemic-logic.md).

**Bears on.** [`status-propagation`](../../TODO.md).

---

## Goal `inquiry-records-round-2`

The goal `inquiry-records-round-2` makes the inquiry records checkable, and closes the gaps of the type graph of activities, among them the recording of a negative detection.

### Four statuses of a detection

A claim of detection takes one of four values, which a record must not conflate:

- **no stored result:** nothing is asserted about whether a result exists;
- **known absence:** a search context, explicitly closed, records that no result exists;
- **disproved:** a counterexample or a contradiction is established;
- **undecided:** the question is open and tracked.

The case that motivated the distinction is the status of a proof, but it holds for any detection. A representation without a clean axis of context does not establish that context is absent: it may show only that no marker shaped like an axis was found, while context deforms the whole space ([example 28](adversarial-statements.md#^example-statement-using-absence-as-evidence)). Reading "no stored result" as "known absence" is the false negative that the distinction blocks. The [choice of the next act](../epistemology/next-act.md) states that no activity records a negative detection, and the four values state what such a record distinguishes.

**Literature.** None cited; the candidate arose from the contrast between open-world and closed-world reading in Description Logics.

**Bears on.** [`inquiry-records-round-2`](../../TODO.md).

---

## Goal `problem-record`

The goal `problem-record` extends the problem record, and decides whether explication becomes an aim judged by criteria of adequacy instead of truth.

### Meta-conceptual statements

A statement can concern the criteria for applying a concept rather than the referent of the concept. "The distinction between information being present and information being used changes what should count as representation" is such a statement ([example 2](adversarial-statements.md#^example-conceptual-distinction-that-also-revises-the-target-concept)). It has no truth value in the research domain, so a check of domain claims does not apply to it, and it is judged by its adequacy, as an explication is. The statement is therefore a test case for the decision of the goal on explication. The same proposal treated a conceptual metaphor, such as "container model" or "shadow", as an object that an argument diagnoses, without naming a mechanism; the statements that carry these metaphors remain in the test set ([example 4](adversarial-statements.md#^example-research-question-embedded-in-a-critique), [example 5](adversarial-statements.md#^example-definition-by-refusal-of-inadequate-operationalizations), [example 7](adversarial-statements.md#^example-derivation-whose-conclusion-is-a-changed-viewpoint)).

**Literature.** None cited.

**Bears on.** [`problem-record`](../../TODO.md), and `inquiry-records-round-2`, which gives a question of explication a record form.
