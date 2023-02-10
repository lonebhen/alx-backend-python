#!/usr/bin/env python3

import asyncio
import random

"""Python async"""


async def wait_random(max_delay: int = 10) -> float:
    """wait with a delay of max_delay"""
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
