#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

scale = 58 # cm per us

def get_time():
    return time.perf_counter()

class HcSr04:
    def __init__(self, trigger, echo):
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self._trigger = trigger
        self._echo = echo
        self._start_time = None
    
    def measure_distance(self):
        GPIO.output(self._trigger, GPIO.HIGH)
        time.sleep(1e-6)
        GPIO.output(self._trigger, GPIO.LOW)
        
        GPIO.wait_for_edge(self._echo, GPIO.RISING, timeout=1)
        start_time = get_time()
        GPIO.wait_for_edge(self._echo, GPIO.FALLING, timeout=1)
        end_time = get_time()
        print('diff: {}'.format(end_time - start_time))
        return float(end_time - start_time) * 58.0
    