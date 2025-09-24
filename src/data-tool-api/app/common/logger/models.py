from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Any, Optional
from .levels import LogLevel

@dataclass(frozen=True)
class LogEvent:
    timestamp_iso: str
    level: LogLevel
    message_template: Optional[str]
    rendered_message: str
    properties: Mapping[str, Any]
