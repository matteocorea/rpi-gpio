#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Pin = 17

buzz_duration = 0.2
off_duration = 2.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin, GPIO.OUT)
GPIO.output(Pin, GPIO.LOW)

def buzz(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(duration)

try:
    while True:
        print("buzz on...")
        buzz(Pin, buzz_duration)
        buzz(Pin, buzz_duration)
        buzz(Pin, buzz_duration)
        print("buzz off...")
        GPIO.output(Pin, GPIO.LOW)
        time.sleep(off_duration)
except KeyboardInterrupt:
    print("clean exit")
    GPIO.output(Pin, GPIO.HIGH)
    GPIO.cleanup()
