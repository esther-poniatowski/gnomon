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

The tests that a candidate answer must pass are derived from the [subject](subject-of-inquiry.md) and the [epistemic task](epistemic-task.md) of the inquiry, and form one [layer of its specification](inquiry-specification.md). The [form of the answer](answer-form.md) fixes the object to which those tests apply: one typed claim, with its core and the block of the aim of its question. Some tests also read the records on which the answer rests: its [model, its binding and the computed comparison](model-and-binding.md), and the [phenomenon](phenomenon.md) of the question.

A candidate answer is evaluated at three levels: ^conditions-satisfaction

1. **admissibility**: is the candidate an *actual* answer to the question?
2. **warrant**: is the answer established by the *route* that the specification implies?
3. **appraisal** (adequacy): how well does an answer that passed serve the virtues that the question selected, and which of several such answers is then preferred?

The first two levels *filter* the answers that *satisfy* the research question. For a candidate answer $h$ to a question $Q$, a member of the set $H$ of [proposed candidates](definitions/inquiry/epistemic-problem.md#^candidates):
$$\mathrm{Sat}(h\mid Q)=\mathrm{Admissible}(h\mid Q)\wedge\mathrm{Warranted}(h\mid Q)$$
The third level, by contrast, *appraises* only the answers that already pass, one at a time.

The **disposition** of an assessment follows from its verdicts at the first two levels. The disposition is `not-satisfied` when one test fails, `withheld` when no test fails and one is pending, and `satisfied` when every test passes or does not apply. For a [corrective answer](#^erotetic-routing), the disposition that would be `satisfied` is `corrective` instead: the answer does not satisfy its question, and shows instead that the question has no true direct answer. The disposition is read from the verdicts and from the erotetic relation of the answer, not recorded beside them, so the record cannot disagree with them. ^disposition

Each test derives from a filled specification, so an empty specification removes its test, whose verdict is then `not-applicable`. A specification left open on purpose, with the maturity `open`, differs from an empty one: it is still to be fixed, so its test stays `pending` until the specification is narrowed.

> [!WARNING] Redundancy
> Most criteria merely *check* whether the answer complies with the specifications of the previous layers, taken singly or in combination.

## Admissibility

The admissibility tests check the *form* of a candidate. Every answer passes the tests of the core. An answer passes, in addition, the tests of the block of the aim of its question, and the tests of the blocks of other aims do not apply to it. ^admissibility-per-block

### Tests of the core

| Criterion      | Test                                                                                                                                                                                                                                                                                                                                                                           | Source                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Product        | - for a complete answer, the claim is a direct answer of the type that the full atomic question fixes: it meets the [answer conditions](epistemic-aim.md#^answer-conditions) of the aim, and the answer holds the block of that aim; for a partial answer, the claim narrows the direct answers of that type, and the block holds the part of the request that the claim settles;<br>- the inquiry fixes every specification [that aim requires](epistemic-aim.md#^required-by-aim);<br>- the answer holds every virtue that the question marks [constitutive](epistemic-pragmatic-virtues.md#^virtue-standing) | question fixed by its answers [hamblin1958]; intelligibility criterion [deregt2005] |
| Scope          | - the [domain of the claim](answer-form.md#^derived-domain) covers the [*reference class* of the system](target-system.md) $S$, restricted by the [*domain*](domain.md) $D$, with the *quantification* that each declared [source of variation across instances](phenomenon.md) carries;<br>- for a deductive route, the domain compared is the one derived from the grounds, not a stated one;<br>- when the claim bears on the target through a binding, the domain of comparison of the binding covers $D$, and each region of extrapolation is marked;<br>- laws stated over derived units hold across the *whole* domain $D$ | target population [lundberg2021] |
| Grain          | - the claim specifies the [*explanandum variable*](phenomenon.md) at the stated grain: its *value set*, the indices that its *signature* retains, and the *expression* or *condition* that fixes it; <br>- the explanandum variable stays definable over the units of the model on which the route runs | proportionality [woodward2010] |
| Individuation  | - each [bearer](model-and-binding.md#^perspective) of the model is declared in the [model record](model-and-binding.md#^model-elements): either as a unit defined by a stated map from the constituents that the system declares, or as a unit of the model alone, which bears on the target only through a binding; <br>- no quantity of the model enters by reference to a target quantity; <br>- the re-individuated model agrees with the declared one on the interventions that both represent, for a causal, mechanistic or constitutive relation, and on the derivations, for a formal target | decomposition as a revisable strategy [bechtel1993]; causal consistency [rubenstein2017] |
| Admissible explanans | every quantity on which the claim depends, through its grounds, its dependence or the factors of an explanatory block, lies within the [*admissible explanans*](admissible-explanans.md). Every intervention on an aggregate also has an unambiguous effect | [spirtes2004] |
| Binding        | - when the route runs on a model other than the target and the claim bears on the target, the answer cites one [binding](model-and-binding.md#^binding-record) of each model to the phenomenon of the question;<br>- an answer that [declares its use](answer-form.md#^declared-use) instead makes a claim on a model or on a formal class only: a claim of actual strength about an empirical target, a prediction or a description of a target fails this test without a binding | [suarez2004] |
| Modal strength | the answer claims the requested *[modal strength](modal-strength.md)*: realized in $S$ (actual), consistent with the laws of $S$ within $D$ (possible), or excluding every foil under those laws (necessary). Whether the claim holds is decided by the warrant tests, along the routes of evidence of each [modal strength](modal-strength.md): for an actual strength, closure, by measurement or intervention, and fidelity for an empirical target, computed through the binding, with selection when the claim extends from the members studied to their class, and closure and law warrant for a formal target, with fidelity when the derivation runs on a model of the target rather than on its laws; for a possible strength, closure and law warrant applied to the model that exhibits the phenomenon; for a necessary strength, closure and law warrant applied to the proof of impossibility or to the exhaustive exclusion | [epistemic task](epistemic-task.md) |

- **The erotetic relation routes the assessment.** The [erotetic relation](answer-form.md#^erotetic-relation) of an answer is a field, not a test, and it decides which tests apply: ^erotetic-routing
    - every test of the core and of the aim block applies to a complete or a partial answer. A partial answer that satisfies these tests still leaves its question open, since the answer is not conclusive;
    - a corrective answer holds no aim block, so the product test and the tests of the aim block are `not-applicable`. The warrant tests then judge the claim that the presupposition is false, and an accepted corrective answer refutes the soundness of the question;
    - a reformulating answer is assessed against the revised question that it names, so its assessment record references that question.

### Tests of the aim block

| Aim block | Criterion | Test | Source |
| --------- | --------- | ---- | ------ |
| `description` | Values | the block assigns a value, with its uncertainty, to every explanandum variable and feature that the request covers, at the grain of the question and per declared source of variation | [woodward2010] |
| `exploration` | Space | the block declares its space and its equivalence criterion, each marked as an input or an output, and every class that it reports meets the [detection criterion](phenomenon.md#^exploratory-phenomenon) of the phenomenon | [steinle1997] |
| `prediction` | Outputs | each predicted output is one of the outputs to match that the [required accuracy](epistemic-task.md) names, under a stated condition of the target, with its uncertainty | — |
| `explanation` | Contrast | the block favors the [*fact over each foil*](contrast.md). For each foil that the question names, some factor *separates* the two, by citing a condition present for the fact and absent for that foil | favoring the topic [vanfraassen1980]; difference condition [lipton2004] |
| `explanation` | Relation | - the dependence that the explanatory claim reads has the [*requested kind*](requested-relation.md) (e.g. invariance under interventions if causal, mutual manipulability if constitutive, a proof if mathematical);<br>- each factor reaches the effect that it *produces* through the laws and relations that it names | [woodward2003]; [craver2007] |
| `explanation` | Target status | - each factor declares a [target status](answer-form.md#^target-status);<br>- when the route runs on a model, the binding holds the feature pair that the status requires, and a limit construct cites among its grounds, with the role `warrant`, the argument that places the target in its universality class;<br>- when the route runs on the target, each factor stated over the symbols of the target is `denoting`;<br>- under a declared use, the test is `not-applicable` | [battermanrice2014]; [rice2021] |
| `modal-knowledge` | Witness or proof | the block states the space of alternatives that the admitted laws and the domain fix, and supplies a witness for a possibility, or a proof or an exhaustive exclusion for an impossibility or a necessity | [modal strength](modal-strength.md) |
| `model-knowledge` | Consequence | the consequence or the counterexample is stated over the declared symbols of the model or of the formal target, and names the proof obligations of the task that it discharges | — |

## Warrant

The warrant tests apply to the answer, and through it to the records on which it rests. Fidelity, in particular, is computed through the binding of the answer and is never asserted beside it. An answer that [declares its use](answer-form.md#^declared-use) binds to no target, so the test of adequacy to use replaces fidelity for it. ^warrant-through-binding

| Criterion              | Test                                                                                                                                                                                                      | Research action                                                                                                                     | Source                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Phenomenon established | the [phenomenon](phenomenon.md) is established before it is explained (depending on the *evidential status*), and its [data model](phenomenon.md#^data-model-declarations) is declared adequate for the purpose of the question | detect or replicate the phenomenon first, when its status is "reported" or "predicted"; state the adequacy of the data model for the question | [bogen1988]; presupposition of the topic [vanfraassen1980]; [bokulichparker2021] |
| Foil evidence          | the evidence for the [contrast](contrast.md) comes from the foil itself (*foil status*)                                                                                                              | - observed foil: compare the recordings of the fact and of the foil;<br>- counterfactual foil: produce the foil by an intervention or a simulation                 | [lipton2004]                                               |
| Law warrant            | each ground meets what its role requires. A law cited with the role `warrant` holds on the basis that its [*warrant value*](background.md#^law-warrant) claims: a law marked `derived` is derivable from the laws on which it rests, and a law marked `fitted` or `measured` names its source data. Each ground with the role `datum` names a version of the data | check each ground against what its role requires, because a conclusion inherits the weakest warrant among the laws that it uses | [nagel1961] |
| Closure                | the route matches the [*closure of the laws*](background.md#^laws) admitted about the system                                                                                                  | - formal target: derive from the laws, by proof or by simulating their consequences;<br>- empirical target: measure or intervene | —                                                          |
| Fidelity               | - when the claim bears on the target through a binding: the [comparison computed](model-and-binding.md#^comparison) from that binding, a version of the data, and the metric and tolerance of the [required accuracy](epistemic-task.md) finds each feature pair within the tolerance; <br>- for a [family of models](model-and-binding.md#^model-family), the rule that the answer declares decides: one comparison per member, each of which must pass, or one comparison of the ensemble of the family; <br>- when the answer declares its use, or when the route runs on the target itself: `not-applicable` | compute the comparison on a version of the data, and state how each of its [three reports](model-and-binding.md#^comparison-reports) bears on the verdict | fidelity criteria [weisberg2013]; adequacy for purpose [parker2020] |
| Adequacy to use        | when the answer [declares its use](answer-form.md#^declared-use): the evidence shows that the model has the property that the use states, such as the behavior that a proof of principle exhibits or the task that a tool performs; otherwise `not-applicable` | exhibit the property in the model, by a derivation or a simulation | adequacy for purpose [parker2020] |
| Robustness             | the claim survives each [*idealization*](answer-form.md#^idealizations) among its grounds, as its dependence records; for a family of models, the claim holds across the members of the family | relax each idealization, or compare models that share the claimed structure                                                         | robustness analysis [weisberg2006]                         |
| Selection              | a claim about a subset of members extends to the full class only after a check for selection bias. That bias can arise exactly where the class is [selected on an outcome](target-system.md#^selection-on-outcome)                           | when a criterion depends on an outcome, test the association in the full class                                                      | [hernan2004]                                               |

- **A fidelity verdict cites its comparison and reads its reports.** The verdict names the binding, its version, and the version of the data, so that any reader recomputes the same comparison. The comparison reports whether the binding was committed before the data, how it treated the data already used for calibration, and whether the data model of the phenomenon overlaps with the grounds of the answer. This method fixes two rules on these reports. First, data used to fit a calibration parameter count toward fidelity only under the treatment `cross-validated` or `bayesian`, since using calibration data for confirmation is legitimate or not depending on the method [steelewerndl2013]. Data under the treatment `excluded` contribute nothing to the verdict, and data under the treatment `reused` never count toward it. Second, a raised flag of circularity keeps the verdict `pending` until the evidence shows that the overlapping models do not decide the compared features [bokulichparker2021]. Such evidence is, for instance, a compared feature that stays within the tolerance when the overlapping model of the data, or the overlapping key, is replaced by an independent one. The time of commitment is reported in the evidence, and the method fixes no rule on it. ^fidelity-reads-reports

- **The discrepancy of a comparison has three owners.** The binding owns the structural discrepancy, the phenomenon owns the observation error, and the question owns the tolerance, as the [owners of the discrepancy](model-and-binding.md#^discrepancy-owners) state. A fidelity test therefore never adjusts the tolerance to a discrepancy, whether found or declared: a declared structural discrepancy that exceeds the tolerance fails its feature pair, as the [comparison](model-and-binding.md#^comparison) states.

*Example* of tests applied to the answer about gamma oscillations, two of admissibility and two of warrant:

- contrast (admissibility, explanatory block): the asynchronous state must be produced, for instance by removing the synaptic delay in the model, since the foil never occurred in the network (counterfactual foil);
- admissible explanans (admissibility, core): the test passes when the question bounds the explanans to population rates, since the claim depends on no other variable;
- robustness (warrant): the claim must hold at finite network size, since the mean-field limit is an idealization among its grounds;
- fidelity (warrant): the comparison of the binding of the rate model with the recorded spectra, at version 3 of the data, must place the predicted frequency within the tolerance of the question; the comparison reports that the coupling strength was fitted on another session, and that this session was excluded.

## Appraisal

The [epistemic and pragmatic virtues](epistemic-pragmatic-virtues.md) appraise an answer that passed both tiers. A virtue therefore never compensates for a failed test (e.g. an economical answer that ignores the foil is still inadmissible).

> [!NOTE] Appraisal records ^appraisal-record
> Appraisal adds no test of its own. Its criteria are the virtues marked [preferred](epistemic-pragmatic-virtues.md#^virtue-standing) by the question, and each of them already carries its operational question. Appraisal therefore adds only a record, filled for one answer at a time.

| Virtue selected | Assessment of this answer                                            | Preferred over                                            |
| --------------- | -------------------------------------------------------------------- | --------------------------------------------------------- |
| [virtue]        | [the result that the operational question of that virtue returns for this answer] | [the candidates that it beats on that virtue, or none assessed] |

- **An answer is appraised on its own.** The assessment states the result that each selected virtue returns for the answer, so a lone candidate is appraised as fully as one of several. A comparison is recorded only once another candidate has been appraised. The comparison is then drawn from the assessments already filled.

- **Only the virtues marked preferred are appraised.** The question commits the inquiry only to the virtues that it selects, so an unselected virtue does not bear on the answer. A virtue that the question marks [constitutive](epistemic-pragmatic-virtues.md#^virtue-standing) is settled by the product test instead. An answer that lacks a constitutive virtue is inadmissible, so appraisal does not assess that virtue a second time.

- **Understanding is a dimension of appraisal.** Understanding is not an [aim](epistemic-aim.md#^understanding), so no test checks it as the product of a question. A question that demands understanding marks intelligibility and structural transparency preferred, and appraisal then records how far the answer makes its dependences followable and exposed [deregt2005]. A question may instead mark these virtues constitutive, and the product test then settles them. An answer whose claim bears on no target may also [declare](answer-form.md#^declared-use) understanding as its use, with the dependences that the model must expose. The warrant test of adequacy to use then checks that the model exposes them, not that a reader understands them. ^understanding-appraised

- **No aggregate score without stated weights.** Virtues conflict with one another, for instance generality with precision [matthewson2009]. A single score computed without weights fixed in advance conceals this trade-off, so the record keeps one assessment per virtue.

## Recording an assessment

The verdicts of the tests and the appraisal are kept outside the answer, in one record per candidate assessed. The record references the candidate that it assesses and the question that fixes the tests. A candidate can then be restated, or a second one added, without rewriting a verdict or an assessment already settled. ^assessment-record

| Specification | When it is required | Options or frame | Examples | Source |
| ------------- | ------------------- | ---------------- | -------- | ------ |
| Answer — the candidate whose verdicts this record holds | always | the identifier of one [candidate answer](answer-form.md) | the answer by inhibitory delay | — |
| Question — the record whose specifications fix which tests apply | always | the identifier of one question | why the network is synchronous rather than asynchronous | [tests drawn from filled specifications](#^conditions-satisfaction) |
| Tests: admissibility | always | per criterion of the tests of the core and of the tests of the block of the aim of the question, a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | contrast: pass, by producing the asynchronous state in a simulation; admissible explanans: not-applicable, since the question bounded the answer to no variables | the [admissibility level](#^admissibility-per-block) |
| Tests: warrant | always | per criterion of the warrant table, a verdict with the evidence that settles it | robustness: fail, since the claim did not survive at finite network size | the [warrant level](#^warrant-through-binding) |
| Comparisons — the inputs from which each comparison cited by a verdict is recomputed | when a verdict of fidelity rests on a binding | per comparison, the binding and its version, and the version of the data; the metric and the tolerance are read from the question | version 2 of the binding of the rate model, with version 3 of the recordings | the [computed comparison](model-and-binding.md#^comparison-recomputed) |
| Obligations | when the question states a proof obligation | per obligation, a verdict with the derivation or the counterexample that settles it | the necessary direction: pass, by the derivation of Lemma 2; the sufficient direction: fail, by a counterexample | — |
| Appraisal | when the question marks a virtue [preferred](epistemic-pragmatic-virtues.md#^virtue-standing) | per virtue, the assessment of this answer, and the candidates over which it is preferred once they have been appraised | intelligibility: the oscillation frequency can be read off the delay, without simulating the network | the [appraisal record](#^appraisal-record) |
| Credence | when the assessor states a degree of belief in the answer | a number between 0 and 1, with the evidence and the prior from which it follows | 0.6, after two replications at a larger width | degree of belief, revised by conditionalization [talbott2016] |
| Credence: value | with the credence | a number between 0 and 1 | 0.6 | — |
| Credence: basis | with the credence | the evidence and the prior from which the value follows | two replications at a larger width, from a prior of 0.3 | [credence beside the verdicts](#^credence) |

- **A credence complements the verdicts and replaces none of them.** A verdict states whether one test passed. A credence states how strongly the assessor believes the answer given all the verdicts and the prior evidence, so it can rise or fall without any verdict changing. The credence carries its basis, so that a later assessor can revise it when the evidence changes. ^credence

- **A verdict of `not-applicable` is a *result*.** The record marks a test removed by an empty specification as `not-applicable`, instead of leaving it pending. A reader can then tell an untested candidate from a fully assessed one.

- **An assessment ends at its verdicts.** Accepting an answer is a further act: a revision of the [background](definitions/inquiry/epistemic-problem.md#^candidates), which moves the answer into the accepted claims, as the [acceptance of an answer](epistemic-aim.md#^acceptance) states.

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the principle behind each test, as cited.
> - **Proposals:**
> 	- deriving one test from each filled specification;
> 	- the three tiers and their order;
> 	- the division of admissibility into tests of the core and tests of each aim block;
> 	- the routing of an assessment by the erotetic relation, and the disposition `corrective`;
> 	- the test of the target status of a factor;
> 	- the test of adequacy to use, in place of fidelity, for an answer that declares its use;
> 	- the rule on the fidelity of a family of models, declared by the answer;
> 	- requiring a stated map and a consistency check whenever the model re-individuates the system;
> 	- computing fidelity through a binding, and the two rules on the reports of a comparison;
> 	- recording one assessment per selected virtue, for one answer at a time, instead of a single score.

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [battermanrice2014] ◐ Batterman & Rice, "Minimal model explanations", *Philosophy of Science* 81(3), 349–376, 2014
- [bechtel1993] ◐ [Bechtel & Richardson, _Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research_, Princeton UP 1993; MIT Press 2010](https://direct.mit.edu/books/monograph/2860/Discovering-ComplexityDecomposition-and)
- [belnap1976] ○ Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976; corrective answers, which deny a presupposition
- [bogen1988] ○ Bogen & Woodward, "Saving the phenomena", _Philosophical Review_ 97(3), 1988
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [hamblin1958] ○ Hamblin, "Questions", *Australasian Journal of Philosophy* 36, 1958
- [hernan2004] ◐ [Hernán, Hernández-Díaz & Robins, "A structural approach to selection bias", _Epidemiology_ 15(5), 2004](https://pubmed.ncbi.nlm.nih.gov/15308962/)
- [lipton2004] ◐ Lipton, _Inference to the Best Explanation_, 2nd ed., ch. 3; [Lipton, "Making a difference"](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [matthewson2009] ◐ [Matthewson & Weisberg, "The structure of tradeoffs in model building", _Synthese_ 170, 2009](https://link.springer.com/article/10.1007/s11229-008-9366-y)
- [nagel1961] ◐ Nagel, _The Structure of Science_, Harcourt, Brace & World, 1961, bridge laws, via [SEP, Scientific Reduction](https://plato.stanford.edu/entries/scientific-reduction/)
- [parker2020] ◐ Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020
- [rice2021] ◐ Rice, *Leveraging Distortions: Explanation, Idealization, and Universality in Science*, MIT Press, 2021
- [rubenstein2017] ◐ [Rubenstein et al., "Causal consistency of structural equation models", *UAI*, 2017](https://www.auai.org/uai2017/proceedings/papers/11.pdf)
- [spirtes2004] ✓ [Spirtes & Scheines, "Causal inference of ambiguous manipulations", *Philosophy of Science* 71(5), 2004](https://philpapers.org/rec/SPICIO)
- [steelewerndl2013] ◐ Steele & Werndl, "Climate models, calibration, and confirmation", *British Journal for the Philosophy of Science* 64(3), 609–635, 2013
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", *Philosophy of Science* 64, S65–S74, 1997](https://philpapers.org/rec/STEENF)
- [suarez2004] ◐ Suárez, "An inferential conception of scientific representation", *Philosophy of Science* 71(5), 767–779, 2004
- [talbott2016] ◐ [Talbott, "Bayesian epistemology", _SEP_, revised 2016](https://plato.stanford.edu/entries/epistemology-bayesian/), §1 on degrees of belief and conditionalization
- [vanfraassen1980] ✓ van Fraassen, _The Scientific Image_, ch. 5; [the chapter text](https://www.fitelson.org/290/vanfraassen_pte.pdf)
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", _Philosophy of Science_ 73(5), 2006](https://philpapers.org/rec/MICRA)
- [weisberg2013] ◐ [Weisberg, _Simulation and Similarity_, OUP, 2013](https://academic.oup.com/book/3141/chapter/143989335)
- [woodward2003] ○ [Woodward, _Making Things Happen_, OUP, 2003](https://academic.oup.com/book/4324)
- [woodward2010] ◐ [Woodward, "Causation in biology…", _Biology & Philosophy_ 25, 2010](https://link.springer.com/article/10.1007/s10539-010-9200-z)
