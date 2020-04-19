#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

REG_DATA = GPIO.HIGH
REG_INSTR = GPIO.LOW
RW_READ = GPIO.HIGH
RW_WRITE = GPIO.LOW
E_READ = GPIO.HIGH
E_EXECUTE = GPIO.LOW

ns = 1e-7
tC = 1000 * ns  # E Cycle time (min)
tSP1 = 60 * ns  # Address setup time (min)
tSP2 = 195 * ns  # Data setup time (min)
tPW = 450 * ns  # E pulse width (min)
tR = 25 * ns  # E rise time (max)
tF = 25 * ns  # E fall time (max)
tHD1 = 20 * ns  # Address hold time (min)
tHD2 = 10 * ns  # Data hold time (min)
tD = 360 * ns  # Data output delay time (max)


class Lcd1602:
    def __init__(self, RW, RS, Enable, Data):
        GPIO.setup((RS, RW, Enable), GPIO.OUT)
        GPIO.setup(Data, GPIO.OUT)
        GPIO.output(RW, RW_WRITE)
        GPIO.output(RS, REG_INSTR)
        GPIO.output(Enable, E_READ)
        
        self.RW = RW
        self.RS = RS
        self.Enable = Enable
        self.Data = Data
        
        print('initializing')
        self.set_function()
        self.turn_on_display()
        self.clear_display()
        print('done')
        
    def clear_display(self):
        self._send_byte(0x01)
    
    def return_home(self):
        self._send_byte(0x02)
    
    def turn_on_display(self, cursor_on=False, blink_on=False):
        code = 0b00001100 | (2 if cursor_on else 0) | (1 if blink_on else 0)
        self._send_byte(code)
    
    def turn_off_display(self):
        self._send_byte(0b00001000)
    
    def set_entry_mode(self, increment=True, shift=True):
        code = 0b00000100
        if increment:
            code = code | 2
        if shift:
            code = code | 1
        self._send_byte(code)
  
    def shift_cursor(self, right=True):
        code = 0b00010000 | (4 if right else 0)
        self._send_byte(code)
    
    def shift_display(self, right=True):
        code = 0b00011000 | (4 if right else 0)
        self._send_byte(code)
  
    def set_function(self, data_length_8_bit=True, display_2_lines=True,
                     big_font=False):
        code = 0x20 | (0x10 if data_length_8_bit else 0) | \
            (0x08 if display_2_lines else 0) | (0x04 if big_font else 0)
        self._send_byte(code)
  
    def set_ddram_address(self, addr):
        self._send_byte(0x80 | addr)
  
    def _send_byte(self, byte, rs=REG_INSTR):
        GPIO.output((self.RS, self.RW), (rs, RW_WRITE))
        GPIO.output(self.Enable, E_READ)
        time.sleep(tR)
        
        for i in range(8):
            GPIO.output(self.Data[i], (byte >> i) & 1)
        time.sleep(tPW)
        GPIO.output(self.Enable, E_EXECUTE)
        time.sleep(tC)
        
        GPIO.output((self.RS, self.RW), (REG_INSTR, RW_READ))
        time.sleep(tSP1 - tR)
        GPIO.output(self.Enable, E_READ)
        time.sleep(1000 * ns)
        GPIO.output(self.Enable, E_EXECUTE)

    def send_string(self, str, line=1):
        self.clear_display()
        self.set_ddram_address(0x67) # should be 0x00, but...
        for i in range(len(str)):
            char = str[i:i+1]
            if char == '\n':
                self.set_ddram_address(0x27) # and here should be 0x40...
            else:
                self._send_byte(ord(char), rs=REG_DATA)

    def cleanup(self):
        self.clear_display()
