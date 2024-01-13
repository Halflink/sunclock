import requests


class SunriseSunsetAPI:

    def __init__(self, settings, oledHandler):
        # CONSTANTS
        self.url = settings["url"]
        self.params = settings["params"]
        self.is_get_sunrise_sunset_successful = False

        self.oledHandler = oledHandler

    def get_sunrise_sunset(self, date_str):
        self.oledHandler.set_line_1("Calling API")
        self.oledHandler.set_line(self.url)
        url = "{}?lat={}&lng={}&date={}&formatted={}&tzId={}".format(self.url, self.params["lat"], self.params["lng"],
                                                                     date_str, self.params["formatted"],
                                                                     self.params["tzId"])
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            self.oledHandler.clear_lines()
            self.is_get_sunrise_sunset_successful = True
            return response.json()
        else:
            self.oledHandler.set_line_1("ERR API")
            self.is_get_sunrise_sunset_successful = False
            return None



