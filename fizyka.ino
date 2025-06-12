#include <avr/io.h>



void setup() {
  Serial.begin(9600);
  delay(5000);  // give you time to open the Serial Monitor

}
const int ldrPins[2] = {A0, A1};


void loop() {
  unsigned long ts = millis();
  Serial.print(ts);
  for (int i = 0; i < 3; i++) {
    int raw = analogRead(ldrPins[i]);
    Serial.print(',');
    Serial.print(raw);
  }
  Serial.println();
  delay(10);
}
