#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math

# Configure pin numbers et al
Pin = 17
pwm = None
frequency = 1000
cycles_per_second = 0.5
steps_per_second = 50

def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin, GPIO.OUT)
    pwm = GPIO.PWM(Pin, frequency)
    pwm.start(0)

def loop():
    delta = 100 * cycles_per_second / steps_per_second
    dc = 0
    asc = True
    while True:
        if dc >= 100:
            asc = False
        elif dc <= 0:
            asc = True
        dc += delta * (1 if asc else -1)
        pwm.ChangeDutyCycle(math.floor(dc))
        time.sleep(1.0 / steps_per_second)

def cleanup():
    print('clean exit')
    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
