from neopixel import Neopixel


class NeopixelHandler:

    def __init__(self, settings):

        # CONSTANTS
        self.numpix = settings["num_leds"]
        self.yellow = (255, 100, 0)
        self.orange = (255, 50, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        # set NEOPIXELS
        self.pixels = Neopixel(self.numpix,
                               settings["state_machine"],
                               settings["gpio_pin"],
                               settings["mode"])
        self.pixels.brightness(settings["brightness"])

    def set_day(self, pixel):
        self.clear_pixels()
        if pixel == 0:
            self.pixels.set_pixel(pixel, self.yellow)
        else:
            self.pixels.set_pixel_line_gradient(max(0, pixel-2), pixel, self.orange, self.yellow)
        self.pixels.show()

    def set_dawn(self, pixel):
        self.clear_pixels()
        if pixel == 0:
            self.pixels.set_pixel(pixel, self.blue)
        else:
            self.pixels.set_pixel_line_gradient(0, min(pixel, self.numpix-1), self.white, self.blue)
        self.pixels.show()

    def set_dusk(self, pixel):
        self.clear_pixels()
        if pixel == 0:
            self.pixels.set_pixel(pixel, self.white)
        else:
            self.pixels.set_pixel_line_gradient(max(pixel, 0), self.numpix-1, self.blue, self.white)
        self.pixels.show()

    def clear_pixels(self):
        self.pixels.fill(self.black)
        self.pixels.show()

    def set_pixel(self, pixel, period):
        p = min(pixel, 29)
        if period == "dawn":
            self.set_dawn(p)
        elif period == "day":
            self.set_day(p)
        elif period == "dusk":
            self.set_dusk(p)
        else:
            self.clear_pixels()

