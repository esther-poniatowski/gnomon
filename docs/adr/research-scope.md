---
tags:
  - decision
status: accepted
created: 2026-10-30
revised: 2026-10-31
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Research as the scope of gnomon
---
# Research as the scope of gnomon

> [!QUESTION] Goal: which tool specifies expositions, glossaries, audiences and project specifications, and which units does `gnomon` keep?

Two earlier decisions placed exposition in `gnomon`. The decision on [expositions as projections](expositions-as-projections.md) gave `gnomon` the exposition records, on two grounds. First, that decision held that an exposition depends on the definitions of the research records presented. Second, it expected no tool other than `gnomon` to read exposition records. The decision on [terminology, audience and project specifications](terminology-audience-project-specifications.md) did the same for glossaries, audiences and project specifications, on one ground: those records depend on the inquiry records and on the exposition records. Each ground now fails or shrinks. The dependence of an exposition on research shrinks to a contract of a few fields, stated in the decision below. A glossary and an audience depend on research only through the identifiers of concepts. The expectation of a single reader fails: a course, a piece of documentation or a decision record needs exposition as well, although no inquiry produced its ideas. Therefore, exposition records have readers outside research.

## Decision

`gnomon` specifies research only. Its records hold the content of an inquiry and the itinerary of the acts that produced that content. A separate project, `ekthesis`, specifies how an author arranges any argument for an audience:

- the selection and the order of its ideas;
- the relations between ideas, and the device that realizes each relation;
- glossaries and audiences.

One test places each record, field, check or note, by the work that needs it:

- a unit belongs to `gnomon` when an inquiry needs it to state, establish or check its content, whether or not an argument ever presents that content;
- a unit belongs to `ekthesis` when only the presentation of an argument to a reader needs it.

Under this test, the units divide as follows:

- **`gnomon` keeps** the research records, the concept record, the symbols declared by the records, and the notation. The notation refers to the records for those symbols, and declares three further parts:
    - the rules composing symbols from bases, modifiers and index sets;
    - the conventions of typography;
    - the LaTeX macros generated from the symbols.

    `gnomon` also receives the research root record of a project. That record holds the questions and the goals of the project.
- **`ekthesis` receives** the exposition records, together with the mechanisms serving them:
    - the status `core` or `elaboration` of a component of an argument;
    - the rhetorical relations, each with its devices;
    - the renaming of a symbol for the convention of a venue;
    - glossaries;
    - audiences;
    - the binding of a project to its glossary, its notation and its audiences.
- **The export of `gnomon` carries** each fact of a research record that a check of an exposition needs, so that `ekthesis` runs that check from the contract.
- **The `repository.yml` of a project holds** the identity of that project.

`gnomon` emits its units, their symbols and their relations as a generated export. `ekthesis` publishes the contract of that export. That contract fixes three kinds of entry:

- a presented unit, with its identifier, its kind and its statement, whose formulas name symbols by identifier;
- a symbol, with its identifier and its LaTeX macro;
- a relation between two units, with its source, its target and its class.

The classes follow the division drawn by Rhetorical Structure Theory between two kinds of relation [mann1988]. A subject-matter relation relates the contents of two units, and its intended effect is that the reader recognizes that relation. Cause, condition and contrast are relations of this kind. A presentational relation aims to increase an inclination of the reader, such as belief or the ability to understand. Motivation, background and concession are relations of this kind.

The records of `gnomon` fix the contents of research units. Therefore, an exposition may present a subject-matter relation between two research units only when the export records a relation of the same class. A presentational relation requires no relation from the export, with two exceptions, since the effect of each rests on a relation between the contents:

- an evidence presents one unit as support for a claim, and requires that the export record that support;
- an antithesis presents two units as incompatible, so that the reader favours one of them, and requires a recorded incompatibility.

Therefore, the classes of the contract are the subject-matter classes, together with support and incompatibility. `gnomon` records support by the relation `supports` between answers, but it records no incompatibility yet, so the class of incompatibility waits on the goal `relation-registry`. `gnomon` maps each exported relation onto one of these classes. That mapping lets `ekthesis` read the classes only, without a code dependency on `gnomon`.

