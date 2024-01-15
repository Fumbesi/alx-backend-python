#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
    and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(wait_random()))
    print(loop.run_until_complete(wait_random(5)))
    print(loop.run_until_complete(wait_random(15)))
