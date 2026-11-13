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
> The five views below and the operational inquiry graph are adopted. The command `gnomon views` writes each as a generated YAML record, which Ekphrasis displays as a read-only form through its [view schema](../../src/gnomon/data/schemas/views/_index.md). The graph connects typed products through typed activity instances and opens on the route of the starting problem. The command `gnomon tree` separately retains the textual question hierarchy. A derived law passes exposure to its recorded descent. When no derivation records that descent, the view reports the law with reason `descent in its origin` when an origin is present, and `descent not recorded` otherwise. Each view is computed from authored records by a declared rule and is never authored, as the [boundary of computation](../adr/no-run-time-inference.md#^admitted-computation) admits. Each entry below names the question that the view answers for the researcher, the records that it reads, and the functions of the [completeness module](../../src/gnomon/completeness/__init__.py) or of the theory from which it is computed.

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

**Bears on.** [`inquiry-views`](../../TODO.md).

## Exposure of an answer

The view identifies the units under which each answer remains revisable. The same view shows which answers reach one shared exposing unit. To [compute exposure](../../src/gnomon/exposure.py), Gnomon walks the dependencies stated by the records under the [exposure rule](../epistemology/objects/knowledge/grounds-and-dependence.md#^weakest-link). For every reported pair, the table states the unit kind, reason and recorded route. The graph connects each answer directly to every exposing unit that the walk reaches. Selecting an answer shows its exposing units. Selecting a shared unit shows its incident answers.

The graph is bipartite: answer nodes connect directly to exposing-unit nodes. The graph does not reproduce Gnomon's intermediate steps. An edge does not assert a direct dependency, a causal relation, a degree of exposure or an order of warrants. When the walk produces no row for an answer, the graph omits that answer. A researcher cannot treat the omitted answer as stable. Each table row states why Gnomon reported the answer–unit pair. The same row records the route. ^exposure-view-model

**Literature.** The exposure rule departs from the weakest-link principle of Pollock, as its note states.

**Bears on.** [`inquiry-views`](../../TODO.md) and [`assembly-schema`](../../TODO.md).

## Progress of an itinerary

The itinerary-progress view reports two results. First, it reports the stage reached by each itinerary. Second, it reports whether each expected output remains usable. Its dependency graph represents each step once. The graph separates recorded outputs from outputs not yet recorded. The graph assigns one of three usability states to every recorded output: `sound`, `conditional` or `impeached`. The graph assigns `not-produced` to an expected output without a record. The graph identifies every displayed step that originates a conditional or impeached state. For an origin outside the displayed steps, the graph adds an explicit source node.

**Literature.** None cited.

**Bears on.** [`inquiry-views`](../../TODO.md).

## Maturity map

The view answers which parts of the research are settled. For each record, it groups the fields by maturity, `open`, `provisional` or `stabilized`, where a field that carries no marker takes the maturity fixed by the [maturity of a field](../specification/maturity.md). Aggregated over a project, the map shows the open fields that accepted results rest on.

**Literature.** None cited.

**Bears on.** [`inquiry-views`](../../TODO.md).
