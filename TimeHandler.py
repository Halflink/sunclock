import requests
import time
import machine

class TimeHandler:

    def __init__(self, api_url):
        self.api_url = api_url
        self.is_set_rtc_successful = False

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
            machine.RTC().datetime((year, month, day, day_of_week, hour, minute, second, milsec))
            self.is_set_rtc_successful = True

        else:
            self.is_set_rtc_successful = False

    @staticmethod
    def get_current_time_tuple():
        current_time = []
        current_time.append(str(time.localtime()[3])[0:1])
        current_time.append(str(time.localtime()[3])[1:2])
        current_time.append(str(time.localtime()[4])[0:1])
        current_time.append(str(time.localtime()[4])[1:2])
        return current_time

