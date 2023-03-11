#!/usr/bin/python3
"""
Pascal's triangle module
"""


def pascal_triangle(n):
    """ Pascal's triangle generator using addition
        Args:
            - n: levels of pascal triangle
        Return:
            - Integer matrix representing pascal triangle
    """
    if n <= 0:
        return []

    pascal_triangle = []
    prev_row = []
    for row in range(n):
        new_row = []
        for num in range(row + 1):
            if num == 0:
                new_row.append(1)
                continue
            try:
                new_row.append(prev_row[num - 1] + prev_row[num])
            except IndexError:
                new_row.append(1)
        prev_row = new_row
        pascal_triangle.append(new_row)
    return pascal_triangle
