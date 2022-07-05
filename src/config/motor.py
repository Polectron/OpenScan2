from dataclasses import dataclass


@dataclass
class MotorConfig:
    steps_per_rotation: int
    direction_pin: int
    step_pin: int

    direction = int
    acceleration_ramp: int
    acceleration: int
    delay: int
