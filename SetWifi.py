import network
import json as json
import time


class SetWifi:

    def __init__(self):

        self.wlan = None
        with open("./secrets.json") as jsonFile:
            secrets_info = json.load(jsonFile)
            jsonFile.close()
        for secrets in secrets_info["secrets"]:
            if secrets["id"] == 0:
                self.ssid = secrets["ssid"]
                self.password = secrets["password"]
        self.time_out = secrets_info["time_out"]
        self.max_tries = secrets_info["max_tries"]

    def open_wifi(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        count = 0
        while True:
            time.sleep(self.time_out)
            if count == self.max_tries and not self.is_connected():
                return False
            elif self.is_connected():
                return True
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