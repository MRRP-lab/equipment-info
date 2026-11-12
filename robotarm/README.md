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


## Simulation

It is always best to test out programs in simulation before trying on the actual
hardware. This command will launch a physics-based simulator (Gazebo), as well as
a visualizer (RViz) containing a model of
our robot arm, which can be controlled with the same exact ROS messages that the
hardware uses.

``` bash
pixi run sim
```

## Control

The following pixi task will build your package, source your environment, and
spin up the ROS2 node defined in `src/ur_moveit_py/ur_moveit_py/move_arm.py`.
The robot arm should move from the home position by rotating one joint, then
will move back to home.

```bash
pixi run control-sim
```

You can leave the Gazebo simulator node running while you iterate on the python
script, re-running the script with the above command. This is because we use
`colcon build symlink-install` to build our package.

You may want to add a
"reset" command at the beginning of the script, because the script will pick
up from wherever the robot is in the simulator.

## Launching MoveIt GUI

The primary software we use for performing motion planning with the arms is
[MoveIt](https://moveit.picknik.ai/main/index.html). MoveIt includes a
graphical user interface for planning, as well as Python and C++ APIs.
The C++ API is more developed and complete than the Python API, but most
things can be done in python. The working example here is in python.

However, sometimes it's easier to use the GUI to prototype poses and plans
rather than spinning up the entire Gazebo simulator.

To launch MoveIt using our Pixi package:

``` bash
pixi run moveit
```

Tip: You must let MoveIt know that the table exists, otherwise it will attempt to path through it.
You should do this programmatically in either your python script or your launch
file, but to do this in the GUI, the simplest way to do this is to go to the scene objects tab, add a box of size (2.0, 2.0, 0.01)
then offset its position by (0, 0, -0.01), finally press publish to add it to the scene.


## Running on Robot Hardware

Once you have tested and validated your control code in simulation, including
checking there are no collisions with the table, you can run your code on the
robot arm.

Make sure the robot arm is turned on and in remote control mode (you switch
modes on the teach pendant; you should be trained in-person on this process
and related safety considerations, reach out to a professor or TA if not).

Make sure the area and table top are clear of humans and other fragile things.

Then you can run the control code on hardware with

```
pixi run control-hw
```

### End Effectors

[See this page for more information on end effectors for the robot arms](./end_effectors.md).
