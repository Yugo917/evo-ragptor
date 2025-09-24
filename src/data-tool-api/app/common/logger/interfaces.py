from __future__ import annotations
from typing import Protocol, Mapping, Any, Optional

class ILogger(Protocol):
    """Minimal logging contract (KISS), now supporting exception overloads."""

    def debug(self, template_or_msg: str, props: Optional[Mapping[str, Any]] = None) -> None: ...
    def info(self, template_or_msg: str, props: Optional[Mapping[str, Any]] = None) -> None: ...
    def warning(self, template_or_msg: str, props: Optional[Mapping[str, Any]] = None) -> None: ...

    # Accepts either props OR an exception as second positional argument.
    def error(
        self,
        template_or_msg: str,
        arg: Optional[object] = None,
        props: Optional[Mapping[str, Any]] = None,
    ) -> None: ...

    def critical(
        self,
        template_or_msg: str,
        arg: Optional[object] = None,
        props: Optional[Mapping[str, Any]] = None,
    ) -> None: ...