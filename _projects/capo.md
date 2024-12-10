---
title: Control and Actuator Placement Optimization for Large-Scale Problems with Nonlinear Dynamics

description: |
 A scalable optimization formulation for the simultaneous control and actuator selection and placement for large scale robot systems.

people:
  - mitch
  - giusy 
  - zac

layout: project
image: "/img/capo/Presentation.gif"
last-updated: 2024-12-09
---

Actuator selection and placement are critical aspects of robot design that are tightly coupled to task performance. Jointly optimizing actuator placement and control policies or trajectories can enhance efficiency and robustness. However, current optimization methods struggle to scale to high-dimensional systems with many degrees of freedom, including soft robots, large flexible spacecraft, or cloth manipulation.
We propose CAPO, a scalable Control and Actuator Placement Optimization method that jointly optimizes the number, type, and placement of actuators, along with control trajectories. CAPO concurrently optimizes over all the control and design parameters in a single computationally tractable nonlinear program that scales favorably with system size and complexity. CAPO is evaluated against a state-of-the-art genetic algorithm and mixed-integer programming solvers on six problems, including an acrobatic multirotor aircraft, a spinning space structure, cloth manipulation, and a soft robotic swimmer. On small-scale problems, CAPO finds comparable solutions with similar objective values in 2.5-218x less time than existing methods. On large-scale problems, CAPO is the only method capable of finding a feasible solution, and it achieves actuator configurations that reduce the total number of actuators by 12\%-27.5\% compared to baselines.

- [Paper](../papers/CAPO_WAFR_2024.pdf)
