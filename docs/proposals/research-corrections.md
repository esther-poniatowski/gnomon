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
