from fastapi import APIRouter
from app.services.conversion_services import convert_currency_amount_service_api


router = APIRouter()


@router.get('/convert')
async def convert(frm: str, to: str, amount: float):
    """
        this endpoint converts curreny rates from one to another
    """
    try:
        converted_currency_result = await convert_currency_amount_service_api(amount, frm, to)
    except Exception as e:
        raise e
    else:
        result = {
            "original_amount": amount,
            "from_currency": frm,
            "to_currency": to,
            "resulting_amount": converted_currency_result['rates'][to]
        }
        return result
