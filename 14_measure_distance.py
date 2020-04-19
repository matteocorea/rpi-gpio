#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from hcsr04 import HcSr04

trigger = 23
echo = 24

distance_sensor = None

def setup():
    global distance_sensor
    GPIO.setmode(GPIO.BCM)
    distance_sensor = HcSr04(trigger=trigger, echo=echo)

def loop():
    global distance_sensor
    while True:
        print(distance_sensor.measure_distance())
        # time.sleep(1e-1)
        time.sleep(1)
        pass

def cleanup():
    print('clean exit')
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
