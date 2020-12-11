```
Assignment 2:

Using the code supplied in https://github.com/venki666/CpE476_demos/tree/master/Arduino/Romi-RPi-I2CSlave

a) Develop the code to move the Romi Robot in a circle using commands issued by the RPi

b) Develop the code to move the Romi Robot in a square/rectangle using commands issued by the RPi

In my code i used the twist function and put it inside a time loop using the built in .time() function.
The only thing my code required is figuring out how long of a delay and the angles I should use to make 
a complete square/circle.
```

## Install and test Raspbian on Raspberri Pi W/4/3

- Download the latest version of Raspberry Pi Imager and install it.
- Connect an SD card reader with the SD card inside.
- Open Raspberry Pi Imager and choose the required OS from the list presented.
- Choose the SD card you wish to write your image to.
- Review your selections and click 'WRITE' to begin writing data to the SD card. 
- After the Raspberry Pi Imager is on your SD card reader, insert the SD card reader into the Raspberry PI
- Connect the Raspberry to a external monitor 
- From there you can login into your pi and create a password
- Sign into your local wifi
- This should enable your ssh and now you must restart your pi
- Now that your ssh is enabled you can ssh into your pi

## Setting up RPI - Romi 32U4 Control Board

Create a module configuration file:

```
sudo nano /etc/modprobe.d/8192cu.conf
```

and add the following lines:

```
#Disable power management
options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
```

After setting up Wi-Fi, enable I²C on your Raspberry Pi by running

```
sudo raspi-config
```

and selecting the option within the “Advanced” or “Interfacing Options” menu. By default, I²C runs at 100 kHz, but you can safely increase that rate to 400 kHz and get a much faster communications channel between the boards. To increase the speed, edit the configuration file:

```
sudo nano /boot/config.txt
```

At the end, add the line:

dtparam=i2c_arm_baudrate=400000

## Getting Arduino Libraries Onto Raspberry PI

- Download winSCP

- Download the Arduino Libraries you want from github

- Transfer these folders into your PI using winSCP

- Move the code on https://github.com/venki666/CpE476_demos/tree/master/Arduino/Romi-RPi-I2CSlave onto your PI

  ## Editing Code Downloaded Prior

  In my code i used the twist function and put it inside a time loop using the built in .time() function.
  The only thing my code required is figuring out how long of a delay and the angles I should use to make 
  a complete square/circle.