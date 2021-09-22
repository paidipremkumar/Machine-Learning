const int LOAD1=11;
const int LOAD2=10;
String readString;
void setup() {
 pinMode(LOAD1,OUTPUT);
 pinMode(LOAD2,OUTPUT);
 pinMode(9,INPUT);
 Serial.begin(38400);
}

void loop() {
  while(Serial.available()){
    delay(50);
    char c=Serial.read();
    readString+=c;
  }
  if(readString.length()>0){
    Serial.println(readString);
  
  if(readString=="ONE"){
    digitalWrite(LOAD1,HIGH);
    delay(50);
  }
   if(readString=="TWO"){
    digitalWrite(LOAD1,LOW);
    delay(50);
  }
   if(readString=="THREE"){
    digitalWrite(LOAD2,HIGH);
    delay(50);
  }
   if(readString=="FOUR"){
    digitalWrite(LOAD2,LOW);
    delay(50);
  }
   if(readString==""){
    digitalWrite(LOAD1,HIGH);
    digitalWrite(LOAD2,HIGH);
    delay(50);
  }
  if(readString =="ALL LOADS OFF"){
    digitalWrite(LOAD1,LOW);
    digitalWrite(LOAD2,LOW);
    delay(50);
  }
  }
  readString="";
}
