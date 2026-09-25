---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Flat symbol table
tags: []
source:
---
# Flat symbol table per record

> [!QUESTION] Goal: in which scope does a symbol of an inquiry record resolve?

An inquiry record declares the elements of a system — its parts, its indices, its quantities and its laws — and every formula of the record names them by symbol. The scope in which a symbol resolves determines three properties:

- whether one identifier can denote two quantities;
- whether a reference from another record reaches its target;
- whether a reader locates a declaration by reading one table.

## Decision

Each record carries one flat table of symbols, and each symbol is unique within the record. A quantity that belongs to an external system is declared among the entries of the record and marked with its owner. Members of one reference class that differ in their declarations partition that table by variant.

## Constraints that decide the scope

- **The uniqueness rule and every inbound reference assume one table.** A reference from another record names a record and a symbol, so a second level of naming inside a record would leave that reference unable to address its target.
- **Two attributes would each introduce a scope.** Nesting a quantity inside its external system, or nesting the declarations of a variant inside a schema of their own, introduces scopes for one attribute apiece, and the resolver then carries a scope rule for each.
- **A member of a class is generated from the declarations that it carries.** Marking each entry with the variant that carries it keeps one table while separating the members, so a claim left unmarked ranges over the whole class.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Nest a quantity inside the external system that owns it | The owner is read from the position of the entry, and no mark is needed | The nesting introduces a scope for one attribute, and every inbound reference to that quantity must then address two levels |
| Give each variant a schema of its own | Each member is read alone, and no entry of its schema needs a mark | The uniqueness rule and every inbound reference assume one table per record, so the schemas would reintroduce scopes for one attribute |
| One flat table, with an owner mark and a variant mark | One reference form addresses every declaration, and a reader locates each symbol in one table | Two marks must be read to establish which members carry a symbol, and a claim that names a marked symbol without carrying the mark is reported only by a check |

## Consequences

- A reference resolves by naming a record and a symbol, in the form that [symbols and expressions](../epistemology/symbols-and-expressions.md) fixes.
- A claim left unmarked asserts a property of every member of the reference class, so the checks report a law, a relation or an external system that names a symbol that only some members carry.
- One symbol table is generated per problem, reversing an earlier decision to collect none. The earlier decision followed from the absence of scope across the corpus. An author fills and consults the records of one problem together, so one table per problem serves the author.
