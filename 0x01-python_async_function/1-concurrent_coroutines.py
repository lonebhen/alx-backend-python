#!/usr/bin/env python3

"""Concurrent coroutines"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function returns list"""

    tmp = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    waiting_time = [await task for task in asyncio.as_completed(tmp)]
    return waiting_time
