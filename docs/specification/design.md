---
tags:
  - specification
index: "[Specification](docs/specification/_index.md)"
aliases:
  - Design record
---
# Design record

> [!QUESTION] Goal: what does a researcher write in each field of a design record, and when is each field required?

A design record holds one plan of acts, whose execution yields data or consequences: the protocol of an experiment on the target, the protocol of a run of a simulation of a model, or a method that solves a task. The design is a construct, judged for its adequacy to its task before any execution, and the [decision on the design record](../adr/design-record.md) states why it is a record of its own. The procedure that assigns the values of a quantity stays apart, in the [target-system record](target-system.md), since it defines the quantity rather than plans an execution. ^design-record

A step, a rule and a mode of failure are named by descriptive identifiers, unique within the record, so that a mode of failure can name the step or the rule that guards against it. ^design-identifiers

| Specification | When it is required | Content | Examples |
| ------------- | ------------------- | ------- | -------- |
| Kind | always | `experiment` · `simulation-run` · `method` | a sweep of the coupling of a simulated lattice (simulation run); a stimulation protocol in slices of cortex (experiment); an algorithm that enumerates the fixed points of a network (method) |
| Serves | for the kinds `experiment` and `simulation-run`; for a method, when it solves the task of one problem | the identifier of the question or of the problem that the design serves; a method that serves none is a reusable scheme, such as a [scheme of derivation](../epistemology/objects/derivation/segment-and-scheme.md) | `quest.nonreciprocal-active-matter.phase-exploration` |
| Task | always | one sentence that states what an execution must achieve | detect the phases of the lattice realization across the nonreciprocal coupling, at each system size |
| Applies when — the conditions of application | for a method that serves no problem | one entry per condition under which the method applies, each a grammatical expression or a named property | the operator is self-adjoint; a small parameter separates two time scales |
| Inputs | when an execution takes objects that the design does not create | one entry per input, with a name and a description | the grid of control parameters; the initial states |
| Inputs: name | in each entry | the name of the input | grid of control parameters |
| Inputs: description | in each entry | the content of the input, in one phrase | the values of the nonreciprocal coupling, crossed with the system sizes |
| Steps | always | one entry per act, in the order of execution | draw the initial states, equilibrate, record, classify |
| Steps: id | in each entry | a descriptive identifier, unique within the record | `equilibrate` |
| Steps: act | in each entry | the act that the step performs | run the stochastic dynamics until relaxation, and discard the transient |
| Rules | when an execution admits or imposes a choice | one entry per admissible move or decision | the reuse of seeds across sizes |
| Rules: id | in each entry | a descriptive identifier, unique within the record | `common-seeds` |
| Rules: rule | in each entry | the move or the decision that the rule admits or imposes | runs at different sizes reuse the same seeds of the random generator |
| Output | always | the data or the consequences that an execution yields | per point of the grid and per run, the correlation matrices between species and the assigned phase |
| Stopping condition | always | the condition under which an execution stops | every point of the grid holds the planned number of runs |
| Failure modes | when an execution can yield a misleading output | one entry per mode, with the step or the rule that guards against it | a transient read as a phase |
| Failure modes: mode | in each entry | the way in which an execution can mislead | a run recorded before relaxation is read as a distinct phase |
| Failure modes: guard | optional, in each entry | the identifier of the step or of the rule that detects or prevents the failure | `equilibrate` |
| Protocol | for the kinds `experiment` and `simulation-run` | the intervention, the control and the observation of the next three rows | — |
| Protocol: intervention | with a protocol | the quantity that an execution sets, with its levels | the nonreciprocal coupling, varied over a grid, crossed with the system size |
| Protocol: control | with a protocol | the condition against which the effect of the intervention is read | the runs at zero nonreciprocal coupling |
| Protocol: observation | with a protocol | the observable recorded, with the key or the measurement procedure that yields it | the correlation matrix between species on the lattice |
