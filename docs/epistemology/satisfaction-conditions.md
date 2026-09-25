---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the conditions of satisfaction
  - Conditions of satisfaction
tags: []
source:
---
# Specifying the conditions of satisfaction

> [!QUESTION] Goal: which tests must a candidate answer pass, given the specified subject and task?

The tests that a candidate answer must pass are derived from the [subject](subject-of-inquiry.md) and the [epistemic task](epistemic-task.md) of the inquiry, and form one [layer of its specification](inquiry-specification.md). The [form of the answer](answer-form.md) fixes the object to which those tests apply.

A candidate answer is evaluated at three levels: ^conditions-satisfaction

1. **admissibility**: is the candidate an *actual* answer to the question?
2. **warrant**: is the answer established by the *route* that the specification implies?
3. **appraisal** (adequacy): how well does an answer that passed serve the virtues that the question selected, and which of several such answers is then preferred?

The first two levels *filter* the answers that *satisfy* the research question:
$$\mathrm{Sat}(M\mid Q)=\mathrm{Admissible}(M\mid Q)\wedge\mathrm{Warranted}(M\mid Q)$$
The third level, by contrast, *appraises* only the answers that already pass, one at a time.

Each test derives from a filled specification, so an empty specification removes its test.

> [!WARNING] Redundancy
> Most criteria merely *check* whether the answer complies with the specifications of the previous layers, taken singly or in combination.

## Admissibility

