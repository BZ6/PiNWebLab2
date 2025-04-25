import asyncio

from consts import MAX_NUMBER, NUM_TASKS
from utils import timer_decorator, get_end_index


async def calculate_sum(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

async def main():
    tasks = []
    chunk_size = MAX_NUMBER // NUM_TASKS

    @timer_decorator("async")
    async def exec():
        for i in range(NUM_TASKS):
            start = i * chunk_size + 1
            end = get_end_index(i, chunk_size, NUM_TASKS)
            
            task = asyncio.create_task(calculate_sum(start, end))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        return sum(results)

    await exec()

if __name__ == "__main__":
    asyncio.run(main())
