---
title: Distributed Trajectory Optimization 

description: |
  Scalable Cooperative Transport of Cable-Suspended Loads with UAVs using Distributed Trajectory Optimization 

people:
  - zac
  - brian
  - taylor 

layout: project
image: "/img/team_lift.jpg"
last-updated: 2019-08-15
---
Most approaches to multi-robot control either rely on local decentralized control policies that scale well in the number of agents, or on centralized methods that can handle constraints and produce rich system-level behavior, but are typically computationally expensive and scale poorly in the number of agents, relegating them to offline planning. This work presents a scalable approach that uses distributed trajectory optimization to parallelize computation over a group of computationally-limited agents while handling general nonlinear dynamics and non-convex constraints. The approach, including near-real-time onboard trajectory generation, is demonstrated in hardware on a cable-suspended load problem with a team of quadrotors automatically reconfiguring to transport a heavy load through a doorway.

The code is available on the "ADMM" branch of [TrajectoryOptimization.jl](https://github.com/RoboticExplorationLab/TrajectoryOptimization.jl/tree/ADMM).

[![dist quad](http://img.youtube.com/vi/INr92G_qOls/0.jpg)](http://www.youtube.com/watch?v=INr92G_qOls "dist quad")
