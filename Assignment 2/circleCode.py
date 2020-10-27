# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

motor_delay_s = 5.0
forward_speed_m_s = 0.25
stop_speed_m_s = 1.25
romi = AStar()

# int main()
# turn off all LEDs
romi.leds(False,False,False)
romi.pixels(0,0,0)
print("Displaying Circle Code")
var = input("Press s/S to stop and any key to continue: ") #input
while var != "s" and var != "S":
	currentTime = time.time()
	nextTime = currentTime + motor_delay_s
	while currentTime < nextTime: #loops for prev time delay
		romi.twist(forward_speed_m_s, stop_speed_m_s) # makes a circle
 		currentTime = time.time()
	romi.twist(0.0, 0.0) # stop
	var = input("Press s/S to stop and any key to continue: ") #input

