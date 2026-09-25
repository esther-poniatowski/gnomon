---
tags:
  - examples
index: "[Neural tangent dynamics](test/neural-tangent-kernel-model-knowledge/_index.md)"
aliases:
  - Neural tangent kernel model-knowledge test description
---
# Validity of neural tangent dynamics

## Research problem

Wide networks can approach a regime in which their empirical neural tangent kernel stays nearly constant during training. The nonlinear output trajectory of such a network can then approach the trajectory of the tangent model linearized at initialization. Which assumptions imply these limits, and what error bounds delimit their validity at finite width?

## Formal target

The target is a class of fully connected networks with scalar output under neural tangent parameterization. Each network is trained by continuous gradient flow on a fixed finite dataset with squared loss. The formal system includes the nonlinear trajectory and its empirical tangent kernel. The same system includes the corresponding linearized trajectory.

## Fixed phenomenon

The phenomenon to characterize is conditional convergence toward linearized dynamics governed by the initial kernel as width increases. Its observables compare the relevant trajectories and kernels at each stage of the limit. The set of network and training specifications for which convergence holds remains part of the requested result.

## Requested model knowledge

A satisfactory answer must state which convergence claims follow from the model. Each claim must identify its assumptions and quantify over initializations. Each claim must also delimit its limiting regime. Its conclusion must state the training horizon and the error at finite width. For this reason, a report of representative simulations remains incomplete when it does not delimit the domain of the claim.

## Expressivity challenge

The records must let the framework:

- specify a consequence sought from the formal model without asserting it in advance;
- distinguish an asymptotic limit from a bound at finite width that supports it;
- state which quantities remain fixed as width grows;
- record the convergence mode and the time interval over which the claim holds;
- derive a product test that checks the requested consequence and its validity domain.

## Scope boundary

The requested product consists of consequences derived from the formal model class. The inquiry therefore excludes explanations of the empirical success of trained networks. Its candidate theorem holds under explicit assumptions on regularity and on the spectrum. The assessment of that theorem serves as a positive control.

## Scientific basis

Under stated initialization and regularity assumptions, the empirical tangent kernel converges to a deterministic limit and remains constant during training as width tends to infinity ([jacot2018](https://papers.nips.cc/paper/2018/hash/5a4be1fa34e62bb8a6ec6b91d2462f5a-Abstract.html)). The training dynamics of wide networks likewise converge to their linearization around initialization under explicit conditions ([lee2019](https://papers.nips.cc/paper_files/paper/2019/hash/0d1a9651497a38d8b1c3871c84528bd4-Abstract.html)). Bounds between the nonlinear and linearized paths under gradient flow depend on the scaling regime and the training horizon ([chizat2019](https://papers.nips.cc/paper/8559-on-lazy-training-in-differentiable-programming.pdf)).
