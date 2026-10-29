---
tags:
  - tasks
aliases:
  - Project goals
---
# Project goals

This list holds the goals of `gnomon` that span several parts of the project. The open decisions of the design stay in the [design task list](docs/TODO.md), and a goal that extends one of them links to that decision.

## Conventions

- [x] In the YAML forms, use an **empty value** instead of the sentinel `open`. This strategy is fragile: "open" must be free so that it can be used as an allowed value in certain fields. Moreover, the sentinel is not necessary. The empty convention aligns with the implementation in ekphrasis. ⏫
- [ ] Align the conventions of `gnomon` with those of `geonexus`, recorded in `/Users/eresther/Documents/research/geonexus/CONVENTIONS.md`. 🆔 geonexus-conventions
	- [ ] Compare the two workspaces on frontmatter keys, conventional file types (task lists, dashboards, handoffs), and task syntax.
	- [ ] Adopt the conventions retained, in this list and in the [design task list](docs/TODO.md) first.
- [ ] Give each entry of `docs/_index.md`, and of the indexes under `docs/design/` and `docs/methods-*`, one sentence stating why a reader opens the file. The indexes of `docs/epistemology/`, `docs/adr/`, and `test/` already follow this rule. 🆔 index-goals

## Frameworks

- [x] Update the README to register the new orientation of the framework and the pending features.
- [ ] Improve the answer and assessment templates from the test cases.
- [ ] Build a framework that formalizes definitions, grounded in the authoritative literature of epistemology and checked against concrete problems of `geonexus`. 🆔 definitions-framework
- [ ] Build a framework that formalizes the decomposition of a question into subquestions. It extends the partly settled [decisions on questions](docs/TODO.md). 🆔 question-decomposition
	- [x] Consolidate the question-decomposition framework and the question-hierarchy framework into the note on [question decomposition](docs/epistemology/question-decomposition.md).
