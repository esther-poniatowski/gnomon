---
tags:
  - generated
index: "[microbial-stable-coexistence](test/microbial-stable-coexistence/_index.md)"
---
# Vocabulary of microbial-stable-coexistence

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `abundance_nonneg` | bg.microbial-formal-population-models.population-dynamics | laws | — | invariance of the nonnegative state space |
| `consume` | bg.microbial-formal-population-models.population-dynamics | laws | res, pop | resource consumption |
| `grow_direct` | bg.microbial-formal-population-models.population-dynamics | laws | pop | evolution of the populations under direct interaction |
| `grow_resource` | bg.microbial-formal-population-models.population-dynamics | laws | pop | evolution of the populations under competition for resources |
| `higher_order` | bg.microbial-formal-population-models.population-dynamics | laws | pop, pop, pop | higher-order influence |
| `mediate` | bg.microbial-formal-population-models.population-dynamics | laws | pop, res | growth mediated by resources |
| `mortality_direct` | bg.microbial-formal-population-models.population-dynamics | laws | pop | mortality in the growth law with direct interactions |
| `mortality_resource` | bg.microbial-formal-population-models.population-dynamics | laws | pop | mortality in the growth law with explicit resources |
| `pairwise` | bg.microbial-formal-population-models.population-dynamics | laws | pop, pop | direct pairwise influence |
| `pools_nonneg` | bg.microbial-formal-population-models.population-dynamics | laws | res | invariance of nonnegative resources |
| `produce` | bg.microbial-formal-population-models.population-dynamics | laws | res, pop | resource production |
| `size_bound` | bg.microbial-formal-population-models.population-dynamics | laws | — | community size |
| `turnover` | bg.microbial-formal-population-models.population-dynamics | laws | res | evolution of the resources |
| `drawdown` | bg.microbial-formal-population-models.population-dynamics | organization | — | resource drawdown |
| `feeding` | bg.microbial-formal-population-models.population-dynamics | organization | — | cross-feeding |
| `mediation` | bg.microbial-formal-population-models.population-dynamics | organization | — | coupling mediated by resources |
| `pairing` | bg.microbial-formal-population-models.population-dynamics | organization | — | direct pairwise coupling |
| `triplet` | bg.microbial-formal-population-models.population-dynamics | organization | — | higher-order coupling |
| `J` | phen.microbial.stable-coexistence | explanandum variables | — | Jacobian of the community at the equilibrium |
| `Nstar` | phen.microbial.stable-coexistence | explanandum variables | pop | abundance of each population at equilibrium |
| `Xstar` | phen.microbial.stable-coexistence | explanandum variables | — | complete equilibrium state |
| `alpha` | phen.microbial.stable-coexistence | explanandum variables | — | spectral abscissa at the equilibrium |
| `mN` | phen.microbial.stable-coexistence | explanandum variables | — | minimum population abundance at equilibrium |
| `feasible` | phen.microbial.stable-coexistence | manifestations | — | feasible coexistence equilibrium |
| `stable` | phen.microbial.stable-coexistence | manifestations | — | local asymptotic stability of the coexistence equilibrium |
| `member` | phen.microbial.stable-coexistence | scope over instances | — | member models of the admitted class |
| `supply` | phen.microbial.stable-coexistence | scope over instances | — | admitted nonnegative vectors of resource supply |
| `pop` | system.microbial-formal-population-models | constituents | — | microbial population |
| `res` | system.microbial-formal-population-models | constituents | — | abiotic resource pool |
| `supply` | system.microbial-formal-population-models | external systems | — | formal environment that supplies the resources |
| `t` | system.microbial-formal-population-models | index sets | — | time |
| `A` | system.microbial-formal-population-models | parameters | pop, pop | coefficient of pairwise interaction |
| `B` | system.microbial-formal-population-models | parameters | pop, pop, pop | coefficient of higher-order interaction |
| `C` | system.microbial-formal-population-models | parameters | res, pop | coefficient of resource consumption |
| `Fd` | system.microbial-formal-population-models | parameters | pop | per-capita growth law with direct interactions |
| `Fr` | system.microbial-formal-population-models | parameters | pop | per-capita growth law with explicit resources |
| `G` | system.microbial-formal-population-models | parameters | res | law of resource turnover |
| `M` | system.microbial-formal-population-models | parameters | — | number of abiotic resource pools |
| `Pr` | system.microbial-formal-population-models | parameters | res, pop | coefficient of resource production |
| `S` | system.microbial-formal-population-models | parameters | — | number of microbial populations |
| `mu` | system.microbial-formal-population-models | parameters | pop | mortality rate of each consumer |
| `rho` | system.microbial-formal-population-models | parameters | res | rate of resource supply |
| `theta` | system.microbial-formal-population-models | parameters | — | specification of the interaction laws: the admissible functional forms and coefficients of one member model |
| `N` | system.microbial-formal-population-models | variables | pop, t | abundance of each microbial population |
| `R` | system.microbial-formal-population-models | variables | res, t | resource concentration |
| `direct` | system.microbial-formal-population-models | variants | — | community with direct interactions |
| `resource_explicit` | system.microbial-formal-population-models | variants | — | community with explicit resources |

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
- Declared by this problem: `community_jacobian` (the Jacobian of the complete dynamics of the member model at a selected equilibrium), `equilibrium` (the predicate that a complete member state belongs to an equilibrium of the dynamics of the member model), `population_component` (the component of a complete member state that holds the population abundances).
