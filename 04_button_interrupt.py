#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 5
ButtonPin = 20

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, GPIO.LOW)

def buttonPressed(channel):
    if GPIO.input(ButtonPin) == GPIO.LOW:
        print('button pressed')
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LedPin, GPIO.LOW)
    else:
        print('button released')
        GPIO.output(LedPin, GPIO.LOW)

def loop():
    GPIO.add_event_detect(ButtonPin, GPIO.BOTH, callback=buttonPressed)
    while True:
        pass

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