- [ ] Define a vocabulary of atomic research actions. It bears on the open decision on [primitive operations](docs/design/2-architecture/operations-and-modes.md#^t2-operation-primitiveness). 🆔 research-actions
- [ ] Build a framework that formalizes derivation (the analysis), its results, and synthesis (the answer). It extends the open decision on [arguments and derivations](docs/design/3-aspect-specific/arguments-reasoning.md) and the [answer form](docs/epistemology/answer-form.md). 🆔 derivation-framework
- [ ] Refactor the documentation for the epistemic framework. Create one file that enumerates all the fields by alphabetic order (including nested paths) and links to a markdown anchor that documents this field.
- [ ] Make the inquiry records checkable on a user's directory. The second review of the records found that a restart of a project can be written but not checked. 🆔 inquiry-records-round-2
	- [ ] Add a command that runs every checker on the records of one directory, keyed by identifier, so that linked questions with several phenomena are checked; resolve the symbols of answers as well.
	- [ ] Let an itinerary step reference a record at the state it had when the step ran (`as_of`), so that an itinerary stays valid once its steps succeed.
	- [ ] Close the gaps of the type graph of activities, as the [choice of the next act](docs/epistemology/next-act.md) marks them in its map from conditions to activities and in its tables of acts:
		- [ ] produce a first `concept` from an explicandum, raise a phenomenon to commitment `specified`, and fill or revise the fields of the epistemic task;
		- [ ] build a candidate model from a target specification and a background without a phenomenon, retrieve an established result as a candidate, derive from a candidate together with the admitted laws, and compare the consequences of several candidates;
		- [ ] record a negative detection; turn a derived consequence into an accepted claim, and into a phenomenon; judge the norm of an itinerary step;
		- [ ] revise a question after a corrective answer, narrow its domain or its contrast, and decompose a problem into subproblems; give a question of explication a record form, since its explicandum is not a slot;
		- [ ] develop a proof technique or an algorithm that gives access to a quantity.
	- [ ] Make the [choice of the next act](docs/epistemology/next-act.md) computable on the records:
		- [ ] record the [state](docs/epistemology/definitions/conditions-of-answerability.md#^condition-states) of each condition of answerability of a question, with pointers, and, for a refutation for lack of means, the means considered, so that the [open conditions](docs/epistemology/next-act.md#^open-condition) can be computed;
		- [ ] record the presuppositions of a question that neither a link `presupposes` nor the evidential status of its phenomenon states;
		- [ ] record the route of construction of a question: the procedure named to yield a direct answer;
		- [ ] make the types of records exact: field paths that a program can read instead of prose, and the type `knowledge-state-change` read from a change of status instead of the present state;
		- [ ] keep the verdicts of an itinerary current: flag a step whose record is stabilized while its verdict is pending, so that its norm is [judged anew](docs/epistemology/next-act.md#^ready-act); in the itinerary of delayed generalization, the steps `check` and `test` are in that state;
		- [ ] add an activity that produces a question generated from an unmet condition of another question, linked to it by `enables`, since `question-decomposition` requires erotetic implication;
		- [ ] then add a command that lists the open conditions and the [act instances](docs/epistemology/next-act.md#^ready-act) whose inputs exist and are warranted, with the reference `as_of` above.
	- [ ] State requirements on leaf fields, so that a block with empty fields fails; require the field path of a product type in the itinerary check.
	- [ ] Give the three remaining slot types a placeholder (contrast, observable, condition), or reduce the closed list of slot types.
	- [ ] Restate the link `explanans-from` as a bound on the admissible answers, and check it.
	- [ ] Reclassify the representation geometry: a property of the encoding map (factor `law-property`), whose occurrence may be a process along training.
	- [ ] Break the dependency between the declaration rule of quantities and the background: give `delimitation` the background as an input, with a decidable norm.
	- [ ] State the empty-value convention in one note: required fields, optional fields with a declared default, and an empty list against a null value.
	- [ ] Restrict process and event to temporal courses, and treat a derivative predicate as a state of motion.
	- [ ] Add general requirements for questions and answers, the missing fields (map of each constituent of an answer, warrant of a fitted parameter, caveat of an explanans factor, vocabulary of test verdicts), a criterion separating possible systems from a formal target, and the value `formal` for a problem kind.
	- [ ] Remove the remaining duplicates (limit rule, occurrence table), the stale mentions of sentinels in the test handoffs, and the name "interactions" for one-way relations in the code.
- [ ] Extend the problem record to the [formal statement of a problem](docs/epistemology/definitions/epistemic-problem.md): a typed demand (type of result, request, explicanda), a stated background, and the obstacle diagnosed on the two axes of the [types of problem](docs/epistemology/definitions/problem-types.md). 🆔 problem-record
	- [x] Decide whether the background is the public corpus of a community, or the accepted records of the project together with the publications that they cite: the second, as the [background of a problem](docs/epistemology/definitions/epistemic-problem.md) states.
	- [ ] Decide whether a formal problem is a third kind of problem, or an attribute read from the closure of the background.
	- [ ] Decide whether explication becomes an aim, judged by criteria of adequacy instead of truth, with a concept record.
	- [ ] Decide whether the field `addresses` of a question becomes required.
	- [ ] Let the problem record hold several obstacles of axis A, each with its pointers; read axis B from the refuted conditions of the associated question instead of storing it twice.
	- [ ] Make the problem typologies of the design layer point to the [types of problem](docs/epistemology/definitions/problem-types.md), and decide which one is the single source.
	- [ ] Stop calling the epistemic task, and the question $Q$, "the epistemic problem" in the [epistemic task](docs/epistemology/epistemic-task.md) and in the [epistemic and pragmatic virtues](docs/epistemology/epistemic-pragmatic-virtues.md).

## Integration of the Geonexus pilot

The Mixture pilot of `geonexus` corrected several parts of the framework while specifying research and exposition records. Its generic decisions belong to `gnomon`, and `geonexus` keeps only its bindings and the application to the pilot. The decisions are listed in the pilot handoff, `/Users/eresther/Documents/research/geonexus/projects/mixture-input-encoding/HANDOFF.md`, and drafted in the decision notes `argument-architecture-records.md`, `research-pilot-profile.md` and `exposition-pilot-profile.md` of `/Users/eresther/Documents/research/geonexus/docs/_decisions/`.

- [ ] Integrate the generic decisions of the Mixture pilot, for research records and for exposition records. 🆔 pilot-integration
	- [x] Rename the plan record to the itinerary and the artifact types to product types, following the [decision on the itinerary and the product types](docs/adr/itinerary-and-product-types.md). 🆔 itinerary-products
	- [x] Name the product types that each epistemic aim admits, in the table of [epistemic aims](docs/epistemology/epistemic-aim.md), as the same decision requires.
	- [ ] Replace the reference form `system.TOPIC#SYMBOL` by the uniform identifier of the [decision on dotted identifiers](docs/adr/dotted-identifiers.md), in the notes, the templates, the checkers and the fixtures. 🆔 dotted-identifiers
	- [ ] Specify each record type by a JSON Schema compatible with Ekphrasis, and derive the templates from the schemas, following the [decision on record schemas](docs/adr/record-schemas.md). 🆔 record-schemas
	- [ ] Specify the exposition family as projections of research records that add no content, following the [decision on expositions as projections](docs/adr/expositions-as-projections.md): a registry of rhetorical moves with the kind of output that each requires, the parts and blocks of an exposition, connectors, announcements and syntheses, and traces to research units. An exposition, or one of its sections, may declare an order strategy, `claim-first` or `support-first` and `general-first` or `specific-first`, checked against the order of its parts, as the retired construction indexes of `geonexus` did for notes. 🆔 exposition-family
	- [ ] Declare the relations between research units, and between exposition units and research units, in one registry of `gnomon`, independent of the citation vocabularies of its consumers. Resolve the senses of `rebuts`, `contrasts`, `motivated-by` and supersession met in the pilot, and give each relation a warrant kind with an optional warrant sentence. 🆔 relation-registry
	- [ ] Specify the assembly of a level: the status `core` or `elaboration` of each component, the output parts that it supplies, typed citations between components, elaboration across levels, views that expand chosen components, and the checks of the core route. 🆔 assembly-schema
	- [ ] Provide the mechanisms of the notation, the glossary, the audience and the project specification, following the [decision on terminology, audience and project specifications](docs/adr/terminology-audience-project-specifications.md): 🆔 vocabulary-records
		- [ ] write the four schemas and generate their templates, starting from the schemas and the decisions of `geonexus`;
		- [ ] port the checks of imports, references, conflicts, aliases and cycles from the glossary checker of `geonexus`;
		- [ ] reference the problem and question records from the scope of a project specification, instead of restating its questions;
		- [ ] keep in a notation only its conventions and the symbols reused across records, and generate the LaTeX macros of an exposition from the symbols;
		- [ ] define the concept record of the research family, with its optional link to a full definition object, following the [decision on concepts, glossaries and notations](docs/adr/concepts-glossaries-notations.md);
		- [ ] reduce the glossary to the names of concepts, with forbidden forms scoped by audience and shared exceptions tested by their examples;
		- [ ] specify the compositional notation, with its bases, modifiers, index sets and conventions, and parse every written expression against it;
		- [ ] reject every declared check that the checker does not run, and give each rule a planted case;
		- [ ] check the terms of an exposition against the audiences cited by its design brief.
	- [ ] Apply the research corrections of the pilot: 🆔 research-corrections
		- [ ] identifiers on idealizations, abstractions and explanans factors, and a key listing the idealizations that a law requires;
		- [ ] typed output parts of an answer, and typed premises in place of the free string `rests_on`;
		- [ ] the warrant `numerical`, the grade of an idealization, supersession of a retracted law, and the open parts of gaps excluded by a question;
		- [ ] the verdicts `partial` and `unsupported`, identifiers on obligations, and verdicts per law that reference the step supplying their evidence;
		- [ ] a rationale on each itinerary step, naming the question served and what the step acts on: one of the eight [conditions of answerability](docs/epistemology/definitions/conditions-of-answerability.md) for obtaining an answer (definiteness, answer type, soundness, candidates, discrimination, access, bridging, representation), the acts that obtain the answer, or the evaluation of an obtained answer, as the [choice of the next act](docs/epistemology/next-act.md) orders them;
		- [ ] a record kind for designs, and the activities of the pilot absent from the registry, beside the gaps listed under `inquiry-records-round-2`: comparing a derived law with a simulation;
		- [ ] the checks of produced content, of the rationale and of revisions.
	- [ ] Repair the indexes of `src/gnomon/data/contracts/`, `schemas/`, `specs/` and `workflow/`, which point to the missing `docs/design/methods/`.

## Open issues of the model-design audits

The [audits of the model design](docs/audits/_index.md) and their [synthesis](docs/audits/model-design-synth.md) left most of their issues open. The synthesis predates the [background records](docs/epistemology/background.md) and the product types, which moved the design away from its premise that the target record is the root model, so its resolution must be re-decided before it is implemented.

- [ ] Repair the inconsistencies that the audits expose under the current rules, without changing the model design. 🆔 audit-local-repairs
	- [x] Re-type the idealizations of the test cases under the current table of [idealizations and abstractions](docs/epistemology/definitions/idealization-and-abstraction.md): the infinitesimal decoder step of `grokking-delayed-generalization` is a limit, not an isolation, and each other entry takes the motive that its kind requires.
	- [x] Align the gloss of the motive `isolation` in the answer template with the minimalist idealization that the table defines, and move to `abstractions` the omissions that the answer does not read as complete.
	- [x] Give the laws of an answer the keys `origin` and `range` of the laws of a background, or state why they differ, and check that the two blocks keep the same keys.
	- [ ] Resolve the symbols of answer records in the vocabulary check. A first attempt, which read an answer against the symbols of its whole problem, failed 19 tests in five answers. Two causes need a decision on the scope of an answer: `explanans.separates` names the foils of the contrast of the question, and the relations of `organization` range over index sets that the target declares. The others are defects to repair: `and` written as an operator, `jacobian` called with one argument instead of three, variables marked shared without a signature, and the variable `Nu` of `swift-hohenberg-localized-states` declared and never used.
	- [x] Give the assessment an overall disposition, with a value for a verdict withheld, since the gates of the tests stay implicit: the [disposition](docs/epistemology/satisfaction-conditions.md#^disposition) is read from the verdicts.
	- [x] Update the [handoff of the framework corrections](test/framework-corrections-handoff.md): pause the repairs of the templates that both audits advise against, decline the candidate that puts the domain beside the selection criteria, and point to this group.
	- [x] Close the issues made obsolete: renaming the record kind `target-system` to `model`, against the present separation of a target specification from a model, and keeping the identifiers `system.TOPIC`, which the [dotted identifiers](docs/adr/dotted-identifiers.md) replace.
- [ ] Revise the model design, following the [decision on answers, models and bindings](docs/adr/answers-models-bindings.md). 🆔 model-design
	- [x] Decide which record holds the model of a target: a model record of its own, which several answers can ground, related to the phenomenon by a binding.
	- [ ] Pilot the design on contrasting test cases before any migration: a prediction, a how-actually explanation with factors of each target status, a theorem about a model, and the stylized model of `earth-system-tipping-cascades`; ratify the resolutions of the synthesis that the decision leaves open, and amend the [flat symbol table](docs/adr/flat-symbol-table.md) for the symbols visible across records.
	- [x] Give the aims an open registry with their answer conditions and their category, and move the change of accepted claims to acceptance, as a revision of a belief base on a named corpus.
	- [ ] Restructure the answer into a core and aim blocks: grounds with typed roles, dependence, route, domain, status, erotetic relation; the explanatory block with the target status of each factor; the declared use of an answer that binds to no target; the typed relations between answers and their lineage. Remains: moving the checkers of `vocabulary.py` and `completeness.py` from the earlier keys of an answer (`explanans`, `realizations`) to those of the [answer template](src/gnomon/data/templates/answer.yml).
	- [ ] Add the record kinds of the model, the binding and the key, with their checks; record how a derived model relates to its parents, by operations typed on the axes of the synthesis rather than by motive, with approximation as a category that states its regime and its class of error, and singular limits with their order; register `binding` and `key` as product types, and give `validation` a binding among its inputs, since it reads the comparison computed from one. Remains: symbol resolution for the three templates, and a field for the parents of a derived model.
	- [ ] Give the phenomenon the models of its data model, its observation error, the selection of its pattern and the purposes of its data model; record a refined phenomenon as a derived phenomenon, leaving the original intact. Remains: a field of the [phenomenon template](src/gnomon/data/templates/phenomenon.yml) that names the phenomenon from which a refined one derives.
	- [ ] Compute the comparison from a binding, a version of the data and the tolerance of the question, with the time of commitment, the treatment of calibration data and the flag of circularity.
	- [ ] Separate the model of an answer from its results, so that a derived law is a consequence, with one derivation record per answer, under the goal `derivation-framework`.
	- [ ] Revise the method notes on the answer, the phenomenon and the assessment, and migrate the test cases, ending the use of `reference` for a stylized constituent. Remains: the migration of the test cases, by the pilot above.

