from SetWifi import SetWifi
from RealTimeClockAPI import TimeHandler
from DisplayHandler import DisplayHandler
from OLEDHandler import OLEDHandler
from Sunclock import Sunclock
from DHT22Sensor import DHT22Sensor
import json as json
import time


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
            self.timeHandler = TimeHandler(self.settings["rtc"], self.oledHandler)
            time_int = time.time()
            self.displayHandler = DisplayHandler(self.settings["segment_display"], time_int)

            # set sunclock
            self.sunclock = Sunclock(self.settings, self.oledHandler)

            # set DHT22 sensor
            self.dht22Sensor = DHT22Sensor(self.settings["DHT22"], self.oledHandler)
        else:
            self.oledHandler.set_line_1("NO WIFI")
            self.oledHandler.set_line_2("CONNECTED")
            print("Not connected")

    def run_clock(self):
        if self.wifi.is_connected() and self.timeHandler.is_set_rtc_successful:
            while True:
                time_int = time.time()
                self.displayHandler.set_display_with_time(time_int, self.timeHandler)
                self.sunclock.calculate_sun_clock_pixels(time_int, self.timeHandler)
                self.timeHandler.evaluate_rtc(time_int, self.oledHandler)
                self.dht22Sensor.get_and_show_measurements(time_int)


if __name__ == '__main__':
    main = Main()
    main.run_clock()


