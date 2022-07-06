from src.config.scanner import ScannerConfig
from src.config.cloud import OpenScanCloudConfig


class OpenScanConfig:
    def __init__(self):
        self.scanner = ScannerConfig(ring_light_pin=3)
        self.cloud = OpenScanCloudConfig("", "", "", "")
        self.cameras = {}
        self.motors = {}


config = OpenScanConfig()
