#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math

# Configure pin numbers et al
Pins = (4, 17, 27, 22, 5, 6, 13, 19)

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in Pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def enablePinByIndex(pinIndex):
    for index in range(len(Pins)):
        if pinIndex == index:
            GPIO.output(Pins[index], GPIO.HIGH)
        else:
            GPIO.output(Pins[index], GPIO.LOW)

def loop():
    current = 0
    cyclesPerSec = 0.7
    stepsPerSec = 32
    while True:
        sin = math.sin(current) * (len(Pins)/2-0.0001) + len(Pins)/2
        pinIndex = math.floor(sin)
        enablePinByIndex(pinIndex)
        current += (2*math.pi * cyclesPerSec / stepsPerSec)
        time.sleep(1.0 / stepsPerSec)

def cleanup():
    print("clean exit")
    for pin in Pins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
