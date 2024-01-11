import requests
import time
from machine import RTC


class TimeHandler:

    def __init__(self, api_url, oledHandler):

        # constants
        self.api_url = api_url
        self.is_set_rtc_successful = False
        self.last_rtc_evaluation = time.time()

        # RTC
        self.rtc = RTC()
        self.set_rtc(oledHandler)

    @staticmethod
    def make_time(time_string):
        time_int = time.mktime((int(time_string[0:4]), int(time_string[5:7]), int(time_string[8:10]),
                                int(time_string[11:13]), int(time_string[14:16]), int(time_string[17:19]), 0, 0))
        return time_int

    @staticmethod
    def get_time_string(time_int):
        time_now = time.localtime(time_int)
        hour = str(time_now[3])
        hour = '0' * max(0, 2 - len(hour)) + hour
        minute = str(time_now[4])
        minute = '0' * max(0, 2 - len(minute)) + minute
        current_time = hour + minute
        return current_time


    def set_rtc(self, oledHandler):
        oledHandler.set_line_1("Get real time...")
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
            oledHandler.set_line_1("Could not connect to")
            oledHandler.set_line_2(self.api_url)
            self.is_set_rtc_successful = False

    def evaluate_rtc(self, time_int):
        time_dif = time_int - self.last_rtc_evaluation
        if not self.is_set_rtc_successful or time_dif > 86400:
            self.set_rtc()






