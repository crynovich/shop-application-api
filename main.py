from contextlib import asynccontextmanager
import os
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from products.api import products_api
from migrations.apply_migrations import main as apply_migrations
from core.logging import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up")
    await apply_migrations()
    yield
    logger.info("Shutting down")


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    logger.info(
        "%s %s -> %d (%.1fms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


# Configure CORS. Set `FRONTEND_ORIGINS` env var to a comma-separated list
# (e.g. "http://localhost:3000,http://localhost:5173") or "*" for all.
_frontend_origins = os.getenv("FRONTEND_ORIGINS")
origins = [o.strip() for o in (_frontend_origins or "").split(",") if o.strip()]
logger.info("CORS allowed origins: %s", origins or "(none)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_api)
