---
tags:
  - audit
index: "[gnomon audits](docs/audits/_index.md)"
aliases:
  - Audit - Model design (F)
---
# Audit - Model design (F)

## Verdict

The diagnosis is correct and the direction is sound. The strategy as stated is not optimal on four points:

- The duplication that motivates it is a shared schema, and no content is duplicated, so the missing element is the *relation* between the two models. 
- The assumption types of the proposal cross two axes without naming them, and they mix motives with operations. 
- One relation that the fixtures need is absent from the list: a surrogate model that no operation on the target produces. 
- Exhibiting how the phenomenon arises requires a derivation object. The design plans that object and has not built it, and the explanans is its difference-making annotation.

The recommended form has four parts:

- one record kind for models, with the role fixed by reference;
- a derivation block organized by axes;
- an ownership rule fixing where an operation is recorded;
- one derivation record per answer.

## Diagnosis: a shared schema, and a missing relation

The answer template shares six declaration blocks with the target template by decision. The decision of 2026-09-24, recorded in the framework corrections handoff (`test/framework-corrections-handoff.md` at commit a4fb1b4), declares the model of an answer with the blocks of the target, and every reused quantity enters by reference. In the six filled answers, the shared blocks hold references and new declarations, and no law is restated. The single-source rule admits a shared schema. However, the records do not state the *operation* that produced each new declaration from the parent. The fixtures carry that operation in three scattered places:

- an expression on a derived quantity;
- a warrant of derivation in a limit on a law;
- an idealization stated in prose.

No field names the map from the quantities of the target to the quantities of the answer. No field names the regime of that map or its error either.

The six answers relate their model to the target as follows:

| Answer | Relation of its model to the target |
| --- | --- |
| Neural tangent theorem | the same model, extended by three bounds |
| Microbial theorem | the same model, restricted to one variant |
| Swift-Hohenberg catalogue | the same model, at the stationary states named by the question, with a finite numerical domain in the derivation |
| Active-matter catalogue | a linearization about a homogeneous state, with the noise dropped |
| Grokking account | a re-individuation into a representation, with a posited effective law |
| Tipping forecast | a stylized network of four elements standing in for the actual system |

Therefore, the relation recurs across the corpus and changes the admissible answers. These two properties are the grounds that the [shared field grounds](../adr/shared-field-grounds.md) decision requires of a new field. Of the five template defects recorded in the answer and assessment template issues (`test/answer-assessment-template-issues.md` at commit a4fb1b4), three follow from the missing relation:

- an answer cannot state its claim domain;
- nonexplanatory aims are forced into explanatory semantics;
- candidate values do not bind to the outputs of the phenomenon.

Each defect is repaired by one element of the missing relation:

1. a derived model has a reference class of its own, and that class is the claim domain;
2. a derivation from a model to a manifestation is the product of every aim, and only explanation annotates that derivation;
3. a derived phenomenon binds the values of the answer to the outputs.

Beyond the fixtures, a model as a record kind passes the [object-kind admission](../design/2-architecture/object-kinds.md) rule of the architecture, on all five of its conditions:

- an identity independent of any answer;
- reuse across answers and questions;
- a local validity condition, namely its regime;
- editability apart from any answer;
- no build from other records.

The target system is already such a model, as the [target system](../epistemology/target-system.md) note states after Elliott-Graves. Therefore, the change adds no kind: the target is the root model, and a derived model is a model with a parent.

## Comparison with standard notions

*Hierarchy of models.* Suppes' hierarchy runs from models of theory through models of experiment to models of data. Mayo elaborated that hierarchy into the standard account of how a theory meets its data through models. The framework already instantiates the hierarchy:

- the target record is the base model of the class;
- the phenomenon record is a model of data, in the sense of Bogen and Woodward;
- the question fixes the design;
- the answer supplies a model of the theory that reproduces the data model.

The proposal inserts intermediate models between the base and the answer. Theoretical physics commonly builds the same structure as a tower of effective models, from microscopic to mesoscopic to macroscopic, each derived from the level below by a stated reduction. Therefore, the design should admit chains: a model derived from a derived model, with the regimes intersected and the warrants propagated along the chain. The framework already propagates the warrant of a law to the results resting on it, so propagating along a chain extends a rule in place.

