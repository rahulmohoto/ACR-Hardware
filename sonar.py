import RPi.GPIO as GPIO
import time

def clean():
    GPIO.cleanup()
    
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = [2,4,27,9,23]
GPIO_ECHO = [3,17,22,11,24]
 
left=0
middle=0
right=0
right_most=0
left_most=0

for i in range(5):
    GPIO.setup(GPIO_TRIGGER[i], GPIO.OUT)
    GPIO.setup(GPIO_ECHO[i], GPIO.IN)
 
def distance(i):

    GPIO.output(GPIO_TRIGGER[i], False)
 

    time.sleep(0.00002)
    GPIO.output(GPIO_TRIGGER[i], True)
    
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER[i], False)
    time.sleep(0.00002)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO[i]) == 0:
        StartTime = time.time()
   
    while GPIO.input(GPIO_ECHO[i]) == 1:
        StopTime = time.time()
        
  
    TimeElapsed=StopTime - StartTime
  
    distance=(TimeElapsed * 34300) / 2
    
    return distance

def read():
    global left
    global right
    global middle
    global left_most
    global right_most

    left = distance(0)
    time.sleep(0.3)
    middle=distance(1)
    time.sleep(0.3)
    right=distance(2)
    time.sleep(0.3)
    left_most=distance(3)
    time.sleep(0.3)
    right_most=distance(4)
    time.sleep(0.3)
        
