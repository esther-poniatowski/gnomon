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

> [!QUESTION] Goal: how does a record name its quantities, so that a formula in one field reaches an entry of another field?

Within an inquiry record, each declared quantity carries a symbol that no other entry shares. Through that symbol, one field reaches a quantity that another field declares: a reference names it directly, and a formula combines it with others into an expression. The same rule governs the symbols of the method itself: [one letter carries one meaning across the notes](notation.md).

A prose name cannot replace the symbol, because such a name resolves to no entry. For example, a name written as "velocity field u(x,t)" holds a symbol, a name and a signature at once. A second field then reaches the quantity only by repeating the whole string, and a formula can name a symbol that no entry declares.

| Construct | When it is required | Form | Examples |
| --------- | ------------------- | ---- | -------- |
| Symbol | with every declared quantity | an identifier of letters, digits and underscores that starts with an alphabetic character and is unique within the record | `u`, `nu`, `N`, `L_train`, `m_N` |
| Name | with every declared quantity, law, manifestation, source of variation and test | the words that designate the entry, carrying no symbol, no signature and no formula | "velocity field"; "kinematic viscosity"; "minimum equilibrium population abundance" |
| Reading | when a formal field stands beside it | the content of that field in words: the mechanism that a formula encodes and the reason for its written form | "the scale at which viscous dissipation balances the energy handed down the cascade" |
| Justification | when the entry records a choice the inquiry made | the reason for the choice, and the product that it secures for the entry | "a forecast is usable only if it commits to how likely each transition is" |
| Differentiation | when a near neighbour could be taken for it | the content that the entry carries and its neighbours lack, or a distinction that it cannot draw | "pooling over positions and times discards the arrangement, so two regimes laid out differently share this distribution" |
| Procedure | when the entry names an operation that is *carried out* | the steps by which it is performed or established | "a candidate regime recurs across stochastic realizations and survives longer observation windows" |
| Caveat | when the record leaves some content of the entry unstated | the missing content and the reason for its absence, beside a reading, a justification, a differentiation or a procedure | "the record declares no curvature operator, so the concavity the measurements show is not written" |
| Reference | when a field names a quantity of its own record | the symbol alone | `signature: [x, t]`; `realized_by: [transmit]`; `shares: [f]` |
| External reference | when a field names a quantity of another record | the identifier of that record, then the symbol | `system.turbulence#u` |
| Expression | when a field states a formula | symbols joined by operators and by binders, each quantity carrying its indices as arguments | `U * L / nu`; `div(u) = 0` |
| Binder | when an expression consumes an index | `aggregator_{indices}(expression)`, the aggregator drawn from `mean`, `sum`, `min`, `max`, `dist`, `ft` | `min_{i}( N(i) )`; `mean_{x, t}( u(a, x, t) * u(b, x + r, t + tau) )` |
| Signature | with every declared quantity | the indices the quantity still takes | `[]` for a scalar; `[a, b, r, tau]` for a correlation matrix |

- **A symbol is unique only *within* its record.** For example, two targets may each declare `L`. A reference from another record therefore prefixes the identifier of the declaring record, and the resulting identifier is unique across the corpus. Within one record, two entries declaring the same symbol are a defect. One entry declaring two quantities is the converse defect: "cross-coupling operators G_AB and G_BA" must become two entries.

- **Only a compound value is quoted: a bare symbol and a vocabulary token stay unquoted.** Inside a bracketed list, the quotes change the parsed value: unquoted, `[maps(prod(a, b), reals)]` splits on its commas, so the record holds one expression cut into three plausible fragments. Outside a list, the serializer parses a compound value the same way in either form. The rule then serves the reader: quotation marks signal that the enclosed string holds more than one identifier. ^quote-compound-values

- **A symbol that a serializer reads as another type is quoted.** YAML resolves ten unquoted tokens to booleans or to nothing: `on`, `off`, `yes`, `no`, `y`, `n`, `true`, `false`, `null` and `~`. A symbol drawn from that set therefore arrives as a value of another type, and its declaration disappears. Two repairs exist: a quoted symbol keeps its type as a string, and a different identifier avoids the collision. ^quote-serializer-keywords

