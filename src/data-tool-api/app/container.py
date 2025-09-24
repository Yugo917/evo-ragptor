# app/container.py
from __future__ import annotations
from dependency_injector import containers, providers

from app.common.logger.interfaces import ILogger
from app.common.logger.mega_logger import MegaLogger
from app.common.logger.sinks.uvicorn_sink import UvicornSink
from app.common.logger.sinks.elastic_sink import ElasticConfig, ElasticSink


from app.common.middleware.http_logger_middleware import HttpLoggerMiddleware
from app.math.business.math_service import MathService
from app.text.business.text_comparer import TextComparer


def _add_http_logger_middleware(app, logger: ILogger) -> None:
    # External: FastAPI/Starlette middleware registration
    app.add_middleware(HttpLoggerMiddleware, logger=logger)


class Container(containers.DeclarativeContainer):
    # External: DI wiring config
    wiring_config = containers.WiringConfiguration(packages=["app"])

    # External: configuration object
    config = providers.Configuration()

    # Sinks
    uvicorn_sink = providers.Singleton(UvicornSink)
    elastic_config = providers.Singleton(
        ElasticConfig,
        host="localhost",
        port=9400,
        index="data-tool-api",
        verify_certs=False,
        scheme="http",
        username=None,
        password=None,
        request_timeout=3.0,
    )
    elastic_sink = providers.Singleton(ElasticSink, config=elastic_config)

    logger: ILogger = providers.Singleton(
        MegaLogger,
        sinks=providers.List(uvicorn_sink, elastic_sink),
    )

    # Middleware setup callable (à invoquer dans main.py)
    http_logger_setup = providers.Callable(
        _add_http_logger_middleware,
        app=providers.Dependency(),
        logger=logger,
    )

    # Services
    math_service = providers.Factory(MathService)
    text_comparer = providers.Singleton(TextComparer)
