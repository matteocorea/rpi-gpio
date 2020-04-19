#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 5
ButtonPin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, GPIO.LOW)

def loop():
    while True:
        if GPIO.input(ButtonPin) == GPIO.LOW:
            print('button pressed')
            GPIO.output(LedPin, GPIO.HIGH)
        else:
            print('button not pressed')
            GPIO.output(LedPin, GPIO.LOW)

def cleanup():
    print("clean exit")
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
