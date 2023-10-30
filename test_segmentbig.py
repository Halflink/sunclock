# IMPORTS
import utime as time
from machine import I2C, Pin, RTC
from ht16k33segmentbig import HT16K33SegmentBig

# CONSTANTS
DELAY = 0.01
PAUSE = 3

# START
if __name__ == '__main__':
    i2c = I2C(1, scl=Pin(19), sda=Pin(18))    # Raspberry Pi Pico
    display = HT16K33SegmentBig(i2c, 0x71)
    display.set_brightness(10)

    # Write 'SYNC' to the LED using custom glyphs
    display.set_character("1", digit=0)
    display.set_character("2", digit=1)
    display.set_character("3", digit=2)
    display.set_character("4", digit=3)
    # display.set_colon(0x02)
    # display.set_colon(0x04)
    # display.set_colon(0x08)
    # display.set_colon(0x10)
    display.draw()