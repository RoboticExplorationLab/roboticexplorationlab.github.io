---
title: Motion Reconstruction and Imitation from Monocular Videos

description: |
  An end-to-end motion transfer framework from monocular videos to legged robots.

people:
  - john
  - shuo
  - arun
  - zac 

layout: project
image: "/img/video_imitation/dog_reach_compiled.gif"
last-updated: 2023-02-09
---

We present SLoMo: a first-of-its-kind framework for transferring skilled motions from casually captured “in-
the-wild” video footage of humans and animals to legged robots. SLoMo works in three stages: 1) synthesize a physically plausible reconstructed key-point trajectory from monocular videos; 2) optimize a dynamically feasible reference trajectory for the robot offline that includes body and foot motion, as well as a contact sequence that closely tracks the key points; 3) track the reference trajectory online using a general-purpose model-predictive controller on robot hardware. Traditional motion imitation for legged motor skills often requires expert animators, collaborative demonstrations, and/or expensive motion-capture equipment, all of which limits scalability. Instead, SLoMo only relies on easy-to-obtain videos, readily available in online repositories such as YouTube. It converts videos into motion primitives that can be executed reliably by real-world robots. We demonstrate our approach by transferring the motions of cats, dogs, and humans to example robots including a quadruped (on hardware) and a humanoid (in simulation).

Check our websites: 
* [PPR](https://gengshan-y.github.io/ppr/)
* [SLoMo](https://slomo-www.github.io/website/)