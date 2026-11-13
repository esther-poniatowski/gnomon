---
tags:
  - decision
status: accepted
created: 2026-11-09
revised: 2026-11-13
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Schema contract compatibility
---
# Schema contract compatibility

> [!QUESTION] Goal: when must a schema contract receive a new logical version, and when may Gnomon stop exporting an earlier version?

The [decision on record schemas](record-schemas.md) binds each record or view to a logical contract through `_schema`. Consumers resolve that contract through a registry materialized from an exact repository commit. Therefore, a schema change must preserve both the meaning of the logical identifier and the ability of a maintained consumer to open an existing document.

## Decision

This rule governs changes accepted after this decision. A logical contract version identifies one validation and rendering contract. Gnomon increments the integer after `@` when either of two properties changes:

- the set of documents admitted by the schema changes;
- a renderer must interpret an admitted document differently, including a change to a control selected by an extension keyword such as `x-kind`.

An editorial correction to a title, description or example retains the version only when the correction leaves the field meaning and renderer behavior unchanged.

The current schema file owns the newest logical version. Each earlier published version remains available as an immutable compatibility schema and remains listed among the exported contracts. Gnomon removes an earlier contract only through a later accepted decision that identifies the contract and establishes three facts: current Gnomon can regenerate or migrate its documents, every maintained consumer accepts the replacement, and no maintained artifact still requires the earlier contract.

The required compatibility direction is backward reading. An updated consumer must open a document bound to an earlier exported contract. The retained schemas make this behavior possible. Consumer support and cross-repository tests remain separate implementation requirements. A consumer pinned to an earlier schema closure need not accept a document emitted under a later contract.

## Contract and resource identities

The `_schema` value is the stable contract identity. The `$id` value identifies one physical schema resource inside a commit-pinned closure. Therefore, the unversioned path of a current schema can advance between commits, while a compatibility schema receives a distinct physical path and preserves its earlier logical contract. A consumer resolves both resources through the registry from the pinned commit instead of dereferencing the repository default branch.

## Migration rule

An authored record is migrated because it is the source of research content. A generated view is regenerated from its authored records and is never edited into conformance. The regenerated view names the current contract and identifies its inputs through `source_state`.

## Current transitions

### View source state

Adding required `source_state` changes every view contract in both directions. A new view fails its predecessor because the predecessor rejects undeclared properties. An old view fails the new schema because the field is required. Therefore, all ten current view contracts receive new versions, and their ten predecessors remain exported from the compatibility folder.

### Record maturity

Binding the maturity of a field to `open`, `provisional` or `stabilized` narrows validation and replaces a generic value control with a closed choice. Therefore, the fourteen record contracts that carry a `maturity` mapping advance from version 1 to version 2. The itinerary contract remains at version 1 because it carries no maturity mapping. Each version-1 record contract remains exported from the compatibility folder and retains the unrestricted maturity values admitted before the transition.

### Starting-record source pointers

Adding the optional field `sources` broadens the set of admitted question documents. Admitting existing notes and models through `problem.sources` changes the meaning and rendered guidance of that field. Therefore, the problem and question contracts advance from version 2 to version 3. Both version-2 contracts remain exported. The retained question contract continues to reject the undeclared field, while the retained problem contract preserves its earlier guidance.

### Promoted model and answer source pointers

Adding the optional field `sources` broadens the model and answer document sets. Therefore, both contracts advance from `@2` to `@3`. Their `@2` contracts remain exported. Those contracts reject the undeclared field.

### Sentence kinds of generated views

Three generated view fields hold sentences, while their contracts declared the kind `label`, which a renderer reads as one word. The reason of an exposure joins vocabulary terms and identifiers into plain words, so it takes the kind `text`. The authored statement of a question copies the field `statement`, of kind `markdown-line`. The composed statement inserts titles and names of the same kind. Therefore, both statements take `markdown-line`. The exposure generator also emits the kind `commitment` for a product of a decision or generation activity, so the current contract admits that value. The renderer changes and the added enum value change the rendering contract and the set of admitted documents. Therefore, the exposure contract advances from `@3` to `@4`, and the question-statements contract from `@2` to `@3`. Both predecessors remain exported and keep the kind `label`; exposure `@3` also keeps its earlier enum. A renderer that limits a label to one word therefore reports a view bound to a predecessor until that view is regenerated.

### Grouped next acts

The next-act view grouped no acts in its data, although the diagnosis assigns every act to one open condition. The current view keeps each open condition with its acts. Therefore, a schema-derived renderer presents one research choice and the activities that address it as one unit. This structural and rendering change advances the next-act contract from `@3` to `@4`. The retained `@3` contract keeps the flat table for existing generated views.

