---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Starting an inquiry from an empty folder
---
# Starting an inquiry from an empty folder

This tutorial builds a new inquiry from an empty folder up to a first candidate answer that `gnomon check` accepts. Each record is filled at the commitment `identified`, and the check runs after each stage, so the tutorial shows what the check reports and how each finding is repaired.

> [!IMPORTANT] Prerequisites
> The package is installed, as the [installation guide](installation.md) states. The commands run from any folder, and the [guide to filling the records](filling-records.md) states the rules that the tutorial applies.

## The problem of the tutorial

The tutorial asks why the period of a pendulum grows with its amplitude. For small swings, the period of a pendulum does not depend on the amplitude; for large swings, the period grows. The problem requires no expertise beyond elementary mechanics, so the reader can attend to the records rather than to the domain.

The inquiry stops at a first candidate answer stated in words. The records stay at the commitment `identified`, so no quantity is declared and no formula is written. Stage 4 of the [order of specification](../epistemology/processes/inquiry/specification-order.md), described by the filling guide, raises a record to the commitment `specified`.

## Create the folder

The following command creates the folder of the problem, with the templates of the first four stages, the itinerary, and an index listing them in the order in which they are filled:

```sh
gnomon init pendulum
```

```text
pendulum/itinerary.yml: written
pendulum/problem.yml: written
pendulum/question.yml: written
pendulum/target-system.yml: written
pendulum/phenomenon.yml: written
pendulum/background.yml: written
pendulum/operators.yml: written
pendulum/_index.md: written
Fill the records in the order of pendulum/_index.md, then run: gnomon check pendulum
```

The check of the new folder shows the starting point:

```sh
gnomon check pendulum
```

```text
0 records checked in 0 folders, 0 findings, 0 warnings, 7 templates not yet filled
```

The check counts apart, and does not check, a template whose identifier still holds its placeholder, such as `prob.TOPIC.NAME`. A record is filled by replacing the lines below the header of its template. The header names the specification notes of the record. The comment of each field states what the field holds, and glosses each admitted value. A record keeps only the lines that it fills, and the other lines of its template are deleted.

## Stage 1: state the problem

The problem states what a solution must deliver. The following body of `problem.yml` demands the factor of the pendulum that makes its period grow, and requires that a solution recover the small-swing period:

```yaml
_schema: gnomon:problem@1
title: "Growth of the period of a pendulum with its amplitude"
statement: "The period of a pendulum is independent of its amplitude for small swings, but grows for large swings; the factor responsible for the growth is sought"
id: prob.pendulum.period-growth
type: problem
status: posed
kind: empirical
demand: "the factor of the pendulum that makes its period grow with its amplitude"
result_type: explanation
request: one
associated_question:
constraints:
  - name: "agreement with the small swings"
    statement: "a solution recovers a period independent of the amplitude in the limit of small swings"
    source: "Landau and Lifshitz, Mechanics, section 11, problem 1"
explicanda:
  - term: "large swing"
    pointer: "Landau and Lifshitz, Mechanics, section 11, problem 1"
sources:
  - "Landau and Lifshitz, Mechanics, section 11, problem 1"
significance: "the departure of a restoring force from linearity governs the dependence of the period on the amplitude in every nonlinear oscillator"
knowledge_obstacles: []
answerability_obstacles: []
```

Three choices in this record follow from the specification of the problem:

- the result type `explanation` and the request `one` type the demand: one explanation is sought;
- the field `associated_question` stays empty, since no question record exists yet. A reference to a missing record is reported under the rule `vocabulary/unknown-record`;
- the two lists of obstacles stay empty. The obstacle of the problem while no answer is proposed, an open gap, is computed from the records by `gnomon views`, so it need not be stated.

The identifier `prob.pendulum.period-growth` opens on the prefix of its type, followed by the topic `pendulum`, which every record of the problem shares, and by the name of the record.

The itinerary records each act of the inquiry as a step, from the statement of the problem on. The following body of `itinerary.yml` holds the first step, an instance of the activity `problematization`, whose norm the researcher judged:

```yaml
_schema: gnomon:itinerary@1
title: "Itinerary of the inquiry into the growth of the period"
id: itin.pendulum.explain-growth
type: itinerary
addresses: prob.pendulum.period-growth

steps:
  - id: pose
    activity: problematization
    inputs:
      - type: source
        ref: "Landau and Lifshitz, Mechanics, section 11, problem 1"
    output:
      type: problem
      ref: prob.pendulum.period-growth
    norm:
      test: norm.problematization
      verdict: pass
      evidence: "The problem states its demand and its constraint, and its explicandum points to its source."
      judged: "2026-11-08"
    rationale:
      serves: prob.pendulum.period-growth
    mode: non-inferential
```

