"""Class for controlling the the dht temp humid reader"""
from dht import DHT11
import time

class SensorDHT11():
    def __init__(self, pin):
        self.temperature: int = 0
        self.humidity: int = 0
        self.prev_time_stamp = time.time()
        self.hum_temp_pin = DHT11(pin)
        self.hum_temp_pin.measure()
    def have_x_sec_passed(self,x):
        has_passed = False
        current_timestamp = time.time()
        if (self.prev_time_stamp < current_timestamp - 5):
            self.prev_time_stamp = current_timestamp
            has_passed = True
        return has_passed
    def measure_temp(self):
        if (self.have_x_sec_passed(5)):
            temp = self.hum_temp_pin.temperature()
            return temp
        return None