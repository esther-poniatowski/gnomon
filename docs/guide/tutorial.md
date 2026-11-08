---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Tutorial
  - Following one inquiry
---
# Following one inquiry from the problem to the assessment

This tutorial follows the worked inquiry into delayed generalization through the five stages of the [order of specification](../epistemology/processes/inquiry/specification-order.md). For each stage, the tutorial names the records filled, the itinerary step recording the act, and the command serving the stage, with its output on the inquiry.

> [!IMPORTANT] Prerequisites
> The repository is cloned and the package is installed from source, as the [installation guide](installation.md) states, since the worked inquiries lie in the folder `examples/` of the repository. Every command runs from the root of the clone.

## Copy the worked inquiry

Every command runs on a copy, so the worked inquiry stays unchanged. The following command copies its folder next to the clone:

```sh
cp -R examples/grokking-delayed-generalization ../grokking
```

The command `gnomon tree` prints the chain of records held by the inquiry, from its problem to the assessment of its candidate answer:

```sh
gnomon tree ../grokking
```

```text
problem prob.grokking.delayed-generalization: Delay between fitting and generalization [posed]
  question quest.grokking.explain-delay: Mathematical explanation of delayed generalization [posed]
    answer ans.grokking.slow-structured-representation: Account of grokking through a structured representation that forms slowly [hypothesized]
      assessment assess.grokking.slow-structured-representation: Assessment of the account through a structured representation [stabilized]
```

Each line names the kind of a record, its identifier, its title and its status. The candidate answer keeps the status `hypothesized`, whereas its assessment has the status `stabilized`. The assessment has judged every test but one, and the stages below trace these verdicts back to the records supporting them.

The command `gnomon check` runs every check of the package on the copy:

```sh
gnomon check ../grokking
```

```text
13 records checked in 1 folders, 0 findings, 0 warnings, 0 templates not yet filled
```

The folder holds fourteen files of records, and the check skips the generated file `vocabulary.yml`, so thirteen records are checked. No finding is reported, so the records of the inquiry meet every check.

## The stages at a glance

The [itinerary record](../../examples/grokking-delayed-generalization/itinerary.yml) of the inquiry lists nine steps. Each step names an activity of the [activity registry](../../src/gnomon/data/registries/activities.yml), its inputs, its output, and the verdict of the norm that judges it. The table below places each record and each step in its stage, with the command presented at that stage:

| Stage | Records | Steps | Command |
| ----- | ------- | ----- | ------- |
| 1. Problem | `problem.yml` | `pose` | `gnomon init` |
| 2. Question schema | `question.yml` | `formulate` | `gnomon itinerary` |
| 3. Identified subject | `phenomenon.yml` | `identify` | `gnomon validate` |
| 4. Background and specified subject | `target-system.yml`, `background.yml`, `operators.yml` | `delimit`, `admit` | `gnomon vocabulary`, `gnomon status` |
| 5. Candidate answer | `answer.yml`, `model.yml`, `derivation.yml`, `design.yml`, `binding.yml`, `assessment.yml` | `propose`, `derive`, `check`, `test` | `gnomon check`, `gnomon views` |

Once presented, a command also serves every later stage; in particular, the command `gnomon check` runs after each stage.

## Stage 1: pose the problem

The problem states what a solution must deliver. The [problem record](../../examples/grokking-delayed-generalization/problem.yml) demands that a solution name the determinants of the delay, derive its duration from them, and cover its variation across random initializations. Its two constraints require consistency with the admitted training laws, and the separation of delayed generalization from two foils: immediate generalization and persistent memorization.

The step `pose` records the act. The step instantiates the activity `problematization`, takes as input the source that reports the delay, and outputs the problem record. Its norm passed on 2026-10-27, with the evidence that each explicandum of the problem points to its source.

A new problem starts from the templates written by `gnomon init`. The inquiry cannot show this command, since its folder already holds its records, so the command runs on a new folder. There, the command writes the itinerary, opened with the problem, the templates of the first four stages, and an index that lists them in the order of filling:

```sh
gnomon init ../my-problem
```

```text
../my-problem/itinerary.yml: written
../my-problem/problem.yml: written
../my-problem/question.yml: written
../my-problem/target-system.yml: written
../my-problem/phenomenon.yml: written
../my-problem/background.yml: written
../my-problem/operators.yml: written
../my-problem/_index.md: written
Fill the records in the order of ../my-problem/_index.md, then run: gnomon check ../my-problem
```

The check of the new folder shows the starting point of every inquiry:

```sh
gnomon check ../my-problem
```

```text
0 records checked in 0 folders, 0 findings, 0 warnings, 7 templates not yet filled
```

The seven templates keep their placeholder identifiers, so the check lists them apart and checks none of them. Their count falls as the stages are filled.

## Stage 2: type the question

The question types the answer that the problem demands, before its terms are identified. The [question record](../../examples/grokking-delayed-generalization/question.yml) serves the problem as its associated question. Its task fixes the aim `explanation`, the requested relation `mathematical` and the modal strength `actual`, and its contrast names the two foils of the problem.

