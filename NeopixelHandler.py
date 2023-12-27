from SunriseSunsetAPI import SunriseSunsetAPI
from datetime import datetime
from dateutil import tz


class NeopixelHandler:

    def __init__(self, settings):
        # set sunrise-sunset API
        self.sunriseSunsetAPI = SunriseSunsetAPI(self.settings["sunrise_sunset_api"])

    def get_local_date_time(self, date_time):
        d = ""
