---
tags:
  - generated
index: "[active-matter-phase-exploration](test/active-matter-phase-exploration/_index.md)"
---
# Vocabulary of active-matter-phase-exploration

Built by `gnomon vocabulary --markdown` from `vocabulary.yml`. Edit a record, not this file.

## Symbols

| Symbol | Declared in | Block | Signature | Gloss |
| --- | --- | --- | --- | --- |
| `C` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | sp, sp, rsep, lag | correlation matrix between species |
| `Cl` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | sp, sp, rsite, lag | correlation matrix between species on the lattice |
| `S` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | sp, sp, k, omega | spectral matrix between species |
| `Sl` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | sp, sp, klat, omega | spectral matrix between species on the lattice |
| `diag` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | L, d | diagnostic of phases for the continuum variant |
| `diag_lattice` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | L, d | diagnostic of phases for the lattice variant |
| `rho_emp` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | sp | empirical distribution of the local field state of each species |
| `rho_lat` | phen.nonreciprocal-active-matter.collective-phases | explanandum variables | sp | empirical distribution of the lattice state of each species |
| `k` | phen.nonreciprocal-active-matter.collective-phases | index sets | — | wavevector |
| `klat` | phen.nonreciprocal-active-matter.collective-phases | index sets | — | lattice wavevector |
| `lag` | phen.nonreciprocal-active-matter.collective-phases | index sets | — | temporal lag |
| `omega` | phen.nonreciprocal-active-matter.collective-phases | index sets | — | frequency |
| `rsep` | phen.nonreciprocal-active-matter.collective-phases | index sets | — | spatial separation |
| `rsite` | phen.nonreciprocal-active-matter.collective-phases | index sets | — | lattice displacement |
| `phase_catalogue` | phen.nonreciprocal-active-matter.collective-phases | manifestations | — | catalogue of distinguishable collective regimes |
| `phase_catalogue_lattice` | phen.nonreciprocal-active-matter.collective-phases | manifestations | — | catalogue of distinguishable lattice regimes |
| `phase` | phen.nonreciprocal-active-matter.collective-phases | manifestations.features | — | candidate collective phase |
| `phase_lattice` | phen.nonreciprocal-active-matter.collective-phases | manifestations.features | — | candidate collective phase on the lattice |
| `coupling` | phen.nonreciprocal-active-matter.collective-phases | scope over instances | — | admitted nonreciprocal operators of cross-coupling |
| `coupling_lattice` | phen.nonreciprocal-active-matter.collective-phases | scope over instances | — | admitted nonreciprocal couplings on the lattice |
| `realization` | phen.nonreciprocal-active-matter.collective-phases | scope over instances | — | stochastic realizations at fixed controls |
| `realization_lattice` | phen.nonreciprocal-active-matter.collective-phases | scope over instances | — | stochastic realizations of the lattice at fixed controls |
| `selfdyn` | phen.nonreciprocal-active-matter.collective-phases | scope over instances | — | admitted self-dynamics, diffusion coefficients and noise laws |
| `selfdyn_lattice` | phen.nonreciprocal-active-matter.collective-phases | scope over instances | — | admitted self-dynamics, diffusion coefficients and noise laws of the lattice |
| `sp` | system.nonreciprocal-active-matter | constituents | — | species field |
| `q` | system.nonreciprocal-active-matter | index sets | — | lattice site |
| `t` | system.nonreciprocal-active-matter | index sets | — | time |
| `x` | system.nonreciprocal-active-matter | index sets | — | spatial position |
| `evolve` | system.nonreciprocal-active-matter | laws | sp, x, t | local stochastic evolution |
| `evolve_lattice` | system.nonreciprocal-active-matter | laws | sp, q, t | local stochastic evolution on the lattice |
| `noiselaw` | system.nonreciprocal-active-matter | laws | sp, x | distribution of the local noise |
| `noiselaw_lattice` | system.nonreciprocal-active-matter | laws | sp, q | distribution of the local noise on the lattice |
| `nonrecip` | system.nonreciprocal-active-matter | laws | sp, sp | nonreciprocity of the cross-coupling |
| `nonrecip_lattice` | system.nonreciprocal-active-matter | laws | sp, sp | nonreciprocity of the lattice cross-coupling |
| `crosscoupling` | system.nonreciprocal-active-matter | organization | — | nonreciprocal cross-coupling |
| `crosscoupling_lattice` | system.nonreciprocal-active-matter | organization | — | nonreciprocal cross-coupling on the lattice |
| `D` | system.nonreciprocal-active-matter | parameters | sp | diffusion coefficient of the continuum |
| `Dl` | system.nonreciprocal-active-matter | parameters | sp | diffusion coefficient on the lattice |
| `F` | system.nonreciprocal-active-matter | parameters | sp | operator of the local self-dynamics |
| `Fl` | system.nonreciprocal-active-matter | parameters | sp | operator of the lattice self-dynamics |
| `G` | system.nonreciprocal-active-matter | parameters | sp, sp | linear operator of the cross-coupling |
| `Gl` | system.nonreciprocal-active-matter | parameters | sp, sp | linear operator of the lattice cross-coupling |
| `L` | system.nonreciprocal-active-matter | parameters | — | linear system size |
| `Q` | system.nonreciprocal-active-matter | parameters | sp | distribution of the local noise |
| `Ql` | system.nonreciprocal-active-matter | parameters | sp | noise law on the lattice |
| `U` | system.nonreciprocal-active-matter | parameters | sp | admitted local state space common to the two species |
| `bgeom` | system.nonreciprocal-active-matter | parameters | — | periodic geometry of the boundary |
| `d` | system.nonreciprocal-active-matter | parameters | — | spatial dimension |
| `W` | system.nonreciprocal-active-matter | variables | sp, x, t | stochastic increment of a species field |
| `Xi` | system.nonreciprocal-active-matter | variables | sp, q, t | stochastic increment at a lattice site |
| `u` | system.nonreciprocal-active-matter | variables | sp, x, t | local state of a species field |
| `v` | system.nonreciprocal-active-matter | variables | sp, q, t | local state at a lattice site |
| `continuum` | system.nonreciprocal-active-matter | variants | — | continuum field |
| `lattice` | system.nonreciprocal-active-matter | variants | — | lattice realization |

