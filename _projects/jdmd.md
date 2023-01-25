---
title: Data-Efficient Model Learning for Control

description: |
  Building new algorithms for learning dynamics models that are sample efficient and generalizable.

people:
  - zac
  - brian
  - jj 

layout: project
image: "/img/jdmd/quad_jdmd.gif"
last-updated: 2022-08-12
---

![Plane](/img/jdmd/plane_jdmd.gif)
![Cartpole](/img/jdmd/cartpole_good.gif)

We present a data-efficient algorithm for learning models for model-predictive control (MPC). Our approach, Jacobian-Regularized Dynamic-Mode Decomposition (JDMD), offers improved sample efficiency over traditional Koopman approaches based on Dynamic-Mode Decomposition (DMD) by leveraging Jacobian information from an approximate prior model of the system, and improved tracking performance over traditional model-based MPC. We demonstrate JDMD’s ability to quickly learn bilinear Koopman dynamics representations across several realistic examples in simulation, including a perching maneuver for a fixed-wing aircraft with an empirically derived high-fidelity physics model. In all cases, we show that the models learned by JDMD provide superior tracking and generalization performance within a model-predictive control framework, even in the presence of significant model mismatch, when compared to approximate prior models and models learned by standard Extended DMD (EDMD).

[![dist quad](http://img.youtube.com/vi/IegIUn9eTrE/0.jpg)](https://www.youtube.com/watch?v=IegIUn9eTrE "koopman")

# Resources
* [Code Repository](https://github.com/bjack205/BilinearControl.jl)