---
title: Pixels to Torques with Linear Feedback

description: |
  Data-driven, linear output-feedback policies can effectively control a robotic system using vision.

people:
  - jj
  - sam
  - zac 

layout: project
image: "/img/linear_pixels_to_torques/linear_pixels_to_torques.gif"
last-updated: 2024-06-26
---

We demonstrate the effectiveness of simple observer-based linear feedback policies for "pixels-to-torques" control of robotic systems using only a robot-facing camera. Specifically, we show that the matrices of an image-based Luenberger observer (linear state estimator) for a "student" output-feedback policy can be learned from demonstration data provided by a "teacher" state-feedback policy via simple linear-least-squares regression. The resulting linear output-feedback controller maps directly from high-dimensional raw images to torques while being amenable to the rich set of analytical tools from linear systems theory, alowing us to enforce closed-loop stability constraints in the learning problem. We also investigate a nonlinear extension of the method via the Koopman embedding. Finally, we demonstrate the surprising effectiveness of linear pixels-to-torques policies on a cartpole system, both in simulation and on real-world hardware. The policy successfully executes both stabilizing and swing-up trajectory tracking tasks using only camera feedback while subject to model mismatch, process and sensor noise, perturbations, and occlusions.

# Resources
* Code coming soon!