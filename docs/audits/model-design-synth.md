---
tags:
  - audit
index: "[gnomon audits](docs/audits/_index.md)"
aliases:
  - Audit - Model design (Synth)
---
# Audit - Model design (Synth)

> [!QUESTION] Goal: a target system and a candidate answer each commit to a model of the system under study. How should the records hold these models and the relations between them?

The inquiry records commit to a model of the system under study at two points: the target-system record fixes the initial model, and each candidate answer proposes its own. Therefore, the two templates share six blocks of declarations (constituents, index sets, variables, parameters, laws and organization). The designer proposed to make this shared commitment explicit. Two expert audits assessed the proposal: [audit F](model-design-f.md) and [audit S](model-design-s.md). This synthesis recommends one design, checked against the method notes, the architecture decisions and the six filled answers.

> [!NOTE] Provenance of the proposal
> No repository file records the proposal. Its three elements are reconstructed from the passages that quote the proposal in the two audits:
> - the model of an answer extends the target-system record;
> - the idealizations generalize into typed assumptions (among them restriction, limit, selection and change of perspective);
> - a relation states how the phenomenon arises in the model.

> [!TIP] Roadmap
> - Points settled by both audits: the base left unchanged by the recommended design.
> - Points raised by one audit: the contribution of each audit absent from the other, with its assessment.
> - Corpus evidence: three findings from the fixtures, absent from both audits or stated there in part.
> - Divergences: for each conflict, the deciding constraint and the resolution.
> - Recommended implementation: the records, the blocks and the checks, with a pointer to the pilot.

## Verdict

- **One record kind for system models.** The target record is the root model. A derived model is a record of the same kind that names its parents.
- **Two relations between models.** A derived model is produced from its parents by typed operations. A correspondence model is produced by no operation: it stands for another model through a posited key.
- **Operations typed by axes and placed by owner.** Each operation is typed by four axes (object acted on, effect on truth, loss of information, error class). Each operation is held by the record that imposes it.
- **An answer that holds claims only.** The answer references a system model and a phenomenon, and states one account entry per output, manifestation or feature reached. Under an explanatory aim only, the explanans annotates those entries.
- **A pilot before migration.** The pilot covers four fixtures (neural tangent kernel, active matter, grokking, tipping cascades).

## Points settled by both audits

Both audits agree on eleven points, the diagnosis first. The recommended design builds on these points without reopening them.