- **A name, a symbol and a prose field answer different questions.** The name designates the entry in words. The symbol identifies the entry in formulas and references. The prose, under the key that names its function, carries the content that name and symbol leave unstated. Each content therefore stays in its own field. A symbol repeated inside a name or a prose field creates a second identifier that no reference resolves. Likewise, a formula written there belongs in the `expression` field: `Re := U L / nu` is the expression of `Re`. ^name-symbol-prose

- **The extent of a set names its *members*, not the values that they carry.** A constituent kind collects labelled units, so its extent is the set of labels: `range(S)` for `S` populations, `enum("A", "B")` for two named species. The `card` operator returns the cardinality of that set, and a bound on that number belongs among the *constraints*. Because an extent names members, an extent written `pos(ints)` states that the units are all the positive integers. ^extent-identifies-members

- **A value set and an extent are *expressions*.** The field `values` names the set of values that a quantity can take. The field `extent` names the set that a constituent kind or an index set collects. Both sets are written with the set constructors. Neither set repeats a restriction that the laws already impose: a velocity field takes values in `maps(x, pow(reals, 3))`, and the condition that its divergence vanishes is a law. A set that the case leaves unfixed is *named by a parameter*: `U(sp)`, for instance, refers to an admitted local state space that the record declares. ^value-sets-are-expressions

- **Every expression uses one field name, and its position fixes its function.** An expression inside a quantity introduces its enclosing entry, so it cannot be false of the system. An expression inside a law or a manifestation makes a claim about the system and can therefore be false. The two share one field name, and hence one syntax, because the enclosing block already separates their functions. ^expression-position

- **A notation gives the LaTeX form of a symbol or an operator, and a renderer composes the rest.** A symbol carries its LaTeX form unless it prints as its own identifier. That form is written in single quotes: inside double quotation marks, the serializer reads `\n` in `\nu` as a newline and corrupts the form. An operator carries a template, with `#0` for the indices that a binder consumes and `#1`, `#2` for its arguments. For instance, the template of `mean` is `\langle #1 \rangle_{#0}`, and that of `maps` is `#1 \to #2`. The renderer derives the LaTeX from the source that the checks read, and no second copy is written. ^notation-renders-in-latex

- **Prose interprets, and never reformulates the name.** For example, `d_t(N) = 0` states that the abundances are at a fixed point. When the reading is absent, the fixed point must be reconstructed from the syntax. The reading therefore states the content that the expression encodes and the reason for its written form. A prose field that repeats the content words of the name is a defect, because it adds no information to the name. A defective record, for instance, pairs the prose "the chance that a subsystem transitions at or before the horizon" with the name "probability that a subsystem transitions by the horizon". Prose also never states a fact that a typed field can hold, since two records of one commitment can come to disagree. ^prose-interprets

- **A quantity that a condition fixes carries a presupposition of existence.** An `expression` builds the quantity from others, so it cannot be false of the system. A `condition`, by contrast, states the relation that the quantity satisfies (e.g. `d_t(N) = 0` for an equilibrium). The condition thereby introduces the quantity and presupposes that a satisfying value exists. The record carries one of the two, never both. When several values meet the condition, `selects` fixes the reading. With `unique`, the record presupposes exactly one satisfying value. With `any`, the claim holds of every such value, and with `all`, the quantity becomes the set of those values. ^condition-presupposes-existence

- **The free indices of an expression form the signature.** A binder consumes the indices that it names, and the defined quantity keeps the free indices. `min_{i}( N(i) )` binds `i` and leaves nothing free, so the minimum abundance is a scalar and its signature is empty. `mean_{x, t}( u(a, x, t) * u(b, x + r, t + tau) )` binds `x` and `t` and leaves `a`, `b`, `r` and `tau` free, so those four form the signature. The Fourier transform `ft` does both: it consumes the indices that it binds and introduces their conjugates into the signature.

- **A binder consumes several indices at once.** `mean_{x, t}` averages jointly over position and time. A binder is needed for that joint average, because no field that holds one index and one retention token expresses a joint average. The aggregator also names the map applied to the consumed indices, so that a minimum and a mean over one index remain distinct quantities. ^binder-consumes-several

- **Grain is fixed by the signature and the definition, so no field records it separately.** A binder consumed every index absent from the signature, and its aggregator fixes how the values were combined. For a quantity with no definition, the signature alone fixes the grain: each retained index is kept apart, and each omitted index was never taken.

