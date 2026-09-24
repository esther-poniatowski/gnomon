---
tags:
  - generated
index: "[neural-tangent-kernel-model-knowledge](_index.md)"
---
# Vocabulary of neural-tangent-kernel-model-knowledge

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `Edrift` | phen.ntk.linearized-dynamics | explanandum variables | m, t | drift of the empirical kernel |
| `Elimit` | phen.ntk.linearized-dynamics | explanandum variables | m | discrepancy from the limiting kernel at initialization |
| `Eout` | phen.ntk.linearized-dynamics | explanandum variables | m, t | discrepancy between output trajectories |
| `kernel_drift_vanishes` | phen.ntk.linearized-dynamics | manifestations | — | vanishing drift of the empirical kernel |
| `limit_error_vanishes` | phen.ntk.linearized-dynamics | manifestations | — | vanishing distance to the limiting kernel |
| `output_converges` | phen.ntk.linearized-dynamics | manifestations | — | convergence of the network output to the linearized output |
| `Bdrift` | phen.ntk.linearized-dynamics | manifestations.features | — | finite-width bound on the drift of the empirical kernel |
| `Binit` | phen.ntk.linearized-dynamics | manifestations.features | — | finite-width bound on the discrepancy from the limiting kernel |
| `Bout` | phen.ntk.linearized-dynamics | manifestations.features | — | finite-width bound on output discrepancy |
| `Tdrift` | phen.ntk.linearized-dynamics | manifestations.features | — | training horizon for the bound on kernel drift |
| `Tout` | phen.ntk.linearized-dynamics | manifestations.features | — | training horizon for the output bound |
| `mode_drift` | phen.ntk.linearized-dynamics | manifestations.features | — | mode of convergence of the kernel-drift bound over initialization draws |
| `mode_init` | phen.ntk.linearized-dynamics | manifestations.features | — | mode of convergence of the initial kernel over initialization draws |
| `mode_out` | phen.ntk.linearized-dynamics | manifestations.features | — | mode of convergence of the output bound over initialization draws |
| `init_draw` | phen.ntk.linearized-dynamics | scope over instances | — | initialization draw |
| `spec` | phen.ntk.linearized-dynamics | scope over instances | — | width-indexed network and training specification |
| `a` | system.ntk-gradient-flow | index sets | — | index of training examples |
| `t` | system.ntk-gradient-flow | index sets | — | training time |
| `flow` | system.ntk-gradient-flow | laws | t | parameter gradient flow |
| `init_draw` | system.ntk-gradient-flow | laws | — | initialization draw |
| `init_state` | system.ntk-gradient-flow | laws | — | parameter initialization |
| `shared_init` | system.ntk-gradient-flow | laws | a | shared initial outputs |
| `K0` | system.ntk-gradient-flow | parameters | a, a | empirical neural tangent kernel at initialization |
| `Kinf` | system.ntk-gradient-flow | parameters | a, a | deterministic infinite-width neural tangent kernel |
| `L` | system.ntk-gradient-flow | parameters | — | number of hidden layers |
| `X` | system.ntk-gradient-flow | parameters | a | training inputs |
| `d` | system.ntk-gradient-flow | parameters | — | dimension of each training input |
| `eta` | system.ntk-gradient-flow | parameters | — | rate of gradient flow |
| `m` | system.ntk-gradient-flow | parameters | — | width of each hidden layer |
| `n` | system.ntk-gradient-flow | parameters | — | number of training examples |
| `p` | system.ntk-gradient-flow | parameters | — | number of trainable parameters |
| `rho0` | system.ntk-gradient-flow | parameters | — | initialization distribution |
| `sigma` | system.ntk-gradient-flow | parameters | — | activation function |
| `theta0` | system.ntk-gradient-flow | parameters | — | initial parameter vector |
| `y` | system.ntk-gradient-flow | parameters | a | training targets |
| `K` | system.ntk-gradient-flow | variables | a, a, t | empirical neural tangent kernel |
| `f` | system.ntk-gradient-flow | variables | a, t | network outputs on the training examples |
| `flin` | system.ntk-gradient-flow | variables | a, t | outputs of the model linearized at initialization |
| `theta` | system.ntk-gradient-flow | variables | t | trainable parameter vector |

## Symbols reused across records

- `init_draw` denotes a distinct quantity in phen.ntk.linearized-dynamics, system.ntk-gradient-flow.

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `at_zero` (the value of a trajectory at zero training time), `grad_output` (the gradient with respect to the output vector), `grad_parameter` (the gradient with respect to the parameter vector), `limiting_ntk` (the deterministic neural tangent kernel in the infinite-width limit), `network` (the outputs of a fully connected network), `ntk` (the empirical neural tangent kernel), `parameter_count` (the number of parameters fixed by width and depth), `risk` (the squared empirical risk).
