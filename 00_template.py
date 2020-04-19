#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Configure pin numbers et al
# Pin = 5
# OtherPin = 7

def setup():
    GPIO.setmode(GPIO.BCM)
    # Configure pin IN or OUT
    # GPIO.setup(Pin, GPIO.OUT)
    # GPIO.setup(OtherPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.output(Pin, GPIO.LOW)

def loop():
    while True:
        # do something
        pass

def cleanup():
    print('clean exit')
    # GPIO.output(Pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
