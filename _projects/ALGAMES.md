---
title: Dynamic Games Solver

description: |
  Developing a fast and robust solver for constrained dynamic games aimed at identifying Nash equilibrium strategies. 

people:
  - zac
  - simon

layout: project
image: "/img/ALGAMES/algames_banner.gif"
last-updated: 2020-03-04
---

Dynamic games are an effective paradigm for dealing with the control of multiple interacting actors. We introduces [ALGAMES](https://github.com/RoboticExplorationLab/ALGAMES.jl.git) (Augmented Lagrangian GAME-theoretic Solver), a solver that handles trajectory optimization problems with multiple actors and general nonlinear state and input constraints. Its novelty resides in satisfying the first order optimality conditions with a quasi-Newton root-finding algorithm and rigorously enforcing constraints using an augmented Lagrangian formulation. We evaluate our solver in the context of autonomous driving on scenarios with a strong level of interactions between the vehicles. We assess the robustness of the solver using MonteCarlo simulations. It is able to reliably solve complex problems like ramp merging with three vehicles three times faster than a state-of-the-art DDP-based approach. A model predictive control (MPC) implementation of the algorithm demonstrates real-time performance on complex autonomous driving scenarios with an update frequency higher than 60 Hz.



<!-- The main results obtained demonstrating ALGAMES performance are presented in this short video. 
[![ALGAMES](/img/algames_video.png)](https://www.youtube.com/watch?v=ZvaVNvw5fYw "ALGAMES") -->

The code for ALGAMES is made available on RexLab's GitHub [ALGAMES.jl](https://github.com/RoboticExplorationLab/ALGAMES.jl.git).

The paper is available at [ALGAMES](https://rexlab.stanford.edu/papers/ALGAMES.pdf).

<!-- ![Nash equilibrium strategies obtained with ALGAMES on a ramp merging scenario.](/img/ramp_merging.gif) -->

<!-- ![Nash equilibrium strategies obtained with ALGAMES on a lane changing scenario.](/img/lane_changing.gif) -->

![Nash equilibrium strategies obtained with ALGAMES for an overtaking maneuver.](/img/ALGAMES/overtaking_landscape.gif)

