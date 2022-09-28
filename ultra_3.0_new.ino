#include <NewPing.h>
int distance;
int pre;
NewPing sonar (10,11,18);
void setup() {
 Serial.begin(9600);
 delay(50);
}
void loop(){
  pre = map(sonar.ping_cm(), 12, 0, 0, 100);
Serial.print("The percentage of water  is:");
Serial.println(pre);//(sonar.ping_cm());
  delay(1000);
}

