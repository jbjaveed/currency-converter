
from fastapi import APIRouter
from app.api.v1.routes import currency_conversion


router = APIRouter()

router.include_router(currency_conversion.router)
