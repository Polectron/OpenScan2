from dataclasses import dataclass
from typing import Optional

from app.config.scanner import ScannerConfig

@dataclass
class Scanner:
    settings: Optional[ScannerConfig]
