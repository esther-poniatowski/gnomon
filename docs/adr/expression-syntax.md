---
role: decision
status: accepted
index: "[Architecture decisions](docs/adr/_index.md)"
aliases:
  - Expression syntax
tags: []
source:
---
# Surface syntax and parseable core for expressions

> [!QUESTION] Goal: in which language are the formulas of an inquiry record written, so that a check can resolve their operands and a reader can follow them?

An inquiry record states its laws, its derived quantities and its manifestations as expressions over declared symbols. The syntax those expressions use decides three things at once: whether a check can resolve each operand, whether a problem can add the mathematics it brings, and whether the author writes something legible.

## Decision

The infix surface stays as authors write it, and a grammar defines that surface over an S-expression core. A parser then operates on the core, and no record changes.

## Constraints that decide it

- **Operands must resolve.** Every check the framework runs — 273 of them — rests on `u` in a law resolving to the `u` a record declares. A syntax that cannot be scanned for identifiers removes the guarantee the framework exists to give.
- **A problem must extend the operator set.** Turbulence declares `div`, `lap` and `restrict`; microbial declares `spectrum`. No fixed external vocabulary admits these, so the syntax must treat an operator as a declared symbol rather than as a reserved word.
- **The author writes mathematics.** The corpus is read by researchers who write infix and LaTeX, and a surface far from that raises the cost of every record.

## Options weighed

| Option | What it buys | Why it is not taken alone |
| ------ | ------------ | ------------------------- |
| LaTeX as the source | Authors already write it; it renders directly in the notes | It encodes presentation, not structure: `\frac{a}{b}` and `a/b` are one quantity, `\mathbf{u}` carries no type, and `\alpha_i` against `\alpha_{i}` makes identifier extraction ambiguous. Resolution, the property the framework depends on, is what LaTeX withholds. |
| SymPy expressions | A parser and a simplifier already exist | The semantics assume commutative algebra over numbers. An index set, a constituent kind and `measures(Z)` have no counterpart, so a large part of the corpus falls outside what the parser means. |
| MathML or OpenMath | Standardised, and extensible through content dictionaries that match the per-problem operator mechanism | The serialization is XML, unwritable by hand inside a YAML record, and no consumer reads that serialization. |
| A proof assistant's term language | Full semantics, and mechanically checkable proofs | It demands that the inquiry be formalized, a later and separate undertaking. Specifying an inquiry is not proving one. |
| An S-expression core under the infix surface | One grammar rule, a parser of a few lines, no reserved vocabulary, and free and bound variables that fall out of the structure | Read directly it is harder than infix, so the surface is kept. |

## Consequences

- A signature becomes derivable from the expression that defines a quantity, rather than declared beside the quantity. The current check is lexical and cannot compare the two, so a record may declare a signature its definition contradicts.
- The operator set stays open: an operator is a head symbol, and a problem declaring one needs no change to the grammar.
- Rendering stays separate from parsing. Each operator carries a LaTeX template, so a renderer composes the printed form without reading the grammar.
- Writing the grammar is the remaining work. Until then the lexical check resolves identifiers without parsing binders.