- **An index set is declared only when no constituent kind, and no parameter of one, supplies the set.** For example, units carrying positions on a lattice need no index set, because the units are the constituents and each coordinate is a parameter defined over a unit. A quantity said to vary "by position" therefore takes the unit as its index. A continuum field, by contrast, has no units, so position is the index and the constituents are empty. A field over a lattice may be modelled either way, and the record states which way it chose. ^index-set-admission

- **The canonical operators follow from the semantics of the framework.** The set has one source, the [registry declaring every canonical operator](../../src/gnomon/data/operators.yml), and falls into the following groups. Binders realize the signature rule and the limits that the domain may take: `mean`, `sum`, `min`, `max`, `dist`, `limit`, `norm`. Relations realize the forms that a manifestation may take and the distributional law that a record may state: `implies`, `depends_on`, `increasing`, `decreasing`, `drawn_from`. The transform `ft` is also a binder, because it consumes the indices that it binds. Set constructors build value sets and extents, name the most frequent shapes, and relate two sets. The set constructors are `reals`, `ints`, `bools`, `complex`, `pos`, `nonneg`, `vectors`, `matrices`, `prod`, `enum`, `range`, `interval`, `maps`, `measures`, `card`, `subset`, `intersect`, `union`, `empty`. Every problem may use two maps: `diff`, the derivative of a quantity along one of its indices, and `abs`, the magnitude of its argument. The same holds for the operations of general mathematics that no problem owns: `dot`, `adjoint`, `re`, `spectrum`, `jacobian`, `grad`, `div`, `lap`. One constant is admitted: `infinity`, the value to which a limit of the domain runs. ^operator-groups

- **One operator vocabulary serves one problem.** Every record of a problem reads the same operator file. A phenomenon, its target and its questions therefore draw on one set, and no record redeclares an operator that a sibling declares. An operator is typed over sets that any record of the problem may declare. The operator file is therefore read against the *whole problem*. ^one-operator-file

- **A problem declares the mathematics that it adds.** Each problem lists in its `operators.yml` the operators that its records use beyond the canonical set. These local operators resolve only within that problem. The restriction of a field to a region, or the Jacobian of a community at equilibrium, belongs to the *problem* that uses it. The canonical set therefore holds only the operators that every inquiry can assume. ^local-operators

## Operator record

One file per problem holds the operators that its records declare, filled from `src/gnomon/data/templates/operators.yml`. The file names the target system of the problem, so a reader reaches the sets over which the operators are typed.

| Specification | When it is required | Form | Examples |
| ------------- | ------------------- | ---- | -------- |
| Operators | when a formula of any record of the problem uses an operator beyond the canonical set | one entry per operator | the restriction of a field to a region; the Jacobian of a community at equilibrium; the empirical neural tangent kernel |
| Operators: name | with every operator | the result that the operator computes, in words and with no symbol or formula | "the restriction of a field to a region" |
| Operators: symbol | with every operator | an identifier, unique across the problem and distinct from every declared quantity | `restrict`, `community_jacobian`, `ntk` |
| Operators: notation | when the operator prints as more than its symbol | a LaTeX template in single quotes, `#0` for the indices that a binder consumes and `#1`, `#2` for its arguments | `'\nabla \cdot #1'`; `'\operatorname{spec}( #1 )'` |
| Operators: for any (type variables of the operator) | when the operator is general over the sets on which it acts | the type variables that its signature and values may name, so that a general operator is typed once for all its call sites | `[S]` for an adjoint, typed `maps(S, S)` to `maps(S, S)`; `[S, n]` for an inner product of two vectors |
| Operators: signature | with every operator | the set expression of each argument, in order | `["maps(Om, pow(reals, 3))"]` |
| Operators: values | with every operator | the set expression in which its result lies | `"maps(Om, reals)"`; `reals` |

- **Each problem gathers its symbols in one table of its own.** A problem fills several records that reference one another, so its author consults one table generated from the whole set. No table spans a corpus, because the scoping rule lets one letter denote a different quantity in each problem. ^one-table-per-problem

- **Identifiers resolve lexically, so a signature is declared rather than derived.** Each identifier in a formula must resolve to a declared symbol, and a reference must point to exactly one entry. A signature, by contrast, is computed from its definition only by a parser that reads the binders. Until such a parser exists, a record can declare a signature that its own definition contradicts. ^resolution-is-lexical
