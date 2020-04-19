#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Configure pin numbers et al
Pin = 13

def setup():
    GPIO.setmode(GPIO.BCM)
    # Configure pin IN or OUT
    GPIO.setup(Pin, GPIO.OUT)
    GPIO.output(Pin, GPIO.HIGH)

def loop():
    while True:
        # do something
        time.sleep(1)
        print('relay on')
        GPIO.output(Pin, GPIO.LOW)
        time.sleep(1)
        print('relay off')
        GPIO.output(Pin, GPIO.HIGH)

def cleanup():
    print("clean exit")
    GPIO.output(Pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
