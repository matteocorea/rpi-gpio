#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Red = 17
Green = 20
Blue = 13

blink_duration = 0.2
off_duration = 1.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)
GPIO.output(Red, GPIO.HIGH)
GPIO.output(Green, GPIO.HIGH)
GPIO.output(Blue, GPIO.HIGH)

def blink(pin, duration):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(duration)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)

order = {
    2: Red,
    1: Green,
    3: Blue
}

try:
    while True:
        print ("led on...")
        blink(order[1], blink_duration)
        blink(order[2], blink_duration)
        blink(order[3], blink_duration)
        print ("led off...")
        time.sleep(off_duration)
except KeyboardInterrupt:
    print ("clean exit")
    GPIO.output(Red, GPIO.HIGH)
    GPIO.output(Green, GPIO.HIGH)
    GPIO.output(Blue, GPIO.HIGH)
    GPIO.cleanup()
