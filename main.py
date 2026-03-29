from fastapi import FastAPI
from products.api import products_api

app = FastAPI()
app.include_router(products_api)
