from __future__ import annotations
from typing import Protocol

from app.common.logger.models import LogEvent

class ISink(Protocol):
    def emit(self, event: LogEvent) -> None:
        ...