## Directed interactions

The nodes are kinds, not identified members: which tuples are joined is fixed by a parameter of a member model, and the last column says where to read it from. A tuple of three or more carries a joint influence, which no pair of endpoints could state.

| Sources | Edge | Reach | Through | Ordered tuples |
| --- | --- | --- | --- | --- |
| `sp` | `answer_crosscoupling` | `sp` | — | `prod(sp, sp)` |
| `sp` | `crosscoupling` | `sp` | `G` | `prod(sp, sp)` |
| `sp` | `crosscoupling_lattice` | `sp` | `Gl` | `prod(sp, sp)` |

## Operators

- Canonical: `abs`, `adjoint`, `bools`, `card`, `complex`, `decreasing`, `depends_on`, `diff`, `dist`, `div`, `dot`, `drawn_from`, `empty`, `enum`, `ft`, `grad`, `implies`, `increasing`, `infinity`, `intersect`, `interval`, `ints`, `jacobian`, `lap`, `limit`, `maps`, `matrices`, `max`, `mean`, `measures`, `min`, `nonneg`, `norm`, `pos`, `prod`, `range`, `re`, `reals`, `spectrum`, `subset`, `sum`, `union`, `vectors`.
- Declared by this problem: `lattice_lap` (the discrete Laplacian on the declared lattice), `regions` (the admissible regions of a space, of a given linear size and boundary geometry), `sites` (the sites of a finite lattice of a given dimension, size and boundary geometry).
