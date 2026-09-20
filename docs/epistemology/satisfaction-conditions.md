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

This [layer of inquiry](inquiry-specification.md) derives the tests that a candidate answer must pass from the [subject of inquiry](subject-of-inquiry.md) and the [epistemic task](epistemic-task.md). The [form of the answer](answer-form.md) fixes what the tests apply to.

A candidate answer is evaluated at several levels. The verdict of each test, and the assessment of the answer on each virtue, are recorded apart from the answer itself, one record per candidate assessed, so that a candidate can be restated without touching its assessment: ^conditions-satisfaction

1. **admissibility**: is the candidate an *actual* answer to the question?
2. **warrant**: is the answer established by the *route* that the specification implies?
3. **appraisal** (adequacy): how well does an answer that passed serve the virtues the question selected, and which of several such answers is then preferred?

The first two levels *filter* the answers that *satisfy* the research question:
$$\mathrm{Sat}(M\mid Q)=\mathrm{Admissible}(M\mid Q)\wedge\mathrm{Warranted}(M\mid Q)$$
The third level *appraises* only the answers that already pass, one at a time.

Each test is derived from filled specifications, so an empty specification removes its test. 

> [!WARNING] Redundancy
> Most criteria merely *check* whether the answer complies with the specifications of the previous layers, or combinations of them.

## Admissibility

