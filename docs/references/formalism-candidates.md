---
tags:
  - ideas
index: "[References](docs/references/_index.md)"
aliases:
  - Formalism candidates
---
# Formalism candidates

These candidates are formalisms and mechanisms, drawn from programming languages, logic and the study of argument, that may serve an open goal of the [project goals](../../TODO.md). Each entry states the idea, the literature that it draws on, and the goal on which it bears, with a second goal when a part of the idea bears elsewhere. The entries are grouped by goal, and an entry stays here until the work on its goal adopts or declines it. The statements cited as examples belong to the [adversarial statements](../../examples/adversarial-statements.md).

The candidates that bore only on the retired design documentation, and the triage log that recorded the provenance of every candidate, remain in the git history, in the note of fleeting ideas at commit 9e138e2. An entry recovered from the other retired design notes names its file at the same commit, under **Retired source**. The same note holds the progressive formalization of relations, which let a relation pass from a free linking phrase to a controlled type. The [decision on closed typed relations](../adr/closed-typed-relations.md#^closed-relations) settles that candidate: a relation takes its type from the closed vocabulary at every commitment and maturity, since an untyped link cannot be checked, and a prose reading carries the informal sense of a relation.

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

### Constructors of operations

An activity could derive from four constructors applied to schemas of operations, instead of standing as a primitive entry of the registry:

- `compose(s1, s2, …)` applies schemas in order, and passes the output of each schema to the next;
- `parallel(s1, …, sn)` applies schemas to disjoint parts of a target, and gathers their outputs;
- `branch(condition, s_true, s_false)` selects a schema by a predicate over its inputs;
- `iterate(s, until)` applies a schema until a predicate of termination holds.

Each constructor, and each schema treated as primitive, declares five parts: a typed signature, its conditions of admissibility, the semantics of its transformation, its condition of success, and the kind of licence that justifies it. A schema that lacks one part does not enter the library. The registry of activities already declares a signature, a mode and a norm for each activity, so the candidate adds the semantics of the transformation and the condition of success. In an itinerary, `branch` and `iterate` would give a step a branch and a fallback, which a sequence of steps cannot state.

**Literature.** The precedents that the retired notes name: the inference rules of [proof theory](proof-theory.md), the primitive instructions of a programming language, the typed tasks of a workflow system, and the morphisms of category-theoretic semantics.

**Bears on.** [`research-actions`](../../TODO.md), and `inquiry-records-round-2` for the branches and fallbacks of an itinerary.

**Retired source.** `docs/design/3-aspect-specific/operation-schemas.md`, `docs/design/_backup/architecture-2-audit.md` and `docs/design/_backup/arguments-reasoning/primitive-operations.md`, at commit 9e138e2.

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

- **A bounded scope.** A relation holds only within a stated boundary, and fails outside it under a stated condition. An analogy holds only while both of its terms share intrinsic directions of transformation ([example 12](../../examples/adversarial-statements.md#^example-argument-whose-premise-is-an-analogy-with-restricted-scope)). A model isolates a structure that a phenomenon instantiates under some conditions only, pending a mapping still to be found ([example 35](../../examples/adversarial-statements.md#^example-ambiguous-relation-between-model-and-phenomenon)).
- **A status local to the relation.** A hedge can bear on one inferential link inside a statement, rather than on the whole statement: "plausible, though not yet demonstrated" bears on one link from an observation to a mechanism ([example 23](../../examples/adversarial-statements.md#^example-mixed-epistemic-status-within-a-single-statement)). A statement is then asserted in part and hedged in part.

**Literature.** The literature of the two candidates that it unites.

**Bears on.** [`relation-registry`](../../TODO.md).

### Argumentation relations

Abstract and structured argumentation represent arguments together with relations of attack, support and defeat, and compute the acceptance of each argument under a semantics. Only the relations are a candidate here, since the decision on answers already excludes a network of untyped claims linked by support and attack. That decision fixes `supports` and `defeats` between answers. The statements of the test set require one further relation, between two explanations offered for one observation, neither of which attacks, supports or defeats the other:

- a separation of manifolds that is the mechanism or a trace of a routing process of lower level ([example 9](../../examples/adversarial-statements.md#^example-statement-that-introduces-an-explanatory-gap-rather-than-a-claim));
- a gating mechanism or a change of the decoding basis ([example 23](../../examples/adversarial-statements.md#^example-mixed-epistemic-status-within-a-single-statement));
- context as a separable axis or as a deformation of the whole space ([example 28](../../examples/adversarial-statements.md#^example-statement-using-absence-as-evidence));
- decodability read as evidence of representation or of redundant statistical alignment ([example 3](../../examples/adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example)).

The registry must decide whether two candidate answers to one question already state this competition, or whether a relation of competition is declared. The senses of attack, such as `rebuts`, belong to the same goal.

**Literature.** Dung-style abstract argumentation and structured argumentation, as stated in [argumentation theory](argumentation-theory.md).

**Bears on.** [`relation-registry`](../../TODO.md).

### Semantic and justificatory dependence

Two kinds of dependence link records. A record depends semantically on another when its statement cannot be interpreted without the other, as a theorem depends on the definitions of its terms. A record depends justificatorily on another when the other supports its claim, as a proof depends on its lemmas and its assumptions. The candidate vocabulary splits the relations into two strata:

- the relations declared between records: `defines`, from a definition to a concept; `uses`, or `requires_for_interpretation` for a semantic dependence; `assumes`; `proves`, from a proof to a claim; `specializes` and `generalizes`; `exemplifies`; `contradicts` and `refutes`; and `addresses`, to a question;
- the relations relative to an inquiry, which belong to an assembly and not to a record: `selected_for`, `load_bearing_for`, `bridge_for`, `deferred_in` and `ordered_before_in`.

The split keeps a weak relation on the record and a strong one on the assembly. A record states once that it `addresses` a question, whereas its use as a part of the minimal answer of one inquiry is stated by the assembly of that inquiry.

**Literature.** None cited.

**Bears on.** [`relation-registry`](../../TODO.md), and `assembly-schema` for the relations relative to an inquiry.

**Retired source.** `docs/design/_backup/object-types-ontology/relations-graph-edges.md` and `docs/design/3-aspect-specific/semantic-relations.md`, at commit 9e138e2.

### Warrant kinds

Each support relation carries a warrant kind from a closed list: `deductive`, `empirical`, `abductive`, `analogical`, `heuristic`, `methodological`, `definitional` and `interpretive`. Each kind is declared monotonic or defeasible, so the defeasibility of a record is computed from the kinds of the relations that support it, and reported: a record is defeasible when one of its supports is defeasible. Such a computation applies a declared rule to authored relations, which the [decision against inference at run time](../adr/no-run-time-inference.md#^admitted-computation) admits. The retired notes classed `deductive` as monotonic, and `empirical`, `abductive`, `analogical` and `heuristic` as defeasible, and left the three other kinds unclassified.

The list must be aligned with two vocabularies that already exist in the [vocabulary registry](../../src/gnomon/data/vocabularies.yml): the `mode` of an activity, declared under `itinerary`, and the `laws.warrant` of a model and of a background (`derived`, `derived-in-a-limit`, `posited`, `fitted`, `measured`).

**Literature.** None cited.

**Bears on.** [`relation-registry`](../../TODO.md), and `status-propagation`, whose rule of sensitivity reads the warrant kind.

**Retired source.** `docs/design/3-aspect-specific/warrant-vocabulary.md`, at commit 9e138e2.

### Locus of an attack

An attack bears on one of three loci. A rebuttal attacks the claim of an answer. An undercutter grants the grounds and denies that the warrant licenses the step from the grounds to the claim. A third attack rejects the presupposition that the framing of a question carries. The [dotted identifiers](../adr/dotted-identifiers.md) already address a unit nested inside a record, so the locus needs no label of its own: a rebuttal names the answer, and an undercutter names a ground of role `warrant`, or one entry of the dependence of the answer. Two undercutters recur. In method-result circularity, the method partly constructs the object that it then measures. In a critique that re-types the target, the failure of a criterion shows that the inquiry asked for the wrong kind of object.

**Literature.** Structured argumentation, ASPIC+, as stated in [argumentation theory](argumentation-theory.md).

**Bears on.** [`relation-registry`](../../TODO.md), to which the [argumentation relations](#argumentation-relations) already assign the senses of attack.

**Retired source.** `docs/design/3-aspect-specific/arguments-reasoning.md`, at commit 9e138e2.

### Relations between frameworks

The product `inter-theory-relation` of the [registry of product types](../../src/gnomon/data/registries/product-types.yml) has no record yet. Four relations between frameworks would state it: `incommensurable-with`, `translates-into`, `subsumes` and `conflicts-with`. Without them, a comparison of frameworks, a change of paradigm or a claim of incommensurability is asserted in prose instead of recorded.

**Literature.** None cited.

**Bears on.** [`relation-registry`](../../TODO.md), and the product `inter-theory-relation`.

**Retired source.** `docs/design/_backup/object-types-ontology/taxo-criteria-ontology.md`, at commit 9e138e2.

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

- **A hypothetical statement.** A whole statement is conditional: "if such evidence held, it would mean Z" ([example 3](../../examples/adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example), [example 4](../../examples/adversarial-statements.md#^example-research-question-embedded-in-a-critique)).
- **A counterfactual claim.** A claim concerns what a computation would have been under an intervention that did not take place. "The feature contributes to the task" unpacks as a claim about the computation without the feature ([example 37](../../examples/adversarial-statements.md#^example-statement-with-implicit-dependency-on-counterfactuals)). Such a claim has a meaning only relative to a family of admissible interventions.

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

A rewrite can preserve meaning and still change what reads as explanatory. Rewriting the function of a network as a sum over paths makes some distributed effects look local, because locality moves from the units to the paths ([example 24](../../examples/adversarial-statements.md#^example-derivation-with-a-hidden-change-of-representation-language)). The trace must therefore also record this explanatory shift: what the new representation makes local, simple or salient, which the former one did not.

**Literature.** Term rewriting systems.

**Bears on.** [`derivation-framework`](../../TODO.md). The candidate first bore on the primitiveness of operations, now held by `research-actions`, as a kind of operation that transforms content.

### Format of a derivation step

A step of a derivation holds three fields, each of which answers its own question:

- the **warrant** states what licenses the step: the rule, the theorem or the definition applied;
- the **operative property** names the structural feature of the objects that makes the warrant apply at that step, such as the finiteness of an index set, which reduces an infinite intersection to a finite one;
- the **strategic function** states what the step achieves toward its subgoal, by exposing, eliminating, reducing or constructing.

A separability test checks the format: when the operative property and the strategic function restate the warrant, the step is not represented. A reader who follows the operative properties and the strategic functions alone can then reconstruct why the subgoal is reachable in the chosen direction.

A step also transforms a proof state, made of the target, the facts available and the obstacle that blocks an immediate conclusion. The step records the state before and after, so its change shows which facts became available and which obstacle disappeared. The obstacles recur: a target too complex, a mismatch of syntactic form, a hidden existential quantifier, a missing witness or bound, a dependence on several cases, an invariant not yet isolated, and facts stated in the wrong vocabulary. The progress of a step takes one of a few forms: a compound goal split into subgoals, a target rewritten to match an available theorem, a component extracted from a conjunction, a witness introduced for an existential goal, an expression normalized, an exhaustive partition into cases, and a global property replaced by a local criterion. The reason for a move differs from its warrant: the warrant states why the step is valid, and the reason states why the step is relevant at that point. The [proof objects](#proof-objects) already hold the goal state, and the [grammars for the rationale of a step](#grammars-for-the-rationale-of-a-step) give the reason a grammar; the candidate adds the operative property, the obstacle and the typed progress.

**Literature.** Steiner's account of mathematical explanation, in which an explanatory proof rests on a characterizing property of the objects involved.

**Bears on.** [`derivation-framework`](../../TODO.md).

**Retired source.** `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-C.md` and `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-G.md`, at commit 9e138e2.

### Closed vocabulary of moves

The moves of a derivation fall in four families:

- **structural** moves reorganize the target or the facts without adding information: `unfold_definition`, `fold_definition`, `decompose_goal`, `decompose_fact`, `rephrase_goal`, `normalize_expression`;
- **transport** moves carry information through a rule or a map: `instantiate_rule`, `specialize_hypothesis`, `transport_along_equivalence`, `monotonic_transfer`, `substitute_equals`;
- **search** moves create a missing object or a structure of cases: `introduce_witness`, `choose_parameter`, `split_cases`, `introduce_auxiliary_claim`, `introduce_invariant`;
- **closure** moves complete a prepared derivation: `apply_criterion`, `derive_contradiction`, `aggregate_subresults`, `discharge_assumption`.

A structural move needs no operative property, so the cost of annotating a step follows its content. A compression rule lets a step omit its obstacle and its reason only when the move is terminally obvious: the target matches a standard rule, no alternative move is plausible, and the progress is immediate and unique. These moves act inside a derivation, whereas the [moves that improve an idea](#moves-that-improve-an-idea) act on research content as a whole.

**Literature.** None cited.

**Bears on.** [`derivation-framework`](../../TODO.md).

**Retired source.** `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-G.md`, at commit 9e138e2.

### Kernel, segments and defects of a derivation

A kernel step is the conceptual core of a derivation: without it, the rest of the derivation is invalid or cannot be built by routine means. An isolation test checks a step flagged as kernel: once the step and every step that depends on it are removed, no path of the dependence graph leads from the premises to the conclusion. The test is a query of reachability over authored dependence, which the [decision against inference at run time](../adr/no-run-time-inference.md#^admitted-computation) admits.

Between the step and the whole derivation, a segment groups the contiguous steps that serve one subgoal, and names its strategy, such as a reduction to the finite-dimensional case by compactness, and the obstacles that it resolves. Three conditions make a derivation adequate:

- **C1**, the warrant of each step is stated at the right generality, neither restating the instance nor trivially permissive;
- **C2**, the reason for a step names a contrastive choice: why this inference rather than one salient alternative;
- **C3**, the subgoals form a well-founded tree rooted at the thesis, and a step that closes no assumption, discharges no obstacle and serves no segment is idle.

Six named defects make a derivation look arbitrary: a **blind step** has a warrant and no local reason; a **hidden obstacle** is a non-trivial rewrite without the obstacle that it removes; a **spurious move** is valid and makes no progress; a **teleological gap** is a move that does not aim at the current target; an **untyped transition** is a move outside the vocabulary of moves; and a **state ambiguity** leaves unclear which facts are active at a step.

An intermediate lemma becomes a unit with an identifier of its own. A consequence derived on the way to another result then has a record, which closes the gap that the [registry of product types](../../src/gnomon/data/registries/product-types.yml) states for the product `consequence`.

**Literature.** Kitcher's account of explanation by unification, for segments that instantiate one pattern across derivations.

**Bears on.** [`derivation-framework`](../../TODO.md), whose report of idle units C3 specifies.

**Retired source.** `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-C.md`, `docs/design/_backup/arguments-reasoning/derivation-proof-encoding-G.md` and `docs/design/_backup/architecture-C.md`, at commit 9e138e2.

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

### Record of a design

A design has no record: the [registry of product types](../../src/gnomon/data/registries/product-types.yml) marks the product `design` as to create. A record of a method would hold seven fields: the task, the inputs, the steps, the rules that state the admissible moves or decisions, the output, the condition of stopping, and the modes of failure. An experimental design adds the intervention, the control and the observation. The record passes the five conditions of the [admission of a record kind](../adr/record-kind-admission.md#^five-conditions): a design is meaningful apart from the inquiry that uses it, several inquiries can cite it, a check can judge it alone, an author can revise it without rewriting its users, and no tool generates it. The same record would hold the procedure that assigns the values of a quantity, which the product `measurement-procedure` lacks.

**Literature.** None cited.

**Bears on.** [`research-corrections`](../../TODO.md), which asks for a record kind for designs, and the products `design` and `measurement-procedure`.

**Retired source.** `docs/design/_backup/object-types-ontology/obj-method-procedure.md`, at commit 9e138e2.

---

## Goal `definitions-framework`

The goal `definitions-framework` formalizes definitions, and produces the full definition object to which a concept record may link.

### Legitimate mutual constraint

Two structures look circular without being vicious cycles of justification:

- **Co-definition.** Two definitions can depend on each other. "Task variable" cannot be fixed independently of "task", because what counts as a variable depends on which distinctions the task makes relevant ([example 29](../../examples/adversarial-statements.md#^example-conceptual-dependence-between-two-definitions)). Such definitions are admitted together, as a cluster that records its mutual constraint as legitimate.
- **Co-determination.** Two objects can each explain an aspect of the other. The task explains the geometry, and the geometry explains which aspects of the task are treated as relevant ([example 32](../../examples/adversarial-statements.md#^example-ambiguous-explanatory-priority)). A directed relation `explains` cannot state this. A distinction, here between the task and the effective task, often removes the apparent circle, because it separates the endpoints of the two relations.

The note on the [order of specification](../epistemology/specification-order.md#^iteration-circularity) already separates circularity in the order of execution from circularity in warrant, and admits cycles between questions resolved by iteration. The candidate draws the same distinction for definitions and for explanatory relations.

**Literature.** None cited; the candidate derives from the statements of the test set.

**Bears on.** [`definitions-framework`](../../TODO.md) for co-definition, and `relation-registry` for co-determination.

### Identity criterion of a concept

A concept carries an identity criterion, which decides whether two records denote the same concept, instead of serving as a label without conditions. The concept record of the [decision on concepts, glossaries and notations](../adr/concepts-glossaries-notations.md) holds a gloss, a kind, a broader concept, a source note and its confusions with other concepts, but no identity criterion. The criterion is therefore a candidate part of the full definition object to which the record may link. The same proposal held an equivalence criterion, which the decision on answers already places in the block of an exploration.

**Literature.** None cited.

**Bears on.** [`definitions-framework`](../../TODO.md).

### Normal form of a definition

A definition holds six fields:

- the **definiendum**, the concept, predicate or term that the definition fixes;
- the **definiens**, the content that fixes its use;
- the **force**: `stipulative`, `descriptive`, `operational`, `canonical` or `revisionary`;
- the **scope**, the domain in which the definition applies;
- the **boundaries**, the borderline uses and the uses ruled out;
- the **variants**, such as an equivalent or a scope-restricted definition.

The genus–differentia form splits the definiens further, into a genus, which the definiendum specializes, and a differentia, which is an attribute of the genus together with the value that the attribute takes. The definitional force of the definiens is recorded apart, as necessary, sufficient, biconditional or informal: prose rarely marks it, and the record must not commit to the strongest reading. A registry of surface templates maps a sentence to the roles of its parts:

| Template | Role |
| --- | --- |
| `X is a Y` | subtype |
| `X is a Y where Z is W` | genus–differentia |
| `X is defined as Y` | equivalence |
| `X refers to Y` | terminological |
| `X consists of A, B, C` | compositional |
| `X is characterized by P` | property-based |
| `X differs from Y by P` | contrastive |
| `X is used to Y` | functional |
| `X measures Y` | operational |
| `X approximates Y` | methodological approximation |
| `X is not P but Q` | negative: rejects a competing definition P |

Three operations on a definition stay separate: normalization makes the roles explicit, completion defines every referenced term, and validation checks that every reference is well formed. A definition is accepted once normalized. The separation fails for a concept whose meaning is fixed by its test, such as the contribution of a feature to a task ([example 37](../../examples/adversarial-statements.md#^example-statement-with-implicit-dependency-on-counterfactuals)).

An undefined term enters as a typed placeholder, not as a bare token. The position of the term in its template fixes its kind: a genus is a system, and an attribute is a property. The placeholder carries a candidate set of referents and a resolution policy:

- `will-resolve`: one candidate will be selected later;
- `cannot-resolve`: the object forces the plurality, which is permanent;
- `will-not-resolve`: the author keeps the plurality by choice, and a check of canonical terms exempts the term.

A placeholder is shared, so resolving it once resolves it in every statement that uses it. A statement may also assert a usage norm, that is, how a named community uses a term, such as "in neuroscience, 'represented' often means recoverable from activity". A usage norm is a claim with a source and a truth value, and differs from the concept that the project fixes for the term.

As a record kind, the definition passes the five conditions of the [admission of a record kind](../adr/record-kind-admission.md#^five-conditions). Its alternative home is the aim block of an answer of explication, which the goal `problem-record` decides together with the question whether explication becomes an aim.

**Literature.** Carnap's explication; implicit definition by a theory, after Hilbert and Carnap; and the holism of Quine and Putnam, which denies that a finite set of definitional claims exhausts a theoretical concept. The retired notes also name frame semantics, typed feature structures and Abstract Meaning Representation as precedents of the normalization.

**Bears on.** [`definitions-framework`](../../TODO.md), and `problem-record` for the alternative home.

**Retired source.** `docs/design/_backup/object-types-ontology/obj-definition.md`, `docs/design/3-aspect-specific/ontology.md` (anchor `^t3-definition-normal-form`) and `docs/design/3-aspect-specific/arguments-reasoning.md`, at commit 9e138e2.

---

## Goal `vocabulary-records`

The goal `vocabulary-records` provides the mechanisms of notations, glossaries, audiences and project specifications, and defines the concept record.

### Concept as class and concept as object

A concept is both a category, a class of things, and an object of inquiry, which carries a definition, a history, sources, variants and critiques. "Representation" is at once a class and an object about that class. The discipline keeps both readings explicit: a concept object that `denotesClass` a category. The concept record already holds both: its broader concept states an inclusion between the classes that two concepts denote, whereas its source note and its confusions describe the concept as an object of inquiry. The candidate requires the schema of the record to mark which fields bear on the class and which on the object, so that no check reads one as the other.

**Literature.** Metamodeling in Description Logics.

**Bears on.** [`vocabulary-records`](../../TODO.md), for the schema of the concept record, and `definitions-framework`.

### Kind, confusions and boundary of a concept

Three parts of the concept record admit a closed form:

- **The kind of a concept** takes one of four values: a system, a subtype or class, a property, which may have an antagonist, and a process. The values are aligned with the definitions of [system, constituent and environment](../epistemology/definitions/system-constituent-environment.md), [kind, class and population](../epistemology/definitions/kind-class-population.md), [property, attribute and predicate](../epistemology/definitions/property-attribute-predicate.md), and [process, event and history](../epistemology/definitions/process-event-history.md).
- **A confusion with another concept** names the other concept, the axis along which the two differ, the feature that blocks their interchange, the source of the risk of conflating them, and the consequence of that conflation.
- **The boundary criterion** separates a concept from a claim: content that fixes a meaning without asserting belongs to the concept, and content that asserts, denies, defines or evaluates belongs to a claim or a definition.

**Literature.** None cited.

**Bears on.** [`vocabulary-records`](../../TODO.md), for the schema of the concept record.

**Retired source.** `docs/design/3-aspect-specific/ontology.md`, `docs/design/_backup/object-types-ontology/obj-distinction.md` and `docs/design/_backup/object-types-ontology/taxo-boundaries.md`, at commit 9e138e2.

---

## Goal `status-propagation`

The goal `status-propagation` decides which changes of the attitude or of the support of a claim mark the records resting on it for review.

### Revision operations

Belief revision names five operations on an epistemic state: expansion adds a claim without resolving a conflict, revision adds a claim while preserving consistency, contraction removes a commitment, consolidation restores consistency after a contradiction, and merge combines two epistemic states. The [note on revision](../epistemology/definitions/activities/revision.md) already adopts expansion, contraction and revision, under the AGM postulates, as the activity `belief-revision`. The candidate adds consolidation and merge, and offers the five operations as the classes of change that the goal sorts: the goal can state, for each operation, whether it marks the records resting on the changed claim for review.

**Literature.** The AGM theory of belief revision, as stated in [belief revision and dynamic epistemic logic](belief-revision-dynamic-epistemic-logic.md).

**Bears on.** [`status-propagation`](../../TODO.md).

### Kinds of a content revision

A revision of content takes one kind or several:

- `retraction`: a record that was once active is no longer pursued;
- `scope_narrowing` and `scope_generalization`: the domain of a record shrinks or extends;
- `reorientation`: the content is reframed without narrowing or generalizing, as when a question is reformulated;
- `taxonomic_restructure`: the classification of a record changes, by renaming, regrouping, splitting or merging;
- `correction`: the content changes within its scope, as when an error of a proof is fixed.

The sensitivity of a dependent follows from the warrant of the relation through which it rests on the revised record. A monotonic warrant is sensitive only to `retraction`, `correction` and `taxonomic_restructure`. A defeasible warrant is sensitive as well to the kinds that bring qualifying evidence: `scope_narrowing`, `scope_generalization` and `reorientation`. Each flagged dependent then records its state: `pending`, `revised`, `confirmed_unaffected` or `retracted`. The recorded state holds the judgment that the [decision on revision accountability](../adr/revision-accountability.md#^flag-not-edit) leaves to the researcher for each dependent.

**Literature.** None cited.

**Bears on.** [`status-propagation`](../../TODO.md), and `relation-registry` for the [warrant kinds](#warrant-kinds).

**Retired source.** `docs/design/3-aspect-specific/revision-vocabulary.md`, at commit 9e138e2.

---

## Goal `inquiry-records-round-2`

The goal `inquiry-records-round-2` makes the inquiry records checkable, and closes the gaps of the type graph of activities, among them the recording of a negative detection.

### Four statuses of a detection

A claim of detection takes one of four values, which a record must not conflate:

- **no stored result:** nothing is asserted about whether a result exists;
- **known absence:** a search context, explicitly closed, records that no result exists;
- **disproved:** a counterexample or a contradiction is established;
- **undecided:** the question is open and tracked.

The case that motivated the distinction is the status of a proof, but it holds for any detection. A representation without a clean axis of context does not establish that context is absent: it may show only that no marker shaped like an axis was found, while context deforms the whole space ([example 28](../../examples/adversarial-statements.md#^example-statement-using-absence-as-evidence)). Reading "no stored result" as "known absence" is the false negative that the distinction blocks. The [choice of the next act](../epistemology/next-act.md) states that no activity records a negative detection, and the four values state what such a record distinguishes.

**Literature.** None cited; the candidate arose from the contrast between open-world and closed-world reading in Description Logics.

**Bears on.** [`inquiry-records-round-2`](../../TODO.md).

### Record of a technique

The act of developing a proof technique or an algorithm that gives access to a quantity yields a product that no record holds. A record of a technique would state the local problem, the need for a new technique, its construction, the properties that the inquiry needs from it, an example of use, and its boundary of applicability.

**Literature.** None cited.

**Bears on.** [`inquiry-records-round-2`](../../TODO.md), whose gaps of the type graph of activities include this act.

**Retired source.** `docs/design/_backup/rendering/note-types.md`, at commit 9e138e2.

---

## Goal `problem-record`

The goal `problem-record` extends the problem record, and decides whether explication becomes an aim judged by criteria of adequacy instead of truth.

### Meta-conceptual statements

A statement can concern the criteria for applying a concept rather than the referent of the concept. "The distinction between information being present and information being used changes what should count as representation" is such a statement ([example 2](../../examples/adversarial-statements.md#^example-conceptual-distinction-that-also-revises-the-target-concept)). It has no truth value in the research domain, so a check of domain claims does not apply to it, and it is judged by its adequacy, as an explication is. The statement is therefore a test case for the decision of the goal on explication. The same proposal treated a conceptual metaphor, such as "container model" or "shadow", as an object that an argument diagnoses, without naming a mechanism; the statements that carry these metaphors remain in the test set ([example 4](../../examples/adversarial-statements.md#^example-research-question-embedded-in-a-critique), [example 5](../../examples/adversarial-statements.md#^example-definition-by-refusal-of-inadequate-operationalizations), [example 7](../../examples/adversarial-statements.md#^example-derivation-whose-conclusion-is-a-changed-viewpoint)).

**Literature.** None cited.

**Bears on.** [`problem-record`](../../TODO.md), and `inquiry-records-round-2`, which gives a question of explication a record form.

---

## Goal `exposition-family`

The goal `exposition-family` specifies the expositions as projections of research records that add no content.

### Examples as relations

An example enters an exposition as a research unit through a relation `exemplifies`, from an existing record to a concept or an answer, whose `use` takes one of five values: `instance`, `witness`, `boundary-case`, `counterexample` and `construction`. A counterexample also names the feature of the case that makes its target fail. The relation, not a record kind, carries the example, since an example is a role that a case plays relative to a target: a record of its own would misrepresent that role as content, against the condition of non-distortion of the retired notes.

**Literature.** None cited.

**Bears on.** [`exposition-family`](../../TODO.md), and `relation-registry` for the relation `exemplifies`.

**Retired source.** `docs/design/_backup/object-types-ontology/obj-example.md` and `docs/design/_backup/object-types-ontology/obj-counterexample.md`, at commit 9e138e2.

---

## Goal `model-design`

The goal `model-design` revises the model design, following the [decision on answers, models and bindings](../adr/answers-models-bindings.md).

### Analogy between models

An analogy maps a source onto a target. The analogy holds the source, the target, the correspondences between their elements, the transfer that the correspondences license, and the limits where the mapping breaks. Under the decision on answers, models and bindings, an analogy has two possible homes: a typed operation by which a derived model comes from its parent, or a binding whose target is a model instead of a phenomenon. Four subtypes differ by function:

- a **structural** analogy preserves the relations between the elements of source and target;
- a **model-transfer** analogy reuses a source model to structure a target domain;
- a **heuristic** analogy guides a search without licensing a claim;
- an **illustrative** analogy clarifies a target without inferential force.

The [reified relation](#the-reified-relation) already gives an analogy a bounded scope.

**Literature.** None cited.

**Bears on.** [`model-design`](../../TODO.md).

**Retired source.** `docs/design/_backup/object-types-ontology/obj-analogy.md`, at commit 9e138e2.

---

## Goal `assembly-schema`

The goal `assembly-schema` specifies the assembly of a level, its components and the checks of its core route.

### Locus of the content that depends on an inquiry

Content that depends on an inquiry belongs to an assembly or to one of its steps, never to a reusable record: the motivation for citing a record, its strategic role, and the gain that it yielded. A record takes part in several inquiries, each with its own gap and its own gain, so a field of the record would let one inquiry stand for all of them. The assemblies that cite a record, with their roles, are found by a query over the graph of relations.

The assembly is no record kind, because its identity is relative to an inquiry and a target. The same records arranged toward another target form another assembly, and a lemma may serve as a premise in one assembly and as a conclusion in another. A record local to an assembly, such as an internal lemma, a named rejected route or the end of a support relation, is promoted to a record of its own once it passes the [admission of a record kind](../adr/record-kind-admission.md#^five-conditions). Strategic notes, work metadata and the records of applied operations stay local. A check flags a candidate for promotion, and the author performs the promotion.

Three fields complete the assembly: its gaps, which are the dependencies not yet resolved; its limits of validity, which are its scope and its exclusions; and its deferred components, left out at the current grain. A weakest-link query reports each core component whose support stays below the demand of the assembly.

**Literature.** None cited.

**Bears on.** [`assembly-schema`](../../TODO.md), and `relation-registry` for the [relations relative to an inquiry](#semantic-and-justificatory-dependence).

**Retired source.** `docs/design/2-architecture/reasoning-structure.md`, `docs/design/_backup/arguments-reasoning/argument-bundles.md` and `docs/design/_backup/schema-fields-base.md`, at commit 9e138e2.
