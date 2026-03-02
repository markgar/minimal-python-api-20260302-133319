import logging
from fastapi import FastAPI
from app.routers import health

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(health.router)