*Axes crossed by the proposed assumption types.* Norton separates an idealization from an approximation. An idealization is a new system whose properties approximate the target. An approximation is an inexact description of the same system. The [domain of conditions](../epistemology/domain.md) note already applies this separation, since a limit belongs to the subject only when the question concerns the limit system. The assumption types of the proposal cross this axis without naming it. Of those types, restriction, limit and selection act on the reference class. The remaining types act on the description. Jones and Cartwright add a second axis inside the description: abstraction omits without distorting, and idealization misrepresents. The current motive `isolation` covers both, so a robustness test cannot tell whether a removed factor was omitted or falsified. Weisberg's three kinds of idealization, from which the current motives derive, name the *reason* for a distortion. No field names the operation performed.

*Change of perspective is several operations.* An eigendecomposition changes coordinates exactly and invertibly. Such a change is conservative in the sense already used in the [answer form](../epistemology/answer-form.md) note after Gupta: no new claim about the old terms is proved in the new terms. By contrast, a mean-field reduction is a many-to-one projection followed by a closure, and the closure is a posited or derived law. A re-individuation of units in Bechtel's sense may be either. The two differ by information loss, because the individuation test applies only to a lossy map. Rubenstein's exact transformations, refined by Beckers and Halpern into a ladder of stricter abstractions, supply the consistency condition for a lossy map: the coarse model must agree with the fine one on the interventions represented by both. The framework already cites Rubenstein for aggregates, so the check for a lossy map is ready.

*Error control.* The practice of theoretical physics separates a controlled approximation from an uncontrolled one. A controlled approximation bounds its error by a function of a small parameter. An uncontrolled approximation, such as mean-field theory below its upper critical dimension, carries no such bound. The neural tangent fixture is controlled: every bound scales as the inverse square root of the width, uniformly over training time. Batterman's singular limits mark a reduced model with properties that no finite member has. Under a singular limit the approach to the limit is not uniform, and the result depends on the order of two limits. The phenomenon note already records the quenched-versus-annealed instance. Therefore, a derivation record must state its error class and, for two or more limits, their order. The robustness test can then discharge a controlled operation by its bound, and it can only flag an uncontrolled one.

*The surrogate relation.* The model of an answer is not always derived from the target. The tipping forecast uses a stylized network that stands in for the actual Earth system, and no operation on the declarations of the target produces that network. Three accounts describe a model that represents its target through a claimed correspondence, with no derivation:

- the multiple-models idealization of Weisberg;
- the mediating models of Morgan and Morrison;
- the minimal models of Batterman and Rice.

Frigg and Nguyen give the correspondence a structure: a key maps features of the model onto features imputed to the target. In physics, the Ising model stands in for a ferromagnet by a universality claim. Therefore, the derivation vocabulary needs a value for a posited correspondence, warranted by universality or by matching. The scope test then reads the class of the surrogate, and the fidelity test reads the correspondence. As evidence, the scope failure of the tipping assessment is the absence of exactly this field.

*How the phenomenon arises.* Under every aim except explanation, the phenomenon arises in a model when its manifestation is *derived* from the laws of the model. The derivation proceeds by proof, simulation or measurement, within the tolerance fixed by the question. In the semantic view, this derivability embeds a data model in a theoretical model. Under explanation, a derivation is insufficient, as the answer form note already states. Strevens' kairetic account supplies the missing structure. An explanation is a derivation from which every non-difference-making detail has been abstracted, and an idealization marks a factor shown by the derivation to make no difference. Therefore, the explanans of the current template is the difference-making annotation of a derivation, and the idealizations are its complement. The template lacks the derivation itself. That object is planned in the design tier and listed as unbuilt among the features of the README. Once that object exists, one structure serves every aim: the derivation carries its route and its warrant, and only under an explanatory aim does it carry factors and foils.

## Recommended form

**One kind for models, with two roles fixed by reference.** The target-system template gains two optional fields: the parent model, and a derivation block. A question references a model as its target. An answer references a model as its commitment. When an answer keeps the description of the target, it references the target directly, and no derived record is written. The phenomenon template gains the same two fields, and its derivations are operationalizations:

- a qualitative label parametrized by features;
- an observable pushed forward through an aggregation map;
- a change of grain or of scope.

A derived phenomenon must reference a derived system model, since the grain test requires its observables to be definable over the quantities of that model.

**A derivation block organized by axes.** Each entry of the block names:

- its kind;
- the parent symbols acted on;
- the symbols of this model that realize it;
- its regime;
- its error class;
- its warrant;
- for two or more limits, their order.

