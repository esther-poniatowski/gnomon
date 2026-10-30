---
tags:
  - reference
index: "[References](docs/references/_index.md)"
aliases:
  - OntoClean
---
# OntoClean

OntoClean is a methodology for validating the ontological adequacy of taxonomic relationships, introduced by Guarino and Welty in 2000 [guarino2004]. The methodology characterizes the intended meaning of each property of an ontology by formal metaproperties, drawn from the philosophical notions of essence, identity and unity. These metaproperties impose constraints on subsumption, and a violated constraint reveals a subsumption link that misrepresents the intended meaning [guarino2004].

## Method

### Properties and subsumption

A property is the meaning, or intension, of an expression such as *being an apple*. Its class, or extension, is the set of its instances in one possible state of affairs. A property $p$ subsumes a property $q$ if and only if, in every possible state of affairs, every instance of $q$ is an instance of $p$ [guarino2004]. Subsumption is therefore a modal relation between properties, not a relation between the classes of one state of affairs.

### Metaproperties

| Metaproperty | Marks | Definition |
| --- | --- | --- |
| Rigidity | `+R` rigid · `-R` semi-rigid · `~R` anti-rigid | a property is *essential* to an entity when the entity must have it in every possible state of affairs; a property is *rigid* when it is essential to all its instances, *anti-rigid* when it is essential to none of them, and *semi-rigid* when it is essential to some instances and not to others |
| Identity | `+I` carries an identity criterion · `+O` supplies its own · `-I` carries none | an identity criterion states the conditions that determine and are entailed by the equality of two instances; `+O` marks a property that supplies a criterion not inherited from a subsuming property |
| Unity | `+U` carries a common unity criterion · `-U` carries none · `~U` anti-unity | a unity criterion states the conditions under which the parts of an entity form one whole; under anti-unity, no instance of the property is necessarily a whole |
| Dependence | `+D` · `-D` | the overview relies on intuitive examples and leaves dependence informal; its formal treatment is given by Welty and Guarino [welty2001] |

*Being a student* is anti-rigid, since every student can cease to be one, whereas *being a human* is rigid. *Being an amount of water* is anti-unitary, *being an ocean* carries unity, and *being a legal agent* carries no common unity criterion, since its instances include both persons and companies [guarino2004].

### Constraints

When a property $q$ subsumes a property $p$, four constraints hold [guarino2004]:

1. if $q$ is anti-rigid, then $p$ is anti-rigid;
2. if $q$ carries an identity criterion, then $p$ carries the same criterion;
3. if $q$ carries a unity criterion, then $p$ carries the same criterion;
4. if $q$ has anti-unity, then $p$ has anti-unity.

Two assumptions on identity, adapted from Lowe, complete the constraints. Under *sortal individuation*, every entity instantiates some property that carries an identity criterion. Under *sortal expandability*, an entity that instantiates several such properties also instantiates a more general property that carries a criterion of its identity. Together, the two assumptions imply that every entity instantiates a unique most general property carrying its identity criterion [guarino2004].

### Backbone taxonomy

The *backbone taxonomy* is the taxonomy of the rigid properties of an ontology, ordered by subsumption. The backbone represents the invariant aspects of the domain, and no element of the domain is lost by restricting attention to it, since every element instantiates at least one backbone property that supplies its identity criterion [guarino2004]. The analysis therefore checks the backbone first, and adds the non-rigid properties afterward.

### Kinds of non-rigid property

| Kind | Metaproperties | Example | Treatment |
| --- | --- | --- | --- |
| Phased sortal | independent, anti-rigid, supplies an identity criterion | *caterpillar*, *butterfly* | each phase is subsumed by a rigid property that supplies an identity criterion across the phases, such as *lepidopteran* |
| Role | anti-rigid, supplies no identity criterion; characterizes the way in which an entity participates in a contingent event or state of affairs | *agent*, *food*, *legal agent* | a role never subsumes a rigid property; a statement that the instances of a rigid property *can* play the role is a type restriction, stated by a covering axiom or elsewhere than in the taxonomy |
| Attribution | `-I-U-R` | *red* (thing) | the property is represented by an attribute and a value, such as a colour, and stays out of the backbone |

### Misuses of subsumption

The worked example of the overview traces most violations to a linguistic "is a" read as subsumption [guarino2004]:

- **Constitution.** A living being is constituted of an amount of matter, and is not itself an amount of matter: anti-unity cannot subsume unity, and the two properties carry different identity criteria. The link becomes a relation of constitution.
- **Type restriction.** "An animal can be an agent" restricts the type of the role *agent*. Subsuming *animal* under *agent* makes an anti-rigid property subsume a rigid one.
- **Purpose.** "An apple is food" states a purpose of apples. Under the role reading of *food*, the link is removed.
- **Polysemy.** *Country* lumps a geographical region and a geopolitical entity. Splitting it into two rigid properties removes the anti-rigidity that the merged property showed.

### Scope

OntoClean evaluates the subsumption links between properties. The methodology does not choose the properties of an ontology, and its metaproperty assignments record modelling choices: the point of the analysis is to explore the logical consequences of those choices, not to decide the ontological nature of a property [guarino2004]. The full taxonomy of property kinds, with the formal treatment of dependence, is given by Welty and Guarino [welty2001].

## Bearing on gnomon

OntoClean constrains subsumption between properties, so it applies to `gnomon` wherever the framework or a researcher asserts that every instance of one kind is an instance of another.

- **The status of the terms of the method.** The [statuses of a term](../epistemology/definitions/systems/things-and-constructs.md) separate a feature of the world from a role fixed by a chosen boundary or a chosen behavior. System, constituent and environment are [roles](../epistemology/definitions/systems/system-constituent-environment.md), and so are the target and the model system. These terms are anti-rigid in the sense of OntoClean. The method states that "a model is itself a system", which is a subsumption between two roles and satisfies the first constraint.
- **The slots of a record.** A slot of a question awaits a referent of a declared type, such as a `system` in the target-system slot. Such a slot states a type restriction, stated by the type of the slot rather than by subsumption, as OntoClean prescribes for roles.
- **The record kinds.** A record of each kind carries its own identifier, so the kind of a record supplies an identity criterion for its instances. The components of a record, such as the contrast or the domain of a question, carry no identifier and exist only as parts of their record. Identity, not rigidity, therefore separates a record kind from a component of a record. A folder of notes is a container rather than a subsumption, so the constraints of OntoClean do not bind the layout of the documentation.
- **The taxonomies built by a researcher.** The activity `classification` builds classes from the attributes of a [qualitative feature system](../procedures/classification/construction-procedure.md). OntoClean classes a property defined by an attribute value as an attribution, which stays out of a backbone taxonomy. The taxonomic layer that the [proposals for the classification method](../proposals/classification-method.md) compare can therefore be checked against the four constraints.

## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [guarino2004] ✓ [Guarino and Welty, "An overview of OntoClean", in Staab and Studer (eds.), *Handbook on Ontologies*, Springer, 2004, pp. 151–171](https://www.loa.istc.cnr.it/wp-content/uploads/2020/03/OverviewOntoClean-compresso.pdf)
- [welty2001] ○ Welty and Guarino, "Supporting ontological analysis of taxonomic relationships", *Data and Knowledge Engineering*, 39(1), 2001, pp. 51–74
