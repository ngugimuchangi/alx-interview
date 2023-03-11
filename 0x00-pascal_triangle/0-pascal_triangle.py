#!/usr/bin/python3
"""
Pascal's triangle module
"""


def factorial(n):
    """ Computes the factorial of n
    """
    if not n:
        return 1
    res = 1
    for num in range(1, n + 1):
        res *= num

    return res


def pascal_triangle(n):
    """ Pascal's triangle generator that uses binomial theorem
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
