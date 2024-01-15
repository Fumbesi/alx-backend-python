#!/usr/bin/env python3
"""
Async routine wait_n that takes in 2 int arguments (n and max_delay).
It spawns wait_random n times with the specified max_delay.
Returns the list of all the delays (float values) in ascending order.
"""

import asyncio
from typing import List

# Import the wait_random coroutine from the previous file
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Use asyncio.gather to concurrently execute wait_random n times
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    
    # Return the sorted list of delays
    return sorted(delays)


if __name__ == "__main__":
    # Test the wait_n coroutine
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