The step `formulate` records the act. The step instantiates the activity `question-formulation`, and takes the problem by the full identifier of the step that produced it, `itin.grokking.explain-delay.pose`. Its output states the type `question-schema` without a record: the schema became the question once its slots were identified, so no record holds the schema any longer.

The command `gnomon itinerary` checks the steps of the itinerary, as the [command reference](cli-reference.md) states:

```sh
gnomon itinerary ../grokking
```

```text
1 itineraries checked, 0 problems found
```

For the step `formulate`, this result means two things. Its input names a step whose output type, `problem`, is the input type of the activity `question-formulation`. Its declared output type, `question-schema`, is the output type of that activity. A defect would print one line, prefixed with the identifier of the itinerary, and the command would exit with code 1.

## Stage 3: identify the subject

The subject fixes the object of the question, so that each slot of the question refers to a record. The [phenomenon record](../../examples/grokking-delayed-generalization/phenomenon.yml) fixes the regularity through six observables. Two are references to the training and test losses declared by the target. The four others are declared by the phenomenon: the first crossing times of the training and the generalization criteria, `tfit` and `tgen`, the delay between them, `delay`, and its distribution across initialization draws, `Pdelay`. The evidential status of the phenomenon is `established`, and its commitment `specified` also meets the commitment `identified` required by the question, as the [levels of commitment](../epistemology/objects/question/question.md#^commitment-levels) define them.

The step `identify` records the act. The step instantiates the activity `subject-identification`, takes the question schema produced by the step `formulate`, and outputs the identified subject, held by the phenomenon record. Its norm passed on 2026-10-27.

The command `gnomon validate` checks each record against the contract that its field `_schema` names, such as `gnomon:phenomenon@1`:

```sh
gnomon validate ../grokking
```

```text
13 records checked, 0 errors found
```

For this stage, the result means that the phenomenon record fits the contract `gnomon:phenomenon@1`: for instance, its commitment and its evidential status take admitted values. A contract reads one record at a time, so only the command `gnomon check` compares the records with one another.

## Stage 4: specify the target and admit the background

The target system and the background supply the formal declarations used by a candidate answer. The [target system](../../examples/grokking-delayed-generalization/target-system.yml), at commitment `specified`, declares the constituents, the index sets, the variables and the parameters of the trained networks. The [background record](../../examples/grokking-delayed-generalization/background.yml) admits six laws of the forward computation and of the training, each with the warrant `posited`. The [operator record](../../examples/grokking-delayed-generalization/operators.yml) declares the operators used by the formulas beyond the canonical set.

Two steps record these acts:

- the step `delimit`, an instance of the activity `delimitation`, outputs the target specification held by the target system; its verdict is `pending`;
- the step `admit`, an instance of the activity `background-appraisal`, outputs the admitted laws held by the background record. Its norm failed on 2026-10-27, since no admitted law states its origin or the range over which it is established.

The command `gnomon vocabulary` lists the symbols already declared in the problem, so that a new quantity takes a free symbol:

```sh
gnomon vocabulary ../grokking
```

```text
../grokking/vocabulary.yml: 58 symbols, 5 operators of the problem, 0 symbols reused across records
```

No symbol is declared by two records, so no letter of the inquiry denotes two quantities. The command rewrites the file `vocabulary.yml` of the copy, and names its record after the folder, `vocab.grokking`.

The failed step changes the acts open to the inquiry. The command `gnomon status` applies the [choice of the next act](../procedures/inquiry/next-act.md) to the records, question by question:

```sh
gnomon status ../grokking
```

```text
quest.grokking.explain-delay [selection]
  open definiteness
    ready: explication, explicit-definition, delimitation, formalization, phenomenon-specification
    waiting for an input: operationalization (concept), concept-revision (concept)
  open candidates: 1 answer recorded, none yet passes the admissibility tests of an assessment
    ready: abduction, induction, analogical-inference, causal-inference, decomposition-localization, model-analogy, de-idealization, idealization, abstraction, formalization, fitting, derivation, critique, admissibility-check, result-retrieval
    waiting for an input: model-assembly (admitted-laws)
judge anew the norm of itin.grokking.explain-delay.check, whose record is stabilized
judge anew the norm of itin.grokking.explain-delay.test, whose record is stabilized
impeached records: bg.delayed-generalization-networks.training-specification
each ready act can be taken now; the choice among them is the researcher's, as docs/procedures/inquiry/next-act.md states
each activity is defined in the note of its family, which docs/epistemology/processes/activities/_index.md lists; a name in parentheses is the type of the missing input, which docs/epistemology/processes/activities/epistemic-activities.md defines
```

The diagnosis follows the route of selection: candidates are proposed, and an obtained value selects one of them, as the [two routes to an answer](../epistemology/objects/question/conditions-of-answerability.md#^routes) define it. Each open condition can be addressed now, since its dependencies are established. Its activities are split into the ready ones and those waiting for an input, named in parentheses. The condition of candidates stays open until an assessment passes the admissibility tests of an answer. The background record is impeached, since the step producing it failed. Therefore, the activity `model-assembly` waits for its admitted laws: the only record holding them is impeached. The two lines on norms to judge anew belong to stage 5.

## Stage 5: propose, derive and assess a candidate answer

The candidate answer is filled last, with the records supporting it. In the inquiry, they hold the following content:

- the [candidate answer](../../examples/grokking-delayed-generalization/answer.yml), with the status `hypothesized`, attributes the delay to the slow formation of a structured representation, and grounds this claim on the model and the binding;
- the [model](../../examples/grokking-delayed-generalization/model.yml) derives an effective theory from the target through four operations. Its three laws are a relaxation law with the warrant `posited`, a timescale with the warrant `derived`, and a link to generalization with the warrant `measured`;
- the [derivation](../../examples/grokking-delayed-generalization/derivation.yml) constructs the timescale in five moves, and states two consequences, a scale law and a threshold lemma;
- the [scheme of relaxation](../../examples/grokking-delayed-generalization/design.yml) states the reusable way of deriving applied by the derivation;
- the [binding](../../examples/grokking-delayed-generalization/binding.yml) pairs the model with the phenomenon at the grain `qualitative`;
- the [assessment](../../examples/grokking-delayed-generalization/assessment.yml), with the status `stabilized`, fails three tests of admissibility, the product, the scope and the grain, and three tests of warrant, the closure, the fidelity and the robustness.

The command `gnomon init` adds the templates of these record kinds to a folder through its option `--with`. In a folder already holding records, the command writes only the missing templates, as its run on the folder of stage 1 shows:

```sh
gnomon init ../my-problem --with answer --with assessment
```

```text
../my-problem/answer.yml: written
../my-problem/assessment.yml: written
../my-problem/_index.md: updated
7 existing files kept
Fill the records in the order of ../my-problem/_index.md, then run: gnomon check ../my-problem
```

The two new templates are registered in the index of the folder, under the heading of the stage of candidate answers, and the seven existing files stay as they stand.

Four steps record these acts:

- the step `propose`, an instance of the activity `abduction`, outputs the candidate answer; its norm passed;
- the step `derive`, an instance of the activity `derivation`, takes the model and outputs its derived consequence, and its field `derivation` names the derivation record judged by its norm; its verdict is `pending`;
- the steps `check` and `test`, instances of the activities `admissibility-check` and `testing`, output the verdicts held by the assessment; their verdicts are `pending`.

The assessment is stabilized while the norms of the steps `check` and `test` are pending. For this reason, the command `gnomon status` asks above to judge them anew: the verdicts now exist, and the steps that produced them have not been judged.

The command `gnomon check` reports each defect at its field. A misspelled symbol in a factor of the explanation shows the form of a finding. In the file `answer.yml` of the copy, replace the symbol `eta_rep` by `eta_rp` in the line `holds: "0 < lambda3 * eta_rep"`, then run the check:

```sh
gnomon check ../grokking
```

```text
answer.yml: ans.grokking.slow-structured-representation: vocabulary/unresolved: aim_block.explanation.factors[].holds -> eta_rp; did you mean eta_rep?
13 records checked in 1 folders, 1 findings, 0 warnings, 0 templates not yet filled
```

The line names the file, the record and the rule, then the path of the expression, the identifier that resolves to no declaration, and the closest declared symbol. The command exits with code 1. Restoring the symbol `eta_rep` returns the check to no finding.

The command `gnomon views` writes the state of the inquiry as YAML views that a renderer displays:

```sh
gnomon views ../grokking --output ../grokking-views
```

```text
../grokking-views/problem-state.yml: written
../grokking-views/next-act.yml: written
../grokking-views/exposure.yml: written
../grokking-views/itinerary-progress.yml: written
../grokking-views/maturity.yml: written
../grokking-views/question-tree.yml: written
../grokking-views/question-statements.yml: written
../grokking-views/expressions.yml: written
```

Two of the eight views serve this stage. The view `itinerary-progress.yml` states the stage of the itinerary, `in-progress` here, and lists the steps with a state each: `impeached` when a failed norm lies upstream of the output of the step, `conditional` when a pending norm does, and `sound` otherwise. The step `admit` is impeached, and the steps `delimit`, `derive`, `check` and `test` are conditional. The view `exposure.yml` lists the revisable units supporting each answer. The candidate answer is exposed through eleven units. Seven belong to the model: three operations, two laws, and the existence of `lambda3` and of `Rstar`, two quantities fixed by a condition. Four belong to the derivation: two consequences, one move and one posit.

## What the itinerary leaves out

The itinerary of the inquiry records only part of its acts. No step records how the model, the scheme and the binding were built: the step `derive` reads the model as its input, and records the derived consequence in it. A complete itinerary adds one step per act, each an instance of an activity of the registry, and the command `gnomon itinerary` checks each added step as it checks the present ones.

## Remove the copies

The tutorial created three folders next to the clone. The following command removes them:

```sh
rm -rf ../grokking ../my-problem ../grokking-views
```

A new problem follows the same five stages with its own records, as the [guide to filling the records](filling-records.md) states.
