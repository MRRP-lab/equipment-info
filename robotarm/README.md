# UR3E arm setup

## Setup

Install pixi, and setup the environment:

``` bash
curl -fsSL https://pixi.sh/install.sh | sh
pixi install
```

## Launch the driver

``` bash
pixi run driver
```

> Make sure the robot arm is turned on and in remote control mode.

## Test the joint trajectory controller

``` bash
pixi run test
```

## Launch MoveIt

You must let MoveIt know that the table exists, otherwise it will attempt to path through it.
The simplest way to do this is to go to the scene objects tab, add a box of size (2.0, 2.0, 0.01)
then offset its position by (0, 0, -0.01), finally press publish to add it to the scene.

``` bash
pixi run moveit
```

# If you want to test with mock hardware

``` bash
pixi run mock
```