 

|      | Assignment 1:                                                |
| ---- | ------------------------------------------------------------ |
|      |                                                              |
|      | Using the code supplied in https://github.com/venki666/CpE476_demos/tree/master/Arduino/Romi-NoRpi-Debug |
|      |                                                              |
|      | a) Develop the code to move the Romi Robot in a circle (you can use your own parameters) |
|      |                                                              |
|      | b) Develop the code to move the Romi Robot in a square/rectangle (you can use your own parameters) |

### Install Arduino IDE (latest) in Linux (host system)

Arduino integrated development environment (IDE) software @ [Arduino Software](http://arduino.cc/en/Main/Software). Start a clean install. Do not us the App version, use the zip version to install.

### Install Arduino Support Libraries

1. Romi32U4 library - Use the one provided in the class github.
2. Arduino library for interfacing with the LSM6DS33 accelerometer and gyro - [LSM6 library for Arduino](https://github.com/pololu/lsm6-arduino)
3. PID Library - [TimedPID](https://www.arduino.cc/reference/en/libraries/timedpid/)
4. Alternate PID - [PID_v1](https://github.com/br3ttb/Arduino-PID-Library/)
5. Timer Library -

### Test your Romi Control Board

Using built-in example codes test the Romi Controller Board - In Class demo

### Make Changes to preexisting code 

Using the code found in https://github.com/venki666/CpE476_demos/tree/master/Arduino/Romi-NoRpi-Debug create a code the makes the romi move in a circle 

This can be accomplished by  using the set twitst target command and moving the left wheel slower than the right to create a diameter.

Then create a code to move the romi in a square. This can be done by going straight then using pid to move the romi 90 degrees with a delay. Repeat this process 4 times to make a square.