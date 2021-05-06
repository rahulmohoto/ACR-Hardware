//int analogPin = A0; // potentiometer wiper (middle terminal) connected to analog pin 3
//                    // outside leads to ground and +5V
//int val = 0;  // variable to store the value read
//
//void setup() {
//  Serial.begin(9600);           //  setup serial
//}
//
//void loop() {
//  val = analogRead(analogPin);  // read the input pin
//  Serial.println(val);          // debug value
//}

int analogInput = A0;
float vout = 0.0;
float vin = 0.0;
float R1 = 30000.0; // resistance of R1 (100K) -see text!
float R2 = 10000.0; // resistance of R2 (10K) - see text!
int value = 0;

void setup(){
    Serial.begin(9600); 
   pinMode(analogInput, INPUT);
}

void loop(){
   // read the value at analog input
   value = analogRead(analogInput);
//   Serial.println(value);
   vout = (value * 5) / 1024.0; // see text
   vin = vout / (R2/(R1+R2)); 
   Serial.println(vin);
//   if (vin<0.09) {
//   vin=0.0;//statement to quash undesired reading !
delay(500);
} 
