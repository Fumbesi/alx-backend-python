#!/usr/bin/env python3

import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time

# Test the coroutine
async def main():
    return await measure_runtime()

# Run the test
print(asyncio.run(main()))
