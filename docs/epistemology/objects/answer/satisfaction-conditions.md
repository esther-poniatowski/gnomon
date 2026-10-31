---
tags:
  - theory
index: "[Answer and assessment](docs/epistemology/objects/answer/_index.md)"
aliases:
  - Conditions of satisfaction
---
# Conditions of satisfaction

> [!QUESTION] Goal: which tests must a candidate answer pass, given the specification of its question?

The tests that a candidate answer must pass are derived from the [specification of its question](../question/question-specification.md), $\langle\Sigma,T,\mathcal{V}\rangle$: its [subject](../subject/subject-of-inquiry.md), its [epistemic task](../task/epistemic-task.md) and its [virtues](../task/epistemic-pragmatic-virtues.md). The tests follow from those three layers and add no decision of their own, so they form no layer of the specification. The [form of the answer](answer-form.md) fixes the object to which those tests apply: one typed claim, with its core and the block of the aim of its question. Some tests also read the records on which the answer rests: its [model, its binding and the computed comparison](model-and-binding.md), and the [phenomenon](../subject/phenomenon.md) of the question.

An **assessment** is the object that holds the result of testing one candidate answer against one version of the specification of its question. An assessment holds four results: ^assessment

- the verdict of each test of admissibility and of warrant, with the evidence that settles it;
- the disposition, read from those verdicts;
- the appraisal of the answer for each virtue that the question marks preferred;
- an optional credence of the assessor, with its basis.

