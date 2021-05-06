import serial_read
import time
import motor
import RPi.GPIO as GPIO
import sonar
import RPi.GPIO as GPIO

enable = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(enable,GPIO.OUT)

def getMillis():    
    return int(round(time.time() * 1000))


GPIO.output(enable, GPIO.HIGH)
    
try:
    
    while(True):
        #print(type(data))
        motor.drive("p")
        startTime = getMillis()
        while(getMillis() - startTime <= 3000):
            #data = serial_read.readSerialData()
            sonar.read()
            motor.drive("p")
            time.sleep(0.1)
            if(sonar.middle<2):
                print("both sonar")
                motor.drive("s")
                time.sleep(0.35)
                motor.drive("p")
                time.sleep(0.01)
                motor.drive("a")
                time.sleep(0.08)
                
            elif(sonar.left<=10):
                motor.drive("p")
                print("sonar left")
                motor.drive("s")
                time.sleep(0.35)
                motor.drive("p")
                time.sleep(0.01)
                motor.drive("a")
                time.sleep(0.08)
        
            elif(sonar.right<=10):
                motor.drive("p")
                print("sonar right")
                motor.drive("s")
                time.sleep(0.35)
                motor.drive("p")
                time.sleep(0.01)
                motor.drive("d")
                time.sleep(0.08)
            
            elif(sonar.left_most<=10):
                motor.drive("p")
                print("sonar left most")
                motor.drive("s")
                time.sleep(0.3)
                motor.drive("p")
                time.sleep(0.01)
                motor.drive("a")
                time.sleep(0.08)
            
            elif(sonar.right_most<=10):
                motor.drive("p")
                print("sonar right most")
                motor.drive("s")
                time.sleep(0.3)
                motor.drive("p")
                time.sleep(0.01)
                motor.drive("d")
                time.sleep(0.08)
        
        GPIO.output(enable, GPIO.LOW)
        GPIO.output(enable, GPIO.HIGH)
        startTime = getMillis()
        while(getMillis() - startTime <= 1000):
            data = serial_read.readSerialData()
            stringData = data.rstrip()
            print(stringData)
        
        
            if(stringData=="forward"):
                motor.drive("w")
                time.sleep(0.1)
                #motor.drive("p")
                #print(data)
            elif(stringData=="left"):
                motor.drive("a")
                time.sleep(0.1)
                motor.drive("p")
                #print(data)
            elif(stringData=="right"):
                motor.drive("d")
                time.sleep(0.1)
                motor.drive("p")
                #print(data)
            elif(stringData=="stop"):
                motor.drive("p")
                #motor.drive(move)        
                #print(move)
        
        
except KeyboardInterrupt:
    
    #GPIO.output(enable, GPIO.LOW)
    GPIO.cleanup()
    print("Terminated")
