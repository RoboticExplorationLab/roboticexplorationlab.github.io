---
title: Enhanced Balance for Legged Robots Using Reaction Wheels

description: |
  Novel hardware design to enhace quadruped robots

people:
  - shuo
  - chiyen
  - bbokser
  - zac

layout: project
image: "/img/reaction_wheel_mpc2.gif"
last-updated: 2023-02-07
---

We introduce a reaction wheel system that enhances quadrupedal robots' balancing capabilities and stability during challenging locomotion tasks. Inspired by both the standard centroidal dynamics model common in legged robotics and models of spacecraft commonly used in the aerospace community, we model the coupled quadruped-reaction-wheel system as a gyrostat, and simplify the dynamics to formulate the problem as a linear discrete-time trajectory optimization problem. Modifications are made to a standard centroidal model-predictive control (MPC) algorithm to solve for both stance foot ground reaction forces and reaction wheel torques simultaneously. The MPC problem is posed as a quadratic program and solved online at 1000 Hz. We demonstrate improved attitude stabilization both in simulation and on hardware compared to a quadruped without reaction wheels, and perform a challenging traversal of a narrow balance beam that would be impossible for a standard quadruped.