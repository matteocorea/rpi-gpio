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
        print('\n' * 30)
        distance = distance_sensor.measure_distance_cm()
        print('{:.3f} cm'.format(distance) if
              distance is not None else 'out of range')
        time.sleep(0.1)
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
