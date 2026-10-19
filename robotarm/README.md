# UR3E arm Getting Started

Our lab contains two UR3e robot arms, each bolted in place on its own table.

[The official documentation for using Universal Robot arms with ROS2 is
here.](https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/)

If you *really* hate ROS, there is a standalone C++ client library also
described at that link. If you're in the robotics class, you should use ROS.

## Setup

In this folder, we have a `pixi.toml` file to make install and usage easier.
Feel free to copy this file into your own project as a starting point.

To install pixi, and set up the environment:

``` bash
curl -fsSL https://pixi.sh/install.sh | sh
pixi install
```

The example commands below will launch ROS nodes; to kill the node, press
`CTRL+C` in the terminal where the node was launched.


## Starting Driver

Whether using simulation or the real robot, you'll need to launch the official
Universal Robots ROS2 driver, which sets the robot arm up
to listen for ROS2 messages:

``` bash
pixi run driver
```

## Simulation

It is always best to test out programs in simulation before trying on the actual
hardware. This command will launch a visualizer (RViz) containing a model of
our robot arm, which can be controlled with the same exact ROS messages that the
hardware uses.

``` bash
pixi run mock
```

To run a full physics-based simulator (Gazebo) with the robot arm, run:

```bash
pixi run sim
```

## Test the joint trajectory controller

To actually get the robot to move, you need to use a controller. There are
various different controllers, which you can read about [in the
docs](https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_robot_driver/ur_controllers/doc/index.html).


The following command will launch a joint trajectory controller. You may need to set the arm into its "up" position before running this.
THIS WILL CAUSE THE ROBOT TO MOVE: if using the physical robot, make sure the workspace is clear of humans
and other obstacles before running. This will also work with a simulated robot.

``` bash
pixi run test
```

This command uses [this launch file](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver/blob/jazzy/ur_robot_driver/launch/test_scaled_joint_trajectory_controller.launch.py) and [this configuration file](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver/blob/jazzy/ur_robot_driver/config/test_goal_publishers_config.yaml).

## Launching MoveIt

The primary software we use for performing motion planning with the arms is
[MoveIt](https://moveit.picknik.ai/main/index.html). MoveIt includes a
graphical user interface for planning actions, as well as Python and C++ APIs.
The C++ API is more developed and complete than the Python API, but most basic
things can be done in python.

Tip: You must let MoveIt know that the table exists, otherwise it will attempt to path through it.
The simplest way to do this is to go to the scene objects tab, add a box of size (2.0, 2.0, 0.01)
then offset its position by (0, 0, -0.01), finally press publish to add it to the scene.

To launch MoveIt using our Pixi package:

``` bash
pixi run moveit
```

## Running on Robot Hardware

To use the robot arms, you must plug the ethernet cable from the robot arm into
the nearest desktop computer. You must then switch network profiles, in the
top-right corner of the screen click the "Network/System menu", then "Wired",
then select the option that looks like "UR3*".

Make sure the robot arm is turned on and in remote control mode (you switch
modes on the teach pendant; you should be trained in-person on this process
and related safety considerations, reach out to a professor or TA if not).
