from dataclasses import dataclass
from typing import Optional

from src.config.scanner import ScannerConfig

@dataclass
class Scanner:
    settings: Optional[ScannerConfig]
