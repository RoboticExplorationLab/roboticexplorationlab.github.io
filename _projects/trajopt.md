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
last-updated: 2019-03-26
---

Trajectory optimization is a powerful tool for motion planning, enabling the synthesis of dynamic motion for complex underactuated robotic systems. This general framework can be applied to robots with nonlinear dynamics and constraints where other motion planning paradigms---such as sample-based planning, inverse dynamics, or differential flatness---are impractical or ineffective.

In early 2019, we released the first iteration of the ALTRO algorithm (Augmented Lagrangian TRajectory Optimizer), which combines the robustness, versatility, and generality of direct methods such as DIRCOL with the speed of indirect methods like iterative LQR (iLQR). The core of the algorithm applies iLQR within an Augmented Lagrangian outer loop that handles general inequality and equality constraints, including obstacle avoidance. Novel refinements include improved numerical conditioning, minimum time formulations, the ability to feed a dynamically infeasible state trajectory as an initial guess, and anytime feasibility through using projected Newton steps. The result is a state-of-the-art trajectory optimization solver that has already been applied to a variety of problems with some promising results.

Future work includes performance enhancements through more careful implementation and parallelization. Some of our current research is investigating distrubuted and parallelizable optimization methods like ADMM to break the problem into smaller pieces that can be solved simultaneously through parallelization, with application to multi-agent systems. 

The code for ALTRO is included in our package [TrajectoryOptimization.jl](https://github.com/RoboticExplorationLab/TrajectoryOptimization.jl.git), a library of solvers for trajectory optimization presented within an easy-to-use, unified framework. 

![ALTRO running a quadcopter through a maze](/img/maze_v2.gif)

<img src="/img/kuka_combined.png" alt="drawing" width="600"/>

