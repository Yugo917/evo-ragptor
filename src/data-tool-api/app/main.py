from fastapi import FastAPI
from app.math.api.endpoints import router as math_router
from app.text.api.endpoints import router as text_router
from app.logging.api.endpoints import router as log_router
from app.container import Container
import logging


import app.math.api.endpoints as math_endpoints
import app.text.api.endpoints as text_endpoints
import app.logging.api.endpoints as log_endpoints

app = FastAPI(title="DATA TOOL API")

# DI container setup
container = Container()
container.config.logger.update({
    "host": "localhost",
    "port": 9400,
    "index": "data-tool-api",
    "verify_certs": False,
})
app.container = container

# Wire resolve dependencys
container.wire(modules=[math_endpoints, text_endpoints, log_endpoints])

# Include both routers
app.include_router(math_router)
app.include_router(text_router)
app.include_router(log_router)

# Log Swagger URL
logger = logging.getLogger("uvicorn")
logger.info("✅ Swagger is available at http://127.0.0.1:8000/docs")
