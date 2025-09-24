from __future__ import annotations
from typing import Mapping, Dict
from traceback import format_exception


class ExceptionConverter:
    """Converts Python exceptions to a flat log-friendly mapping."""

    def convert(self, exc: BaseException) -> Mapping[str, str]:
        message = str(exc) or exc.__class__.__name__
        type_name = f"{exc.__class__.__module__}.{exc.__class__.__name__}"
        stacktrace = "".join(format_exception(type(exc), exc, exc.__traceback__)).rstrip()
        return {
            "exception_message": message,
            "exception_type": type_name,
            "exception_stacktrace": stacktrace,
        }
