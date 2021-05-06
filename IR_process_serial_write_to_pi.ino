int analogInputRightIr = A5;
int analogInputLeftIr = A4;
unsigned long int waitTime=50;
int left_delay=25;
int right_delay=25;
int left_count=0;
int right_count=0;
int runTime = 25;

void setup() {
  Serial.begin(9600);
  pinMode(analogInputRightIr, INPUT);
  pinMode(analogInputLeftIr, INPUT);
}

void loop() {
  
  unsigned long int startTime=millis();
  while(millis()-startTime<=100){
    if(rightIrGotHit())
    right_count++;
    delayMicroseconds(10);
    
    if(leftIrGotHit())
    left_count++;
    delayMicroseconds(10);
  }
    
  if(abs(left_count-right_count)==2 && (left_count-right_count!=0)){
    left_count=0;
    right_count=0;
    forward();
  }
  if(left_count>right_count){
    left_count=0;
    right_count=0;
    left();
  }
  if(left_count<right_count){
    left_count=0;
    right_count=0;
    right();
  }
  
  stopp();
  
}
  
 boolean leftIrGotHit(){
  
  int PreValueLeftIr = analogRead(analogInputLeftIr);
  delayMicroseconds(left_delay);
  int PostValueLeftIr = analogRead(analogInputLeftIr);
  int pulseCount=0;
  unsigned long int startTime = millis();
  unsigned long int currentTime = millis();
  while(abs(startTime-currentTime)<=waitTime){
      if(abs(PreValueLeftIr - PostValueLeftIr)>30){
        pulseCount+=1;
//        Serial.println(pulseCount);
//        return;
      }
      int PreValueRightIr = analogRead(analogInputRightIr);
      delayMicroseconds(left_delay);
      int PostValueRightIr = analogRead(analogInputRightIr);
      currentTime = millis();
      if(pulseCount>=3){
//        Serial.println("Go Left");
        return true;
        }
    }
    return false;
 }

 boolean rightIrGotHit(){
  
  int PreValueRightIr = analogRead(analogInputRightIr);
  delayMicroseconds(right_delay);
  int PostValueRightIr = analogRead(analogInputRightIr);
  int pulseCount=0;
  unsigned long int startTime = millis();
  unsigned long int currentTime = millis();
  while(abs(startTime-currentTime)<=waitTime){
      if(abs(PreValueRightIr - PostValueRightIr)>30){
        pulseCount+=1;
//        Serial.println(pulseCount);
//        return;
      }
      int PreValueRightIr = analogRead(analogInputRightIr);
      delayMicroseconds(right_delay);
      int PostValueRightIr = analogRead(analogInputRightIr);
      currentTime = millis();
      if(pulseCount>=3){
//        Serial.println("Go Right");
        return true;
        }
    }
    return false;
    
  }

  void forward(){

  int countForward = 2;
  int nextSetupTime = 0;
  unsigned long int startTime=millis();
  while(millis()-startTime<=runTime){

    Serial.println("forward");
  
    if(rightIrGotHit())
    right_count++;
    
    if(leftIrGotHit())
    left_count++;
    
    if(abs(left_count-right_count)==2){
      nextSetupTime = 1*countForward++ ; 
      }
    }
    runTime -= nextSetupTime;
  }

  void left(){

  Serial.println("left");
  delayMicroseconds(10);
    
    }

  void right(){
    
  Serial.println("right");
  delayMicroseconds(10); 
    
    }

  void stopp(){

  Serial.println("stop");
    
    }

  

 
