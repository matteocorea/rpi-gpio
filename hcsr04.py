#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


class HcSr04:
    def __init__(self, trigger, echo):
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self._trigger = trigger
        self._echo = echo
    
    def measure_distance_cm(self):
        GPIO.output(self._trigger, GPIO.HIGH)
        time.sleep(10e-6)
        GPIO.output(self._trigger, GPIO.LOW)
        
        GPIO.wait_for_edge(self._echo, GPIO.RISING, timeout=200)
        start_time = time.perf_counter()
        GPIO.wait_for_edge(self._echo, GPIO.FALLING, timeout=200)
        end_time = time.perf_counter()
        distance_cm = (end_time - start_time) / 2 * 340 * 100
        return distance_cm if distance_cm <= 400 else None
