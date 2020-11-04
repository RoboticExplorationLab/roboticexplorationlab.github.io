---
title: Fast Trajectory Optimization

description: |
  Building new solvers for trajectory optimization problems that are fast, accurate, and numerically robust.

people:
  - zac
  - taylor
  - brian
  - andrew

layout: project
image: "/img/quadrotor_maze.png"
last-updated: 2019-12-04
---

Trajectory optimization is a powerful tool for motion planning, enabling the synthesis of dynamic motion for complex underactuated robotic systems. This general framework can be applied to robots with nonlinear dynamics and constraints where other motion planning paradigms---such as sample-based planning, inverse dynamics, or differential flatness---are impractical or ineffective.

In early 2019, we released the first iteration of the ALTRO algorithm (Augmented Lagrangian TRajectory Optimizer), which combines the robustness, versatility, and generality of direct methods such as DIRCOL with the speed of indirect methods like iterative LQR (iLQR). The core of the algorithm applies iLQR within an Augmented Lagrangian outer loop that handles general inequality and equality constraints, including obstacle avoidance. Novel refinements include improved numerical conditioning, minimum time formulations, the ability to feed a dynamically infeasible state trajectory as an initial guess, and anytime feasibility through using projected Newton steps. The result is a state-of-the-art trajectory optimization solver that has already been applied to a variety of problems with some promising results.

In 2020, ALTRO was split into several core packages, including [RobotDynamics.jl](https://github.com/RoboticExplorationLab/RobotDynamics.jl), [TrajectoryOptimization.jl](https://github.com/RoboticExplorationLab/TrajectoryOptimization.jl.git), and [Altro.jl](https://github.com/RoboticExplorationLab/ALTRO.jl), and was optimized for performance. In late 2020, we released ALTRO-C, a modification that included the ability to handle second-order cone programs (SOCPs) and demonstrated state-of-the-art performance against both OSQP and ECOS. 

ALTRO also has the ability to plan directly on the space of 3D rotations by optimizing on the Lie Algebra while representing the trajectory using unit quaternions. 


![ALTRO running a quadcopter through a maze](/img/maze_v2.gif)
![Quadrotor Flip](/img/quadflip.gif)

<img src="/img/kuka_combined.png" alt="drawing" width="600"/>

