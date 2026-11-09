---
tags:
  - decision
status: accepted
created: 2026-11-09
revised: 2026-11-09
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Assembly of a level
---
# Assembly of a level

> [!QUESTION] Goal: which records state the assembly of a level of an inquiry, which part of it is authored, and which rule computes the rest?

A level of an inquiry is a problem, or a question that other questions serve. The assembly of a level lists its components, the parts of its answer, the citations between them, the dependencies still open, its limits of validity and the parts that it leaves out. The pilot of a research project gave each level a record of its own. That record stated each dependency a second time, beside the links, the answers and the relations. The options weighed below include the four candidate formalisms of the proposal for the assembly schema, which this decision retires. The theory of a level belongs to the [assembly of a level](../epistemology/processes/inquiry/question-decomposition.md#^assembly-level) in the note on question decomposition.

## Decision

The assembly of a level is a computed view, `gnomon:view.assembly@1`, and no record kind. An assembly fails five of the seven [conditions of admission](record-kind-admission.md#^admission-conditions): ^assembly-view

- its identity depends on its level;
- no other record cites it;
- its checks read the records of its components;
- a rule generates its content from the records;
- the questions, links, answers and relations already state that content.

Each part of the answer to a level is an answer of its own, to a question linked to the level by `subquestion-of`, as the [parts of an answer](../epistemology/processes/inquiry/question-decomposition.md#^parts-as-answers) state. The level question holds the synthesis, an answer that the parts support by `supports`. A question whose demand is a conjunction of its parts also holds a synthesis. A part that is not a claim is a record obtained by a step of an itinerary. The rationale of that step serves the component and acts on the condition `obtaining`. ^parts-as-answers

The parts that a level leaves out form the only authored element of its assembly. They are stated in the field `excludes` of the level question, as the [parts left out by a level](../epistemology/processes/inquiry/question-decomposition.md#^excluded-parts) define them. A deferred part keeps its link and counts as open. Deferring a part leaves the version of the question unchanged. A part out of scope is no component. Adding such a part revises the question and raises its version, as the [version of a question](../specification/question.md#^question-version) requires. ^excludes-field

One function returns the questions of a problem: the questions that address it and narrow no other question, as the question tree shows them. The demand met, the obstacles and the answers of a problem are read from the answers to these questions only. Therefore, an accepted answer to a subquestion never meets the demand of a problem, whereas the accepted synthesis can. ^problem-questions

The view computes each table by a declared rule, which reports a value and adds no claim, as the [boundary of computation](no-run-time-inference.md#^admitted-computation) admits: ^assembly-rules

- `levels`: each problem, and each question with a component, with the number of its parts, the number settled, and its accepted synthesis;
- `components`: the questions that serve a level, read from the links in the direction that the [decomposition graph](../epistemology/processes/inquiry/question-decomposition.md#^decomposition-graph) fixes, and, for a problem, the questions of the problem;
- `parts`: the answers to each supplying component, and the constructs obtained for it, with the state of their assessments;
- `citations`: each link between two questions of the level, and each edge of an answer to one of them whose other end is an answer to another, or a unit inside it, with the record and the field that state it;
- `gaps`: each supplying component not settled, deferred or open, a decomposed question with no accepted synthesis, and each accepted part or synthesis without a satisfied assessment against the present version;
- `limits`: the domain restrictions and the limit of the level question, the domain, conditions, idealization ranges, abstractions and variant of each accepted part and synthesis, and the parts out of scope, listed and never combined;
- `excluded`: the entries of `excludes`.

A component is settled once an accepted answer to it, or a stabilized construct obtained for it, holds a satisfied assessment against the present version of its question.

The exposure of each part is not repeated: the [exposure view](../../src/gnomon/data/schemas/views/exposure.schema.yml) reports it by answer.

Three checks read the decomposition of a question: ^decomposition-checks

- `completeness/misplaced-exclusion`, an error: a deferred part names a question that is no subquestion of its question, or a part out of scope names a question that still is one;
- `completeness/excluded-answered`, a warning: a deferred subquestion holds an accepted answer, so its deferral is stale;
- `completeness/answered-with-open-component`, a warning: a question marked `answered` has a subquestion that is not settled.

## Constraints that decide the assembly

- **A tool never judges sufficiency.** A decomposition certifies erotetic implication, under which each part narrows the answers to the level. The researcher certifies joint sufficiency by accepting the [synthesis](../epistemology/processes/inquiry/question-decomposition.md#^synthesis-answer). Therefore, a count of settled parts feeds no demand.
- **One answer holds one claim.** A level whose answer needs several claims needs several answers, and two answers to one question compete.
- **Every unit has one authored source.** The components, parts and citations are stated by the links, the answers and the relations, so the assembly may only report them, as the [decision on one source per unit](one-source-per-unit.md) requires.
- **A deferral is relative to its level.** A question can serve several levels, so a deferral is not a property of the deferred question.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| A record kind `assembly` | One file per level, as the pilot wrote it | An assembly fails five of the seven conditions of admission |
| An authored block `architecture` on the question, listing its components, its parts and its citations | The level is read in one place | Each entry restates a link, an answer or a relation, and needs a check that the block matches them |
| A key `output` on the answer, listing typed parts | One answer per level | An answer would hold several claims, and a part could carry no grounds of its own |
| A synthesis that answers a subquestion of its own | The level question holds no answer | That subquestion has the direct answers of the level question, so it restates the level question |
| No synthesis on a question whose demand is a conjunction, with a norm of joint sufficiency on a step | No answer restates the conjunction of its parts | Two rules decide whether a demand is met, and the restated conjunction is short and cites its parts |
| Counting the settled parts as meeting the demand | No synthesis to write | The tool would assert a joint sufficiency that no record states |
| A status `deferred` on the deferred question | No new field | A deferral would become absolute, whereas it is relative to one level |
| Inquiry-relative relations: selected for, load-bearing for, bridge for, deferred in, ordered before in | Each role of a component is named | Each restates the input or the rationale of a step, the dependence of an answer, a bridging condition, an exclusion, or a reading order that belongs to `ekthesis` |
| A check that flags a unit as a candidate record | Promotion of a unit is prompted | Whether a unit deserves a record is a judgment, and a dotted identifier already makes every unit citable |

## Consequences

- The view `gnomon:view.assembly@1` joins the views of `gnomon views`, and its schema joins the exports of the [schema resources](../../specs/schema-resources.yml).
- The question schema gains the optional field `excludes`, and the question contract stays at version 1, since an optional field leaves every valid record valid.
- The demand met, the obstacles and the answers of a problem read only the questions of the problem, so an answer to a subquestion that also names the problem no longer meets its demand.
- The [global revisions of a question](../epistemology/processes/inquiry/question-decomposition.md#^global-revision) include the removal of a part.
