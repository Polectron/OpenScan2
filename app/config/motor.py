from dataclasses import dataclass


@dataclass
class MotorConfig:
    steps_per_rotation: int
    direction: int
    acceleration_ramp: int
    acceleration: int
    delay: int

    direction_pin: int
    step_pin: int
    enable_pin: int
    endstop_pin: int