An artifact may rename a symbol to follow the convention of its venue. The renaming changes the printed form of the symbol but keeps its identifier, so every check of `gnomon` still resolves the symbol. From the symbol entries of the contract alone, `ekthesis` checks that no two symbols of one artifact print alike.

## Constraints that decide the scope

- **The ideas of an argument may come from any activity.** Therefore, an exposition tool cannot depend on the fields of one source of ideas. The tool reads only the entries of the contract, and a check needing more binds the two tools.
- **Research does not need a reader.** Under the [criterion of an epistemic activity](../epistemology/processes/activities/epistemic-activities.md#^epistemic-criterion), an operation is epistemic only when its output is an epistemic object. Presenting a result to a reader outputs a text, not a new epistemic object. Therefore, the content and the warrant of a research unit stay the same for every reader.
- **The status `core` or `elaboration` is relative to one argument.** An argument may answer a question stated by no research record, so the same unit may be core in one argument and an elaboration in another. An assembly of research is also relative to a question, but to a question recorded by the inquiry. Its checks read the [grounds](../epistemology/objects/knowledge/grounds-and-dependence.md#^ground) of an answer. Those grounds follow from declared dependencies. In research, an act is relevant through the [open condition](../epistemology/processes/inquiry/choice-of-act.md#^open-condition) served by the act, so no declared status is needed.
- **Each family declares its own relations.** An epistemic act fixes the relation between the objects consumed and produced by the act. A rhetorical relation, such as an illustration, which falls under the abstraction–instance form of elaboration in Rhetorical Structure Theory [mann1988], or an antithesis, is realized by a device, such as a connector or a synthesis. Therefore, `gnomon` declares the relations between research units, `ekthesis` declares the rhetorical relations and the class of the contract required by each, and the contract of the export joins the two.
- **A concept and its symbols serve research, whereas its names serve readers.** A concept is produced by explication, and keeps one meaning. A researcher formulates and manipulates concepts in a notation, and writes derivations with its conventions and its macros, so the notation stays with research. An artifact selects among the symbols of that notation, many for a thesis and few for a poster, and may print a symbol in the convention of its venue. Therefore, neither the density nor the printed forms required by research bind an artifact. A research record names a concept by its identifier and its gloss, whereas the names admitted or forbidden for an audience matter only to a reader. Therefore, the glossary leaves `gnomon`.
- **A reference across tools creates no dependency.** Under the decision of `geonexus` on [tool roles](https://github.com/esther-poniatowski/geonexus/blob/0712bb5136960141f82ec65d5ae475834293af4a/docs/_decisions/tool-roles.md), a record of one field refers to a record of another field by a logical target, typed by the contract that the target must satisfy. Therefore, the project specification divides by the work that needs each part. The questions and the goals of a project state its inquiry, so they form a research root record of `gnomon`. The bindings to a glossary, a notation and audiences serve the presentation of the project, so they go to `ekthesis`. The binding names the notation of `gnomon` by a logical target. The identity of the project serves neither tool alone, and stays in its `repository.yml`.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| `gnomon` specifies research and exposition | One owner for the content and its presentations | An argument without research records still depends on `gnomon`, and the theory of inquiry of `gnomon` still specifies the rhetorical records |
| One repository holds two packages, research and exposition | The shared mechanisms are imported directly | The two packages release together, and an argument without research records still installs the repository of `gnomon` |
| Each consumer specifies its expositions | No new project | Each consumer restates the same schemas and checks |
| A separate exposition project, with each shared mechanism held by the tool that owns it | Each tool holds one family, and exposition works without research | Each tool follows the conventions shared by the record tools, besides the contract of the export |

The present decision takes the last option. Identifiers, schemas, typed relations and diagnostics serve other record tools as well. The decision on [tool roles](https://github.com/esther-poniatowski/geonexus/blob/0712bb5136960141f82ec65d5ae475834293af4a/docs/_decisions/tool-roles.md) assigns the addressing of records to Anagraphe, the delivery and the binding of schemas to Kleisis, and the format of findings to a gate. The mechanism of typed relations has no owner yet.

## Consequences

- The present decision supersedes the decision on [expositions as projections](expositions-as-projections.md). The present decision amends two others:
    - the decision on [terminology, audience and project specifications](terminology-audience-project-specifications.md) keeps the mechanism of the notation in `gnomon`, loses the glossary and the audience, and divides the project specification as the present decision states;
    - the decision on [concepts, glossaries and notations](concepts-glossaries-notations.md) keeps the concept record and the notation, and loses the glossary.
- The rule that an exposition adds no content, formerly a commitment of `gnomon`, leaves the theory of `gnomon`. In its place, `ekthesis` states a rule of provenance. Under that rule, each idea of an exposition takes one of two forms:
    - a reference to a unit of an external source;
    - an authored idea of a declared kind, such as an illustration, an analogy or a premise granted by the audience.

    For artifacts presenting research, `ekthesis` requires each idea that carries content about the objects of the inquiry to reference a research unit. That requirement keeps the guard against one failure named in the [motivation of `gnomon`](../../README.md#motivation): content held only in exposition.
- Two notes move to `ekthesis`: the note on [exposition](https://github.com/esther-poniatowski/ekthesis/blob/main/docs/theory/exposition.md), and the glossary half of the note on glossary and notation, now the note on the [glossary](https://github.com/esther-poniatowski/ekthesis/blob/main/docs/theory/glossary.md). The note on exposition counts `supports` among the relations matched by a subject-matter connector, whereas Rhetorical Structure Theory counts evidence as presentational [mann1988], so `ekthesis` corrects that reading under the contract above. The half that stays states that the notation serves research, and drops the claim that symbols belong to expression. The foundation notes, the inventory of [epistemic objects](../epistemology/objects/status/epistemic-objects.md) and the README drop the exposition family. The note on [virtues](../epistemology/objects/task/epistemic-pragmatic-virtues.md) names the form of a representation, rather than the form of its presentation.
- The candidate relation `exemplifies` of the [proposals for the relation registry](../proposals/relation-registry.md#examples-as-relations), from a case to a concept or an answer, stays in `gnomon` with its five uses:
    - four uses test or establish a claim: `witness`, `counterexample`, `boundary-case` and `construction`;
    - the use `instance` relates an existing case to the illustrated concept or answer. An exposition that presents this illustration relates two research units, so the relation must be recorded in `gnomon`; only an authored illustration needs no record.
- The goals of `gnomon` divide as follows:
    - `exposition-family` moves to `ekthesis`;
    - `relation-registry` keeps the relations between research units;
    - `assembly-schema` keeps the gaps of an assembly, its limits of validity and its deferred components. The goal also keeps the query of the laws to which an answer is exposed, computed over the grounds of the answer rather than over a declared status, as the [exposure rule](../epistemology/objects/knowledge/grounds-and-dependence.md#^weakest-link) states. The status `core` or `elaboration`, the views and the check of the core route move;
    - `vocabulary-records` keeps the concept record, the notation and the research root record of a project; the glossary, the audience and the bindings of a project move;
    - `record-view` stays, since a researcher checks a record through its view, and the view presents no argument.
- The schema and the template of the notation, and the checks of symbols, move from `geonexus` to `gnomon`, in the order of extraction set by the decision on tool roles. The project specifications of the standalone projects migrate in the same order: their questions and goals become research root records.
- The export is a copy generated from its sources. The [rule of one source](one-source-per-unit.md#^generated-copies-only) admits such a copy.
- The moved files keep their history, carried by `git filter-repo`.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). A mark ◐ records a check of the bibliographic record.

- [mann1988] ◐ [Mann & Thompson, "Rhetorical Structure Theory: toward a functional theory of text organization", *Text* 8(3), 243–281, 1988](https://doi.org/10.1515/text.1.1988.8.3.243); subject-matter and presentational relations