| Criterion      | Test                                                                                                                                                                                                                                                                                                                                                                           | Source                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Scope          | - the claim ranges over the [*reference class* of the system](target-system.md) $S$, restricted by the [*domain*](domain.md) $D$, with the [*scope over instances*](phenomenon.md) stated for the phenomenon $P$;<br>- laws stated over derived units hold across $D$ the domain, rather than case by case                                                                     | target population [lundberg2021]                                                         |
| Grain          | - the answer fixes the [*explanandum variable*](phenomenon.md) at the stated grain: its *value scale*, its *aggregation over parts* and its *profile*; <br>- the explanandum variable stays definable over the units that the answer uses                                                                                                                                      | proportionality [woodward2010]                                                           |
| Contrast       | the explanans favors the [*fact over each foil*](contrast.md): it cites a factor present in the case of the fact and absent in the case of the foil                                                                                                                                                                                                                            | favoring the topic [vanfraassen1980]; difference condition [lipton2004]                  |
| Relation       | the link between the explanans and the explanandum has the [*requested kind*](requested-relation.md) (e.g. a dependence invariant under interventions for a causal relation, mutual manipulability for a constitutive relation, a proof for a mathematical relation)                                                                                                           | [woodward2003]; [craver2007]                                                             |
| Individuation  | - every [constituent that the answer treats as a bearer](answer-form.md#^perspective) is declared for the system or carries a stated map from the declared constituents; <br>- the re-individuated model agrees with the declared one, on the interventions that both represent for a causal, mechanistic or constitutive relation, and on the derivations for a formal target | decomposition as a revisable strategy [bechtel1993]; causal consistency [rubenstein2017] |
| Level          | every explanans *term* is declared, or derived by a stated map, at the [*admitted level*](explanans-level.md); every aggregate has unambiguous intervention effects                                                                                                                                                                                                            | [spirtes2004]                                                                            |
| Modal-strength | the answer has the requested *[modal-strength](modal-strength.md)*: either realized in the system $S$ (actual), consistent with the laws of the system within the domain $D$ (possible), or excluding every foil under those laws (necessary)                                                                                                                              | [epistemic task](epistemic-task.md)                                                      |
| Product        | the answer delivers the [product of the *epistemic aim*](epistemic-aim.md), together with the [virtues that this aim forces to select](epistemic-pragmatic-virtues.md#^entailed-virtues)                                                         | intelligibility criterion [deregt2005]                                                   |

## Warrant

| Criterion              | Test                                                                                                                                                                                                      | Research action                                                                                                                     | Source                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Phenomenon established | the [phenomenon](phenomenon.md) is established before it is explained (depending on the *evidential status*)                                                                                              | detect or replicate the phenomenon first, when its status is "reported" or "predicted"                                              | [bogen1988]; presupposition of the topic [vanfraassen1980] |
| Foil evidence          | the evidence for the [contrast](contrast.md) comes from the case of the foil (*foil status*)                                                                                                              | observed foil: compare the recorded cases; counterfactual foil: produce the foil by an intervention or a simulation                 | [lipton2004]                                               |
| Closure                | the derivation or the test matches the [*closure of the laws* of the system](target-system.md)                                                                                                  | formal target: derive from the laws, by proof or by simulating their consequences; empirical target: measure or intervene | —                                                          |
| Fidelity               | the model matches the [target system](target-system.md) within stated [tolerances](epistemic-task.md): which outputs must match which observables, to what accuracy, and which structures must correspond | check the candidate against the [required accuracy](epistemic-task.md) fixed with the task                                          | fidelity criteria [weisberg2013]                           |
| Robustness             | the conclusion survives the [*idealizations*](answer-form.md#^answer-elements) $I$ of the analysis                                                                                                        | relax each idealization, or compare models that share the claimed structure                                                         | robustness analysis [weisberg2006]                         |
| Selection              | a claim about selected members extends to the full class only after a check for selection bias (depending on the [selection criteria of the reference class](target-system.md))                           | when a criterion depends on an outcome, test the association in the full class                                                      | [hernan2004]                                               |

*Example* of tests applied to the gamma-oscillation answer, two of admissibility and one of warrant:

- contrast (admissibility): the asynchronous state must be produced, for instance by removing the synaptic delay in the model, since the foil never occurred in the network (counterfactual foil);
- level (admissibility): the test passes when the stated level is population rates, since the explanans uses only population variables;
- robustness (warrant): the conclusion must hold at finite network size, since the mean-field limit is an idealization of the analysis.

## Appraisal

The [epistemic and pragmatic virtues](epistemic-pragmatic-virtues.md) appraise an answer that passed both tiers. A virtue never compensates a failed test (e.g. an economical answer that ignores the foil is still inadmissible).

> [!NOTE] Appraisal records ^appraisal-record
> Appraisal adds no test of its own: its criteria are the virtues that the question selected or that its [aim forced](epistemic-pragmatic-virtues.md#^entailed-virtues), and each virtue already carries its operational question. What appraisal adds is a record, filled for one answer at a time.

| Virtue selected | Assessment of this answer                                            | Preferred over                                            |
| --------------- | -------------------------------------------------------------------- | --------------------------------------------------------- |
| [virtue]        | [what the operational question of that virtue returns for this answer] | [the candidates it beats on that virtue, or none assessed] |

- **An answer is appraised on its own.** The assessment states what each selected virtue returns for this answer, so a lone candidate is appraised as fully as one of several. A comparison is recorded only once another candidate has been appraised, and it then reads off the assessments already filled.

- **Only the selected virtues are appraised.** A virtue that the question did not select does not bear on the answer, since the inquiry did not commit to that virtue. The [aim itself selects some virtues](epistemic-pragmatic-virtues.md#^entailed-virtues), which the product test then applies.

- **No aggregate score without stated weights.** Virtues conflict, as generality does with precision [matthewson2009]. Without weights fixed in advance, the record keeps one assessment per virtue, and the trade-off stays visible instead of disappearing into a single number.

## Recording an assessment

The verdicts and the appraisal are held apart from the answer, one record per candidate assessed. The record points at what it assesses and at the question that fixes the tests, so that a candidate can be restated, or a second candidate added, without rewriting anything already settled. ^assessment-record

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Assesses — the candidate whose verdicts this record holds | always | the identifier of one [candidate answer](answer-form.md) | the answer by inhibitory delay | — |
| Against — the question that fixes which tests apply | always | the identifier of one question | why the network is synchronous rather than asynchronous | [each test comes from a filled specification](#^conditions-satisfaction) |
| Tests: admissibility | always | per criterion of the admissibility table, a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | contrast: pass, by producing the asynchronous state in a simulation; level: not-applicable, since the question left the level open | [admissibility](#^conditions-satisfaction) |
| Tests: warrant | always | per criterion of the warrant table, a verdict with the evidence that settles it | robustness: fail, since the conclusion did not survive at finite network size | [warrant](#^conditions-satisfaction) |
| Appraisal | when the question selected a virtue, or when its [aim forced one](epistemic-pragmatic-virtues.md#^entailed-virtues) | per virtue, the assessment of this answer, and the candidates it is preferred over once those have been assessed | intelligibility: the oscillation frequency can be read off the delay, without simulating the network | [appraisal records](#^appraisal-record) |

- **A verdict of not-applicable is a result, not a gap.** An empty specification in the question removes its test, so the record states that the test does not apply rather than leaving it pending, and a reader can tell an untested candidate from a fully assessed one.

---
## Sources

> [!NOTE] What is established
> - **Established:** the principle behind each test, as cited.
> - **Proposals:** deriving one test from each filled specification; the three tiers and their order; requiring a stated map and a consistency check whenever the answer re-individuates the system, and folding the tests of a re-individuation into the criteria that already apply rather than adding a tier; recording one assessment per selected virtue, for one answer at a time, instead of a single score.

Marks: ✓ the text itself was read · ◐ checked through an abstract, the publisher page or a secondary summary · ○ cited from standard knowledge, not fetched in this session.

- [bechtel1993] ◐ [Bechtel & Richardson, _Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research_, Princeton UP 1993; MIT Press 2010](https://direct.mit.edu/books/monograph/2860/Discovering-ComplexityDecomposition-and)
- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", _Philosophical Review_ 97(3), 1988
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [hernan2004] ◐ [Hernán, Hernández-Díaz & Robins, "A structural approach to selection bias", _Epidemiology_ 15(5), 2004](https://pubmed.ncbi.nlm.nih.gov/15308962/)
- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [matthewson2009] ◐ [Matthewson & Weisberg, "The structure of tradeoffs in model building", _Synthese_ 170, 2009](https://link.springer.com/article/10.1007/s11229-008-9366-y)
- [rubenstein2017] ◐ [Rubenstein et al., "Causal consistency of structural equation models", *UAI*, 2017](https://www.auai.org/uai2017/proceedings/papers/11.pdf)
- [spirtes2004] ✓ [Spirtes & Scheines, "Causal inference of ambiguous manipulations", *Philosophy of Science* 71(5), 2004](https://philpapers.org/rec/SPICIO)
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", _Philosophy of Science_ 73(5), 2006](https://philpapers.org/rec/MICRA)
- [weisberg2013] ◐ [Weisberg, _Simulation and Similarity_, OUP, 2013](https://academic.oup.com/book/3141/chapter/143989335)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
