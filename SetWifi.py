import network
import json as json
import time


class SetWifi:

    def __init__(self):

        # Get secrets
        with open("./secrets.json") as jsonFile:
            self.secrets_info = json.load(jsonFile)
            jsonFile.close()

        # init WIFI
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def try_connecting_wifi(self):
        for secrets in self.secrets_info["secrets"]:
            if not self.is_connected():
                self.open_wifi(secrets["ssid"], secrets["password"])

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


if __name__ == '__main__':
    setWifi = SetWifi()
    connected = setWifi.open_wifi()
    if connected:
        print("Connection succesful")
    else:
        print("Connection unsuccesful")