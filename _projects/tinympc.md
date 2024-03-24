---
title: Model-Predictive Control on Resource-Constrained Microcontrollers

description: |
  A high-speed MPC solver with a low memory footprint that works on microcontrollers common on small robots. 

people:
  - khai
  - sam
  - anoushka
  - elakhya
  - zac

layout: project
image: "/img/tinympc/tinympc.gif"
last-updated: 2024-03-22
---

### Paper 1. TinyMPC: Model-Predictive Control on Resource-Constrained Microcontrollers
Model-predictive control (MPC) is a powerful
tool for controlling highly dynamic robotic systems subject
to complex constraints. However, MPC is computationally
demanding, and is often impractical to implement on small,
resource-constrained robotic platforms. We present TinyMPC,
a high-speed MPC solver with a low memory footprint targeting
the microcontrollers common on small robots. Our approach
is based on the alternating direction method of multipliers
(ADMM) and leverages the structure of the MPC problem for
efficiency. We demonstrate TinyMPC’s effectiveness by benchmarking against the state-of-the-art solver OSQP, achieving
nearly an order of magnitude speed increase, as well as through
hardware experiments on a 27 gram quadrotor, demonstrating
high-speed trajectory tracking and dynamic obstacle avoidance.

### Paper 2. Code Generation for Conic Model-Predictive Control on Microcontrollers with TinyMPC
Conic constraints appear in many important control applications like legged locomotion, robotic manipulation,
and autonomous rocket landing. However, current solvers for
conic optimization problems have relatively heavy computational demands in terms of both floating-point operations and
memory footprint, making them impractical for use on small
embedded devices. We extend TinyMPC, an open-source, high-speed solver targeting low-power embedded control applications, to handle second-order cone constraints. We also present
code-generation software to enable deployment of TinyMPC
on a variety of microcontrollers. We benchmark our generated
code against state-of-the-art embedded QP and SOCP solvers,
demonstrating a two-order-of-magnitude speed increase over
ECOS while consuming less memory. Finally, we demonstrate
TinyMPC’s efficacy on the Crazyflie, a lightweight, resource-constrained quadrotor with fast dynamics.

**TinyMPC is publicly available at [https://tinympc.org](https://tinympc.org).**
