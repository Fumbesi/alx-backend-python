#!/usr/bin/env python3
"""
Module with task_wait_random function for creating an asyncio.Task.
"""

import asyncio
from typing import Task

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Task:
    """
    Creates an asyncio.Task for wait_random with the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task object.
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
