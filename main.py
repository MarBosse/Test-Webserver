import logging
import os

from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

app_resources = {}


# ------------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):

    yield
    app_resources.clear()


# ------------------------------------------------------------------------------
app = FastAPI(lifespan=lifespan)


# ------------------------------------------------------------------------------
@app.get("/api/health")
def health() -> dict:
    logging.info("Health endpoint processed a request.")
    return {"info": "I'm healthy"}