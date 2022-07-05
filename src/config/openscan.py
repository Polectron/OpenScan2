from dataclasses import dataclass
from config.camera import CameraConfig

from config.motor import MotorConfig


@dataclass
class OpenScanConfig:
    rotor: MotorConfig
    tt: MotorConfig
    ring_light_pin: int
    cameras: list[CameraConfig]
