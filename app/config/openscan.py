from typing import Any
from app.config.camera import CameraSettings
from app.config.motor import MotorConfig
from app.config.scanner import ScannerConfig
from app.config.cloud import OpenScanCloudConfig


class OpenScanConfig:
    def __init__(self):
        OpenScanConfig.reload()

    @classmethod
    def reload(cls):
        cls.scanner = ScannerConfig(turntable_mode=False)
        cls.cloud = OpenScanCloudConfig("", "", "", "")
        cls.cameras: dict[str, CameraSettings] = OpenScanConfig._get_camera_configs()
        cls.motors: dict[str, MotorConfig] = {
            "tt": OpenScanConfig._load_motor_config("turntable"),
            "rotor": OpenScanConfig._load_motor_config("rotor"),
        }

    @staticmethod
    def _load_motor_config(name: str) -> MotorConfig:
        return {}

    @staticmethod
    def _load_camera_config(name: str) -> CameraSettings:
        return {}

    @staticmethod
    def _get_camera_configs() -> "dict[str, CameraSettings]":
        return {}
