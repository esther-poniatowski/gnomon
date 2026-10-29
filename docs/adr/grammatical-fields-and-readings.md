---
tags:
  - decision
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Grammatical fields and prose readings
---
# Grammatical fields and prose readings

> [!QUESTION] Goal: which fields of a record may a tool interpret, and what may a prose field hold?

A record holds two kinds of field. The value of a grammatical field follows a declared grammar: a value of a closed vocabulary, an identifier, an expression over declared symbols, or a block of declared keys. The value of a prose field is free text, such as the `statement` of a problem, the `reading` of a law, or the `description` that identifies a phenomenon. The [phenomenon template](../../src/gnomon/data/templates/phenomenon.yml) marks its statement as "a reading only", and other templates mark a reading as holding "only content beyond" the fields beside it. No decision stated which of these fields a tool may interpret.

## Decision

A tool interprets the value of a field only when a grammar declares that value. The grammars are the closed vocabularies of the [registries](registries-as-source.md), the [dotted identifiers](dotted-identifiers.md), the [expressions](expression-syntax.md) over declared symbols, and the blocks that a [record schema](record-schemas.md) declares. ^grammar-for-read-fields

A prose field is opaque to every tool. A requirement may test that a prose field is filled, and no tool reads its content to resolve, count, compare, derive or check anything. ^prose-opaque

A prose field holds a reading for a reader. The reading restates grammatical fields in words, or states content that no field of the record can yet express. When a reading restates grammatical fields, those fields carry the fact, and the reading yields to them. ^reading-yields

Content that only a prose field holds receives no check and enters no relation. A distinction that a check must read earns a grammatical field, on the [grounds for a shared field](shared-field-grounds.md). ^prose-unchecked

The cost of writing a grammatical value is paid in full, never lowered by admitting prose in its place. An author lowers that cost by leaving the field empty until the inquiry fills it, and the requirements registry states when an empty field is a gap. ^cost-of-grammar

## Constraints that decide the partition

- **A check that reads prose depends on its wording.** The decision on registries excludes the method notes from the checks for that reason, and the reason holds for a prose field inside a record.
- **An inquiry starts before its grammatical fields can be filled.** A phenomenon at the commitment `identified` is fixed by a definite description and by pointers, before any observable is declared, so a prose field is required at that commitment.
- **A field read by a tool must hold one kind of value.** A field that admits either a sentence or a grammatical value obliges every tool that reads it to test which kind it holds, and a sentence in it yields no verdict.
- **A grammatical value costs more to write than a sentence.** The retired design notes (commit 9e138e2) record this tension between formal expression and authoring cost, for rationales and explanatory gains in particular.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------- | ---------------------------- |
| Admit prose in a field that a tool reads, and extract its value with a parser or a language model | Authors write sentences, and every field still contributes to the checks | Two phrasings of one claim receive different verdicts, and the extraction infers content, which the [decision against inference at run time](no-run-time-inference.md#^excluded-inference) excludes |
| Forbid every prose field | Every value of a record is checkable | A phenomenon at the commitment `identified` cannot be stated, and a reader loses the reading of each expression |
| Annotate prose with typed values inline, as a semantic wiki does [krotzsch2006] | One text serves the reader and the checker | The checker must locate the annotations inside the text, so it depends on the format of that text, as a checker reading a note does |
| Let a field rise from prose to a grammatical value as the inquiry matures | An author records content before formalizing it | One field then holds values of two kinds, whereas the key `maturity` already records how far each field is settled |
| Grammatical fields interpreted by tools, prose fields opaque to them | Each verdict follows from grammatical values, and a reader keeps a reading of each | A reading can drift from the fields that it restates, and no check reports the drift |

## Consequences

- A requirement such as the `statement` of a problem tests presence only.
- The count of unused declarations in `src/gnomon/vocabulary.py` reads the whole text of the records, readings and comments included, so a symbol named only in a reading counts as used. The count must be restricted to grammatical fields.
- A reading that only restates its fields can be generated by a renderer, which removes the drift. The [question template](../../src/gnomon/data/templates/question.yml) names such a command, `gnomon render`, which does not exist yet.
- A relation between records is a grammatical value, so its type is never stated in prose, as the [decision on closed typed relations](closed-typed-relations.md#^closed-relations) states.

---
## Sources

Marks follow the [legend of reading marks](../../CONTRIBUTING.md#^reading-marks). A mark ◐ records a check of the bibliographic record.

- [krotzsch2006] ◐ Krötzsch, Vrandečić & Völkel, "Semantic MediaWiki", in *The Semantic Web – ISWC 2006*, Lecture Notes in Computer Science 4273, Springer, 935–942, 2006
