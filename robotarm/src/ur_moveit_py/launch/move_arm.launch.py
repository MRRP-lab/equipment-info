import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
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
    my_package_share = get_package_share_directory('ur_moveit_py')
    ur_description_share = get_package_share_directory('ur_description')
    
    # Process Robot Description (URDF)
    xacro_file = os.path.join(ur_description_share, 'urdf', 'ur.urdf.xacro')
    robot_description_config = xacro.process_file(
        xacro_file, mappings={'name': 'ur', 'ur_type': 'ur3e', 'safety_limits': 'true'}
    )
    robot_description = {'robot_description': robot_description_config.toxml()}

    # Process SRDF
    srdf_xacro_file = os.path.join(my_package_share, 'srdf', 'ur.srdf.xacro')
    semantic_description_config = xacro.process_file(srdf_xacro_file, mappings={'name': 'ur', 'tf_prefix': ''})
    robot_description_semantic = {'robot_description_semantic': semantic_description_config.toxml()}

    # Load Configurations
    # kinematics
    kinematics_yaml = load_yaml('ur_moveit_py', 'config/kinematics.yaml')
    robot_description_kinematics = {'robot_description_kinematics': kinematics_yaml}

    # joint limits
    raw_joint_limits_yaml = load_yaml('ur_description', 'config/ur3e/joint_limits.yaml')
    
    # Extract the inner contents directly so the joints sit at the top level
    if raw_joint_limits_yaml and 'joint_limits' in raw_joint_limits_yaml:
        joint_limits_data = raw_joint_limits_yaml['joint_limits']
    else:
        joint_limits_data = raw_joint_limits_yaml

    # Package directly under the required MoveIt parameter block
    robot_description_planning = {'robot_description_planning': {
        'joint_limits': joint_limits_data
        }
    }

    # OMPL (default planner)
    moveit_py_yaml = {
        'planning_pipelines': {
            'pipeline_names': ['ompl'],
        },
        'ompl': {
            'planning_plugin': 'ompl_interface/OMPLPlanner',
            'request_adapters': """default_planner_request_adapters/AddTimeOptimalParameterization default_planner_request_adapters/FixWorkspaceBounds default_planner_request_adapters/FixStartStateBounds default_planner_request_adapters/FixStartStateCollision default_planner_request_adapters/FixStartStatePathConstraints""",
            'start_state_max_bounds_error': 0.1,
        },
        'plan_request_params': {
            'planning_pipeline': 'ompl',
            'planner_id': 'RRTConnectkConfigDefault',
            'planning_time': 10.0,
            'planning_attempts': 5,
            'max_velocity_scaling_factor': 0.2,
            'max_acceleration_scaling_factor': 0.2,
        }
    }

    # Merge your custom profile values safely if they exist
    ompl_profiles = load_yaml('ur_moveit_py', 'config/ompl_planning.yaml')
    if ompl_profiles:
        if 'ompl' in ompl_profiles:
            moveit_py_yaml['ompl'].update(ompl_profiles['ompl'])
        else:
            moveit_py_yaml['ompl'].update(ompl_profiles)

    # controllers
    # add custom controllers here if desired
    moveit_controllers_dict = load_yaml('ur_moveit_py', 'config/moveit_controllers.yaml')

    # Launch the custom python script
    move_arm_node = Node(
        package='ur_moveit_py',
        executable='move_arm',
        name='ur3e_moveit_py_node',  # Must match the node_name inside your move_arm.py script!
        output='screen',
        parameters=[
            robot_description,
            robot_description_semantic,
            robot_description_kinematics,
            robot_description_planning, 
            moveit_py_yaml,
            moveit_controllers_dict,
            {'use_sim_time': True},
        ]
    )

    return LaunchDescription([move_arm_node])

