# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

motor_delay_s = 2.2
forward_speed_m_s = 0.25
stop_speed_m_s = 0.0
romi = AStar()

# int main()
# turn off all LEDs
romi.leds(False,False,False)
romi.pixels(0,0,0)

print("Displaying Square Code")
var = input("Press s/S to stop and any key to continue: ") #input
while var != "s" and var != "S":
# twist format is forward vector, rotation vector
# moves in square
    for i in range(4):
        currentTime = time.time()
        nextTime = currentTime + motor_delay_s # next time 
        while currentTime < nextTime:  # loops for prev time
            romi.twist(forward_speed_m_s, stop_speed_m_s) #go forward
            currentTime = time.time()

        romi.twist(stop_speed_m_s, stop_speed_m_s) # stop
        currentTime = time.time()
        nextTime = currentTime + (motor_delay_s / 2.0)
        while currentTime < nextTime:  # loops for prev time
            romi.twist(stop_speed_m_s, 3.14159265358979323846/2) #turns
            currentTime = time.time()
        romi.twist(stop_speed_m_s, stop_speed_m_s)    # stop
    var = input("Press s/S to stop and any key to continue: ") #input