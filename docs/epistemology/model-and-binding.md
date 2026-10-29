---
tags:
  - method
  - wip
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Specifying the model and its binding
  - Model and binding
---
# Specifying the model and its binding

> [!QUESTION] Goal: which records state the model on which an answer rests, relate that model to the phenomenon, and compute the comparison of its values with the data?

A [candidate answer](answer-form.md) is one typed claim with its grounds. When the route of the answer runs on a model, the model and its relation to the target are stated in records of their own, so that several answers can share them. Four records divide the work:

- the **model** declares the units, the quantities and the laws of a system that stands in for the target;
- the **binding** states which inferences from the model to the target its asserter licenses;
- the **key** states one shared, versioned map between the two sides of a binding;
- the **comparison** is computed from a binding, a version of the data and the tolerance of the question, and is never recorded by hand.

> [!IMPORTANT] When an answer needs a model and a binding
> The object on which the route of an answer runs decides which records the answer needs. ^when-a-binding
> - **The route runs on the target itself.** A measurement or an estimation runs on the data of the [phenomenon](phenomenon.md), and a derivation from the [laws admitted in the background](background.md#^laws) of a formal target runs on the declarations of the target. The claim is then stated over the symbols of the target and of the phenomenon, and the answer needs neither a model record nor a binding.
> - **The route runs on a model other than the target.** The claim is stated over the symbols of the model, and a binding of that model to the phenomenon carries the claim to the target. The warrant test of [fidelity](satisfaction-conditions.md) is computed through that binding.
> - **The route runs on a model, and the claim bears only on that model or on a formal class.** The answer then [declares its use](answer-form.md#^declared-use) instead of a binding. A claim of actual strength about an empirical target, a prediction or a description of a target never takes this route.

## The model record

A model is a record of its own, which several answers can ground, such as the [answers of two aims](answer-form.md#^answer-elements) that the model serves. Each answer cites the model instead of declaring it again. ^model-record

A model is a system studied as a stand-in for a target: laws relate quantities that units bear and that take values over indices. Therefore, the model is declared with the blocks and the fields of a [target system](target-system.md), and its laws and organization with those of a [background record](background.md). The value sets of the two formats already carry every distinction that a model draws, so no separate vocabulary is needed. The model $M$ holds the elements below. None of them refers to one question, since several questions can share the model. ^model-elements

| Element | When it is required | Content | Constraint on the element | Examples |
| ------- | ------------------- | ------- | ------------------------- | -------- |
| Background — the record from which the laws of the model are derived | when a law of the model carries the warrant `derived` or `derived-in-a-limit` | the identifier of one [background record](background.md) | — | the admitted training laws of the networks of a class |
| Constituents $C$ | always | the units that the model treats as bearers | - either units defined by a stated map from the [constituents declared for the target](target-system.md) (e.g. coarse-graining, mode decomposition, aggregation, quotient by a symmetry), or units of the model alone, related to the target only through a binding; <br>- the organization $O$ and the terms $V$ range over these units | the slow eigenmodes of the connectivity (defined by a map); the four tipping elements of a box model of the Earth system (units of the model alone) |
| Index sets | when a quantity of the model is indexed by a set that the target does not declare | the set, its extent and its structure, in the format of a target system | — | a coarse-grained scale; a mode number |
| Variables | always, for each quantity that varies in the model | per variable, its own symbol, signature and value set, and its construction: an expression over the symbols of the model, or a map other than the identity from the quantities that the target declares | - a map from the declarations of the target defines a [derived term](#^derived-terms); <br>- a variable never enters by reference to a target quantity, nor by an identity map, which is a reference under another name | the population rate; the overlap with a stored pattern |
| Parameters | when the model holds a quantity fixed | the same content as for a variable, for each quantity that the model holds fixed while the phenomenon unfolds | the parameters that a binding calibrates are marked in that binding, not here | the coupling strength; the adaptation timescale |
| Laws or structural relations $L$ | always | the dependences that link the terms $V$ | - each law states its *warrant* (`derived`, `derived-in-a-limit`, `posited`, `fitted` or `measured`) together with its grounds, and, as a [law of the background](background.md#^law-warrant) does, its origin and the range over which it is established; <br>- a law derived in a limit names the assumption of the model that the limit introduces | the mean-field rate equations (derived in a limit); the stability condition that follows from them (derived); a transfer function obtained from recordings (fitted) |
| Organization $O$ | when the parts or the laws stand in a relation on which the behavior of the model depends | per relation, the tuples that it connects and the laws that state it, in the format of a background record | its constituents follow the [definition of a mechanism](mechanism.md) | a delayed feedback loop, in which excitation drives inhibition and is suppressed in return |
| Assumptions of the laws | when a law of the model holds only under an assumption, such as a limit | per assumption, its motive, the gain that it provides, and whether it is removable, as the [rule on idealizations](answer-form.md#^idealizations) defines them | - only the assumptions that the laws of the model require; <br>- whether an assumption is an idealization, and over which range it holds, depends on the target, so each answer that rests on the model classifies it | the mean-field limit, which closes the rate equations (motive: limit; controlled) |

- **The perspective of a model is its choice of bearers.** A [subject of inquiry](subject-of-inquiry.md) declares one decomposition of the system, under its original description. A model may retain only some of the declared parts, or take other bearers (e.g. collective coordinates, modes, order parameters, effective units). A model may do so because the parts of a system *result* from decomposition, a research strategy that can fail and be revised [bechtel1993]. By choosing its bearers, a model adopts a *perspective* on the system, and such a perspective spans *several* levels of organization [wimsatt1994]. Different models of one system may thus adopt different perspectives, and several perspectives taken together reveal the stable dependencies of the system [massimi2022]. A bearer defined from the declared constituents states its map from them, and each derived term likewise carries its definition, so that the [individuation test](satisfaction-conditions.md) can check the model against the declared system. ^perspective

- **Derived terms change only the *vocabulary* of a model.** A derived term is *defined* from the declared terms. Such a term can be eliminated by substituting its definition, so it proves no new claim about the declared terms [gupta2023]. A *law stated in derived terms*, in contrast, may require a proof. When that proof holds only in a limit or under specific assumptions, each such restriction is recorded as an assumption of that law, which an answer classifies relative to its target, as the [rule on idealizations](answer-form.md#^idealizations) states. ^derived-terms

- **A map from the target defines; a binding asserts.** A map from the declarations of the target defines a bearer or a term of the model, so it cannot be false of the target. The claim that a value of the model matches a value of the target, by contrast, can be false. Such a claim is a surrogative inference from the model to the target, so a binding states it, and a model never enters a quantity of its target by reference. A reference would assert an identity, and a model never stands in an identity with its target. Three consequences follow. First, a map is never the identity, since an identity map would enter a target quantity by reference under another name. Second, a map that both defines a bearer of the model and links the model to the target is stated once, in the model, and the key of a binding that uses it references that definition. Third, a law of the model stated over a mapped term can be false of the target, although the map that defines the term cannot: such a law reaches the target only through a binding, unless it is derived from the laws admitted about the target. ^map-versus-binding

- **A model derived from another model names its parent.** A reduced model, a limit model or a model corrected by de-idealization is derived from a parent model. The typing of the operations that derive it remains open, under the goal `model-design` of the [project goals](../../TODO.md). ^model-parents

- **A family of models can ground one answer.** Several models then ground the claim together, each with its own binding. The family is assessed as a whole: the [robustness test](satisfaction-conditions.md) asks whether the claim holds across its members, which is the form of robustness analysis [weisberg2006]. The answer also declares how the fidelity of the family is judged: by one comparison per member, each of which must pass, or by one comparison of the ensemble of the family. ^model-family

## The binding record

A binding relates a model in use to a phenomenon, or to its data, and records the surrogative inferences from the model to the target that its asserter licenses [suarez2004]. The binding denotes the phenomenon, pairs a feature that the model exemplifies with a feature imputed to the target, and states the key that carries the one onto the other [friggnguyen2020]. Each binding therefore records the inferences that it licenses, and stays neutral between the theories of what makes a model represent. Similarity holds in respects and to degrees fixed by a purpose [giere2004] [weisberg2013], so the pairs of a binding state those respects, and the tolerance of the question states those degrees. ^binding-record

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Model — the model in use | always | the identifier of one model record | the rate model of an excitatory and an inhibitory population |
| Target — the denotation of the phenomenon, and the level at which the model is compared | always | the identifier of one phenomenon, and the target level: `phenomenon`, when the model is compared with the explanandum variables that the phenomenon estimates; `data`, when it is compared with a version of the data through an observation operator | the gamma oscillations of the network (phenomenon); the recorded local field potentials, version 3 (data) |
| Asserter — the agent who licenses the inferences | always | a person, a group or a publication | the authors of the answer; the publication that proposed the model |
| Feature pairs | always | per pair, a feature that the model exemplifies and the feature of the target to which it is imputed, typed: `quantity` · `pattern` · `regime` · `invariance-class` (an invariance or a universality class) · `modal-profile` · `component` (a unit of the model and the constituent or the admissible part of the target that it denotes); the [mode](#^pair-modes) of the pair, `computed` or `argued`; and, for a computed pair, the key that carries the one onto the other | the model frequency and the peak of the measured spectrum (quantity); the oscillating regime of the model and the synchronous regime of the network (regime); the scaling exponents shared by a universality class (invariance class) |
| Condition pairs | when a condition of the model is set to stand for a condition of the target | per pair, a condition of the model, the condition of the target that it stands for, and the key; a parameter fitted to the data is marked as a *calibration parameter* | the external drive of the model and the stimulus contrast; the coupling strength (calibration parameter) |
| Domain of comparison | always | the conditions of the target over which the pairs are asserted, each region marked as *interpolation*, within the range of the calibration data, or *extrapolation*, outside it | contrasts from 10 % to 80 % (interpolation); a contrast of 100 % (extrapolation) |
| Structural discrepancy | when the grain is quantitative | the model of the systematic difference between the output of the model at its best parameters and the value of the target, or a stated bound on it [kennedyohagan2001]; a discrepancy model fitted to data counts as calibration on those data, and the calibration provenance records it | a Gaussian process over the contrast; a bound of 5 Hz on the frequency |
| Calibration provenance | when a pair carries a calibration parameter | per calibration parameter, the version of the data that fitted it, the method of fitting, and whether the parameter is identifiable under the structural discrepancy [brynjarsdottir2014] | the coupling strength, fitted by least squares to the session of day 1, not identifiable apart from the discrepancy |
| Grain | always | `quantitative`, when the pairs are compared by a metric · `qualitative`, when they are compared by a match of patterns or regimes | — |
| Version | always | a version identifier, and the time at which the binding was committed | version 2, committed before the recordings of version 3 |

- **The binding belongs to neither the model nor the answer.** One model grounds several answers, so a binding owned by an answer would be repeated across every answer that shares the model, together with its keys. The binding therefore stands between the model and the phenomenon, and an answer cites the binding through which its claim bears on the target. ^binding-owner

- **A feature pair is computed or argued.** A pair is *computed* when a key maps the feature of the model onto a value or a label that the data of the target determine, as for a quantity, a pattern or a regime. A pair is *argued* when no data determine it, as for the membership of the target in a universality class, argued from its symmetries and its dimension, or for a modal profile. An argued pair cites its argument as a ground of the answer with the role `warrant`, and the law-warrant test judges that ground. The comparison reports an argued pair without computing it. ^pair-modes

- **A unit of the model alone reaches the target through a pair of type `component`.** A unit defined by a stated map from the declared constituents cannot be false of the target, so it needs no pair. A unit of the model alone, such as a box that stands for a subsystem in a stylized model, has no such map. The claim that this unit stands for a constituent of the target, or for a part that the [admissible explanans](admissible-explanans.md) admits, is a localization, and a localization can fail [bechtel1993]. A binding therefore states that claim as a pair of type `component`, argued from evidence of localization, such as the mutual manipulability of the unit and the part [craver2007]. The [explanatory mapping](definitions/regularities/mechanism-and-mechanistic-model.md#^mechanistic-model-test) of a mechanistic model reads these pairs, since a model explains in the how-actually sense only when its components correspond to parts of the target [kaplan2011]. ^component-pairs

- **The discrepancy has three owners.** The structural discrepancy belongs to the binding, since it describes how the model departs from the target. The observation error belongs to the data, so the [phenomenon](phenomenon.md#^data-model-declarations) declares it. The tolerance belongs to the question, through the [required accuracy](epistemic-task.md) of its task [kennedyohagan2001] [brynjarsdottir2014]. ^discrepancy-owners

- **A calibration parameter states whether the data identify it.** When the structural discrepancy is ignored, a calibrated parameter can absorb the discrepancy and take a value without physical meaning [brynjarsdottir2014]. The calibration provenance therefore states, per parameter, whether the parameter is identifiable apart from the discrepancy. ^calibration-provenance

- **A revised binding is a new version.** A change of a pair, a key, the domain or the discrepancy creates a new version with its own time of commitment. The earlier version, and every comparison computed from it, stays unchanged, so that a reader can tell a binding fixed before the data from a binding adjusted to them. A version of the data whose comparison motivated the revision counts as calibration data for the new version. A comparison of the new version with those data therefore reports its [calibration treatment](#^comparison-reports), as for any data used to fit a parameter. ^binding-version

## The key record

A key states one map between the two sides of a binding: an observation operator, a map of units, a map of aggregation, or a qualitative abstraction. Several bindings use the same observation operator or the same map of units, so a key is a record of its own, which those bindings reference by identifier and version. A key carries a version because a measurement outcome is itself inferred through a model, which can be revised [tal2013] [parker2017]. ^key-record

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Kind | always | `observation-operator` · `unit-map` · `aggregation-map` · `qualitative-abstraction` | the forward model from population rates to a local field potential (observation operator); the conversion of the dimensionless time of a model to seconds (unit map) |
| Domain and codomain | always | the side of the model and the side of the target that the key connects, each as a set expression or a type | from the rates of two populations to one potential; from trajectories to the labels `oscillating` and `silent` |
| Expression | always | an expression over the symbols of its domain, or a pointer to the procedure that computes the map | the mean over the neurons of a population; a threshold on the power in the gamma band |
| Version | always | a version identifier | version 1 |

## The computed comparison

A comparison is computed, not recorded. Its inputs are a binding at one version, a version of the data, and the metric and the tolerance that the [required accuracy](epistemic-task.md) of the question fixes, together with the observation error that the phenomenon declares. Its output states, per computed feature pair of the binding, the difference between the model and the target, and whether that difference lies within the tolerance once the observation error is accounted for. The output also reports the structural discrepancy that the binding declares for the pair. A declared discrepancy that exceeds the tolerance fails the pair, so a binding cannot pass a pair by declaring a discrepancy wider than the question tolerates. A discrepancy model fitted to the compared data counts as calibration on those data [kennedyohagan2001] [brynjarsdottir2014], and the calibration treatment then governs those data. ^comparison

Each comparison also reports three facts about its own conditions: ^comparison-reports

- **commitment**: whether the binding was committed before the version of the data;
- **calibration treatment**: how the comparison treated the data already used to fit a calibration parameter: `excluded`, `cross-validated`, `bayesian`, or `reused` when the data are compared again without any correction. Using calibration data for confirmation is legitimate or not depending on the method [steelewerndl2013], so the treatment is reported rather than assumed, and the [rules on the reports](satisfaction-conditions.md#^fidelity-reads-reports) state which treatments count;
- **circularity**: a flag raised when a model declared by the [data model of the phenomenon](phenomenon.md#^data-model-declarations) overlaps with the model or the grounds of the answer, or with a key of the binding, since an observation operator can contain the model under test. Data models can contain the models under test [bokulichparker2021], and a comparison that ignores the overlap can be circular.

- **The comparison is recomputed, never edited.** The inputs of a comparison fix its output, so an assessment that cites a comparison records only those inputs, and any reader recomputes the same output. A revised binding or a new version of the data yields a new comparison, and the earlier comparisons stay as they were. ^comparison-recomputed

- **Adequacy is relative to a purpose.** A comparison judges the model for the purpose that the question states through its feature pairs and its tolerance, not in general [parker2020]. A model adequate for one question can therefore fail for another question about the same phenomenon. ^adequacy-for-purpose

---
## Sources

> [!NOTE] Status of the claims
> - **Established:** the inferential view of representation, the vocabulary of denotation, exemplification, key and imputation, the separation of structural discrepancy from observation error, and the dependence of data on models, as cited.
> - **Proposals:**
> 	- the division into four records, with the model, the binding and the key shared by several answers;
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

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks).

- [bechtel1993] ◐ [Bechtel & Richardson, _Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research_, Princeton UP 1993; MIT Press 2010](https://direct.mit.edu/books/monograph/2860/Discovering-ComplexityDecomposition-and)
- [bokulichparker2021] ◐ Bokulich & Parker, "Data models, representation and adequacy-for-purpose", *European Journal for Philosophy of Science* 11, 31, 2021
- [brynjarsdottir2014] ◐ Brynjarsdóttir & O'Hagan, "Learning about physical parameters: the importance of model discrepancy", *Inverse Problems* 30, 114007, 2014
- [craver2007] ◐ [Craver, *Explaining the Brain*, OUP, 2007](https://philpapers.org/rec/CRAETB-2)
- [friggnguyen2020] ◐ Frigg & Nguyen, *Modelling Nature: An Opinionated Introduction to Scientific Representation*, Springer, 2020; denotation, exemplification, key and imputation
- [giere2004] ◐ Giere, "How models are used to represent reality", *Philosophy of Science* 71(5), 742–752, 2004
- [gupta2023] ✓ [Gupta & Mackereth, "Definitions", _SEP_, revised 2023](https://plato.stanford.edu/entries/definitions/), §2.3 on conservativeness and eliminability
- [kaplan2011] ◐ [Kaplan & Craver, "The explanatory force of dynamical and mathematical models in neuroscience: a mechanistic perspective", *Philosophy of Science* 78(4), 601–627, 2011](https://doi.org/10.1086/661755); the model-to-mechanism-mapping requirement, checked through the abstract
- [kennedyohagan2001] ◐ Kennedy & O'Hagan, "Bayesian calibration of computer models", *Journal of the Royal Statistical Society B* 63(3), 425–464, 2001
- [massimi2022] ◐ [Massimi, _Perspectival Realism_, OUP, 2022](https://academic.oup.com/book/43074)
- [parker2017] ◐ Parker, "Computer simulation, measurement, and data assimilation", *British Journal for the Philosophy of Science* 68(1), 273–304, 2017
- [parker2020] ◐ Parker, "Model evaluation: an adequacy-for-purpose view", *Philosophy of Science* 87(3), 457–477, 2020
- [steelewerndl2013] ◐ Steele & Werndl, "Climate models, calibration, and confirmation", *British Journal for the Philosophy of Science* 64(3), 609–635, 2013
- [suarez2004] ◐ Suárez, "An inferential conception of scientific representation", *Philosophy of Science* 71(5), 767–779, 2004
- [tal2013] ◐ Tal, "Old and new problems in philosophy of measurement", *Philosophy Compass* 8(12), 1159–1173, 2013
- [weisberg2006] ◐ [Weisberg, "Robustness analysis", _Philosophy of Science_ 73(5), 2006](https://philpapers.org/rec/MICRA)
- [weisberg2013] ◐ Weisberg, *Simulation and Similarity: Using Models to Understand the World*, Oxford University Press, 2013
- [wimsatt1994] ◐ [Wimsatt, "The ontology of complex systems: levels of organization, perspectives, and causal thickets", _Canadian Journal of Philosophy_ 24(sup1), 1994](https://www.tandfonline.com/doi/abs/10.1080/00455091.1994.10717400)
