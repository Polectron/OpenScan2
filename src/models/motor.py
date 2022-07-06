from dataclasses import dataclass
from typing import Optional

from src.config.motor import MotorConfig

@dataclass
class Motor:
    name: str

    settings: Optional[MotorConfig]
