import logging

from pydub import AudioSegment
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

@app.get("/api/test")
def health() -> dict:
    audio = AudioSegment.from_file("test.m4a", format="m4a")
    new_filename = "1_test.mp3"
    audio.export(new_filename, format="mp3", bitrate="64k")
    return {"info": "I'm done"}