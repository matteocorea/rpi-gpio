#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Pin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin, GPIO.OUT)

def cleanup():
    print("clean exit...\n")
    pwm.stop()
    GPIO.cleanup()

def tune(pwm, frequency, duration):
    pwm.start(50)
    pwm.ChangeFrequency(frequency)
    time.sleep(duration)
    pwm.stop()

try:
    setup()
    pwm = GPIO.PWM(Pin, 50)
    while True:
        tune(pwm, 400, 0.3)
        tune(pwm, 450, 0.3)
        tune(pwm, 510, 0.3)
        tune(pwm, 550, 0.3)
        time.sleep(1)
except KeyboardInterrupt:
    cleanup()
