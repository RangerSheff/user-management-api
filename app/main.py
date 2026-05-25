from fastapi import FastAPI

from app.api.user_router import router as user_router
from app.core.logging import configure_logging, get_logger
from app.core.middleware import request_logging_middleware
from app.db.database import Base, engine
from app.models.user_model import User  # noqa: F401

# Required for SQLAlchemy metadata registration

configure_logging()
logger = get_logger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    description="FastAPI challenge for Stefanini",
    version="1.0.0",
)

app.middleware("http")(request_logging_middleware)

app.include_router(user_router)


@app.get("/health")
def health_check():
    logger.info("Health check executed")
    return {"status": "OK"}
