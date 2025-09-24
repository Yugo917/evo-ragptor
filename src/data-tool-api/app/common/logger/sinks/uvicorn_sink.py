from __future__ import annotations
import logging
from typing import Optional
from ..models import LogEvent

_LEVEL_MAP = {
    "TRC": logging.DEBUG,
    "DBG": logging.DEBUG,
    "INF": logging.INFO,
    "WRN": logging.WARNING,
    "ERR": logging.ERROR,
    "CRT": logging.CRITICAL,
}

class UvicornSink:
    """SRP: forward events to Uvicorn logger so its colorized formatter applies."""

    def __init__(self, logger_name: str = "uvicorn") -> None:
        self._logger = logging.getLogger(logger_name)  # stdlib logging (Uvicorn handlers/formatters apply)

    def emit(self, event: LogEvent) -> None:
        py_level = _LEVEL_MAP.get(event.level.short(), logging.INFO)

        props = event.properties or {}
        exc = props.get("_exc")  # optional raw exception object if provided
        stack: Optional[str] = props.get("stack")

        if isinstance(exc, BaseException):
            # stdlib logging call with exc_info → Uvicorn colors + traceback
            self._logger.log(py_level, event.rendered_message, exc_info=(type(exc), exc, exc.__traceback__))
            return

        if stack:
            msg = f"{event.rendered_message}\n{stack}"
            # stdlib logging call → Uvicorn colors (traceback already embedded as text)
            self._logger.log(py_level, msg)
            return

        # stdlib logging call → Uvicorn colors
        self._logger.log(py_level, event.rendered_message)
