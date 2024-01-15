#!/usr/bin/env python3
"""
Function task_wait_random that returns an asyncio.Task.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random with the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: Task for wait_random.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
