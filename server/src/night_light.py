"""Class for controlling the night lights"""

from machine import Pin, ADC

class NightLight():
    def __init__(self, pin_photo, pin_led, threshold = 60000):
        self.photo_res_pin = pin_photo 
        self.led_pin = pin_led  # LED connected to GP15
        self.light_threshold = threshold # when to turn on the nightlight
    def read_photo_light_sensor(self):
        return self.photo_res_pin.read_u16()  # Read the LDR value (0-65535)
    def led_control(self):
        sens_val = self.read_photo_light_sensor()
        print(sens_val)
        if sens_val < self.light_threshold:
            self.led_pin.value(1)  # Turn on LED
        else:
            self.led_pin.value(0)  # Turn off LED   