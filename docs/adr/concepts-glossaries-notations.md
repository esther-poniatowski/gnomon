---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Concepts, glossaries and notations
tags: []
source:
---
# Concepts, glossaries and notations

> [!QUESTION] Goal: which record holds the meaning of a concept, which record holds its names, and how does a notation compose its symbols?

The [decision on terminology, audience and project specifications](terminology-audience-project-specifications.md) gives `gnomon` the mechanisms of glossaries and notations. An adversarial review of the formats of `geonexus` then found that their checker reports no issue on three instances, although the defects below sit in those instances:

- **checks declared and never run**: inverse pairs, the acyclicity of narrower terms, and the language of expressions;
- **one entry holding two kinds of fact**: a glossary term mixes the meaning of a concept with its names, so two glossaries define one concept differently, and forbid one form with different replacements;
- **symbols that a notation cannot compose**: the Mixture notation registers 529 symbols, links 25 of them to a term, and lists 60 alternatives under one placeholder condition. Those alternatives mostly enumerate entries, index instances and derivatives of a base symbol;
- **exceptions copied entry by entry**, two of which can never apply;
- **deprecated symbols kept as full entries**.

## Decision

**A concept record holds the meaning of a concept.** The record belongs to the research family, and it states:

- a gloss;
- a kind;
- its broader concept, in one direction only;
- the note that sources it;
- its confusions with other concepts, each with its distinction;
- optionally, a link to a full definition object when one exists.

A concept of another project is referenced, never copied.

**A glossary holds the names of concepts.** Each entry names one concept, with:

- its label and literal variants;
- its patterns of variants;
- its alternative forms with their contexts;
- its names in other frameworks, each with the way to introduce it.

A forbidden form keeps its replacement, its reason and its severity. The form also states the audiences for which it is forbidden, and an absent list of audiences means every audience, so that audience specifications stay independent of projects. An exception to a forbidden form names a shared exception, such as a mention, a quotation or a citation, or states its own pattern. In both cases, it carries an example that the checker tests.

**A notation composes its symbols.** The notation declares once:

- each **base**: a letter or a command with its meaning, linked to the concept that it denotes when it denotes a quantity;
- each **modifier**: a label such as `mix` or `bsl`, a typed superscript, an accent or a mark of derivative, with its meaning, its admitted positions and the bases that admit it;
- each **index set**: the letters that range over it, and the set that they range over, so that a dummy index is bound by its set;
- each **convention**: a font, a reserved letter, the way to write an entry, the commands held equivalent.

An expression is admitted when it parses as one base with admitted modifiers and indices, and its meaning is composed from theirs. When the meaning of a compound symbol does not follow from its parts, the notation declares that symbol explicitly. A deprecated expression is listed as a former form of the symbol that replaces it.

**A glossary composes its sources by merging imports only.** A text is bound to one glossary, an imported entry resolves its references in its source file, and an entry that shadows an imported one is reported.

## Constraints that decide the formats

- **An unreported rule goes unapplied.** The agents writing these records learn the rules from the reports of the checker, so every declared rule is run, and every rule has a planted case.
- **A concept has one meaning, and several names.** The names of a concept vary with the audience and the context, whereas its meaning does not.
- **A combination is generated, not enumerated.** Crossing every label and index with every base multiplies the entries, while each modifier carries one meaning that composes.
- **A form has one schema construct.** Ekphrasis renders a choice between object schemas, but not a choice decided by required keys only, and it writes defaults into new records. Therefore, each alternative is an object schema, and a status is required rather than defaulted.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Keep one glossary entry for meaning and names | One file per project | Two projects then define one concept twice, and a name differing by audience duplicates the meaning |
| Move every audience-specific ban to the audience specifications | Glossaries hold only universal bans | An audience specification then names the forms of each project, so it no longer serves every project |
| Enumerate every symbol with its alternatives | Each written form is listed | The entries multiply with the labels and indices, and the alternatives come to hold entries, instances and other objects |
| Compose symbols from bases, modifiers and index sets | One declaration per meaning, and every written form checked | The checker must parse expressions |

## Consequences

- The concept record joins the research family, and the glossary refers to its concepts.
- The forbidden forms carry their audiences, and the register rules of a project stay in its glossary.
- The checker of `gnomon` rejects any declared check that it does not run. It also compares the label of a symbol with the label of its concept, and scans the prose fields of a glossary for forbidden forms.
- Once an inquiry record declares a quantity, the notation refers to that record for the symbol of the quantity. The Mixture project has no inquiry record yet, so its symbols stay in its notation until its encoding.
- The instances of `geonexus` migrate: its copied exceptions become shared exceptions, its deprecated symbols become former forms, and most of its alternatives become modifiers.
