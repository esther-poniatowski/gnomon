---
tags:
  - definition
  - wip
index: "[Representations](docs/epistemology/definitions/representations/_index.md)"
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

## Senses

| Term | Community | Definition | Source |
| --- | --- | --- | --- |
| Claim | logic, epistemology | a proposition put forward for evaluation, supportable or refutable by evidence or by proof | — |
| Hypothesis | general usage | a claim held provisionally, while it is tested | — |
| Theoretical hypothesis | semantic view of theories | the claim that a model is similar to a target system in specified respects and to specified degrees | [giere1988] |
| Empirical claim | structuralist view of theories | the claim that the intended applications of a theory-element can be completed into its actual models | [balzer1987] |
| Prediction | philosophy of science | a claim about the values of observables not yet observed, derived from a model and conditions | [hempel1948] |
| Explanation | philosophy of science | a pair of an explanans and an explanandum, in which the explanans bears to the explanandum a relation that counts as explanatory: deductive subsumption, causal production, or another | [hempel1948]; [salmon1984] |

The relations that count as explanatory are compared in the [specification of the requested relation](../../requested-relation.md). This note does not restate that comparison.

## Distinctions

Three kinds of expression are often confused. Each kind adds properties to the kind listed before:

| Expression | Has a truth value? | General? | Supports counterfactuals and holds over a range of interventions? | Example |
| --- | --- | --- | --- | --- |
| [Predicate](../systems/property-attribute-predicate.md) | no | — | — | "$x$ oscillates at frequency $f$" |
| Claim | yes | not necessarily | not necessarily | "this network oscillates at 40 Hz" |
| [Law statement](../regularities/law.md) | yes | yes | yes | "the frequency of the oscillation is inversely proportional to the inhibitory time constant" |

The attitude and the support of a claim take values in two closed lists: ^attitude-support

| Attribute | Content | Values |
| --- | --- | --- |
| Attitude | the stance of the inquiry toward the claim | `entertained`, `hypothesized`, `accepted`, `retracted` |
| Support | the grounds of the claim, independent of the attitude | `unsupported`, `informal`, `formally-proven`, `empirically-supported` |

- **A hypothesis and an accepted claim differ by attitude only.** Their content can be identical: the same proposition is hypothesized while it is tested, and accepted once a revision of the belief base admits it, as the [acceptance of an answer](../../epistemic-aim.md#^acceptance) states.
- **The attitude and the support vary independently.** *Examples*: a claim can be hypothesized with informal support, or accepted with no more than informal support. A formally proven claim can be retracted when its assumptions turn out to be false of the target.
- **An explanation, as a product, is a claim.** Its content is that the explanans $E$ explains the phenomenon $P$ under the requested relation $R$. Therefore, the explanation carries an attitude and a support, as any claim does. The activity of explaining is typed in the [taxonomy of epistemic activities](../activities/epistemic-activities.md).
- **A prediction and an explanation can share their logical form.** In the deductive-nomological model, both derive the explanandum from laws and conditions. The two differ in the epistemic status of the explanandum, already known or not yet known [hempel1948]. Accounts that require a causal relation separate the two, since a prediction may rest on a symptom that does not cause the predicted event [salmon1984].

## Consequences for a record

- **A candidate answer records the attitude and the support of its claim.** The fields are specified under the [status and support of an answer](../../answer-form.md#^status-and-support), with the values of the [two lists](#^attitude-support). Therefore, an answer whose attitude is `hypothesized` is a hypothesis.
- **The laws on which a candidate answer rests are claims, each with a warrant of its own.** The [warrant of a law](../../background.md#^law-warrant) traces the law to its origin, so it differs from the support of the claim of an answer.
- **The conditions of satisfaction fix the tests of the claims before evaluation.** Before any answer is assessed, the [conditions of satisfaction](../../satisfaction-conditions.md) state the tests deciding whether its claims hold.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [balzer1987] ◐ [Balzer, Moulines & Sneed, *An Architectonic for Science: The Structuralist Program*, Reidel, 1987](https://doi.org/10.1007/978-94-009-3765-9)
- [giere1988] ◐ [Giere, *Explaining Science: A Cognitive Approach*, University of Chicago Press, 1988](https://press.uchicago.edu/ucp/books/book/chicago/E/bo3622319.html); p. 81, checked through secondary sources
- [hempel1948] ◐ [Hempel & Oppenheim, "Studies in the logic of explanation", *Philosophy of Science* 15(2), 135–175, 1948](https://doi.org/10.1086/286983)
- [salmon1984] ◐ [Salmon, *Scientific Explanation and the Causal Structure of the World*, Princeton University Press, 1984](https://press.princeton.edu/books/paperback/9780691101705/scientific-explanation-and-the-causal-structure-of-the-world)
