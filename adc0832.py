import RPi.GPIO as GPIO
import time

CLK_FREQ = 100 * 1000  # 100Khz

class Adc0832:
    def __init__(self, CS, CLK, DI, DO):
        GPIO.setup((CS, CLK, DI), GPIO.OUT)
        GPIO.setup(DO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(CS, GPIO.HIGH)
        self.CS = CS
        self.CLK = CLK
        self.DO = DO
        self.DI = DI
    
    def _clk(self):
        GPIO.output(self.CLK, GPIO.HIGH)
        time.sleep(1.0 / CLK_FREQ / 2)
        GPIO.output(self.CLK, GPIO.LOW)
        time.sleep(1.0 / CLK_FREQ / 2)
    
    def read_single(self, channel=0):
        return self._read(GPIO.HIGH, channel)
    
    def read_differential(self, ch0_plus=True):
        return self._read(GPIO.LOW, GPIO.LOW if ch0_plus else GPIO.HIGH)
    
    def _read(self, sgl_dif, odd_sign):
        GPIO.output((self.CS, self.DI), (GPIO.LOW, GPIO.HIGH))
        self._clk()
        GPIO.output(self.DI, sgl_dif)
        self._clk()
        GPIO.output(self.DI, odd_sign)
        self._clk()
        
        value = 0
        for i in range(8):
            self._clk()
            value = value << 1 | GPIO.input(self.DO)
        for i in range(8):
            # discard LSB data
            self._clk()

        GPIO.output(self.CS, GPIO.HIGH)
        return value / 255.0