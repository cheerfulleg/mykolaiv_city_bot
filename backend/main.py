from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.base_router import base_router
from config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base_router)
