---
title: ALGAMES: A Fast Solver for Constrained Dynamic Games

description: |
  Developing a general solver for dynamic games aimed at identifying Nash equilibrium strategies specifically tailored to robotics applications. 

people:
  - zac
  - simon

layout: project
image: "/img/ALGAMES.png"
last-updated: 2019-09-17
---

Dynamic games are an effective paradigm for dealing with the control of multiple interacting actors. Current algorithms for solving these problems either rely on Hamilton-Jacobi-Isaacs (HJI) methods, dynamic programming (DP), differential dynamic programming (DDP), or an iterative best response approach (IBR). The first two approaches have strong theoretical guarantees; however they becomes intractable in high-dimensional real-world applications. The third approach is grounded in the success of iLQR. It is scalable, but it cannot handle constraints. Finally, the iterative best response algorithm is a heuristic approach with unknown convergence properties, and it can suffer from stability and tractability issues. 

We propose ALGAMES (Augmented Lagrangian GAME-theoretic Solver), a solver that handles trajectory optimization problems with multiple actors and general nonlinear state and input constraints. We evaluate our solver in the context of autonomous driving on scenarios involving numerous vehicles such as ramp merging, overtaking, and lane changing. We present simulation and timing results demonstrating the speed and the ability of the solver to produce efficient, safe, and natural autonomous behaviors. 

The main results obtained demonstrating ALGAMES performance are presented in this short video. 
[![ALGAMES](https://img.youtube.com/vi/ZvaVNvw5fYw/1.jpg)](https://www.youtube.com/watch?v=ZvaVNvw5fYw "ALGAMES")

The code for ALGAMES is made available on RexLab's GitHub [ALGAMES.jl](https://github.com/RoboticExplorationLab/ALGAMES.jl.git).

The paper is available at [ALGAMES](https://rexlab.stanford.edu/papers/ALGAMES.pdf).

![Nash equilibrium strategies obtained with ALGAMES on a ramp merging scenario.](/img/ramp_merging.gif)

![Nash equilibrium strategies obtained with ALGAMES on a lane changing scenario.](/img/lane_changing.gif)

![Nash equilibrium strategies obtained with ALGAMES for an overtaking maneuver.](/img/overtaking.gif)

