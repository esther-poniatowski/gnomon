---
tags:
  - guide
index: "[User guide](docs/guide/_index.md)"
aliases:
  - Starting from existing research
---
# Starting from existing research

One active question from an existing project can be isolated as a checked Gnomon inquiry slice with a current view of the next research acts. The surrounding notes, publications, models and data remain in place.

> [!IMPORTANT] Prerequisites
> Install Gnomon in a dedicated Python environment, as the [installation guide](installation.md) states. Open the existing project folder as an Obsidian vault. Install and enable Ekphrasis by following its [installation guide](https://github.com/esther-poniatowski/ekphrasis/blob/main/docs/guide/installation.md). Run every terminal command from the vault root with the dedicated environment active.

## Select the active question

Select the question whose answer currently controls the research. The worked route uses this question:

> Which mathematical properties of training produce the delay between fitting the training data and generalizing to held-out data?

The existing note and data set remain external. Their paths enter the question record under the [source-pointer rule](../specification/question.md#^question-sources), which imports neither their content nor an epistemic classification.

## Prepare the vault and inquiry slice

Install the portable form contracts in the current vault:

```sh
gnomon setup .
```

The final output line gives the registry path for Ekphrasis. The default path is `.gnomon/schema-registry.yml`.

Create a question-led inquiry slice without creating a problem record:

```sh
gnomon init ./active-slice --start-with question
```

The command creates three files and leaves the rest of the project unchanged:

```text
active-slice/itinerary.yml: written
active-slice/question.yml: written
active-slice/_index.md: written
Fill active-slice/question.yml first, then record subsequent acts in active-slice/itinerary.yml. Run: gnomon check active-slice
```

## Connect Ekphrasis

Ekphrasis needs the registry and the Python interpreter that runs Gnomon. Print the absolute interpreter path:

```sh
python -c "import sys; print(sys.executable)"
```

Ekphrasis reads four values under **Settings → Ekphrasis**:

- **Schema registry:** `.gnomon/schema-registry.yml`
- **Python interpreter:** the absolute path printed by the preceding command
- **Post-creation command:**

  ```json
  ["-m", "gnomon", "register", "{vault}/{path}"]
  ```

- **Primary-view command:**

  ```json
  ["-m", "gnomon", "views", "{vault}/active-slice", "--scope", "{target}", "--output", "{vault}/active-slice/views", "--result", "json"]
  ```

Open `active-slice/question.yml`, then run *Diagnose setup*. The groups *Blocks schema-derived forms* and *Blocks saving authored records* must pass. The [recovery guide](recovery.md) covers failures of the schema or Python runtime. A missing custom checker does not block this tutorial because the Gnomon checks run in the terminal.

## Fill the adopted question

The sparse question form contains only the fields required at the `question-typed` checkpoint. Fill the form until its saved source has the following content:

```yaml
_schema: gnomon:question@3
title: "Mathematical account of delayed generalization"
statement: "Which mathematical properties of training produce the delay between fitting the training data and generalizing to held-out data?"
id: quest.grokking.explain-delay
type: question
status: posed
version: "1"
sources:
  - "notes/delayed-generalization.md#open-question"
  - "data/run-17.zarr"
request: one
links: []
subject:
  target_system:
    placeholder: system
    description: "the trained neural networks in the selected project runs"
  background: []
  phenomenon:
    placeholder: phenomenon
    description: "the observed delay between fitting and generalization"
  contrast:
    locus: none
    foil_set: []
    compatibility: derived
    foil_status: not-applicable
task:
  epistemic_aim: explanation
  requested_relation: mathematical
  modal_strength: actual
  admissible_explanans: null
  required_accuracy:
    standard: qualitative
virtues: []
```

The field `addresses` is absent because this route has no problem record. Under the [placeholder rule](../specification/question-subject.md#^placeholder-slots), the two subject slots remain typed placeholders until their source units are promoted. The file `active-slice/itinerary.yml` remains unchanged. Its first step records the first act performed under Gnomon. Acts performed before this inquiry slice are not reconstructed from memory.

## Verify the typed question

Validate the saved record against its contract, then check only the requirements due at the current checkpoint:

```sh
gnomon validate ./active-slice
gnomon check ./active-slice --scope question-typed
```

A successful check reports zero current findings and warnings. The scoped check assigns the subject records and the candidate answer to later checkpoints:

```text
1 records checked in 1 folders, 0 findings, 0 warnings, 1 templates not yet filled, 5 future requirements
```

The itinerary is the unfilled template. The five future items belong to checkpoints after `question-typed`, so the typed question remains valid.

## Inspect the first operational view

Run *Open primary view*, enter the completion target `question-typed`, then select *Generate and open*. Gnomon opens the `next-act` view for the saved question.

At this checkpoint, the view derives the answer type as established but reports the subject as not yet definite. Its coverage assigns the target-system and phenomenon records to `subject-identified`. The open-condition rows show that candidate-producing acts still lack a phenomenon, so none is ready.

The worked inquiry therefore applies the [selective-promotion rule](../procedures/inquiry/promoting-external-research.md#^selective-promotion) to the missing inputs. The worked inquiry selects the target system and the observed delay. The source note and data set remain external; only the selected units receive Gnomon records.

## Promote the selected subject

Run *Create instance* twice. First, choose *Target system record — gnomon:target-system@2* for `active-slice/target-system.yml`. Second, choose *Phenomenon record — gnomon:phenomenon@2* for `active-slice/phenomenon.yml`. The configured post-creation command places both records in the inquiry index.

Fill the target-system form:

```yaml
_schema: gnomon:target-system@2
title: "Trained networks in selected runs"
id: system.delayed-generalization-networks
type: target-system
status: provisional
commitment: identified
target_type: actual-systems
identification:
  description: "the trained neural networks in the selected project runs"
  pointers:
    - "notes/delayed-generalization.md#systems"
reference_class:
  name: "trained neural networks in the selected project runs"
  projectibility:
    status: not-claimed
```

Fill the phenomenon form with the observed behavior and its data pointer:

```yaml
_schema: gnomon:phenomenon@2
title: "Delayed generalization"
statement: "The network fits its training data before its performance on held-out data improves."
id: phen.grokking.delayed-generalization
type: phenomenon
status: provisional
commitment: identified
target_system: system.delayed-generalization-networks
identification:
  description: "the observed delay between fitting the training data and generalizing to held-out data"
  pointers:
    - "data/run-17.zarr"
```

Reopen the question form and replace both placeholders with the promoted record identifiers:

```yaml
subject:
  target_system: system.delayed-generalization-networks
  background: []
  phenomenon: phen.grokking.delayed-generalization
```

Run the scoped check after identifying the subject:

```sh
gnomon check ./active-slice --scope subject-identified
```

The successful check leaves only the candidate answer for the `candidate-proposed` checkpoint:

```text
3 records checked in 1 folders, 0 findings, 0 warnings, 1 templates not yet filled, 1 future requirements
```

## Choose the next act

Open the primary view again with the completion target `subject-identified`. The regenerated `next-act` view now lists `abduction` as ready under the open condition `candidates`. Its row answers three operational questions:

- the act reads the phenomenon;
- the act writes a target claim in an answer record;
- the act may make derivation, critique, admissibility checking and result retrieval available.

Gnomon reports the ready acts and their effects, but it selects none. The researcher in this worked inquiry chooses abduction because the current objective is to propose a candidate and the required phenomenon is available. The [guide to filling inquiry records](filling-records.md) leads from this choice to the answer record and the first genuinely tracked itinerary step.

## Apply the promotion rule to later sources

The worked route has promoted only the target system and phenomenon required by its first operational view. When a later check or chosen act needs another external unit, apply the [procedure for promoting selected external research](../procedures/inquiry/promoting-external-research.md). The procedure classifies the smallest required unit, places it in its owning record and retains its immediate source pointer. All other source content remains external.

## Problem-led entry route

A project controlled by an unmet demand rather than an explicit question can start from a problem record. The [`init` command](cli-reference.md#^cli-init) documents this route. Once the problem produces a question, the inquiry follows the records, checks and views used in this tutorial.
