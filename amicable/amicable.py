"""Amicable number computation.

Two numbers (a, b) are amicable if the sum of proper divisors of a equals b
and the sum of proper divisors of b equals a, where a != b.

Reference: https://en.wikipedia.org/wiki/Amicable_numbers
"""

import math
from typing import Iterator


def sum_of_proper_divisors(n: int) -> int:
    """Return the sum of all proper divisors of n (excluding n itself).

    Uses trial division up to sqrt(n) for O(sqrt(n)) performance.
    """
    if n < 2:
        return 0

    total = 1  # 1 is always a proper divisor for n >= 2
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            total += i
            counterpart = n // i
            if counterpart != i:
                total += counterpart

    return total


def find_amicable_pairs(limit: int) -> Iterator[tuple[int, int]]:
    """Yield all amicable pairs (a, b) where a < b < limit."""
    for a in range(2, limit):
        b = sum_of_proper_divisors(a)
        if b > a and b < limit and sum_of_proper_divisors(b) == a:
            yield a, b


def sum_of_amicable_numbers(limit: int) -> int:
    """Return the sum of all amicable numbers below limit."""
    return sum(a + b for a, b in find_amicable_pairs(limit))


if __name__ == "__main__":
    limit = 10000
    for a, b in find_amicable_pairs(limit):
        print(f"  {a} <-> {b}")
    print(f"Sum of amicable numbers below {limit}: {sum_of_amicable_numbers(limit)}")
