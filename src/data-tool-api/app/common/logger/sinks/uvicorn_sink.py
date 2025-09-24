from __future__ import annotations
import logging  # External: stdlib logging

from app.common.logger.sinks.interface import ISink
from ..models import LogEvent

_LEVEL_MAP = {
    "TRC": logging.DEBUG,
    "DBG": logging.DEBUG,
    "INF": logging.INFO,
    "WRN": logging.WARNING,
    "ERR": logging.ERROR,
    "CRT": logging.CRITICAL,
}

class UvicornSink(ISink):
    """SRP: forward events to Uvicorn logger so its colorized formatter applies."""

    def __init__(self, logger_name: str = "uvicorn") -> None:
        self._logger = logging.getLogger(logger_name)  # External: get Uvicorn logger

    def emit(self, event: LogEvent) -> None:
        py_level = _LEVEL_MAP.get(event.level.short(), logging.INFO)
        ts = getattr(event, "timestamp_iso", None)
        prefix = f"{str(ts)}    " if ts is not None else ""
        # External: stdlib logging → Uvicorn formatter/color remains applied
        self._logger.log(py_level, f"{prefix}{event.rendered_message}")
