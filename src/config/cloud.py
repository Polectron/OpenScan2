from dataclasses import dataclass


@dataclass
class OpenScanCloudConfig:
    server: str
    user: str
    password: str
    token: str