| Criterion      | Test                                                                                                                                                                                                                                                                                                                                                                           | Source                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Scope          | - the claim ranges over the [*reference class* of the system](target-system.md) $S$, restricted by the [*domain*](domain.md) $D$, with the *quantification* that each declared [source of variation across instances](phenomenon.md) carries;<br>- laws stated over derived units hold across the *whole* domain $D$                                                                     | target population [lundberg2021]                                                         |
| Grain          | - the answer specifies the [*explanandum variable*](phenomenon.md) at the stated grain: its *value set*, the indices that its *signature* retains, and the *expression* or *condition* that fixes it; <br>- the explanandum variable stays definable over the units that the answer uses                                                                                                                                      | proportionality [woodward2010]                                                           |
| Contrast       | the explanans favors the [*fact over each foil*](contrast.md). For each foil that the question names, some factor *separates* the two, by citing a condition present for the fact and absent for that foil                                                                                                                                                                                                                            | favoring the topic [vanfraassen1980]; difference condition [lipton2004]                  |
| Relation       | - the link between the explanans and the explanandum has the [*requested kind*](requested-relation.md) (e.g. invariance under interventions if causal, mutual manipulability if constitutive, a proof if mathematical);<br>- each factor reaches the effect that it *produces* through the laws and relations that it names                                                                                                           | [woodward2003]; [craver2007]                                                             |
| Individuation  | - every constituent that the answer treats as a [bearer](answer-form.md#^perspective) either *references* a constituent that the system declares or carries its own *expression*; <br>- the re-individuated model agrees with the declared one on the interventions that both represent, for a causal, mechanistic or constitutive relation, and on the derivations, for a formal target | decomposition as a revisable strategy [bechtel1993]; causal consistency [rubenstein2017] |
| Admissible explanans | every *variable* and *parameter* of the answer either *references* a quantity that the system declares or carries its own *expression*, and lies within the [*admissible explanans*](admissible-explanans.md). Every intervention on an aggregate also has an unambiguous effect                                                                                                                                                                                                            | [spirtes2004]                                                                            |
| Modal strength | the answer has the requested *[modal strength](modal-strength.md)*: realized in $S$ (actual), consistent with the laws of $S$ within $D$ (possible), or excluding every foil under those laws (necessary)                                                                                                                              | [epistemic task](epistemic-task.md)                                                      |
| Product        | - the answer delivers the [product of the *epistemic aim*](epistemic-aim.md);<br>- the inquiry fixes every specification [that aim requires](epistemic-aim.md#^required-by-aim);<br>- the answer holds every virtue that the question marks [constitutive](epistemic-pragmatic-virtues.md#^virtue-standing)                                                         | intelligibility criterion [deregt2005]                                                   |

## Warrant

| Criterion              | Test                                                                                                                                                                                                      | Research action                                                                                                                     | Source                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Phenomenon established | the [phenomenon](phenomenon.md) is established before it is explained (depending on the *evidential status*)                                                                                              | detect or replicate the phenomenon first, when its status is "reported" or "predicted"                                              | [bogen1988]; presupposition of the topic [vanfraassen1980] |
| Foil evidence          | the evidence for the [contrast](contrast.md) comes from the case of the foil (*foil status*)                                                                                                              | - observed foil: compare the recorded cases;<br>- counterfactual foil: produce the foil by an intervention or a simulation                 | [lipton2004]                                               |
| Law warrant            | each law of the answer holds on the [*warrant*](target-system.md#^law-warrant) that it claims. A law marked `derived` is derivable from the laws on which it rests. A law marked `fitted` or `measured` names its source data | check each law of the answer against the grounds of its warrant, because a conclusion inherits the weakest warrant among the laws that it uses | [nagel1961] |
| Closure                | the derivation or the test matches the [*closure of the laws*](target-system.md) of the system                                                                                                  | - formal target: derive from the laws, by proof or by simulating their consequences;<br>- empirical target: measure or intervene | —                                                          |
| Fidelity               | the model matches the [target system](target-system.md) within stated [tolerances](epistemic-task.md). The tolerances name the outputs that must match each observable, the required accuracy, and the structures that must correspond | check the candidate against the [required accuracy](epistemic-task.md) fixed with the task                                          | fidelity criteria [weisberg2013]                           |
| Robustness             | the conclusion survives the [*idealizations*](answer-form.md#^answer-elements) $I$ of the analysis                                                                                                        | relax each idealization, or compare models that share the claimed structure                                                         | robustness analysis [weisberg2006]                         |
| Selection              | a claim about a subset of members extends to the full class only after a check for selection bias. That bias can arise exactly where the class is [selected on an outcome](target-system.md#^selection-on-outcome)                           | when a criterion depends on an outcome, test the association in the full class                                                      | [hernan2004]                                               |

*Example* of tests applied to the answer about gamma oscillations, two of admissibility and one of warrant:

- contrast (admissibility): the asynchronous state must be produced, for instance by removing the synaptic delay in the model, since the foil never occurred in the network (counterfactual foil);
- admissible explanans (admissibility): the test passes when the question bounds the explanans to population rates, since the explanans uses no other variable;
- robustness (warrant): the conclusion must hold at finite network size, since the mean-field limit is an idealization of the analysis.

## Appraisal

The [epistemic and pragmatic virtues](epistemic-pragmatic-virtues.md) appraise an answer that passed both tiers. A virtue therefore never compensates for a failed test (e.g. an economical answer that ignores the foil is still inadmissible).

> [!NOTE] Appraisal records ^appraisal-record
> Appraisal adds no test of its own. Its criteria are the virtues marked [preferred](epistemic-pragmatic-virtues.md#^virtue-standing) by the question, and each of them already carries its operational question. Appraisal therefore adds only a record, filled for one answer at a time.

| Virtue selected | Assessment of this answer                                            | Preferred over                                            |
| --------------- | -------------------------------------------------------------------- | --------------------------------------------------------- |
| [virtue]        | [the result that the operational question of that virtue returns for this answer] | [the candidates that it beats on that virtue, or none assessed] |

- **An answer is appraised on its own.** The assessment states the result that each selected virtue returns for the answer, so a lone candidate is appraised as fully as one of several. A comparison is recorded only once another candidate has been appraised. The comparison is then drawn from the assessments already filled.

- **Only the virtues marked preferred are appraised.** The question commits the inquiry only to the virtues that it selects, so an unselected virtue does not bear on the answer. A virtue that the question marks [constitutive](epistemic-pragmatic-virtues.md#^virtue-standing) is settled by the product test instead. An answer that lacks a constitutive virtue is inadmissible, so appraisal does not assess that virtue a second time.

- **No aggregate score without stated weights.** Virtues conflict with one another, for instance generality with precision [matthewson2009]. A single score computed without weights fixed in advance conceals this trade-off, so the record keeps one assessment per virtue.

## Recording an assessment

The verdicts of the tests and the appraisal are kept outside the answer, in one record per candidate assessed. The record references the candidate that it assesses and the question that fixes the tests. A candidate can then be restated, or a second one added, without rewriting a verdict or an assessment already settled. ^assessment-record

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Answer — the candidate whose verdicts this record holds | always | the identifier of one [candidate answer](answer-form.md) | the answer by inhibitory delay | — |
| Question — the record whose specifications fix which tests apply | always | the identifier of one question | why the network is synchronous rather than asynchronous | [tests drawn from filled specifications](#^conditions-satisfaction) |
| Tests: admissibility | always | per criterion of the admissibility table, a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | contrast: pass, by producing the asynchronous state in a simulation; admissible explanans: not-applicable, since the question bounded the answer to no variables | the [admissibility level](#^conditions-satisfaction) |
| Tests: warrant | always | per criterion of the warrant table, a verdict with the evidence that settles it | robustness: fail, since the conclusion did not survive at finite network size | the [warrant level](#^conditions-satisfaction) |
| Obligations | when the question states a proof obligation | per obligation, a verdict with the derivation or the counterexample that settles it | the necessary direction: pass, by the derivation of Lemma 2; the sufficient direction: fail, by a counterexample | — |
| Appraisal | when the question marks a virtue [preferred](epistemic-pragmatic-virtues.md#^virtue-standing) | per virtue, the assessment of this answer, and the candidates over which it is preferred once they have been appraised | intelligibility: the oscillation frequency can be read off the delay, without simulating the network | the [appraisal record](#^appraisal-record) |

- **A verdict of `not-applicable` is a *result*.** The record marks a test removed by an empty specification as `not-applicable`, instead of leaving it pending. A reader can then tell an untested candidate from a fully assessed one.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the principle behind each test, as cited.
> - **Proposals:**
> 	- deriving one test from each filled specification;
> 	- the three tiers and their order;
> 	- requiring a stated map and a consistency check whenever the answer re-individuates the system;
> 	- testing a re-individuation with the existing criteria alone;
> 	- recording one assessment per selected virtue, for one answer at a time, instead of a single score.

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [bechtel1993] ◐ [Bechtel & Richardson, _Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research_, Princeton UP 1993; MIT Press 2010](https://direct.mit.edu/books/monograph/2860/Discovering-ComplexityDecomposition-and)
- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", _Philosophical Review_ 97(3), 1988
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [hernan2004] ◐ [Hernán, Hernández-Díaz & Robins, "A structural approach to selection bias", _Epidemiology_ 15(5), 2004](https://pubmed.ncbi.nlm.nih.gov/15308962/)
- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [matthewson2009] ◐ [Matthewson & Weisberg, "The structure of tradeoffs in model building", _Synthese_ 170, 2009](https://link.springer.com/article/10.1007/s11229-008-9366-y)
- [nagel1961] ◐ Nagel, _The Structure of Science_, Harcourt, Brace & World, 1961, bridge laws, via [SEP, Scientific Reduction](https://plato.stanford.edu/entries/scientific-reduction/)
- [rubenstein2017] ◐ [Rubenstein et al., "Causal consistency of structural equation models", *UAI*, 2017](https://www.auai.org/uai2017/proceedings/papers/11.pdf)
- [spirtes2004] ✓ [Spirtes & Scheines, "Causal inference of ambiguous manipulations", *Philosophy of Science* 71(5), 2004](https://philpapers.org/rec/SPICIO)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", _Philosophy of Science_ 73(5), 2006](https://philpapers.org/rec/MICRA)
- [weisberg2013] ◐ [Weisberg, _Simulation and Similarity_, OUP, 2013](https://academic.oup.com/book/3141/chapter/143989335)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
