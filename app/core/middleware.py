import time

from fastapi import Request

from app.core.logging import get_logger

logger = get_logger(__name__)


async def request_logging_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round((time.time() - start_time) * 1000, 2)

    logger.info(
        "method=%s path=%s status_code=%s process_time_ms=%s",
        request.method,
        request.url.path,
        response.status_code,
        process_time
    )

    return response