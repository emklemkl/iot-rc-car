from machine import Pin, PWM
from time import sleep_ms
from ws_server import  WebSocketClient
from ws_connection import ClientClosedError
from .motor import Motor
from .night_light import NightLight
import uasyncio as asyncio

class OperateCar(WebSocketClient):
    """
    This class is responsible for executing all the commands of the car.
    """
    led = Pin(16, Pin.OUT)   # led pin initialization for Raspberry Pi Pico W   
    current_instruction = ""
    prev_instruction = "f"
    speaker = Pin(11, Pin.OUT)
    def __init__(self, conn, _motor1, _motor2):
        super().__init__(conn)
        self.motor1 = _motor1
        self.motor2 = _motor2
    def check_for_new_instructions(self):
        """
            Read and flag when the client sends new directional instructions to the car.
        """
        got_new_instruction = False
    
        self.current_instruction = self.connection.read()
        if self.current_instruction:
            self.current_instruction = self.current_instruction.decode("utf-8")
            got_new_instruction = True
        return got_new_instruction

    async def honk(self,duration_on, duration_off, repeat):
        for _ in range(repeat):
            self.speaker.value(1)  # Turn the buzzer on
            await asyncio.sleep(duration_on)  # Keep it on for the specified duration
            self.speaker.value(0)  # Turn the buzzer off
            await asyncio.sleep(duration_off)  # Keep it off for the specified duration

    def check_if_rec_two_chars(self):
        ONE_CHAR = 1
        return len(self.current_instruction) > ONE_CHAR

    def _prevent_instant_direction_change(self, direction):
        if self.prev_instruction == direction:
            self.motor1.stop()
            self.motor2.stop()
            sleep_ms(150)

    def execute_instructions(self):
        try:
            got_new_instruction = self.check_for_new_instructions()
            if got_new_instruction:
                Motor.set_same_speed_on_all_motors() # Sets the speed of all motors to the same value from start.
                got_advanced_instruction = self.check_if_rec_two_chars()
                try:
                    print("Current instruction:", self.current_instruction[0],self.current_instruction[1])
                except:
                    print("Current instruction:", self.current_instruction[0])
                print("Previous instruction:", self.prev_instruction)

                if self.current_instruction[0] == "f":
                    self.led.value(0)
                    self._prevent_instant_direction_change("r")
                    if got_advanced_instruction and self.current_instruction[1] == "R":
                        self.motor2.use_half_speed()
                    elif got_advanced_instruction and self.current_instruction[1] == "L":
                        self.motor1.use_half_speed()
                    self.motor1.forward()
                    self.motor2.forward()
                    
                elif self.current_instruction == "L":
                    self.led.value(0)
                    self._prevent_instant_direction_change("R")
                    self.motor1.reverse()
                    self.motor2.forward()
                elif self.current_instruction == "R":
                    self.led.value(0)
                    self._prevent_instant_direction_change("L")
                    self.motor1.forward()
                    self.motor2.reverse()

                elif self.current_instruction == "s":
                    self.led.value(0)
                    self.motor1.stop()
                    self.motor2.stop()

                elif self.current_instruction[0] == "r":
                    self.led.value(1)
                    self._prevent_instant_direction_change("f")
                    if got_advanced_instruction and self.current_instruction[1] == "R":
                        self.motor2.use_half_speed()
                    elif got_advanced_instruction and self.current_instruction[1] == "L":
                        self.motor1.use_half_speed()
                    self.motor1.reverse()
                    self.motor2.reverse()

                elif self.current_instruction.isdigit():
                    Motor.set_same_speed_on_all_motors(float(self.current_instruction) / 100)
                    if self.prev_instruction == "fR" or self.prev_instruction == "rR":
                        self.motor2.use_half_speed()
                    if self.prev_instruction == "fL" or self.prev_instruction == "rL":
                        self.motor1.use_half_speed()

                elif self.current_instruction == "honk":
                    _honk_task = asyncio.create_task(self.honk(0.1, 0.04, 10))
                if (not self.current_instruction.isdigit()):
                    self.prev_instruction = self.current_instruction
        except ClientClosedError as e:
            print("CientCloseError", e)
            self.connection.close()