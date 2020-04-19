#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import datetime as dt
from lcd1602 import Lcd1602
from adc0832 import Adc0832

RS = 4
RW = 17
Enable = 27
Data = (5, 6, 13, 19, 26, 18, 23, 24)

ADC_out = 25
ADC_cmd = 20
ADC_clock = 12
ADC_chip_select = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    lcd = Lcd1602(RS, RW, Enable, Data)
    adc = Adc0832(ADC_chip_select, ADC_clock, ADC_cmd, ADC_out)
    try:
        while True:
            value = adc.read_single() * 5.0
            lcd.send_string('     {:.4f}'.format(value))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('')
        lcd.cleanup()
        GPIO.cleanup()
0