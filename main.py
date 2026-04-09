from contextlib import asynccontextmanager
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from products.api import products_api
from migrations.apply_migrations import main as apply_migrations


@asynccontextmanager
async def lifespan(app: FastAPI):
    await apply_migrations()
    yield


app = FastAPI(lifespan=lifespan)

# Configure CORS. Set `FRONTEND_ORIGINS` env var to a comma-separated list
# (e.g. "http://localhost:3000,http://localhost:5173") or "*" for all.
_frontend_origins = os.getenv("FRONTEND_ORIGINS")
print(_frontend_origins)
origins = [o.strip() for o in (_frontend_origins or "").split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_api)
