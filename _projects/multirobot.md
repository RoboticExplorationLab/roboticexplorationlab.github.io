---
title: Distributed Trajectory Optimization 

description: |
  Extends the power and generality of trajectory optimization to multi-agent systems with sparse constraint interaction.  

people:
  - zac
  - brian
  - taylor 

layout: project
image: "/img/slung_load.jpg"
last-updated: 2019-08-15
---
Cooperation among autonomous agents is important in many robotics applications. Approaches for coordinating multi-robot systems range from decentralized or "bottom up" techniques that use simple local controllers with limited communication or computation that achieve desirable global behavior to centralized or "top down" methods that jointly optimize agents using information about the full system. While bottom up approaches can achieve interesting global behavior there are important limitations. Simple (and often homogeneous) dynamics (e.g., double integrators) are typically required and it is often difficult to explicitly reason about constraints on the system. Alternatively, top down approaches can reason about general dynamics and constraints but requiring solving large optimization problems with the results being communicated to each agent. 

In this work we present an approach for solving the centralized problem in a distributed manner that enables coordination of a system with general nonlinear dynamics subject to general nonlinear constraints. The centralized batch problem can be solved using a trajectory optimization solver. We employ ALTRO, which uses an augmented Lagrangian (AL) method for constraint handling. Because multi-robot systems are typically sparsely constrained, the centralized optimization problem is often nearly separable. Using AL decomposition methods, most closely related to nonlinear Jacobi algorithms, we present an algorithm that decomposes and distributes the batch optimization problem to each agent in the system for a parallel solve that converges to a desired system behavior. 

To demonstrate the algorithm, we consider a team-lift problem where multiple agents must coordinate their motion in order to transport a load. We verify the results in simulation for both double integrator and quadrotor (thirteen dimensional state with quaternion angular representation) teams. In hardware we demonstrate the algorithm solving the team-lift problem onboard three quadrotors with limited computational resources in a distributed manner.

The code is available on the "ADMM2" branch of [TrajectoryOptimization.jl](https://github.com/RoboticExplorationLab/TrajectoryOptimization.jl/tree/ADMM2).

![Quadload Door Switch](/img/quad_doorswitch.gif)
