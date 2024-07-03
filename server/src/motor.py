from machine import Pin, PWM
from time import sleep_ms

class Motor():
    MAX_DUTY_CYCLE = 65535
    _all_motors = []
    def __init__(self, pin_x : Pin, pin_y : Pin, pin_pwm : Pin) -> None:
        self.IN_X = pin_x
        self.IN_Y = pin_y
        self.pwm = PWM(pin_pwm, freq = 500)
        self.set_speed()
        self.current_speed_multiplier = 1
        self._all_motors.append(self)

    def forward(self) -> None:
        self.IN_X.value(1) 
        self.IN_Y.value(0) 

    def reverse(self) -> None:
        self.IN_X.value(0)
        self.IN_Y.value(1) 

    def stop(self) -> None:
        self.IN_X.value(0) 
        self.IN_Y.value(0) 

    def set_speed(self, multiplier : float = 1):
        self.current_speed_multiplier = multiplier
        if multiplier < 0.5:
            multiplier = 0.5
        elif multiplier > 1:
            multiplier = 1
        self.current_duty_cycle = int(self.MAX_DUTY_CYCLE * self.current_speed_multiplier)
        self.pwm.duty_u16(self.current_duty_cycle)

    def use_half_speed(self):
        self.current_duty_cycle = int(self.MAX_DUTY_CYCLE * (self.current_speed_multiplier / 2))
        self.pwm.duty_u16(self.current_duty_cycle)

    @classmethod
    def set_same_speed_on_all_motors(cls, new_speed = 0):
        for motor in cls._all_motors:
            if (not new_speed):
                motor.set_speed(motor.current_speed_multiplier)
            else:
                motor.set_speed(new_speed)

    def get_speed(self):
        return self.current_duty_cycle / self.MAX_DUTY_CYCLE


