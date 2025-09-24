from __future__ import annotations
from typing import Mapping, Any, Tuple
import re

_PLACEHOLDER_RE = re.compile(r"\{([a-zA-Z_]\w*)\}")

class MessageTemplateProcessor:
    """
    Serilog-style KISS interpolation:
    - Replaces {name} with props["name"] when present (applies str() to the value).
    - Leaves the placeholder as-is if missing (no exception).
    - Captures the properties used during rendering (flat destructuring).
    - Supports escaping {{ and }} like str.format (normalized before/after).
    """
    def render(self, template: str, props: Mapping[str, Any]) -> Tuple[str, Mapping[str, Any]]:
        if not template:
            return "", {}

        # Handle escapes: {{ -> __LBRACE__, }} -> __RBRACE__
        tmp = template.replace("{{", "__LBRACE__").replace("}}", "__RBRACE__")

        captured: dict[str, Any] = {}
        def _replace(m: re.Match) -> str:
            key = m.group(1)
            if key in props:
                val = props[key]
                captured[key] = val
                return str(val)
            # If missing, keep the original placeholder
            return "{" + key + "}"

        rendered = _PLACEHOLDER_RE.sub(_replace, tmp)
        rendered = rendered.replace("__LBRACE__", "{").replace("__RBRACE__", "}")
        return rendered, captured
