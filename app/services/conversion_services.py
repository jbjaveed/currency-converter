from fastapi import HTTPException
import aiohttp
import os


async def convert_currency_amount_service_api(amount, frm, to):
    """
        api for currency amount conversion
    """ 
    conversion_url = os.getenv("CURRENCY_CONVERSION_API_URL")
    conversion_full_url = conversion_url+'?amount='+str(amount)+'&from='+frm+'&to='+to

    async with aiohttp.ClientSession() as session:
        async with session.get(conversion_full_url) as response:
            if response.status == 200:
                return await response.json()
            if response.status == 404:
                raise HTTPException(status_code=400, detail="unsupported currency code. check docs for supported currencies")
            raise HTTPException(status_code=404, detail="some error occured")
