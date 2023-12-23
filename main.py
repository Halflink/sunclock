from SetWifi import SetWifi
from TimeHandler import TimeHandler
from DisplayHandler import DisplayHandler
import json as json


class Main:

    def __init__(self):
        # Get settings
        with open("./settings.json") as jsonFile:
            self.settings = json.load(jsonFile)
            jsonFile.close()

        # set WIFI
        self.wifi = SetWifi()
        self.wifi.try_connecting_wifi()
        if self.wifi.is_connected():
            self.timeHandler = TimeHandler(self.settings["rtc_url"])
            self.displayHandler = DisplayHandler()
        else:
            print("Not connected")


if __name__ == '__main__':
    main = Main()
    while True:
        main.displayHandler.evaluate_display()



