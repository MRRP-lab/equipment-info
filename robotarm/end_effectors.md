# End Effectors

We have various end effectors for the robot arm, or you may want to design your own.

## Designing your Own End Effector

You may find one or both of these CAD models useful when designing your own end effector, at least for getting a model of the base plate that mounts to the ur3e robot arm:

[Sharpie holder](https://www.printables.com/model/259360-robot-spring-loaded-sharpie-end-effector-eoat-for-/files)

[Mount for camera](./ur3e-camera-holder.zip)

## Sharpie Holder

We have two of these
[sharpie holders](https://www.printables.com/model/259360-robot-spring-loaded-sharpie-end-effector-eoat-for-/files), and plenty of sharpies. There is a roll of paper in the supply cabinet (bottom of rightmost cabinet).

## Pneumatic Gripper

There is a pneumatic gripper. You must be trained in-person by Dr. Nilles or the TA to use the pneumatic gripper. Be aware it runs off an air compressor, which can be somewhat loud while it is reaching pressure.

The pneumatic gripper is wired to the UR control box, and can be controlled via the ROS2 link to the robot arm.

## Two-finger parallel plate gripper

We have a two-finger parallel plate gripper based on [this design](https://github.com/Evroc/Robotic-gripper). The gripper is powered and controlled by a USB cable that must be plugged into the host computer, but can then be controlled through ROS with rosserial as detailed on that repository README.
