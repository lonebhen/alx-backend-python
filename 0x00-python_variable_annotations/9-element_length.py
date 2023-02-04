#!/usr/bin/env python3

"""Annotations"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """returns length of a list of sequence"""
    return [(i, len(i)) for i in lst]
