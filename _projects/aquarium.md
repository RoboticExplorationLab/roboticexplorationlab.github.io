---
title: Differentiable Fluid-Structure Interaction for Robotics

description: |
  A fully differentiable solver for simulating coupled fluid-robot dynamics

people:
  - jj
  - zac 

layout: project
image: "/img/aquarium/aquarium.gif"
last-updated: 2023-02-09
---

![freestream_cylinder](/img/aquarium/cylinder_animation.gif)
![foil_optimization](/img/aquarium/foil_animation.gif)

We present Aquarium, a differentiable fluid-structure interaction solver for robotics that offers stable simulation, accurately coupled fluid-robot physics in two dimensions, and full differentiability with respect to fluid and robot states and parameters. Aquarium achieves stable simulation with accurate flow physics by directly integrating over the incompressible Navier-Stokes equations using a fully implicit Crank-Nicolson scheme with a second-order finite-volume spatial discretization. The fluid and robot physics are coupled using the immersed-boundary method by formulating the no-slip condition as an equality constraint applied directly to the Navier-Stokes system. This choice of coupling allows the fluid-structure interaction to be posed and solved as a nonlinear optimization problem. This optimization-based formulation is then exploited using the implicit-function theorem to compute derivatives. Derivatives can then be passed to downstream gradient-based optimization or learning algorithms. We demonstrate Aquarium's ability to accurately simulate coupled fluid-robot physics with numerous 2D examples, including a cylinder in free stream and a soft robotic fish tail with hardware validation. We also demonstrate Aquarium's ability to provide analytical gradients by performing gradient-based shape-and-gait optimization of an oscillating diamond foil to maximize its generated thrust.

# Resources
* [Code Repository](https://github.com/RoboticExplorationLab/Aquarium.jl)
* [Supplemental Video](https://www.youtube.com/watch?v=vDr03uDEUL0)