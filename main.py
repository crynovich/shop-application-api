from contextlib import asynccontextmanager
from fastapi import FastAPI
from products.api import products_api
from migrations.apply_migrations import main as apply_migrations


@asynccontextmanager
async def lifespan(app: FastAPI):
    await apply_migrations()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(products_api)
