#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import datetime as dt
from lcd1602 import Lcd1602

RS = 4
RW = 17
Enable = 27
Data = (5, 6, 13, 19, 26, 18, 23, 24)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    lcd = Lcd1602(RS, RW, Enable, Data)
    try:
        while True:
            now = dt.datetime.now()
            current_date = now.strftime('%Y-%m-%d')
            current_time = now.strftime('%H:%M:%S')
            lcd.send_string('   {}\n    {}'.format(current_date, current_time))
            time.sleep(1)
    except KeyboardInterrupt:
        print('')
        lcd.cleanup()
        GPIO.cleanup()
