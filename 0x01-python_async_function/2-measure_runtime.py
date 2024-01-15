#!/usr/bin/env python3

""" Module documentation """
import asyncio
import time 

wait_n = _import_("1-concurrent_coroutines").wait_n

def measure_time(n: int, max_delay: int) -> float:
    """doc func"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start
