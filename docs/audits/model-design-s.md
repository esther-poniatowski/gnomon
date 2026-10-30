---
tags:
  - audit
index: "[gnomon audits](docs/audits/_index.md)"
aliases:
  - Audit - Model design (S)
---
# Audit - Model design (S)

## Verdict

The proposed refactor is directionally correct. The duplicated fields express a genuine invariant: both the inquiry and its answer use models of the system. The current candidate-answer form (`docs/epistemology/objects/answer/answer-form.md`, line 25, at commit c9179ed) already recognizes that invariant.

The optimal architecture should therefore make models reusable and model transformations explicit. However, it should not make an answer model a simple extension of the initial target-system record. The stronger design is a **provenance graph of models connected by typed transformations**.

Three qualifications are essential:

- The target system and its model must remain distinct.
- Transformations, assumptions, restrictions, approximations, and idealizations must retain distinct semantics.
- “How the phenomenon arises” must become an aim-sensitive account relation. Explanatory production is only one possible relation.

## Evidence from the current framework

The proposed refactor explains several existing defects.

First, six blocks occur in both system and answer records: constituents, index sets, variables, parameters, laws, and organization. The duplication is structural, as shown by the system template (`src/gnomon/data/templates/target-system.yml`, line 25, at commit c9179ed) and answer template (`src/gnomon/data/templates/answer.yml`, line 14, at commit c9179ed).

Second, the current documentation already treats the answer as a model derived under constraints. Derived terms, changed bearers, and reduced models appear in the answer-model rules (`docs/epistemology/objects/answer/answer-form.md`, line 46, at commit c9179ed). What remains implicit is the transformation connecting the two model specifications.

Third, the phenomenon record already contains a model-like representation. Its observables map system states into explanandum variables, while manifestations state claims about those variables. Scope, evidence, and detection criteria complete the characterization. These functions appear in the phenomenon template (`src/gnomon/data/templates/phenomenon.yml`, line 23, at commit c9179ed).

Fourth, the active diagnosis identifies three defects that the refactor can solve directly:

- candidate answers lack an explicit claim domain;
- nonexplanatory aims are forced into `explanans.produces`;
- candidate values are not structurally bound to phenomenon outputs.

These defects are recorded in the answer-trial findings (`test/answer-assessment-template-issues.md`, line 27, at commit a4fb1b4). The proposed refactor therefore has priority over a local repair of the current answer template.

One inconsistency also confirms that the current boundary has become unstable. The answer documentation says that law warrants belong only to answers, but the target template and target documentation now assign warrants to target laws. Compare the answer claim (`docs/epistemology/objects/answer/answer-form.md`, line 56, at commit c9179ed) with the target-law fields (`src/gnomon/data/templates/target-system.yml`, line 69, at commit c9179ed).

## Recommended architecture

The central structure should be:

```
inquiry
├── initial system model
├── initial phenomenon model
└── epistemic task

answer
├── answer system model
├── answer phenomenon model
├── transformations from prior models
└── aim-sensitive account
```

The corresponding records should have separate responsibilities.

|Record|Responsibility|
|---|---|
|`target`|Identifies the represented system or reference class and its selection conditions.|
|`system-model`|Declares constituents, quantities, laws, organization, boundaries, and warrants.|
|`phenomenon`|Identifies the phenomenon whose characterization may change across models.|
|`phenomenon-model`|Declares observables, manifestations, scope, evidence, and detection criteria.|
|`model-transformation`|Records how one or more source models produce a destination model.|
|`answer`|References the selected models and states the epistemic product and its support.|
|`assessment`|Tests the answer against the inquiry and the obligations introduced by its transformations.|

The existing `target-system` record could initially remain intact for compatibility. Conceptually, however, it combines a target specification with an initial system model. The relation between them should eventually become explicit as `represents`.

This separation agrees with the DDI account of modeling. That account distinguishes denotation of the physical target, demonstration within the model, and interpretation of the derived result [Hughes’s DDI account](https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/models-and-representation/F842E4D23AD3A703F2FDBDAC03F83838).

## Transformations instead of inheritance

