---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Starting an inquiry from an empty folder
---
# Starting an inquiry from an empty folder

This tutorial builds a new inquiry from an empty folder up to a first candidate answer that `gnomon check` accepts. Ekphrasis supplies the forms in Obsidian, while Gnomon creates records, checks the inquiry and generates operational views. Each record is filled at the commitment `identified`, and the check runs after each stage, so the tutorial shows what the check reports and how each finding is repaired.

> [!IMPORTANT] Prerequisites
> Install Gnomon in a dedicated Python environment, as the [installation guide](installation.md) states. Create or select a folder for the research, and open that folder as an Obsidian vault. Install and enable Ekphrasis by following its [installation guide](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/guide/installation.md). If another plugin, such as YAML Editor, claims `.yml` or `.yaml` files, disable it while following this tutorial. Run every terminal command from the vault root with the dedicated environment active. The [guide to filling the records](filling-records.md) states the Gnomon rules that the tutorial applies.

## The problem of the tutorial

The tutorial asks why the period of a pendulum grows with its amplitude. For small swings, the period of a pendulum does not depend on the amplitude; for large swings, the period grows. The problem requires no expertise beyond elementary mechanics, so the reader can attend to the records rather than to the domain.

The inquiry stops at a first candidate answer stated in words. The records stay at the commitment `identified`, so no quantity is declared and no formula is written. Stage 4 of the [order of specification](../epistemology/processes/inquiry/specification-order.md), described by the filling guide, raises a record to the commitment `specified`.

## Prepare the vault and inquiry folder

First, install the Gnomon form contracts in the current vault:

```sh
gnomon setup .
```

```text
103 schema files available; 104 files written, 0 unchanged
Set Ekphrasis Schema registry to: .gnomon/schema-registry.yml
```

