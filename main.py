from datetime import datetime
from uvicorn import run
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import chat_router
from routes.auth import auth_router

app = FastAPI()

# middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # allow all origins
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(chat_router)
app.include_router(auth_router)


if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=8000)
