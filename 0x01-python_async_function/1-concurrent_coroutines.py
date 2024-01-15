#!/usr/bin/env python3
"""
Asynchronous coroutines for concurrent operations.

This module provides two asynchronous coroutines:
- `wait_random`: Waits for a random delay between 0 and max_delay seconds.
- `wait_n`: Spawns `wait_random` n times with a specified max_delay.

These coroutines are intended for concurrent asynchronous operations.

"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
    and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay.
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random` n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    delays.sort()  # Sorting the list in ascending order
    return delays


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
