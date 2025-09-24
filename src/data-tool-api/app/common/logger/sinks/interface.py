from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol

from app.common.logger.models import LogEvent

class ISink(ABC):
    @abstractmethod
    def emit(self, event: LogEvent) -> None:
        ...