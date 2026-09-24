---
tags:
  - generated
index: "[microbial-stable-coexistence](_index.md)"
---
# Vocabulary of microbial-stable-coexistence

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `J` | phen.microbial.stable-coexistence | explanandum variables | — | community Jacobian at the equilibrium |
| `Nstar` | phen.microbial.stable-coexistence | explanandum variables | pop | equilibrium population abundance |
| `Xstar` | phen.microbial.stable-coexistence | explanandum variables | — | complete equilibrium state |
| `alpha` | phen.microbial.stable-coexistence | explanandum variables | — | equilibrium spectral abscissa |
| `mN` | phen.microbial.stable-coexistence | explanandum variables | — | minimum equilibrium population abundance |
| `feasible` | phen.microbial.stable-coexistence | manifestations | — | feasible coexistence equilibrium |
| `stable` | phen.microbial.stable-coexistence | manifestations | — | local asymptotic stability of the coexistence equilibrium |
| `member` | phen.microbial.stable-coexistence | scope over instances | — | member models of the admitted class |
| `supply` | phen.microbial.stable-coexistence | scope over instances | — | admitted nonnegative resource-supply vectors |
| `pop` | system.microbial-formal-population-models | constituents | — | microbial population |
| `res` | system.microbial-formal-population-models | constituents | — | abiotic resource pool |
| `supply` | system.microbial-formal-population-models | external systems | — | formal resource-supply environment |
| `t` | system.microbial-formal-population-models | index sets | — | time |
| `abundance_nonneg` | system.microbial-formal-population-models | laws | — | nonnegative state-space invariance |
| `consume` | system.microbial-formal-population-models | laws | res, pop | resource consumption |
| `grow_direct` | system.microbial-formal-population-models | laws | pop | population evolution under direct interaction |
| `grow_resource` | system.microbial-formal-population-models | laws | pop | population evolution under resource competition |
| `higher_order` | system.microbial-formal-population-models | laws | pop, pop, pop | higher-order influence |
| `mediate` | system.microbial-formal-population-models | laws | pop, res | resource-mediated growth |
| `mortality_direct` | system.microbial-formal-population-models | laws | pop | mortality dependence of direct growth |
| `mortality_resource` | system.microbial-formal-population-models | laws | pop | mortality dependence of resource-mediated growth |
| `pairwise` | system.microbial-formal-population-models | laws | pop, pop | direct pairwise influence |
| `pools_nonneg` | system.microbial-formal-population-models | laws | res | nonnegative resource invariance |
| `produce` | system.microbial-formal-population-models | laws | res, pop | resource production |
| `size_bound` | system.microbial-formal-population-models | laws | — | community size |
| `turnover` | system.microbial-formal-population-models | laws | res | resource evolution |
| `drawdown` | system.microbial-formal-population-models | organization | — | resource drawdown |
| `feeding` | system.microbial-formal-population-models | organization | — | cross-feeding |
| `mediation` | system.microbial-formal-population-models | organization | — | resource-mediated coupling |
| `pairing` | system.microbial-formal-population-models | organization | — | direct pairwise coupling |
| `triplet` | system.microbial-formal-population-models | organization | — | higher-order coupling |
| `A` | system.microbial-formal-population-models | parameters | pop, pop | pairwise interaction coefficient |
| `B` | system.microbial-formal-population-models | parameters | pop, pop, pop | higher-order interaction coefficient |
| `C` | system.microbial-formal-population-models | parameters | res, pop | resource-consumption coefficient |
| `Fd` | system.microbial-formal-population-models | parameters | pop | per-capita population growth law of a direct-interaction member |
| `Fr` | system.microbial-formal-population-models | parameters | pop | per-capita population growth law of a resource-explicit member |
| `G` | system.microbial-formal-population-models | parameters | res | resource-turnover law |
| `M` | system.microbial-formal-population-models | parameters | — | number of abiotic resource pools |
| `Pr` | system.microbial-formal-population-models | parameters | res, pop | resource-production coefficient |
| `S` | system.microbial-formal-population-models | parameters | — | number of microbial populations |
| `mu` | system.microbial-formal-population-models | parameters | pop | consumer mortality rate |
| `rho` | system.microbial-formal-population-models | parameters | res | resource-supply rate |
| `theta` | system.microbial-formal-population-models | parameters | — | interaction-law specification: the admissible functional forms and coefficients of one member model |
| `N` | system.microbial-formal-population-models | variables | pop, t | microbial-population abundance |
| `R` | system.microbial-formal-population-models | variables | res, t | resource concentration |
| `direct` | system.microbial-formal-population-models | variants | — | direct-interaction community |
| `resource_explicit` | system.microbial-formal-population-models | variants | — | resource-explicit community |

## Symbols reused across records

- `supply` denotes a distinct quantity in phen.microbial.stable-coexistence, system.microbial-formal-population-models.

## Directed interactions

The nodes are kinds, not identified members: which tuples are joined is fixed by a parameter of a member model, and the last column says where to read it from. A tuple of three or more carries a joint influence, which no pair of endpoints could state.

| Sources | Edge | Reach | Through | Ordered tuples |
| --- | --- | --- | --- | --- |
| `pop` | `pairing` | `pop` | `A` | `prod(pop, pop)` |
| `pop` · `pop` | `triplet` | `pop` | `B` | `prod(pop, pop, pop)` |
| `pop` | `drawdown` | `res` | `C` | `prod(pop, res)` |
| `pop` | `feeding` | `res` | `Pr` | `prod(pop, res)` |
| `res` | `mediation` | `pop` | `C` | `prod(res, pop)` |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `community_jacobian` (the Jacobian of the complete member-model dynamics at a selected equilibrium), `equilibrium` (the predicate that a complete member state belongs to an equilibrium of the member-model dynamics), `population_component` (the population-abundance component of a complete member state).
