#!/usr/bin/env python3
"""
Function task_wait_n that returns a list of asyncio.Tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    """
    Returns a list of asyncio.Tasks for task_wait_random with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[asyncio.Task]: List of tasks for task_wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return tasks

if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    result = asyncio.run(task_wait_n(n, max_delay))

    # Print results
    for task in asyncio.as_completed(result):
        print(await task)

