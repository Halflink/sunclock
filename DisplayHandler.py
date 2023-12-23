import time
from machine import I2C, Pin
from ht16k33segmentbig import HT16K33SegmentBig


class DisplayHandler:

    def __init__(self):

        # CONSTANTS
        self.last_colon_evaluation = time.time()
        self.last_time_evaluation = time.time() - 60

        self.current_time_string = "0000"
        self.colon_state = False

        # DISPLKAY
        i2c = I2C(1, scl=Pin(19), sda=Pin(18))  # Raspberry Pi Pico
        self.display = HT16K33SegmentBig(i2c, 0x71)
        self.display.set_brightness(10)

    @staticmethod
    def get_current_time_string():
        hour = str(time.localtime()[3])
        hour = '0' * max(0, 2 - len(hour)) + hour
        minute = str(time.localtime()[4])
        minute = '0' * max(0, 2 - len(minute)) + minute
        current_time = hour + minute
        return current_time

    def toggle_colon(self):
        if self.colon_state:
            self.colon_state = False
            self.display.set_colon(0x00)
        else:
            self.colon_state = True
            self.display.set_colon(0x02)

    def evaluate_display(self):
        current_time = time.time()
        colon_diff = current_time - self.last_colon_evaluation
        time_diff = current_time - self.last_time_evaluation
        if colon_diff >= 1:
            self.toggle_colon()
            self.last_colon_evaluation = current_time
            self.display.draw()
        if time_diff >= 60:
            current_time_string = self.get_current_time_string()
            self.display.set_character(current_time_string[0:1], digit=0)
            self.display.set_character(current_time_string[1:2], digit=1)
            self.display.set_character(current_time_string[2:3], digit=2)
            self.display.set_character(current_time_string[3:4], digit=3)
            self.last_time_evaluation = current_time
            self.display.draw()


