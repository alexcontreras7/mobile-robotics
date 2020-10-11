#include <Romi32U4.h>

Romi32U4Motors motors;
Romi32U4ButtonA buttonA;

void setup() {

  buttonA.waitForButton();

  delay(2000);

}

void loop() {

  for(int i = 0; i < 4; i++){
    //go striaght 
    motors.setSpeeds(300,300);
    delay(500);
    for(int speed = 300; speed > 0; speed--){
      motors.setSpeeds(speed,speed);
      delay(1.7);
    }

    //stop and turn
    motors.setSpeeds(0,0);
    delay(500);
    motors.setRightSpeed(110);
    delay(1000);
    motors.setRightSpeed(0);
    delay(500);
  }
  
  while(1){    
  }


}
