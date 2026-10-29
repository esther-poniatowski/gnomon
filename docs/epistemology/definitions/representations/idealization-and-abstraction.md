---
tags:
  - definition
  - wip
index: "[Representations](docs/epistemology/definitions/representations/_index.md)"
aliases:
  - Idealization and abstraction
  - Idealization
  - Abstraction
---
# Idealization and abstraction

> [!QUESTION] Goal: does a simplifying assumption omit a fact about the target, or assert a falsehood about the target?

A model departs from its target in two ways. An **abstraction** omits factors of the target and asserts no falsehood about the factors kept. An **idealization** asserts a falsehood about the target, on purpose, to make the model tractable or to isolate a factor [jones2005] [cartwright1989].

## Senses

| Term | Definition | Example | Source |
| --- | --- | --- | --- |
| Abstraction | omission of factors: the model is true of the target but partial | a rate model silent about dendritic geometry | [jones2005]; [cartwright1989] |
| Idealization | deliberate distortion: the model ascribes to the target a feature absent from the target | an infinite number of neurons; a frictionless plane | [mcmullin1985]; [weisberg2007] |

Idealizations divide into three kinds by the justification given to each [weisberg2007]:

| Kind | Justification | Fate of the distortion | Example |
| --- | --- | --- | --- |
| Galilean | tractability: the undistorted model cannot be analyzed | removed step by step, by de-idealization, as methods improve | a mean-field limit, later corrected for finite size |
| Minimalist | the model keeps only the factors that make a difference to the phenomenon | kept, since the omitted factors make no difference | the Ising model of a phase transition |
| Multiple-models | no single model serves all the aims of an inquiry, so several incompatible models are kept | kept, since each model serves one aim | several models of the climate, each tuned to one variable |

## Distinctions

- **Abstraction and idealization are told apart by truth.** The test is whether the model, read as a description of the target, asserts a falsehood. Omitting a factor asserts nothing about that factor. Setting a factor to a value not taken by the target, such as zero friction, asserts a falsehood. ^truth-test
- **An omission becomes a distortion when the model is read as complete.** A model without adaptation is an abstraction when it is read as silent about adaptation. The same model is an idealization when its predictions are read as those of the full system, since the model then asserts that adaptation is absent.

## Consequences for a record

- **A candidate answer records its abstractions apart from its idealizations.** The element Abstractions of an [answer](../../answer-form.md#^answer-elements) makes the [truth test](#^truth-test) operative: the answer asserts nothing about a factor listed among its abstractions, whereas an omission read as complete is a distortion and belongs to the idealizations.
- **An idealization is relative to a target, and names its motive.** An assumption distorts only a target that lacks the assumed feature: the mean-field limit distorts a network of finite size, and is exact of the limit system. Therefore, the [model](../../model-and-binding.md#^model-elements) declares the assumptions that its laws require, and an answer classifies each of them relative to its target, as the [idealizations of an answer](../../answer-form.md#^idealizations) state. Each idealization carries one of three motives, tractability, isolation or limit, and a degree of removability.

**The motives of an idealization and its kinds classify on different axes.** The motive names the purpose of an assumption in the derivation, whereas the kind states how the distortion is justified. On a correspondence proposed by this method, the motives map onto kinds as follows:

| Motive | Kind of idealization | Distortion |
| --- | --- | --- |
| tractability | Galilean | the distortion is introduced because the undistorted model resists analysis, and de-idealization removes it |
| isolation | minimalist | an omission read as complete: the omitted factors are claimed to make no difference to the phenomenon |
| limit | asymptotic, a kind outside the three kinds classified by justification [weisberg2007] | the behavior of a limit system stands in for that of finite systems; the idealization is `controlled` when a finite-size correction is known, and it is then also Galilean |

A multiple-models idealization keeps several incompatible models of one target. A model is a [record of its own](../../model-and-binding.md#^model-record), so each such model grounds the answers of the aim that it serves. When several of these models ground one claim, they form a [family of models](../../model-and-binding.md#^model-family), each member with its own binding, and the robustness test asks whether the claim holds across the members.

- **One limit is a restriction of the domain or an idealization, depending on the question.** When the reference class of the question is the limit system itself, the limit distorts nothing about the target, so it restricts the domain. Otherwise, the behavior of the limit system stands in for that of finite systems, so the limit is an idealization with the motive `limit`. *Example*: a question about the kernel regime of infinitely wide networks concerns the limit system. A question about finite networks, answered through the infinite-width kernel, idealizes them by the same limit, which is `controlled` when the finite-width corrections are known. The place of each case in the records is fixed by the [domain of conditions](../../domain.md) and by the [rule on limits](../../answer-form.md#^limit-rule). ^limit-rule
- **An assumption of the analysis is not a condition of the question.** The [analysis assumptions](../../domain.md#^analysis-assumptions) are introduced after the question is fixed, so they belong to the grounds of the answer, or to the model whose laws require them.

---
## Sources

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [cartwright1989] ◐ [Cartwright, *Nature's Capacities and Their Measurement*, Clarendon Press, 1989](https://doi.org/10.1093/0198235070.001.0001)
- [jones2005] ◐ [Jones, "Idealization and abstraction: a framework", in Jones & Cartwright (eds.), *Idealization XII: Correcting the Model. Idealization and Abstraction in the Sciences*, Poznań Studies in the Philosophy of the Sciences and the Humanities 86, Rodopi, 173–217, 2005](https://philportal.de/records/kug/EBP9789401202732)
- [mcmullin1985] ◐ [McMullin, "Galilean idealization", *Studies in History and Philosophy of Science* 16(3), 247–273, 1985](https://doi.org/10.1016/0039-3681(85)90003-2)
- [weisberg2007] ◐ [Weisberg, "Three kinds of idealization", *Journal of Philosophy* 104(12), 639–659, 2007](https://doi.org/10.5840/jphil20071041240)
