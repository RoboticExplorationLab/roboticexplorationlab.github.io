---
title: Differentiable Collision-Free Parametric Corridors

description: |
  A differentiable collision-free corridor generator. 

people:
  - jon_arrizabalaga
  - zac 

layout: project
image: "/img/corrgen.gif"
last-updated: 2024-07-24
---

This paper presents a method to compute differentiable collision-free parametric corridors. In contrast to existing solutions that decompose the obstacle-free space into multiple convex sets, the continuous corridors computed by our method are smooth and differentiable, making them compatible with existing numerical techniques for learning and optimization. To achieve this, we represent the collision-free corridors as a path-parametric off-centered ellipse with a polynomial basis. We show that the problem of maximizing the volume of such corridors is convex, and can be efficiently solved. To assess the effectiveness of the proposed method, we examine its performance in a synthetic case study and subsequently evaluate its applicability in a real-world scenario from the KITTI dataset. 

# Resources
* Code: https://github.com/jonarriza96/corrgen
* Video: https://youtu.be/MvC7bPodXz8
* Paper: https://arxiv.org/pdf/2407.12283