The kinds are fixed by the axes named in the comparison with standard notions. The corpus exhibits seven kinds at present:

| Kind | Acts on | Truth | Information | Error | Occurrence in the corpus |
| --- | --- | --- | --- | --- | --- |
| restrict | class | exact | none lost | exact | microbial, by the variant key |
| limit | class | new system | none lost | controlled or singular | neural tangent, limiting kernel; turbulence, on the question side |
| idealize | description | distorts | lost | uncontrolled unless bounded | active matter, noise dropped |
| aggregate | description | exact map, posited closure | lost | per closure | grokking |
| linearize | description | approximates | lost | controlled near the state | active matter |
| extend | description | adds a posited law or a definition | none lost | per warrant | grokking, effective law |
| surrogate | class and description | posited correspondence | not comparable | per fidelity | tipping |

A derived law is a consequence, recorded in a derivation, and no extension of the model. A kind enters the registry when a filled problem requires that kind, per the shared field grounds decision. The block restates no expression. The map of an aggregate stays on its variable, and the proof of a derived law stays in its derivation. An entry points to them, as an organization entry points to its realizing laws. The [single field per fact](../adr/single-field-per-fact.md) decision excludes a block restating them.

**An ownership rule for the position of an operation.** One entry shape serves three records, and the record that imposes an operation holds that operation:

- a selection on an outcome stays with the target;
- a restriction or a limit imposed by the question stays in its domain;
- every operation of the analysis lives in a derived model.

This rule keeps the layer order of the framework: the subject is fixed before any answer. The rule also settles the pending candidate on moving the domain beside the selection criteria: the two share a vocabulary and differ in owner. A root model records no idealization, because a distortion is defined relative to a parent description. The posited laws of a root model carry their warrant as they do now.

**One derivation record per answer.** The answer keeps its statement and its status, and it references a model of the system and a model of the phenomenon. The answer adds one derivation per manifestation:

- the laws and the operations used;
- the route, among the five evidence routes that the warrant tests already name;
- the warrant of the derivation;
- the manifestation reached.

Under an explanatory aim, each factor of the explanans annotates that derivation through the keys that it carries now: `bears_on`, `through` and `separates`. Realizations remain the mapping between two descriptions that a question about a link requests.

**Checks that the form makes possible.** Every new symbol of a derived model must carry one of three warrants of origin:

- a reference to its parent;
- an expression over parent symbols;
- an extension entry that introduces it.

Every lossy aggregation is held to the individuation test. The claim domain of an answer is computed as the reference class of its model, intersected with the regimes along its chain. The scope test then compares that domain with the domain of the question. Warrants propagate along the chain. The robustness test enumerates the uncontrolled operations as the operations that no bound discharges.

**Costs and dependencies.** Authoring cost rises only where an answer transforms its model, and there it replaces prose already written under idealizations. The checker must add the model kind to its declaring blocks. The checker must also follow the parent field when it collects the symbols reachable by a record. Three of the six fixtures transform the description of the target, so their declarations move into a derived model. The other three keep the target as their model, and their new quantities move to a derived phenomenon or to a derivation. Deviating from the handoff is justified by the handoff's own open items: the three template defects exposed by the trials follow from the missing relation, so repairing the answer template without recording the relation between models repairs symptoms.

**Refactoring updates.** Renaming the root kind from `target-system` to `model` changes every reference in the corpus and is editorial.

Sources:
- [Suppes 1962, Models of data](https://errorstatistics.com/wp-content/uploads/2016/12/suppes-p-1962-models-of-data.pdf)
- [Jones 2005, Idealization and abstraction: a framework](https://philpapers.org/s/Martin%20Jones)
- [Beckers and Halpern 2019, Abstracting causal models](https://arxiv.org/abs/1812.03789)
- [Strevens 2008, Depth](https://ndpr.nd.edu/news/depth-an-account-of-scientific-explanation/)
- [Nickles 1973, via the Stanford Encyclopedia entry on intertheory relations](https://plato.stanford.edu/archives/sum2020/entries/physics-interrelate)
- [Frigg and Nguyen, the DEKI account](https://link.springer.com/10.1007/s13194-017-0182-4)
- [Batterman and Rice 2014, Minimal model explanations](https://www.cambridge.org/core/product/640580F4EA5571EA1AA971C5DC063FA6)
- [Batterman, The Devil in the Details](https://academic.oup.com/book/10652/chapter/158683815)