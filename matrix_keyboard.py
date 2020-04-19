#!/usr/bin/env python
import RPi.GPIO as GPIO

class MatrixKeyboard:
    def __init__(self, rows, cols, callback, chars=(
                (1, 2, 3, 'A'),
                (4, 5, 6, 'B'),
                (7, 8, 9, 'C'),
                ('*', 0, '#', 'D')
            ), bouncetime=200):
        GPIO.setup(rows, GPIO.OUT)
        GPIO.setup(cols, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.output(rows, GPIO.HIGH)
        self._rows = rows
        self._cols = cols
        self._chars = chars
        self._can_read = True
        self._callback = callback
        
        for col in cols:
            GPIO.add_event_detect(col, GPIO.BOTH, callback=self._evt_callback,
                                  bouncetime=bouncetime)
    
    def _evt_callback(self, col_pin):
        if not self._can_read:
            can_read_tmp = True
            for col in self._cols:
                if GPIO.input(col):
                    can_read_tmp = False
            self._can_read = can_read_tmp
            return
        
        self._can_read = False
        entered_char = self._find_pressed_button(col_pin)
        if entered_char is not None:
            self._callback(entered_char)

    def _find_pressed_button(self, pressed_col_pin):
        col = self._cols.index(pressed_col_pin)
        row = None
        for row_pin in self._rows:
            values = list(map(lambda pin: 1 if pin == row_pin else 0, self._rows))
            GPIO.output(self._rows, values)
            if GPIO.input(pressed_col_pin):
                row = self._rows.index(row_pin)
        GPIO.output(self._rows, GPIO.HIGH)
        return self._chars[row][col] if row is not None else None