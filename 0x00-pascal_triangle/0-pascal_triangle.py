#!/usr/bin/env python3
"""
Pascal's triangle module
"""
from functools import reduce
from typing import List


def factorial(n: int) -> int:
    """ Computes the factorial of n
    """
    if not n:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


def pascal_triangle(n: int) -> List[List[int]]:
    """ Pascal triangle generator that uses binomial theorem
        Args:
            - n: levels of pascal triangle
        Return:
            - Integer matrix representing pascal triangle
    """
    if n <= 0:
        return []
    pascal_triangle = []
    for exponent in range(n):
        row = []
        for k in range(exponent + 1):
            coefficient = (factorial(exponent)
                           / (factorial(exponent - k)
                           * factorial(k)))
            row.append(int(coefficient))
        pascal_triangle.append(row)

    return pascal_triangle
