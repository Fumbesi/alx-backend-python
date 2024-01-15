#!/usr/bin/env python3
"""
Module with measure_time function for measuring the execution time of wait_n.
"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Average execution time per iteration.
    """
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(asyncio.run(measure_time(n, max_delay)))
