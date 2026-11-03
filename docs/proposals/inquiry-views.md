---
tags:
  - proposal
index: "[Proposals](docs/proposals/_index.md)"
aliases:
  - Proposals for the inquiry views
---
# Proposals for the inquiry views

The goal [`inquiry-views`](../../TODO.md) generates views of the state of an inquiry from its records, beside the question tree that `gnomon tree` already prints.

> [!IMPORTANT] Decision of 2026-11-03
> The five views below and the question tree are adopted. The command `gnomon views` writes each as a generated YAML record, which a renderer such as Ekphrasis displays as a read-only form through its [view schema](../../src/gnomon/data/views/_index.md). A tree or a graph is stated by a table of nodes and a table of edges, and its picture awaits a renderer of trees and graphs in Ekphrasis. The exposure through a derived law is reported as a descent not yet recorded, until the laws state their premises. Each view is computed from authored records by a declared rule and is never authored, as the [boundary of computation](../adr/no-run-time-inference.md#^admitted-computation) admits. Each entry below names the question that the view answers for the researcher, the records that it reads, and the functions of the [completeness module](../../src/gnomon/completeness.py) or of the theory from which it is computed.

## State of each problem

The view answers whether a problem is solved, and which obstacles remain. For each problem record, it shows the demand, the type of result and the request, then three computed parts:

- the [demand met](../epistemology/objects/problem/epistemic-problem.md#^demand-met), read by `demand_met` from the answers or the constructs that serve the problem and from their assessments;
- the accepted answers and the candidates that bear on the problem, which restrict $K$ and $H$ to that problem;
- the obstacles stated in the problem record, set beside the obstacles that `readable_obstacles` derives from the records, with each disagreement that `misstated_obstacles` reports, and a denied presupposition that `presupposition_denied` finds.

The computation exists, so the view adds only its presentation. The view also shows a problem that could be marked solved or dissolved but still has the status `posed`.

**Literature.** None cited.

**Bears on.** [`inquiry-views`](../../TODO.md).

## Open conditions and ready acts

The view answers which act comes next. For each question, it lists the [open conditions](../epistemology/processes/inquiry/choice-of-act.md#^open-condition) of answerability, and the [ready act instances](../epistemology/processes/inquiry/choice-of-act.md#^ready-act) whose inputs exist and are unimpeached, as the procedure of the [next act](../procedures/inquiry/next-act.md) states. The stub `gnomon status` of the command module was declared for this view. The view requires the reference of a step to a record at a stated state (`as_of`), since an input is unimpeached only relative to the state that its step read.

**Literature.** None cited.

**Bears on.** [`inquiry-views`](../../TODO.md), and `inquiry-records-round-2`, which holds the stub and the reference `as_of`.

## Exposure of an answer

The view answers to which revisable laws an accepted result stays exposed. For each answer, it follows the grounds, and the derived laws back to the laws from which they descend, and reports the set of laws marked `posited`, `fitted` or `measured`, as the [exposure rule](../epistemology/objects/knowledge/grounds-and-dependence.md#^weakest-link) states. The set is reported without a degree, since the warrants of laws are not ordered. Grouped by law, the same computation shows which results a revision of one law would reach.

**Literature.** The exposure rule departs from the weakest-link principle of Pollock, as its note states.

**Bears on.** [`inquiry-views`](../../TODO.md), and `assembly-schema`, which keeps the query of the laws to which an answer is exposed.

## Progress of an itinerary

The view answers how far an itinerary has advanced. For each itinerary, it lists the steps in the order of their dependencies, with the verdict of each norm, `pass`, `fail` or `pending`, and the record that holds each output. A step downstream of a failed norm is shown as impeached, as the readiness of an act defines impeachment.

**Literature.** None cited.

**Bears on.** [`inquiry-views`](../../TODO.md).

## Maturity map

The view answers which parts of the research are settled. For each record, it groups the fields by maturity, `open`, `provisional` or `stabilized`, where a field that carries no marker takes the maturity fixed by the [maturity of a field](../specification/maturity.md). Aggregated over a project, the map shows the open fields that accepted results rest on.

**Literature.** None cited.

**Bears on.** [`inquiry-views`](../../TODO.md).
