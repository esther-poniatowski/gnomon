---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Model
  - Model system
  - Representation (model and target)
tags: []
source:
---
# Model

> [!QUESTION] Goal: which of the four senses of "model" does a statement use, and how is a model related to the system that it represents?

"Model" carries four senses, separated in the literature on models in science [frigg2025]. Two senses are logical, since they make a model a structure that satisfies sentences. The other two make a model a stand-in for a target: an object used to represent the target, or a family of probability distributions.

## Senses

| Sense | Community | Definition | Source |
| --- | --- | --- | --- |
| Logical | logic, model theory | a structure that satisfies a set of sentences, under an interpretation of their non-logical symbols | [hodges1993] |
| Semantic view | philosophy of science | a set-theoretical structure that satisfies the predicate defining a theory; in this view, a theory is identified with a class of such structures | [suppes1960]; [vanfraassen1980] |
| Representational | philosophy of science | an object, concrete, mathematical or computational, used to represent a target system | [giere1988]; [giere2004]; [morgan1999]; [weisberg2013] |
| Statistical | statistics | a family $\{P_\theta:\theta\in\Theta\}$ of probability distributions on a sample space, indexed by a parameter | [mccullagh2002] |

The senses are related but not interchangeable. A mathematical model in the representational sense is often a structure in the semantic sense, but the representational sense adds a target and a relation to that target. A statistical model is a representational model whose objects are distributions. The relation of a statistical model to its target is the claim that the data were drawn from one member of the family.

## Model system and target

A **model system** is the object studied in place of a **target**: the system, or the class of systems, about which knowledge is sought. A target can be a class of merely possible systems. The record that delimits a target is its **target specification**, a construct, as the [two senses of target](things-and-constructs.md#^target-senses) separate them. The model system and the target are linked by a relation of representation, never by identity [giere2004] [weisberg2013]. Three relations are proposed for that link:

| Relation | Requirement on the model | Example |
| --- | --- | --- |
| Similarity | the model resembles the target in specified respects and to specified degrees | a rate model similar to a cortical population in its oscillation frequency |
| Isomorphism | a bijection between the model and the target preserves every relation of the model | — |
| Partial homomorphism | a map preserves some relations of the model, for some elements | a network model whose connectivity matches the measured connectivity of some neurons only |

Strict isomorphism is rarely met by an empirical target. Accounts of scientific representation have weakened that requirement to partial morphisms or replaced it by similarity [frigg2025].

## Distinctions

- **A model is itself a system, studied as a stand-in.** The test is the use of the object: a system counts as a model when it is studied to learn about a target other than itself. A cell culture is the target of one inquiry and a model system of a brain region in another.
- **A model and a theory are separated by the [vocabulary of theories](theory.md).** That note states the relation under each view of theories.
- **A model and a mechanism belong to different layers.** A mechanism is separated from a mechanistic model in the [vocabulary of mechanism](mechanism-and-mechanistic-model.md).

## Consequences for a record

- **A candidate answer whose route runs on a model rests on a model in the representational sense.** The [model record](../model-and-binding.md#^model-record) declares that model with the blocks of a [target specification](../target-system.md), and a [binding](../model-and-binding.md#^binding-record) relates it to the phenomenon. The feature pairs of the binding state the respects of similarity, and the tolerance that the [required accuracy](../epistemic-task.md) of the question fixes states the degrees.
- **The target of the benchmark is a class of possible systems.** The benchmark project studies networks in their most abstract form, a class that encompasses artificial and biological networks. Therefore, its target specification states `target_type: possible-systems`. A network model of that class represents members of the class, and it is not a model of cortex. A claim about cortex requires cortex as a second target, and a relation of representation between the class and cortex.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [frigg2025] ◐ [Frigg & Hartmann, "Models in science", *Stanford Encyclopedia of Philosophy*, substantive revision 2 April 2025](https://plato.stanford.edu/entries/models-science/)
- [giere1988] ◐ [Giere, *Explaining Science: A Cognitive Approach*, University of Chicago Press, 1988](https://press.uchicago.edu/ucp/books/book/chicago/E/bo3622319.html)
- [giere2004] ◐ [Giere, "How models are used to represent reality", *Philosophy of Science* 71(5), 742–752, 2004](https://doi.org/10.1086/425063)
- [hodges1993] ◐ [Hodges, *Model Theory*, Cambridge University Press, 1993](https://doi.org/10.1017/CBO9780511551574)
- [mccullagh2002] ◐ [McCullagh, "What is a statistical model?", *Annals of Statistics* 30(5), 1225–1310, 2002](https://doi.org/10.1214/aos/1035844977)
- [morgan1999] ◐ [Morgan & Morrison (eds.), *Models as Mediators: Perspectives on Natural and Social Science*, Cambridge University Press, 1999](https://doi.org/10.1017/CBO9780511660108)
- [suppes1960] ◐ [Suppes, "A comparison of the meaning and uses of models in mathematics and the empirical sciences", *Synthese* 12(2–3), 287–301, 1960](https://doi.org/10.1007/BF00485107)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001)
- [weisberg2013] ◐ [Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013](https://doi.org/10.1093/acprof:oso/9780199933662.001.0001)
