import asyncio
from app.model import mock_model

async def process_with_retry(data, retries=3):
    for _ in range(retries):
        try:
            return mock_model(data)
        except Exception:
            await asyncio.sleep(0.1)
    return fallback_model(data)

def fallback_model(data):
    return {"prediction": "fallback"}