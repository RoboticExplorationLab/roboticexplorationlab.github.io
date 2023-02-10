---
title: Differentiable Fluid-Structure Interaction for Robotics

description: |
  A fully differentiable solver for simulating coupled fluid-solid dynamics

people:
  - jj
  - zac 

layout: project
image: "/img/aquarium/aquarium.gif"
last-updated: 2023-02-09
---

![freestream_cylinder](/img/aquarium/freestream_cylinder_comparison.gif)
![foil_optimization](/img/aquarium/oscillating_foil_gait_optimization_comparison.gif)

We present Aquarium, a differentiable fluid-structure interaction solver for robotics that offers stable simulation, accurate coupled robot-fluid physics, and full differentiability with respect to fluid states, robot states, and shape parameters. Aquarium achieves stable simulation with accurate flow physics by integrating over the discrete, incompressible Navier-Stokes equations directly using a fully-implicit Crank-Nicolson scheme with a second-order finite-volume spatial discretization. The robot and fluid physics are coupled using the immersed boundary method by formulating the no-slip condition as an equality constraint applied directly to the Navier-Stokes system. This choice of coupling allows the fluid-structure interaction to be posed and solved as a nonlinear optimization problem. This optimization-based formulation is then exploited using the implicit-function theorem to compute derivatives. The derivatives can then be passed to a gradient-based optimization or learning framework. We demonstrate Aquarium's ability to accurately simulate coupled fluid-solid physics with numerous examples, including a cylinder in free stream and a soft robotic tail with hardware validation. We also demonstrate Aquarium's ability to provide full, analytical gradients by performing both shape and gait optimization of a robotic fish tail to maximize generated thrust.

# Resources
* [Code Repository](https://github.com/RoboticExplorationLab/Aquarium.jl)