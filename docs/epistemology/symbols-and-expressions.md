---
role: definition
status: stable
index: "[Epistemology](docs/epistemology/_index.md)"
aliases:
  - Symbols and expressions
  - Symbols of an inquiry record
tags: []
source:
---
# Symbols and expressions of an inquiry record

> [!QUESTION] Goal: how does a record name the quantities it declares, so that a formula in one field reaches a quantity declared in another?

Every quantity that an inquiry record declares carries a symbol, unique within that record. A reference names that symbol, and a formula is an expression over symbols, so one field reaches a quantity that another field declares. [One letter for one meaning across the notes](notation.md) fixes the same discipline for the alphabet of the method itself.

A prose name does not resolve to an entry. A name written as "velocity field u(x,t)" holds a symbol, a name and a signature at once, so a second field reaches the quantity only by repeating the whole string, and a formula can name a symbol that no entry declares.

| Construct | When it is required | Form | Examples |
| --------- | ------------------- | ---- | -------- |
| Symbol | with every declared quantity | an identifier of letters, digits and underscores, opening on a letter, unique within the record | `u`, `nu`, `N`, `L_train`, `m_N` |
| Name | with every declared quantity, law, manifestation, source of variation and test | what the entry is called, in words, carrying no symbol, no signature and no formula | "velocity field"; "kinematic viscosity"; "minimum equilibrium population abundance" |
| Reading | when a formal field stands beside it | what that field says, in words: the mechanism a formula encodes and why it is written that way | "the scale at which viscous dissipation balances the energy handed down the cascade" |
| Justification | when the entry records a choice the inquiry made | why the choice was made, and what an entry without it would fail to deliver | "a forecast is usable only if it commits to how likely each transition is" |
| Differentiation | when a near neighbour could be taken for it | what it carries that the others do not, or what it cannot distinguish | "pooling over positions and times discards the arrangement, so two regimes laid out differently share this distribution" |
| Procedure | when the entry is carried out rather than stated | how it is done or established | "a candidate regime recurs across stochastic realizations and survives longer observation windows" |
| Caveat | when the record leaves something unstated here | what is missing and why, beside any of the four above | "the record declares no curvature operator, so the concavity the measurements show is not written" |
| Reference | when a field names a quantity of its own record | the symbol alone | `signature: [x, t]`; `realized_by: [transmit]`; `shares: [f]` |
| External reference | when a field names a quantity of another record | the identifier of that record, then the symbol | `system.turbulence#u` |
| Expression | when a field states a formula | symbols joined by operators and by binders, each quantity carrying its indices as arguments | `U * L / nu`; `div(u) = 0` |
| Binder | when an expression consumes an index | `aggregator_{indices}(expression)`, the aggregator drawn from `mean`, `sum`, `min`, `max`, `dist`, `ft` | `min_{i}( N(i) )`; `mean_{x, t}( u(a, x, t) * u(b, x + r, t + tau) )` |
| Signature | with every declared quantity | the indices the quantity still takes | `[]` for a scalar; `[a, b, r, tau]` for a correlation matrix |

- **A symbol is unique within its record, not across records.** Two targets may each declare `L`. A reference from outside carries the record identifier, so the record and the symbol together identify a quantity globally. Within one record, two entries declaring the same symbol are a defect, and one entry declaring two quantities is the same defect seen from the other side: "cross-coupling operators G_AB and G_BA" must become two entries.

- **A compound value is quoted; a bare symbol and a vocabulary token are not.** Inside a bracketed list the quotes are load-bearing rather than stylistic: `[maps(prod(a, b), reals)]` splits on its commas into three items, and the record then holds plausible fragments instead of one expression. Outside a list the serializer needs no quotes, so the rule is written for the reader: quotation marks mark a value that is more than one identifier. ^quote-compound-values

- **A symbol that a serializer reads as another type is quoted.** YAML resolves the unquoted words `on`, `off`, `yes`, `no`, `y`, `n`, `true`, `false`, `null` and `~` to booleans or to nothing, so a symbol drawn from that set arrives as a value of another type and its declaration disappears. Writing it in quotes keeps it a symbol, and choosing another identifier avoids the question. ^quote-serializer-keywords

