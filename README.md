# AMR_project  
## Designing a two-wheeled differential drive robot to navigate a given maze.

## ddr 
It contains the urdf for the differential drive robot, launch files, default rviz configuration, maze world file and the map generated from it.

## ddr_nav
It contains the send goal script which makes the robot move to the end of the maze and the amcl launch file.

## Working 
Individual launch files are given in each folder for specific purposes. Example : original_spawn.launch just spawns the bot into an empty world and so on..

IF you want to go to the main purpose, just launch amcl, it will launch gazebo,rviz,map_server and amcl for you. Change the x,y values in the send_goal.py
to change end goal to navigation stack.

