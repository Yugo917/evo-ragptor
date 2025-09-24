from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any, Mapping
from elasticsearch import Elasticsearch
from ..models import LogEvent

@dataclass(frozen=True)
class ElasticConfig:
    host: str
    port: int
    index: str
    scheme: str = "http"
    username: Optional[str] = None
    password: Optional[str] = None
    verify_certs: bool = False
    request_timeout: float = 3.0 

class ElasticSink:
    """KISS: 1 event = 1 index() vers Elasticsearch."""
    def __init__(self, config: ElasticConfig) -> None:
        self._cfg = config
        http_auth = None
        if self._cfg.username and self._cfg.password:
            http_auth = (self._cfg.username, self._cfg.password)

        self._client = Elasticsearch(
            hosts=[{"host": self._cfg.host, "port": self._cfg.port, "scheme": self._cfg.scheme}],
            http_auth=http_auth,
            verify_certs=self._cfg.verify_certs,
            request_timeout=self._cfg.request_timeout,
        )

    def emit(self, event: LogEvent) -> None:
        doc: dict[str, Any] = {
            "@timestamp": event.timestamp_iso,
            "level": event.level.name.lower(),
            "message": event.rendered_message,
        }
        if event.message_template:
            doc["messageTemplate"] = event.message_template
        if event.properties:
            for k, v in event.properties.items():
                doc[k] = v

        try:
            # TODO optim with bulk
            self._client.index(index=self._cfg.index, body=doc)
        except Exception as e:
            # pass
            raise 
