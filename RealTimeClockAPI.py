import requests
import time
from machine import RTC


class TimeHandler:

    def __init__(self, settings, oledHandler):

        # constants
        self.api_url = settings["url"]
        self.is_set_rtc_successful = False
        self.last_rtc_evaluation = time.time()
        self.evaluate_interval = settings["evaluate_interval"]

        # RTC
        self.rtc = RTC()
        self.set_rtc(oledHandler)

    @staticmethod
    def make_time(time_string):
        time_int = time.mktime((int(time_string[0:4]), int(time_string[5:7]), int(time_string[8:10]),
                                int(time_string[11:13]), int(time_string[14:16]), int(time_string[17:19]), 0, 0))
        return time_int

    @staticmethod
    def is_on_same_day(time_int_a, time_int_b):
        time_struc_a = time.localtime(time_int_a)
        time_struc_b = time.localtime(time_int_b)
        if time_struc_a[0] != time_struc_b[0] \
                or time_struc_a[1] != time_struc_b[1] \
                or time_struc_a[2] != time_struc_b[2]:
            return False
        else:
            return True

    @staticmethod
    def get_time_string(time_int):
        time_now = time.localtime(time_int)
        hour = str(time_now[3])
        hour = '0' * max(0, 2 - len(hour)) + hour
        minute = str(time_now[4])
        minute = '0' * max(0, 2 - len(minute)) + minute
        current_time = hour + minute
        return current_time

    @staticmethod
    def get_date_string(time_int):
        time_now = time.localtime(time_int)
        year = str(time_now[0])
        month = str(time_now[1])
        month = '0' * max(0, 2 - len(month)) + month
        day = str(time_now[2])
        day = '0' * max(0, 2 - len(day)) + day
        date = "{}-{}-{}".format(year, month, day)
        return date

    def set_rtc(self, oledHandler):
        oledHandler.set_line("Getting real time...")
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
            oledHandler.clear_lines()
        else:
            oledHandler.set_line_1("ERR CONNECT")
            oledHandler.set_line_2(self.api_url)
            self.is_set_rtc_successful = False

    def evaluate_rtc(self, time_int, oledHandler):
        time_dif = time_int - self.last_rtc_evaluation
        if not self.is_set_rtc_successful or time_dif > self.evaluate_interval:
            self.set_rtc(oledHandler)