An assessment ends at these results. Accepting the answer is a further act, the [act of acceptance](../status/statuses-and-acceptance.md#^acceptance-act). The [assessment record](../../../specification/assessment.md) documents the fields of an assessment.

A candidate answer is evaluated at three levels: ^conditions-satisfaction

1. **admissibility**: is the candidate an *actual* answer to the question?
2. **warrant**: does the *route* that the specification implies support the answer?
3. **appraisal**: how well does an answer that passed serve the virtues that the question selected, and which of several such answers is then preferred?

The first two levels *filter* the answers that *satisfy* the research question. For a candidate answer $h$ to a question $Q$, a member of the set $H$ of [proposed candidates](../../foundations/inquiry-and-state.md#^state):
$$\mathrm{Sat}(h\mid Q)=\mathrm{Admissible}(h\mid Q)\wedge\mathrm{Warranted}(h\mid Q)$$
The first conjunct holds when $h$ is an [admissible answer](../question/question.md#^answer-sets) of $Q$: a direct or a partial answer that passes the tests of admissibility, the constitutive virtues included. The whole holds when $h$ is also warranted, and so a satisfying answer. The third level, by contrast, *appraises* only the answers that already pass, one at a time.

The **disposition** of an assessment follows from its verdicts at the first two levels. The disposition is `not-satisfied` when one test fails, `withheld` when no test fails and one is pending, and `satisfied` when every test passes or does not apply. For a [corrective answer](#^erotetic-routing), the disposition that would be `satisfied` is `corrective` instead: the answer does not satisfy its question, and shows instead that the question has no true direct answer. The disposition is read from the verdicts and from the erotetic relation of the answer, not recorded beside them, so the record cannot disagree with them. ^disposition

Each test derives from a filled specification, so an empty specification removes its test, whose verdict is then `not-applicable`. A specification left open on purpose, with the maturity `open`, differs from an empty one: it is still to be fixed, so its test stays `pending` until the specification is narrowed.

**The tests are fixed before the assessment, under iteration too.** Each assessment is made against the version of the specification of its question fixed before it, so that no test is adjusted to the candidate that it judges [nosek2018]. A revision of a layer of the specification voids the verdicts made under the earlier version, and the revision records its trigger, as the second condition of [controlled iteration](../../processes/inquiry/specification-order.md#^controlled-iteration) requires. A new assessment against the revised version then replaces the voided one. A revision prompted by a verdict therefore names that verdict as its trigger, so that a reader can tell a specification fixed before the evidence from a specification adjusted to it. ^tests-fixed-before

> [!WARNING] Redundancy
> Most criteria merely *check* whether the answer complies with the three layers of the specification of its question, taken singly or in combination.

## Admissibility

The admissibility tests check that the candidate is an answer to the question as specified. Most of them read only the candidate and the records that it cites, before any evidence is weighed; a few may require evidence, such as the agreement of two models on the interventions that both represent. Every answer passes the tests of the core. An answer passes, in addition, the tests of the block of the aim of its question, and the tests of the blocks of other aims do not apply to it. ^admissibility-per-block

### Tests of the core

| Criterion      | Test                                                                                                                                                                                                                                                                                                                                                                           | Source                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Product        | - for a complete answer, the claim is a direct answer of the type that the full atomic question fixes: it meets the [answer conditions](../task/epistemic-aim.md#^answer-conditions) of the aim, and the answer holds the block of that aim; for a partial answer, the claim narrows the direct answers of that type, and the block holds the part of the request that the claim settles;<br>- the inquiry fixes every specification [that aim requires](../../../specification/question-task.md#^required-by-aim);<br>- the answer holds every virtue that the question marks [constitutive](../task/epistemic-pragmatic-virtues.md#^virtue-standing) | direct answers [belnap1976]; intelligibility criterion [deregt2005] |
| Scope          | - the [domain of the claim](answer-form.md#^derived-domain) covers the [*reference class* of the system](../subject/target-system.md) $S$, restricted by the [*domain*](../subject/domain.md) $D$, with the *quantification* that each declared [source of variation across instances](../subject/phenomenon.md) carries;<br>- for a deductive route, the domain compared is the one derived from the grounds, not a stated one;<br>- when the claim bears on the target through a binding, the domain of comparison of the binding covers $D$, and each region of extrapolation is marked;<br>- laws stated over derived units hold across the *whole* domain $D$ | target population [lundberg2021] |
| Grain          | - the claim specifies the [*observable*](../subject/phenomenon.md) at the stated grain: its *value set*, the indices that its *signature* retains, and the *expression* or *condition* that fixes it; <br>- the explanandum variable stays definable over the units of the model on which the route runs | proportionality [woodward2010] |
| Individuation  | - each [bearer](model-and-binding.md#^perspective) of the model is either a unit defined by a stated map from the constituents that the system declares, or a unit of the model alone, which bears on the target only through a binding, as the [elements of a model](../../../specification/model.md#^model-elements) declare it; <br>- no quantity of the model enters by reference to a target quantity; <br>- the re-individuated model agrees with the declared one on the interventions that both represent, for a causal, mechanistic or constitutive relation, and on the derivations, for a formal target | decomposition as a revisable strategy [bechtel1993]; causal consistency [rubenstein2017] |
| Admissible explanans | applies only to an answer under the aim `explanation`, and is `not-applicable` under any other aim, since only the [block of an explanation](answer-form.md#^explanation-block) holds an explanans: every factor of that block, and every quantity on which the explanatory claim depends through the grounds and the dependence that it reads, lies within the set of variables that the [bound on the explanans](../task/admissible-explanans.md#^bound-and-induced-set) $\lambda$ admits for the target system $S$. Every intervention on an aggregate also has an unambiguous effect | [spirtes2004] |
| Binding        | - when the route runs on a model that stands in for the target and the claim bears on the target, the answer cites one [binding](../../../specification/binding.md#^binding-record) of each model to the phenomenon of the question;<br>- an answer that [declares its use](answer-form.md#^declared-use) instead makes a claim on a model or on a formal class only: a claim of actual strength about an empirical target, a prediction or a description of a target fails this test without a binding | [suarez2004] |
| Modal strength | the answer claims the requested *[modal strength](../task/modal-strength.md)*: realized in $S$ (actual), consistent with the laws of $S$ within $D$ (possible), or excluding every foil under those laws (necessary). Whether the claim holds is decided by the warrant tests, along the routes of evidence of each [modal strength](../task/modal-strength.md): for an actual strength, closure, by measurement or intervention, and fidelity for an empirical target, computed through the binding, with selection when the claim extends from the members studied to their class, and closure and law warrant for a formal target, with fidelity when the derivation runs on a model of the target rather than on its laws; for a possible strength, closure and law warrant applied to the model that exhibits the phenomenon; for a necessary strength, closure and law warrant applied to the proof of impossibility or to the exhaustive exclusion | [epistemic task](../task/epistemic-task.md) |

- **The erotetic relation routes the assessment.** The [erotetic relation](answer-form.md#^erotetic-relation) of an answer is a field, not a test, and it decides which tests apply: ^erotetic-routing
    - every test of the core and of the aim block applies to a complete or a partial answer. A partial answer that satisfies these tests still leaves its question open, since the answer is not conclusive;
    - a corrective answer, which denies a presupposition of the question [belnap1976], holds no aim block, so the product test and the tests of the aim block are `not-applicable`. The warrant tests then judge the claim that the presupposition is false, and an accepted corrective answer refutes the soundness of the question;
    - a reformulating answer is assessed against the revised question that it names.

### Tests of the aim block

| Aim block | Criterion | Test | Source |
| --------- | --------- | ---- | ------ |
| `description` | Values | the block assigns a value, with its uncertainty, to every observable and feature that the request covers, at the grain of the question and per declared source of variation | [woodward2010] |
| `exploration` | Space | the block declares its space and its equivalence criterion, each marked as an input or an output, and every class that it reports meets the [detection criterion](../subject/phenomenon.md#^exploratory-phenomenon) of the phenomenon | [steinle1997] |
| `prediction` | Outputs | each predicted output is one of the outputs to match that the [required accuracy](../task/epistemic-task.md) names, under a stated condition of the target, with its uncertainty | — |
| `explanation` | Contrast | the block favors the [*fact over each foil*](../subject/contrast.md). For each foil that the question names, some factor *separates* the two, by citing a condition present for the fact and absent for that foil | favoring the topic [vanfraassen1980]; difference condition [lipton2004] |
| `explanation` | Relation | - the dependence that the explanatory claim reads has the [*requested kind*](../task/requested-relation.md) (e.g. invariance under interventions if causal, mutual manipulability if constitutive, a proof if mathematical);<br>- each factor reaches the effect that it *produces* through the laws and relations that it names | [woodward2003]; [craver2007] |
| `explanation` | Target status | - each factor declares a [target status](answer-form.md#^target-status);<br>- when the route runs on a model, the binding holds the [feature pair that the status requires](../../../specification/answer.md#^status-pairs), and a limit construct cites among its grounds, with the role `warrant`, the argument that places the target in its universality class;<br>- when the route runs on the target description, each factor stated over the symbols of the target is `denoting`;<br>- under a declared use, the test is `not-applicable` | [battermanrice2014]; [rice2021] |
| `modal-knowledge` | Witness or proof | the block states the space of alternatives that the admitted laws and the domain fix, and supplies a witness for a possibility, or a proof or an exhaustive exclusion for an impossibility or a necessity | [modal strength](../task/modal-strength.md) |
| `model-knowledge` | Consequence | the consequence or the counterexample is stated over the declared symbols of the model or of the formal target, and names the proof obligations of the task that it discharges | — |

## Warrant

The warrant tests apply to the answer, and through it to the records on which it rests. Fidelity, in particular, is computed through the binding of the answer and is never asserted beside it. An answer that [declares its use](answer-form.md#^declared-use) binds to no target, so the test of adequacy to use replaces fidelity for it. ^warrant-through-binding

| Criterion              | Test                                                                                                                                                                                                      | Research action                                                                                                                     | Source                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Phenomenon established | the [phenomenon](../subject/phenomenon.md) has the *evidential status* `established` before it is explained, and its [data model](../subject/phenomenon.md#^data-model-declarations) is declared adequate for the purpose of the question | detect or replicate the phenomenon first, when its status is "reported" or "predicted"; state the adequacy of the data model for the question | [bogen1988]; presupposition of the topic [vanfraassen1980]; [bokulichparker2021] |
| Foil evidence          | the evidence for the [contrast](../subject/contrast.md) comes from the foil itself (*foil status*)                                                                                                              | - observed foil: compare the recordings of the fact and of the foil;<br>- counterfactual foil: produce the foil by an intervention or a simulation                 | [lipton2004]                                               |
| Law warrant            | each ground meets what its role requires. A law cited with the role `warrant` holds on the basis that its [*warrant*](../knowledge/background.md#^law-warrant), the provenance of the law, claims: a law marked `derived` is derivable from the laws on which it rests, and a law marked `fitted` or `measured` names its source data. Each ground with the role `datum` names a version of the data | check each ground against what its role requires, since the warrant of a law propagates to the results that rest on it | — |
| Closure                | the route fits the target, as the [*closure of the laws*](../knowledge/background.md#^laws) admitted about the system decides: a derivation for a formal target, whose admitted laws define it completely, and a measurement or an intervention otherwise | - formal target: derive from the laws, by proof or by simulating their consequences;<br>- empirical target: measure or intervene | —                                                          |
| Fidelity               | - when the claim bears on the target through a binding: the [comparison computed](model-and-binding.md#^comparison) from that binding, a version of the data, and the metric and tolerance of the [required accuracy](../task/epistemic-task.md) finds each feature pair within the tolerance; <br>- for a [family of models](model-and-binding.md#^model-family), the rule that the answer declares decides: one comparison per member, each of which must pass, or one comparison of the ensemble of the family; <br>- when the answer declares its use, or when the route runs on the target description: `not-applicable` | compute the comparison on a version of the data, and state how each of its [three reports](model-and-binding.md#^comparison-reports) bears on the verdict | fidelity criteria [weisberg2013]; adequacy for purpose [parker2020] |
| Adequacy to use        | when the answer [declares its use](answer-form.md#^declared-use): the evidence shows that the model has the property that the use states, such as the behavior that a proof of principle exhibits or the task that a tool performs; otherwise `not-applicable` | exhibit the property in the model, by a derivation or a simulation | adequacy for purpose [parker2020] |
| Robustness             | the claim survives each [*idealization*](answer-form.md#^idealizations) among its grounds, as its dependence records; for a family of models, the claim holds across the members of the family; the [virtue of robustness](../task/epistemic-pragmatic-virtues.md#^robustness-two-tiers), by contrast, ranks answers by the breadth of the changes that they survive | relax each idealization, or compare models that share the claimed structure                                                         | robustness analysis [weisberg2006]                         |
| Selection              | a claim about a subset of members extends to the full class only after a check for selection bias. That bias can arise exactly where the class is [selected on an outcome](../subject/target-system.md#^selection-on-outcome)                           | when a criterion depends on an outcome, test the association in the full class                                                      | [hernan2004]                                               |

- **A fidelity verdict cites its comparison and reads its reports.** The verdict names the binding, its version, and the version of the data, so that any reader recomputes the same comparison. The comparison reports whether the binding was committed before the data, how it treated the data already used for calibration, and whether the data model of the phenomenon overlaps with the grounds of the answer. This method fixes two rules on these reports. First, data used to fit a calibration parameter count toward fidelity only under the treatment `cross-validated` or `bayesian`, since using calibration data for confirmation is legitimate or not depending on the method [steelewerndl2013]. Data under the treatment `excluded` contribute nothing to the verdict, and data under the treatment `reused` never count toward it. Second, a raised flag of circularity keeps the verdict `pending` until the evidence shows that the overlapping models do not decide the compared features [bokulichparker2021]. Such evidence is, for instance, a compared feature that stays within the tolerance when the overlapping model of the data, or the overlapping key, is replaced by an independent one. The time of commitment is reported in the evidence, and the method fixes no rule on it. ^fidelity-reads-reports

- **The discrepancy of a comparison has three owners.** The binding owns the structural discrepancy, the phenomenon owns the observation error, and the question owns the tolerance, as the [owners of the discrepancy](model-and-binding.md#^discrepancy-owners) state. A fidelity test therefore never adjusts the tolerance to a discrepancy, whether found or declared: a declared structural discrepancy that exceeds the tolerance fails its feature pair, as the [comparison](model-and-binding.md#^comparison) states.

*Example* of tests applied to the answer about gamma oscillations, two of admissibility and two of warrant:

- contrast (admissibility, explanatory block): the asynchronous state must be produced, for instance by removing the synaptic delay in the model, since the foil never occurred in the network (counterfactual foil);
- admissible explanans (admissibility, read on the explanatory block): the test passes when the question bounds the explanans to population rates, since the claim depends on no other variable;
- robustness (warrant): the claim must hold at finite network size, since the mean-field limit is an idealization among its grounds;
- fidelity (warrant): the comparison of the binding of the rate model with the recorded spectra, at version 3 of the data, must place the predicted frequency within the tolerance of the question; the comparison reports that the coupling strength was fitted on another session, and that this session was excluded.

## Appraisal

The [epistemic and pragmatic virtues](../task/epistemic-pragmatic-virtues.md) appraise an answer that passed both tiers. A virtue therefore never compensates for a failed test (e.g. an economical answer that ignores the foil is still inadmissible).

> [!NOTE] Appraisal records ^appraisal-record
> Appraisal adds no test of its own. Its criteria are the virtues marked [preferred](../task/epistemic-pragmatic-virtues.md#^virtue-standing) by the question, and each of them already carries its operational question. Appraisal therefore adds only a record, filled for one answer at a time, whose fields the [assessment record](../../../specification/assessment.md) documents.

- **An answer is appraised on its own.** The assessment states the result that each selected virtue returns for the answer, so a lone candidate is appraised as fully as one of several. A ranking against another candidate is recorded only once that candidate has been appraised. The ranking is then drawn from the assessments already filled.

- **Only the virtues marked preferred are appraised.** The question commits the inquiry only to the virtues that it selects, so an unselected virtue does not bear on the answer. A virtue that the question marks [constitutive](../task/epistemic-pragmatic-virtues.md#^virtue-standing) is settled by the product test instead. An answer that lacks a constitutive virtue is inadmissible, so appraisal does not assess that virtue a second time.

- **Understanding is a dimension of appraisal.** Understanding is not an [aim](../task/epistemic-aim.md#^understanding), so no test checks it as the product of a question. A question that demands understanding marks intelligibility and structural transparency preferred, and appraisal then records how far the answer makes its dependences followable and exposed [deregt2005]. A question may instead mark these virtues constitutive, and the product test then settles them. An answer whose claim bears on no target may also [declare](answer-form.md#^declared-use) understanding as its use, with the dependences that the model must expose. The warrant test of adequacy to use then checks that the model exposes them, not that a reader understands them. ^understanding-appraised

- **No aggregate score without stated weights.** Virtues conflict with one another, for instance generality with precision [matthewson2009]. A single score computed without weights fixed in advance conceals this trade-off, so the record keeps one assessment per virtue.

## Norms of evidence

The verdicts of the tests and the credence of the assessor follow two norms, which the method holds as complements rather than as rival norms of one verdict. The [activities of evaluation](../../processes/activities/evaluation.md) are typed with these norms. ^evidence-norms

- **Severity governs the verdict of a test.** A passing result supports a claim only if the test would probably have failed the claim, had the claim been false [mayo2018].

- **A credence complements the verdicts and replaces none of them.** A verdict states whether one test passed. A credence states how strongly the assessor believes the answer given all the verdicts and the prior evidence, so it can rise or fall without any verdict changing. The credence carries its basis, so that a later assessor can revise it when the evidence changes. A credence is optional, and a credence that the assessor states is a Bayesian degree of belief, revised by conditionalization: the new credence in the answer equals the old credence conditional on the evidence [howson2006]. ^credence

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the principle behind each test, as cited.
> - **Proposals:**
> 	- deriving one test from each filled specification of the three layers;
> 	- the three tiers and their order;
> 	- the division of admissibility into tests of the core and tests of each aim block;
> 	- the routing of an assessment by the erotetic relation, and the disposition `corrective`;
> 	- the test of the target status of a factor;
> 	- the test of adequacy to use, in place of fidelity, for an answer that declares its use;
> 	- the rule on the fidelity of a family of models, declared by the answer;
> 	- requiring a stated map and a consistency check whenever the model re-individuates the system;
> 	- computing fidelity through a binding, and the two rules on the reports of a comparison;
> 	- recording one assessment per selected virtue, for one answer at a time, instead of a single score;
> 	- severity for the verdict of a test and an optional Bayesian credence, held as complements;
> 	- the assessment as one object, which ends at its verdicts, its disposition, its appraisal and its credence;
> 	- each assessment made against the version of the specification fixed before it, with a revision that voids the earlier verdicts and records its trigger;
> 	- the test of the admissible explanans confined to the block of an explanation.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [battermanrice2014] ◐ Batterman & Rice, "Minimal model explanations", *Philosophy of Science* 81(3), 349–376, 2014
- [bechtel1993] ◐ [Bechtel & Richardson, *Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research*, Princeton University Press, 1993; reissued MIT Press, 2010](https://doi.org/10.7551/mitpress/8328.001.0001)
- [belnap1976] ◐ [Belnap & Steel, *The Logic of Questions and Answers*, Yale University Press, 1976](https://catalogue.bnf.fr/ark:/12148/cb353871722); direct answers, which settle a question, and corrective answers, which deny a presupposition
- [bogen1988] ◐ [Bogen & Woodward, "Saving the phenomena", *Philosophical Review* 97(3), 303–352, 1988](https://doi.org/10.2307/2185445)
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Oxford University Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [deregt2005] ◐ [de Regt & Dieks, "A contextual approach to scientific understanding", _Synthese_ 144, 2005](https://link.springer.com/article/10.1007/s11229-005-5000-4); criterion for intelligibility checked through secondary summaries
- [hernan2004] ◐ [Hernán, Hernández-Díaz & Robins, "A structural approach to selection bias", _Epidemiology_ 15(5), 2004](https://pubmed.ncbi.nlm.nih.gov/15308962/)
- [howson2006] ◐ [Howson & Urbach, *Scientific Reasoning: The Bayesian Approach*, 3rd ed., Open Court, 2006](https://researchonline.lse.ac.uk/id/eprint/12474/)
- [lipton2004] ◐ [Lipton, *Inference to the Best Explanation*, 2nd ed., Routledge, 2004](https://doi.org/10.4324/9780203470855); ch. 3, "The causal model", checked through [Lipton, "Making a difference", *Philosophica* 51, 39–54, 1993](https://www.hps.cam.ac.uk/files/lipton-making-difference.pdf)
- [lundberg2021] ✓ [Lundberg, Johnson & Stewart, "What is your estimand?", _ASR_ 86(3), 2021](https://journals.sagepub.com/doi/abs/10.1177/00031224211004187)
- [matthewson2009] ◐ [Matthewson & Weisberg, "The structure of tradeoffs in model building", _Synthese_ 170, 2009](https://link.springer.com/article/10.1007/s11229-008-9366-y)
- [mayo2018] ◐ [Mayo, *Statistical Inference as Severe Testing: How to Get beyond the Statistics Wars*, Cambridge University Press, 2018](https://doi.org/10.1017/9781107286184)
- [nosek2018] ◐ [Nosek, Ebersole, DeHaven & Mellor, "The preregistration revolution", _PNAS_ 115(11), 2018](https://www.pnas.org/doi/10.1073/pnas.1708274114)
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [rice2021] ◐ Rice, *Leveraging Distortions: Explanation, Idealization, and Universality in Science*, MIT Press, 2021
- [rubenstein2017] ◐ [Rubenstein et al., "Causal consistency of structural equation models", *UAI*, 2017](https://www.auai.org/uai2017/proceedings/papers/11.pdf)
- [spirtes2004] ✓ [Spirtes & Scheines, "Causal inference of ambiguous manipulations", *Philosophy of Science* 71(5), 2004](https://philpapers.org/rec/SPICIO)
- [steelewerndl2013] ◐ Steele & Werndl, "Climate models, calibration, and confirmation", *British Journal for the Philosophy of Science* 64(3), 609–635, 2013
- [steinle1997] ◐ [Steinle, "Entering new fields: exploratory uses of experimentation", *Philosophy of Science* 64(S4), S65–S74, 1997](https://doi.org/10.1086/392587)
- [suarez2004] ◐ Suárez, "An inferential conception of scientific representation", *Philosophy of Science* 71(5), 767–779, 2004
- [vanfraassen1980] ◐ [van Fraassen, *The Scientific Image*, Clarendon Press, 1980](https://doi.org/10.1093/0198244274.001.0001); ch. 5, read in its abridged reprint, "The pragmatic theory of explanation", in Pitt (ed.), *Theories of Explanation*, Oxford University Press, 1988, 136–155 ([PDF](https://www.fitelson.org/290/vanfraassen_pte.pdf))
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", *Philosophy of Science* 73(5), 730–742, 2006](https://doi.org/10.1086/518628)
- [weisberg2013] ◐ [Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013](https://doi.org/10.1093/acprof:oso/9780199933662.001.0001)
- [woodward2003] ◐ [Woodward, *Making Things Happen: A Theory of Causal Explanation*, Oxford University Press, 2003](https://doi.org/10.1093/0195155270.001.0001)
- [woodward2010] ◐ [Woodward, "Causation in biology: stability, specificity, and the choice of levels of explanation", *Biology & Philosophy* 25(3), 287–318, 2010](https://doi.org/10.1007/s10539-010-9200-z)
