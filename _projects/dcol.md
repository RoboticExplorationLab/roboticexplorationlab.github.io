---
title: Differentiable Collision Detection
description: |
  Smooth and differentiable collision detection between pairs of convex primitives, enabled by differentiable convex optimization.

people:
  - kevin
  - taylor
  - simon
  - zac

layout: project
image: "/img/dcol/dcol.gif"
no-link: true
last-updated: 2022-08-10
---
Collision detection between objects is critical for simulation, control, and learning for robotic systems. However, existing collision detection routines are inherently non-differentiable, limiting their usefulness in optimization-based algorithms. In this work, we propose a fully differentiable collision-detection framework that reasons about distances between a set of composable and highly expressive convex primitive shapes. This is achieved by formulating the collision detection problem as a convex optimization problem that seeks to find the minimum uniform scaling to be applied to each object before there is an intersection.  The optimization problem is fully differentiable and is able to return both the collision detection status as well as the contact points on each object.

- [paper](https://arxiv.org/abs/2207.00669) 
