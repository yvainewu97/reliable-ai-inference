from fastapi import FastAPI
from app.queue import request_queue
import time
import uuid

app = FastAPI()

@app.post("/predict")
async def predict(data: dict):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    result = await request_queue.enqueue(data)

    latency = time.time() - start_time

    return {
        "request_id": request_id,
        "result": result,
        "latency": latency
    }