The check now reads two records:

```text
2 records checked in 1 folders, 0 findings, 0 warnings, 5 templates not yet filled
```

## Stage 2: type the question

The question types the answer that the problem demands, before its subject is identified. In this state, called a question schema, each slot of the subject holds a placeholder that describes the record awaited. The following body of `question.yml` asks why the period grows rather than keeps its small-swing value:

```yaml
_schema: gnomon:question@1
title: "Explanation of the growth of the period"
statement: "Why does the period of a pendulum grow with its amplitude, rather than stay at its value for small swings?"
id: quest.pendulum.explain-growth
type: question
status: posed
addresses: prob.pendulum.period-growth
request: one
links: []
subject:
  target_system:
    placeholder: system
    description: "a rigid pendulum swinging in a uniform gravitational field"
  background: []
  phenomenon:
    placeholder: phenomenon
    description: "the growth of the period with the amplitude"
  contrast:
    locus: other-outcome
    foil_set:
      - name: "constant period"
        reading: "the period keeps its value for small swings at every amplitude"
    compatibility: derived
    foil_status: counterfactual

task:
  epistemic_aim: explanation
  requested_relation: nomological
  modal_strength: actual
  admissible_explanans:
  required_accuracy:
    standard: qualitative

virtues: []
```

The contrast states what the explanation must rule out: the foil "constant period" is the other outcome of the same pendulum, and it is counterfactual, since no large swing keeps the small-swing period. The task asks for an explanation by laws, the relation `nomological`, of the actual behavior, with a qualitative accuracy.

The question now exists, so the field `associated_question` of the problem names it:

```yaml
associated_question: quest.pendulum.explain-growth
```

The step `formulate` is appended to the steps of the itinerary. Its output is the type `question-schema`, and it names no record, since the schema will become the question once its slots name records:

```yaml
  - id: formulate
    activity: question-formulation
    inputs:
      - type: problem
        ref: itin.pendulum.explain-growth.pose
    output:
      type: question-schema
    norm:
      test: norm.question-formulation
      verdict: pending
    rationale:
      serves: quest.pendulum.explain-growth
      acts_on: answer-type
    mode: non-inferential
```

The input of the step names the step `pose` by its full identifier, the identifier of the itinerary followed by the identifier of the step. The check reads three records:

```text
3 records checked in 1 folders, 0 findings, 0 warnings, 4 templates not yet filled
```

The command `gnomon status` states, for each question, the conditions of answerability still open and the acts that can address them:

```sh
gnomon status pendulum
```

```text
quest.pendulum.explain-growth [selection]
  open definiteness
    ready: explication, explicit-definition
    waiting for an input: operationalization (concept), concept-revision (concept; phenomenon), delimitation (question; identified-subject), formalization (model), phenomenon-specification (identified-subject; target-specification)
  open candidates: no answer recorded yet
    waiting for an input: abduction (phenomenon), induction (data), analogical-inference (model; phenomenon), causal-inference (data; model), decomposition-localization (phenomenon; target-specification), model-analogy (model), de-idealization (model), idealization (model), abstraction (model), formalization (model), fitting (model; data), derivation (admitted-laws | model | target-claim), critique (model | target-claim), admissibility-check (model | target-claim; question), model-assembly (target-specification; admitted-laws), result-retrieval (question; target-claim)
each ready act can be taken now; the choice among them is the researcher's, as docs/procedures/inquiry/next-act.md states
each activity is defined in the note of its family, which docs/epistemology/processes/activities/_index.md lists; a name in parentheses is the type of the missing input, which docs/epistemology/processes/activities/epistemic-activities.md defines
```

Most acts wait for an input. In particular, the activity `abduction`, which proposes a candidate answer, waits for a phenomenon, a record that the next stage writes. The two ready acts, `explication` and `explicit-definition`, would make the explicandum "large swing" exact; this tutorial leaves it as stated.

## Stage 3: identify the target and the phenomenon

The subject fixes the object of the question, so that each slot of the question names a record. At the commitment `identified`, a record fixes its referent by a definite description and pointers, and declares no quantity. The following body of `target-system.yml` identifies the class of rigid pendulums:

