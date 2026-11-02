---
tags:
  - decision
status: accepted
created: 2026-11-02
revised: 2026-11-02
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Design record
---
# Design record

> [!QUESTION] Goal: which record holds a design, the plan of acts whose execution yields data or consequences?

The activity `experimental-design` outputs a design, which the activities of observation, measurement, intervention and simulation take as an input, as the [empirical activities](../epistemology/processes/activities/empirical-activities.md) state. A problem can also demand a design as its result. No record held a design, and the inventory of epistemic objects gave it no role. Therefore, a design could be named by an itinerary, but neither recorded nor assessed.

## Decision

**A design record holds one plan of acts.** Its kind is one of three: the protocol of an experiment on the target, the protocol of a run of a simulation of a model, or a method that solves a task. The record states:

- the question or the problem that the design serves;
- the task, which an execution must achieve;
- the inputs that an execution takes;
- the steps, in their order;
- the rules that state the admissible moves or decisions;
- the output that an execution yields;
- the condition under which an execution stops;
- the modes of failure, each with the step or the rule that guards against it;
- for an experiment or a simulation run, the protocol: the intervention, the control and the observation.

**A design bears the role Plan.** A plan licenses an execution: a run that follows its steps and its rules on its inputs yields its output. This role joins the [table of epistemic roles](../epistemology/objects/status/epistemic-objects.md#^unit-roles).

**The procedure that assigns the values of a quantity stays apart.** That procedure keeps the role Definition and stays in the target-system record.

The record takes the prefix `design`, with three segments, and the contract `gnomon:design@1`.

## Conditions of admission

The kind meets the seven [conditions of admission](record-kind-admission.md#^admission-conditions):

- **independent identity**: a protocol or a method is meaningful without the question that it serves, as a published protocol is;
- **reuse**: several observations, simulations or itineraries can execute one design;
- **local validity**: a check judges the steps, the rules, the stopping condition and the guards of the modes of failure without reading the records that cite the design;
- **independent editing**: an author can revise a step or a rule without rewriting the records that cite the design;
- **irreducibility**: no tool generates a plan of acts from other records;
- **non-distortion**: each existing kind would distort a design:
    - an itinerary records the epistemic acts of one inquiry, each an instance of a registered activity, whereas the steps of a design are acts on a target or on a model, so an itinerary holding them would merge two kinds of act;
    - an answer holds one typed claim, whereas a design asserts nothing, so its steps would move into prose;
    - a model is a system that stands in for the target, whereas a protocol is not a system;
- **unitary epistemic role**: every design, of each of the three kinds, licenses the same operation, an execution that yields its output, and is judged for its adequacy to its task before any execution.

## Constraints that decide the record

- **A demand for a construct is met by a record.** The [demand met](../epistemology/objects/problem/epistemic-problem.md#^demand-met) for a construct type requires a stabilized record of the construct and a satisfied assessment of it, so a design without a record could never meet a demand.
- **One record kind holds one role.** The criterion of a unitary epistemic role excludes a record whose instances license different operations.
- **The activity of measurement takes two inputs.** The `measurement` activity takes a `measurement-procedure` and a `design` as separate inputs, so the theory already distinguishes the procedure that defines a quantity from the plan of its execution.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep the design without a record, in the prose of a question or of an itinerary | No kind is added | The steps and the stopping condition move into prose, and a problem that demands a design can never be solved |
| A record for the protocols of experiments and of simulation runs only | The record matches the single activity that outputs a design | A method that a problem demands has no home, although it has the same parts and licenses the same execution |
| One record for designs and for measurement procedures | One record for every procedure | A measurement procedure defines a quantity and licenses substitution, so the record would hold two roles |
| One record for every plan of acts, with a protocol for experiments and simulation runs | One record and one role for every plan, and a demand for a design can be met | A method needs an activity of its own, since the norm of experimental design does not judge it |

## Consequences

- The record kinds gain `design`, with its [specification](../specification/design.md), its base schema and its contract.
- The table of epistemic roles gains the role Plan, and the demand table gains the type of result `design`.
- The product type `measurement-procedure` stays partial in the target-system record.
- The activity `method-design` outputs a design of the kind `method`, and `experimental-design` outputs the protocols.
- The protocol is required for the kinds `experiment` and `simulation-run`, as the specification states and the requirements by value of the requirement registry declare.
