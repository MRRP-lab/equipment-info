import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)
    try:
        with open(absolute_file_path, "r") as file:
            return yaml.safe_load(file)
    except EnvironmentError:
        return None


def generate_launch_description():
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="true",
        description="Use simulation clock if true",
    )
    use_sim_time = LaunchConfiguration("use_sim_time")

    pkg_share = get_package_share_directory("ur_moveit_py")

    # Build base MoveIt configs (URDF, SRDF, kinematics, joint limits, controllers)
    moveit_config = (
        MoveItConfigsBuilder("ur", package_name="ur_moveit_config")
        .robot_description(
            mappings={
                "name": "ur",
                "ur_type": "ur3e",
                "safety_limits": "true",
            }
        )
        .robot_description_semantic(
            file_path=os.path.join(pkg_share, "srdf", "ur.srdf.xacro"),
            mappings={"name": "ur", "tf_prefix": ""},
        )
        .robot_description_kinematics(
            file_path=os.path.join(pkg_share, "config", "kinematics.yaml")
        )
        .trajectory_execution(
            file_path=os.path.join(pkg_share, "config", "moveit_controllers.yaml")
        )
        .to_moveit_configs()
    )

    # Convert to dictionary and override planning_pipelines for MoveItPy's expected schema
    moveit_params = moveit_config.to_dict()
    moveit_params["planning_pipelines"] = {
        "pipeline_names": ["ompl"],
    }
    moveit_params["ompl"] = {
        "planning_plugin": "ompl_interface/OMPLPlanner",
        "request_adapters": (
            "default_planner_request_adapters/AddTimeOptimalParameterization "
            "default_planner_request_adapters/FixWorkspaceBounds "
            "default_planner_request_adapters/FixStartStateBounds "
            "default_planner_request_adapters/FixStartStateCollision "
            "default_planner_request_adapters/FixStartStatePathConstraints"
        ),
        "start_state_max_bounds_error": 0.1,
    }

    # Default plan request parameters required by MoveItPy
    moveit_py_plan_params = {
        "plan_request_params": {
            "planning_pipeline": "ompl",
            "planner_id": "RRTConnectkConfigDefault",
            "planning_time": 10.0,
            "planning_attempts": 5,
            "max_velocity_scaling_factor": 0.2,
            "max_acceleration_scaling_factor": 0.2,
        }
    }

    # Merge your custom OMPL planner profiles if present
    ompl_profiles = load_yaml("ur_moveit_py", "config/ompl_planning.yaml")
    if ompl_profiles:
        if "ompl" in ompl_profiles:
            moveit_params["ompl"].update(ompl_profiles["ompl"])
        else:
            moveit_params["ompl"].update(ompl_profiles)

    move_arm_node = Node(
        package="ur_moveit_py",
        executable="move_arm",
        name="ur3e_moveit_py_node",
        output="screen",
        parameters=[
            moveit_params,
            moveit_py_plan_params,
            {"use_sim_time": use_sim_time},
        ],
    )

    return LaunchDescription([
        use_sim_time_arg,
        move_arm_node,
    ])
