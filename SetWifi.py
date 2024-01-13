import network
import json as json
import time


class SetWifi:

    def __init__(self, oledHandler):

        # CONSTANTS
        self.oledHandler = oledHandler

        # Get secrets
        with open("./secrets.json") as jsonFile:
            self.secrets_info = json.load(jsonFile)
            jsonFile.close()

        # init WIFI
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def try_connecting_wifi(self):
        self.oledHandler.set_line_1("Init WIFI")
        self.oledHandler.set_line_2("Try SSID:")
        for secrets in self.secrets_info["secrets"]:
            if not self.is_connected():
                self.oledHandler.set_line_3(secrets["ssid"])
                self.open_wifi(secrets["ssid"], secrets["password"])
        if self.is_connected():
            self.oledHandler.clear_lines()
            i = self.wlan.ifconfig()
            self.oledHandler.set_line_3(i[0])
            print(i[0])

    def open_wifi(self, ssid, password):
        self.wlan.connect(ssid, password)
        count = 0
        while True:
            time.sleep(self.secrets_info["time_out"])
            if count > self.secrets_info["max_tries"] or self.is_connected():
                break
            count += 1

    def is_connected(self):
        return self.wlan.isconnected()


