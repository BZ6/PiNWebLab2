import aiohttp
import asyncio
import time

from urls import urls
from parse_and_save_async import parse_and_save_async
from connection_async import init_db_async


async def main():
    await init_db_async()
    
    async with aiohttp.ClientSession() as session:
        tasks = [parse_and_save_async(url, session) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Async execution time: {end_time - start_time} seconds")
