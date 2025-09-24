from __future__ import annotations
from typing import Mapping, Any, Optional
from time import perf_counter

from starlette.middleware.base import BaseHTTPMiddleware  # External: Starlette middleware base
from starlette.requests import Request  # External: Starlette request
from starlette.responses import Response

from app.common.logger.interfaces import ILogger  # External: Starlette response


class HttpLoggerMiddleware(BaseHTTPMiddleware):
    """
    Logs each HTTP request/response using the provided ILogger.

    Template:
    "HTTP {httpMethod} {httpUrl} responded {httpResponseStatusCode} in {httpElapsed} ms"
    """

    def __init__(self, app, logger: ILogger) -> None:
        super().__init__(app)  # External: Starlette BaseHTTPMiddleware initialization
        self._logger = logger

    async def dispatch(self, request: Request, call_next) -> Response:
        start = perf_counter()
        try:
            response = await call_next(request)  # External: Starlette delegates to next handler
            status_code: int = response.status_code
        except Exception as exc:
            elapsed_ms = int((perf_counter() - start) * 1000)
            self._logger.error(
                "HTTP {httpMethod} {httpUrl} responded {httpResponseStatusCode} in {httpElapsed} ms",
                {
                    "httpMethod": request.method,
                    "httpUrl": str(request.url),
                    "httpResponseStatusCode": 500,
                    "httpElapsed": elapsed_ms,
                },
            )
            # Also emit the exception with structured conversion for troubleshooting
            self._logger.error("Unhandled request exception", exc)
            raise

        elapsed_ms = int((perf_counter() - start) * 1000)
        self._logger.info(
            "HTTP {httpMethod} {httpUrl} responded {httpResponseStatusCode} in {httpElapsed} ms",
            {
                "httpMethod": request.method,
                "httpUrl": str(request.url),
                "httpResponseStatusCode": status_code,
                "httpElapsed": elapsed_ms,
            },
        )
        return response
