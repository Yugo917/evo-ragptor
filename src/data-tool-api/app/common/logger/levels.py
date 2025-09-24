from __future__ import annotations
from enum import Enum

class LogLevel(Enum):
    TRACE = 10
    DEBUG = 20
    INFO = 30
    WARNING = 40
    ERROR = 50
    CRITICAL = 60

    def short(self) -> str:
        return {
            LogLevel.TRACE: "TRC",
            LogLevel.DEBUG: "DBG",
            LogLevel.INFO: "INF",
            LogLevel.WARNING: "WRN",
            LogLevel.ERROR: "ERR",
            LogLevel.CRITICAL: "CRT",
        }[self]