- **A name, a symbol and a prose field answer different questions.** The name says what the entry is called, the symbol is the handle every formula and reference uses, and the prose carries what the two of them leave unsaid, under the key naming the job it does. A symbol repeated inside a name or a prose field creates a second handle that nothing resolves, and a formula there belongs in the field that holds formulas: `Re := U L / nu` is the expression of `Re`. ^name-symbol-prose

- **The extent of a set names its members, not the values they carry.** A constituent kind collects identified units, so its extent is the identifying set: `range(S)` for `S` populations, `enum("A", "B")` for two named species. A cardinality is read off that set with `card`, and a bound on the cardinality is a constraint, not an extent. Writing `pos(ints)` as an extent would say that the units are every positive integer. ^extent-identifies-members

- **A value set and an extent are expressions, not prose.** `values` names the set a quantity takes its values in, and `extent` names the set a constituent kind or an index set collects, each written with the set constructors. A restriction the laws already impose is not repeated there: a velocity field takes values in `maps(x, pow(reals, 3))`, and its divergence-free condition is a law. A set the case does not fix is named by a declared parameter rather than described, so `U(sp)` refers to an admitted local state space that the record declares. ^value-sets-are-expressions

- **One field name carries every expression, and its position fixes what the expression does.** An expression inside a quantity introduces that quantity, so it cannot be false of the system. An expression inside a law or a manifestation asserts something about the system, so it can. Naming the two alike keeps the syntax one thing; the block already separates what they do. ^expression-position

- **A notation renders a symbol or an operator in LaTeX, and a renderer composes the rest.** A symbol carries the form it prints as, omitted where the symbol prints as itself, and the value is written in single quotes: a double-quoted serializer reads `\n` in `\nu` as a newline, so the form arrives broken. An operator carries a template, with `#0` for the indices a binder consumes and `#1`, `#2` for its arguments, so `mean` renders `\langle #1 \rangle_{#0}` and `maps` renders `#1 \to #2`. The source stays the expression the checks read, and the LaTeX is derived rather than written a second time. ^notation-renders-in-latex

- **Prose interprets; it does not reformulate the name.** `d_t(N) = 0` states that the abundances sit at a fixed point, and a reader who has to reconstruct that from the syntax is paying for the formality, so the reading says what the expression encodes and why it is written that way. A prose field whose content words are already in the name, such as "the chance that a subsystem transitions at or before the horizon" beside the name "probability that a subsystem transitions by the horizon", states nothing and is a defect. It never states a fact the typed fields could hold either, since a commitment recorded twice drifts. ^prose-interprets

- **A quantity fixed by a condition rather than by a map carries that condition, and thereby a presupposition.** An `expression` builds the quantity from others, so it cannot be false of the system. A `condition` states what the quantity satisfies — an equilibrium satisfies `d_t(N) = 0` — so it introduces the quantity and presupposes that a value satisfying it exists. The record carries one of the two, never both. Where several values satisfy the condition, `selects` fixes the reading: `unique` presupposes exactly one, `any` makes the claim hold of whichever value satisfies it, and `all` makes the quantity the set of them. ^condition-presupposes-existence

- **The free indices of an expression form the signature.** A binder consumes the indices it names, and the indices left free are the ones the defined quantity still takes. `min_{i}( N(i) )` binds `i` and leaves nothing free, so the minimum abundance is a scalar and its signature is empty. `mean_{x, t}( u(a, x, t) * u(b, x + r, t + tau) )` binds `x` and `t` and leaves `a`, `b`, `r` and `tau` free, so those four form the signature. An operator that introduces an index rather than consuming one, such as `ft`, contributes the introduced index to the signature.

- **A binder consumes several indices at once.** `mean_{x, t}` averages jointly over position and time. No field holding one index and one retention token expresses that joint average. The aggregator also names the map that collapses an index, so a minimum is distinguished from a mean where the index is collapsed. ^binder-consumes-several

- **Grain is fixed by the signature and the definition, so no field records it separately.** An index absent from the signature was consumed by a binder, and the aggregator naming that binder determines how. For a quantity with no definition, the signature alone fixes the grain: an index it retains is kept apart, and an index it omits was never taken.

