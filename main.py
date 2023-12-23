from SetWifi import SetWifi
from TimeHandler import TimeHandler
import requests
import time


class Main:

    def __init__(self):
        self.api_url = "http://worldtimeapi.org/api/timezone/Europe/Amsterdam"

        self.wifi = SetWifi()
        connected = self.wifi.open_wifi()
        if connected:
            self.timeHandler = TimeHandler(self.api_url)
            self.timeHandler.set_rtc()
        else:
            print("Not connected")


if __name__ == '__main__':
    main = Main()
    print(main.timeHandler.get_current_time_tuple())


