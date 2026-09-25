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

An inquiry record states its laws, its derived quantities and its manifestations as expressions over declared symbols. The syntax of those expressions determines three properties at once:

- whether a check can resolve each operand;
- whether a problem can declare the operators that its mathematics requires;
- whether the author writes a legible formula.

## Decision

A grammar defines the infix surface that authors write over an S-expression core, and a parser operates on that core. Because the surface stays unchanged, no record has to change.

## Constraints that decide the syntax

- **Operands must resolve.** Each of the 273 checks of the framework assumes that the `u` in a law resolves to the `u` that a record declares. A syntax that cannot be scanned for identifiers leaves operands unresolved, so the framework loses the guarantee that it exists to give.
- **A problem must extend the operator set.** For instance, the turbulence problem declares `restrict` and `regions`, and the microbial problem `community_jacobian`. No fixed external vocabulary admits these names, so the syntax must treat an operator as a declared symbol rather than as a reserved word.
- **The author writes mathematics.** The corpus is read by researchers who write infix notation and LaTeX, so a surface syntax that differs from both raises the cost of writing each record.

## Options weighed

| Option | Benefit | Reason it is not taken alone |
| ------ | ------------ | ------------------------- |
| LaTeX as the source | Authors already write it, and it renders directly in the notes | It encodes presentation, not structure: `\frac{a}{b}` and `a/b` are one quantity, `\mathbf{u}` carries no type, and a scanner cannot tell whether `\alpha_i` and `\alpha_{i}` name one identifier. LaTeX therefore does not support resolution, the property that the framework depends on. |
| SymPy expressions | A parser and a simplifier already exist | The semantics assume commutative algebra over numbers, so an index set, a constituent kind and `measures(Z)` have no counterpart. The parser therefore assigns no meaning to a large part of the corpus. |
| MathML or OpenMath | Standardized, and extensible through content dictionaries that match the mechanism by which each problem declares its operators | Both standards serialize to XML: no consumer of the corpus reads that format, and an author cannot write it by hand inside a YAML record. |
| A proof assistant's term language | Full semantics, and mechanically checkable proofs | The term language requires the inquiry to be formalized, and that step belongs to a later and separate undertaking, because the framework specifies an inquiry without proving any of its claims. |
| An S-expression core under the infix surface | One grammar rule, a parser of a few lines, no reserved vocabulary, and free and bound variables readable from the structure | An S-expression is harder to read than infix notation, so the core stays under the surface that authors write. |

## Consequences

- A signature becomes derivable from the expression that defines a quantity, rather than declared separately. Deriving the signature excludes a contradiction that the current check cannot detect: that check is lexical and cannot compare a declared signature with the defining expression, so a record may currently declare a signature that its own definition contradicts.
- The operator set stays open: an operator is a head symbol, so a problem that declares a new one needs no change to the grammar.
- The renderer stays separate from the parser, because each operator carries a LaTeX template from which a renderer composes the printed form without reading the grammar.
- The grammar remains to be written. Until it is, the lexical check resolves identifiers without parsing binders.
