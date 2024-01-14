from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf


class OLEDHandler:

    def __init__(self, settings):
        # CONSTANTS
        wifi_image = bytearray(
            b'\x0f\xf0|~\xe0\x07\x00\x00\x07\xe0\x0ep8\x1c\x00\x00\x03\xc0\x07\xe0\x0c0\x00\x00\x00\x00\x01\x80\x03\xc0\x01\x80')
        self.frame_buffer = framebuf.FrameBuffer(wifi_image, 16, 16, framebuf.MONO_HLSB)
        degrees_image = bytearray(b'`\x90\x90`\x00\x00\x00\x00')
        self.frame_buffer_line_1 = framebuf.FrameBuffer(degrees_image, 8, 8, framebuf.MONO_HLSB)
        self.line1 = ""
        self.line2 = ""
        self.line3 = ""
        self.show_frame_buffer = False
        self.degrees_xpos = -1

        # init OLED
        i2c = I2C(settings["i2c_id"], scl=Pin(settings["scl"]), sda=Pin(settings["sda"]),
                  freq=settings["frequency"])  # Init I2C using pins GP8 & GP9 (default I2C0 pins)
        self.oled = SSD1306_I2C(settings["width"], settings["height"], i2c)  # Init oled display
        self.oled.fill(0)

    def enable_wifi_image(self):
        self.show_frame_buffer = True
        self.render_oled()

    def disable_wifi_image(self):
        self.show_frame_buffer = False
        self.render_oled()

    def set_degrees_image(self, xpos=-1):
        if xpos > 12: xpos = -1
        self.degrees_xpos = xpos
        self.render_oled()

    def disable_degrees_image(self):
        self.show_frame_buffer = False
        self.render_oled()

    def set_line(self, text):
        self.set_line_1(text[0:13], xpos=-1)
        if len(text) > 12:
            self.set_line_2(text[13:26])

    def set_line_1(self, text, xpos=-1):
        self.line1 = text[0:13]
        self.set_degrees_image(xpos)
        self.render_oled()

    def set_line_2(self, text):
        self.line2 = text[0:13]
        self.render_oled()

    def set_line_3(self, text):
        self.line3 = text[0:16]
        self.render_oled()

    def clear_lines(self):
        self.set_line_1("")
        self.set_line_2("")

    def render_oled(self):
        self.oled.fill(0)
        if self.show_frame_buffer:
            self.oled.blit(self.frame_buffer, 112, 0)
        if self.degrees_xpos >= 0:
            self.oled.blit(self.frame_buffer_line_1, (self.degrees_xpos * 8), 2)
        self.oled.text(self.line1, 5, 2)
        self.oled.text(self.line2, 5, 12)
        self.oled.text(self.line3, 5, 25)
        self.oled.show()
