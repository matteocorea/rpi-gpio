#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from matrix_keyboard import MatrixKeyboard

rows = (18, 23, 24, 25)
cols = (12, 16, 20, 21)
keyboard = None

code = ''

def setup():
    GPIO.setmode(GPIO.BCM)
    keyboard = MatrixKeyboard(rows=rows, cols=cols,
                              callback=char_entered, bouncetime=50)

def char_entered(chr):
    global code
    if chr == '#':
        code = code[0:-1]
    elif chr == '*':
        code = ''
        print('\n' * 100)
    else:
        code = code + str(chr)
    print(code)

def loop():
    while True:
        pass

def cleanup():
    print("clean exit")
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        cleanup()
