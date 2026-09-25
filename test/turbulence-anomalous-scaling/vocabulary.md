---
tags:
  - generated
index: "[turbulence-anomalous-scaling](test/turbulence-anomalous-scaling/_index.md)"
---
# Vocabulary of turbulence-anomalous-scaling

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `P` | phen.turbulence.velocity-increment-distributions | explanandum variables | rmag, rdir | joint distribution of the increments |
| `S` | phen.turbulence.velocity-increment-distributions | explanandum variables | p, rmag, rdir | longitudinal structure function |
| `ST` | phen.turbulence.velocity-increment-distributions | explanandum variables | p, rmag, rdir | transverse structure function |
| `du` | phen.turbulence.velocity-increment-distributions | explanandum variables | x, t, rmag, rdir | velocity increment across a separation |
| `duL` | phen.turbulence.velocity-increment-distributions | explanandum variables | x, t, rmag, rdir | longitudinal increment |
| `duT` | phen.turbulence.velocity-increment-distributions | explanandum variables | x, t, rmag, rdir | transverse increment |
| `p` | phen.turbulence.velocity-increment-distributions | index sets | — | order of the structure function |
| `rdir` | phen.turbulence.velocity-increment-distributions | index sets | — | direction of the separation, a unit vector |
| `rmag` | phen.turbulence.velocity-increment-distributions | index sets | — | magnitude of the separation |
| `anomalous_scaling` | phen.turbulence.velocity-increment-distributions | manifestations | — | power-law scaling of the longitudinal structure functions |
| `increment_disparity` | phen.turbulence.velocity-increment-distributions | manifestations | — | disparity between longitudinal and transverse intermittency |
| `transverse_scaling` | phen.turbulence.velocity-increment-distributions | manifestations | — | power-law scaling of the transverse structure functions |
| `zetaL` | phen.turbulence.velocity-increment-distributions | manifestations.features | — | longitudinal scaling exponents, one per order |
| `zetaT` | phen.turbulence.velocity-increment-distributions | manifestations.features | — | transverse scaling exponents, one per order |
| `family` | phen.turbulence.velocity-increment-distributions | scope over instances | — | admitted families of forcing and boundary conditions |
| `realization` | phen.turbulence.velocity-increment-distributions | scope over instances | — | flow realizations under one family of forcing and boundary conditions |
| `boundaryenv` | system.turbulence-incompressible-navier-stokes | external systems | — | formal environment at the boundary |
| `forcing` | system.turbulence-incompressible-navier-stokes | external systems | — | formal forcing process |
| `t` | system.turbulence-incompressible-navier-stokes | index sets | — | time |
| `x` | system.turbulence-incompressible-navier-stokes | index sets | — | spatial location in the flow domain |
| `boundary_law` | system.turbulence-incompressible-navier-stokes | laws | x | boundary constraint |
| `gauge` | system.turbulence-incompressible-navier-stokes | laws | — | pressure gauge |
| `incompressible` | system.turbulence-incompressible-navier-stokes | laws | x | incompressibility constraint |
| `momentum` | system.turbulence-incompressible-navier-stokes | laws | x | incompressible momentum balance |
| `Lc` | system.turbulence-incompressible-navier-stokes | parameters | — | characteristic length scale |
| `Om` | system.turbulence-incompressible-navier-stokes | parameters | — | flow domain |
| `Re` | system.turbulence-incompressible-navier-stokes | parameters | — | Reynolds number |
| `U` | system.turbulence-incompressible-navier-stokes | parameters | — | characteristic velocity scale |
| `eps` | system.turbulence-incompressible-navier-stokes | parameters | — | mean rate of energy injection by the forcing |
| `etaK` | system.turbulence-incompressible-navier-stokes | parameters | — | Kolmogorov dissipation scale |
| `nu` | system.turbulence-incompressible-navier-stokes | parameters | — | kinematic viscosity |
| `b` | system.turbulence-incompressible-navier-stokes | variables | x, t | boundary data |
| `f` | system.turbulence-incompressible-navier-stokes | variables | x, t | field of body force |
| `pr` | system.turbulence-incompressible-navier-stokes | variables | x, t | field of kinematic pressure |
| `u` | system.turbulence-incompressible-navier-stokes | variables | x, t | velocity field |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `boundary` (the boundary of a spatial domain), `norm_one` (whether a three-dimensional vector has unit Euclidean norm), `regions` (the admissible regions of a space), `restrict` (the restriction of a field to a region), `stationary` (whether the statistics of a field indexed by time are invariant under time translation).
