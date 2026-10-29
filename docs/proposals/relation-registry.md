---
tags:
  - ideas
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the relation registry
---
# Proposals for the relation registry

The goal [`relation-registry`](../../TODO.md) declares, in one registry, the relations between research units and between exposition units and research units, each with a warrant kind, and decides which relations transmit a revision. The [decision on answers, models and bindings](../adr/answers-models-bindings.md) already fixes the relations between answers: `supports`, `presupposes`, `tests`, `defeats`, and `revises` for the lineage of an answer.

## Typed-relation discipline

Description Logics provide three disciplines for relations, each of which a check can apply when a record is written:

- **Domain and range.** Each relation declares the kind of its source and the kind of its target: `proves` relates a proof to a mathematical statement, `defines` a definition to a concept, `supports` an argument to a claim, and `cites` any record to a source.
- **Structural properties.** Each relation declares whether it is transitive or symmetric, and names its inverse: `dependsOn` is transitive, `proves` has the inverse `isProvedBy`, and `attacks` is directed, not symmetric.
- **Reification.** A relation that needs a provenance, a strength or a status becomes a record of its own, such as a support relation that holds its supporter, its supported claim, its strength, its context and its source.

Declaring that a relation is transitive differs from computing its transitive closure. The declaration is a property of the relation, whereas the closure would add relations that no author wrote.

**Literature.** Description Logics, restricted to their static modelling discipline.

**Bears on.** [`relation-registry`](../../TODO.md).

## Source-qualified assertions

In RDF, each assertion belongs to a named graph, which identifies the source and the context of the assertion. The same edge, a subject, a predicate and an object, can then hold in the graph of one source and fail in the graph of another, and each relation carries a source, a context and a confidence. The decision on answers already places the acceptance of an answer in a belief base on a named corpus with a named owner. The candidate extends that qualification to each relation, so that a relation asserted in one corpus is not read as asserted in every corpus.

**Literature.** RDF named graphs.

**Bears on.** [`relation-registry`](../../TODO.md).

## Citation intent

CiTO types a citation by its intent: whether the citing work extends, disputes, uses a method from, or corroborates the cited work. A relation `cites` without an intent records only that the link exists. The goal requires the registry to stay independent of the citation vocabularies of the consumers of `gnomon`, so an intent taken from CiTO is declared in the registry of `gnomon` rather than imported from a consumer.

**Literature.** The Citation Typing Ontology (CiTO).

**Bears on.** [`relation-registry`](../../TODO.md).

## The reified relation

