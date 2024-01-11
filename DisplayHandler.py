import time
from machine import I2C, Pin
from ht16k33segmentbig import HT16K33SegmentBig


class DisplayHandler:

    def __init__(self, settings, time_int):

        # CONSTANTS
        self.last_colon_evaluation = time_int
        self.last_time_evaluation = time_int - 60
        self.colon_state = False

        # DISPLKAY
        i2c = I2C(settings["i2c_id"], scl=settings["scl"], sda=settings["sda"])  # Raspberry Pi Pico
        address = int(settings["address"], 16)
        self.display = HT16K33SegmentBig(i2c, address)
        self.display.set_brightness(settings["brightness"])

    def toggle_colon(self):
        if self.colon_state:
            self.colon_state = False
            self.display.set_colon(0x00)
        else:
            self.colon_state = True
            self.display.set_colon(0x02)

    def set_display_with_time(self, time_int, timeHandler):
        colon_diff = time_int - self.last_colon_evaluation
        time_diff = time_int - self.last_time_evaluation
        if colon_diff >= 1:
            self.toggle_colon()
            self.last_colon_evaluation = time_int
            self.display.draw()
        if time_diff >= 60:
            time_string = timeHandler.get_time_string(time_int)
            self.display.set_character(time_string[0:1], digit=0)
            self.display.set_character(time_string[1:2], digit=1)
            self.display.set_character(time_string[2:3], digit=2)
            self.display.set_character(time_string[3:4], digit=3)
            self.last_time_evaluation = time_int
            self.display.draw()


