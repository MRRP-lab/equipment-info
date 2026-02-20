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

## Test the joint trajectory controller

``` bash
pixi run test
```

## Launch MoveIt

``` bash
pixi run moveit
```

# If you want to test with mock hardware

``` bash
pixi run mock
```