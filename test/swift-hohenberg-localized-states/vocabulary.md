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
| `stability` | phen.swift-hohenberg.localized-states | manifestations.features | — | intervals of linear stability along the branches |
| `symmetry` | phen.swift-hohenberg.localized-states | manifestations.features | — | symmetry classes of the profiles |
| `topology` | phen.swift-hohenberg.localized-states | manifestations.features | — | topology of the solution branches |
| `t` | system.swift-hohenberg-localized-states | index sets | — | time |
| `x` | system.swift-hohenberg-localized-states | index sets | — | spatial position |
| `evolve` | system.swift-hohenberg-localized-states | laws | x | Swift-Hohenberg evolution with quadratic and cubic nonlinearities |
| `localized` | system.swift-hohenberg-localized-states | laws | — | localized boundary condition in the far field |
| `b` | system.swift-hohenberg-localized-states | parameters | — | coefficient of the quadratic nonlinearity |
| `r` | system.swift-hohenberg-localized-states | parameters | — | control coefficient of the linear term |
| `u` | system.swift-hohenberg-localized-states | variables | x, t | amplitude field of the pattern |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `far_field` (the common value approached by a scalar field at both spatial infinities), `powerset` (the set of all subsets of a declared set).
