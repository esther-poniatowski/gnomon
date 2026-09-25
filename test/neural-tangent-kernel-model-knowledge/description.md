---
tags:
  - examples
index: "[Neural tangent dynamics](test/neural-tangent-kernel-model-knowledge/_index.md)"
aliases:
  - Neural tangent kernel model-knowledge test description
---
# Validity of neural tangent dynamics

## Research problem

Wide neural networks can approach a regime in which their empirical neural tangent kernel stays nearly constant during training. Their nonlinear output trajectory can then approach the trajectory of the tangent model linearized at initialization. Which assumptions imply these limits, and what error bounds delimit their validity at finite width?

## Formal target

The target is a class of fully connected scalar-output networks under neural tangent parameterization. Each network is trained by continuous gradient flow on a fixed finite dataset with squared loss. The formal system includes the nonlinear trajectory and its empirical tangent kernel. The same system includes the corresponding linearized trajectory.

## Fixed phenomenon

The phenomenon to characterize is conditional convergence toward linearized dynamics governed by the initial kernel as width increases. Its observables compare the relevant trajectories and kernels at each stage of the limit, while the set of network and training specifications for which convergence holds remains part of the requested result.

## Model-knowledge product

A satisfactory answer must state which convergence claims follow from the model. Each claim must identify its assumptions and quantify over initializations. The claim must also delimit its limiting regime. Its conclusion must state the training horizon and finite-width error. A report of representative simulations remains incomplete when it does not delimit the claim's domain.

## Expressivity challenge

The records must let the framework:

- specify a consequence sought from the formal model without asserting that consequence in advance;
- distinguish an asymptotic limit from a finite-width bound that supports it;
- state which quantities remain fixed as width grows;
- record the convergence mode and the time interval over which the claim holds;
- derive a product test that checks the requested consequence and its validity domain.

## Scope boundary

The requested product consists of consequences derived from the formal model class. The inquiry excludes explanations of the empirical success of trained networks. The test also supplies no candidate theorem, proof, or assessment.

## Scientific basis

Under stated initialization and regularity assumptions, the empirical tangent kernel converges to a deterministic kernel and remains constant during training in the infinite-width limit ([jacot2018](https://papers.nips.cc/paper/2018/hash/5a4be1fa34e62bb8a6ec6b91d2462f5a-Abstract.html)). Wide-network dynamics likewise converge to the first-order linearization around initialization under explicit conditions ([lee2019](https://papers.nips.cc/paper_files/paper/2019/hash/0d1a9651497a38d8b1c3871c84528bd4-Abstract.html)). Bounds between nonlinear and linearized gradient-flow paths depend on the scaling regime and the training horizon ([chizat2019](https://papers.nips.cc/paper/8559-on-lazy-training-in-differentiable-programming.pdf)).
