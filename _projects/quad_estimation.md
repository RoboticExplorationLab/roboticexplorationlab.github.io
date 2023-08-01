---
title: State Estimation For Legged Robots

description: |
  Several different state estimation methods for legged robots.

people:
  - zac
  - shuo
  - zixin

layout: project
image: "/img/vilo.gif"
last-updated: 2023-07-31
---

One important challenge for autonomous robots operating in GPS-denied environments is long-term state estimation. We have studied several different state estimation methods for legged robots.

Cerberus, a visual-inertial-leg odometer for legged robots, is one of the best open-source visual-inertial odometry systems for legged robots. It is a factor graph based state estimation system that integrates visual, inertial, joint and foot contact sensor measurements. It is able to estimate the robot's position, velocity, attitude, inertial sensor biases, and leg kinematics parameters.

The controller and the state estimator used on legged robots need accurate forward kinematics functions to calculate foothold locations and estimate robot velocity. Due to foot deformation, the actual forward kinematics often differ from the forward kinematics model. We propose a method to estimate forward kinematics parameters online within a visual-inertial-leg odometer whose state contains not only physical states like position and velocity, but also leg kinematics parameters such as actual contact points on the feet. The odometer integrates multi-modal information from visual sensor, inertial sensor, joint sensor and foot contact sensor in a factor graph manner. The factor graph defines a probabilistic inference problem whose solution contains the best estimation of the physical states, inertial sensor biases and forward kinematics parameters.

It has been discovered that adding IMUs on robot feet can significantly improve the state estimation accuracy. In addition to conventional sensors, including one body Inertial Measurement Unit (IMU) and joint encoders, we attach an additional IMU to each calf link of the robot just above the foot. An extended Kalman filter is used to fuse data from all sensors to estimate the robot's body and foot positions in the world frame. Using the additional IMUs, the filter is able to reliably determine foot contact modes and detect foot slips without tactile or pressure-based foot contact sensors. This sensing solution is validated in various hardware experiments, which confirm that it can reduce position drift by nearly an order of magnitude compared to conventional approaches with only a very modest increase in hardware and computational costs. 
