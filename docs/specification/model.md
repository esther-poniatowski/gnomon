---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Model record
---
# Model record

> [!QUESTION] Goal: what does a researcher write in each field of a model record, and when is each field required?

The [theory of models and bindings](../epistemology/objects/answer/model-and-binding.md) states the grounds of these fields.

A model is a record of its own, which several answers can ground, such as the [answers of two aims](answer.md#^answer-elements) that the model serves. Each answer cites the model instead of declaring it again. ^model-record

A model is a system studied as a stand-in for a target: laws relate quantities that units bear and that take values over indices. Therefore, the model is declared with the blocks and the fields of a [target system](../epistemology/objects/subject/target-system.md), and its laws and organization with those of a [background record](../epistemology/objects/knowledge/background.md). The value sets of the two formats already carry every distinction that a model draws, so no separate vocabulary is needed. The model $M$ holds the elements below. None of them refers to one question, since several questions can share the model. ^model-elements

| Element | When it is required | Content | Constraint on the element | Examples |
| ------- | ------------------- | ------- | ------------------------- | -------- |
| Background — the record from which the laws of the model are derived | when a law of the model carries the warrant `derived` or `derived-in-a-limit` | the identifier of one [background record](../epistemology/objects/knowledge/background.md) | — | the admitted training laws of the networks of a class |
| Constituents $C$ | always | the units that the model treats as bearers | - either units defined by a stated map from the [constituents declared for the target](../epistemology/objects/subject/target-system.md) (e.g. coarse-graining, mode decomposition, aggregation, quotient by a symmetry), or units of the model alone, related to the target only through a binding; <br>- the organization $O$ and the terms $V$ range over these units | the slow eigenmodes of the connectivity (defined by a map); the four tipping elements of a box model of the Earth system (units of the model alone) |
| Index sets | when a quantity of the model is indexed by a set that the target does not declare | the set, its extent and its structure, in the format of a target system | — | a coarse-grained scale; a mode number |
| Variables | always, for each quantity that varies in the model | per variable, its own symbol, signature and value set, and its construction: an expression over the symbols of the model, or a map other than the identity from the quantities that the target declares | - a map from the declarations of the target defines a [derived term](../epistemology/objects/answer/model-and-binding.md#^derived-terms); <br>- a variable never enters by reference to a target quantity, nor by an identity map, which is a reference under another name | the population rate; the overlap with a stored pattern |
| Parameters | when the model holds a quantity fixed | the same content as for a variable, for each quantity that the model holds fixed while the phenomenon unfolds | the parameters that a binding calibrates are marked in that binding, not here | the coupling strength; the adaptation timescale |
| Laws or structural relations $L$ | always | the dependences that link the terms $V$ | - each law states its *warrant* (`derived`, `derived-in-a-limit`, `posited`, `fitted` or `measured`) together with its grounds, and, as a [law of the background](../epistemology/objects/knowledge/background.md#^law-warrant) does, its origin and the range over which it is established; <br>- a law derived in a limit names the assumption of the model that the limit introduces | the mean-field rate equations (derived in a limit); the stability condition that follows from them (derived); a transfer function obtained from recordings (fitted) |
| Organization $O$ | when the parts or the laws stand in a relation on which the behavior of the model depends | per relation, the tuples that it connects and the laws that state it, in the format of a background record | its constituents follow the [definition of a mechanism](../epistemology/objects/answer/mechanism.md) | a delayed feedback loop, in which excitation drives inhibition and is suppressed in return |
| Assumptions of the laws | when a law of the model holds only under an assumption, such as a limit | per assumption, its motive, the gain that it provides, and whether it is removable, as the [rule on idealizations](../epistemology/objects/answer/answer-form.md#^idealizations) defines them | - only the assumptions that the laws of the model require; <br>- whether an assumption is an idealization, and over which range it holds, depends on the target, so each answer that rests on the model classifies it | the mean-field limit, which closes the rate equations (motive: limit; controlled) |

- **A model derived from another model names its parent.** A reduced model, a limit model or a model corrected by de-idealization is derived from a parent model. The typing of the operations that derive it remains open, under the goal `model-design` of the [project goals](../../TODO.md). ^model-parents
