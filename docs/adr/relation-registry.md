---
tags:
  - decision
status: accepted
created: 2026-11-08
revised: 2026-11-08
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Relation registry
---
# Relation registry

> [!QUESTION] Goal: which file declares the relations between research units, what does each declaration state, and how does a revision travel along a relation?

The [decision on closed typed relations](closed-typed-relations.md) closes the vocabulary of relations and types their ends, and left open the registry that gathers them, with their warrant and their transmission of a revision. Until now, an answer and a question each took their relations from a list of the vocabulary registry. The other relations were written as fields with no declaration, and every reference to a revised record transmitted its revision, prose included. The pilot of a research project needed an incompatibility between answers, a contrast, a supersession of laws and a motivation, and the export to `ekthesis` needs an incompatibility for an antithesis, as the [decision on the scope of gnomon](research-scope.md) states. The candidate formalisms are compared in the [proposals for the relation registry](../proposals/relation-registry.md).

## Decision

One registry in package data, `registries/relations.yml`, declares every relation between research units, and the [note on relations between research units](../epistemology/objects/knowledge/relations-between-units.md) owns their senses. The registry is the source of the closed values of `relations[].relation` of an answer and of a concept and of `links[].relation` of a question, which the vocabulary registry no longer lists. ^one-relation-registry

Each relation declares: ^relation-declaration

- the record kinds that its source and its target may take;
- its arity, `binary` or `set`; a set relation is symmetric, holds of two or more members, and is written once, on one member;
- whether it is symmetric and irreflexive;
- its policy of cycles: forbidden, judged, or admitted, with the exemption of a declared co-definition, and the graph whose cycles are searched as a whole, such as the graph of claims;
- the end that a revision flags, if any, and its warrant: a mode of inference, fixed by the relation, written on its entry, or read from the dependent;
- its class in the contract of the export, or none.

A relation stated by a field of its own, such as the question answered by an answer, keeps its field. The registry names that field by its path, and a test checks each path against the base schema. A reference in another field of an identifier or an expression transmits a revision as a constitutive dependence, and a reference in prose transmits none. A check builds the graph of relations from these fields and from the entries of `relations` and `links`. ^field-relations

A revision travels along each edge separately. The warrant of an edge falls in one of three classes: monotonic, constitutive or defeasible. A revision flags the dependent at the other end when the class transmits its kind, as the [transmission of a revision](../epistemology/objects/knowledge/relations-between-units.md#^transmission) states. An edge without a stated warrant counts as defeasible. No priority orders the revisions. ^edge-transmission

The terms of the pilot resolve into the relations of `gnomon`: a rebuttal into `incompatible-with`, a rivalry of readings into two answers to one question, a motivation into the inputs of a step or `pattern_selection.motivated_by`, and a supersession into `revises` between answers, or into the step that revises a unit, such as a law, by its dotted identifier. A workspace that types the citations between its documents keeps that vocabulary for its documents. Its citations between research units migrate to the relations of `gnomon` when those units become records, and the table that maps its terms onto these relations serves that migration only. Its properties of a presentation belong to `ekthesis`. ^pilot-terms

## Constraints that decide the registry

- **A property that nothing reads is dead data.** Each declared property is read by a check or by the propagation: the ends, the arity, the symmetry, the cycles, the transmission, the class of the export. Transitivity and inverse names are not declared, since no query reads them.
- **A warrant is a kind, not a degree.** The [exposure rule](../epistemology/objects/knowledge/grounds-and-dependence.md#^weakest-link) reports the exposed units instead of a degree, so no order of priority combines with the warrant.
- **A revision must flag exactly what it can invalidate.** A reference written in prose bears no dependence that a revision can invalidate, and a deductive conclusion is not flagged by a reorientation of an answer that it does not interpret.
- **The export reads classes only.** `ekthesis` reads the class of each exported relation, without a code dependency on `gnomon`, as the [decision on the scope of gnomon](research-scope.md) states.

## Options weighed

| Option | Benefit | Reason it is not taken |
| ------ | ------- | ---------------------- |
| Keep the relation types in the vocabulary registry, with properties beside them | One registry fewer | A vocabulary entry carries a value and a gloss only, and the relations stated by fields have no vocabulary at all |
| A record of its own for each relation | A relation carries its own status and context | It fails the [admission of a record kind](record-kind-admission.md#^admission-conditions): the entry already states its ends, and a status local to a link is the warrant of the entry |
| Eight warrant kinds of their own | One kind per manner of support | They restate the modes of inference, whose split into explicative and ampliative inference the theory already draws, and three of them have no theory |
| A priority of revisions, combined with the weakest warrant | One number per flag | A warrant is not a degree, so no warrant is the weakest |
| Assertions qualified by their source, as named graphs | Separates the corpora that assert | One project holds one corpus, and no check reads the name of a graph |
| A relation of a pair only | A simpler declaration | An incompatibility can hold of three claims and of none of their pairs, and a co-definition holds of a cluster |

## Consequences

- This registry completes the [decision on closed typed relations](closed-typed-relations.md). The provisional rule of the [decision on revision accountability](revision-accountability.md), under which every reference transmits a revision, gives way to the transmission along each edge.
- The relations `incompatible-with` and `defeats` fill the class of incompatibility of the export, left open by the [decision on the scope of gnomon](research-scope.md). An incompatible set of more than two members has no class of the contract yet.
- A new family of rules, `relation/`, reports a mistyped end, a relation of a unit to itself, a forbidden cycle, a judged cycle, a symmetric relation stated twice, and an attribute that a relation does not admit.
