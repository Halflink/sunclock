import requests
import time
from machine import RTC


class TimeHandler:

    def __init__(self, api_url):

        # constants
        self.api_url = api_url
        self.is_set_rtc_successful = False
        self.last_rtc_evaluation = time.time()

        # RTC
        self.rtc = RTC()
        self.set_rtc()

    def set_rtc(self):
        response = requests.get(self.api_url)
        if 200 <= response.status_code < 300:
            dateString = response.json()["datetime"]
            year = int(dateString[0:4])
            month = int(dateString[5:7])
            day = int(dateString[8:10])
            hour = int(dateString[11:13])
            minute = int(dateString[14:16])
            second = int(dateString[17:19])
            milsec = int(dateString[20:26])
            day_of_week = int(response.json()["day_of_week"])
            self.rtc.datetime((year, month, day, day_of_week, hour, minute, second, milsec))
            self.last_rtc_evaluation = time.time()
            self.is_set_rtc_successful = True
        else:
            self.is_set_rtc_successful = False

    def evaluate_rtc(self):
        time_dif = time.time() - self.last_rtc_evaluation
        if not self.is_set_rtc_successful or  time_dif > 86400:
            self.set_rtc()






