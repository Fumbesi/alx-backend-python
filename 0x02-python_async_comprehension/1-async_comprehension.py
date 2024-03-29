#!/usr/bin/env python3

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]

# Test the coroutine
async def main():
    print(await async_comprehension())

# Run the test
import asyncio
asyncio.run(main())
