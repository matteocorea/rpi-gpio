#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

color = '#7300ff'

Red = 17
Green = 22
Blue = 5
pwm_pins = {}

def setup():
    GPIO.setmode(GPIO.BCM)
    # Configure pin IN or OUT
    for pin in (Red, Green, Blue):
        GPIO.setup(pin, GPIO.OUT)
        pwm_pins[pin] = GPIO.PWM(pin, 100)
        pwm_pins[pin].start(0)

def loop():
    dc = lambda str: 100 - (int(str, 16)/255.0*100)
    pwm_pins[Red].ChangeDutyCycle(dc(color[1:3]))
    pwm_pins[Green].ChangeDutyCycle(dc(color[3:5]))
    pwm_pins[Blue].ChangeDutyCycle(dc(color[5:7]))
    while True:
        pass

def cleanup():
    print("clean exit. Stop pwms")
    for pin in pwm_pins:
        pwm_pins[pin].stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
