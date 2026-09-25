---
tags:
  - generated
index: "[grokking-delayed-generalization](test/grokking-delayed-generalization/_index.md)"
---
# Vocabulary of grokking-delayed-generalization

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `Pdelay` | phen.grokking.delayed_generalization | explanandum variables | — | distribution of the delay across initialization draws |
| `delay` | phen.grokking.delayed_generalization | explanandum variables | — | delay duration |
| `tfit` | phen.grokking.delayed_generalization | explanandum variables | — | first crossing time of the training criterion |
| `tgen` | phen.grokking.delayed_generalization | explanandum variables | — | first crossing time of the generalization criterion |
| `crossing_order` | phen.grokking.delayed_generalization | manifestations | — | order of the two crossing times |
| `positive_delay` | phen.grokking.delayed_generalization | manifestations | — | strictly positive delay |
| `delay_obs` | phen.grokking.delayed_generalization | manifestations.features | — | observed delay duration |
| `init` | phen.grokking.delayed_generalization | scope over instances | — | initialization draw |
| `spec` | phen.grokking.delayed_generalization | scope over instances | — | training specification |
| `coord` | system.delayed_generalization_networks | constituents | — | trainable parameter coordinate |
| `unit` | system.delayed_generalization_networks | constituents | — | computational unit |
| `source` | system.delayed_generalization_networks | external systems | — | task data-generating process |
| `step` | system.delayed_generalization_networks | index sets | — | training step |
| `test` | system.delayed_generalization_networks | index sets | — | held-out sample |
| `train` | system.delayed_generalization_networks | index sets | — | training sample |
| `forward` | system.delayed_generalization_networks | laws | — | forward computation |
| `init_draw` | system.delayed_generalization_networks | laws | — | initialization draw |
| `initial_optimizer_state` | system.delayed_generalization_networks | laws | — | initial optimizer state |
| `initial_state` | system.delayed_generalization_networks | laws | coord | initial parameter state |
| `update` | system.delayed_generalization_networks | laws | coord | gradient-based update |
| `update_state` | system.delayed_generalization_networks | laws | — | optimizer-state update |
| `Arch` | system.delayed_generalization_networks | parameters | — | architecture specification: a finite computation graph with activation functions and a task readout |
| `Nu` | system.delayed_generalization_networks | parameters | — | number of computational units |
| `P` | system.delayed_generalization_networks | parameters | — | number of trainable parameter coordinates |
| `T` | system.delayed_generalization_networks | parameters | — | observation horizon in training steps |
| `algorithmic` | system.delayed_generalization_networks | parameters | — | predicate selecting the admitted algorithmic supervised tasks |
| `data` | system.delayed_generalization_networks | parameters | — | space of labeled examples for the supervised task |
| `ell` | system.delayed_generalization_networks | parameters | — | task loss |
| `eps_fit` | system.delayed_generalization_networks | parameters | — | near-zero training-loss threshold |
| `eps_gen` | system.delayed_generalization_networks | parameters | — | generalization threshold on the test loss |
| `opt` | system.delayed_generalization_networks | parameters | — | gradient-based optimizer specification with its hyperparameters |
| `opt_state` | system.delayed_generalization_networks | parameters | — | optimizer auxiliary-state update rule |
| `p0` | system.delayed_generalization_networks | parameters | — | initialization distribution |
| `proto` | system.delayed_generalization_networks | parameters | — | evaluation protocol fixing when the losses are read and how a crossing time is classified before the horizon |
| `test_set` | system.delayed_generalization_networks | parameters | — | realized held-out set |
| `theta0` | system.delayed_generalization_networks | parameters | coord | initial parameter vector |
| `train_set` | system.delayed_generalization_networks | parameters | — | realized training set |
| `z0` | system.delayed_generalization_networks | parameters | — | initial optimizer auxiliary state |
| `Ltest` | system.delayed_generalization_networks | referenced | — |  |
| `Ltrain` | system.delayed_generalization_networks | referenced | — |  |
| `Ltest` | system.delayed_generalization_networks | variables | step | test loss |
| `Ltrain` | system.delayed_generalization_networks | variables | step | training loss |
| `pred` | system.delayed_generalization_networks | variables | step | network prediction, in the prediction space of the task readout |
| `theta` | system.delayed_generalization_networks | variables | coord, step | network parameter coordinate |
| `z` | system.delayed_generalization_networks | variables | step | optimizer auxiliary state, of the finite dimension the selected optimizer fixes |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `powerset` (the set of all subsets of a declared set).
