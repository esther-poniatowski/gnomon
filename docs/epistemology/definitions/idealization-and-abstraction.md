---
role: definition
status: wip
index: "[Definitions](docs/epistemology/definitions/_index.md)"
aliases:
  - Idealization and abstraction
  - Idealization
  - Abstraction
tags: []
source:
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

- **A candidate answer records its abstractions apart from its idealizations.** The block `abstractions` of an [answer](../answer-form.md) lists the factors left out by the answer, each with the reason why the answer makes no claim about it. The block makes the [truth test](#^truth-test) operative: the answer asserts nothing about a factor listed among its abstractions, whereas an omission read as complete is a distortion and belongs to the idealizations.
- **Each idealization of an answer names its motive.** The [idealizations of an answer](../answer-form.md#^idealizations) carry one of three motives: tractability, isolation or limit. Each also states whether it is `removable`: `controlled` when a correction to the idealized result is known, `ineliminable` when the model cannot be stated without it, and `unknown` otherwise.

**The motives of an answer and the kinds of idealization classify on different axes.** The motive names the purpose of an assumption in the derivation, whereas the kind states how the distortion is justified. On a correspondence proposed by this method, the motives map onto kinds as follows:

| Motive | Kind of idealization | Distortion |
| --- | --- | --- |
| tractability | Galilean | the distortion is introduced because the undistorted model resists analysis, and de-idealization removes it |
| isolation | minimalist | an omission read as complete: the omitted factors are claimed to make no difference to the phenomenon |
| limit | asymptotic, a kind outside the three kinds classified by justification [weisberg2007] | the behavior of a limit system stands in for that of finite systems; the idealization is `controlled` when a finite-size correction is known, and it is then also Galilean |

Multiple-models idealization concerns a set of answers, and no single record holds such a set.

- **One rule decides where a limit is recorded.** When the reference class of the question is the limit system itself, the limit is a restriction of the domain, recorded in `question.subject.domain.limit` of the [domain of conditions](../domain.md). Otherwise, the limit is an idealization of the answer, with the motive `limit` and a value of `removable`. *Example*: a question about the kernel regime of infinitely wide networks records the infinite width in its domain. A question about finite networks, answered through the infinite-width kernel, records the same limit as an idealization, `controlled` when the finite-width corrections are known. ^limit-rule
- **An assumption of the analysis is not a condition of the question.** The [analysis assumptions](../domain.md#^analysis-assumptions) are introduced after the question is fixed, so they belong to the answer.

---
## Sources

Marks follow the [legend of reading marks](../../../CONTRIBUTING.md#^reading-marks).

- [cartwright1989] ◐ [Cartwright, *Nature's Capacities and Their Measurement*, Clarendon Press, 1989](https://doi.org/10.1093/0198235070.001.0001)
- [jones2005] ◐ [Jones, "Idealization and abstraction: a framework", in Jones & Cartwright (eds.), *Idealization XII: Correcting the Model. Idealization and Abstraction in the Sciences*, Poznań Studies in the Philosophy of the Sciences and the Humanities 86, Rodopi, 173–217, 2005](https://philportal.de/records/kug/EBP9789401202732)
- [mcmullin1985] ◐ [McMullin, "Galilean idealization", *Studies in History and Philosophy of Science* 16(3), 247–273, 1985](https://doi.org/10.1016/0039-3681(85)90003-2)
- [weisberg2007] ◐ [Weisberg, "Three kinds of idealization", *Journal of Philosophy* 104(12), 639–659, 2007](https://doi.org/10.5840/jphil20071041240)
