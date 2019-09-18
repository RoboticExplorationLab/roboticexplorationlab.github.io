---
title: Fast Solution of Optimal Control Problems With L1 Cost

description: |
  Developing a fast, low memory footprint algorithm to solve minimum-fuel problems with possible implementation onboard a CubeSat for embedded trajectory optimization.

people:
  - zac
  - simon

layout: project
image: "/img/rendezvous.png"
last-updated: 2019-08-06
---

Finding trajectories that minimize fuel-consumption or time to reach a goal is essential in many engineering fields and especially in astrodynamics. The formulation of such minimization problem is simple and involves a L1-norm cost term. This type of cost, however, greatly complicates the solve because of its nondifferentiability. This prevents the use of classical trajectory optimization solvers relying on cost differentiation. Also using commercial solvers without taking the structure of the optimization problem into account leads to long solving time and large memory footprint. This prevents the implementation of such solvers onboard of embedded systems such as small satellites.

This research proposes an iterative algorithm to solve optimal control problems with L1 cost. It decompose the original problem into a sequence of simple linear-quadratic problems (LQR) using the alternating direction method of multipliers (ADMM). The low computational complexity coupled with the fast execution of this algorithm make it suitable for implementation in flight software.

Future work includes implementation of the optimization algorithm  to embedded hardware. Potential application of this algorithm could be autonomous trajectory planning on small satellites, which is the objective of the [Pathfinder for Autonomous Navigation mission(PAN)](https://www.spacecraftresearch.com/pan). 

The code for the proposed algorithm is made available on RexLab's GitHub [L1CostOptimizer.jl](https://github.com/RoboticExplorationLab/L1CostOptimizer.jl.git).

![L1CostOptimizer solving a spacecraft rendezvous problem](/img/rendezvous.gif)
