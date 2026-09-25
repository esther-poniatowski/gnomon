---
tags:
  - generated
index: "[earth-system-tipping-cascades](test/earth-system-tipping-cascades/_index.md)"
---
# Vocabulary of earth-system-tipping-cascades

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `Fi` | phen.earth-tipping-subsystems.transition-sequences | explanandum variables | sub, H | censored distribution of the transition time |
| `PZ` | phen.earth-tipping-subsystems.transition-sequences | explanandum variables | H | joint law of the marked sequence of transitions |
| `Tev` | phen.earth-tipping-subsystems.transition-sequences | explanandum variables | sub | transition time of a subsystem |
| `Z` | phen.earth-tipping-subsystems.transition-sequences | explanandum variables | — | marked sequence of transitions |
| `pi` | phen.earth-tipping-subsystems.transition-sequences | explanandum variables | sub, H | probability that a subsystem transitions by the horizon |
| `H` | phen.earth-tipping-subsystems.transition-sequences | index sets | — | prediction horizon |
| `overshoot_dependence` | phen.earth-tipping-subsystems.transition-sequences | manifestations | — | dependence of the transition sequence on the warming trajectory |
| `overshoot_effect` | phen.earth-tipping-subsystems.transition-sequences | manifestations.features | — | effect of an overshoot trajectory on the sequence law |
| `param` | phen.earth-tipping-subsystems.transition-sequences | scope over instances | — | admissible dynamical parameters of each subsystem |
| `realization` | phen.earth-tipping-subsystems.transition-sequences | scope over instances | — | internal climate variability |
| `scenario` | phen.earth-tipping-subsystems.transition-sequences | scope over instances | — | prescribed emission scenario |
| `struct` | phen.earth-tipping-subsystems.transition-sequences | scope over instances | — | admissible interaction architectures among subsystems |
| `sub` | system.earth-tipping-subsystems | constituents | — | climate subsystem |
| `observation` | system.earth-tipping-subsystems | external systems | — | systems of Earth observation and paleoclimate measurement |
| `scenario_source` | system.earth-tipping-subsystems | external systems | — | specification of the forcing scenario and Earth-system processes outside the selected subsystems |
| `t` | system.earth-tipping-subsystems | index sets | — | time |
| `detect_law` | system.earth-tipping-subsystems | laws | sub | detection of regimes and events |
| `evolve` | system.earth-tipping-subsystems | laws | sub | evolution of a subsystem |
| `transmit` | system.earth-tipping-subsystems | laws | sub, sub, t | directed interaction between subsystems |
| `coupling` | system.earth-tipping-subsystems | organization | — | directed coupling between subsystems |
| `Aij` | system.earth-tipping-subsystems | parameters | sub, sub | directed architecture of the interactions |
| `Tend` | system.earth-tipping-subsystems | parameters | — | end of the prescribed scenario |
| `Theta` | system.earth-tipping-subsystems | parameters | sub | critical threshold of the forcing |
| `baseline` | system.earth-tipping-subsystems | parameters | sub | baseline regime of a subsystem |
| `conv` | system.earth-tipping-subsystems | parameters | — | convergence level of the prescribed warming |
| `detect` | system.earth-tipping-subsystems | parameters | sub | rule detecting regimes and events |
| `emit` | system.earth-tipping-subsystems | parameters | sub, sub | emission law of a transmitted signal |
| `intern` | system.earth-tipping-subsystems | parameters | sub | law of the internal feedback of a subsystem |
| `peak` | system.earth-tipping-subsystems | parameters | — | peak of the prescribed warming |
| `s` | system.earth-tipping-subsystems | parameters | sub, sub | law of the response along a directed interaction |
| `tau` | system.earth-tipping-subsystems | parameters | sub | intrinsic timescale of the transition |
| `DGMT` | system.earth-tipping-subsystems | variables | t | prescribed trajectory of global mean surface temperature |
| `eta` | system.earth-tipping-subsystems | variables | sub, t | internal climate variability left unresolved |
| `ind` | system.earth-tipping-subsystems | variables | sub, t | physical indicators of the state of a subsystem |
| `r` | system.earth-tipping-subsystems | variables | sub, t | qualitative regime of a subsystem |
| `rate` | system.earth-tipping-subsystems | variables | t | rate of prescribed warming |
| `u` | system.earth-tipping-subsystems | variables | sub, sub, t | physical signal transmitted from one subsystem to another: the climatic flux or field specific to that ordered pair |
| `z` | system.earth-tipping-subsystems | variables | sub, t | physical state of a subsystem, in its empirically admissible state space |

## Directed interactions

The nodes are kinds, not identified members: which tuples are joined is fixed by a parameter of a member model, and the last column says where to read it from. A tuple of three or more carries a joint influence, which no pair of endpoints could state.

| Sources | Edge | Reach | Through | Ordered tuples |
| --- | --- | --- | --- | --- |
| `sub` | `model_coupling` | `sub` | — | `subset(prod(sub, sub), Aij)` |
| `sub` | `coupling` | `sub` | `Aij`, `emit`, `s`, `u` | `subset(prod(sub, sub), Aij)` |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `sequence` (the ordered sequence of identities paired with their event times).
