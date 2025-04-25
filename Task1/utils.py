import time
from functools import wraps
import asyncio

from consts import MAX_NUMBER


def timer_decorator(message):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"Выполнено с использованием: {message}")
            print(f"Сумма: {result}")
            print(f"Время: {end_time - start_time:.10f} секунд")
            return result
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"Выполнено с использованием: {message}")
            print(f"Сумма: {result}")
            print(f"Время: {end_time - start_time:.10f} секунд")
            return result
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    return decorator

def get_end_index(i, chunk_size, num):
    if i < num - 1:
        return (i + 1) * chunk_size + 1
    return MAX_NUMBER + 1
