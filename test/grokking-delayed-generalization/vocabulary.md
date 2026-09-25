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
| `delay` | phen.grokking.delayed_generalization | explanandum variables | — | duration of the delay |
| `tfit` | phen.grokking.delayed_generalization | explanandum variables | — | first crossing time of the training criterion |
| `tgen` | phen.grokking.delayed_generalization | explanandum variables | — | first crossing time of the generalization criterion |
| `crossing_order` | phen.grokking.delayed_generalization | manifestations | — | order of the two crossing times |
| `positive_delay` | phen.grokking.delayed_generalization | manifestations | — | strictly positive delay |
| `delay_obs` | phen.grokking.delayed_generalization | manifestations.features | — | observed duration of the delay |
| `init` | phen.grokking.delayed_generalization | scope over instances | — | initialization draw |
| `spec` | phen.grokking.delayed_generalization | scope over instances | — | training specification |
| `coord` | system.delayed_generalization_networks | constituents | — | coordinate of the trainable parameters |
| `unit` | system.delayed_generalization_networks | constituents | — | computational unit |
| `source` | system.delayed_generalization_networks | external systems | — | process that generates the task data |
| `step` | system.delayed_generalization_networks | index sets | — | training step |
| `test` | system.delayed_generalization_networks | index sets | — | held-out sample |
| `train` | system.delayed_generalization_networks | index sets | — | training sample |
| `forward` | system.delayed_generalization_networks | laws | — | forward computation |
| `init_draw` | system.delayed_generalization_networks | laws | — | initialization draw |
| `initial_optimizer_state` | system.delayed_generalization_networks | laws | — | initial state of the optimizer |
| `initial_state` | system.delayed_generalization_networks | laws | coord | initial state of the parameters |
| `update` | system.delayed_generalization_networks | laws | coord | gradient-based update |
| `update_state` | system.delayed_generalization_networks | laws | — | update of the optimizer state |
| `Arch` | system.delayed_generalization_networks | parameters | — | specification of the architecture: a finite computation graph with activation functions and a task readout |
| `Nu` | system.delayed_generalization_networks | parameters | — | number of computational units |
| `P` | system.delayed_generalization_networks | parameters | — | number of coordinates of the trainable parameters |
| `T` | system.delayed_generalization_networks | parameters | — | observation horizon in training steps |
| `algorithmic` | system.delayed_generalization_networks | parameters | — | predicate selecting the admitted algorithmic supervised tasks |
| `data` | system.delayed_generalization_networks | parameters | — | space of labeled examples for the supervised task |
| `ell` | system.delayed_generalization_networks | parameters | — | task loss |
| `eps_fit` | system.delayed_generalization_networks | parameters | — | near-zero threshold on the training loss |
| `eps_gen` | system.delayed_generalization_networks | parameters | — | generalization threshold on the test loss |
| `opt` | system.delayed_generalization_networks | parameters | — | specification of the gradient-based optimizer with its hyperparameters |
| `opt_state` | system.delayed_generalization_networks | parameters | — | update rule for the auxiliary state of the optimizer |
| `p0` | system.delayed_generalization_networks | parameters | — | initialization distribution |
| `proto` | system.delayed_generalization_networks | parameters | — | evaluation protocol fixing when the losses are read and how a crossing time is classified before the horizon |
| `test_set` | system.delayed_generalization_networks | parameters | — | realized held-out set |
| `theta0` | system.delayed_generalization_networks | parameters | coord | initial parameter vector |
| `train_set` | system.delayed_generalization_networks | parameters | — | realized training set |
| `z0` | system.delayed_generalization_networks | parameters | — | initial auxiliary state of the optimizer |
| `Ltest` | system.delayed_generalization_networks | referenced | — |  |
| `Ltrain` | system.delayed_generalization_networks | referenced | — |  |
| `Ltest` | system.delayed_generalization_networks | variables | step | test loss |
| `Ltrain` | system.delayed_generalization_networks | variables | step | training loss |
| `pred` | system.delayed_generalization_networks | variables | step | prediction of the network, in the prediction space of the task readout |
| `theta` | system.delayed_generalization_networks | variables | coord, step | coordinate of the network parameters |
| `z` | system.delayed_generalization_networks | variables | step | auxiliary state of the optimizer, of the finite dimension that the selected optimizer fixes |

## Directed interactions

The nodes are kinds, not identified members: which tuples are joined is fixed by a parameter of a member model, and the last column says where to read it from. A tuple of three or more carries a joint influence, which no pair of endpoints could state.

| Sources | Edge | Reach | Through | Ordered tuples |
| --- | --- | --- | --- | --- |
| — | `two_timescale_training` | `None` | — | `None` |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `effective_loss` (the effective loss on a learned representation), `powerset` (the set of all subsets of a declared set), `representation` (the learned representation extracted from a parameter trajectory), `representation_quality` (the fraction of the relations consistent with the task that are realized by a learned representation).
