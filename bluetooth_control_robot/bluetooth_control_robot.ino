#include<AFMotor.h>
AF_DCMotor front_motor(3,MOTOR12_8KHZ);
AF_DCMotor aft_motor(4,MOTOR12_8KHZ);
String readString;
void setup() {
 pinMode(13,OUTPUT);
 Serial.begin(9600);
 front_motor.setSpeed(250);
 aft_motor.setSpeed(250);
 pinMode(11,OUTPUT);

}

void loop() {
  int i=0;
  while(Serial.available()){
    delay(50);
    char c=Serial.read();
    readString+=c;
  }
  if(readString.length()>0){
    Serial.println(readString);
    if(readString=="FORWARD"){
    aft_motor.run(FORWARD);
    front_motor.run(FORWARD);
    delay(50);
    digitalWrite(11,HIGH);
  }
  if(readString=="BACKWARD"){
                               aft_motor.run(BACKWARD);
                               front_motor.run(BACKWARD);
                               delay(50);
  }
  if(readString=="LEFT"){
                         aft_motor.run(RELEASE);
                         front_motor.run(FORWARD);
                         delay(50);
  }
  if(readString=="RIGHT"){
                          aft_motor.run(FORWARD);
                          front_motor.run(RELEASE);
                          delay(50);
  }
  if(readString=="STOP"){
    aft_motor.run(RELEASE);
    front_motor.run(RELEASE);
    delay(50);
  }
  }
}
