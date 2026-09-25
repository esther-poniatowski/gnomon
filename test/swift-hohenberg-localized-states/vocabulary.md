---
tags:
  - generated
index: "[swift-hohenberg-localized-states](test/swift-hohenberg-localized-states/_index.md)"
---
# Vocabulary of swift-hohenberg-localized-states

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `Uloc` | phen.swift-hohenberg.localized-states | explanandum variables | r, b | set of localized stationary profiles |
| `localized_states_exist` | phen.swift-hohenberg.localized-states | manifestations | — | existence of localized stationary states |
| `stability` | phen.swift-hohenberg.localized-states | manifestations.features | — | linear-stability intervals along the branches |
| `symmetry` | phen.swift-hohenberg.localized-states | manifestations.features | — | profile symmetry classes |
| `topology` | phen.swift-hohenberg.localized-states | manifestations.features | — | solution-branch topology |
| `t` | system.swift-hohenberg-localized-states | index sets | — | time |
| `x` | system.swift-hohenberg-localized-states | index sets | — | spatial position |
| `evolve` | system.swift-hohenberg-localized-states | laws | x | quadratic-cubic Swift-Hohenberg evolution |
| `localized` | system.swift-hohenberg-localized-states | laws | — | localized far-field boundary condition |
| `b` | system.swift-hohenberg-localized-states | parameters | — | quadratic nonlinear coefficient |
| `r` | system.swift-hohenberg-localized-states | parameters | — | linear control coefficient |
| `u` | system.swift-hohenberg-localized-states | variables | x, t | pattern-amplitude field |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `far_field` (the common value approached by a scalar field at both spatial infinities), `powerset` (the set of all subsets of a declared set).
