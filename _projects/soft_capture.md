---
title: Convex Trajectory optimization for the Soft-Capture Problem

description: |
  A safe and real-time trajectory optimization algorithm for agile spacecraft maneuvers.

people:
  - ibrahima
  - zac

layout: project
image: "/img/soft_capture/approach.gif"
last-updated: 2024-05-05
---

We present a fast trajectory optimization algorithm for the soft capture of uncooperative tumbling space objects. Our algorithm generates safe, dynamically feasible, and minimum-fuel trajectories for a six-degree-of-freedom servicing spacecraft to achieve soft capture (near-zero relative velocity at contact) between predefined locations on the servicer spacecraft and target body. We solve a convex problem by enforcing a convex relaxation of the field-of-view constraint, followed by a sequential convex program correcting the trajectory for collision avoidance. The optimization problems can be solved with a standard second-order cone programming solver, making the algorithm both fast and practical for implementation in flight software. We demonstrate the performance and robustness of our algorithm in simulation over a range of object tumble rates up to 10 °/s.

- [Paper](https://arxiv.org/abs/2405.00867) 

# Resources
* [Code Repository](https://github.com/RoboticExplorationLab/SoftCapture)