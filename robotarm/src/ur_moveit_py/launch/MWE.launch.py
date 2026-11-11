from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder
from ament_index_python.packages import get_package_share_directory
import os
import xacro
import yaml

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)
    try:
        with open(absolute_file_path, "r") as file:
            return yaml.safe_load(file)
    except EnvironmentError:
        return None

def generate_launch_description():

    # handle environment
    my_package_share = get_package_share_directory("ur_moveit_py")
    ur_description_share = get_package_share_directory("ur_description")

    # load basic robot model from ur_description (cloned locally to help pixi env work properly)
    xacro_file = os.path.join(ur_description_share, 'urdf', 'ur.urdf.xacro')
    robot_description_config = xacro.process_file(
        xacro_file, mappings={'name': 'ur', 'ur_type': 'ur3e', 'safety_limits': 'true'}
    )
    robot_description = {'robot_description': robot_description_config.toxml()}

    # load semantic robot model from location in this package, ur_moveit_py
    srdf_xacro_file = os.path.join(my_package_share, 'srdf', 'ur.srdf.xacro')
    semantic_description_config = xacro.process_file(
        srdf_xacro_file,
        mappings={
            'name': 'ur',
            'tf_prefix': '',
        }
    )
    robot_description_semantic = {'robot_description_semantic': semantic_description_config.toxml()}

    # Kinematics Plugin Configuration from this package
    kinematics_yaml = load_yaml('ur_moveit_py', 'config/kinematics.yaml')
    robot_description_kinematics = {'robot_description_kinematics': kinematics_yaml}

    # Planning Pipeline Configuration (OMPL) from this package
    ompl_planning_yaml = {
        'planning_pipelines': ['ompl'],
        'default_planning_pipeline': 'ompl',
        'ompl': {
            'planning_plugin': 'ompl_interface/OMPLPlanner',
            'request_adapters': """default_planner_request_adapters/AddTimeOptimalParameterization default_planner_request_adapters/FixWorkspaceBounds default_planner_request_adapters/FixStartStateBounds default_planner_request_adapters/FixStartStateCollision default_planner_request_adapters/FixStartStatePathConstraints""",
            'start_state_max_bounds_error': 0.1,
        }
    }
    ompl_profiles = load_yaml('ur_moveit_py', 'config/ompl_planning.yaml')
    if ompl_profiles:
        ompl_planning_yaml['ompl'].update(ompl_profiles)

    # Load your standard MoveIt Controller YAML definitions directly
    # Add new controllers in moveit_controllers.yaml if needed
    moveit_controllers_dict = load_yaml('ur_moveit_py', 'config/moveit_controllers.yaml')

    # MoveIt node
    run_move_group_node = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen',
        parameters=[
            robot_description,
            robot_description_semantic,
            robot_description_kinematics,
            ompl_planning_yaml,
            moveit_controllers_dict,
            {'use_sim_time': True},  # Set to False when connecting to physical ur3e hardware
        ]
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters = [robot_description, {'use_sim_time': True}]
    )

    nodes_to_start = [
        robot_state_publisher,
        run_move_group_node,
    ]

    return LaunchDescription(nodes_to_start)
