# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

motor_delay_s = 1.0
forward_speed_m_s = 0.25
stop_speed_m_s = 0.0
romi = AStar()

# int main()
# turn off all LEDs
romi.leds(False,False,False)
romi.pixels(0,0,0)

print("Displaying Square Code")
var = input("Press s/S to stop and any key to continue: ")
while var != "s" and var != "S":
# twist format is forward vector, rotation vector
    for i in range(4):
        currentTime = time.time()
        nextTime = currentTime + motor_delay_s
        while currentTime < nextTime:  
            romi.twist(forward_speed_m_s, stop_speed_m_s)
            currentTime = time.time()

        romi.twist(stop_speed_m_s, stop_speed_m_s)
        currentTime = time.time()
        nextTime = currentTime + (motor_delay_s / 2)
        while currentTime < nextTime:      
            romi.twist(stop_speed_m_s, 3.14159265358979323846/2)
            currentTime = time.time()
        romi.twist(stop_speed_m_s, stop_speed_m_s)    
    var = input("Press s/S to stop and any key to continue: ")
   