---
title: Convex Maneuver Planning for Spacecraft Collision Avoidance

description: |
  An algorithm to design globally optimal low-thrust collision-avoidance maneuvers for short-term conjunction events. 

people:
  - fausto
  - jon_arrizabalaga
  - zac 

layout: project
image: "/img/spacecraft_cola.png"
last-updated: 2025-12-1
---

Conjunction analysis and maneuver planning for spacecraft collision avoidance remains a manual and time-consuming process, typically involving repeated forward simulations of hand-designed maneuvers. With the growing density of satellites in low-Earth orbit (LEO), autonomy is becoming essential for efficiently evaluating and mitigating collisions. 
In this work, we present an algorithm to design low-thrust collision-avoidance maneuvers for short-term conjunction events. We first formulate the problem as a nonconvex quadratically-constrained quadratic program (QCQP), which we then relax into a convex semidefinite program (SDP) using Shor's relaxation. We demonstrate empirically that the relaxation is tight,  which enables the recovery of globally optimal solutions to the original nonconvex problem. Our formulation produces a minimum-energy solution while ensuring a desired probability of collision at the time of closest approach. Finally, if the desired probability of collision cannot be satisfied, we relax this constraint into a penalty, yielding a minimum-risk solution. We validate our algorithm with a high-fidelity simulation of a satellite conjunction in low-Earth orbit with a simulated conjunction data message (CDM), demonstrating its effectiveness 
in reducing collision risk. 

Checkout our code:
* [Collision Avoidance Maneuver Planning Code](https://github.com/RoboticExplorationLab/cvx-spacecraft-cola)
