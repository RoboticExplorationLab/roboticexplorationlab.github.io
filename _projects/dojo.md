---
title: Dojo - A Differentiable Simulator for Robotics

description: |
  Differentiable rigid-body-dynamics with contact simulator for robotic systems.

people:
  - taylor
  - simon
  - jan
  - zac

layout: project
image: "/img/dojo/quadruped.gif"
no-link: true
last-updated: 2022-03-07
---
We present a differentiable rigid-body-dynamics simulator for robotics that prioritizes physical accuracy and differentiability, Dojo. The simulator utilizes an expressive maximal-coordinates representation, achieves stable simulation at low sample rates, and conserves energy and momentum by employing a variational integrator. A nonlinear complementarity problem, with nonlinear friction cones, models hard contact and is reliably solved using a custom primal-dual interior-point method. The implicit-function theorem enables efficient differentiation of an intermediate relaxed problem and computes smooth gradients from the contact model. We demonstrate the usefulness of the simulator and its gradients through a number of examples including: simulation, trajectory optimization, reinforcement learning, and system identification. 

- [code](https://github.com/dojo-sim) 
- [paper](https://arxiv.org/abs/2203.00806) 
- [website](https://sites.google.com/view/dojo-sim/home)
