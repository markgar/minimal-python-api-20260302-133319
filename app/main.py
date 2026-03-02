import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
