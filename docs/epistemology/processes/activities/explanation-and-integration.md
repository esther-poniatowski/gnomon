---
tags:
  - theory
  - wip
index: "[Epistemic activities](docs/epistemology/processes/activities/_index.md)"
aliases:
  - Explanatory and integrative activities
  - Explanation (activity)
  - Unification
  - Reduction
  - Integration of theories
---
# Explanation and integration

> [!QUESTION] Goal: which activities explain a phenomenon or relate theories to one another, and by which norm is each judged?

The activities of this family output an explanation or a relation between theories. The word *explanation* names an activity of this family, its product and an aim: the [senses of explanation](epistemic-activities.md#^explanation-senses) separate the three. Each activity of this family is typed by its [signature](epistemic-activities.md#^activity-criterion).

## Signatures

| Activity | Inputs | Output | Mode | Context |
| --- | --- | --- | --- | --- |
| `explanation` | `phenomenon`, `model` (optional), `question` | `explanation` | deductive | justification |
| `unification` | `explanation` (several) | `inter-theory-relation` | deductive | both |
| `reduction` | `model` (two theories) | `inter-theory-relation` | deductive | justification |
| `integration` | `model` (several fields or levels) | `inter-theory-relation` | non-inferential | both |

## Norms

| Activity | Operation | The test `norm.<activity-id>` passes when |
| --- | --- | --- |
| `explanation` | show that the explanans, drawn from a model or from the target description, bears to the phenomenon the relation requested by the question | the requested relation holds between the explanans and the explanandum (e.g. deductive subsumption, causal production, invariant dependence) [hempel1948] [salmon1984] [woodward2003] |
| `unification` | derive many explananda from a small set of argument patterns | the explanations are derived from fewer argument patterns than before [kitcher1989] |
| `reduction` | derive the laws of one theory from the laws of another, with bridge laws that connect their terms | the derivation is valid, and the bridge laws are true or stipulated [nagel1961] |
| `integration` | connect theories of different fields or levels by relations such as part–whole, structure–function or cause–effect, without reducing one to the other | interfield consistency holds: the stated relations agree with the accepted results of each field [darden1977] [mitchell2003] |

## Distinctions

- **An explanation needs a model only when its route runs on one.** When the route of the answer runs on the target description, with no stand-in, the explanans is drawn from the admitted laws and the declarations of the target, and no model enters the step. The input `model` of explanation is therefore optional.
- **Abduction and explanation are separate activities.** [Abduction](ampliative-inference.md) proposes a candidate hypothesis and licenses its pursuit. Explanation works inside the answer schema of a question, and judges whether an explanans bears the requested relation to the phenomenon.
- **Reduction outputs a relation, and the derivation is its evidence.** The output of reduction is the relation between the reduced and the reducing theory, and the derivation with bridge laws shows that the relation holds between the two theories [nagel1961].
- **Reduction and integration differ in the theories kept.** Reduction derives one theory from another, so the reduced theory becomes dispensable in principle. Integration keeps both theories and relates them, as an interfield theory relates genetics and cytology [darden1977].
- **A theory enters this family as a model.** The input type of reduction and integration is `model`, read as a class of models, as the semantic view of [theories](../../vocabulary/representations/theory.md) defines a theory.

## Relations to the method

- **The requested relation of a question fixes the norm of explanation.** A causal, a mechanistic and a mathematical explanation succeed under different conditions, so the norm that judges an explanation follows from the [relation that the question requests](../../objects/task/requested-relation.md).
- **An explanans factor can be the explanandum of a linked question.** *Example*: a question that explains a capacity of readout by the [representation geometry](../../vocabulary/representations/representation-and-encoding.md) links to the question describing that geometry, with the relation `explanans-from` of [linked questions](../../objects/question/question.md#^linked-questions).
- **A bridge law that identifies two quantities can be false.** When a bridge law identifies a separately measured quantity with an aggregate, it states a factual hypothesis.

The fields that record the norm of a step, the links between questions and the admitted laws are documented in the [itinerary record](../../../specification/itinerary.md), in the [question record](../../../specification/question.md) and in the [background record](../../../specification/background.md).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [darden1977] ◐ [Darden & Maull, "Interfield theories", *Philosophy of Science* 44(1), 43–64, 1977](https://doi.org/10.1086/288723)
- [hempel1948] ◐ [Hempel & Oppenheim, "Studies in the logic of explanation", *Philosophy of Science* 15(2), 135–175, 1948](https://doi.org/10.1086/286983)
- [kitcher1989] ◐ [Kitcher, "Explanatory unification and the causal structure of the world", in Kitcher & Salmon (eds.), *Scientific Explanation*, Minnesota Studies in the Philosophy of Science 13, University of Minnesota Press, 410–505, 1989](https://philpapers.org/rec/KITEUA)
- [mitchell2003] ◐ [Mitchell, *Biological Complexity and Integrative Pluralism*, Cambridge University Press, 2003](https://doi.org/10.1017/CBO9780511802683)
- [nagel1961] ◐ [Nagel, *The Structure of Science: Problems in the Logic of Scientific Explanation*, Harcourt, Brace & World, 1961](https://casbs.stanford.edu/structure-science-problems-logic-scientific-explanation)
- [salmon1984] ◐ [Salmon, *Scientific Explanation and the Causal Structure of the World*, Princeton University Press, 1984](https://press.princeton.edu/books/paperback/9780691101705/scientific-explanation-and-the-causal-structure-of-the-world)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
