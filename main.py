from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as authentication_router
from conversations.routes import router as convesation_roter
app = FastAPI()

# middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # allow all origins
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(router=authentication_router, prefix="/users")
app.include_router(router=convesation_roter, prefix="/chat")

if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=8000)