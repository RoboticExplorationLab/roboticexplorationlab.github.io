---
title: Low-thrust Trajectory Optimization

description: |
  Optimizing long duration spacecraft maneuvers for electric propulsion. 

people:
  - zac
  - kevin

layout: project
image: "/img/gto_2_geo.png"
last-updated: 2019-12-01
---

We are using ALTRO (Augmented Lagrangian TRajectory Optimizer) to solve for time optimal orbital transfers from Geostationary Transfer Orbit (GTO), to Geostationary Orbit (GEO). This process is commonly referred to as "orbit raising", and has been performed successfully for decades with chemical propulsion. With more fuel efficient electric propulsion options (Hall effect thrusters, stationary plasma thrusters, etc), the thrust available is significantly less than that of chemical propulsion. This extends the orbit raising period from a few days with chemical propulsion, to a few months with electric propulsion. This significant decrease in available thrust makes using traditional chemical based methods for orbit raising infeasible with electric propulsion. Trajectory optimization is being utilized to solve for a novel thrust plan to take advantage of the specifics of the electric propulsion subsystem. 

