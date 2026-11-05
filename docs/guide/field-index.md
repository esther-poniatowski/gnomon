---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Field index
---
# Field index

Looks up each field of each record by its path, with its title, its description and the row of the specification that documents it.

> [!IMPORTANT] Generated file
> `gnomon schemas` writes this index from the base schemas and the specification notes. Edit a schema or a note, not this file. A path marks the entries of a list with `[]`, and a field without a row of its own links to the row of its parent.

## `answer`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `abstractions` | Abstractions | per factor, the factor left out | [Abstractions](../specification/answer.md) |
| `abstractions[].factor` | Factor | The factor of the record. | [Abstractions](../specification/answer.md) |
| `abstractions[].id` | Id | The id of the record. | [Abstractions](../specification/answer.md) |
| `aim_block` | Aim block | the block of the aim of the question | [Aim block](../specification/answer.md) |
| `aim_block.description` | `description` | The `description` of the record. | [description](../specification/answer.md) |
| `aim_block.description.values` | Values | one entry per observable or feature that the request covers, per source of variation | [description](../specification/answer.md) |
| `aim_block.description.values[].across` | Across | the source of variation of the phenomenon whose quantification the value takes; omit for a single instance | [description](../specification/answer.md) |
| `aim_block.description.values[].data_version` | Data version | for a value that the estimator of the phenomenon computes: the version of the data on which it runs | [description](../specification/answer.md) |
| `aim_block.description.values[].of` | Of | The of of the record. | [description](../specification/answer.md) |
| `aim_block.description.values[].value` | Value | only for a characterization that no estimator computes | [description](../specification/answer.md) |
| `aim_block.explanation` | `explanation` | The `explanation` of the record. | [explanation](../specification/answer.md) |
| `aim_block.explanation.contrastive_explanandum` | Contrastive explanandum | the fact and the foils that the explanation separates, read from the contrast of the question, or the fact alone when its locus is `none` | [Contrastive explanandum](../specification/answer.md) |
| `aim_block.explanation.explanatory_claim` | Explanatory claim | the claim that named dependences of the core are explanatory: they make the difference between the fact and its foils, or they make the fact arise | [Explanatory claim](../specification/answer.md) |
| `aim_block.explanation.explanatory_claim[].determinant` | Determinant | The determinant of the record. | [Explanatory claim](../specification/answer.md) |
| `aim_block.explanation.explanatory_claim[].explanatory` | Explanatory | false for a dependence that the explanation declares not explanatory | [Explanatory claim](../specification/answer.md) |
| `aim_block.explanation.explanatory_claim[].ground` | Ground | the ground on which the claim depends | [Explanatory claim](../specification/answer.md) |
| `aim_block.explanation.factors` | Factors $E$ | per factor, its claim: a *condition* on a quantity, a *property* of a structure or of a law, or a feature of the *organization*; the element on which it bears; the laws and relations that carry its effect; the explanandum variable or manifestation that it accounts for; the foils that it rules out; the external systems on which it draws; and, in `procedure`, only the steps that the chain from the factor to the phenomenon leaves unstated | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].appeals_to` | Appeals to | external systems drawn on, by declared symbol; empty when none | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].bears_on` | Bears on | elements the factor applies to as a property or condition; one entry per element, so a family spans several entries | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].caveat` | Caveat | The caveat of the record. | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].factor` | Factor | The factor of the record. | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].holds` | Holds | empty while the claim is unformalized, with a caveat naming the gap | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].id` | Id | The id of the record. | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].name` | Name | The name of the record. | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].pair` | Pair | the feature pair of the binding that carries the status; omit when the route runs on the target | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].procedure` | Procedure | only content beyond the chain `bears_on`, `through`, `produces` | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].produces` | Produces | explanandum variable or manifestation the factor accounts for | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].separates` | Separates | foils ruled out, by their symbols in the foil set; empty where the contrast has no locus | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].target_status` | target status | `denoting` · `coarse-graining` · `limit-construct` · `structural-constraint`, as the target status of a factor states; not applicable under a declared use | [Factors: target status](../specification/answer.md) |
| `aim_block.explanation.factors[].through` | Through | laws and relations carrying the effect from `bears_on` to the explanandum | [Factors](../specification/answer.md) |
| `aim_block.explanation.factors[].under` | Under | the transformation group of an invariance stated by `holds`; omit for any other claim | [Factors](../specification/answer.md) |
| `aim_block.explanation.relation` | Relation | the type of the relation, one of the requested relations | [Relation](../specification/answer.md) |
| `aim_block.exploration` | `exploration` | The `exploration` of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.classes` | Classes | one entry per class found | [exploration](../specification/answer.md) |
| `aim_block.exploration.classes[].detection` | Detection | the result of the detection criterion of the phenomenon | [exploration](../specification/answer.md) |
| `aim_block.exploration.classes[].id` | Id | The id of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.classes[].pattern` | Pattern | The pattern of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.classes[].reading` | Reading | The reading of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.criterion` | Criterion | the equivalence criterion that partitions the space | [exploration](../specification/answer.md) |
| `aim_block.exploration.criterion.expression` | Expression | The expression of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.criterion.origin` | Origin | The origin of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.criterion.reading` | Reading | The reading of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.space` | Space | the observables and the varied factors | [exploration](../specification/answer.md) |
| `aim_block.exploration.space.observables` | Observables | of the phenomenon | [exploration](../specification/answer.md) |
| `aim_block.exploration.space.origin` | Origin | The origin of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.space.varied` | Varied | The varied of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.space.varied[].factor` | Factor | The factor of the record. | [exploration](../specification/answer.md) |
| `aim_block.exploration.space.varied[].range` | Range | The range of the record. | [exploration](../specification/answer.md) |
| `aim_block.modal_knowledge` | `modal-knowledge` | The `modal-knowledge` of the record. | [modal-knowledge](../specification/answer.md) |
| `aim_block.modal_knowledge.modality` | Modality | The modality of the record. | [modal-knowledge](../specification/answer.md) |
| `aim_block.modal_knowledge.proof` | Proof | for an impossibility or a necessity | [modal-knowledge](../specification/answer.md) |
| `aim_block.modal_knowledge.property` | Property | the property that the modal claim bears on | [modal-knowledge](../specification/answer.md) |
| `aim_block.modal_knowledge.space` | Space | The space of the record. | [modal-knowledge](../specification/answer.md) |
| `aim_block.modal_knowledge.witness` | Witness | for a possibility: the instance that witnesses it, such as a model | [modal-knowledge](../specification/answer.md) |
| `aim_block.model_properties` | `model-properties` | The `model-properties` of the record. | [model-properties](../specification/answer.md) |
| `aim_block.model_properties.discharges` | Discharges | the proof obligations of the question that the consequence discharges, by name | [model-properties](../specification/answer.md) |
| `aim_block.model_properties.form` | Form | The form of the record. | [model-properties](../specification/answer.md) |
| `aim_block.prediction` | `prediction` | The `prediction` of the record. | [prediction](../specification/answer.md) |
| `aim_block.prediction.outputs` | Outputs | one entry per predicted output | [prediction](../specification/answer.md) |
| `aim_block.prediction.outputs[].condition` | Condition | the condition of the target under which the output is predicted | [prediction](../specification/answer.md) |
| `aim_block.prediction.outputs[].target` | Target | one of the outputs to match that the required accuracy of the question names | [prediction](../specification/answer.md) |
| `aim_block.prediction.outputs[].value` | Value | a value or a distribution | [prediction](../specification/answer.md) |
| `answers` | Answers | The answers of the record. | — |
| `binding` | Binding | the record through which the claim bears on the target per model, the identifier and the version of one binding of that model to the phenomenon of the question | [Binding](../specification/answer.md) |
| `binding[].record` | Record | The record of the record. | [Binding](../specification/answer.md) |
| `binding[].version` | Version | The version of the record. | [Binding](../specification/answer.md) |
| `claim` | Claim | "[the claim of the answer]", as a reading, and, once formalized, an expression over declared symbols | [Claim](../specification/answer.md) |
| `claim.caveat` | Caveat | The caveat of the record. | [Claim](../specification/answer.md) |
| `claim.expression` | Expression | empty while the claim is not formalized, with a caveat naming the gap | [Claim](../specification/answer.md) |
| `claim.interventions` | Interventions | For a counterfactual claim, the admissible interventions, each named by an experiment or a simulation run whose protocol states it, or by the parameter or the variable of a model that it sets; naming them marks the claim as counterfactual. | [Claim](../specification/answer.md) |
| `claim.presuppositions` | Presuppositions | optional; one entry per commitment that the claim takes for granted beyond the presuppositions of its question and the existence that the conditions of its quantities presuppose | [Claim](../specification/answer.md) |
| `claim.presuppositions[].expression` | Expression | The presupposition in the expression syntax, over declared symbols. | [Claim](../specification/answer.md) |
| `claim.presuppositions[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes the presupposition; empty while it is undischarged. A presupposition that another answer establishes is a relation `presupposes` to that answer. | [Claim](../specification/answer.md) |
| `claim.presuppositions[].id` | Id | A descriptive identifier of the presupposition, unique within the record. | [Claim](../specification/answer.md) |
| `claim.presuppositions[].reading` | Reading | The commitment that the claim and every other direct answer of its question take for granted. | [Claim](../specification/answer.md) |
| `claim.reading` | Reading | The reading of the record. | [Claim](../specification/answer.md) |
| `claim.realizations` | Realizations | fill when the question bounds the explanans to the link between two substrates; one entry per role | [Claim](../specification/answer.md) |
| `claim.realizations[].by` | By | The by of the record. | [Claim](../specification/answer.md) |
| `claim.realizations[].id` | Id | The id of the record. | [Claim](../specification/answer.md) |
| `claim.realizations[].reading` | Reading | only content beyond the expression of `by` | [Claim](../specification/answer.md) |
| `claim.realizations[].realizes` | Realizes | a role, declared by the model independently of any substrate | [Claim](../specification/answer.md) |
| `dependence` | Dependence | how the claim depends on its grounds per entry, a minimal set of grounds that suffices for the claim; the result of a sensitivity analysis over one ground [saltelli2008]; or the result of a robustness analysis across models that share the claimed structure [weisberg2006] | [Dependence](../specification/answer.md) |
| `dependence[].grounds` | Grounds | grounds of this answer, by identifier | [Dependence](../specification/answer.md) |
| `dependence[].kind` | Kind | The kind of the record. | [Dependence](../specification/answer.md) |
| `dependence[].models` | Models | robustness only: the models compared | [Dependence](../specification/answer.md) |
| `dependence[].result` | Result | omit for a minimal sufficient set | [Dependence](../specification/answer.md) |
| `domain` | Domain | the systems and the conditions over which the claim holds | [Domain](../specification/answer.md) |
| `erotetic_relation` | Erotetic relation | how the answer stands to its question `complete` · `partial` · `corrective` · `reformulating`, with the presupposition that a corrective answer denies, or the revised question that a reformulating answer answers | [Erotetic relation](../specification/answer.md) |
| `erotetic_relation.denies` | Denies | corrective only | [Erotetic relation](../specification/answer.md) |
| `erotetic_relation.revised_question` | Revised question | reformulating only: the question that the answer answers and is assessed against | [Erotetic relation](../specification/answer.md) |
| `erotetic_relation.value` | Value | The value of the record. | [Erotetic relation](../specification/answer.md) |
| `grounds` | Grounds | what the claim depends on per ground, its content, its *role*: `assumption` · `idealization` · `condition` · `datum` · `warrant` · `criterion`, and the record that holds it. A ground with the role `idealization` also states the distortion that it introduces, its motive (tractability, isolation or limit), the gain that it provides, the range over which it holds, and whether it is removable (controlled, ineliminable or unknown) | [Grounds](../specification/answer.md) |
| `grounds[].content` | Content | The content of the record. | [Grounds](../specification/answer.md) |
| `grounds[].distortion` | Distortion | idealization only, as are the four keys below | [Grounds](../specification/answer.md) |
| `grounds[].gain` | Gain | The gain of the record. | [Grounds](../specification/answer.md) |
| `grounds[].id` | Id | The id of the record. | [Grounds](../specification/answer.md) |
| `grounds[].motive` | Motive | The motive of the record. | [Grounds](../specification/answer.md) |
| `grounds[].range` | Range | The range of the record. | [Grounds](../specification/answer.md) |
| `grounds[].record` | Record | the record or the unit that holds the ground: a law of the model or of the background, or an argued pair of a binding, for a warrant; a restriction of the domain; a criterion of the question; a phenomenon for a datum | [Grounds](../specification/answer.md) |
| `grounds[].removable` | Removable | The removable of the record. | [Grounds](../specification/answer.md) |
| `grounds[].role` | Role | The role of the record. | [Grounds](../specification/answer.md) |
| `grounds[].version` | Version | datum only: the version of the data | [Grounds](../specification/answer.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; a specification left out is provisional | [Maturity of a field](../specification/maturity.md) |
| `modal_strength` | Modal strength | the strength that the answer claims actual · possible · necessary | [Modal strength](../specification/answer.md) |
| `relations` | Relations | the links to other answers per link, the other answer and the relation: `supports` · `presupposes` · `tests` · `defeats` · `revises` | [Relations](../specification/answer.md) |
| `relations[].answer` | Answer | The answer of the record. | [Relations](../specification/answer.md) |
| `relations[].relation` | Relation | The relation of the record. | [Relations](../specification/answer.md) |
| `route` | Route | `derivation` · `proof` · `simulation` · `estimation` · `measurement`, the records on which it runs (the target, one model, or a family of models), and a pointer to the derivation, the code or the data | [Route](../specification/answer.md) |
| `route.derivations` | Derivations | for a derivation or a proof; the derivation records on which the claim rests | [Route](../specification/answer.md) |
| `route.family_fidelity` | Family fidelity | fill for a family of models only | [Route](../specification/answer.md) |
| `route.kind` | Kind | The kind of the record. | [Route](../specification/answer.md) |
| `route.pointer` | Pointer | a pointer to the code, the data or a published derivation; a recorded derivation is named in `derivations`, and its internal steps stay in it | [Route](../specification/answer.md) |
| `route.runs_on` | Runs on | the target system, one model, or every model of a family, by identifier | [Route](../specification/answer.md) |
| `status` | Status | the attitude taken toward the answer entertained · hypothesized · accepted · retracted | [Status](../specification/answer.md) |
| `support` | Support | the kind of evidence for the answer as a whole unsupported · informal · formally-proven · empirically-supported | [Support](../specification/answer.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `uncertainty` | Uncertainty | the uncertainty of each value, as an interval, a distribution or a bound | [Uncertainty](../specification/answer.md) |
| `uncertainty[].expression` | Expression | The expression of the record. | [Uncertainty](../specification/answer.md) |
| `uncertainty[].form` | Form | The form of the record. | [Uncertainty](../specification/answer.md) |
| `uncertainty[].of` | Of | The of of the record. | [Uncertainty](../specification/answer.md) |
| `use` | Use | the purpose of an answer whose claim bears on no target a use such as `tool`, `proof-of-principle`, `conceptual-exploration` or `understanding`, with the property that the model must have for that use | [Use](../specification/answer.md) |
| `use.property` | Property | The property of the record. | [Use](../specification/answer.md) |
| `use.value` | Value | a new use enters the vocabulary registry first | [Use](../specification/answer.md) |
| `variant` | Variant | the variant of the target that the answer accounts for, and one further variant for each of its parts with a narrower scope | [Variant](../specification/answer.md) |

## `assessment`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `against` | Against | the record whose specifications fix which tests apply for an answer, the identifier of one question, or the revised question that a reformulating answer names; for a construct, the identifier of its problem | [Against](../specification/assessment.md) |
| `appraisal` | Appraisal | per virtue, the assessment of this answer, and the candidates over which it is preferred once they have been appraised | [Appraisal](../specification/assessment.md) |
| `appraisal[].assessment` | Assessment | The assessment of the record. | [Appraisal](../specification/assessment.md) |
| `appraisal[].preferred_over` | Preferred over | fill when other candidates have been assessed | [Appraisal](../specification/assessment.md) |
| `appraisal[].virtue` | Virtue | The virtue of the record. | [Appraisal](../specification/assessment.md) |
| `assesses` | Assesses | the candidate answer or the construct whose verdicts this record holds the identifier of one candidate answer, or of the record of a construct that a problem demands, such as a model | [Assesses](../specification/assessment.md) |
| `comparisons` | Comparisons | the inputs from which each comparison cited by a verdict is recomputed per comparison, the binding and its version, and the version of the data; the metric and the tolerance are read from the question | [Comparisons](../specification/assessment.md) |
| `comparisons[].binding` | Binding | The binding of the record. | [Comparisons](../specification/assessment.md) |
| `comparisons[].data_version` | Data version | the version of the data | [Comparisons](../specification/assessment.md) |
| `comparisons[].id` | Id | The id of the record. | [Comparisons](../specification/assessment.md) |
| `comparisons[].version` | Version | the version of the binding | [Comparisons](../specification/assessment.md) |
| `credence` | Credence | a number between 0 and 1, with the evidence and the prior from which it follows | [Credence](../specification/assessment.md) |
| `credence.basis` | basis | the evidence and the prior from which the value follows | [Credence: basis](../specification/assessment.md) |
| `credence.value` | value | a number between 0 and 1 | [Credence: value](../specification/assessment.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `obligations` | Obligations | per obligation, a verdict with the derivation or the counterexample that settles it | [Obligations](../specification/assessment.md) |
| `obligations[].derivation` | Derivation | The identifier of the derivation record that settles the obligation. | [Obligations](../specification/assessment.md) |
| `obligations[].evidence` | Evidence | The evidence of the record. | [Obligations](../specification/assessment.md) |
| `obligations[].verdict` | Verdict | The verdict of the record. | [Obligations](../specification/assessment.md) |
| `status` | Status | The status of the record. | — |
| `tests` | Tests | verdict: pending \| pass \| fail \| not-applicable | [Tests](../specification/assessment.md) |
| `tests.admissibility` | admissibility | per criterion of the tests of the core and of the tests of the block of the aim of the question, a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.admissible-explanans` | Admissible-explanans | block of an explanation | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.binding` | Binding | The binding of the record. | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.consequence` | Consequence | block of model properties | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.contrast` | Contrast | block of an explanation | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.grain` | Grain | The grain of the record. | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.individuation` | Individuation | The individuation of the record. | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.modal-strength` | Modal-strength | The modal-strength of the record. | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.outputs` | Outputs | block of a prediction | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.product` | Product | The product of the record. | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.relation` | Relation | block of an explanation | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.scope` | Scope | The scope of the record. | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.space` | Space | block of an exploration | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.target-status` | Target-status | block of an explanation | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.values` | Values | block of a description | [Tests: admissibility](../specification/assessment.md) |
| `tests.admissibility.witness-or-proof` | Witness-or-proof | block of modal knowledge | [Tests: admissibility](../specification/assessment.md) |
| `tests.constraints` | constraints | per constraint of the problem, its name and a verdict — pending · pass · fail · not-applicable — with the evidence that settles it | [Tests: constraints](../specification/assessment.md) |
| `tests.constraints[].constraint` | Constraint | The constraint of the record. | [Tests: constraints](../specification/assessment.md) |
| `tests.constraints[].evidence` | Evidence | The evidence of the record. | [Tests: constraints](../specification/assessment.md) |
| `tests.constraints[].verdict` | Verdict | The verdict of the record. | [Tests: constraints](../specification/assessment.md) |
| `tests.warrant` | warrant | per criterion of the warrant table, a verdict with the evidence that settles it | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.adequacy-to-use` | Adequacy-to-use | replaces fidelity for an answer that declares its use | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.closure` | Closure | The closure of the record. | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.fidelity` | Fidelity | name the comparisons that the verdict reads, and how each of their three reports bears on it | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.foil-evidence` | Foil-evidence | The foil-evidence of the record. | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.law-warrant` | Law-warrant | The law-warrant of the record. | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.phenomenon-established` | Phenomenon-established | The phenomenon-established of the record. | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.robustness` | Robustness | The robustness of the record. | [Tests: warrant](../specification/assessment.md) |
| `tests.warrant.selection` | Selection | The selection of the record. | [Tests: warrant](../specification/assessment.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `background`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `closure` | Closure (of the laws) | separates a formal target from an empirical one complete, for a formal target whose laws define the system · partial, for an empirical target that may admit a rule independent of them | [Closure (of the laws)](../specification/background.md) |
| `describes` | Describes | the target whose quantities the laws use the identifier of one target-system record | [Describes](../specification/background.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `laws` | Laws | known behaviors of the components or of the system an expression over the symbols that the target declares, with its signature and the places that the claim ranges over (one entry each, empty when the law concerns the system as a whole). Its warrant (derived from other admitted laws, in a limit or not, posited, fitted or measured), with its grounds. Its role, one of six:<br>- evolution: how the state changes along the course<br>- input-output: how one quantity is determined by others at the same point<br>- measurement: how an instrument registers the state<br>- state-constraint: which states may hold together, including at the start and at the boundary<br>- distribution: the law of a random quantity<br>- admissibility: a restriction on the parameters or on the forms that a member may take | [Laws](../specification/background.md) |
| `laws[].expression` | Expression | the claim of the law: the only part of the entry that can be false of the system | [Laws](../specification/background.md) |
| `laws[].name` | Name | The name of the record. | [Laws](../specification/background.md) |
| `laws[].origin` | origin | a pointer to the publication, the data set or the derivation from which the law is taken | [Laws: origin](../specification/background.md) |
| `laws[].range` | range | an expression over declared symbols that bounds the conditions under which the law is established | [Laws: range](../specification/background.md) |
| `laws[].reading` | Reading | The reading of the record. | [Laws](../specification/background.md) |
| `laws[].requires` | Requires | The units on which the law rests, each by its dotted identifier, an assumption or an operation of a model, a law of a background or of a model, or a posit or a consequence of a derivation; a law whose descent a derivation records leaves its premises to that derivation. | [Laws: requires](../specification/background.md) |
| `laws[].rests_on` | Rests on | What the warrant of the law refers to beyond the units that it requires, in words, such as a source or a data set. | [Laws](../specification/background.md) |
| `laws[].role` | Role | The role of the record. | [Laws](../specification/background.md) |
| `laws[].signature` | Signature | one entry per place of the claim; empty for a claim about the system as a whole | [Laws](../specification/background.md) |
| `laws[].symbol` | Symbol | The symbol of the record. | [Laws](../specification/background.md) |
| `laws[].variant` | Variant | variant of the target governed by the law; omit when the law governs every member | [Laws](../specification/background.md) |
| `laws[].warrant` | Warrant | The warrant of the record. | [Laws](../specification/background.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `organization` | Organization | per relation, its tuples and its laws. The tuples take the form `prod(source, reach)` or `subset(prod(source, reach), adjacency)`. A directed relation puts the reach last, and a joint one has three or more components. When the ends are laws, the relation names the laws that it orders, with the reach last | [Organization](../specification/background.md) |
| `organization[].among` | Among | for a relation among laws: the laws, reach last; fill exactly one of `relates` and `among` | [Organization](../specification/background.md) |
| `organization[].name` | Name | The name of the record. | [Organization](../specification/background.md) |
| `organization[].reading` | Reading | only content beyond the relation and the laws | [Organization](../specification/background.md) |
| `organization[].realized_by` | Realized by | laws stating a relation among parts; the parts are read from their expressions | [Organization](../specification/background.md) |
| `organization[].relates` | Relates | for a relation among parts: the connected tuples, reach last | [Organization](../specification/background.md) |
| `organization[].symbol` | Symbol | The symbol of the record. | [Organization](../specification/background.md) |
| `organization[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [Organization](../specification/background.md) |
| `status` | Status | The status of the record. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `binding`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `asserter` | Asserter | the agent who licenses the inferences a person, a group or a publication | [Asserter](../specification/binding.md) |
| `calibration_provenance` | Calibration provenance | per calibration parameter, the version of the data that fitted it, the method of fitting, and whether the parameter is identifiable under the structural discrepancy [brynjarsdottir2014] | [Calibration provenance](../specification/binding.md) |
| `calibration_provenance[].data_version` | Data version | the version of the data that fitted the parameter | [Calibration provenance](../specification/binding.md) |
| `calibration_provenance[].identifiable` | Identifiable | true when the data identify the parameter apart from the structural discrepancy | [Calibration provenance](../specification/binding.md) |
| `calibration_provenance[].method` | Method | The method of the record. | [Calibration provenance](../specification/binding.md) |
| `calibration_provenance[].parameter` | Parameter | a parameter of the model | [Calibration provenance](../specification/binding.md) |
| `condition_pairs` | Condition pairs | per pair, a condition of the model, the condition of the target that it stands for, and the key; a parameter fitted to the data is marked as a *calibration parameter* | [Condition pairs](../specification/binding.md) |
| `condition_pairs[].calibration` | Calibration | true for a parameter of the model fitted to the data | [Condition pairs](../specification/binding.md) |
| `condition_pairs[].id` | Id | The id of the record. | [Condition pairs](../specification/binding.md) |
| `condition_pairs[].key` | Key | The key of the record. | [Condition pairs](../specification/binding.md) |
| `condition_pairs[].key_version` | Key version | The key version of the record. | [Condition pairs](../specification/binding.md) |
| `condition_pairs[].model_condition` | Model condition | The model condition of the record. | [Condition pairs](../specification/binding.md) |
| `condition_pairs[].target_condition` | Target condition | The target condition of the record. | [Condition pairs](../specification/binding.md) |
| `domain` | Domain of comparison | the conditions of the target over which the pairs are asserted, each region marked as *interpolation*, within the range of the calibration data, or *extrapolation*, outside it | [Domain of comparison](../specification/binding.md) |
| `domain[].kind` | Kind | The kind of the record. | [Domain of comparison](../specification/binding.md) |
| `domain[].region` | Region | The region of the record. | [Domain of comparison](../specification/binding.md) |
| `feature_pairs` | Feature pairs | per pair, a feature that the model exemplifies and the feature of the target to which it is imputed, typed: `quantity` · `pattern` · `regime` · `invariance-class` (an invariance or a universality class) · `modal-profile` · `component` (a unit of the model and the constituent or the admissible part of the target that it denotes); the mode of the pair, `computed` or `argued`; and, for a computed pair, the key that carries the one onto the other | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].exemplified` | Exemplified | The exemplified of the record. | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].id` | Id | The id of the record. | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].imputed` | Imputed | the feature of the target, by the symbol that the phenomenon declares; for a component pair, the constituent that the target system declares or the part that the admissible explanans admits | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].key` | Key | computed pairs only | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].key_version` | Key version | The key version of the record. | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].mode` | Mode | The mode of the record. | [Feature pairs](../specification/binding.md) |
| `feature_pairs[].type` | Type | The type of the record. | [Feature pairs](../specification/binding.md) |
| `grain` | Grain | `quantitative`, when the pairs are compared by a metric · `qualitative`, when they are compared by a match of patterns or regimes | [Grain](../specification/binding.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `model` | Model | the model in use the identifier of one model record | [Model](../specification/binding.md) |
| `status` | Status | The status of the record. | — |
| `structural_discrepancy` | Structural discrepancy | the model of the systematic difference between the output of the model at its best parameters and the value of the target, or a stated bound on it [kennedyohagan2001]; a discrepancy model fitted to data counts as calibration on those data, and the calibration provenance records it | [Structural discrepancy](../specification/binding.md) |
| `structural_discrepancy[].expression` | Expression | The expression of the record. | [Structural discrepancy](../specification/binding.md) |
| `structural_discrepancy[].form` | Form | The form of the record. | [Structural discrepancy](../specification/binding.md) |
| `structural_discrepancy[].pairs` | Pairs | the feature pairs that the discrepancy concerns | [Structural discrepancy](../specification/binding.md) |
| `structural_discrepancy[].reading` | Reading | a discrepancy model fitted to data counts as calibration on those data | [Structural discrepancy](../specification/binding.md) |
| `target` | Target | the denotation of the phenomenon, and the level at which the model is compared the identifier of one phenomenon, and the target level: `phenomenon`, when the model is compared with the observables that the phenomenon estimates; `data`, when it is compared with a version of the data through an observation operator | [Target](../specification/binding.md) |
| `target.level` | Level | The level of the record. | [Target](../specification/binding.md) |
| `target.phenomenon` | Phenomenon | the phenomenon that the binding denotes | [Target](../specification/binding.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `version` | Version | a version identifier, and the time at which the binding was committed | [Version](../specification/binding.md) |
| `version.committed` | Committed | The committed of the record. | [Version](../specification/binding.md) |
| `version.label` | Label | a version identifier | [Version](../specification/binding.md) |

## `concept`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `antagonist` | Antagonist | The concept of the opposed property, for a concept of the kind property. | [Antagonist](../specification/concept.md) |
| `broader` | Broader concept | The broader concept that this one specializes, named from the narrower concept only. | [Broader concept](../specification/concept.md) |
| `confusions` | Confusions | The concepts with which this one risks being conflated, each with the distinction that separates them. | [Confusions](../specification/concept.md) |
| `confusions[].axis` | Axis of difference | The axis along which the two concepts differ. | [Confusions: axis of difference](../specification/concept.md) |
| `confusions[].blocking_feature` | Blocking feature | The feature of one concept that the other lacks, which blocks their interchange. | [Confusions: blocking feature](../specification/concept.md) |
| `confusions[].consequence` | Consequence | The error that the inquiry commits when it conflates the two concepts. | [Confusions: consequence](../specification/concept.md) |
| `confusions[].other` | Other concept | The concept, or the term in use, with which this one risks being conflated. | [Confusions: other concept](../specification/concept.md) |
| `confusions[].risk` | Source of the risk | The shared feature that makes the two concepts easy to conflate. | [Confusions: risk](../specification/concept.md) |
| `definition` | Definition | A pointer to the full definition object of the concept, when one exists. | [Definition](../specification/concept.md) |
| `gloss` | Gloss | One sentence that fixes the meaning of the concept, without asserting a claim about its instances. | [Gloss](../specification/concept.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `kind` | Kind | Whether the concept names a system, a subtype or a class, a property, or a process. | [Kind](../specification/concept.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `source` | Source | The note or the publication that states the concept and its grounds. | [Source](../specification/concept.md) |
| `status` | Status | The maturity of the record as a whole, or its retraction. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `derivation`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `consequences` | Consequences | The statements that the derivation establishes; a consequence answering a subordinate sought is a lemma. | [Consequences](../specification/derivation.md) |
| `consequences[].answers` | Answers | The identifier of the sought that the consequence answers, or the record served for the root sought of a derivation that serves one. | [Consequences: answers](../specification/derivation.md) |
| `consequences[].from` | From | The identifier of the object that states the consequence. | [Consequences: from](../specification/derivation.md) |
| `consequences[].gain` | Gain | The gain that the derivation actually brought. | [Consequences: gain](../specification/derivation.md) |
| `consequences[].id` | Identifier | A descriptive identifier of the consequence, unique within the record. | [Consequences: id](../specification/derivation.md) |
| `consequences[].pattern` | Pattern | The scheme applied, with the other problems within its reach. | [Consequences: pattern](../specification/derivation.md) |
| `consequences[].principle` | Principle | The identifier of the variation interpretation that names the property making the consequence hold. | [Consequences: principle](../specification/derivation.md) |
| `consequences[].record` | Record | The identifier of the law, the answer or the obligation that states the consequence; a law named here is marked derived. | [Consequences: record](../specification/derivation.md) |
| `features` | Features of the calculation | The events that the calculation exhibits, which only a diagnostic interpretation reads. | [Features of the calculation](../specification/derivation.md) |
| `features[].at` | At | The identifier of the object at which the event occurs. | [Features: at](../specification/derivation.md) |
| `features[].id` | Identifier | A descriptive identifier of the feature, unique within the record. | [Features: id](../specification/derivation.md) |
| `features[].kind` | Kind | The kind of event. | [Features: kind](../specification/derivation.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `impasses` | Impasses | The obstacles left by the derivation, each leaving a sought without answer. | [Impasses](../specification/derivation.md) |
| `impasses[].obstacle` | Obstacle | The identifier of the diagnostic interpretation that names the obstacle. | [Impasses: obstacle](../specification/derivation.md) |
| `impasses[].sought` | Sought | The identifier of the sought left without answer. | [Impasses: sought](../specification/derivation.md) |
| `interpretations` | Interpretations | The meanings assigned to the items of the derivation, each with its ground. | [Interpretations](../specification/derivation.md) |
| `interpretations[].grounds` | Grounds | The references on which the meaning rests, of the type that its kind requires. | [Interpretations: grounds](../specification/derivation.md) |
| `interpretations[].id` | Identifier | A descriptive identifier of the interpretation, unique within the record. | [Interpretations: id](../specification/derivation.md) |
| `interpretations[].kind` | Kind | The kind of meaning assigned. | [Interpretations: kind](../specification/derivation.md) |
| `interpretations[].of` | Of | The identifier of the item interpreted: an object, a move, a feature, a segment or a consequence. | [Interpretations: of](../specification/derivation.md) |
| `interpretations[].reading` | Reading | The meaning assigned, in one sentence. | [Interpretations: reading](../specification/derivation.md) |
| `kernel` | Kernel | The identifier of the move declared as the kernel of the derivation. | [Kernel](../specification/derivation.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `moves` | Moves | The steps that the record states: every non-routine move, and the routine moves that no segment bridges. | [Moves](../specification/derivation.md) |
| `moves[].binds` | Binds | The slots that the move binds, by symbol. | [Moves: binds](../specification/derivation.md) |
| `moves[].id` | Identifier | A descriptive identifier of the move, unique within the record. | [Moves: id](../specification/derivation.md) |
| `moves[].inputs` | Inputs | The objects, posits or premises that the move takes, by identifier. | [Moves: inputs](../specification/derivation.md) |
| `moves[].kind` | Kind | The atomic kind of the move. | [Moves: kind](../specification/derivation.md) |
| `moves[].outputs` | Outputs | The objects that the move yields, by identifier. | [Moves: outputs](../specification/derivation.md) |
| `moves[].warrant` | Warrant | What licenses the move: its source, the class of its error, its regime and the property that makes it apply. | [Moves: warrant](../specification/derivation.md) |
| `moves[].warrant.applies_because` | Applies because | The identifier of the structural or magnitude interpretation that makes the warrant apply at this point. | [Moves: warrant: applies because](../specification/derivation.md) |
| `moves[].warrant.cites` | Cites | The definition, the theorem, the record or the step that licenses the move. | [Moves: warrant: cites](../specification/derivation.md) |
| `moves[].warrant.error` | Class of error | The class of the error that the move introduces. | [Moves: warrant: error](../specification/derivation.md) |
| `moves[].warrant.regime` | Regime | The regime in which the warrant holds, for an approximation, a limit or a truncation. | [Moves: warrant: regime](../specification/derivation.md) |
| `moves[].warrant.source` | Source | The source of the license. | [Moves: warrant: source](../specification/derivation.md) |
| `objects` | Intermediate objects | The intermediate objects that the moves take and yield, cited by no other record. | [Objects](../specification/derivation.md) |
| `objects[].expression` | Expression | The object, written in the expression syntax over the symbols that the derivation sees. | [Objects: expression](../specification/derivation.md) |
| `objects[].form` | Form | Whether the object is a symbol, a quantity or a term, or an equation, an inequality or a condition. | [Objects: form](../specification/derivation.md) |
| `objects[].id` | Identifier | A descriptive identifier of the object, unique within the record. | [Objects: id](../specification/derivation.md) |
| `objects[].reading` | Reading | The object stated in one phrase. | [Objects: reading](../specification/derivation.md) |
| `orientations` | Orientations | The prospective rationale of each non-routine move and of each segment. | [Orientations](../specification/derivation.md) |
| `orientations[].alternatives` | Alternatives | The moves considered at that point and set aside, each with its reason. | [Orientations: alternatives](../specification/derivation.md) |
| `orientations[].alternatives[].move` | Move | The move set aside. | [Orientations: alternatives: move](../specification/derivation.md) |
| `orientations[].alternatives[].reason` | Reason | The reason for setting the move aside. | [Orientations: alternatives: reason](../specification/derivation.md) |
| `orientations[].change` | Change | The intended change of state that the purpose brings about. | [Orientations: change](../specification/derivation.md) |
| `orientations[].determines` | Determines | The identifier of the sought that the purpose determines. | [Orientations: determines](../specification/derivation.md) |
| `orientations[].expected_gain` | Expected gain | The gain that the move is expected to bring. | [Orientations: expected gain](../specification/derivation.md) |
| `orientations[].id` | Identifier | A descriptive identifier of the orientation, unique within the record. | [Orientations: id](../specification/derivation.md) |
| `orientations[].means` | Means | The kind of move, the scheme or the act that the purpose calls for. | [Orientations: means](../specification/derivation.md) |
| `orientations[].occasion` | Occasion | The identifier of the interpretation that makes the purpose relevant now. | [Orientations: occasion](../specification/derivation.md) |
| `orientations[].of` | Of | The identifier of the move or the segment that the orientation selects. | [Orientations: of](../specification/derivation.md) |
| `orientations[].provenance` | Provenance | Whether the orientation was written while the derivation was carried out, or reconstructed afterwards from a source. | [Orientations: provenance](../specification/derivation.md) |
| `orientations[].purpose` | Purpose | The end of the move, written as a goal: to determine an unknown, or to bring about a change. | [Orientations: purpose](../specification/derivation.md) |
| `posits` | Posits | The premises that the derivation introduces on trial, each with its origin and its tests. | [Posits](../specification/derivation.md) |
| `posits[].id` | Identifier | A descriptive identifier of the posit, unique within the record. | [Posits: id](../specification/derivation.md) |
| `posits[].kind` | Kind | The kind of posit. | [Posits: kind](../specification/derivation.md) |
| `posits[].origin` | Origin | Where the guess came from. | [Posits: origin](../specification/derivation.md) |
| `posits[].origin.kind` | Type | The type of origin of the guess. | [Posits: origin: kind](../specification/derivation.md) |
| `posits[].origin.ref` | Reference | The act, the source or the scheme from which the guess came. | [Posits: origin: ref](../specification/derivation.md) |
| `posits[].statement` | Statement | The form or the relation assumed. | [Posits: statement](../specification/derivation.md) |
| `posits[].tests` | Tests | The tests of the posit, each with its verdict. | [Posits: tests](../specification/derivation.md) |
| `posits[].tests[].by` | By | The move, the record or the source that carries the test. | [Posits: tests: by](../specification/derivation.md) |
| `posits[].tests[].kind` | Test | The kind of test. | [Posits: tests: kind](../specification/derivation.md) |
| `posits[].tests[].standard` | Standard | For a computation, whether the computation is certified or numerical. | [Posits: tests: standard](../specification/derivation.md) |
| `posits[].tests[].verdict` | Verdict | Whether the test supports or refutes the posit. | [Posits: tests: verdict](../specification/derivation.md) |
| `refutations` | Refutations | The statements that the derivation falsifies by a counterexample. | [Refutations](../specification/derivation.md) |
| `refutations[].by` | By | The object that is the counterexample; a refuting test of a posit is recorded among the tests of that posit. | [Refutations: by](../specification/derivation.md) |
| `refutations[].target` | Target | The posit, the consequence or the claim refuted, by identifier. | [Refutations: target](../specification/derivation.md) |
| `runs_on` | Runs on | The records whose laws, assumptions or claims are the premises of the derivation, by identifier. | [Runs on](../specification/derivation.md) |
| `segments` | Segments | The groups of contiguous moves that serve one sought under one idea, each bridging the moves that it omits. | [Segments](../specification/derivation.md) |
| `segments[].applies` | Applies | The identifier of the design of kind scheme that the segment applies. | [Segments: applies](../specification/derivation.md) |
| `segments[].id` | Identifier | A descriptive identifier of the segment, unique within the record. | [Segments: id](../specification/derivation.md) |
| `segments[].inputs` | Inputs | The objects or premises that the segment consumes. | [Segments: inputs](../specification/derivation.md) |
| `segments[].moves` | Moves | The moves stated inside the segment, by identifier. | [Segments: moves](../specification/derivation.md) |
| `segments[].outputs` | Outputs | The objects that the segment produces. | [Segments: outputs](../specification/derivation.md) |
| `segments[].within` | Within | The identifier of the segment that encloses this one. | [Segments: within](../specification/derivation.md) |
| `serves` | Serves | The identifier of the record that the derivation serves: a question, a proof obligation, or a law or an operation of a derived model stated in advance; empty for a derivation that constructs its result. | [Serves](../specification/derivation.md) |
| `slots` | Slots | The symbols introduced by a move or a posit, and bound later by a move. | [Slots](../specification/derivation.md) |
| `slots[].introduced_by` | Introduced by | The identifier of the move or the posit that introduces the slot. | [Slots: introduced by](../specification/derivation.md) |
| `slots[].reading` | Reading | What the slot stands for. | [Slots: reading](../specification/derivation.md) |
| `slots[].symbol` | Symbol | The symbol of the slot, unique within the record. | [Slots: symbol](../specification/derivation.md) |
| `sought` | Sought | The root sought of a derivation that serves no record: the unknown or the statement that the derivation seeks; its type and its condition fix its degree of determinacy. A derivation that serves a record reads its root sought from that record. | [Sought](../specification/derivation.md) |
| `sought.condition` | Condition | The condition that the unknown must satisfy; empty for an open or a typed sought. | [Sought: condition](../specification/derivation.md) |
| `sought.id` | Identifier | A descriptive identifier of the sought, unique within the record. | [Sought: id](../specification/derivation.md) |
| `sought.statement` | Statement | The unknown or the statement sought, in one phrase. | [Sought: statement](../specification/derivation.md) |
| `sought.type` | Type | The type of the unknown, once known; empty for an open sought. | [Sought: type](../specification/derivation.md) |
| `status` | Status | The maturity of the record as a whole, or its retraction. | — |
| `subordinate` | Subordinate soughts | The soughts that the derivation sets for itself, each answered by a lemma or left at an impasse. | [Subordinate soughts](../specification/derivation.md) |
| `subordinate[].condition` | Condition | The condition that the unknown must satisfy. | [Subordinate: condition](../specification/derivation.md) |
| `subordinate[].id` | Identifier | A descriptive identifier of the sought, unique within the record. | [Subordinate: id](../specification/derivation.md) |
| `subordinate[].reason` | Reason | The reason for the replacement. | [Subordinate: reason](../specification/derivation.md) |
| `subordinate[].replaces` | Replaces | The identifier of the subordinate sought that this one replaces, when the earlier one proved ill-posed. | [Subordinate: replaces](../specification/derivation.md) |
| `subordinate[].statement` | Statement | The unknown or the statement sought, in one phrase. | [Subordinate: statement](../specification/derivation.md) |
| `subordinate[].type` | Type | The type of the unknown, once known; empty for an open sought. | [Subordinate: type](../specification/derivation.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `uses` | Uses | The derivations whose consequences the derivation uses, by identifier. | [Uses](../specification/derivation.md) |

## `design`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `applies_when` | Conditions of application | The conditions under which the scheme applies, each a grammatical expression or a named property. | [Applies when](../specification/design.md) |
| `failure_modes` | Failure modes | The ways in which an execution can yield a misleading output, or an application of a scheme can fail, each with the step or the rule that guards against it, and for a scheme with the situation that announces the failure and the patch that it calls for. | [Failure modes](../specification/design.md) |
| `failure_modes[].guard` | Guard | The identifier of the step or the rule that detects or prevents the failure. | [Failure modes: guard](../specification/design.md) |
| `failure_modes[].mode` | Mode | The way in which an execution can yield a misleading output. | [Failure modes: mode](../specification/design.md) |
| `failure_modes[].patch` | Patch | The change of the scheme that the failure calls for. | [Failure modes: patch](../specification/design.md) |
| `failure_modes[].situation` | Situation | The situation that announces the failure, at the boundary of the conditions of application or where a posit fails. | [Failure modes: situation](../specification/design.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `inputs` | Inputs | The objects that an execution takes, such as systems, a sample, initial states or data. | [Inputs](../specification/design.md) |
| `inputs[].description` | Description | The content of the input, stated in one phrase. | [Inputs: description](../specification/design.md) |
| `inputs[].name` | Name | The name of the input. | [Inputs: name](../specification/design.md) |
| `kind` | Kind | Whether the design plans an experiment on the target, a run of a simulation of a model, a method that solves a task, or a scheme that derivations apply. | [Kind](../specification/design.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `output` | Output | What an execution yields, such as data or consequences. | [Output](../specification/design.md) |
| `posits` | Posits | The posits that the scheme prescribes, each stated as the form or the relation assumed. | [Posits](../specification/design.md) |
| `posits[].id` | Id | A descriptive identifier of the posit, unique within the record. | [Posits: id](../specification/design.md) |
| `posits[].statement` | Statement | The form or the relation that the scheme assumes. | [Posits: statement](../specification/design.md) |
| `protocol` | Protocol | The intervention, the control and the observation of an experiment or of a simulation run. | [Protocol](../specification/design.md) |
| `protocol.control` | Control | The condition against which the effect of the intervention is read. | [Protocol: control](../specification/design.md) |
| `protocol.intervention` | Intervention | The quantity that an execution sets, with its levels. | [Protocol: intervention](../specification/design.md) |
| `protocol.observation` | Observation | The observable that an execution records, with the key or the measurement procedure that yields it. | [Protocol: observation](../specification/design.md) |
| `rules` | Rules | The rules that state the admissible moves or decisions of an execution. | [Rules](../specification/design.md) |
| `rules[].id` | Identifier | A descriptive identifier of the rule, unique within the record. | [Rules: id](../specification/design.md) |
| `rules[].rule` | Rule | The move or the decision that the rule admits or imposes. | [Rules: rule](../specification/design.md) |
| `serves` | Serves | The identifier of the question or the problem that the design serves; optional for a method or a scheme that serves no single problem. | [Serves](../specification/design.md) |
| `status` | Status | The maturity of the record as a whole, or its retraction. | — |
| `steps` | Steps | The acts of an execution, in their order. | [Steps](../specification/design.md) |
| `steps[].act` | Act | The act that the step performs. | [Steps: act](../specification/design.md) |
| `steps[].id` | Identifier | A descriptive identifier of the step, unique within the record. | [Steps: id](../specification/design.md) |
| `stopping` | Stopping condition | The condition under which an execution stops. | [Stopping condition](../specification/design.md) |
| `task` | Task | One sentence that states what an execution of the design must achieve. | [Task](../specification/design.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `itinerary`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `addresses` | Addresses | the identifier of one problem record or of one question record | [Addresses](../specification/itinerary.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `status` | Status | The status of the record. | — |
| `steps` | Steps | one entry per activity instance, listed in any order | [Steps](../specification/itinerary.md) |
| `steps[].activity` | activity | the identifier of one activity of the registry | [Steps: activity](../specification/itinerary.md) |
| `steps[].branch` | branch | the condition under which the step is taken, and the step of the same output type taken otherwise | [Steps: branch](../specification/itinerary.md) |
| `steps[].branch.condition` | Condition | the condition under which the step is taken | [Steps: branch](../specification/itinerary.md) |
| `steps[].branch.otherwise` | Otherwise | the step taken when the condition fails, which produces the same output type | [Steps: branch](../specification/itinerary.md) |
| `steps[].derivation` | derivation | The identifier of the derivation record that holds the reasoning of the step, below the grain of its product; required once a step of the activity derivation passes its norm. | [Steps: derivation](../specification/itinerary.md) |
| `steps[].id` | id | a name unique within the itinerary, by which a later step refers to the output of this one | [Steps: id](../specification/itinerary.md) |
| `steps[].inputs` | inputs | per input, its product type and a reference: a record identifier, the full identifier of the step that produces the input, or a pointer for a `source` | [Steps: inputs](../specification/itinerary.md) |
| `steps[].inputs[].as_of` | As of | the revision of the repository at which the step read the record | [Steps: inputs](../specification/itinerary.md) |
| `steps[].inputs[].ref` | Ref | a record identifier, the identifier of the step that produces the input, or a pointer for a `source` | [Steps: inputs](../specification/itinerary.md) |
| `steps[].inputs[].type` | Type | an identifier of the product-type registry | [Steps: inputs](../specification/itinerary.md) |
| `steps[].iterate` | iterate | the criterion that ends the repetition of a step that takes its own output type as input | [Steps: iterate](../specification/itinerary.md) |
| `steps[].iterate.until` | Until | the criterion that ends the repetition | [Steps: iterate](../specification/itinerary.md) |
| `steps[].mode` | mode | deductive · inductive · abductive · analogical · error-statistical · model-based · non-inferential, equal to the mode of the activity | [Steps: mode](../specification/itinerary.md) |
| `steps[].norm` | norm | the test named by the registry for the activity, written `norm.<activity>`, its verdict: pass · fail · pending, and, once judged, the evidence and the date of the judgment | [Steps: norm](../specification/itinerary.md) |
| `steps[].norm.evidence` | Evidence | why the product meets the norm or fails it | [Steps: norm](../specification/itinerary.md) |
| `steps[].norm.judged` | Judged | the date of the last judgment of the verdict | [Steps: norm](../specification/itinerary.md) |
| `steps[].norm.test` | Test | the test named by the activity registry for this activity | [Steps: norm](../specification/itinerary.md) |
| `steps[].norm.verdict` | Verdict | The verdict of the record. | [Steps: norm](../specification/itinerary.md) |
| `steps[].output` | output | the product type of the product, and the record that holds the product, given while that record holds the output type | [Steps: output](../specification/itinerary.md) |
| `steps[].output.before` | Before | for a knowledge-state-change only, the revision of the repository before the change | [Steps: output](../specification/itinerary.md) |
| `steps[].output.ref` | Ref | the record that holds the product; omit until that record exists | [Steps: output](../specification/itinerary.md) |
| `steps[].output.type` | Type | The type of the record. | [Steps: output](../specification/itinerary.md) |
| `steps[].rationale` | rationale | the question that the step serves, or its problem, and the object on which the step acts: one of the eight conditions for obtaining an answer, the obtaining of the answer, or its evaluation | [Steps: rationale](../specification/itinerary.md) |
| `steps[].rationale.acts_on` | Acts on | The condition or the act on which the step acts. | [Steps: rationale](../specification/itinerary.md) |
| `steps[].rationale.serves` | Serves | the question that the step serves, or the problem | [Steps: rationale](../specification/itinerary.md) |
| `steps[].revises` | revises | the record that the step revises, the kind of the revision, and the review of each flagged dependent: pending · revised · unaffected · retracted | [Steps: revises](../specification/itinerary.md) |
| `steps[].revises.kind` | Kind | The kind of the revision. | [Steps: revises](../specification/itinerary.md) |
| `steps[].revises.record` | Record | the record that the step revises | [Steps: revises](../specification/itinerary.md) |
| `steps[].revises.reviews` | Reviews | one entry per flagged dependent that the researcher has reviewed | [Steps: revises](../specification/itinerary.md) |
| `steps[].revises.reviews[].dependent` | Dependent | a record that the revision flags | [Steps: revises](../specification/itinerary.md) |
| `steps[].revises.reviews[].state` | State | The state of the review. | [Steps: revises](../specification/itinerary.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `key`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `domain_and_codomain` | Domain and codomain | the side of the model and the side of the target that the key connects, each as a set expression or a type | [Domain and codomain](../specification/key.md) |
| `domain_and_codomain.codomain` | Codomain | the side of the target | [Domain and codomain](../specification/key.md) |
| `domain_and_codomain.domain` | Domain | the side of the model | [Domain and codomain](../specification/key.md) |
| `expression` | Expression | an expression over the symbols of its domain, or a pointer to the procedure that computes the map | [Expression](../specification/key.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `kind` | Kind | `observation-operator` · `unit-map` · `aggregation-map` · `qualitative-abstraction` | [Kind](../specification/key.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `status` | Status | The status of the record. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `version` | Version | a version identifier | [Version](../specification/key.md) |

## `model`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `assumptions` | Assumptions of the laws | per assumption, its motive, the gain that it provides, and whether it is removable, as the rule on idealizations defines them | [Assumptions of the laws](../specification/model.md) |
| `assumptions[].assumption` | Assumption | The assumption of the record. | [Assumptions of the laws](../specification/model.md) |
| `assumptions[].gain` | Gain | The gain of the record. | [Assumptions of the laws](../specification/model.md) |
| `assumptions[].id` | Id | The id of the record. | [Assumptions of the laws](../specification/model.md) |
| `assumptions[].motive` | Motive | The motive of the record. | [Assumptions of the laws](../specification/model.md) |
| `assumptions[].removable` | Removable | The removable of the record. | [Assumptions of the laws](../specification/model.md) |
| `background` | Background | the record from which the laws of the model are derived the identifier of one background record | [Background](../specification/model.md) |
| `constituents` | Constituents $C$ | the units that the model treats as bearers | [Constituents](../specification/model.md) |
| `constituents[].extent` | Extent | The extent of the record. | [Constituents](../specification/model.md) |
| `constituents[].map` | Map | give for a unit defined from the target, such as a coarse-graining, a mode decomposition, an aggregation or a quotient by a symmetry; omit for a unit of the model alone | [Constituents](../specification/model.md) |
| `constituents[].name` | Name | The name of the record. | [Constituents](../specification/model.md) |
| `constituents[].notation` | Notation | only when the LaTeX form differs from the symbol | [Constituents](../specification/model.md) |
| `constituents[].symbol` | Symbol | The symbol of the record. | [Constituents](../specification/model.md) |
| `constituents[].variant` | Variant | symbol of the target variant that the entry models; omit when the model stands for every member of the class | [Constituents](../specification/model.md) |
| `derives_from` | Derives from | The parent models, such as a target system or another model, from which the operations derive this model. | [Derives from](../specification/model.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `index_sets` | Index sets | the set, its extent and its structure, in the format of a target system | [Index sets](../specification/model.md) |
| `index_sets[].dimensional_formula` | dimensional formula | optional; the dimensional formula of the coordinate that the index set collects, such as L for a spatial domain or T for a time axis, so that a derivative along the index is checked | [Index sets: dimensional formula](../specification/model.md) |
| `index_sets[].extent` | Extent | The extent of the record. | [Index sets](../specification/model.md) |
| `index_sets[].name` | Name | The name of the record. | [Index sets](../specification/model.md) |
| `index_sets[].notation` | Notation | only when the LaTeX form differs from the symbol | [Index sets](../specification/model.md) |
| `index_sets[].structure` | Structure | The structure of the record. | [Index sets](../specification/model.md) |
| `index_sets[].symbol` | Symbol | The symbol of the record. | [Index sets](../specification/model.md) |
| `index_sets[].variant` | Variant | symbol of the target variant that the entry models; omit when the model stands for every member of the class | [Index sets](../specification/model.md) |
| `laws` | Laws or structural relations $L$ | the dependences that link the terms $V$ | [Laws or structural relations](../specification/model.md) |
| `laws[].expression` | Expression | The expression of the record. | [Laws or structural relations](../specification/model.md) |
| `laws[].name` | Name | The name of the record. | [Laws or structural relations](../specification/model.md) |
| `laws[].origin` | Origin | The origin of the record. | [Laws or structural relations](../specification/model.md) |
| `laws[].range` | Range | omit when the law is established across the whole model | [Laws or structural relations](../specification/model.md) |
| `laws[].reading` | Reading | The reading of the record. | [Laws or structural relations](../specification/model.md) |
| `laws[].requires` | Requires | The units on which the law rests, each by its dotted identifier, an assumption or an operation of a model, a law of a background or of a model, or a posit or a consequence of a derivation; a law whose descent a derivation records leaves its premises to that derivation. | [Laws: requires](../specification/model.md) |
| `laws[].rests_on` | Rests on | What the warrant of the law refers to beyond the units that it requires, in words, such as a source or a data set. | [Laws or structural relations](../specification/model.md) |
| `laws[].role` | Role | The role of the record. | [Laws or structural relations](../specification/model.md) |
| `laws[].signature` | Signature | places the claim ranges over; empty for a claim about the model as a whole | [Laws or structural relations](../specification/model.md) |
| `laws[].symbol` | Symbol | The symbol of the record. | [Laws or structural relations](../specification/model.md) |
| `laws[].variant` | Variant | symbol of the target variant that the entry models; omit when the model stands for every member of the class | [Laws or structural relations](../specification/model.md) |
| `laws[].warrant` | Warrant | The warrant of the record. | [Laws or structural relations](../specification/model.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `operations` | Operations | The typed operations that derive this model from its parents, in the order in which they are applied. | [Operations](../specification/model.md) |
| `operations[].acts_on` | Acts on | The symbols of a parent on which the operation acts. | [Operations: acts on](../specification/model.md) |
| `operations[].bound` | Bound | The bound on the error, for a controlled operation. | [Operations: bound](../specification/model.md) |
| `operations[].error` | Class of error | The class of the error that the operation introduces. | [Operations: error class](../specification/model.md) |
| `operations[].gain` | Gain | The derivation or the factor that the operation makes available. | [Operations: gain](../specification/model.md) |
| `operations[].id` | Identifier | A descriptive identifier of the operation, unique within the record. | [Operations: id](../specification/model.md) |
| `operations[].kind` | Kind | The kind of the operation, relative to the parent. | [Operations: kind](../specification/model.md) |
| `operations[].order` | Order | The order in which the limits of the operation are taken. | [Operations: order](../specification/model.md) |
| `operations[].regime` | Regime | The regime in which the operation holds, as an expression over declared symbols. | [Operations: regime](../specification/model.md) |
| `operations[].rests_on` | Rests on | The result, the limit or the source that justifies the operation. | [Operations: rests on](../specification/model.md) |
| `operations[].retires` | Retires | The symbols of a parent that this model no longer carries. | [Operations: retires](../specification/model.md) |
| `operations[].yields` | Yields | The symbols of this model that realize the operation. | [Operations: yields](../specification/model.md) |
| `organization` | Organization $O$ | per relation, the tuples that it connects and the laws that state it, in the format of a background record | [Organization](../specification/model.md) |
| `organization[].among` | Among | for a relation among laws: the laws, reach last; fill exactly one of `relates` and `among` | [Organization](../specification/model.md) |
| `organization[].name` | Name | The name of the record. | [Organization](../specification/model.md) |
| `organization[].reading` | Reading | only content beyond the relation and the laws | [Organization](../specification/model.md) |
| `organization[].realized_by` | Realized by | laws stating a relation among parts; the parts are read from their expressions | [Organization](../specification/model.md) |
| `organization[].relates` | Relates | for a relation among parts: the connected tuples, reach last | [Organization](../specification/model.md) |
| `organization[].symbol` | Symbol | The symbol of the record. | [Organization](../specification/model.md) |
| `organization[].variant` | Variant | symbol of the target variant that the entry models; omit when the model stands for every member of the class | [Organization](../specification/model.md) |
| `parameters` | Parameters | the same content as for a variable, for each quantity that the model holds fixed while the phenomenon unfolds | [Parameters](../specification/model.md) |
| `parameters[].condition` | Condition | give when no map builds the quantity | [Parameters](../specification/model.md) |
| `parameters[].dimensional_formula` | dimensional formula | optional; a monomial over the base dimensions and the base scales of the problem, such as M L T^-2, or 1 for a pure number | [Parameters](../specification/model.md) |
| `parameters[].expression` | Expression | give for a derived parameter | [Parameters](../specification/model.md) |
| `parameters[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes a value satisfying the condition; empty while the existence that the condition presupposes is undischarged. | [Parameters](../specification/model.md) |
| `parameters[].name` | Name | The name of the record. | [Parameters](../specification/model.md) |
| `parameters[].notation` | Notation | only when the LaTeX form differs from the symbol | [Parameters](../specification/model.md) |
| `parameters[].reading` | Reading | The reading of the record. | [Parameters](../specification/model.md) |
| `parameters[].scale` | Scale | The scale of the record. | [Parameters](../specification/model.md) |
| `parameters[].selects` | Selects | required with a condition | [Parameters](../specification/model.md) |
| `parameters[].shared` | Shared | true when one value holds for every tuple of the signature | [Parameters](../specification/model.md) |
| `parameters[].signature` | Signature | The signature of the record. | [Parameters](../specification/model.md) |
| `parameters[].symbol` | Symbol | The symbol of the record. | [Parameters](../specification/model.md) |
| `parameters[].values` | Values | The values of the record. | [Parameters](../specification/model.md) |
| `parameters[].variant` | Variant | symbol of the target variant that the entry models; omit when the model stands for every member of the class | [Parameters](../specification/model.md) |
| `status` | Status | The status of the record. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `variables` | Variables | per variable, its own symbol, signature and value set, and its construction: an expression over the symbols of the model, or a map other than the identity from the quantities that the target declares | [Variables](../specification/model.md) |
| `variables[].condition` | Condition | give when no map builds the quantity | [Variables](../specification/model.md) |
| `variables[].determined` | Determined | The determined of the record. | [Variables](../specification/model.md) |
| `variables[].dimensional_formula` | dimensional formula | optional; a monomial over the base dimensions and the base scales of the problem, such as M L T^-2, or 1 for a pure number | [Variables: dimensional formula](../specification/model.md) |
| `variables[].expression` | Expression | an expression over the symbols of the model, or a map other than the identity from quantities of the target | [Variables](../specification/model.md) |
| `variables[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes a value satisfying the condition; empty while the existence that the condition presupposes is undischarged. | [Variables](../specification/model.md) |
| `variables[].name` | Name | The name of the record. | [Variables](../specification/model.md) |
| `variables[].notation` | Notation | only when the LaTeX form differs from the symbol | [Variables](../specification/model.md) |
| `variables[].reading` | Reading | The reading of the record. | [Variables](../specification/model.md) |
| `variables[].scale` | Scale | The scale of the record. | [Variables](../specification/model.md) |
| `variables[].selects` | Selects | required with a condition | [Variables](../specification/model.md) |
| `variables[].shared` | Shared | true when one value holds for every tuple of the signature | [Variables](../specification/model.md) |
| `variables[].signature` | Signature | one constituent kind or index set per place; empty for the model as a whole | [Variables](../specification/model.md) |
| `variables[].symbol` | Symbol | The symbol of the record. | [Variables](../specification/model.md) |
| `variables[].values` | Values | The values of the record. | [Variables](../specification/model.md) |
| `variables[].variant` | Variant | symbol of the target variant that the entry models; omit when the model stands for every member of the class | [Variables](../specification/model.md) |

## `operators`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `base_scales` | Base scales | The base scales of the problem, beside the base dimensions of the package, that the dimensional formulas of its quantities may name. | [Base scales](../specification/operators.md) |
| `base_scales[].name` | name | The quantity whose scale the base scale measures. | [Base scales: name](../specification/operators.md) |
| `base_scales[].symbol` | symbol | The symbol of the base scale, unique among the base dimensions. | [Base scales: symbol](../specification/operators.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `operators` | Operators | The operators of the record. | [Operators](../specification/operators.md) |
| `operators[].dimension` | dimension | How the operator combines the dimensional formulas of its arguments; an operator that states no rule leaves the formula of its result undecided. | [Operators: dimension](../specification/operators.md) |
| `operators[].for_any` | for any (type variables of the operator) | type variables the operator is general over, usable in `signature` and `values`; omit when the operator acts on declared sets alone | [Operators: for any (type variables of the operator)](../specification/operators.md) |
| `operators[].name` | name | The name of the record. | [Operators: name](../specification/operators.md) |
| `operators[].notation` | notation | write #0 for the bound indices and #1 for each argument | [Operators: notation](../specification/operators.md) |
| `operators[].signature` | signature | The signature of the record. | [Operators: signature](../specification/operators.md) |
| `operators[].symbol` | symbol | The symbol of the record. | [Operators: symbol](../specification/operators.md) |
| `operators[].values` | values | The values of the record. | [Operators: values](../specification/operators.md) |
| `status` | Status | The maturity of the record as a whole, or its retraction. | — |
| `target_system` | Target system | The target system of the record. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `phenomenon`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `adequacy` | Adequacy | the purposes for which the data model is adequate per purpose, the question or the kind of use for which the data model is adequate, with its grounds | [Adequacy](../specification/phenomenon.md) |
| `adequacy[].grounds` | Grounds | The grounds of the record. | [Adequacy](../specification/phenomenon.md) |
| `adequacy[].purpose` | Purpose | The purpose of the record. | [Adequacy](../specification/phenomenon.md) |
| `category` | Category | particular occurrence · regularity (effect) · capacity · structural property | [Category](../specification/phenomenon.md) |
| `commitment` | Commitment | how far the record fixes the phenomenon `identified`: a definite description and pointers fix the referent · `specified`: the observables and the manifestations are written, and their symbols resolve | [Commitment](../specification/phenomenon.md) |
| `conditions_and_byproducts` | Conditions and byproducts | put a factor the question varies among the indices or the scope entries instead | [Conditions and byproducts](../specification/phenomenon.md) |
| `conditions_and_byproducts.byproducts` | byproducts | per byproduct, an expression over declared symbols with a justification that gives the reason for excluding it from the phenomenon | [Conditions and byproducts: byproducts](../specification/phenomenon.md) |
| `conditions_and_byproducts.byproducts[].expression` | Expression | The expression of the record. | [Conditions and byproducts: byproducts](../specification/phenomenon.md) |
| `conditions_and_byproducts.byproducts[].justification` | Justification | only content beyond the expression | [Conditions and byproducts: byproducts](../specification/phenomenon.md) |
| `conditions_and_byproducts.byproducts[].name` | Name | The name of the record. | [Conditions and byproducts: byproducts](../specification/phenomenon.md) |
| `conditions_and_byproducts.byproducts[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Conditions and byproducts: byproducts](../specification/phenomenon.md) |
| `conditions_and_byproducts.inhibiting` | inhibiting conditions | per condition, an expression over declared symbols with a justification | [Conditions and byproducts: inhibiting conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.inhibiting[].caveat` | Caveat | The caveat of the record. | [Conditions and byproducts: inhibiting conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.inhibiting[].expression` | Expression | The expression of the record. | [Conditions and byproducts: inhibiting conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.inhibiting[].justification` | Justification | only content beyond the expression | [Conditions and byproducts: inhibiting conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.inhibiting[].name` | Name | The name of the record. | [Conditions and byproducts: inhibiting conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.inhibiting[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Conditions and byproducts: inhibiting conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.modulating` | modulating conditions | per condition, the relation that it induces, as an expression naming the affected feature and the controlling quantity. An entry names the regime when the relation holds only there. Each condition carries a reading | [Conditions and byproducts: modulating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.modulating[].effect` | Effect | relate the modulating factor to the affected feature | [Conditions and byproducts: modulating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.modulating[].expression` | Expression | give when the modulation holds in a single regime only | [Conditions and byproducts: modulating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.modulating[].name` | Name | The name of the record. | [Conditions and byproducts: modulating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.modulating[].reading` | Reading | only content beyond the `effect` | [Conditions and byproducts: modulating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.modulating[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Conditions and byproducts: modulating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.nonstandard` | nonstandard circumstances | per circumstance, an expression over declared symbols, with a justification. The justification names the unusual feature and the procedure that produces the circumstance | [Conditions and byproducts: nonstandard circumstances](../specification/phenomenon.md) |
| `conditions_and_byproducts.nonstandard[].differentiation` | Differentiation | The differentiation of the record. | [Conditions and byproducts: nonstandard circumstances](../specification/phenomenon.md) |
| `conditions_and_byproducts.nonstandard[].expression` | Expression | The expression of the record. | [Conditions and byproducts: nonstandard circumstances](../specification/phenomenon.md) |
| `conditions_and_byproducts.nonstandard[].name` | Name | The name of the record. | [Conditions and byproducts: nonstandard circumstances](../specification/phenomenon.md) |
| `conditions_and_byproducts.nonstandard[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Conditions and byproducts: nonstandard circumstances](../specification/phenomenon.md) |
| `conditions_and_byproducts.precipitating` | precipitating conditions | per condition, an expression over declared symbols with a justification | [Conditions and byproducts: precipitating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.precipitating[].expression` | Expression | The expression of the record. | [Conditions and byproducts: precipitating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.precipitating[].justification` | Justification | only content beyond the expression | [Conditions and byproducts: precipitating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.precipitating[].name` | Name | The name of the record. | [Conditions and byproducts: precipitating conditions](../specification/phenomenon.md) |
| `conditions_and_byproducts.precipitating[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Conditions and byproducts: precipitating conditions](../specification/phenomenon.md) |
| `course` | Course | the ordered index along which the behavior unfolds an index, a grain and the parameters of the target that vary along the course | [Course](../specification/phenomenon.md) |
| `course.grain` | grain | an expression giving the shortest segment on which a predicate of the behavior is evaluated | [Course: grain](../specification/phenomenon.md) |
| `course.index` | index | the symbol of an index set of the target or of this record: time, a training step, or an input parameter | [Course: index](../specification/phenomenon.md) |
| `course.varies` | varies | the symbols of those parameters | [Course: varies](../specification/phenomenon.md) |
| `data` | Data | per entry, "[pointer to a data set, a recording or a derivation]" that establishes the phenomenon, with its version | [Data](../specification/phenomenon.md) |
| `data[].pointer` | Pointer | The pointer of the record. | [Data](../specification/phenomenon.md) |
| `data[].version` | Version | The version of the record. | [Data](../specification/phenomenon.md) |
| `data_model` | Data model | the models through which the data are produced or processed before they establish the phenomenon per model, its kind: instrument model · background simulation · assimilation model · reconstruction, and the model record or the publication that states it | [Data model](../specification/phenomenon.md) |
| `data_model[].kind` | Kind | The kind of the record. | [Data model](../specification/phenomenon.md) |
| `data_model[].reading` | Reading | The reading of the record. | [Data model](../specification/phenomenon.md) |
| `data_model[].source` | Source | the model record, or a pointer to the publication that states the model | [Data model](../specification/phenomenon.md) |
| `detection_criterion` | Detection criterion | per test, the condition that a candidate pattern must satisfy to count as established. The test also names the sources of variation across which the pattern must hold, and the external systems of the target that bound its conclusions | [Detection criterion](../specification/phenomenon.md) |
| `detection_criterion[].across` | Across | sources of variation the test must hold across | [Detection criterion](../specification/phenomenon.md) |
| `detection_criterion[].expression` | Expression | The expression of the record. | [Detection criterion](../specification/phenomenon.md) |
| `detection_criterion[].limited_by` | Limited by | external systems of the target whose reach bounds what the test can establish | [Detection criterion](../specification/phenomenon.md) |
| `detection_criterion[].name` | Name | The name of the record. | [Detection criterion](../specification/phenomenon.md) |
| `detection_criterion[].procedure` | Procedure | only content beyond the name of the test | [Detection criterion](../specification/phenomenon.md) |
| `detection_criterion[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Detection criterion](../specification/phenomenon.md) |
| `evidential_status` | Evidential status | established across data sets or methods · reported · predicted · derived within a model · absent from a closed search · disproved · undecided | [Evidential status](../specification/phenomenon.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `identification` | Identification | what fixes the referent before any observable is declared a definite description of the behavior, with pointers to the data, the results or the publications that report it | [Identification](../specification/phenomenon.md) |
| `identification.description` | description | a noun phrase that picks out one behavior of the target | [Identification: description](../specification/phenomenon.md) |
| `identification.pointers` | pointers | per pointer, a data set, a result or a publication | [Identification: pointers](../specification/phenomenon.md) |
| `index_sets` | Index sets | "[symbol]", with the set expression that it collects and its structure: continuum · discrete set · interval | [Index sets](../specification/phenomenon.md) |
| `index_sets[].dimensional_formula` | dimensional formula | optional; the dimensional formula of the coordinate that the index set collects, such as L for a spatial domain or T for a time axis, so that a derivative along the index is checked | [Index sets: dimensional formula](../specification/phenomenon.md) |
| `index_sets[].extent` | Extent | The extent of the record. | [Index sets](../specification/phenomenon.md) |
| `index_sets[].name` | Name | The name of the record. | [Index sets](../specification/phenomenon.md) |
| `index_sets[].notation` | Notation | only when the LaTeX form differs from the symbol | [Index sets](../specification/phenomenon.md) |
| `index_sets[].structure` | Structure | The structure of the record. | [Index sets](../specification/phenomenon.md) |
| `index_sets[].symbol` | Symbol | The symbol of the record. | [Index sets](../specification/phenomenon.md) |
| `index_sets[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [Index sets](../specification/phenomenon.md) |
| `manifestations` | Manifestations | per form, "[expression over the observables]" with its form: value · dependence · functional form · scaling · relation | [Manifestations](../specification/phenomenon.md) |
| `manifestations[].expression` | Expression | The expression of the record. | [Manifestations](../specification/phenomenon.md) |
| `manifestations[].features` | features | per feature, "[symbol] ∈ [set expression]" with the value observed within that set | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].caveat` | Caveat | The caveat of the record. | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].condition` | Condition | give when the measurement constrains the feature without fixing its value | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].dimensional_formula` | dimensional formula | optional; a monomial over the base dimensions and the base scales of the problem, such as M L T^-2, or 1 for a pure number | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes a value satisfying the condition; empty while the existence that the condition presupposes is undischarged. | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].name` | Name | The name of the record. | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].observed` | Observed | The observed of the record. | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].procedure` | Procedure | only content beyond the name and the value set | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].selects` | Selects | required with a condition | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].symbol` | Symbol | The symbol of the record. | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].features[].values` | Values | The values of the record. | [Manifestations: features](../specification/phenomenon.md) |
| `manifestations[].form` | Form | The form of the record. | [Manifestations](../specification/phenomenon.md) |
| `manifestations[].name` | Name | The name of the record. | [Manifestations](../specification/phenomenon.md) |
| `manifestations[].reading` | Reading | only content beyond the name and the form | [Manifestations](../specification/phenomenon.md) |
| `manifestations[].symbol` | Symbol | The symbol of the record. | [Manifestations](../specification/phenomenon.md) |
| `manifestations[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Manifestations](../specification/phenomenon.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `observables` | Observables | a reference to a quantity that the target declares, or "[symbol] ∈ [set expression]" with a reading naming it in words | [Observables](../specification/phenomenon.md) |
| `observables[].condition` | Condition | give when no map builds the quantity | [Observables](../specification/phenomenon.md) |
| `observables[].dimensional_formula` | dimensional formula | optional; a monomial over the base dimensions and the base scales of the problem, such as M L T^-2, or 1 for a pure number | [Observables: dimensional formula](../specification/phenomenon.md) |
| `observables[].estimator` | estimator | the estimator that computes the values from the data, the version of the data on which it runs, and the uncertainty that it reports; the estimates themselves are computed from these entries, not recorded | [Observables: estimator](../specification/phenomenon.md) |
| `observables[].estimator.data_version` | Data version | the version of the data on which the estimator runs | [Observables: estimator](../specification/phenomenon.md) |
| `observables[].estimator.method` | Method | The method of the record. | [Observables: estimator](../specification/phenomenon.md) |
| `observables[].estimator.uncertainty` | Uncertainty | The uncertainty of the record. | [Observables: estimator](../specification/phenomenon.md) |
| `observables[].event` | event | the origin from which the clock starts, the horizon at which observation stops, and the censoring (right · left · interval · none) for an event whose time is unknown | [Observables: event](../specification/phenomenon.md) |
| `observables[].event.censoring` | Censoring | The censoring of the record. | [Observables: event](../specification/phenomenon.md) |
| `observables[].event.horizon` | Horizon | The horizon of the record. | [Observables: event](../specification/phenomenon.md) |
| `observables[].event.origin` | Origin | The origin of the record. | [Observables: event](../specification/phenomenon.md) |
| `observables[].event.reading` | Reading | The reading of the record. | [Observables: event](../specification/phenomenon.md) |
| `observables[].expression` | expression | "[expression over declared symbols]", whose binders consume the indices that it aggregates | [Observables: expression](../specification/phenomenon.md) |
| `observables[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes a value satisfying the condition; empty while the existence that the condition presupposes is undischarged. | [Observables](../specification/phenomenon.md) |
| `observables[].name` | Name | The name of the record. | [Observables](../specification/phenomenon.md) |
| `observables[].notation` | Notation | only when the LaTeX form differs from the symbol | [Observables](../specification/phenomenon.md) |
| `observables[].reading` | Reading | The reading of the record. | [Observables](../specification/phenomenon.md) |
| `observables[].reference` | Reference | for an observable the target already declares as a quantity, give only this reference | [Observables](../specification/phenomenon.md) |
| `observables[].scale` | scale | nominal · ordinal · interval · ratio · absolute · not-applicable | [Observables: scale](../specification/phenomenon.md) |
| `observables[].selects` | Selects | required with a condition | [Observables](../specification/phenomenon.md) |
| `observables[].signature` | signature (indices $i$ and $t$) | the free indices of the definition: a constituent kind, an index set, time, a parameter, or a new index that it introduces | [Observables: signature (indices and )](../specification/phenomenon.md) |
| `observables[].symbol` | Symbol | The symbol of the record. | [Observables](../specification/phenomenon.md) |
| `observables[].values` | Values | The values of the record. | [Observables](../specification/phenomenon.md) |
| `observables[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Observables](../specification/phenomenon.md) |
| `observation_error` | Observation error | per observable or per data set, an error model: a distribution or a bound | [Observation error](../specification/phenomenon.md) |
| `observation_error[].expression` | Expression | The expression of the record. | [Observation error](../specification/phenomenon.md) |
| `observation_error[].form` | Form | The form of the record. | [Observation error](../specification/phenomenon.md) |
| `observation_error[].of` | Of | an observable, or the pointer of a data set | [Observation error](../specification/phenomenon.md) |
| `occurrence` | Occurrence | the class of the occurrences that the phenomenon concerns state · process · event · not-applicable, for a capacity | [Occurrence](../specification/phenomenon.md) |
| `pattern_selection` | Pattern selection | how the pattern stated by the manifestations was selected from the data the selection procedure, the patterns set aside, and the question that motivated the selection | [Pattern selection](../specification/phenomenon.md) |
| `pattern_selection[].manifestation` | Manifestation | the manifestation whose pattern was selected | [Pattern selection](../specification/phenomenon.md) |
| `pattern_selection[].motivated_by` | Motivated by | the question that motivated the selection | [Pattern selection](../specification/phenomenon.md) |
| `pattern_selection[].procedure` | Procedure | The procedure of the record. | [Pattern selection](../specification/phenomenon.md) |
| `pattern_selection[].set_aside` | Set aside | The set aside of the record. | [Pattern selection](../specification/phenomenon.md) |
| `scope_over_instances` | Scope over instances (index $k$) | an instance is a member of the reference class of $S$, or one realization of a system (a trial, a random initialization, a disorder sample) per source of variation, the declared quantities that it varies and the other sources held fixed meanwhile. Each entry also records its source: class member · realization · parameter draw · structure draw · scenario. It records its quantification as well: single instance · typical instance · ensemble summary · ensemble distribution · universal, meaning every member of the admitted class | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].conditional_on` | Conditional on | other sources held fixed while this one varies | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].differentiation` | Differentiation | only content beyond the name | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].name` | Name | The name of the record. | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].over` | Over | declared quantities this source changes; empty when the instance itself varies | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].quantification` | Quantification | The quantification of the record. | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].source` | Source | The source of the record. | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].symbol` | Symbol | The symbol of the record. | [Scope over instances (index )](../specification/phenomenon.md) |
| `scope_over_instances[].variant` | Variant | symbol of the target variant carrying the entry; omit when every member of the class carries it | [Scope over instances (index )](../specification/phenomenon.md) |
| `search` | Search | the search behind a negative status, its scope and procedure for an absence, its counterexample for a disproof | [Search](../specification/phenomenon.md) |
| `search.counterexample` | Counterexample | the record or the publication that establishes the counterexample or the contradiction | [Search: counterexample](../specification/phenomenon.md) |
| `search.procedure` | Procedure | the procedures and the data searched, and why they would have detected the behavior within the scope | [Search: procedure](../specification/phenomenon.md) |
| `search.scope` | Scope | the region of the members, conditions and courses that the search covered | [Search: scope](../specification/phenomenon.md) |
| `statement` | Statement | "[bearer of the phenomenon] [its behavior]", as a reading | [Statement](../specification/phenomenon.md) |
| `status` | Status | The status of the record. | — |
| `target_system` | Target system | The target system of the record. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `problem`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `answerability_obstacles` | Answerability obstacles | per obstacle, the condition — definiteness · answer type · discrimination · access · bridging · representation —, its refutation — outright · lack of means — and the records or the publications that establish it | [Answerability obstacles](../specification/problem.md) |
| `answerability_obstacles[].condition` | Condition | The condition of the record. | [Answerability obstacles](../specification/problem.md) |
| `answerability_obstacles[].pointers` | Pointers | the records or the publications that establish the refutation | [Answerability obstacles](../specification/problem.md) |
| `answerability_obstacles[].refutation` | Refutation | The refutation of the record. | [Answerability obstacles](../specification/problem.md) |
| `associated_question` | Associated question | the identifier of that question record, whose request equals the request of the problem | [Associated question](../specification/problem.md) |
| `constraints` | Constraints | per constraint, a name, the condition that a solution must satisfy, and the source that imposes it: a result, an admitted law or a publication | [Constraints](../specification/problem.md) |
| `constraints[].name` | Name | The name of the record. | [Constraints](../specification/problem.md) |
| `constraints[].source` | Source | The source of the record. | [Constraints](../specification/problem.md) |
| `constraints[].statement` | Statement | The statement of the record. | [Constraints](../specification/problem.md) |
| `demand` | Demand | "[the result required of a solution]" | [Demand](../specification/problem.md) |
| `explicanda` | Explicanda | per term, the term as used and a pointer to the data, the result or the publication that fixes its use | [Explicanda](../specification/problem.md) |
| `explicanda[].pointer` | Pointer | The pointer of the record. | [Explicanda](../specification/problem.md) |
| `explicanda[].term` | Term | The term of the record. | [Explicanda](../specification/problem.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `kind` | Kind | empirical, when the problem concerns the objects of a domain · conceptual, when it concerns the consistency of a theory or its fit with other theories | [Kind](../specification/problem.md) |
| `knowledge_obstacles` | Knowledge obstacles | per obstacle, its value — open gap · unassessed candidates · conflict · unwarranted claim · ill-defined terms · unsound presupposition — and the records or the publications that establish it | [Knowledge obstacles](../specification/problem.md) |
| `knowledge_obstacles[].obstacle` | Obstacle | The obstacle of the record. | [Knowledge obstacles](../specification/problem.md) |
| `knowledge_obstacles[].pointers` | Pointers | the records or the publications that establish the obstacle | [Knowledge obstacles](../specification/problem.md) |
| `maturity` | Maturity | optional; one maturity per field: open \| provisional \| stabilized; a field left out is provisional | [Maturity of a field](../specification/maturity.md) |
| `request` | Request | one · all · over-a-parameter · decision, as the request of a demand defines them | [Request](../specification/problem.md) |
| `result_type` | Result type | the type of result of the demand, one of the rows of the demand table: phenomenon · consequence · target-claim · model · explanation · classification · concept · measurement-procedure · knowledge-state-change · inter-theory-relation | [Result type](../specification/problem.md) |
| `significance` | Significance | the consequences of a solution for other work | [Significance](../specification/problem.md) |
| `sources` | Sources | per source, a pointer | [Sources](../specification/problem.md) |
| `statement` | Statement | "[the result sought], [the obstacle to obtaining it]", as a reading | [Statement](../specification/problem.md) |
| `status` | Status | The status of the record. | — |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |

## `question`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `addresses` | Addresses | the identifier of one problem record | [Addresses](../specification/question.md) |
| `answerability` | Answerability | per condition asserted, its route, its state (established · refuted), how a refutation holds (outright · lack-of-means) with the means tried, and the pointers that show the state | [Answerability](../specification/question.md) |
| `answerability[].condition` | Condition | The condition whose state is stated. | [Answerability](../specification/question.md) |
| `answerability[].means` | Means | every means considered, each tried and failed | [Answerability](../specification/question.md) |
| `answerability[].pointers` | Pointers | the records, the steps or the publications that show the state | [Answerability](../specification/question.md) |
| `answerability[].refutation` | Refutation | refuted only | [Answerability](../specification/question.md) |
| `answerability[].route` | Route | The route on which the state holds. | [Answerability](../specification/question.md) |
| `answerability[].state` | State | The state of the condition. | [Answerability](../specification/question.md) |
| `answerability[].term` | Term | definiteness only: the term whose definiteness is stated | [Answerability](../specification/question.md) |
| `construction` | Construction | the procedure named for the route of construction, and how it would yield a direct answer | [Construction](../specification/question.md) |
| `construction.procedure` | Procedure | a design of kind method, or a pointer to the procedure | [Construction](../specification/question.md) |
| `construction.reading` | Reading | how the procedure would yield a direct answer | [Construction](../specification/question.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `links` | Links | per link, the other question, the relation, and the record shared by the two questions | [Links](../specification/question.md) |
| `links[].question` | question | the identifier of the other question record | [Links: question](../specification/question.md) |
| `links[].relation` | relation | subquestion-of · explanans-from · presupposes · enables | [Links: relation](../specification/question.md) |
| `links[].via` | via | the identifier of the shared record, such as a phenomenon | [Links: via](../specification/question.md) |
| `maturity` | Maturity | optional; one maturity per field: open \| provisional \| stabilized; a field left out is provisional | [Maturity of a field](../specification/maturity.md) |
| `presuppositions` | Presuppositions | per presupposition, its part of soundness (existence · topic), its reading and, once formalized, its expression | [Presuppositions](../specification/question.md) |
| `presuppositions[].expression` | Expression | optional; empty while the presupposition is not formalized | [Presuppositions](../specification/question.md) |
| `presuppositions[].id` | Id | a name unique within the question | [Presuppositions](../specification/question.md) |
| `presuppositions[].part` | Part | The part of soundness to which the presupposition belongs. | [Presuppositions](../specification/question.md) |
| `presuppositions[].reading` | Reading | the presupposition in words | [Presuppositions](../specification/question.md) |
| `request` | Request | how many possible answers a direct answer selects, and whether it claims completeness: one · all · over-a-parameter · decision, as the request of a question defines them; the request of the problem that the question serves, when one exists | [Request](../specification/question.md) |
| `statement` | Statement | the question in words, restating its fields in the statement frame | [Statement](../specification/question.md) |
| `status` | Status | posed · refined · answered · abandoned | [Status](../specification/question.md) |
| `subject` | Subject | The subject of the record. | [Subject of a question](../specification/question-subject.md) |
| `subject.background` | Background of $S$ | background records whose laws the question admits; empty when it admits none | [Background of](../specification/question-subject.md) |
| `subject.contrast` | Contrast class $X$ | The contrast class $x$ of the record. | [Contrast class](../specification/question-subject.md) |
| `subject.contrast.compatibility` | Compatibility | exclusive · compatible (fact and foil co-occur in different systems) | [Compatibility](../specification/question-subject.md) |
| `subject.contrast.foil_set` | Foil set | per foil, the expressions over the declared observables that hold in that case, with a reading | [Foil set](../specification/question-subject.md) |
| `subject.contrast.foil_set[].expression` | Expression | The expression of the record. | [Foil set](../specification/question-subject.md) |
| `subject.contrast.foil_set[].name` | Name | The name of the record. | [Foil set](../specification/question-subject.md) |
| `subject.contrast.foil_set[].reading` | Reading | only content beyond the name and the expression | [Foil set](../specification/question-subject.md) |
| `subject.contrast.foil_set[].symbol` | Symbol | The symbol of the record. | [Foil set](../specification/question-subject.md) |
| `subject.contrast.foil_status` | Foil status | observed (a realized comparison case) · counterfactual | [Foil status](../specification/question-subject.md) |
| `subject.contrast.locus` | Locus | other outcome (same system and conditions, other value of $P$) · other system ($P$ absent) · other condition (same system, different setting or intervention) | [Locus](../specification/question-subject.md) |
| `subject.domain` | Domain of conditions $D$ | only restrictions of the a priori specification; assumptions of the analysis belong to the answer | [Domain of conditions](../specification/question-subject.md) |
| `subject.domain.limit` | Limit | the expression "[quantity] → [limit value]", with a justification stating why the question is about the limit system | [Limit](../specification/question-subject.md) |
| `subject.domain.limit.expression` | Expression | The expression of the record. | [Limit](../specification/question-subject.md) |
| `subject.domain.limit.justification` | Justification | The justification of the record. | [Limit](../specification/question-subject.md) |
| `subject.domain.restrictions` | Restrictions | Per restriction: the quantity held and the value set that it is held to. When no single quantity carries a restriction, the entry names it and states its defining expression. A restriction on a variable also states its mode: `clamped` · `restricted` · `initial` · `stationary` · `without-event`. Each restriction carries a justification stating why the question is put only within those bounds. | [Restrictions](../specification/question-subject.md) |
| `subject.domain.restrictions[].expression` | Expression | replaces `values` when no single quantity carries the restriction | [Restrictions](../specification/question-subject.md) |
| `subject.domain.restrictions[].justification` | Justification | The justification of the record. | [Restrictions](../specification/question-subject.md) |
| `subject.domain.restrictions[].name` | Name | required when no quantity names the entry | [Restrictions](../specification/question-subject.md) |
| `subject.domain.restrictions[].of` | Of | quantity held; omit when no single quantity carries the restriction | [Restrictions](../specification/question-subject.md) |
| `subject.domain.restrictions[].restriction` | Restriction | only where the entry names a variable, since a parameter is already fixed | [Restrictions](../specification/question-subject.md) |
| `subject.domain.restrictions[].values` | Values | set the quantity is held to | [Restrictions](../specification/question-subject.md) |
| `subject.phenomenon` | Phenomenon $P$ (the explanandum, under the aim explanation) | a record identifier `phen.TOPIC.NAME`; in a question schema, the placeholder below | [Phenomenon (the explanandum, under the aim explanation)](../specification/question-subject.md) |
| `subject.phenomenon.description` | Description | The description of the record. | [Phenomenon (the explanandum, under the aim explanation)](../specification/question-subject.md) |
| `subject.phenomenon.placeholder` | Placeholder | The placeholder of the record. | [Phenomenon (the explanandum, under the aim explanation)](../specification/question-subject.md) |
| `subject.target_system` | Target system $S$ | a record identifier; in a question schema, a placeholder written as for `phenomenon` | [Target system](../specification/question-subject.md) |
| `task` | Task | The task of the record. | [Epistemic task of a question](../specification/question-task.md) |
| `task.admissible_explanans` | Admissible explanans $\lambda$ | optional; when null, proportionality bounds the answer | [Admissible explanans](../specification/question-task.md) |
| `task.admissible_explanans.compositional` | Compositional level | the constituents of the target system · their sub-parts · aggregates of them | [Compositional level](../specification/question-task.md) |
| `task.admissible_explanans.justification` | Justification | one clause that carries no commitment already held by the axes | [Justification](../specification/question-task.md) |
| `task.admissible_explanans.substrate` | Substrate dependence | substrate-specific (variables of the particular parts) · substrate-independent (variables shared by every realization: functional roles, universality classes) · mapping (how substrate-specific variables realize substrate-independent ones) | [Substrate dependence](../specification/question-task.md) |
| `task.epistemic_aim` | Epistemic aim $A$ | The epistemic aim $a$ of the record. | [Epistemic aim](../specification/question-task.md) |
| `task.explicandum` | Explicandum | explication only: the term of an explicandum that the problem addressed by the question names, not a slot of the subject | [Explicandum](../specification/question-task.md) |
| `task.function_sense` | Function sense | required when the requested relation is `functional` | [Function sense](../specification/question-task.md) |
| `task.modal_strength` | Modal strength $\mu$ | The modal strength $\mu$ of the record. | [Modal strength](../specification/question-task.md) |
| `task.proof_obligations` | Proof obligations $\omega$ | fill when the answer must derive a statement rather than match a measurement | [Proof obligations](../specification/question-task.md) |
| `task.proof_obligations[].antecedent` | Antecedent | The antecedent of the record. | [Proof obligations](../specification/question-task.md) |
| `task.proof_obligations[].consequent` | Consequent | The consequent of the record. | [Proof obligations](../specification/question-task.md) |
| `task.proof_obligations[].id` | Id | a name unique within the question | [Proof obligations](../specification/question-task.md) |
| `task.proof_obligations[].name` | Name | The name of the obligation. | [Proof obligations](../specification/question-task.md) |
| `task.proof_obligations[].reading` | Reading | The reading of the record. | [Proof obligations](../specification/question-task.md) |
| `task.requested_relation` | Requested relation $R$ | The requested relation $r$ of the record. | [Requested relation](../specification/question-task.md) |
| `task.required_accuracy` | Required accuracy $\tau$ | The required accuracy $\tau$ of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.outputs_to_match` | Outputs to match | name only the target side; the answer reproduces each output | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.outputs_to_match[].justification` | Justification | The justification of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.outputs_to_match[].target` | Target | The target of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.outputs_to_match[].tolerance` | Tolerance | omit when the standard is `qualitative` or `structural-only` | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.outputs_to_match[].tolerance.bound` | Bound | The bound of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.outputs_to_match[].tolerance.metric` | Metric | measure the difference between `answer` and `target` | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.standard` | Standard | The standard of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.structures_to_match` | Structures to match | The structures to match of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.structures_to_match[].justification` | Justification | The justification of the record. | [Required accuracy](../specification/question-task.md) |
| `task.required_accuracy.structures_to_match[].target` | Target | The target of the record. | [Required accuracy](../specification/question-task.md) |
| `title` | Title | A short name of the record, as a label. | [Title](../specification/question.md) |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `virtues` | Virtues | one entry per virtue the inquiry weighs, under any epistemic aim | [Virtues of a question](../specification/question-virtues.md) |
| `virtues[].justification` | Justification | also state the shortfall of an answer that lacks this virtue | [Virtues of a question](../specification/question-virtues.md) |
| `virtues[].standing` | Standing | The standing of the record. | [Virtues of a question](../specification/question-virtues.md) |
| `virtues[].virtue` | Virtue | The virtue of the record. | [Virtues of a question](../specification/question-virtues.md) |

## `target-system`

| Path | Title | Description | Documented in |
| ---- | ----- | ----------- | ------------- |
| `commitment` | Commitment | how far the record fixes the target `identified`: a definite description and pointers fix the referent · `specified`: the declarations are written and their symbols resolve | [Commitment](../specification/target-system.md) |
| `constituents` | Constituents | "[symbol]", with its reading and the set expression that it collects | [Constituents](../specification/target-system.md) |
| `constituents[].extent` | Extent | The extent of the record. | [Constituents](../specification/target-system.md) |
| `constituents[].name` | Name | The name of the record. | [Constituents](../specification/target-system.md) |
| `constituents[].notation` | Notation | only when the LaTeX form differs from the symbol | [Constituents](../specification/target-system.md) |
| `constituents[].symbol` | Symbol | The symbol of the record. | [Constituents](../specification/target-system.md) |
| `constituents[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [Constituents](../specification/target-system.md) |
| `external_systems` | External systems | per external system, its symbol, its class, the variables that it shares and its constraints. A constraint restricts the shared variables beyond their declared value sets. Each constraint takes the fields of a law: its name, the places that its claim ranges over, its role among the six of a law, its expression and a reading. The field is never left empty: the list `[]` states that the external system imposes no constraint | [External systems](../specification/target-system.md) |
| `external_systems[].class` | Class | candidates for the external system, as a reference class for the target; empty where the record fixes no class | [External systems](../specification/target-system.md) |
| `external_systems[].constrains` | Constrains | constraints on the shared variables beyond their declared value sets; `[]` when there is none | [External systems](../specification/target-system.md) |
| `external_systems[].constrains[].expression` | Expression | The expression of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].constrains[].name` | Name | The name of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].constrains[].reading` | Reading | The reading of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].constrains[].role` | Role | The role of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].constrains[].signature` | Signature | places the claim ranges over; empty for a claim about the system as a whole | [External systems](../specification/target-system.md) |
| `external_systems[].name` | Name | The name of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].reading` | Reading | only content beyond the shared variables | [External systems](../specification/target-system.md) |
| `external_systems[].shares` | Shares | The shares of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].symbol` | Symbol | The symbol of the record. | [External systems](../specification/target-system.md) |
| `external_systems[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [External systems](../specification/target-system.md) |
| `id` | Identifier | The identifier of the record, in the dotted form whose prefix names the record type. | — |
| `identification` | Identification | what fixes the referent before any quantity is declared a definite description, with pointers to the data, the results or the publications that fix the referent | [Identification](../specification/target-system.md) |
| `identification.description` | description | a noun phrase that picks out one system or one class of systems | [Identification: description](../specification/target-system.md) |
| `identification.pointers` | pointers | per pointer, a data set, a result or a publication | [Identification: pointers](../specification/target-system.md) |
| `index_sets` | Index sets | "[symbol]", with the set expression that it collects and its structure: continuum · discrete set · interval | [Index sets](../specification/target-system.md) |
| `index_sets[].dimensional_formula` | dimensional formula | optional; the dimensional formula of the coordinate that the index set collects, such as L for a spatial domain or T for a time axis, so that a derivative along the index is checked | [Index sets: dimensional formula](../specification/target-system.md) |
| `index_sets[].extent` | Extent | The extent of the record. | [Index sets](../specification/target-system.md) |
| `index_sets[].name` | Name | The name of the record. | [Index sets](../specification/target-system.md) |
| `index_sets[].notation` | Notation | only when the LaTeX form differs from the symbol | [Index sets](../specification/target-system.md) |
| `index_sets[].structure` | Structure | The structure of the record. | [Index sets](../specification/target-system.md) |
| `index_sets[].symbol` | Symbol | The symbol of the record. | [Index sets](../specification/target-system.md) |
| `index_sets[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [Index sets](../specification/target-system.md) |
| `maturity` | Maturity | optional; one maturity per specification: open \| provisional \| stabilized; the record status applies to every specification left out | [Maturity of a field](../specification/maturity.md) |
| `parameters` | Parameters | "[symbol] ∈ [set expression]", with its reading and the signature that it takes, one entry per place. A flag states whether one value is shared by every tuple. The set is written without restriction, because a restriction of it belongs to $D$ | [Parameters](../specification/target-system.md) |
| `parameters[].condition` | Condition | give when no map builds the quantity | [Parameters](../specification/target-system.md) |
| `parameters[].dimensional_formula` | dimensional formula | optional; a monomial over the base dimensions and the base scales of the problem, such as M L T^-2, or 1 for a pure number | [Parameters](../specification/target-system.md) |
| `parameters[].expression` | Expression | give for a derived parameter | [Parameters](../specification/target-system.md) |
| `parameters[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes a value satisfying the condition; empty while the existence that the condition presupposes is undischarged. | [Parameters](../specification/target-system.md) |
| `parameters[].name` | Name | The name of the record. | [Parameters](../specification/target-system.md) |
| `parameters[].notation` | Notation | only when the LaTeX form differs from the symbol | [Parameters](../specification/target-system.md) |
| `parameters[].of` | Of | external system the entry characterizes; omit when the entry belongs to the target | [Parameters](../specification/target-system.md) |
| `parameters[].reading` | Reading | The reading of the record. | [Parameters](../specification/target-system.md) |
| `parameters[].scale` | Scale | The scale of the record. | [Parameters](../specification/target-system.md) |
| `parameters[].selects` | Selects | required with a condition | [Parameters](../specification/target-system.md) |
| `parameters[].shared` | Shared | true when one value holds for every tuple of the signature | [Parameters](../specification/target-system.md) |
| `parameters[].signature` | Signature | one entry per place, e.g. two neurons for a connectivity weight | [Parameters](../specification/target-system.md) |
| `parameters[].symbol` | Symbol | The symbol of the record. | [Parameters](../specification/target-system.md) |
| `parameters[].values` | Values | The values of the record. | [Parameters](../specification/target-system.md) |
| `parameters[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [Parameters](../specification/target-system.md) |
| `reference_class` | Reference class | a name, "[kind]", for the class that the other specifications generate | [Reference class](../specification/target-system.md) |
| `reference_class.name` | Name | The name of the record. | [Reference class](../specification/target-system.md) |
| `reference_class.projectibility` | projectibility | whether a claim about some members holds of the class assumed · tested · not-claimed, with the evidence for an assumed or a tested projection | [Reference class: projectibility](../specification/target-system.md) |
| `reference_class.projectibility.evidence` | Evidence | omit when the status is `not-claimed` | [Reference class: projectibility](../specification/target-system.md) |
| `reference_class.projectibility.status` | Status | The status of the record. | [Reference class: projectibility](../specification/target-system.md) |
| `reference_class.selection_criteria` | selection criteria | per criterion, the expression that a member satisfies, with a justification. The justification gives the reason for imposing the criterion and the inferences that it changes about the class | [Reference class: selection criteria](../specification/target-system.md) |
| `reference_class.selection_criteria[].expression` | Expression | The expression of the record. | [Reference class: selection criteria](../specification/target-system.md) |
| `reference_class.selection_criteria[].justification` | Justification | also state how the selection affects the inferences the population supports | [Reference class: selection criteria](../specification/target-system.md) |
| `reference_class.selection_criteria[].name` | Name | The name of the record. | [Reference class: selection criteria](../specification/target-system.md) |
| `status` | Status | The status of the record. | — |
| `target_type` | Target type | particular system · class of actual systems · class of possible systems · hypothetical system · no external target (the model class itself) | [Target type](../specification/target-system.md) |
| `title` | Title | A short name of the record, as a label. | — |
| `type` | Record type | The record type, which fixes the contract that the record follows. | — |
| `variables` | Variables | what changes while the phenomenon unfolds per variable, its signature and its value set, with a reading. The role test decides whether a quantity is a variable or a parameter. The value sets of the variables that $S$ determines, aggregates excepted, form the state space of $S$ | [Variables](../specification/target-system.md) |
| `variables[].condition` | Condition | give when no map builds the quantity | [Variables](../specification/target-system.md) |
| `variables[].determined` | determined (side of the boundary that sets the value) | within, when the system fixes its value, or outside, when it is set externally and still varies | [Variables: determined (side of the boundary that sets the value)](../specification/target-system.md) |
| `variables[].dimensional_formula` | dimensional formula | optional; a monomial over the base dimensions and the base scales of the problem, such as M L T^-2, or 1 for a pure number | [Variables: dimensional formula](../specification/target-system.md) |
| `variables[].expression` | Expression | give when a map builds the quantity from declared symbols | [Variables](../specification/target-system.md) |
| `variables[].held_by` | Held by | The law of a background or of a model, or the consequence of a derivation, that establishes a value satisfying the condition; empty while the existence that the condition presupposes is undischarged. | [Variables](../specification/target-system.md) |
| `variables[].name` | Name | The name of the record. | [Variables](../specification/target-system.md) |
| `variables[].notation` | Notation | only when the LaTeX form differs from the symbol | [Variables](../specification/target-system.md) |
| `variables[].of` | Of | external system the entry characterizes; omit when the entry belongs to the target | [Variables](../specification/target-system.md) |
| `variables[].reading` | Reading | The reading of the record. | [Variables](../specification/target-system.md) |
| `variables[].scale` | scale | the comparisons between values that carry meaning nominal · ordinal · interval · ratio · absolute · not-applicable, for a variable and for a parameter alike | [Variables: scale](../specification/target-system.md) |
| `variables[].selects` | Selects | required with a condition | [Variables](../specification/target-system.md) |
| `variables[].shared` | Shared | true when one value holds for every tuple of the signature | [Variables](../specification/target-system.md) |
| `variables[].signature` | Signature | one constituent kind or index set per place; empty for the system as a whole | [Variables](../specification/target-system.md) |
| `variables[].symbol` | Symbol | The symbol of the record. | [Variables](../specification/target-system.md) |
| `variables[].values` | Values | The values of the record. | [Variables](../specification/target-system.md) |
| `variables[].variant` | Variant | variant carrying the entry; omit when every member of the class carries it | [Variables](../specification/target-system.md) |
| `variants` | Variants | per variant, a name and a symbol. An entry carried by only some members names its variant (e.g. a declaration, a law, a relation, an external system). An unmarked entry holds for the whole class | [Variants](../specification/target-system.md) |
| `variants[].caveat` | Caveat | The caveat of the record. | [Variants](../specification/target-system.md) |
| `variants[].differentiation` | Differentiation | The differentiation of the record. | [Variants](../specification/target-system.md) |
| `variants[].name` | Name | The name of the record. | [Variants](../specification/target-system.md) |
| `variants[].symbol` | Symbol | The symbol of the record. | [Variants](../specification/target-system.md) |
