#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Configure pin numbers et al
segments = [4, 17, 22, 5, 6, 13, 19]
digits = [18, 23, 24, 25]
clock = 1000
delay = 1.0 / clock

def display_digit(digit, n):
    if n is None:
        GPIO.output(digits[digit], GPIO.HIGH)
        return
    num_codes = (126, 48, 109, 121, 51, 91, 95, 112, 127, 123)
    digit_codes = (8, 4, 2, 1)
    num = num_codes[n]
    for i in range(7):
        GPIO.output(segments[6 - i], (num & (1 << i)) >> i)
    for i in range(4):
        GPIO.output(
            digits[i], GPIO.LOW if i == digit else GPIO.HIGH)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(segments, GPIO.OUT)
    GPIO.setup(digits, GPIO.OUT)
    GPIO.output(segments, GPIO.LOW)
    GPIO.output(digits, GPIO.HIGH)

def display_number(num):
    assert 0 <= num <= 9999
    display_digit(0, num // 1000 if num >= 1000 else None)
    time.sleep(delay)
    display_digit(1, num // 100 % 10 if num >= 100 else None)
    time.sleep(delay)
    display_digit(2, num // 10 % 10 if num >= 10 else None)
    time.sleep(delay)
    display_digit(3, num % 10)
    time.sleep(delay)

def loop():
    counter = 0
    while True:
        for i in range(int(clock / 5.0 * 0.01)):
            display_number(counter % 10000)
            time.sleep(delay)
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
