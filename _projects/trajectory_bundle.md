---
title: The Trajectory Bundle Method

description: |
  Unifying Sequential-Convex Programming and Sampling-Based Trajectory Optimization for robust motion planning.

people:
  - kevin
  - john
  - jon_arrizabalaga
  - zac

layout: project
image: "/img/trajectory_bundle_method.png"
last-updated: 2025-09-30
---

We present a unified framework for solving trajectory optimization problems in a derivative-free manner through the use of sequential convex programming. Traditionally, nonconvex optimization problems are solved by forming and solving a sequence of convex optimization problems, where the cost and constraint functions are approximated locally through Taylor series expansions. This presents a challenge for functions where differentiation is expensive or unavailable. In this work, we present a derivative-free approach to form these convex approximations by computing samples of the dynamics, cost, and constraint functions and letting the solver interpolate between them. Our framework includes sample-based trajectory optimization techniques like model-predictive path integral (MPPI) control as a special case and generalizes them to enable features like multiple shooting and general equality and inequality constraints that are traditionally associated with derivative-based sequential convex programming methods. The resulting framework is simple, flexible, and capable of solving a wide variety of practical motion planning and control problems. 