```yaml
_schema: gnomon:target-system@1
title: "Rigid pendulum in a uniform gravitational field"
id: system.rigid-pendulum
type: target-system
status: provisional
commitment: identified
target_type: actual-systems

identification:
  description: "a rigid body that swings without friction about a fixed horizontal axis, under a uniform gravitational field"
  pointers:
    - "Landau and Lifshitz, Mechanics, section 11, problem 1"

reference_class:
  name: "rigid pendulum"
  projectibility:
    status: not-claimed
```

A target system takes a topic of its own, so its identifier is `system.rigid-pendulum`, with no second segment. The projectibility `not-claimed` states that no claim about some pendulums is projected onto the whole class.

The following first draft of `phenomenon.yml` identifies the growth of the period:

```yaml
_schema: gnomon:phenomenon@1
title: "Growth of the period with the amplitude"
statement: "the period of a rigid pendulum grows with the amplitude of its swing"
id: phen.pendulum.period-growth
type: phenomenon
status: provisional
commitment: identified
target_system: system.rigid-pendulum

identification:
  description: "the increase of the period of a frictionless rigid pendulum as its amplitude grows from small swings toward a half turn"
  pointers:
    - "Landau and Lifshitz, Mechanics, section 11, problem 1"

category: regularity
occurrence: process
evidential_status: established
```

The two slots of the question now name these records, in place of their placeholders:

```yaml
  target_system: system.rigid-pendulum
  background: []
  phenomenon: phen.pendulum.period-growth
```

The step `identify` is appended to the itinerary, with the input `itin.pendulum.explain-growth.formulate`, the output type `identified-subject` and the reference `phen.pendulum.period-growth`. The check then reports one finding:

```text
phenomenon.yml: phen.pendulum.period-growth: completeness/mismatched-occurrence: occurrence: process is no occurrence class of a regularity, which admits not-applicable
5 records checked in 1 folders, 1 findings, 0 warnings, 2 templates not yet filled
```

The line names the file, the record, the rule and the field, then the defect and its repair. A regularity, such as the dependence of the period on the amplitude, is no single occurrence, so its occurrence class is `not-applicable`. The category and the occurrence class are required only from the commitment `specified`, so an identified record may also leave both out; once stated, they are checked. Writing `occurrence: not-applicable` returns the check to no finding:

```text
5 records checked in 1 folders, 0 findings, 0 warnings, 2 templates not yet filled
```

## Stage 5: propose a first candidate answer

A record is raised to the commitment `specified` only when an open condition of a question requires it, so this tutorial passes over stage 4 and proposes a candidate answer in words. The following command adds the answer template to the folder and keeps the records already filled:

```sh
gnomon init pendulum --with answer
```

```text
pendulum/answer.yml: written
pendulum/_index.md: updated
7 existing files kept
Fill the records in the order of pendulum/_index.md, then run: gnomon check pendulum
```

The candidate answer attributes the growth of the period to the restoring torque of gravity, which grows more slowly than the angle of the swing. Its claim stays unformalized: the field `expression` is empty, and the caveat names the gap. The following first draft of `answer.yml` states the claim, its grounds, its route and its explanatory block:

```yaml
_schema: gnomon:answer@1
title: "Restoring torque weaker than linear"
id: ans.pendulum.weak-restoring-torque
type: answer
answers: quest.pendulum.explain-growth

claim:
  reading: "the restoring torque of gravity grows more slowly than the angle of the swing, so a large swing is pulled back less strongly than a linear oscillator of the same small-swing period would be, and takes longer"
  expression:
  caveat: "the claim is not formalized, since the target system declares no quantity yet"

grounds:
  - id: rigid-frictionless
    role: assumption
    content: "the pendulum is rigid and swings without friction about a fixed axis"
    record: system.rigid-pendulum
  - id: sine-torque
    role: warrant
    content: "the restoring torque of gravity is proportional to the sine of the angle of the swing"

route:
  kind: derivation
  runs_on: [system.rigid-pendulum]
  pointer: "Landau and Lifshitz, Mechanics, section 11, problem 1"

status: entertained
support: informal
modal_strength: actual

erotetic_relation:
  value: complete

aim_block:
  explanation:
    contrastive_explanandum: "the period grows with the amplitude, rather than keeping its value for small swings"
    relation: nomological
    factors:
      - id: sublinear-torque
        name: "restoring torque weaker than linear"
        factor: law-property
        holds:
        caveat: "the claim of the factor is not formalized, since the target system declares no quantity yet"
```

