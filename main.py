from SetWifi import SetWifi
from RealTimeClockAPI import TimeHandler
from DisplayHandler import DisplayHandler
from OLEDHandler import OLEDHandler
from NeopixelHandler import NeopixelHandler
import json as json


class Main:

    def __init__(self):
        # Get settings
        with open("./settings.json") as jsonFile:
            self.settings = json.load(jsonFile)
            jsonFile.close()

        # set OLED
        self.oledHandler = OLEDHandler(self.settings["oled"])

        # set WIFI
        self.wifi = SetWifi(self.oledHandler)
        self.wifi.try_connecting_wifi()

        if self.wifi.is_connected():
            self.oledHandler.enable_wifi_image()

            # set clock
            self.timeHandler = TimeHandler(self.settings["rtc_url"])
            self.displayHandler = DisplayHandler(self.settings["segment_display"])

            # set sunclock
            self.neopixelHandler = NeopixelHandler(self.settings)
        else:
            self.oledHandler.set_line_1("NO WIFI")
            self.oledHandler.set_line_2("CONNECTED")
            print("Not connected")


if __name__ == '__main__':
    main = Main()
    while True:
        main.displayHandler.evaluate_display()




