---
tags:
  - definition
  - wip
index: "[Bearers and systems](docs/epistemology/definitions/systems/_index.md)"
aliases:
  - Things and constructs
  - Ontological and representational layers
  - Relational status
  - Target and target specification
---
# Things and constructs

> [!QUESTION] Goal: does a term of the vocabulary name a feature of the world, a role fixed by a choice of the modeller, or a representation, and what changes when the frame is dropped?

The terms of an inquiry fall under three statuses. Two of them come from realist ontology [bunge1977]:

- **things**: concrete entities; each thing has states and changes;
- **constructs**: concepts, propositions and theories; each construct represents things and does not change by itself.

A third status, **relational**, holds of a term whose relata belong to the world while its role is fixed by a chosen boundary or a chosen behavior. A neuron, for instance, is a thing, whereas its being a *constituent* depends on the circuit chosen as the system.

> [!IMPORTANT] Reading aid for the notes
> The frame of this note helps a reader of the notes to keep the senses of a term apart. The records stay neutral between realism and empiricism, as the [decision on the neutrality of the records](../../../adr/neutral-records-on-existence.md) fixes: no field of a record states the status of an item, and an empiricist reading of every record stays admissible.

## Status test

The status of a term is decided by one test. A term is *ontological* when its instances would exist independently of any representation and of any choice of the modeller. A term is *relational* when its relata would exist without representation, and a choice of boundary or of behavior fixes which of them fill its role. A term is *representational* when each of its instances results from a choice of the modeller, such as a codomain, a unit, a level of description or a wording. ^layer-test

## Two senses of target

"Target" names two objects with different statuses: ^target-senses

- the **target** is the system, or the class of systems, that an inquiry is about. The target can be a class of merely possible systems. Its members belong to the world or to the space of possible systems, and the inquiry chooses which systems form the target, so the target is relational;
- the **target specification** is the record of kind `target-system` that delimits the target, through its identification and its declared quantities. The target specification is a construct.

The [specification of the target system](../../subject/target-system.md) fixes the fields of the target specification. An error in delimiting the target lies in the target specification, and revising the record can correct the error.

## Assignment of the terms

Each term of the [vocabulary of inquiry](../_index.md) takes one status. A term with two senses on two statuses takes one row per sense.