The step `propose` is appended to the itinerary: an instance of the activity `abduction`, with the phenomenon as input and the answer as output. Its output type is `target-claim`, the type that the [activity registry](../../src/gnomon/data/registries/activities.yml) fixes for `abduction`; the command `gnomon itinerary` reports any other type. The check then reports three findings and one warning:

```text
answer.yml: ans.pendulum.weak-restoring-torque: completeness/unmet-requirement: always required: dependence
answer.yml: ans.pendulum.weak-restoring-torque: warning: completeness/unstated-domain: domain: not stated, although the route is a derivation
answer.yml: ans.pendulum.weak-restoring-torque: completeness/unmet-requirement: always required: aim_block.explanation.explanatory_claim
answer.yml: ans.pendulum.weak-restoring-torque: completeness/unmet-requirement: always required: aim_block.explanation.factors[].target_status
6 records checked in 1 folders, 3 findings, 1 warnings, 2 templates not yet filled
```

Each finding names a field that every answer requires. The three blocks below fill them:

- the dependence states that the two grounds suffice for the claim;
- the explanatory claim names the determinant: the property of the law that makes it relevant to the growth of the period;
- the target status `denoting` states that the factor bears on a quantity of the target itself, its restoring torque, rather than on a limit system or a coarse description of it.

```yaml
dependence:
  - kind: minimal-set
    grounds: [rigid-frictionless, sine-torque]
```

```yaml
    explanatory_claim:
      - ground: sine-torque
        explanatory: true
        determinant: "the sine grows more slowly than its argument"
```

```yaml
        target_status: denoting
```

The block `dependence` follows the grounds, the explanatory claim precedes the relation, and the target status closes the factor. With these blocks, the check reports only the warning:

```text
answer.yml: ans.pendulum.weak-restoring-torque: warning: completeness/unstated-domain: domain: not stated, although the route is a derivation
6 records checked in 1 folders, 0 findings, 1 warnings, 2 templates not yet filled
```

A warning fails no check, and the command exits with code 0. This warning anticipates the scope test of the assessment, since a derivation holds only over a domain of conditions. The domain is written over declared symbols, so it is stated once the target reaches the commitment `specified`. The two templates not yet filled, the background and the operator record, serve stage 4.

## Read the next acts

The command `gnomon status` now reads the answer among the records:

```text
quest.pendulum.explain-growth [selection]
  open definiteness
    ready: explication, explicit-definition, delimitation
    waiting for an input: operationalization (concept), concept-revision (concept), formalization (model), phenomenon-specification (target-specification)
  open candidates: 1 answer recorded, none yet passes the admissibility tests of an assessment
    ready: abduction, derivation, critique, admissibility-check, result-retrieval
    waiting for an input: induction (data), analogical-inference (model), causal-inference (data; model), decomposition-localization (target-specification), model-analogy (model), de-idealization (model), idealization (model), abstraction (model), formalization (model), fitting (model; data), model-assembly (target-specification; admitted-laws)
each ready act can be taken now; the choice among them is the researcher's, as docs/procedures/inquiry/next-act.md states
each activity is defined in the note of its family, which docs/epistemology/processes/activities/_index.md lists; a name in parentheses is the type of the missing input, which docs/epistemology/processes/activities/epistemic-activities.md defines
```

Two conditions stay open:

- definiteness, since the question asserts no state for it, and the definiteness of a term can be established only once its record reaches the commitment `specified`. The ready act `delimitation` writes the formal declarations of the target, as stage 4 does;
- candidates, since one answer is recorded and no assessment of it passes the admissibility tests. The ready act `admissibility-check` produces those verdicts, in an assessment record added by `gnomon init pendulum --with assessment`.

The choice between these acts is the researcher's, as the [choice of the next act](../procedures/inquiry/next-act.md) states. The command `gnomon tree` prints the chain of records built so far:

```text
problem prob.pendulum.period-growth: Growth of the period of a pendulum with its amplitude [posed]
  question quest.pendulum.explain-growth: Explanation of the growth of the period [posed]
    answer ans.pendulum.weak-restoring-torque: Restoring torque weaker than linear [entertained]
```

## Continue the inquiry

The [guide to filling the records](filling-records.md) states how a record is raised to the commitment `specified`, with its quantities, its laws and its formulas. The tutorial [following one inquiry](tutorial.md) reads a complete inquiry, from its problem to the assessment of its candidate answer. The following command removes the folder of this tutorial:

```sh
rm -rf pendulum
```