- **An index set is declared only when neither a constituent kind nor a parameter of a constituent supplies the set.** Units carrying positions on a lattice need no index set: the units are the constituents, and each coordinate is a parameter defined over a unit, so a quantity indexed "by position" is indexed by the unit. A continuum field has no units, so position is the index and the constituents are empty. A field over a lattice may be modelled either way, and the record states the way chosen. ^index-set-admission

- **The canonical operators are the ones the framework's own semantics require.** [The operator registry](../../src/gnomon/data/operators.yml) owns the set, and the list here documents that registry. Binders realize the signature rule and the limits the domain may take: `mean`, `sum`, `min`, `max`, `dist`, `limit`, `norm`. Relations realize the forms a manifestation may take and the distributional law a record may state: `implies`, `depends_on`, `increasing`, `decreasing`, `drawn_from`. A transform that consumes the indices it binds is a binder too: `ft`. Set constructors build a value set or an extent, name the shapes a reader meets most often, and relate two sets: `reals`, `ints`, `bools`, `complex`, `pos`, `nonneg`, `vectors`, `matrices`, `prod`, `enum`, `range`, `interval`, `maps`, `measures`, `card`, `subset`, `intersect`, `union`, `empty`. The maps admitted everywhere are the derivative of a quantity along an index it takes, `diff`, its magnitude, `abs`, and the operations of general mathematics that no problem owns: `dot`, `adjoint`, `re`, `spectrum`, `jacobian`, `grad`, `div`, `lap`. One constant is admitted: `infinity`, the value a limit of the domain runs to. ^operator-groups

- **One operator vocabulary serves one problem.** Every record of a problem reads the same operator file, so a phenomenon, its target and its questions draw on one set and no record declares an operator a sibling already declares. An operator is typed over the sets the problem declares, in whichever record declares them, so the file is read against the problem rather than against one record. ^one-operator-file

- **A problem declares the mathematics it brings.** The `operators.yml` of a problem declares each operator its records use beyond the canonical set, and those operators resolve in that problem alone. A divergence, a spectrum or a Fourier transform belongs to the problem needing it, not to the framework, so the canonical set stays at what every inquiry can assume. ^local-operators

## The operator record

One file per problem holds the operators its records declare, filled from `src/gnomon/data/templates/operators.yml`. It names the target system of the problem, so a reader reaches the sets the operators are typed over.

| Specification | When it is required | Form | Examples |
| ------------- | ------------------- | ---- | -------- |
| Operators | when a formula of any record of the problem uses an operator beyond the canonical set | one entry per operator | the divergence of a field; the spectrum of a matrix; a Fourier transform |
| Operators: name | with every operator | what the operator computes, in words, carrying no symbol and no formula | "the divergence of a vector field" |
| Operators: symbol | with every operator | an identifier, unique across the problem and distinct from every declared quantity | `div`, `spectrum`, `ft` |
| Operators: notation | when the operator prints as more than its symbol | a LaTeX template in single quotes, `#0` for the indices a binder consumes and `#1`, `#2` for its arguments | `'\nabla \cdot #1'`; `'\operatorname{spec}( #1 )'` |
| Operators: for any | when the operator is general in the sets it acts on | the type variables its types below may name, so a general operator is typed once instead of at the one call site it happens to have | `[S]` for an adjoint, typed `maps(S, S)` to `maps(S, S)`; `[S, n]` for an inner product of two vectors | — |
| Operators: signature | with every operator | the set expression of each argument it takes, in order | `["maps(Om, pow(reals, 3))"]` |
| Operators: values | with every operator | the set expression its result lies in | `"maps(Om, reals)"`; `reals` |

- **One table collects the symbols of one problem, and none collects those of a corpus.** A problem fills several records that reference one another, so its author consults a table spanning them, generated from those records. Across problems there is nothing to collect: the same letter denotes different quantities in different problems, and the scoping rule admits the repetition. ^one-table-per-problem

- **Resolution is lexical, so a signature is declared rather than derived.** Every identifier occurring in a formula must resolve to a declared symbol, and every reference must resolve to one entry. A signature is computed from its definition only by a parser that reads the binders. Until such a parser exists, a record can declare a signature that its own definition contradicts. ^resolution-is-lexical
