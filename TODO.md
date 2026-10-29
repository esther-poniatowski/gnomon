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
	- [ ] Commit and register the [question-decomposition framework](docs/methods-reasoning/question-decomposition-framework.md), from which the [conditions of answerability](docs/epistemology/definitions/conditions-of-answerability.md) take their breakdown and to which several notes link.
- [ ] Define a vocabulary of atomic research actions. It bears on the open decision on [primitive operations](docs/design/2-architecture/operations-and-modes.md#^t2-operation-primitiveness). 🆔 research-actions
- [ ] Build a framework that formalizes derivation (the analysis), its results, and synthesis (the answer). It extends the open decision on [arguments and derivations](docs/design/3-aspect-specific/arguments-reasoning.md) and the [answer form](docs/epistemology/answer-form.md). 🆔 derivation-framework
- [ ] Refactor the documentation for the epistemic framework. Create one file that enumerates all the fields by alphabetic order (including nested paths) and links to a markdown anchor that documents this field.
- [ ] Make the inquiry records checkable on a user's directory. The second review of the records found that a restart of a project can be written but not checked. 🆔 inquiry-records-round-2
	- [ ] Add a command that runs every checker on the records of one directory, keyed by identifier, so that linked questions with several phenomena are checked; resolve the symbols of answers as well.
	- [ ] Let a plan step reference a record at the state it had when the step ran (`as_of`), so that a plan stays valid once its steps succeed.
	- [ ] Close the gaps of the type graph of activities, as the [choice of the next act](docs/epistemology/next-act.md) marks them in its map from conditions to activities and in its tables of acts:
		- [ ] produce a first `concept` from an explicandum, raise a phenomenon to commitment `specified`, and fill or revise the fields of the epistemic task;
		- [ ] check the admissibility of a candidate; build a candidate model from a target specification and a background without a phenomenon, retrieve an established result as a candidate, derive from a candidate together with the admitted laws, and compare the consequences of several candidates;
		- [ ] record a negative detection; turn a derived consequence into an accepted claim, and into a phenomenon; judge the norm of a plan step;
		- [ ] revise a question after a corrective answer, narrow its domain or its contrast, and decompose a problem into subproblems; give a question of explication a record form, since its explicandum is not a slot;
		- [ ] develop a proof technique or an algorithm that gives access to a quantity.
	- [ ] Make the [choice of the next act](docs/epistemology/next-act.md) computable on the records:
		- [ ] record the [state](docs/epistemology/definitions/conditions-of-answerability.md#^condition-states) of each condition of answerability of a question, with pointers, and, for a refutation for lack of means, the means considered, so that the [open conditions](docs/epistemology/next-act.md#^open-condition) can be computed;
		- [ ] record the presuppositions of a question that neither a link `presupposes` nor the evidential status of its phenomenon states;
		- [ ] record the route of construction of a question: the procedure named to yield a direct answer;
		- [ ] make the types of records exact: field paths that a program can read instead of prose, and the type `knowledge-state-change` read from a change of status instead of the present state;
		- [ ] keep the verdicts of a plan current: flag a step whose record is stabilized while its verdict is pending, so that its norm is [judged anew](docs/epistemology/next-act.md#^ready-act); in the plan of delayed generalization, the step `test` is in that state;
		- [ ] add a link between questions for a question generated from an unmet condition of another question, beside the closed list `subquestion-of | explanans-from | presupposes`;
		- [ ] then add a command that lists the open conditions and the [act instances](docs/epistemology/next-act.md#^ready-act) whose inputs exist and are warranted, with the reference `as_of` above.
	- [ ] State requirements on leaf fields, so that a block with empty fields fails; require the field path of an artifact type in the plan check.
	- [ ] Give the three remaining slot types a placeholder (contrast, observable, condition), or reduce the closed list of slot types.
	- [ ] Restate the link `explanans-from` as a bound on the admissible answers, and check it.
	- [ ] Reclassify the representation geometry: a property of the encoding map (factor `law-property`), whose occurrence may be a process along training.
	- [ ] Break the dependency between the declaration rule of quantities and the background: give `delimitation` the background as an input, with a decidable norm.
	- [ ] State the empty-value convention in one note: required fields, optional fields with a declared default, and an empty list against a null value.
	- [ ] Restrict process and event to temporal courses, and treat a derivative predicate as a state of motion.
	- [ ] Add general requirements for questions and answers, the missing fields (map of each constituent of an answer, warrant of a fitted parameter, caveat of an explanans factor, vocabulary of test verdicts), a criterion separating possible systems from a formal target, and the value `formal` for a problem kind.
	- [ ] Remove the remaining duplicates (limit rule, occurrence table), the stale mentions of sentinels in the test handoffs, and the name "interactions" for one-way relations in the code.
- [ ] Extend the problem record to the [formal statement of a problem](docs/epistemology/definitions/epistemic-problem.md): a typed demand (type of result, request, explicanda), a stated background, and the obstacle diagnosed on the two axes of the [types of problem](docs/epistemology/definitions/problem-types.md). 🆔 problem-record
	- [ ] Decide whether the background is the public corpus of a community, or the accepted records of the project together with the publications that they cite.
	- [ ] Decide whether a formal problem is a third kind of problem, or an attribute read from the closure of the background.
	- [ ] Decide whether explication becomes an aim, judged by criteria of adequacy instead of truth, with a concept record.
	- [ ] Decide whether the field `addresses` of a question becomes required.
	- [ ] Let the problem record hold several obstacles of axis A, each with its pointers; read axis B from the refuted conditions of the associated question instead of storing it twice.
	- [ ] Make the problem typologies of the [question-hierarchy framework](docs/methods-reasoning/question-hierarchy-framework.md) and of the design layer point to the types of problem, and decide which one is the single source.
	- [ ] Stop calling the epistemic task, and the question $Q$, "the epistemic problem" in the [epistemic task](docs/epistemology/epistemic-task.md) and in the [epistemic and pragmatic virtues](docs/epistemology/epistemic-pragmatic-virtues.md).

## Integration of the Geonexus pilot

The Mixture pilot of `geonexus` corrected several parts of the framework while specifying research and exposition records. Its generic decisions belong to `gnomon`, and `geonexus` keeps only its bindings and the application to the pilot. The decisions are listed in the pilot handoff, `/Users/eresther/Documents/research/geonexus/projects/mixture-input-encoding/HANDOFF.md`, and drafted in the decision notes `argument-architecture-records.md`, `research-pilot-profile.md` and `exposition-pilot-profile.md` of `/Users/eresther/Documents/research/geonexus/docs/_decisions/`.

- [ ] Integrate the generic decisions of the Mixture pilot, for research records and for exposition records. 🆔 pilot-integration
	- [ ] Rename the plan record to the itinerary and the artifact types to product types, following the [decision on the itinerary and the product types](docs/adr/itinerary-and-product-types.md). Name the product types that each epistemic aim admits. 🆔 itinerary-products
	- [ ] Replace the reference form `system.TOPIC#SYMBOL` by the uniform identifier of the [decision on dotted identifiers](docs/adr/dotted-identifiers.md), in the notes, the templates, the checkers and the fixtures. 🆔 dotted-identifiers
	- [ ] Specify each record type by a JSON Schema compatible with Ekphrasis, and derive the templates from the schemas, following the [decision on record schemas](docs/adr/record-schemas.md). 🆔 record-schemas
	- [ ] Specify the exposition family as projections of research records that add no content, following the [decision on expositions as projections](docs/adr/expositions-as-projections.md): a registry of rhetorical moves with the product type that each requires, the levels of an exposition, transitions, announcements and syntheses, and traces to research units. 🆔 exposition-family
	- [ ] Merge the relation vocabulary of `geonexus` and the semantic relations of `gnomon` into one registry, resolving the conflicts on `rebuts`, `contrasts`, `motivated-by` and supersession; give each relation a warrant kind and admit a warrant sentence. 🆔 relation-registry
	- [ ] Specify the assembly of a level: the status `core` or `elaboration` of each component, the output parts that it supplies, typed citations between components, elaboration across levels, views that expand chosen components, and the checks of the core route. 🆔 assembly-schema
	- [ ] Apply the research corrections of the pilot: 🆔 research-corrections
		- [ ] identifiers on idealizations, abstractions and explanans factors, and a key listing the idealizations that a law requires;
		- [ ] typed output parts of an answer, and typed premises in place of the free string `rests_on`;
		- [ ] the warrant `numerical`, the grade of an idealization, supersession of a retracted law, and the open parts of gaps excluded by a question;
		- [ ] the verdicts `partial` and `unsupported`, identifiers on obligations, and verdicts per law that reference the step supplying their evidence;
		- [ ] a rationale on each itinerary step, naming the question served and the way the step acts on it, with the eight conditions of the [choice of the next act](docs/epistemology/next-act.md);
		- [ ] a record kind for designs, and the activities of the pilot absent from the registry, beside the gaps listed under `inquiry-records-round-2`: comparing a derived law with a simulation;
		- [ ] the checks of produced content, of the rationale and of revisions.
	- [ ] Repair the indexes of `src/gnomon/data/contracts/`, `schemas/`, `specs/` and `workflow/`, which point to the missing `docs/design/methods/`.
