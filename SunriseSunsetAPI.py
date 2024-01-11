import requests
import json


class SunriseSunsetAPI:

    def __init__(self, settings):
        self.url = settings["url"]
        self.params = settings["params"]

    def get_sunrise_sunset(self):
        url = "{}?lat={}&lng={}&date={}&formatted={}&tzId={}".format(self.url, self.params["lat"], self.params["lng"],
                                                                     self.params["date"], self.params["formatted"],
                                                                     self.params["tzId"])
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            return response.json()
        else:
            return None


if __name__ == '__main__':
    with open("./settings.json") as jsonFile:
        settings = json.load(jsonFile)
        jsonFile.close()

    sunriseSunsetAPI = SunriseSunsetAPI(settings["sunrise_sunset_api"])
    print(sunriseSunsetAPI.get_sunrise_sunset())


