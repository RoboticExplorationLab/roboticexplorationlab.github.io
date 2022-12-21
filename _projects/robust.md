---
title: Robust Motion Planning

description: |
  Making things get where they're supposed to go when we don't know exactly how they move and what disturbance forces might be pushing on them.

people:
  - zac
  - kevin
  - giusy

layout: project
image: "/img/funnel.jpg"
last-updated: 2018-08-09
---

We're applying recent ideas from robotic motion planning to atmospheric entry vehicles. Knowledge of a planet’s atmosphere, winds, and the vehicle’s position and velocity are all imperfect. As future NASA missions seek to land larger payloads with greater precision on Mars and elsewhere, effectively reasoning about these uncertainties will be crucial. To meet this challenge, we're developing a unified framework for modeling, trajectory design, and control that explicitly deals with uncertainty at every stage in the process to enhance performance and safety. Our approach harnesses new tools from optimization to compute "invariant funnels" - tubes around a nominal vehicle trajectory that bound the effects of uncertainties and disturbances like winds. Using these funnels, we can plan trajectories that are guaranteed to meet safety and accuracy requirements while taking full advantage of vehicle capabilities to enhance performance.
