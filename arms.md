# Getting Started with UR3e Robot Arms

Our lab contains two UR3e robot arms, each bolted in place on its own table.

The arms can be controlled either by [URScript](https://www.universal-robots.com/developer/urscript/), the Universal Robots in-house scripting language, or through the [ROS2 driver](https://docs.universal-robots.com/Universal_Robots_ROS_Documentation/index.html), consisting of a C++ API and related libraries. It is also possible to control the arm using a Python ROS2 system by publishing messages using the Universal Robots message format.

URScript is somewhat limited, so the rest of this guide will focus on ROS2 development.

## Installation


### Simulator

It is a good idea to design your programs in simulation first, before moving to the industrial robot arm. 
