#!/usr/bin/env python3


"""Python Async"""
import asyncio
import random


async def async_generator():
    """asynchronously wait 1 second, then yield a random number between 10"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        return random.randint(0, 10)
