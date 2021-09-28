---
title: Fast Contact-Implicit Model-Predictive Control

description: |
  Fast model-predictive control for systems that make and break contact with objects and the environment.

people:
  - simon
  - taylor
  - zac

layout: project
image: "/img/ci_mpc/hopper_parkour.gif"
no-link: true
last-updated: 2021-09-27
---

We present a general approach for controlling robotic systems that make and break contact with their environments. Contact-implicit model-predictive control (CI-MPC) generalizes linear MPC to contact-rich settings by relying on linear complementarity problems (LCP) computed using strategic Taylor approximations about a reference trajectory and retaining non-smooth impact and friction dynamics, allowing the policy to not only reason about contact forces and timing, but also generate entirely new contact mode sequences online. To achieve reliable and fast numerical convergence, we devise a structure-exploiting, path-following solver for the LCP contact dynamics and a custom trajectory optimizer for trajectory-tracking MPC problems. We demonstrate CI-MPC at real-time rates in simulation, and show that it is robust to model mismatch and can respond to disturbances by discovering and exploiting new contact modes across a variety of robotic systems, including a pushbot, hopper, and planar quadruped and biped. 

Our implementation and examples can be found [here](https://github.com/thowell/ContactImplicitMPC.jl).