The exact counts can increase when Gnomon adds a contract. The final line is the value needed by Ekphrasis. The generated directory defaults to `.gnomon/schemas`; both that directory and the registry path can be changed through the [setup options](cli-reference.md#cli-setup).

Then, create the inquiry folder. The option `--with` adds additional records when the inquiry requires them.

```sh
gnomon init pendulum
```

```text
pendulum/itinerary.yml: written
pendulum/problem.yml: written
pendulum/_index.md: written
Fill the records in the order of pendulum/_index.md, then run: gnomon check pendulum
```

The check of the new folder shows the starting point:

```sh
gnomon check pendulum
```

```text
0 records checked in 0 folders, 0 findings, 0 warnings, 2 templates not yet filled
```

The check counts apart, and does not check, a template whose identifier still holds its placeholder, such as `prob.TOPIC.NAME`.

## Connect the folder to Ekphrasis

Ekphrasis needs the Gnomon registry and the Python interpreter of the environment that runs Gnomon. Print the absolute interpreter path: ^ekphrasis-setup

```sh
python -c "import sys; print(sys.executable)"
```

In **Settings → Ekphrasis**, set these values:

- **Schema registry:** `.gnomon/schema-registry.yml`
- **Python interpreter:** the absolute path printed by the preceding command
- **Post-creation command:**

  ```json
  ["-m", "gnomon", "register", "{vault}/{path}"]
  ```

- **Primary-view command:**

  ```json
  ["-m", "gnomon", "views", "{vault}/pendulum", "--scope", "{target}", "--output", "{vault}/pendulum/views", "--result", "json"]
  ```

Open `pendulum/problem.yml`, then run the command *Diagnose setup*. The groups *Blocks schema-derived forms* and *Blocks saving authored records* must pass. The [recovery guide](recovery.md) covers a schema or Python-runtime failure. A message that no custom checker is registered does not block this tutorial, because its Gnomon checks run in the terminal.

The record should now open as a form. For every YAML block below, enter the displayed values through that form; the block shows the resulting saved source, not text to paste over the file. A text field saves after a pause or when focus leaves it. *Toggle form and source view* lets you compare the saved source with the block without making source editing the normal workflow.

The initial form displays the fields needed to state the problem. Optional branches remain behind *+ Add a field* until the inquiry needs them. The complete commented source template remains available through `gnomon init --full-template` for source-based authoring.

## Stage 1: state the problem

Use the [problem-record fields](../specification/problem.md) to state what a solution must deliver. In this inquiry, fill the form of `problem.yml` so that its saved body demands the factor of the pendulum that makes its period grow, and requires that a solution recover the small-swing period:

```yaml
_schema: gnomon:problem@3
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

Three choices in this record apply the [problem-record specification](../specification/problem.md):

- the result type `explanation` and the request `one` type the demand: one explanation is sought;
- the field `associated_question` stays empty, since no question record exists yet. A reference to a missing record is reported under the rule `vocabulary/unknown-record`;
- the two lists of obstacles stay empty. The obstacle of the problem while no answer is proposed, an open gap, is computed from the records by `gnomon views`, so it need not be stated.

Under the [record-identifier form](../adr/dotted-identifiers.md#^identifier-form), the worked identifier is `prob.pendulum.period-growth`: its prefix names the type, its topic is `pendulum`, and its final segment names the record.

Open `itinerary.yml` and use the [fields of an itinerary step](../specification/itinerary.md) to record the first tracked act. This step instantiates the activity `problematization`, and its norm carries the judgment of the researcher:

```yaml
_schema: gnomon:itinerary@3
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

Run `gnomon check pendulum` again. The check now reads two records:

```text
2 records checked in 1 folders, 0 findings, 0 warnings, 0 templates not yet filled
```

Run *Open primary view* in Obsidian, enter `problem-posed`, then select *Generate and open*. Gnomon generates the `problem-state` view. Read its demand, obstacles, closure state and coverage statement. This view is computed from the inquiry; it is not another authored record.

## Stage 2: type the question

Create a [question schema](../epistemology/objects/question/question.md#^question-schema) for the answer that the problem demands. At this stage, the [target and phenomenon slots](../specification/question-subject.md#^placeholder-slots) hold typed placeholders for the records awaited.

Run *Create instance* in Obsidian, choose *Question record — gnomon:question@3*, and enter `pendulum/question.yml`. Ekphrasis creates and opens the form. Its post-creation command asks Gnomon to add the question under stage 2 of `pendulum/_index.md`.

Fill the new form so that the saved record asks why the period grows rather than keeps its small-swing value:

```yaml
_schema: gnomon:question@3
title: "Explanation of the growth of the period"
statement: "Why does the period of a pendulum grow with its amplitude, rather than stay at its value for small swings?"
id: quest.pendulum.explain-growth
type: question
status: posed
version: "1"
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

The worked [contrast](../specification/question-subject.md#^contrast-fields) must rule out the foil "constant period". This foil is counterfactual because no large swing keeps the small-swing period. The worked [epistemic task](../specification/question-task.md) asks for an explanation by laws, through the relation `nomological`, of the actual behavior, with qualitative accuracy.

The question now exists, so reopen the problem form and make its field `associated_question` name the question:

```yaml
associated_question: quest.pendulum.explain-growth
```

Reopen the itinerary form and append the step `formulate`. Its output is the type `question-schema`, and it names no record, since the schema will become the question once its slots name records:

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
3 records checked in 1 folders, 0 findings, 0 warnings, 0 templates not yet filled
```

Run *Open primary view* with the target `question-typed`. Gnomon opens the `next-act` view, which distinguishes conditions that are open now, activities that are ready and activities waiting for an input. Its coverage statement identifies the records used to compute this state.

The command `gnomon status` states, for each question, the conditions of answerability still open and the acts that can address them:

```sh
gnomon status pendulum
```

```text
quest.pendulum.explain-growth [selection]
  open definiteness
    ready: explication, explicit-definition
    waiting for an input: operationalization (concept), concept-revision (concept; phenomenon), delimitation (question; identified-subject; admitted-laws), formalization (model), phenomenon-specification (identified-subject; target-specification)
  open candidates: no answer recorded yet
    waiting for an input: abduction (phenomenon), induction (data), analogical-inference (model; phenomenon), causal-inference (data; model), decomposition-localization (phenomenon; target-specification), model-analogy (model), de-idealization (model), idealization (model), abstraction (model), formalization (model), fitting (model; data), derivation (admitted-laws | model | target-claim), critique (model | target-claim), admissibility-check (model | target-claim; question), model-assembly (target-specification; admitted-laws), result-retrieval (question; target-claim)
each ready act can be taken now; the choice among them is the researcher's, as docs/procedures/inquiry/next-act.md states
each activity is defined in the note of its family, which docs/epistemology/processes/activities/_index.md lists; a name in parentheses is the type of the missing input, which docs/epistemology/processes/activities/epistemic-activities.md defines
```

Most acts wait for an input. In particular, the activity `abduction`, which proposes a candidate answer, waits for a phenomenon, a record that the next stage writes. The two ready acts, `explication` and `explicit-definition`, would make the explicandum "large swing" exact; this tutorial leaves it as stated.

## Stage 3: identify the target and the phenomenon

Identify the [subject of the question](../epistemology/objects/subject/subject-of-inquiry.md) by replacing its placeholders with records. The target and phenomenon remain at the [commitment `identified`](../epistemology/objects/question/question.md#^commitment-levels), so their descriptions and pointers fix their referents without formal declarations.

Run *Create instance* twice. Choose *Target system record — gnomon:target-system@2* and enter `pendulum/target-system.yml`; then choose *Phenomenon record — gnomon:phenomenon@2* and enter `pendulum/phenomenon.yml`. Gnomon places both entries under stage 3 of the inquiry index.

Fill the form of `target-system.yml` so that it identifies the class of rigid pendulums:

```yaml
_schema: gnomon:target-system@2
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

The [record-identifier form](../adr/dotted-identifiers.md#^identifier-form) gives a target system its own topic, so the worked identifier is `system.rigid-pendulum`. The [projectibility field](../specification/target-system.md) takes the value `not-claimed` because this inquiry projects no claim from some pendulums onto the whole class.

Fill the form of `phenomenon.yml` with this first identification of the growth of the period:

```yaml
_schema: gnomon:phenomenon@2
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

Reopen the question form and make its two subject slots name these records, in place of their placeholders:

```yaml
  target_system: system.rigid-pendulum
  background: []
  phenomenon: phen.pendulum.period-growth
```

Append the step `identify` through the itinerary form, with the input `itin.pendulum.explain-growth.formulate`, the output type `identified-subject` and the reference `phen.pendulum.period-growth`:

```yaml
  - id: identify
    activity: subject-identification
    inputs:
      - type: question-schema
        ref: itin.pendulum.explain-growth.formulate
    output:
      type: identified-subject
      ref: phen.pendulum.period-growth
    norm:
      test: norm.subject-identification
      verdict: pass
      evidence: "The target and phenomenon are fixed by definite descriptions and pointers at the commitment identified."
      judged: "2026-11-08"
    rationale:
      serves: quest.pendulum.explain-growth
      acts_on: definiteness
    mode: non-inferential
```

Run `gnomon check pendulum`. The check reports one finding:

```text
phenomenon.yml: phen.pendulum.period-growth: completeness/mismatched-occurrence: occurrence: process is no occurrence class of a regularity, which admits not-applicable
5 records checked in 1 folders, 1 findings, 0 warnings, 0 templates not yet filled
```

The line names the file, record, rule and field, followed by the defect and its repair. Under the [occurrence classes admitted by each phenomenon category](../specification/phenomenon.md#^occurrence-by-category), the worked regularity is not a single occurrence, so its occurrence class is `not-applicable`. These fields may be omitted at the commitment `identified`; once stated, they are checked. Writing `occurrence: not-applicable` returns the check to no finding:

```text
5 records checked in 1 folders, 0 findings, 0 warnings, 0 templates not yet filled
```

Open the primary view for `subject-identified`. The same `next-act` view now reflects the identified target and phenomenon. Compare its remaining open conditions with the earlier view; regenerating the view replaces computed state rather than editing an authored record.

## Stage 5: propose a first candidate answer

The [specified-subject stage](../epistemology/processes/inquiry/specification-order.md#^specification-stages) is entered only when an open condition requires formal declarations. This tutorial therefore passes over stage 4 and proposes a candidate answer in words. Run *Create instance*, choose *Answer record — gnomon:answer@3*, and enter `pendulum/answer.yml`. Gnomon adds the new record under stage 5 of the inquiry index.

The candidate answer attributes the growth of the period to the restoring torque of gravity, which grows more slowly than the angle of the swing. Its claim stays unformalized: the field `expression` is empty, and the caveat names the gap. Fill the form with this first draft of the claim, its grounds, its route and its explanatory block:

```yaml
_schema: gnomon:answer@3
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

Append the step `propose` through the itinerary form. It instantiates the activity `abduction`, with the phenomenon as input and the answer as output:

```yaml
  - id: propose
    activity: abduction
    inputs:
      - type: phenomenon
        ref: phen.pendulum.period-growth
    output:
      type: target-claim
      ref: ans.pendulum.weak-restoring-torque
    norm:
      test: norm.abduction
      verdict: pass
      evidence: "The candidate states a mechanism that would produce the growth of the period, while its status claims no acceptance for it."
      judged: "2026-11-08"
    rationale:
      serves: quest.pendulum.explain-growth
      acts_on: candidates
    mode: abductive
```

The output type `target-claim` is the type that the [activity registry](../../src/gnomon/data/registries/activities.yml) fixes for `abduction`; the command `gnomon itinerary` reports any other type. Run `gnomon check pendulum`. The check reports three findings and one warning:

```text
answer.yml: ans.pendulum.weak-restoring-torque: completeness/unmet-requirement: always required: dependence
answer.yml: ans.pendulum.weak-restoring-torque: warning: completeness/unstated-domain: domain: not stated, although the route is a derivation
answer.yml: ans.pendulum.weak-restoring-torque: completeness/unmet-requirement: always required: aim_block.explanation.explanatory_claim
answer.yml: ans.pendulum.weak-restoring-torque: completeness/unmet-requirement: always required: aim_block.explanation.factors[].target_status
6 records checked in 1 folders, 3 findings, 1 warnings, 0 templates not yet filled
```

Each finding names a field required by the [core or explanatory block of an answer](../specification/answer.md#^answer-elements). The three blocks below apply those fields to the worked claim:

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
6 records checked in 1 folders, 0 findings, 1 warnings, 0 templates not yet filled
```

A warning fails no check, and the command exits with code 0. This warning anticipates the assessment of the [domain of a deductive claim](../epistemology/objects/answer/answer-form.md#^derived-domain), since this derivation must state the conditions over which it holds. The domain uses declared symbols, so this inquiry can add it after the target reaches the commitment `specified`. If the inquiry proceeds through stage 4, then the option `--with` adds the background and operator records.

Open the primary view for `candidate-proposed`. Gnomon opens the `exposure` view. Inspect the revisable units of the candidate answer, their dependencies and the coverage statement. The view makes the current answer available for appraisal without treating it as established.

## Read the next acts

The command `gnomon status` now reads the answer among the records:

```text
quest.pendulum.explain-growth [selection]
  open definiteness
    ready: explication, explicit-definition
    waiting for an input: operationalization (concept), concept-revision (concept), delimitation (admitted-laws), formalization (model), phenomenon-specification (target-specification)
  open candidates: 1 answer recorded, none yet passes the admissibility tests of an assessment
    ready: abduction, derivation, critique, admissibility-check, result-retrieval
    waiting for an input: induction (data), analogical-inference (model), causal-inference (data; model), decomposition-localization (target-specification), model-analogy (model), de-idealization (model), idealization (model), abstraction (model), formalization (model), fitting (model; data), model-assembly (target-specification; admitted-laws)
each ready act can be taken now; the choice among them is the researcher's, as docs/procedures/inquiry/next-act.md states
each activity is defined in the note of its family, which docs/epistemology/processes/activities/_index.md lists; a name in parentheses is the type of the missing input, which docs/epistemology/processes/activities/epistemic-activities.md defines
```

Two conditions stay open:

- definiteness, since the question asserts no state for it, and the definiteness of a term can be established only once its record reaches the commitment `specified`. The act `delimitation` writes the formal declarations of the target, as stage 4 does, once a background record holds the admitted laws of the pendulum, an input of that act;
- candidates, since one answer is recorded and no assessment of it passes the admissibility tests. The ready act `admissibility-check` produces those verdicts, in an assessment record added through *Create instance*.

The choice between these acts is the researcher's, as the [choice of the next act](../procedures/inquiry/next-act.md) states. The command `gnomon tree` prints the chain of records built so far:

```text
problem prob.pendulum.period-growth: Growth of the period of a pendulum with its amplitude [posed]
  question quest.pendulum.explain-growth: Explanation of the growth of the period [posed]
    answer ans.pendulum.weak-restoring-torque: Restoring torque weaker than linear [entertained]
```

## Continue the inquiry

If the Obsidian creation command is unavailable, `gnomon init pendulum --with KIND` remains the CLI fallback. It creates the same current sparse record and updates the same inquiry index before the record is opened in Ekphrasis.

Keep the `pendulum` folder as a resumable inquiry. The forms reconstruct their state from the saved YAML, and each primary view can be regenerated from the current records. The [guide to filling the records](filling-records.md) states how a record is raised to the commitment `specified`, with its quantities, its laws and its formulas. The tutorial [following one inquiry](tutorial.md) reads a complete inquiry, from its problem to the assessment of its candidate answer.
