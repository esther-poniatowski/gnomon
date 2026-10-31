---
tags:
  - definition
  - wip
index: "[Representations](docs/epistemology/vocabulary/representations/_index.md)"
aliases:
  - Claim and hypothesis
  - Claim
  - Hypothesis
  - Prediction (product)
  - Explanation (product)
---
# Claim and hypothesis

> [!QUESTION] Goal: what turns an expression into a claim, and which kinds of claim does an inquiry produce?

A **claim** is a proposition put forward for evaluation. A claim carries two attributes: the **attitude** taken toward it, and the **support** that it has. The kinds of claim produced by an inquiry differ in attitude or in content:

- a hypothesis is a claim held under the attitude *hypothesized*;
- a prediction states values not yet observed;
- an explanation states that an explanans explains an explanandum under a requested relation.

The explanans is the set of factors that explain, and the explanandum is the phenomenon explained. The requested relation is the kind of dependence that the question asks the explanation to state, as the note on the [requested relation](../../objects/task/requested-relation.md) defines it.

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Claim | logic, epistemology | a proposition put forward for evaluation, supportable or refutable by evidence or by proof | — |
| Hypothesis, as an attitude | general usage, this method | a claim held provisionally, while it is tested; in a record, a claim held under the attitude `hypothesized` | — |
| Hypothesis, as an ampliative product | logic of inference | a claim whose content exceeds that of its premises, reached by an [ampliative inference](../../processes/activities/ampliative-inference.md), such as an induction or an abduction | — |
| Hypothesis, as a target claim | this method | a claim about the target, as opposed to a consequence, which holds of a model and may fail of the target | — |
| Resistance hypothesis | this method | the hypothesis $\eta$ that explains why the formulation of a question resists the inquiry, by a hidden assumption, a missing property or an inadequate formalism, as the [types of serving question](../../processes/inquiry/question-decomposition.md#^functional-types) use it | — |
| Theoretical hypothesis | semantic view of theories | the claim that a model is similar to a target system in specified respects and to specified degrees | [giere1988] |
| Empirical claim | structuralist view of theories | the claim that the intended applications of a theory-element can be completed into its actual models | [balzer1987] |
| Prediction | philosophy of science | a claim about the values of observables not yet observed, derived from a model and conditions | [hempel1948] |
| Explanation | philosophy of science | a pair of an explanans and an explanandum, in which the explanans bears to the explanandum a relation that counts as explanatory: deductive subsumption, causal production, or another | [hempel1948]; [salmon1984] |

The relations that count as explanatory are compared in the note on the [requested relation](../../objects/task/requested-relation.md). This note does not restate that comparison.

## Distinctions

Three kinds of expression are often confused. Each kind adds properties to the kind listed before:

| Expression | Has a truth value? | General? | Supports counterfactuals and holds over a range of interventions? | Example |
| --- | --- | --- | --- | --- |
| [Predicate](../systems/property-attribute-predicate.md) | no | — | — | "$o$ oscillates at frequency $\nu$" |
| Claim | yes | not necessarily | not necessarily | "this network oscillates at 40 Hz" |
| [Law statement](../regularities/law.md) | yes | yes | yes | "the frequency of the oscillation is inversely proportional to the inhibitory time constant" |

The law statement of this table is a law in the lawhood sense. A [law of a record](../regularities/law.md#^law-of-a-record) is a general claim that need not support counterfactuals.

The attitude and the support of a claim take values in two closed lists: ^attitude-support

| Attribute | Content | Values |
| --- | --- | --- |
| Attitude | the stance of the inquiry toward the claim | `entertained`, `hypothesized`, `accepted`, `retracted` |
| Support | the grounds of the claim, independent of the attitude | `unsupported`, `informal`, `formally-proven`, `empirically-supported` |

The other statuses of an inquiry, such as the warrant of a law or the evidential status of a phenomenon, qualify other bearers along other axes, as the [table of statuses](../../objects/status/statuses-and-acceptance.md#^status-axes) places them.

- **The senses of hypothesis are told apart by the claim that each sense opposes to a hypothesis.** The attitude opposes it to an entertained or an accepted claim. The ampliative product opposes it to the premises of the inference that reaches it. The target claim opposes it to a consequence, which holds of a model. The resistance hypothesis $\eta$ bears on the formulation of a question, not on its target. The theoretical hypothesis is a target claim of one form: it states that a model is similar to its target in stated respects and degrees, which the computed pairs of a binding assert, as the [neutrality of the binding](../../objects/answer/model-and-binding.md#^binding-neutrality) states. Several senses can hold of one claim: an abduction, the inference to a hypothesis that would explain the evidence, reaches a claim about the target, and the inquiry holds that claim under the attitude `hypothesized`. The product type `hypothesis` of the epistemic activities takes one combination of these senses, as the [product types](../../processes/activities/epistemic-activities.md#^product-types) state.
- **A hypothesis and an accepted claim differ by attitude only.** Their content can be identical: the same proposition is hypothesized while it is tested, and accepted once the researcher accepts it into the accepted knowledge $K$, the claims accepted by an act of the researcher. The verdicts of its [assessment](../../objects/answer/satisfaction-conditions.md), the record of the tests applied to it, inform that act without computing it, as the [act of acceptance](../../objects/status/statuses-and-acceptance.md#^acceptance-act) states.
- **The attitude and the support vary independently.** *Examples*: a claim can be hypothesized with informal support, or accepted with no more than informal support. A formally proven claim can be retracted when its assumptions turn out to be false of the target.
- **An explanation, as a product, is a claim.** Its content is that the explanans $E$ explains the phenomenon $P$ under the requested relation $R$. Therefore, the explanation carries an attitude and a support, as any claim does. The activity of explaining is typed in the [taxonomy of epistemic activities](../../processes/activities/epistemic-activities.md).
- **A prediction and an explanation can share their logical form.** In the deductive-nomological model, both derive the explanandum from laws and conditions. The two differ in the epistemic status of the explanandum, already known or not yet known [hempel1948]. A prediction may rest on a symptom that does not cause the predicted event. Therefore, an account that requires a causal relation between explanans and explanandum admits such a prediction and refuses the corresponding explanation.

## Relations to the method

- An answer whose attitude is `hypothesized` is a hypothesis.
- **The laws on which a candidate answer rests are claims, each with a warrant of its own.** The [warrant of a law](../../objects/knowledge/background.md#^law-warrant) traces the law to its origin, so it differs from the support of the claim of an answer.
- **The conditions of satisfaction fix the tests of the claims before evaluation.** Before any answer is assessed, the [conditions of satisfaction](../../objects/answer/satisfaction-conditions.md) state the tests deciding whether its claims hold.

The fields that bear on the attitude and the support of a claim are documented in the [answer record](../../../specification/answer.md#^status-and-support).

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [balzer1987] ◐ [Balzer, Moulines & Sneed, *An Architectonic for Science: The Structuralist Program*, Reidel, 1987](https://doi.org/10.1007/978-94-009-3765-9)
- [giere1988] ◐ [Giere, *Explaining Science: A Cognitive Approach*, University of Chicago Press, 1988](https://press.uchicago.edu/ucp/books/book/chicago/E/bo3622319.html); p. 81, checked through secondary sources
- [hempel1948] ◐ [Hempel & Oppenheim, "Studies in the logic of explanation", *Philosophy of Science* 15(2), 135–175, 1948](https://doi.org/10.1086/286983)
- [salmon1984] ◐ [Salmon, *Scientific Explanation and the Causal Structure of the World*, Princeton University Press, 1984](https://press.princeton.edu/books/paperback/9780691101705/scientific-explanation-and-the-causal-structure-of-the-world); causal production
