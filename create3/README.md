# iRobot Create3 Quick Start

The iRobot Create3's are one of our easier to configure and set-up bots in the lab. Their documentation can be found here: https://iroboteducation.github.io/create3_docs/

# Connecting to a Bot.
The best way to connect to the Create3's for our lab is over WiFi. To initially setup the robot for WiFi, we have to connect to its hot spot. This is done by:

- Plugging the robot into one of the docking stations. It should turn on by itself and have a glowing white halo around the power button.
- Pressing the two smaller buttons on either side, holding them down. This should make a noise and turn the halo blue.
- You can now connect to the hot spot. It should be labeled Create-XXXX in your WiFi manager. The IP address for the bot is http://192.168.10.1
- Go to the 'Connect' tab in the webpage.
- You can set the WiFi here to the lab's WiFi. Make sure it is robo_wifi and not robo_wifi_5G. Ask one of the lab people for the password.
  - Important if multiple groups are using Create3s: You have to setup a ROS2 namespace for your bot. Call it what you want, but make sure that it is distinct from any other group's. If you don't do this, you will end up writing over each other's topics. Which is not good.
- Once it is connected to the WiFi you will lose access to the webpage. If your computer is also connected to the WiFi, you will have access to the bot through ROS2.
- You can verify that you are properly connected to the bot by running "ros2 topic list" on your computer. You should see a list of topics including:
  - /battery_state
  - /cmd_audio (Play notes through the speaker)
  - /cmd_lightring (Change color of bot's ring_
  - /cmd_vel (Command velocities to the reference frame)
  - /dock
  - /hazard_detection
  - /imu
  - /interface_buttons
  - /ir_intensity
  - /ir_opcode
  - /kidnap_status
  - /mobility_monitor/transition_event
  - /mouse
  - /odom
  - /parameter_events
  - /robot_state/transition_event
  - /rosout
  - /slip_status
  - /static_transform/transition_event
  - /stop_status
  - /tf
  - /tf_static
  - /wheel_status
  - /wheel_ticks
  - /wheel_vels
# How to do basic controls of the bot
The robot is controlled by publishing geometry_msgs/msg/Twist messages to the cmd_vel topic. The robot will continuously execute the last received message for the topic until a fixed timeout or a new command s received. This is a very primitive approach and there are better options available.
## Driving using Actions
Create3s come with a variety of Actions and Action Servers for autonomous movement. You can command the robot to drive at a fixed angle by sending a goal to the /drive_arc server.

- ros2 action send_goal /drive_arc irobot_create_msgs/action/DriveArc "{angle: 1.57,radius: 0.3,translate_direction: 1,max_translation_speed: 0.3}"

You can also command the bot to drive a certain distance by sending a goal to the /drive_distance server.

- ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 0.5,max_translation_speed: 0.15}"

This one's especially useful, you can command the bot to move to a specific odometry position. (This, combined with a subscription to the /odom topic can give you reliable fine-tuned control).

- ros2 action send_goal /navigate_to_position irobot_create_msgs/action/NavigateToPosition "{achieve_goal_heading: true,goal_pose:{pose:{position:{x: 1,y: 0.2,z: 0.0}, orientation:{x: 0.0,y: 0.0, z: 0.0, w: 1.0}}}}"

Less important, but you can also specific a heading for the robot

- ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 1.57,max_rotation_speed: 0.5}"

## Wall Following
You are able to command the bot to wall follow. It will move around its general area until it finds a wall. Once it does, it will follow along the wall on the side specified. (1 = left side, -1 = right side)

- ros2 action send_goal /wall_follow irobot_create_msgs/action/WallFollow "{follow_side: 1, max_runtime: {sec: 1, nanosec: 0}}"

# Final Notes
Not everything that is available on the Create3 is covered here, there's plenty more functionality that you can program into these things. Check the docs to see if there's a behavior that you want already available through the ROS2 API.

Happy hacking!
