import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay
from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(4)    #pin number for motion sensor input
led = LED(16)            #pin number for LED output

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()

GPIO.cleanup()