from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf


class OLEDHandler:

    def __init__(self, settings):
        # CONSTANTS
        wifi_image = bytearray(
            b'\x00?\xfc\x00\x01\xff\xfe\x00\x07\x80\x07\x80\x1c\x00\x00\xe0\x00\x00\x00\x00\x00\x0f\xc0\x00\x00?\xf0\x00\x00\xf0<\x00\x01\x80\x06\x00\x00\x00\x00\x00\x00\x07\x80\x00\x00\x1f\xe0\x00\x008p\x00\x00`\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x07\x80\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.frame_buffer = framebuf.FrameBuffer(wifi_image, 32, 32, framebuf.MONO_HLSB)
        degrees_image = bytearray(b'`\x90\x90`\x00\x00\x00\x00')
        self.frame_buffer_line_1 = framebuf.FrameBuffer(degrees_image, 8, 8, framebuf.MONO_HLSB)
        self.line1 = ""
        self.line2 = ""
        self.line3 = ""
        self.show_frame_buffer = False
        self.show_frame_buffer_line_1 = False

        # init OLED
        i2c = I2C(settings["i2c_id"], scl=Pin(settings["scl"]), sda=Pin(settings["sda"]), freq=settings["frequency"])  # Init I2C using pins GP8 & GP9 (default I2C0 pins)
        self.oled = SSD1306_I2C(settings["width"], settings["height"], i2c)  # Init oled display
        self.oled.fill(0)

    def enable_wifi_image(self):
        self.show_frame_buffer = True
        self.render_oled()

    def disable_wifi_image(self):
        self.show_frame_buffer = False
        self.render_oled()

    def enable_degrees_image(self):
        self.show_frame_buffer_line_1 = True
        self.render_oled()

    def disable_degrees_image(self):
        self.show_frame_buffer = False
        self.render_oled()

    def set_line_1(self, text):
        self.line1 = text[0:11]
        self.render_oled()

    def set_line_2(self, text):
        self.line2 = text[0:11]
        self.render_oled()

    def set_line_3(self, text):
        self.line3 = text[0:16]
        self.render_oled()

    def render_oled(self):
        self.oled.fill(0)
        if self.show_frame_buffer:
            self.oled.blit(self.frame_buffer, 96, 0)
        self.oled.text(self.line1, 5, 2)
        if self.show_frame_buffer_line_1:
            self.oled.blit(self.frame_buffer_line_1, 40, 2)
        self.oled.text(self.line2, 5, 12)
        self.oled.text(self.line3, 5, 25)
        self.oled.show()
