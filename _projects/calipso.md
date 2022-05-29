---
title: CALIPSO - A Differentiable Solver for Trajectory Optimization with Conic and Complementarity Constraints

description: |
  Trajectory optimization with conic and complementarity constraints--plus differentiable!

people:
  - taylor
  - kevin
  - simon
  - zac

layout: project
image: "/img/calipso/atlas_bunnyhop.gif"
no-link: true
last-updated: 2022-05-28
---
We present a new solver for non-convex trajectory optimization problems that is specialized for robotics applications. CALIPSO, or the Conic Augmented Lagrangian Interior-Point SOlver, combines several strategies for constrained numerical optimization to natively handle second-order cones and complementarity constraints. It reliably solves challenging motion-planning problems that include contact-implicit formulations of impacts and Coulomb friction, thrust limits subject to conic constraints, and state-triggered constraints where general-purpose nonlinear programming solvers like SNOPT and Ipopt fail to converge. Additionally, CALIPSO supports efficient differentiation of solutions with respect to problem data, enabling bi-level optimization applications like auto-tuning of feedback policies. Reliable convergence of the solver is demonstrated on a range of problems from manipulation, locomotion, and aerospace domains. An open-source implementation of this solver is available. 

- [code](https://github.com/thowell/CALIPSO.jl) 
- [paper](https://arxiv.org/abs/2205.09255) 
