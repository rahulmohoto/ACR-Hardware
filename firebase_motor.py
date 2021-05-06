from firebase import firebase
import RPi.GPIO as GPIO
import time
import motor

firebase=firebase.FirebaseApplication("https://acr-project-8f9b6.firebaseio.com/",None)
pushed=firebase.get('/Test','') 

try:
    while 1:
        pushed=firebase.get('/Test','')
        if(pushed['up_btn']):
            motor.drive("w")
        elif(pushed['down_btn']):
            motor.drive("s")
        elif(pushed['left_btn']):
            motor.drive("a")
        elif(pushed['right_btn']):
            motor.drive("d")
        else:
            motor.drive("p")
            
            
except KeyboardInterrupt:
    GPIO.cleanup()

