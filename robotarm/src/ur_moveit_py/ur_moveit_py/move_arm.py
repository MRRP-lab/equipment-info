#!/usr/bin/env python3
import time
import rclpy
from rclpy.logging import get_logger
from moveit.planning import MoveItPy, PlanRequestParameters
from geometry_msgs.msg import PoseStamped


def main(args=None):
    # Initialize ROS 2 context
    rclpy.init()
    logger = get_logger("ur_moveit_py_test")
    logger.info("Initializing MoveItPy Node...")

    # set controller
    active_controllers = ["scaled_joint_trajectory_controller"]

    # Instantiate MoveItPy
    # This automatically processes the robot_description and parameters from the launch context
    ur3e = MoveItPy(node_name="ur3e_moveit_py_node")
    time.sleep(2.0) # give time for action client to connect to Gazebo

    # access the primary arm planning group
    arm = ur3e.get_planning_component("ur_manipulator")

    # Command a move to the 'home' pose first to ensure a known start state
    logger.info("Setting goal state to 'home'...")
    arm.set_start_state_to_current_state()
    arm.set_goal_state(configuration_name="home")

    logger.info("Planning trajectory to 'home'...")
    plan_to_home = arm.plan()

    if plan_to_home:
        logger.info("Executing movement to 'home'...")
        ur3e.execute(plan_to_home.trajectory, controllers=active_controllers)
    else:
        logger.error("Planning to 'home' failed!")

    # Plan and move to a Pose Goal defined on the end effector
    logger.info("Setting goal state to pose...")
    arm.set_start_state_to_current_state()

    pose_goal = PoseStamped()
    pose_goal.header.frame_id = "base_link"
    # Set a position and quaternion describing pose of tool in base frame
    # You can get this orientation in the MoveIt GUI with the following steps:
    # (expand field by clicking arrow on left of field name)
    # > Expand "MotionPlanning" on the top left sidebar in MoveIt
    # > Expand "Scene Robot" to see current robot state, or "Planned Path" to see goal state
    # > Expand "Links", and find "tool0"
    # > Expand "tool0"
    # Will see fields for position (x,y,z in meters) and orientation (x, y, z, w defining a quaternion)
    # You can also plan to a "robot state" defining joint angles; you can get
    # these from the real robot on the tablet while moving the robot in freedrive mode
    # Be careful of using the pose estimates on the tablet: need to convert units
    pose_goal.pose.orientation.x = -0.09
    pose_goal.pose.orientation.y = 0.99
    pose_goal.pose.orientation.z = 0.07
    pose_goal.pose.orientation.w = 0.02
    pose_goal.pose.position.x = -0.08
    pose_goal.pose.position.y = 0.45
    pose_goal.pose.position.z = 0.25
    arm.set_goal_state(pose_stamped_msg=pose_goal, pose_link="tool0")

    logger.info("Planning trajectory to pose...")
    plan_to_pose = arm.plan()

    if plan_to_pose:
        logger.info("Executing movement to pose goal...")
        ur3e.execute(plan_to_pose.trajectory, controllers=active_controllers)
        logger.info("Movement complete!")
    else:
        logger.error("Planning to pose failed!")

    # 6. Shutdown cleanly
    rclpy.shutdown()


if __name__ == "__main__":
    main()
