---
tags:
  - theory
  - wip
index: "[Answer and assessment](docs/epistemology/objects/answer/_index.md)"
aliases:
  - Model and binding
---
# Model and binding

> [!QUESTION] Goal: how does a model stand in for its target, and how is a value of the model carried to a value of the target?

A [candidate answer](answer-form.md) is one typed claim with its grounds. When the route of the answer runs on a model, the model and its relation to the target are stated in records of their own, so that several answers can share them. Three records and one computed object divide the work:

- the **model** declares the units, the quantities and the laws of a model system, a system that stands in for the target;
- the **binding** states which inferences from the model to the target its asserter licenses;
- the **key** states one shared, versioned map between the two sides of a binding;
- the **comparison** is computed from a binding, a version of the data and the tolerance of the question, and is never recorded by hand.

The [model record](../../../specification/model.md), the [binding record](../../../specification/binding.md) and the [key record](../../../specification/key.md) document the fields of the three records.

> [!IMPORTANT] When an answer needs a model and a binding
> The object on which the route of an answer runs decides which records the answer needs. ^when-a-binding
> - **The route runs on the target description.** The target description is the target specification with its background, and no model stands in for it. A measurement or an estimation runs on the data of the [phenomenon](../subject/phenomenon.md), and a derivation from the [laws admitted in the background](../knowledge/background.md#^laws) of a formal target runs on the declarations of the target. The claim is then stated over the symbols of the target and of the phenomenon, and the answer needs neither a model record nor a binding.
> - **The route runs on a model that stands in for the target.** The claim is stated over the symbols of the model, and the step of [transfer to the target](#^binding-records) carries it through a binding of that model to the phenomenon. The warrant test of [fidelity](satisfaction-conditions.md) is computed through that binding.
> - **The route runs on a model, and the claim bears only on that model or on a formal class.** The answer then [declares its use](answer-form.md#^declared-use) instead of a binding. A claim of actual strength about an empirical target, a prediction or a description of a target never takes this route.

## The model

- **The perspective of a model is its choice of bearers.** A [subject of inquiry](../subject/subject-of-inquiry.md) declares one decomposition of the system, under its original description. A model may retain only some of the declared parts, or take other bearers (e.g. collective coordinates, modes, order parameters, effective units). A model may do so because the parts of a system *result* from decomposition, a research strategy that can fail and be revised [bechtel1993]. By choosing its bearers, a model adopts a *perspective* on the system, and such a perspective spans *several* levels of organization [wimsatt1994]. Different models of one system may thus adopt different perspectives, and several perspectives taken together reveal the stable dependencies of the system [massimi2022]. A bearer defined from the declared constituents states its map from them, and each derived term likewise carries its definition, so that the [individuation test](satisfaction-conditions.md) can check the model against the declared system. ^perspective

- **Derived terms change only the *vocabulary* of a model.** A derived term is *defined* from the declared terms. Such a term can be eliminated by substituting its definition, so it proves no new claim about the declared terms [gupta2023]. A *law stated in derived terms*, in contrast, may require a proof. When that proof holds only in a limit or under specific assumptions, each such restriction is recorded as an assumption of that law, which an answer classifies relative to its target, as the [rule on idealizations](answer-form.md#^idealizations) states. ^derived-terms

- **A map from the target defines; a binding asserts.** A map from the declarations of the target defines a bearer or a term of the model, so it cannot be false of the target. The claim that a value of the model matches a value of the target, by contrast, can be false. Such a claim is a surrogative inference, an inference from a feature of the model to a claim about the target, so a binding states it, and a model never enters a quantity of its target by reference. A reference would assert an identity, and a model never stands in an identity with its target. Three consequences follow. First, a map is never the identity, since an identity map would enter a target quantity by reference under another name. Second, a map that both defines a bearer of the model and links the model to the target is stated once, in the model, and the key of a binding that uses it references that definition. Third, a law of the model stated over a mapped term can be false of the target, although the map that defines the term cannot: such a law reaches the target only through a binding, unless it is derived from the laws admitted about the target. ^map-versus-binding

- **A family of models can ground one answer.** Several models then ground the claim together, each with its own binding. The family is assessed as a whole: the [robustness test](satisfaction-conditions.md) asks whether the claim holds across its members, which is the form of robustness analysis [weisberg2006]. The answer also declares how the fidelity of the family is judged: by one comparison per member, each of which must pass, or by one comparison of the ensemble of the family. ^model-family

## The binding

A binding relates a model in use to a phenomenon, or to its data, and records the surrogative inferences from the model to the target that its asserter licenses [suarez2004]. A binding records the claim that Giere calls a *theoretical hypothesis*: the claim that relates a model to a real system [giere1988]. A consequence of the model becomes a claim about the target through the step of *transfer to the target*, which carries the consequence through the binding that licenses it. Neither that step nor a binding activity, which would produce a binding from a model, a phenomenon and a key under a norm, is yet typed among the activities: both are pending a change of the [registry of activities](../../../../src/gnomon/data/registries/activities.yml). ^binding-records

To state a binding, the method adopts, as a choice, the vocabulary of the DEKI account of Frigg and Nguyen, named after denotation, exemplification, keying-up and imputation [friggnguyen2020]:

- the binding *denotes* the phenomenon;
- the binding pairs a feature that the model *exemplifies*, a feature that the model has and is used to refer to, with a feature *imputed* to the target, a feature ascribed to the target;
- the binding states the *key*, the stated map that converts the exemplified feature into the imputed feature.

That vocabulary is a choice of the method, not a settled result of the literature. The neutrality of the binding therefore bears on the grounds that make its inferences sound, not on its vocabulary: a binding records which inferences its asserter licenses, and it stays neutral among the accounts of the grounds that make those inferences sound.

- **A feature pair is computed or argued.** A pair is *computed* when a key maps the feature of the model onto a value or a label that the data of the target determine, as for a quantity, a pattern or a regime. A pair is *argued* when no data determine it, as for the membership of the target in a universality class, argued from its symmetries and its dimension, or for a modal profile. An argued pair cites its argument as a ground of the answer with the role `warrant`, and the law-warrant test judges that ground. The comparison reports an argued pair without computing it. ^pair-modes

- **A unit of the model alone reaches the target through a pair of type `component`.** A unit defined by a stated map from the declared constituents cannot be false of the target, so it needs no pair. A unit of the model alone, such as a box that stands for a subsystem in a stylized model, has no such map. The claim that this unit stands for a constituent of the target, or for a part that the [admissible explanans](../task/admissible-explanans.md) admits, is a localization, and a localization can fail [bechtel1993]. A binding therefore states that claim as a pair of type `component`, argued from evidence of localization, such as the mutual manipulability of the unit and the part [craver2007]. The [explanatory mapping](../../vocabulary/regularities/mechanism-and-mechanistic-model.md#^mechanistic-model-test) of a mechanistic model reads these pairs, since a model explains in the how-actually sense only when its components correspond to parts of the target [kaplan2011]. ^component-pairs

- **The discrepancy has three owners.** The structural discrepancy, the systematic difference between the model and the target that remains at the best parameter values, belongs to the binding, since it describes how the model departs from the target. The observation error belongs to the data, so the [phenomenon](../subject/phenomenon.md#^data-model-declarations) declares it. The tolerance belongs to the question, through the [required accuracy](../task/epistemic-task.md) of its task [kennedyohagan2001] [brynjarsdottir2014]. ^discrepancy-owners

## The computed comparison

A comparison is computed, not recorded. Its inputs are a binding at one version, a version of the data, and the metric and the tolerance that the [required accuracy](../task/epistemic-task.md) of the question fixes, together with the observation error that the phenomenon declares. Its output states, per computed feature pair of the binding, the difference between the model and the target, and whether that difference lies within the tolerance once the observation error is accounted for. The output also reports the structural discrepancy that the binding declares for the pair. A declared discrepancy that exceeds the tolerance fails the pair, so a binding cannot pass a pair by declaring a discrepancy wider than the question tolerates. A discrepancy model fitted to the compared data counts as calibration on those data [kennedyohagan2001] [brynjarsdottir2014], and the calibration treatment then governs those data. ^comparison

Each comparison also reports three facts about its own conditions: ^comparison-reports

- **commitment**: whether the binding was committed before the version of the data;
- **calibration treatment**: how the comparison treated the data already used to fit a calibration parameter: `excluded`, `cross-validated`, `bayesian`, or `reused` when the data are compared again without any correction. Using calibration data for confirmation is legitimate or not depending on the method [steelewerndl2013], so the treatment is reported rather than assumed, and the [rules on the reports](satisfaction-conditions.md#^fidelity-reads-reports) state which treatments count;
- **circularity**: a flag raised when a model declared by the [data model of the phenomenon](../subject/phenomenon.md#^data-model-declarations) overlaps with the model or the grounds of the answer, or with a key of the binding, since an observation operator, the map from the state of a model to the quantities that the data record, can contain the model under test. Data models can contain the models under test [bokulichparker2021], and a comparison that ignores the overlap can be circular.

- **The comparison is recomputed, never edited.** The inputs of a comparison fix its output, so an assessment that cites a comparison records only those inputs, and any reader recomputes the same output. A revised binding or a new version of the data yields a new comparison, and the earlier comparisons stay as they were. ^comparison-recomputed

- **Adequacy for purpose is judged per question.** A comparison judges the model for the purpose that the question states through its feature pairs and its tolerance, not in general [parker2020]. A model adequate for one question can therefore fail for another question about the same phenomenon. A problem that demands a model is solved by the [claim of its adequacy](../problem/epistemic-problem.md#^solution-claim) for the purpose of the problem. ^adequacy-for-purpose

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the surrogative character of inferences from a model to its target, the theoretical hypothesis that relates a model to a real system, the vocabulary of denotation, exemplification, key and imputation within its own account, the separation of structural discrepancy from observation error, and the dependence of data on models, as cited.
> - **Proposals:**
> 	- the division into three records and one computed object, with the model, the binding and the key shared by several answers;
> 	- the adoption of the vocabulary of denotation, exemplification, key and imputation to state a binding, as a choice, with a neutrality that bears on the grounds of the licensed inferences and not on that vocabulary;
> 	- the step of transfer to the target, through a binding, and the binding activity, both pending a change of the registry of activities;
> 	- the rule that decides, from the object on which the route runs, whether an answer needs a binding;
> 	- the distinction between a map that defines a term of the model and a binding that asserts a match with the target;
> 	- the types of a feature pair, and its two modes, computed or argued;
> 	- the pair of type `component`, which relates a unit of the model alone to a part of the target;
> 	- a declared discrepancy bounded by the tolerance of the question, and a fitted discrepancy model counted as calibration;
> 	- maps other than the identity, stated once in the model and referenced by keys;
> 	- the assignment of the structural discrepancy to the binding, of the observation error to the phenomenon, and of the tolerance to the question;
> 	- the structural discrepancy required only at quantitative grain, and interpolation and extrapolation delimited by the range of the calibration data;
> 	- the data that motivated a revised binding counted as calibration data for the new version;
> 	- the three reports of a computed comparison.

Marks follow the [legend of reading marks](../../../../CONTRIBUTING.md#^reading-marks).

- [bechtel1993] ◐ [Bechtel & Richardson, *Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research*, Princeton University Press, 1993; reissued MIT Press, 2010](https://doi.org/10.7551/mitpress/8328.001.0001)
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [brynjarsdottir2014] ◐ Brynjarsdóttir & O'Hagan, "Learning about physical parameters: the importance of model discrepancy", *Inverse Problems* 30, 114007, 2014
- [craver2007] ◐ [Craver, *Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience*, Oxford University Press, 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)
- [friggnguyen2020] ◐ [Frigg & Nguyen, *Modelling Nature: An Opinionated Introduction to Scientific Representation*, Synthese Library 427, Springer, 2020](https://doi.org/10.1007/978-3-030-45153-0); denotation, exemplification, key and imputation
- [giere1988] ◐ [Giere, *Explaining Science: A Cognitive Approach*, University of Chicago Press, 1988](https://press.uchicago.edu/ucp/books/book/chicago/E/bo3622319.html); the theoretical hypothesis, which asserts a relation between a model and a real system, checked through secondary sources
- [gupta2023] ✓ [Gupta & Mackereth, "Definitions", _SEP_, revised 2023](https://plato.stanford.edu/entries/definitions/), §2.3 on conservativeness and eliminability
- [kaplan2011] ◐ [Kaplan & Craver, "The explanatory force of dynamical and mathematical models in neuroscience: a mechanistic perspective", *Philosophy of Science* 78(4), 601–627, 2011](https://doi.org/10.1086/661755); the model-to-mechanism-mapping requirement, checked through the abstract
- [kennedyohagan2001] ◐ [Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society, Series B* 63(3), 425–464, 2001](https://doi.org/10.1111/1467-9868.00294); the model discrepancy separated from the observation error; the tolerance set by a question has no counterpart in the paper
- [massimi2022] ◐ [Massimi, *Perspectival Realism*, Oxford University Press, 2022](https://doi.org/10.1093/oso/9780197555620.001.0001)
- [parker2020] ◐ [Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020](https://doi.org/10.1086/708691)
- [steelewerndl2013] ◐ Steele & Werndl, "Climate models, calibration, and confirmation", *British Journal for the Philosophy of Science* 64(3), 609–635, 2013
- [suarez2004] ◐ Suárez, "An inferential conception of scientific representation", *Philosophy of Science* 71(5), 767–779, 2004
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", *Philosophy of Science* 73(5), 730–742, 2006](https://doi.org/10.1086/518628)
- [wimsatt1994] ◐ [Wimsatt, "The ontology of complex systems: levels of organization, perspectives, and causal thickets", _Canadian Journal of Philosophy_ 24(sup1), 1994](https://www.tandfonline.com/doi/abs/10.1080/00455091.1994.10717400)
