import RPi.GPIO as GPIO
import time

pinA=21
pinB=20
pinC=16
pinD=12

en1=7
en2=8

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinA,GPIO.OUT)
GPIO.setup(pinB,GPIO.OUT)
GPIO.setup(pinC,GPIO.OUT)
GPIO.setup(pinD,GPIO.OUT)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
duty1=38
duty2=46
p1=GPIO.PWM(en1, 500)
p2=GPIO.PWM(en2, 500)
p1.start(duty1)
p2.start(duty2)

def clean():
    GPIO.cleanup()
    
def fwd():
    print("Forward called..")
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)

def bck():
    print("Backward called..")
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinD, GPIO.HIGH)
    
def left():
    print("Left called..")
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    
def right():
    print("Right called..")
    GPIO.output(pinC, GPIO.HIGH)
    GPIO.output(pinD, GPIO.LOW)
    
def stop():
    print("Stop called..")
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)
    GPIO.output(pinD, GPIO.LOW)
    
def drive(move):
    try:
        if(move=='w'):
            fwd()
            #time.sleep(0.2)
        elif(move=='s'):
            bck()
        elif(move=='a'):
            left()
        elif(move=='d'):
            right()
        elif(move=='p'):
            stop()
         
    except KeyboardInterrupt:
        GPIO.cleanup()