### Required predecessors and ready acts

The grouped acts table combined two different relations. A ready act is a choice available now. A waiting activity has input types that an unimpeached record must hold before that activity can run. The current view places those requirements under *Required predecessors* and the available choices under *Ready acts*. It does not select how the researcher will satisfy a missing input. This structural and rendering change advances the next-act contract from `@4` to `@5`. The retained `@4` contract keeps the combined acts table for existing generated views.

### Operative consequences of acts

An activity name and its readiness do not state what selecting the activity can change. The current view adds its required inputs, output type and possible storage locations. It also lists waiting activities that admit the output type as a missing input. This last relation is conditional because the selected activity must pass its norm. Another product of the same type may also satisfy the downstream slot. These added fields change the admitted documents and their rendered tables. Therefore, the next-act contract advances from `@5` to `@6`. The retained `@5` contract keeps the earlier rows for existing generated views.

### Act appraisals

An itinerary previously recorded only acts already selected as steps. The current contract adds optional act appraisals before a selection. Each appraisal holds researcher-supplied criteria, ordered scales, preferred directions, available means and grounded judgments. Gnomon neither supplies the judgments nor ranks the acts. The added field broadens the admitted document set. Therefore, the itinerary contract advances from `@1` to `@2`, while the retained `@1` contract continues to reject the undeclared field.

### Transparent act comparisons

The comparison requires a declared rule and a stable identifier for each considered act. These fields broaden the admitted itinerary documents. Therefore, the itinerary contract advances from `@2` to `@3`, while version 2 retains appraisals without comparison fields.

The next-act view now displays the authored criteria, judgments and bases. It also displays each relation derived by ordinal dominance and the undominated acts. These additions change its documents and rendering. Therefore, the next-act contract advances from `@6` to `@7`, while version 6 retains the diagnosis without comparisons.

### Selected-view coverage

A view selected for one completion target may carry a coverage block. The first coverage table names the authored records read by Gnomon. The second table names each absent record kind. The same row names the subsequent completion target that requires the kind. The new field admits documents rejected by each preceding contract and changes their rendered form. Therefore, problem-state advances from `@2` to `@3`. Next-act advances from `@7` to `@8`. Exposure advances from `@4` to `@5`. Their immediate predecessors remain exported without coverage.

### Exposure reachability graph

The exposure view now requires a graph before its detailed findings table. The graph contains only answers named in exposure rows. Each such answer appears once. Each exposing unit also appears once. For each answer–unit pair, one edge aggregates the reasons and recorded routes. The new nodes, edges and graph-rendering roles change both the admitted views and their rendering. Therefore, exposure advances from `@5` to `@6`. The retained contract `@5` preserves the table-only view for existing generated views.

### Itinerary dependency graph

The itinerary-progress view now represents each step and state origin as a node. Directed edges preserve every dependency, including cycles and multiple predecessors. The state `not-produced` separates an output not yet recorded from a sound output. Because these changes alter the structure and rendering, the contract advances from `@3` to `@4`. The retained contract `@3` preserves the tabular steps and edges for existing generated views.

### Assembly topology graph

The assembly view now requires a graph before its detailed tables. The graph gives each level, component and part one node. Each component edge retains its level context. The tables retain citation provenance, counts and gaps. The tables also list limits and exclusions. The graph changes the admitted documents and their rendering. Therefore, assembly advances from `@2` to `@3`. The retained contract `@2` preserves the table-only view for existing generated views.

## Alternatives weighed

The alternatives differ in whether they preserve provenance and existing artifacts.

| Option | Benefit | Reason it is not selected |
| --- | --- | --- |
| Keep the old logical identifiers and make `source_state` optional | No version transition | A schema pinned before the change rejects the new property, while an optional field cannot establish provenance |
| Export only current contracts and require immediate regeneration | No compatibility archive | A current renderer cannot open an existing generated view during a non-atomic upgrade |
| Retain only the immediately preceding version | Bounded archive size | The bound can remove a contract still required by a maintained artifact or consumer |
| Retain published contracts until an explicit retirement decision | Existing artifacts remain readable | Each incompatible change adds an immutable schema until the retirement evidence exists |

## Consequences

This decision imposes four requirements.

- The schema resource record exports current and retained logical contracts.
- The generated schema registry maps each retained logical identifier to exactly one schema file.
- Tests validate newly generated views against current contracts and equivalent views without new fields against their retained predecessors.
- Gnomon may remove a contract only through a separate decision supported by migration evidence. Removal during an unrelated change is invalid.
