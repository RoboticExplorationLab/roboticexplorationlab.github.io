---
title: Model-Predictive Control on Resource-Constrained Microcontrollers

description: |
  A high-speed MPC solver with a low memory footprint that works on microcontrollers common on small robots. 

people:
  - anoushka
  - khai
  - sam
  - zac

layout: project
image: "/img/tinympc/tinympc.gif"
last-updated: 2023-10-26
---

Model-predictive control (MPC) is a powerful tool for controlling highly dynamic robotic systems subject to complex constraints. However, MPC is computationally demanding, and is often impractical to implement on small, resource-constrained robotic platforms. We present TinyMPC, a high-speed MPC solver with a low memory footprint targeting the microcontrollers common on small robots. Our approach is based on the alternating direction method of multipliers (ADMM) and leverages the structure of the MPC problem for efficiency. We demonstrate TinyMPC both by benchmarking against the state-of-the-art solver OSQP, achieving nearly an order of magnitude speed increase, as well as through hardware experiments on a 27 g quadrotor, demonstrating high-speed trajectory tracking and dynamic obstacle avoidance.

TinyMPC is publicly available at [tinympc.org](https://tinympc.org/).