A simple parent–child inheritance mechanism would be too restrictive. Scientific models can draw on several sources: an initial description, a general theory, empirical calibration, and an independently developed effective model. Models also have partial autonomy from both theories and targets [models as mediators](https://www.cambridge.org/core/books/abs/models-as-mediators/models-as-mediating-instruments/10737C6DD4744A65E4B5B89B3D489B21).

Each derived model should therefore name one or more parents. Its content should consist of explicit operations. An evaluator can then materialize the complete model without duplicating unchanged declarations.

The operation vocabulary should distinguish at least these families:

|Operation|Epistemic effect|Required check|
|---|---|---|
|Rename, reparameterize, change coordinates|Preserves represented structure|Equivalence or invertibility|
|Define a derived quantity|Conservatively extends the vocabulary|Eliminability through substitution|
|Restrict the domain or select a submodel|Narrows the claim scope|Explicit inclusion map and scope|
|Add a law or constituent|Increases model commitments|Derivation, measurement, fit, or other warrant|
|Approximate or truncate|Introduces quantitative error|Error estimate and validity regime|
|Idealize|Replaces the target description with a deliberate distortion|Robustness or de-idealization test|
|Coarse-grain or aggregate|Removes degrees of freedom|Closure and cross-level consistency|
|Compose models|Joins independently specified systems|Interface and symbol compatibility|

This taxonomy matters in theoretical physics. A full eigendecomposition is normally an invertible coordinate change. A truncated eigendecomposition is a projection and approximation. A mean-field reduction usually combines aggregation, a closure assumption, and either a limit or approximation.

Likewise, Kadanoff’s block-spin construction replaces microscopic spins with collective variables [Kadanoff 1966](https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263). Such an operation loses information and requires a regime-specific justification. It cannot be represented adequately as an untyped “change of perspective.”

Causal models impose a stronger obligation. A microscopic-to-macroscopic map must preserve the interventions represented at both levels [causal consistency](https://is.mpg.de/ei/publications/rubensteinetal17). The current individuation test (`docs/epistemology/objects/answer/satisfaction-conditions.md`, line 40, at commit c9179ed) already anticipates this requirement.

## Assumptions require several homes

The proposed generalization of idealizations identifies a real commonality, but one generic `assumptions` block would erase important distinctions.

The framework should separate:

- **model commitments**, including posited, fitted, measured, and derived laws;
- **scope restrictions**, including the domain of the question and a theorem’s validity regime;
- **selection criteria**, which determine membership in the reference class;
- **transformation premises**, such as closure or scale-separation assumptions;
- **idealizations**, which deliberately distort the represented system;
- **approximations**, which describe the same target inexactly;
- **correspondence assumptions**, which connect model quantities with target or phenomenon quantities.

This distinction follows a standard epistemological boundary. An approximation is an inexact description, whereas an idealization introduces another system that supplies such a description [Norton’s analysis](https://sites.pitt.edu/~jdnorton/homepage/research/Ideal_Approx.html). The current framework correctly distinguishes domain restrictions from analysis idealizations in the domain specification (`docs/epistemology/objects/subject/domain.md`, line 31, at commit c9179ed); the refactor should preserve that result.

## Phenomenon models

A phenomenon and a phenomenon model should also remain distinct. Phenomena are supported by data, but they are not identical with those data [Bogen and Woodward](https://fitelson.org/woodward/bogen.pdf).

An initial phenomenon model may state a qualitative manifestation. A later model may then:

- operationalize it through a measurable observable;
- refine its grain or scope;
- introduce quantitative features;
- replace a label with a functional dependence;
- assign predicted or derived values;
- reject the initial characterization.

These changes should create another phenomenon model connected by typed operations. They should not mutate the initial phenomenon silently.

The phenomenon model should reuse generic components such as quantities, expressions, claims, scopes, and warrants. It should not reuse the entire system-model schema. A phenomenon model has no independent dynamics unless the inquiry explicitly models the phenomenon as a system.

## Accounting for the phenomenon

The universal relation should be called `accounts_for`, `supports`, or `connects_to`. Calling it “arises from” would impose explanatory semantics on description, prediction, and exploration.

A common account entry should name:

- the model result;
- the phenomenon manifestation or observable;
- the relation between them;
- the derivation, simulation, measurement, or fit supporting that relation;
- its scope, modal strength, and required accuracy.

The epistemic aim should then specialize the relation:

|Aim|Appropriate relation|
|---|---|
|Description|characterizes or assigns a value|
|Exploration|detects, classifies, or catalogues|
|Prediction|predicts a value or distribution|
|Explanation|identifies difference-makers and their path to the phenomenon|
|Modal knowledge|entails, permits, or excludes|
|Model knowledge|derives a property of the model|

Under this design, `realizations` and `explanans` receive narrower roles.

- `realizations` becomes a transformation or correspondence between model vocabularies.
- `explanans` remains specific to explanatory answers.
- `through` should split into inferential dependencies, mechanistic paths, and correspondence mappings.
- `produces` should remain available only when production is the requested relation.

This division resolves the current pressure to describe catalogues, forecasts, and theorems as explanantia.

## Recommendation for the handoff

The direct repair of the answer template should pause. The new architecture subsumes three of the five active answer defects and changes the object being repaired. The validation-pipeline gap and the assessment-gate gap remain independent tasks.

The smallest reliable design test would apply the architecture to three contrasting cases:

1. The neural-tangent theorem tests derivation and output assignment without explanatory production.
2. The grokking case tests re-individuation, derived variables, and an explanatory path.
3. The active-matter case tests exploration, partial scope, and a catalogue produced under idealizations.

A design that represents all three without unused compulsory blocks is a strong candidate for ratification. Model transformations should then be tested for composition, reversibility, information loss, and propagated scope before any corpus migration begins.
