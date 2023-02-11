#!/usr/bin/env python3


"""Python Async"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """asynchronously wait 1 second, then yield a random number between 10"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
