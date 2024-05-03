#!/usr/bin/env python3
"""Function Type-annotated  make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies the float"""
    return lambda x: x * multiplier
