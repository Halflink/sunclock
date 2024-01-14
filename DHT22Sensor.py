from machine import Pin
import dht


class DHT22Sensor:

    def __init__(self, settings, oledHandler):
        pin = settings["pin"]
        self.measurement_interval = settings["measurement_interval"]
        self.sensor = dht.DHT22(Pin(pin))
        self.oledHandler = oledHandler
        self.last_measurement = None

    def get_measurements(self):
        measurements = []
        try:
            self.sensor.measure()
            measurements.append(self.sensor.temperature())
            measurements.append(self.sensor.humidity())
            return measurements
        except:
            return None

    def print_measurements(self, temperature, humidity):
        text_line_1 = "Temp.: {}".format(temperature)
        self.oledHandler.set_line_1(text_line_1, len(text_line_1)+1)
        self.oledHandler.set_line_2("Hum.: {}%".format(humidity))

    def get_and_show_measurements(self, time_int):
        if self.last_measurement is None\
                or self.last_measurement + self.measurement_interval < time_int:
            measurements = self.get_measurements()
            if measurements is None or len(measurements) <= 0:
                self.oledHandler.set_line("Failed to read sensor")
            else:
                self.print_measurements(measurements[0], measurements[1])
            self.last_measurement = time_int
