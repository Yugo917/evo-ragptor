# app/container.py
from dependency_injector import containers, providers

from app.common.logger.interfaces import ILogger
from app.common.logger.mega_logger import MegaLogger
from app.common.logger.sinks.uvicorn_sink import UvicornSink
from app.common.logger.sinks.elastic_sink import ElasticConfig, ElasticSink

from app.math.business.math_service import MathService
from app.text.business.text_comparer import TextComparer


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app"])

    # Configuration externe (à remplir au bootstrap)
    config = providers.Configuration()

    # Sinks
    uvicorn_sink = providers.Singleton(UvicornSink)
    

    elastic_config = providers.Singleton(
        ElasticConfig,
        host="localhost",                 # "localhost" ou "sai-elasticsearch"
        port=9400,        # 9400 (host) / 9200 (docker)
        index="data-tool-api",               # "logs-maga"
        verify_certs=False,
        scheme="http",
        username=None,
        password=None,
        request_timeout=3.0,
    )
    elastic_sink = providers.Singleton(ElasticSink, config=elastic_config)

    logger: ILogger = providers.Singleton(MegaLogger,
        sinks=providers.List(uvicorn_sink, elastic_sink),)

    # Services
    math_service = providers.Factory(MathService)
    text_comparer = providers.Singleton(TextComparer)
