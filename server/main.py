
from src.motor import Motor
from src.sensor_dht11 import SensorDHT11
from src.operate_car import OperateCar
from src.night_light import NightLight
import src.keys

from machine import Pin, PWM, ADC
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient

import time
import uasyncio as asyncio

NIGHT_LIGHT_CHECK_TIME = 4 # Seconds
RANDOMS_INTERVAL = 20000    # milliseconds
last_random_sent_ticks = 0  # milliseconds

class AppServer(WebSocketServer):
    def __init__(self, motor1, motor2):
        super().__init__(10)
        self._motor1 = motor1
        self._motor2 = motor2

    def _make_client(self, conn):
        return OperateCar(conn, self._motor1, self._motor2)

# Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
        pass
        # led.on()                 # ... then LED on
    elif msg == b"OFF":          # If message says "OFF" ...
        pass
        # led.off()                # ... then LED off
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.

# Function to publish random number to Adafruit IO MQTT server at fixed interval
def send_temp(temp = 0):
    global last_random_sent_ticks
    global RANDOMS_INTERVAL

    if ((time.ticks_ms() - last_random_sent_ticks) < RANDOMS_INTERVAL):
        return; # Too soon since last one sent.

    print("Publishing: {0} to {1} ... ".format(temp, src.keys.AIO_TEMPERATURE_FEED), end='')
    try:
        client.publish(topic=src.keys.AIO_TEMPERATURE_FEED, msg=str(temp))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_random_sent_ticks = time.ticks_ms()


# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(src.keys.AIO_CLIENT_ID, src.keys.AIO_SERVER, src.keys.AIO_PORT, src.keys.AIO_USER, src.keys.AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(src.keys.AIO_LIGHTS_FEED)
print("Connected to %s, subscribed to %s topic" % (src.keys.AIO_SERVER, src.keys.AIO_LIGHTS_FEED))

async def main_loop():
    ts = time.time()
    while True:
        if ts + NIGHT_LIGHT_CHECK_TIME < time.time():
            night_light.led_control()
            ts = time.time()
        temp = temp_hum.measure_temp()
        client.check_msg()
        if temp:
            send_temp(temp)  # Send a current temp to Adafruit IO if it's time.
        server.process_all()
        await asyncio.sleep(0.1)

try:
    server = AppServer(Motor(Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4)), Motor(Pin(6, Pin.OUT), Pin(7, Pin.OUT), Pin(8)))
    server.start(3000)
    temp_hum = SensorDHT11(Pin(10))
    night_light = NightLight(ADC(27), Pin(17, Pin.OUT), 59000)
    asyncio.run(main_loop())
except KeyboardInterrupt:
    pass
server.stop()

