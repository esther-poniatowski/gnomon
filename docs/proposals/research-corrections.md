---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the research corrections
---
# Proposals for the research corrections

The goal [`research-corrections`](../../TODO.md) applies the research corrections of the Mixture pilot, among them a rationale on each itinerary step.

## Grammars for the rationale of a step

The fields that state why a step of reasoning was taken are read by checks, so each of them requires a grammar rather than free prose. The candidate grammars are:

- **strategic rationale:** a record `{move_type, target_deficiency_ref, expected_gain_kind}`, or a grammar over the signatures of the operations;
- **explanatory gain:** a reference to the property of the state that the step made present, such as a newly licensed claim, a discharged assumption or a closed subgoal;
- **route selected and alternatives rejected:** references to candidate operations, each in a record `{candidate_ref, rejection_reason_kind}` whose kind is drawn from a closed list;
- **deficiency addressed:** a reference to a question or a gap.

The goal already requires the rationale of each step to name the question served and what the step acts on, which covers the deficiency addressed. The candidate adds the gain obtained and the alternatives rejected.

**Literature.** None cited.

**Bears on.** [`research-corrections`](../../TODO.md), and `inquiry-records-round-2`, which requires field paths that a program can read instead of prose.

## Record of a design

A design has no record: the [registry of product types](../../src/gnomon/data/registries/product-types.yml) marks the product `design` as to create. A record of a method would hold seven fields: the task, the inputs, the steps, the rules that state the admissible moves or decisions, the output, the condition of stopping, and the modes of failure. An experimental design adds the intervention, the control and the observation. The record passes the first five of the seven conditions of the [admission of a record kind](../adr/record-kind-admission.md#^five-conditions): a design is meaningful apart from the inquiry that uses it, several inquiries can cite it, a check can judge it alone, an author can revise it without rewriting its users, and no tool generates it. Non-distortion and unitary epistemic role remain to be checked. The same record would hold the procedure that assigns the values of a quantity, which the product `measurement-procedure` lacks.

**Literature.** None cited.

**Bears on.** [`research-corrections`](../../TODO.md), which asks for a record kind for designs, and the products `design` and `measurement-procedure`.

**Retired source.** `docs/design/_backup/object-types-ontology/obj-method-procedure.md`, at commit 9e138e2.