| Term | Status | Justification |
| --- | --- | --- |
| [Entity](entity-object-thing.md) | ontological | anything that exists, whether or not it is represented |
| [Object](entity-object-thing.md), in ontology | ontological | a particular that bears properties |
| [Object](entity-object-thing.md), in logic | representational | an element of the domain of a structure, possibly standing for no thing |
| [Thing](entity-object-thing.md) | ontological | a concrete object that changes state |
| [System](system-constituent-environment.md) | relational | the constituents are in the world, and the boundary is chosen |
| [Constituent](system-constituent-environment.md) | relational | a part of the world that fills a role relative to a chosen system |
| [Environment](system-constituent-environment.md) | relational | the things that act across a chosen boundary |
| [Structure](system-constituent-environment.md) | relational | the relations hold in the world, and the chosen system fixes which of them count |
| [Organization](system-constituent-environment.md) | relational | the relations hold in the world, and a chosen behavior selects those on which it depends |
| [Property](property-attribute-predicate.md) | ontological | a feature that a thing has whether or not it is represented |
| [Relation](property-attribute-predicate.md) | ontological | the counterpart of a property for several bearers |
| [Attribute](property-attribute-predicate.md) | representational | a concept with a chosen codomain and unit |
| [Predicate](property-attribute-predicate.md) | representational | an expression of a chosen language |
| [Kind](kind-class-population.md) | ontological | a collection whose members share properties that support projection |
| [Class](kind-class-population.md) | representational | a collection fixed by a chosen membership condition |
| [Population](kind-class-population.md) | representational | a class chosen so that a target quantity is defined over it |
| [Variable](../quantities/variable-value-observable.md) | representational | a function with a chosen domain and codomain |
| [Value](../quantities/variable-value-observable.md) | representational | an element of a chosen codomain |
| [Parameter](../quantities/variable-value-observable.md) | representational | a variable that a chosen phenomenon holds constant |
| [Observable](../quantities/variable-value-observable.md), in the empiricist sense | ontological | an entity detectable by the unaided senses |
| [Observable](../quantities/variable-value-observable.md), in the physical and control senses | representational | a function on a chosen state space |
| [Data](../quantities/variable-value-observable.md) | representational | records produced by one chosen procedure |
| [Scale](../quantities/scale-and-level.md) | representational | a homomorphism into a chosen numerical structure, or a chosen extent and resolution |
| [Level of description](../quantities/scale-and-level.md) | representational | a chosen vocabulary for one system |
| [Level of organization](../quantities/scale-and-level.md) | relational | the parts are in the world, and the mechanism chosen fixes the ordering |
| [State](../quantities/state-and-configuration.md), as the condition of a thing | ontological | the condition in which a thing is at one time |
| [State](../quantities/state-and-configuration.md), as a tuple of values | representational | the values of chosen state variables |
| [State space](../quantities/state-and-configuration.md) | representational | the set of tuples over chosen variables |
| [Configuration](../quantities/state-and-configuration.md) | relational | the arrangement holds in the world at one instant, and the chosen system fixes which things it arranges |
| [Condition](../quantities/condition.md) | representational | a constraint that an inquiry takes as given |
| [Invariant and symmetry](../quantities/invariant-and-symmetry.md) | representational | each is relative to a stated set of transformations |
| [History](../change/process-event-history.md), as an occurrent | ontological | the sequence of changes undergone by one thing |
| [State, process and event](../change/process-event-history.md), as classes of predicates | representational | predicates on the segments of a chosen course, at a chosen grain |
| [Course and grain](../change/process-event-history.md) | representational | a chosen index set and a chosen resolution |
| [Mechanistic activity](../change/mechanistic-activity.md) | ontological | a producer of change in the world |
| [Activity](../change/mechanistic-activity.md), as a state variable | representational | a variable of a chosen model |
| [Epistemic activity](../../activities/epistemic-activities.md) | ontological | an act of inquirers, occurring whether or not a record describes it |
| [Dynamic](../change/dynamic.md) | representational | an evolution map over a chosen state space |
| [Action and interaction](../change/interaction-and-cause.md) | ontological | one thing changes the history of another |
| [Statistical interaction](../change/interaction-and-cause.md) | representational | a property of a model of effects, relative to a chosen scale |
| [Cause](../change/interaction-and-cause.md) | representational | the interventionist and structural definitions relate chosen variables |
| [Function](../change/function.md) | relational | the contribution of a component to a chosen capacity |
| [Computing](../change/computation.md) | relational | the physical process belongs to the world, and a chosen implementation map fixes which computation it is |
| [Function computed and implementation map](../change/computation.md) | representational | maps between chosen spaces of inputs, outputs and states |
| [Capacity and disposition](../regularities/capacity-and-disposition.md) | ontological | a property held whether or not it is manifested |
| [Law₁](../regularities/law.md) | ontological | a lawlike regularity among the states of things |
| [Law statement](../regularities/law.md) | representational | a general claim in a chosen vocabulary |
| [Regularity, spatial or temporal pattern](../regularities/pattern-and-phenomenon.md) | ontological | an invariant across instances, or one structured configuration |
| [Phenomenon](../regularities/pattern-and-phenomenon.md) | relational | a feature of the world, whose role as explanandum a chosen question fixes |
| [Appearance](../regularities/pattern-and-phenomenon.md) | representational | the content of an observation or the outcome of a measurement |
| [Mechanism](../regularities/mechanism-and-mechanistic-model.md) | relational | entities and activities in the world, individuated by the phenomenon chosen |
| [Mechanistic model](../regularities/mechanism-and-mechanistic-model.md) | representational | a representation of a mechanism |
| [Model](../representations/model.md), in the representational sense | representational | an object used to represent a target |
| [Model system](../representations/model.md) | relational | an object whose role as stand-in is fixed by its use |
| [Target](#^target-senses) | relational | systems of the world, or possible systems, chosen as the object of an inquiry |
| [Target specification](#^target-senses) | representational | a record that delimits a target |
| [Encoding and readout](../representations/representation-and-encoding.md) | representational | maps between a chosen input space, a chosen state space and a chosen output space |
| [Representation](../representations/representation-and-encoding.md) | relational | the states belong to the system, and the readouts that use them fix which states represent |
| [Representation geometry](../representations/representation-and-encoding.md) | representational | a property of an encoding map over chosen variables |
| [Idealization and abstraction](../representations/idealization-and-abstraction.md) | representational | a chosen distortion or omission of a model |
| [Theory](../representations/theory.md) | representational | a set of claims, or a class of models |
| [Framework and formalism](../representations/framework.md) | representational | a chosen vocabulary, set of elements, or calculus |
| [Claim and hypothesis](../representations/claim-and-hypothesis.md) | representational | a proposition put forward for evaluation |
| [Epistemic problem](../../inquiry/epistemic-problem.md) | representational | a demand stated relative to a background of accepted claims |
| [Question](../../inquiry/question.md) | representational | a request with a set of answers |
| [Level of commitment](../../inquiry/question.md#^commitment-levels) | representational | the extent to which a record fixes the referent of a slot |

Two groups of terms invite a confusion of statuses: the terms that take two rows, and the relational terms. For each term with two senses, the note defining it fixes a name for each sense.

## Status of the frame

The frame is realist, and it is **not forced**: the [note on existence and access](../representations/existence-and-access.md) states the positions that read the records otherwise. An empiricist reading keeps the representational status alone. The empiricist reading turns property, law₁ and mechanism into features of representations, and it reads a relational term as a role within a representation. The definitions of this folder state the realist sense first, because the existing notes of the method use it, for instance in the [constitutive requested relation](../../epistemic-task/requested-relation.md). Each definition keeps its representational sense explicit, so that an empiricist reader can drop the other senses without losing the vocabulary.

## Distinctions

- **A target specification is a model of its target.** The target specification, with its background, represents the target, so it is a model in the representational sense, as the [note on models](../representations/model.md#^target-description-is-a-model) states. The target and the target specification therefore separate an object from its description, never a reality known directly from a representation of it.
- **Every field of a record holds a construct.** A record is a representation, so the [status test](#^layer-test) places all its contents among the constructs. The ontological and relational terms name the *subject* of those contents. *Example*: the reading of a declared variable names the property in words, whereas its symbol and its value set form the attribute.
- **A declaration of a quantity has no truth value, and it can still be inadequate.** A declaration introduces a quantity, and an aggregation map defines one, so neither makes a claim. Each declaration nevertheless presupposes that the quantity represents a property of the target, or an admissible aggregate of properties. That presupposition can fail. A quantity defined in the manner of "grue" is well formed, yet it supports no projection [goodman1955]. Such a quantity represents no [property](property-attribute-predicate.md) of the target. Therefore, a declaration is assessed for its adequacy, whereas a claim is assessed for its truth. The [admissibility of an aggregate](../../subject/target-system.md#^aggregate-admissibility) tests that presupposition for aggregates.
- **A construct can be false only when it makes a claim.** A law statement, for instance, asserts a relation among quantities and can be false of the target. The [aggregation maps and bridge laws](../../subject/target-system.md) of a target specification follow this division: the map defines a quantity, and the bridge law asserts an identity that can fail.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bunge1977] ◐ [Bunge, *Treatise on Basic Philosophy*, vol. 3, *Ontology I: The Furniture of the World*, Reidel, 1977](https://doi.org/10.1007/978-94-010-9924-0)
- [goodman1955] ◐ [Goodman, *Fact, Fiction, and Forecast*, Harvard University Press, 1955](https://plato.stanford.edu/entries/goodman/); "grue" in ch. III, §4
