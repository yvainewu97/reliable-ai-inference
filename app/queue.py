import asyncio
from app.reliability import process_with_retry

class RequestQueue:
    def __init__(self):
        self.queue = asyncio.Queue()
        asyncio.create_task(self.worker())

    async def enqueue(self, data):
        loop = asyncio.get_event_loop()
        future = loop.create_future()
        await self.queue.put((data, future))
        return await future

    async def worker(self):
        while True:
            batch = []
            futures = []

            for _ in range(5):
                item, future = await self.queue.get()
                batch.append(item)
                futures.append(future)

            results = await asyncio.gather(
                *[process_with_retry(item) for item in batch]
            )

            for future, result in zip(futures, results):
                future.set_result(result)

request_queue = RequestQueue()