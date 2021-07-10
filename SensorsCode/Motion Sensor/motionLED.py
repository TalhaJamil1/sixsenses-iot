import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay
from gpiozero import MotionSensor, LED
from signal import pause

import ssl
import paho.mqtt.client as mqtt


def send_message(topic, message):
    client = mqtt.Client(client_id='RPi-000000001078')
    client.username_pw_set(username="commandandcontrol", password="Qpc423hwdM")
    client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
    client.connect("cwlicc.zapto.org", 8883, 60)

    client.publish(topic, message);
    client.loop();
    client.disconnect();

def on_motion_detected():
    print("Motion Detected!")
    led.on()
    send_message("commandandcontrol/ms", "1")

def on_no_motion():
    print("No Motion!")
    led.off()
    send_message("commandandcontrol/ms", "0")

pir = MotionSensor(4)    #pin number for motion sensor input
led = LED(16)            #pin number for LED output

pir.when_motion = on_motion_detected
pir.when_no_motion = on_no_motion

pause()

GPIO.cleanup()
