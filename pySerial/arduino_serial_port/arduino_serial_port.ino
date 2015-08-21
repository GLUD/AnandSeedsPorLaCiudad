String readString;

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {
        // send data only when you receive data:
        while (Serial.available()) {
          delay(3);  //delay to allow buffer to fill
          if (Serial.available() >0) {
            char c = Serial.read();  //gets one byte from serial buffer
            readString += c; //makes the string readString
          }
        }
        if(readString.length()>0){
          Serial.print("hums=1000&huma=10000&tems=50.3&tema=20.2");
          Serial.println(readString);
          readString="";
        }
}
