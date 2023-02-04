#!/usr/bin/env python3

"""Annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multipier functio"""

    return lambda x: x * multiplier
