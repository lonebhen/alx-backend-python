#!/usr/bin/env python3

"""
    Measuring runtime of a function
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Fuction to measure time elapsed"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    elapsed = end - start
    return elapsed/n
