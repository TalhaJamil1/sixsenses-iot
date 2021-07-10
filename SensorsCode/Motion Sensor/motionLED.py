import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay
from gpiozero import MotionSensor, LED
from signal import pause

def on_motion_detected():
    print("Motion Detected!")
    led.on()

def on_no_motion():
    print("No Motion!")
    led.off()

pir = MotionSensor(4)    #pin number for motion sensor input
led = LED(16)            #pin number for LED output

pir.when_motion = on_motion_detected
pir.when_no_motion = on_no_motion

pause()

GPIO.cleanup()
