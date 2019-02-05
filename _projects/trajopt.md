---
title: Fast Trajectory Optimization

description: |
  Building new solvers for trajectory optimization problems that are fast, accurate, and numerically robust.

people:
  - zac
  - taylor
  - brian
  
layout: project
image: "http://stanford.edu/group/rexlab/img/perch.png"
no-link: true
last-updated: 2018-10-01
---

We're developing a novel indirect solver, based on iterative LQR (iLQR), that allows for general inequality and equality constraints, infeasible starts with specification of an initial guess trajectory, and high-order integration. The open-source code is available as part of the Julia package [TrajectoryOptimization.jl](https://github.com/RoboticExplorationLab/TrajectoryOptimization.jl.git). 