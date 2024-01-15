#!/usr/bin/env python3
"""
Asynchronous routine wait_n that takes in 2 int arguments (in this order): n and max_delay.
It spawns wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort() because of concurrency.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(wait_n(5, 5)))
    print(loop.run_until_complete(wait_n(10, 7)))
    print(loop.run_until_complete(wait_n(10, 0)))
