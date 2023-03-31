#!/usr/bin/python3
""" Minimum operations questions
"""


def minOperations(n: int) -> int:
    """ Finds the minimum operations needed
        to result in exactly nH characters in
        a file
    """
    available_chars = 1
    pending_chars = n - 1
    copied_chars = 0
    ops = 0

    while (pending_chars > 0):
        if copied_chars and pending_chars % available_chars:
            pending_chars -= copied_chars
            available_chars += copied_chars
            ops += 1
            continue
        if available_chars < pending_chars:
            copied_chars = available_chars
        else:
            copied_chars = pending_chars
        available_chars += copied_chars
        pending_chars -= copied_chars
        ops = ops + 2
    return ops
