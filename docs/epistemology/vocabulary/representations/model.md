---
tags:
  - definition
  - wip
index: "[Representations](docs/epistemology/vocabulary/representations/_index.md)"
aliases:
  - Model
  - Model system
  - Representation (model and target)
---
# Model

> [!QUESTION] Goal: which of the four senses of "model" does a statement use, which role does a model play in the representational sense, and how is a model related to the system that it represents?

"Model" carries four senses, separated in the literature on models in science [frigg2025]. Two senses are logical, since they make a model a structure that satisfies sentences. The representational sense makes a model an object used to represent a target, and that object is either the description of the target itself or a stand-in for the target. The statistical sense makes a model a family of probability distributions. The theory uses the semantic-view sense, for theories, and the representational sense, which divides by role into the target description and the model system. The [senses table of the overview](../../foundations/overview.md#^senses-table) separates these uses from the record and the form that also carry the word.

## Senses

| Sense | Community | Definition | Source |
| --- | --- | --- | --- |
| Logical | logic, model theory | a structure that satisfies a set of sentences, under an interpretation of their non-logical symbols | [hodges1993] |
| Semantic view | philosophy of science | a set-theoretical structure that satisfies the predicate defining a theory; in this view, a theory is identified with a class of such structures | [suppes1960]; [vanfraassen1980] |
| Representational | philosophy of science | an object, concrete, mathematical or computational, used to represent a target system | [giere1988]; [giere2004]; [morgan1999]; [weisberg2013] |
| Statistical | statistics | a family $\{\mathbb{P}_\theta:\theta\in\Theta\}$ of probability distributions on a sample space, indexed by a parameter $\theta$ that ranges over a parameter set $\Theta$ | [mccullagh2002] |

The senses are related but not interchangeable. A mathematical model in the representational sense is often a structure in the semantic sense, but the representational sense adds a target and a relation to that target. A statistical model is a representational model whose objects are distributions. The relation of a statistical model to its target is the claim that the data were drawn from one member of the family.

## Model system and target

A **model system** is the object studied in place of a **target**: the system, or the class of systems, about which knowledge is sought. A target can be a class of merely possible systems. The record that delimits a target is its **target specification**, a construct, as the [two senses of target](../../foundations/things-and-constructs.md#^target-senses) separate them. The model system and the target are linked by a relation of representation, never by identity [giere2004] [weisberg2013]. Three relations are proposed for that link:

| Relation | Requirement on the model | Example |
| --- | --- | --- |
| Similarity | the model resembles the target in specified respects and to specified degrees | a rate model similar to a cortical population in its oscillation frequency |
| Isomorphism | a bijection between the model and the target preserves every relation of the model | — |
| Partial homomorphism | a map preserves some relations of the model, for some elements | a network model whose connectivity matches the measured connectivity of some neurons only |

Strict isomorphism is rarely met by an empirical target. Accounts of scientific representation have weakened that requirement to partial morphisms or replaced it by similarity [frigg2025]. The binding of this method takes no position among these relations as accounts of the constitution of representation, as the [neutrality of the binding](../../objects/answer/model-and-binding.md#^binding-neutrality) states.

## Distinctions

- **A model system is a system studied as a stand-in.** The test is the use of the object: a system counts as a model system when it is studied to learn about a target other than itself. This test defines the model system only, since the description of a target is a model with no stand-in, as the next distinction states. A cell culture is the target of one inquiry and a model system of a brain region in another.
- **The description of a target is a model of that target.** A target specification with its background, the laws admitted about the target, represents the target, so it is a model in the representational sense. The method calls *model record* only the record of a system other than the target, studied in its place. The two differ by their role, the description of the target against a stand-in, and both are representations, as the [note on existence and access](../../foundations/existence-and-access.md#^method-stance) states. ^target-description-is-a-model
- **A model is classified by its role and by its form, independently.** Its role is the description of a target or a stand-in for it. Its form is, for instance, mechanistic, phenomenological or statistical. A *mechanistic model* is a model of mechanistic form in either role, as the [test of a mechanistic model](../regularities/mechanism-and-mechanistic-model.md#^mechanistic-model-test) decides, so the word qualifies the form of a model, never its role.
- **A model and a theory are separated by the [vocabulary of theories](theory.md).** That note states the relation under each view of theories.
- **A model and a mechanism belong to different layers.** A mechanism is separated from a mechanistic model in the [vocabulary of mechanism](../regularities/mechanism-and-mechanistic-model.md).

## Relations to the method

- **A model in the representational sense has four elements.** The method writes a model as $M=\langle C,V,L,O\rangle$, with the symbols of the [notation](../notation/notation.md): ^model-elements
    - the constituents $C$: the units that the model treats as bearers: the constituents declared for the target, units defined from them by a stated map, or units of the model alone;
    - the terms $V$: the variables and the parameters that the constituents bear;
    - the laws $L$: the general claims that link the terms, each with its role, as the [law of a record](../regularities/law.md#^law-of-a-record) defines them; in a mechanistic model, each law represents one activity;
    - the organization $O$: the relations among the constituents and the laws on which the behavior of the model depends; in a mechanistic model, these are the relations among parts and activities that the [vocabulary of systems](../systems/system-constituent-environment.md) calls organization.

  The description of a target has the same four elements, filled by the target specification and its background. The fields that record each element are documented in the [model record](../../../specification/model.md#^model-elements).
- **Every candidate answer rests on a model in the representational sense.** A candidate answer is an answer put forward and not yet accepted, and its route is the derivation or the study through which it is reached. When the route runs on the target description, with no stand-in, the model is that description. When the route runs on a stand-in, the model is a model system, and a binding states which inferences from the model to the target its asserter licenses. The object on which the route runs decides which records the answer needs, as the [records of a model and a binding](../../objects/answer/model-and-binding.md#^when-a-binding) state.
- *Example*: a study of networks in their most abstract form, a class that encompasses artificial and biological networks, takes a class of possible systems as its target. A network model of that class represents members of the class, and it is not a model of cortex. A claim about cortex requires cortex as a second target, and a relation of representation between the class and cortex.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [frigg2025] ◐ [Frigg & Hartmann, "Models in science", *Stanford Encyclopedia of Philosophy*, substantive revision 2 April 2025](https://plato.stanford.edu/entries/models-science/)
- [giere1988] ◐ [Giere, *Explaining Science: A Cognitive Approach*, University of Chicago Press, 1988](https://press.uchicago.edu/ucp/books/book/chicago/E/bo3622319.html)
- [giere2004] ◐ [Giere, "How models are used to represent reality", *Philosophy of Science* 71(5), 742–752, 2004](https://doi.org/10.1086/425063)
- [hodges1993] ◐ [Hodges, *Model Theory*, Cambridge University Press, 1993](https://doi.org/10.1017/CBO9780511551574)
- [mccullagh2002] ◐ [McCullagh, "What is a statistical model?", *Annals of Statistics* 30(5), 1225–1310, 2002](https://doi.org/10.1214/aos/1035844977)
- [morgan1999] ◐ [Morgan & Morrison (eds.), *Models as Mediators: Perspectives on Natural and Social Science*, Cambridge University Press, 1999](https://doi.org/10.1017/CBO9780511660108)
- [suppes1960] ◐ [Suppes, "A comparison of the meaning and uses of models in mathematics and the empirical sciences", *Synthese* 12(2–3), 287–301, 1960](https://doi.org/10.1007/BF00485107)
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); a theory presented by a family of models, ch. 3, p. 64, checked through the [SEP entry on constructive empiricism](https://plato.stanford.edu/entries/constructive-empiricism/)
- [weisberg2013] ◐ [Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013](https://doi.org/10.1093/acprof:oso/9780199933662.001.0001)