Two candidates of this goal describe one object by different routes: the reification of the [typed-relation discipline](#typed-relation-discipline) and the [source-qualified assertion](#source-qualified-assertions). That object is a relation record that holds its source, its target, its relation type, its context, its provenance and its status, so the two candidates are resolved together. Two fields of that record answer statements of the test set:

- **A bounded scope.** A relation holds only within a stated boundary, and fails outside it under a stated condition. An analogy holds only while both of its terms share intrinsic directions of transformation ([example 12](../../examples/adversarial-statements.md#^example-argument-whose-premise-is-an-analogy-with-restricted-scope)). A model isolates a structure that a phenomenon instantiates under some conditions only, pending a mapping still to be found ([example 35](../../examples/adversarial-statements.md#^example-ambiguous-relation-between-model-and-phenomenon)).
- **A status local to the relation.** A hedge can bear on one inferential link inside a statement, rather than on the whole statement: "plausible, though not yet demonstrated" bears on one link from an observation to a mechanism ([example 23](../../examples/adversarial-statements.md#^example-mixed-epistemic-status-within-a-single-statement)). A statement is then asserted in part and hedged in part.

**Literature.** The literature of the two candidates that it unites.

**Bears on.** [`relation-registry`](../../TODO.md).

## Argumentation relations

Abstract and structured argumentation represent arguments together with relations of attack, support and defeat, and compute the acceptance of each argument under a semantics. Only the relations are a candidate here, since the decision on answers already excludes a network of untyped claims linked by support and attack. That decision fixes `supports` and `defeats` between answers. The statements of the test set require one further relation, between two explanations offered for one observation, neither of which attacks, supports or defeats the other:

- a separation of manifolds that is the mechanism or a trace of a routing process of lower level ([example 9](../../examples/adversarial-statements.md#^example-statement-that-introduces-an-explanatory-gap-rather-than-a-claim));
- a gating mechanism or a change of the decoding basis ([example 23](../../examples/adversarial-statements.md#^example-mixed-epistemic-status-within-a-single-statement));
- context as a separable axis or as a deformation of the whole space ([example 28](../../examples/adversarial-statements.md#^example-statement-using-absence-as-evidence));
- decodability read as evidence of representation or of redundant statistical alignment ([example 3](../../examples/adversarial-statements.md#^example-argument-with-an-undercutting-condition-hidden-inside-an-example)).

The registry must decide whether two candidate answers to one question already state this competition, or whether a relation of competition is declared. The senses of attack, such as `rebuts`, belong to the same goal.

**Literature.** Dung-style abstract argumentation and structured argumentation, as stated in [argumentation theory](../references/argumentation-theory.md).

**Bears on.** [`relation-registry`](../../TODO.md).

## Semantic and justificatory dependence

Two kinds of dependence link records. A record depends semantically on another when its statement cannot be interpreted without the other, as a theorem depends on the definitions of its terms. A record depends justificatorily on another when the other supports its claim, as a proof depends on its lemmas and its assumptions. The candidate vocabulary splits the relations into two strata:

- the relations declared between records: `defines`, from a definition to a concept; `uses`, or `requires_for_interpretation` for a semantic dependence; `assumes`; `proves`, from a proof to a claim; `specializes` and `generalizes`; `exemplifies`; `contradicts` and `refutes`; and `addresses`, to a question;
- the relations relative to an inquiry, which belong to an assembly and not to a record: `selected_for`, `load_bearing_for`, `bridge_for`, `deferred_in` and `ordered_before_in`.

The split keeps a weak relation on the record and a strong one on the assembly. A record states once that it `addresses` a question, whereas its use as a part of the minimal answer of one inquiry is stated by the assembly of that inquiry.

**Literature.** None cited.

**Bears on.** [`relation-registry`](../../TODO.md), and `assembly-schema` for the relations relative to an inquiry.

**Retired source.** `docs/design/_backup/object-types-ontology/relations-graph-edges.md` and `docs/design/3-aspect-specific/semantic-relations.md`, at commit 9e138e2.

## Warrant kinds

Each support relation carries a warrant kind from a closed list: `deductive`, `empirical`, `abductive`, `analogical`, `heuristic`, `methodological`, `definitional` and `interpretive`. Each kind is declared monotonic or defeasible, so the defeasibility of a record is computed from the kinds of the relations that support it, and reported: a record is defeasible when one of its supports is defeasible. Such a computation applies a declared rule to authored relations, which the [decision against inference at run time](../adr/no-run-time-inference.md#^admitted-computation) admits. The retired notes classed `deductive` as monotonic, and `empirical`, `abductive`, `analogical` and `heuristic` as defeasible, and left the three other kinds unclassified.

The list must be aligned with two vocabularies that already exist in the [vocabulary registry](../../src/gnomon/data/vocabularies.yml): the `mode` of an activity, declared under `itinerary`, and the `laws.warrant` of a model and of a background (`derived`, `derived-in-a-limit`, `posited`, `fitted`, `measured`).

**Literature.** None cited.

**Bears on.** [`relation-registry`](../../TODO.md), and `status-propagation`, whose rule of sensitivity reads the warrant kind.

**Retired source.** `docs/design/3-aspect-specific/warrant-vocabulary.md`, at commit 9e138e2.

## Locus of an attack

An attack bears on one of three loci. A rebuttal attacks the claim of an answer. An undercutter grants the grounds and denies that the warrant licenses the step from the grounds to the claim. A third attack rejects the presupposition that the framing of a question carries. The [dotted identifiers](../adr/dotted-identifiers.md) already address a unit nested inside a record, so the locus needs no label of its own: a rebuttal names the answer, and an undercutter names a ground of role `warrant`, or one entry of the dependence of the answer. Two undercutters recur. In method-result circularity, the method partly constructs the object that it then measures. In a critique that re-types the target, the failure of a criterion shows that the inquiry asked for the wrong kind of object.

**Literature.** Structured argumentation, ASPIC+, as stated in [argumentation theory](../references/argumentation-theory.md).

**Bears on.** [`relation-registry`](../../TODO.md), to which the [argumentation relations](#argumentation-relations) already assign the senses of attack.

**Retired source.** `docs/design/3-aspect-specific/arguments-reasoning.md`, at commit 9e138e2.

## Relations between frameworks

The product `inter-theory-relation` of the [registry of product types](../../src/gnomon/data/registries/product-types.yml) has no record yet. Four relations between frameworks would state it: `incommensurable-with`, `translates-into`, `subsumes` and `conflicts-with`. Without them, a comparison of frameworks, a change of paradigm or a claim of incommensurability is asserted in prose instead of recorded.

**Literature.** None cited.

**Bears on.** [`relation-registry`](../../TODO.md), and the product `inter-theory-relation`.

**Retired source.** `docs/design/_backup/object-types-ontology/taxo-criteria-ontology.md`, at commit 9e138e2.
