from machine import Pin, PWM
from time import sleep_ms
class Motor():
    MAX_DUTY_CYCLE = 65535
    def __init__(self, pin_x : Pin, pin_y : Pin, pin_pwm : Pin) -> None:
        self.IN_X = pin_x
        self.IN_Y = pin_y
        self.pwm = PWM(pin_pwm, freq = 500)
        self.set_speed()
    def forward(self) -> None:
        self.IN_X.value(0) 
        self.IN_Y.value(0)
        sleep_ms(50) # Pause to let motor easy into direction in case the previously was the opposite direction
        self.IN_X.value(1) 
        self.IN_Y.value(0) 

    def reverse(self) -> None:
        self.IN_X.value(0) 
        self.IN_Y.value(0)
        sleep_ms(50) # Pause to let motor easy into direction in case the previously was the opposite direction
        self.IN_X.value(0)
        self.IN_Y.value(1) 

    def stop(self) -> None:
        self.IN_X.value(0) 
        self.IN_Y.value(0) 

    def set_speed(self, multiplier : float = 0.8):
        if multiplier < 0.5:
            multiplier = 0.5
        elif multiplier > 1:
            multiplier = 1
        self.current_duty_cycle = int(self.MAX_DUTY_CYCLE * multiplier)
        self.pwm.duty_u16(self.current_duty_cycle)

    def get_speed(self):
        return self.current_duty_cycle / self.MAX_DUTY_CYCLE


