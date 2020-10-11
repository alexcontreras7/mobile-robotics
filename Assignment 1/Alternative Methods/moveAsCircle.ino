#include <Romi32U4.h>

Romi32U4Motors motors;
Romi32U4ButtonA buttonA;

void setup() 
{
    buttonA.waitForButton(); //Waut for user input
    delay(2000);
}

void loop() 
{

      motors.setSpeeds(300,180);
      delay(2100);   
    
    //Stop
    motors.setSpeeds(0,0);
 

}
