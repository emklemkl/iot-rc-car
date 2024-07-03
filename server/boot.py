"""
Boot file for pico W
"""

import src.keys as keys
import network
from time import sleep
def connect():
    """
    Connect to wifi using keys module
    """
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print("Connecting to network...")
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS) # Your WiFi Credential
        print('Waiting for connection...', end='')
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip

try:
    ip = connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")
