---
title: The Surprising Effectiveness of Linear Models for Whole-Body Model-Predictive Control

description: |
  A single whole-body linearization is sufficient for basic locomotion tasks on humanoids and quadrupeds.

people:
  - arun
  - juan
  - sam
  - ibrahima
  - willK
  - zac 

layout: project
image: "/img/linear_walking.gif"
last-updated: 2025-10-15
---

When do locomotion controllers require reasoning about nonlinearities? In this work, we show that a whole-body model-predictive controller using a simple linear time-invariant approximation of the whole-body dynamics is able to execute basic locomotion tasks on complex legged robots. The formulation requires no online nonlinear dynamics evaluations or matrix inversions. We demonstrate walking, disturbance rejection, and even navigation to a goal position without a separate footstep planner on a quadrupedal robot. In addition, we demonstrate dynamic walking on a hydraulic humanoid, a robot with significant limb inertia, complex actuator dynamics, and large sim-to-real gap.

Check out our [website](https://linearwalking.github.io/).