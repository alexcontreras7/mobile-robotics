 

|      | Assignment 3: |
| ---- | ------------- |
|      |               |

| Using the code supplied in https://github.com/venki666/RomiPi |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |
|                                                              | a) Download the code in Arduino code in https://github.com/venki666/RomiPi/tree/master/Arduino/Romi-RPi-I2CSlave (Links to an external site.) to your robot controller. |
|                                                              |                                                              |
|                                                              | b) Setup your ROS environment and add the ROS related folders in your catkin workspace. |
|                                                              |                                                              |
|                                                              | c) Execute the commands $ roslaunch romipi_astar romipi_astar_node.launch in one terminal and $ roslaunch romipi_teleop romipi_teleop_key.launch in another terminal. |
|                                                              |                                                              |
|                                                              | d) Record the video and screenshots of the assignment.       |
|                                                              |                                                              |
|                                                              | e) Use markup file to describe the process and upload the third Assignment on your private github repository. |
|                                                              |                                                              |
|                                                              | In this assignment we had to get ROS on our VM and get a prebuitl image of ROS on our raspberry pi and then run the code given to us using the commands above. |

## Get ROS onto Raspberry PI

- Download the zip found on https://yadi.sk/d/YfLc4stnCBljTA

- Extract previous zip

- Write image onto SD card by selecting the installed image as the operating system

- Insert SD card reader into PI and plug PI into a monitor

- Enable ssh by connecting in to the PI

- Enable wifi onto the PI

- Restart the PI

- ssh into PI

  ## Do the following onto your PI

- mkdir catkin_ws

- cd catkin_ws

- source /opt/ros/melodic/setup.bash

- mkdir src

- Install romipi_astar and rompi_teleop folders

- Move previous folders onto directory src using winSCp

- catkin_make (in catkin_ws directory)

- source devel/setup.bash

- Downloaded the following code on  https://github.com/venki666/RomiPi/tree/master/Arduino/Romi-RPi-I2CSlave 

- roslaunch romipi_astar romipi_astar.launch

- The code should now allow you to control your romi board through your PI