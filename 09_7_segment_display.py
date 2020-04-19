#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Configure pin numbers et al
segments = [4, 17, 22, 5, 6, 13, 19]

def display_digit(n):
    digits = (126, 48, 109, 121, 51, 91, 95, 112, 127, 123)
    num = digits[n]
    for i in range(7):
        GPIO.output(segments[6 - i], (num & (1 << i)) >> i)

def setup():
    GPIO.setmode(GPIO.BCM)
    # Configure pin IN or OUT
    GPIO.setup(segments, GPIO.OUT)
    GPIO.output(segments, GPIO.LOW)

def loop():
    counter = 0
    while True:
        display_digit(5)
        time.sleep(0.2)
        counter = counter + 1

def cleanup():
    print("clean exit")
    # GPIO.output(Pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
