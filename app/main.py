from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv, find_dotenv

import app.api.v1.routes.api as api_v1_router

load_dotenv(find_dotenv())


def get_application():
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_v1_router.router, prefix="/v1")
    return application


app = get_application()
