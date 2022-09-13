---
title: Efficient Model Learning for Control

description: |
  Building new solvers for trajectory optimization problems that are fast, accurate, and numerically robust.

people:
  - zac
  - brian
  - jj 

layout: project
image: "/img/koopman/quad_jdmd.gif"
last-updated: 2022-08-12
---

![Plane](/img/koopman/plane_jdmd.gif)
![Cartpole](/img/koopman/cartpole_good.gif)
![Quad](/img/koopman/quad_jdmd.gif)

We present a data-efficient algorithm for learning models for model-predictive control (MPC). Our approach, Jacobian-Regularized DMD (JDMD), offers improved sample efficiency over traditional Koopman approaches based on Dynamic-Mode Decomposition (DMD) by leveraging Jacobian  information from an approximate prior model of the system, and improved tracking performance over traditional model-based MPC. We demonstrate JDMD's ability to quickly learn bilinear Koopman dynamics representations across several realistic examples in simulation, including a perching maneuver for a fixed-wing aircraft with an experimentally derived high-fidelity physics model.   In all cases, we show that the models learned by JDMD provide superior tracking and generalization performance in the presence of significant model mismatch within a model-predictive control framework,  when compared to the approximate prior models used in training and models learned by  standard extended DMD

[![dist quad](http://img.youtube.com/vi/IegIUn9eTrE/0.jpg)](https://www.youtube.com/watch?v=IegIUn9eTrE "koopman")

# Resources
* [Code Repository](https://github.com/bjack205/BilinearControl.jl)

