import time
from SunriseSunsetAPI import SunriseSunsetAPI
from NeopixelHandler import NeopixelHandler


class Sunclock:

    def __init__(self, settings, oledHandler):
        # CONSTANTS
        self.sunrise = None
        self.sunset = None
        self.civil_twilight_begin = None
        self.civil_twilight_end = None
        self.dusk_duration_per_pixel = 0
        self.dawn_duration_per_pixel = 0
        self.day_duration_per_pixel = 0
        self.current_pixel = -1

        self.oledHandler = oledHandler

        # set sunrise-sunset API
        self.sunriseSunsetAPI = SunriseSunsetAPI(settings["sunrise_sunset_api"], oledHandler)
        self.sunrise = None

        # init neopixel
        self.neopixelHandler = NeopixelHandler(settings["neopixel"])

    @staticmethod
    def calc_pixel_number(start_time, end_time, duration_per_pixel):
        pixel = int((end_time - start_time) / duration_per_pixel)
        return pixel

    def print_times(self):
        print(
            "dawn: {}:{}  sunrise: {}:{}  sunset: {}:{}  dusk: {}:{}".format(
                time.gmtime(self.civil_twilight_begin)[3],
                time.gmtime(self.civil_twilight_begin)[4],
                time.gmtime(self.sunrise)[3],
                time.gmtime(self.sunrise)[4],
                time.gmtime(self.sunset)[3],
                time.gmtime(self.sunset)[4],
                time.gmtime(self.civil_twilight_end)[3],
                time.gmtime(self.civil_twilight_end)[4]
            )
        )

    def calc_pixel_durations(self):
        self.dusk_duration_per_pixel = int((self.civil_twilight_end - self.sunset) / self.neopixelHandler.numpix)
        self.dawn_duration_per_pixel = int((self.sunrise - self.civil_twilight_begin) / self.neopixelHandler.numpix)
        self.day_duration_per_pixel = int((self.sunset - self.sunrise) / self.neopixelHandler.numpix)

    def set_times(self, timeHandler, time_int):
        date_str = timeHandler.get_date_string(time_int)
        response = self.sunriseSunsetAPI.get_sunrise_sunset(date_str)
        if response is not None:
            self.sunrise = timeHandler.make_time(response["results"]["sunrise"])
            self.sunset = timeHandler.make_time(response["results"]["sunset"])
            self.civil_twilight_begin = timeHandler.make_time(response["results"]["civil_twilight_begin"])
            self.civil_twilight_end = timeHandler.make_time(response["results"]["civil_twilight_end"])
            self.calc_pixel_durations()

    def set_pixels(self, pixel_number, period, time_int):
        if pixel_number != self.current_pixel:
            self.neopixelHandler.set_pixel(pixel_number, period)
            self.current_pixel = pixel_number

    def has_correct_sunset_times(self):
        return self.sunriseSunsetAPI.is_get_sunrise_sunset_successful

    def calculate_sun_clock_pixels(self, time_int, timeHandler):

        # get sunset times from API
        if self.civil_twilight_end is None or not timeHandler.is_on_same_day(self.civil_twilight_end, time_int):
            self.set_times(timeHandler, time_int)

        if self.has_correct_sunset_times():
            # dawn / day / dusk / night
            if self.civil_twilight_begin <= time_int < self.sunrise:
                pixel_number = self.calc_pixel_number(self.civil_twilight_begin, time_int, self.dawn_duration_per_pixel)
                self.set_pixels(pixel_number, "dawn", time_int)
            elif self.sunrise <= time_int < self.sunset:
                pixel_number = self.calc_pixel_number(self.sunrise, time_int, self.day_duration_per_pixel)
                self.set_pixels(pixel_number, "day", time_int)
            elif self.sunset <= time_int < self.civil_twilight_end:
                pixel_number = self.calc_pixel_number(self.sunset, time_int, self.dusk_duration_per_pixel)
                self.set_pixels(pixel_number, "dusk", time_int)
            else:
                self.set_pixels(-1, "night", time_int)





