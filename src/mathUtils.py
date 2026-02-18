"""
Math Utilities — helper functions used by the calculator.

This file is WORKING correctly. Don't modify it.
It's here so you can see how multi-file projects work.

Author: Nisha Gupta (Tech Lead)
"""

import math


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min and max."""
    return max(min_val, min(value, max_val))
