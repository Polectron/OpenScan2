from dataclasses import dataclass
from typing import Optional

from app.config.motor import MotorConfig

@dataclass
class Motor:
    name: str

    settings: Optional[MotorConfig]