- **One commitment behind the shared blocks.** Both records declare a model, as the [model record](../epistemology/model-and-binding.md#^model-record) now states.
- **A missing relation.** No field states how the model of an answer relates to the model of the target. The fixtures state that relation in three places: derived expressions, warrants, and idealizations written in prose.
- **Three defects repaired by the relation.** Once explicit, the relation repairs three of the five trial defects (`test/answer-assessment-template-issues.md` at commit a4fb1b4: claim domain, explanatory semantics, binding of values). Therefore, the direct repair of the answer template should pause.
- **Chains of models.** A model can derive from a derived model, as each level of a tower of effective models does in theoretical physics.
- **Change of perspective as several operations.** An exact change of coordinates is invertible, so it loses no information and proves no new claim. A mean-field reduction, by contrast, typically projects many states onto one and then closes the dynamics with a posited or derived law.
- **Consistency of a lossy map.** A coarse model must agree with the fine model on the interventions represented at both levels [rubenstein2017]. The [individuation test](../epistemology/satisfaction-conditions.md) already states this requirement.
- **Approximation and idealization.** An approximation describes the same system inexactly, whereas an idealization introduces another system whose properties approximate the target [norton2012]. The [domain](../epistemology/domain.md) should stay separate from the [assumptions of the analysis](../epistemology/domain.md#^analysis-assumptions) after the refactor.
- **No generic block of assumptions.** Each kind of assumption keeps its own semantics (selection, restriction, model commitment, idealization, approximation, correspondence).
- **Refinement of a phenomenon.** A later model can operationalize the phenomenon (features for a qualitative label, an observable pushed forward through a map, a change of grain or of scope). The later model should leave the initial characterization in place.
- **One relation to the phenomenon for every aim.** The explanans is restricted to explanatory answers, and `produces` loses its general role.
- **Regime and error.** Each approximation states its regime of validity and an estimate or a class for its error.

## Points raised by one audit

### Audit F

| Point | Assessment |
| --- | --- |
| Four axes classify an operation (object acted on, effect on truth, loss of information, error class). | Adopted. The axes replace the motive as the classifier, and the [count of idealizations](#^idealizations-by-operation) supports the replacement. |
| The motive `isolation` covers an omission and a distortion alike [jones2005]. | Adopted as an axis value, with a limit. When the laws of a model are complete, as for a formal target, an omitted term is asserted absent, so omission and distortion coincide. The difference matters for an empirical target only, and no fixture requires it yet. |
| A limit can be singular, so the result can depend on the order of two limits [batterman2002]. | Adopted. The position of the entries in the block of operations carries the order. |
| A surrogate model represents its target through a key that maps features of the model onto features imputed to the target [frigg2018]. Universality or matching warrants the key. | Adopted as a [relation of its own](#^div-representation), outside the vocabulary of derivation. |
| The record that imposes an operation holds it. The rule settles the pending candidate on moving the domain beside the selection criteria. | Adopted. The candidate is declined: the domain and the criteria share an entry shape and differ in owner. |
| The explanans annotates a derivation with its difference-makers, and an idealization marks a factor shown to make no difference [strevens2008]. | Adopted for the structure of the answer, under the name resolved for the [account of the phenomenon](#^div-account). |
| A model passes the five conditions of [object-kind admission](../design/2-architecture/object-kinds.md#^t2-object-kind-admission). The target is already a model [elliottgraves2020], so no kind is added. | Adopted, within the limit stated for the [target record](#^div-target). |
| The design makes four checks possible beyond the individuation test (origin of each new symbol, claim domain along the chain, propagated warrants, robustness restricted to uncontrolled operations). | Adopted. |
| A derived law is a consequence of the model, recorded with the derivation, and no extension of the model. | Adopted, with a criterion separating a [defining law from a consequence](#^div-laws). |
| A derived phenomenon must reference a derived system model, for the grain test. | Adopted in a weaker form: the phenomenon references the model, root or derived, that declares the quantities of its observables. |

### Audit S

| Point | Assessment |
| --- | --- |
| The target and its model are distinct, related by `represents`, after the account of modeling by denotation, demonstration and interpretation [hughes1997]. | Not adopted as a split of records. The correspondence relation serves its concern, as resolved for the [target record](#^div-target). |
| A model can draw on two sources or more, and models are also partly autonomous from theories and targets [morgan1999]. | Adopted as a list of parents. |
| An evaluator can materialize a derived model, so unchanged declarations are written once. | Adopted by declaration, without evaluated operations, as resolved for the [content of a derived model](#^div-content). |
| A change of coordinates is an operation, checked by invertibility. | Adopted as a kind. |
| A derived quantity is an operation, checked by eliminability. | Not adopted: the `expression` key of the quantity already carries its definition. |
| An added law or constituent is an operation, checked by its warrant. | Adopted as the `extend` kind of audit F. |
| A composition is an operation, checked by the compatibility of interfaces and symbols. | Deferred until a fixture requires a composition. |
| Each epistemic aim specializes the relation between a model result and the phenomenon. For prediction, the result predicts a value. For modal knowledge, the result entails or excludes. | Not adopted as a field, as resolved for the [account of the phenomenon](#^div-account). The [epistemic aim](../epistemology/epistemic-aim.md) table already names the product of each aim. |
| An account entry states its scope, its modal strength and its accuracy. | Not adopted, as resolved for the [account of the phenomenon](#^div-account). The entry states only the value reached. |
| `through` splits into inferential dependencies, mechanistic paths and correspondence mappings. | Adopted. The account entry lists its inferential dependencies, the factor keeps its path, and the key carries the correspondence. |
| The [answer form](../epistemology/answer-form.md) reserved the warrant of a law to the answer, whereas the [target template](../../src/gnomon/data/templates/target-system.yml) and the [background](../epistemology/background.md#^law-warrant) note give every admitted law a warrant. | Confirmed: a header comment of the [answer template](../../src/gnomon/data/templates/answer.yml) also reserves the warrant to the answer. The inconsistency is corrected when the answer form and its template are rewritten. |
| A phenomenon model reuses generic components, but not the schema of a system model. | Adopted. |
| The design is piloted on three contrasting fixtures, and becomes a strong candidate for ratification when no compulsory block stays unused. Composition, reversibility, loss of information and propagated scope are tested before any migration. | Adopted, with the tipping fixture added to the [pilot](#^pilot). |
| The target-system record can stay intact at first, for compatibility. | Adopted for identifiers, as resolved for the [migration](#^div-migration). |

## Corpus evidence

The three findings below come from the fixtures, and each bears on at least one divergence. Audit F already classifies four of the seven idealizations and notes the tipping scope failure. Neither audit states the rest of the three findings.

### Idealizations by operation ^idealizations-by-operation

Four of the six answers hold idealizations, seven entries in all. Each entry is classified below by the operation performed.

| Answer | Assumption | Motive | Operation performed | Kind recommended |
| --- | --- | --- | --- | --- |
| Active matter | stochastic increments neglected | `isolation` | sets a present factor to zero | idealize |
| Active matter | weak amplitudes about the homogeneous state | `tractability` | expands the dynamics near onset, with an error controlled by the distance to onset | approximate |
| Grokking | toy addition problem | `tractability` | narrows the reference class | restrict |
| Grokking | infinitesimal step of the decoder | `isolation` | separates two time scales | limit |
| Tipping cascades | each subsystem replaced by a normal form | `tractability` | substitutes another system, produced by no operation on the target | correspondence |
| Tipping cascades | no feedback of the transitions on the temperature | `isolation` | removes a feedback that exists | idealize |
| Swift–Hohenberg | infinite line represented by a finite domain | `tractability` | approximates the computation and leaves the model unchanged | approximation of the computation |

Only two of the seven entries are distortions, in the sense defined by the `idealizations` block. The motive also fails to predict the operation: `tractability` labels four different operations, and `isolation` labels a limit beside two distortions. Therefore, the operation must be typed apart from the motive, and the robustness test must read the operation. For instance, the restriction to the toy task is relaxed by enlarging the class. The limit on the decoder step, by contrast, is relaxed by bounding the ratio of the two time scales.

### Reference as identity ^reference-as-identity

The tipping target is `particular`: the four subsystems of the actual Earth system. The answer enters `Theta`, `tau` and `Aij` by `reference`. Therefore, the record asserts that the parameters of four normal forms *are* the thresholds, the timescales and the architecture of interactions of the actual subsystems. That identity cannot hold for a stylized model. The consequence appears in the [tipping assessment](../../examples/earth-system-tipping-cascades/assessment.yml). Its individuation test passes, because "the four model nodes correspond one to one to the four declared subsystems". Its scope and robustness tests, by contrast, fail on the stylized ensemble. Therefore, `reference` must keep the meaning of identity, and an imputed correspondence requires a construct of its own.

### Values without a binding ^values-without-binding

The [neural tangent phenomenon](../../examples/neural-tangent-kernel-model-knowledge/phenomenon.yml) declares three features of the manifestation `output_converges`: the bound `Bout`, the horizon `Tout` and the mode of convergence `mode_out`. Each feature reads `observed: open`. The [neural tangent answer](../../examples/neural-tangent-kernel-model-knowledge/answer.yml) cannot assign a value to a feature. Therefore, the answer declares a parallel quantity `Bout_ans` and restates the bound as a law. The horizon and the mode receive no value: the horizon appears as the range `t >= 0` of the maximum, and the mode only in the reading of that law. The same pattern repeats for the drift and the initial kernel. Thus, the missing binding duplicates three quantities, so a repair must assign values to outputs and features already declared.

## Divergences

### Status of the target record ^div-target

**Positions.** Audit F makes the target record the root model, so no kind is added. Audit S separates two records. The target identifies the represented system, and the system model declares its quantities and laws.

**Deciding constraints.** In the [target system](../epistemology/target-system.md) note, the target already results from a modeling step, and the other specifications generate the reference class. If the target record is split from its model, then it keeps a name, a type and the selection criteria. Every reference of the form `system.TOPIC#SYMBOL` moves with the declarations to the model record. The split brings a benefit only when one target carries two root models, and no fixture does. The split also addresses a risk implicit in audit S: a model can misrepresent a worldly target. The fields `target_type` and `closure` already mark that risk. The correspondence relation covers a model that stands for the target without derivation.

**Resolution.** One kind, as in audit F. The split of audit S is deferred until a target requires two root models with incompatible declarations.

### Representation and derivation ^div-representation

**Positions.** Audit F lists the surrogate as a seventh kind of derivation entry. Audit S makes correspondence assumptions one of seven homes for assumptions, and relates target and model by `represents`.

**Deciding constraints.** A derivation entry acts on symbols of a parent and yields symbols of the model. A surrogate, by contrast, is produced by no operation on the declarations of the target, as audit F states. Audit F's own table accordingly marks its loss of information as "not comparable". The fields of a key entry also differ from those of an operation entry. Under [single field per fact](../adr/single-field-per-fact.md), a block boundary survives when it carries a rule of its own. The key carries such a rule: each entry maps a symbol of one model onto a symbol of another.

**Resolution.** Correspondence is a relation of its own, as in audit S. With the key structure of audit F, the correspondence model declares the correspondence as a key toward the model stood for. A correspondence model has no parent, so it states its own reference class, as a root does. Quantities identical in both models enter by `reference`, after the finding on [reference as identity](#^reference-as-identity), and the key holds only imputed correspondences.

### Number of parents ^div-parents

**Positions.** Audit F gives a derived model one parent. Audit S admits several.

**Deciding constraints.** A list holding one parent adds no cost, whereas converting a scalar into a list later forces a migration. Two parents can declare the same symbol. The uniqueness rule of the [flat symbol table](../adr/flat-symbol-table.md) settles that collision: the symbols visible from all parents must be unique. Under [shared field grounds](../adr/shared-field-grounds.md), a kind of operation earns its place when it recurs across the fixtures or changes the admissible answers. The design of the framework also justifies a kind on its own. No fixture composes two models, and no method note names a composition of models.

**Resolution.** `derives_from` is a list. The `compose` kind is deferred until the first model with two parents.

### Content of a derived model ^div-content

**Positions.** Audit F declares a derived model in the blocks of the target, with entries pointing to the symbols that realize each operation. Audit S writes the operations alone and lets an evaluator materialize the complete model.

**Deciding constraints.** The framework admits [no run-time inference](../design/1-framework/framework-foundations.md#^t1-no-runtime-inference): its tooling records and validates authored reasoning. The expression check is lexical, and no parser exists yet. Hence no tool can compute a linearization, and no tool can ever compute a posited closure.

**Resolution.** The model is declarative, as in audit F. The evaluator of audit S reduces to a set operation over declarations. The visible symbols of a derived model $M$ are $\mathrm{vis}(M)=\big(\bigcup_i \mathrm{vis}(P_i)\setminus R\big)\cup D$, where $P_i$ are its parents, $R$ its retired symbols and $D$ its own declarations. A reference still names the record that declares the symbol. Therefore, the [flat symbol table](../adr/flat-symbol-table.md) decision needs one amendment: the scope of a derived record extends over the symbols visible in its parents. The constraints of that decision still hold, because no block opens a nested scope and every reference keeps the form `record#symbol`.

### Placement of a transformation ^div-placement

**Positions.** Audit S records each transformation as a record of its own. Audit F places the operations in a block of the derived model.

**Deciding constraints.** An instance of a transformation has no identity apart from its destination model and serves no other model, so it fails [object-kind admission](../design/2-architecture/object-kinds.md#^t2-object-kind-admission). A separate record also requires a check holding it one-to-one with its destination. That shape of duplication is retired by [single field per fact](../adr/single-field-per-fact.md).

**Resolution.** A block in the derived model, as in audit F. The kinds of operation are listed in a registry.

### Homes of assumptions ^div-homes

**Positions.** Audit S separates seven homes for assumptions. Audit F uses one entry shape for operations, placed in three records by the ownership rule.

**Deciding constraints.** The seven homes map onto the design of audit F without loss:

- model commitments are laws with their warrants;
- scope restrictions are the domain of the question and the regime of each operation;
- selection criteria stay in the root model;
- transformation premises are the regime and the grounds of an operation, or a law of the derived model when the premise is a closure;
- idealizations and approximations are kinds of operation;
- correspondence assumptions are the key.

One divergence remains: audit S gives idealizations and approximations separate homes. Both carry the same fields, so [single field per fact](../adr/single-field-per-fact.md) admits one block with a kind. The key carries other fields, so it takes its own block.

**Resolution.** One block of operations typed by kind, as in audit F, and a separate key.

### Account of the phenomenon ^div-account

**Positions.** The two audits propose entries with different fields:

- audit F, one derivation record per manifestation: the laws and operations used, the route, the warrant and the manifestation reached;
- audit S, one `accounts_for` entry: the model result, the manifestation or observable, a relation specialized by aim, its support, its scope, its modal strength and its required accuracy.

**Deciding constraints.** Under description and prediction, the route can be a measurement, so "derivation" names one route among several. The [project goals](../../TODO.md) also include a framework for derivations. Therefore, the answer must leave the internal steps of a derivation to that framework. The aim of the question already fixes the relation of audit S. For the aims that require them, the modal strength and the requested relation refine that relation. A field for the relation would restate these fields. The scope can be computed, and the modal strength and the accuracy belong to the question.

**Resolution.** The entry structure of audit F, with the aim-neutral name of audit S. Each entry records the endpoints and the route of a result. Each entry also assigns a value to an output or a feature already declared, after the finding on [values without a binding](#^values-without-binding).

### Derived laws ^div-laws

**Positions.** Audit F records a derived law as a result of the answer. Audit S counts an added law, derived or otherwise, as a commitment of the model.

**Deciding constraints.** A derived model reused by two answers must not carry the theorems of one of them. The model holds the premises, and the answer holds the results. However, a law that defines a derived model cannot be a mere consequence. A closure is such a law, and so is the equation of a limit system: each enters every statement of the derived model.

**Resolution.** A law belongs to the derived model when an operation of that model lists the law under `yields`. Every other derived law is a result, stated in an account entry of the answer. The two derived laws already written in target records stay, as laws admitted a priori.

### Realizations ^div-realizations

**Positions.** Audit F keeps `realizations` as the mapping requested by a question about a link between substrates. Audit S turns it into a transformation or a correspondence between vocabularies.

**Deciding constraints.** A key is a posit of the modeler, set before any result. A realization is the claim sought by a question about a link, so it can be false and belongs among the claims of the answer. A key entry and a realization share a shape and differ in owner, as the ownership rule predicts.

**Resolution.** `realizations` stays in the answer unchanged, as in audit F. The two descriptions connected by a realization move into models.

### Records of a phenomenon ^div-phenomenon

**Positions.** Audit S separates the phenomenon from its successive models. Audit F gives the phenomenon template a parent and a block of operations.

**Deciding constraints.** The constraints that decide the [status of the target record](#^div-target) apply unchanged. One further boundary is drawn by neither audit. That boundary separates definitions from claims: a derived phenomenon may change definitions only, since the values claimed for its outputs are claims of the answer. The framework already draws that line in the [target system](../epistemology/target-system.md) note: an aggregation map "cannot be false of the system", whereas a law can. Consequently, two of the changes listed by audit S leave the phenomenon record:

- assigning predicted values moves to the account entries of the answer;
- rejecting the initial characterization becomes the status `retracted` of the root, followed by a new root.

**Resolution.** The structure of audit F, bounded to definitions.

### Migration ^div-migration

**Positions.** Audit F renames the kind `target-system` to `model` as an editorial change. The same audit migrates all six fixtures. Audit S lets the record stay intact at first, and pilots three fixtures before any migration.

**Deciding constraints.** A renamed identifier breaks every reference in the corpus, whereas a renamed `type` value changes one line per record. The tipping fixture is the only fixture where a correspondence decides a verdict, and audit S leaves it out of the pilot.

**Resolution.** Every `system.TOPIC` identifier stays. The kind and the template are renamed in one editorial commit after the pilot, and the pilot includes the tipping fixture.

## Recommended implementation

### Records

| Record | Content | Fields added or retired |
| --- | --- | --- |
| Root system model, filed as `target-system.yml` | the denotation of the target (type, reference class, selection criteria, variants) and the initial declarations | none |
| Derived system model, from the same template | its parents, its operations, and the declarations yielded by its operations | adds `derives_from` and `operations` |
| Correspondence model, from the same template | its own denotation, its declarations, and a key toward the model stood for | adds `stands_for` and `key` |
| Root phenomenon | as now | none |
| Derived phenomenon, from the phenomenon template | its parents, its operationalizations, and the observables or features added | adds `derives_from` and `operations`; `target_system` may name a derived model |
| Question | as now | `subject.target_system` may name a derived model when the question concerns that model |
| Answer | the statement, the status and the models referenced, followed by the claims (account entries, explanans, realizations) | adds `system_model`, `phenomenon` and `accounts`; retires the six declaration blocks and `idealizations` |
| Assessment | as now, with tests reading the new fields | none |

A derived model takes a file of its own because one model can serve several answers. The [template index](../../src/gnomon/data/templates/_index.md) already separates the target from its phenomena on the same ground.

### Derived and correspondence models

```yaml
id: model.TOPIC.NAME
type: target-system              # renamed after the pilot
derives_from: [system.TOPIC]     # one parent or more
operations:                      # applied in the order listed
  - name: "NAME OF THE OPERATION"
    kind:                        # restrict | limit | change-coordinates | aggregate | approximate | idealize | extend
    acts_on: [SYMBOL]            # symbols visible in a parent
    yields: [SYMBOL]             # symbols of this model that realize the operation
    retires: [SYMBOL]            # parent symbols no longer carried by this model; empty when every symbol stays visible
    regime: "EXPRESSION OVER DECLARED SYMBOLS"
    error:                       # exact | controlled | uncontrolled | singular
    bound: "EXPRESSION OVER DECLARED SYMBOLS"   # required with `controlled`
    buys: "THE DERIVATION OR THE FACTOR MADE AVAILABLE BY THE OPERATION"
    rests_on: "THE RESULT, THE LIMIT OR THE SOURCE THAT JUSTIFIES THE OPERATION"
# the declaration blocks of the template follow, holding only the symbols yielded by the operations
```

```yaml
stands_for: system.TOPIC         # fill instead of `derives_from`; fill the denotation blocks as for a root
key:                             # one entry per imputed correspondence; an identical quantity enters by `reference`
  - name: "NAME OF THE CORRESPONDENCE"
    maps: SYMBOL                 # symbol of this model
    onto: system.TOPIC#SYMBOL    # symbol of the model stood for
    warrant:                     # universality | matching
    rests_on: "THE UNIVERSALITY CLASS OR THE COMPARISON THAT WARRANTS THE CORRESPONDENCE"
```

### Operation vocabulary ^vocabulary

The initial registry holds seven kinds. Six occur in the corpus. The seventh, `change-coordinates`, is admitted on design grounds: the [model record](../epistemology/model-and-binding.md#^model-elements) names a mode decomposition among the maps defining new bearers.

| Kind | Acts on | Truth | Information | Error | Instance in the corpus |
| --- | --- | --- | --- | --- | --- |
| restrict | class | exact | kept | exact | grokking, toy addition task |
| limit | class | a new system | kept | controlled or singular | grokking, decoder step; neural tangent kernel, on the side of the question |
| change-coordinates | description | exact | kept | exact | none |
| aggregate | description | exact map, posited closure | lost | set by the closure | grokking, learned representation |
| approximate | description | inexact description of the same system | lost | controlled near a state, otherwise uncontrolled | active matter, weak amplitude |
| idealize | description | distortion | lost | uncontrolled unless bounded | active matter, noise; tipping cascades, feedback |
| extend | description | an added posited law or definition | kept | set by the warrant | grokking, effective law |

Two kinds are deferred until a fixture requires them:

- `compose`, for a model with two parents;
- `abstract`, for an omission that differs from a distortion, on an empirical target.

### Ownership rule

| Operation | Owner and field | Instance |
| --- | --- | --- |
| selection on an outcome of the dynamics | root model, `selection_criteria` | members that reached zero training error, in the target note |
| restriction or limit imposed by the question | question, `domain` | `m -> infinity` (neural tangent kernel); stationary flow (turbulence) |
| operation of the analysis that changes the model | derived model, `operations` | expansion near onset (active matter) |
| approximation of the computation alone | answer, account entry | finite numerical domain (Swift–Hohenberg) |
| correspondence produced by no operation | correspondence model, `key` | four normal forms standing for four subsystems (tipping cascades) |
| realization requested by a question about a link | answer, `realizations` | no fixture |

A root model holds no operation, because each operation is defined relative to a parent.

### Answer

```yaml
id: ans.TOPIC.NAME
type: answer
status: preliminary              # preliminary | hypothesized | informally-backed | formally-proven | accepted | retracted
answers: quest.TOPIC.NAME
system_model: model.TOPIC.NAME   # `system.TOPIC` when the answer keeps the model of the target
phenomenon: phen.TOPIC.NAME      # the derived phenomenon when the answer refines the observables
variant: SYMBOL                  # unchanged
accounts:                        # one entry per output, manifestation or feature reached by the answer
  - name: "NAME OF THE RESULT"
    symbol: SYMBOL
    reaches: SYMBOL              # output, manifestation or feature of the phenomenon
    assigns: "EXPRESSION OVER DECLARED SYMBOLS"   # the value, the bound or the relation claimed for the symbol reached
    uses: [SYMBOL]               # laws and operations of the model on which the result depends
    route:                       # proof | simulation | measurement | intervention
    approximations: []           # approximations of the computation alone, in the entry form of an operation of kind `approximate`
    rests_on: "THE PROOF, THE COMPUTATION OR THE SOURCE THAT ESTABLISHES THE RESULT"
explanans:                       # fill only under an explanatory aim; `annotates: [SYMBOL]` replaces `produces` and names account entries
realizations:                    # unchanged; fill when the question asks for a link
```

The route values are those named by the [closure test](../epistemology/satisfaction-conditions.md). The neural tangent answer illustrates the binding. Its three account entries reach the three manifestations of its phenomenon. Each entry assigns values to the features of its manifestation: the bound, the mode and, where declared, the horizon. Consequently, the parallel quantities `Bout_ans`, `Bdrift_ans` and `Binit_ans` leave the answer.

### Checks

- **Origin of a symbol.** Each symbol of a derived model is visible in a parent, defined by an expression over visible symbols, or yielded by an operation.
- **Visible table.** The symbols visible from all parents are unique, and no expression uses a retired symbol.
- **Claim domain.** The claim domain is the reference class of the root or of the correspondence model, intersected with the regimes along the chain and with the variant. The scope test compares it with the domain of the question.
- **Robustness.** The test lists the operations whose error is uncontrolled or singular. A controlled operation is discharged by its bound.
- **Individuation and fidelity.** The individuation test reads each `aggregate` operation and each key. The fidelity test reads the key.
- **Warrant.** A warrant propagates along `derives_from`, from each law to every result using that law.
- **Account.** Each account entry reaches a symbol of the phenomenon referenced, and its `uses` resolve in the visible table.
- **Explanans.** An explanans is present exactly under an explanatory aim, and each factor annotates at least one account entry.

### Validation and migration ^pilot

The pilot, the ratification of these resolutions and the migration of the fixtures are tracked in the [project goals](../../TODO.md), under the goal `model-design`.

### Costs and open decisions

The recommended design carries three costs:

- each answer that does not keep the model of the target needs one more file, in three of the six fixtures of the current corpus;
- the checker gains a scope rule and two relations between records;
- an operation entry holds up to ten keys, against four for an idealization.

The same design brings two gains: the answer holds only its claims, and each model becomes reusable across answers and questions.

Three decisions remain with the designer:

- the names of the block `accounts` and of the key `annotates`;
- whether `motive` survives as an optional reason, since its value `limit` duplicates the kind;
- the record declaring the constants of a bound, such as the constant of the neural tangent bound: a feature of the manifestation, or a derived phenomenon.

## Sources

The entries below were checked only through the two audits and the method notes citing them.

- [batterman2002] [Batterman, *The Devil in the Details*, Oxford University Press, 2002](https://academic.oup.com/book/10652/chapter/158683815)
- [elliottgraves2020] [Elliott-Graves, "What is a target system?", *Biology & Philosophy* 35:28, 2020](https://link.springer.com/article/10.1007/s10539-020-09745-3)
- [frigg2018] [Frigg & Nguyen, "The turn of the valve: representing with material models", *European Journal for Philosophy of Science* 8(2), 2018](https://link.springer.com/10.1007/s13194-017-0182-4)
- [hughes1997] [Hughes, "Models and representation", *Philosophy of Science* 64, 1997](https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/models-and-representation/F842E4D23AD3A703F2FDBDAC03F83838)
- [jones2005] [Jones, "Idealization and abstraction: a framework", in *Idealization XII: Correcting the Model*, Rodopi, 2005](https://philpapers.org/s/Martin%20Jones)
- [morgan1999] [Morgan & Morrison, "Models as mediating instruments", in *Models as Mediators*, Cambridge University Press, 1999](https://www.cambridge.org/core/books/abs/models-as-mediators/models-as-mediating-instruments/10737C6DD4744A65E4B5B89B3D489B21)
- [norton2012] [Norton, "Approximation and idealization: why the difference matters", *Philosophy of Science* 79(2), 2012](https://philpapers.org/rec/NORAAI)
- [rubenstein2017] [Rubenstein et al., "Causal consistency of structural equation models", *Conference on Uncertainty in Artificial Intelligence*, 2017](https://www.auai.org/uai2017/proceedings/papers/11.pdf)
- [strevens2008] [Strevens, *Depth: An Account of Scientific Explanation*, Harvard University Press, 2008](https://ndpr.nd.edu/news/depth-an-account-of-scientific-explanation/)
