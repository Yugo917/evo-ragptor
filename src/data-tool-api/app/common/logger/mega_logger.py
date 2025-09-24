from __future__ import annotations
from typing import Mapping, Any, Iterable, Optional
from dataclasses import dataclass, field
from datetime import datetime

from app.common.logger.sinks.interface import ISink

from .levels import LogLevel
from .models import LogEvent
from .message_template_processor import MessageTemplateProcessor
from .interfaces import ILogger
from .exception_converter import ExceptionConverter


_EXCEPTION_TEMPLATE_SUFFIX = (
    "\n type : {exception_type}"
    "\n message: {exception_message}"
    "\n stacktrace: {exception_stacktrace}"
)


@dataclass
class MegaLogger(ILogger):
    sinks: Iterable[ISink]
    template_processor: MessageTemplateProcessor = field(default_factory=MessageTemplateProcessor)
    exception_converter: ExceptionConverter = field(default_factory=ExceptionConverter)

    # --- Public API ---------------------------------------------------------
    def info(self, template_or_msg: str, props: Optional[Mapping[str, Any]] = None) -> None:
        self._log(LogLevel.INFO, template_or_msg, props)

    def debug(self, template_or_msg: str, props: Optional[Mapping[str, Any]] = None) -> None:
        self._log(LogLevel.DEBUG, template_or_msg, props)

    def warning(self, template_or_msg: str, props: Optional[Mapping[str, Any]] = None) -> None:
        self._log(LogLevel.WARNING, template_or_msg, props)

    def error(
        self,
        template_or_msg: str,
        arg: Optional[object] = None,
        props: Optional[Mapping[str, Any]] = None,
    ) -> None:
        if self._log_if_exception(LogLevel.ERROR, template_or_msg, arg):
            return
        self._log(LogLevel.ERROR, template_or_msg, self._merge_props(arg, props))

    def critical(
        self,
        template_or_msg: str,
        arg: Optional[object] = None,
        props: Optional[Mapping[str, Any]] = None,
    ) -> None:
        if self._log_if_exception(LogLevel.CRITICAL, template_or_msg, arg):
            return
        self._log(LogLevel.CRITICAL, template_or_msg, self._merge_props(arg, props))

    # --- Core ---------------------------------------------------------------
    def _log(self, level: LogLevel, template_or_msg: str, props: Optional[Mapping[str, Any]]) -> None:
        effective_props = dict(props or {})
        rendered, captured = self.template_processor.render(template_or_msg, effective_props)

        evt = LogEvent(
            timestamp_iso=datetime.utcnow(),
            level=level,
            message_template=template_or_msg if (effective_props or "{" in template_or_msg) else None,
            rendered_message=rendered or template_or_msg,
            properties=captured,
        )

        for sink in self.sinks:
            try:
                sink.emit(evt)
            except Exception:
                pass

    # --- Helpers ------------------------------------------------------------
    def _log_if_exception(self, level: LogLevel, base_template: str, arg: Optional[object]) -> bool:
        exc_props = self._maybe_convert_exception(arg)
        if exc_props is None:
            return False
        self._log(level, f"{base_template}{_EXCEPTION_TEMPLATE_SUFFIX}", exc_props)
        return True

    def _maybe_convert_exception(self, arg: Optional[object]) -> Optional[Mapping[str, str]]:
        if isinstance(arg, BaseException):
            return self.exception_converter.convert(arg)
        return None

    def _merge_props(
        self,
        arg: Optional[object],
        props: Optional[Mapping[str, Any]],
    ) -> Mapping[str, Any]:
        if isinstance(arg, dict) and props:
            merged = dict(arg)
            merged.update(props)
            return merged
        if isinstance(arg, dict):
            return arg
        return props or {}
