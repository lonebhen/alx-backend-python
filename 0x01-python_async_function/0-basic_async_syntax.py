#!/usr/bin/env python3

"""Python async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait with a delay of max_delay"""
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
