# Routine commands
>> tensorboard --logdir runs
>> ros2 pkg create --build-type ament_python <package_name> -d rclpy
>> ros2 topic list
>> ros2 service list
>> ros2 action list
>> ros2 topic echo /scan

# f1tenth commands
>> ros2 launch f1tenth_gym_ros gym_bridge_launch.py

>> ros2 run teleop_twist_keyboard teleop_twist_keyboard
>> ros2 run f1tenth_gym_agent agent

# TD3 Commands
>> colcon build
>> ros2 launch <package_name> <launch_file_name>


# Map generation
In order to generate the map using Gazebo it is required to install these additional packages.
>> apt install ros-foxy-navigation2 ros-foxy-nav2-bringup ros-foxy-slam-toolbox ros-foxy-turtlebot3*

Below are the dependencies used by map generation procedure.
>> ros2 launch f1tenth_gym_agent agent.launch.py
or
>> ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

>> ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
>> ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
>> ros2 run rviz2 rviz2 -d /opt/ros/foxy/share/nav2_bringup/rviz/nav2_default_view.rviz
>> ros2 run teleop_twist_keyboard teleop_twist_keyboard

>> ros2 run turtlebot3_teleop teleop_keyboard

## Spawn the robot in the world
>> ros2 launch gazebo_ros gazebo.launch.py world:=agent.world 