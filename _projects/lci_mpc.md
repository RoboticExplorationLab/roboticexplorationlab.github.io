---
title: Linear Contact-Implicit Model-Predictive Control

description: |
  Fast model-predictive control for systems that make and break contact with objects and the environment.

people:
  - simon
  - taylor
  - zac

layout: project
image: "/img/lci_mpc/hopper_parkour.gif"
no-link: true
last-updated: 2021-07-09
---

We present a general approach for controlling robotic systems that make and break contact with their environments: linear contact-implicit model-predictive control (LCI-MPC). Our use of differentiable contact dynamics provides a natural extension of linear model-predictive control to contact-rich settings. The policy leverages precomputed linearizations about a reference state or trajectory while contact modes, encoded via complementarity constraints, are explicitly retained, resulting in policies that can be efficiently evaluated while maintaining robustness to changes in contact timings. In many cases, the algorithm is even capable of generating entirely new contact sequences. To enable real-time performance, we devise a custom structure-exploiting linear solver for the contact dynamics. We demonstrate that the policy can respond to disturbances by discovering and exploiting new contact modes and is robust to model mismatch and unmodeled environments for a collection of simulated robotic systems, including: pushbot, hopper, quadruped, and biped.
