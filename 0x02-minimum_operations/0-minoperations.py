#!/usr/bin/python3
""" Minimum operations questions
"""


def minOperations(n: int) -> int:
    """ Finds the minimum operations needed
        to result in exactly nH characters in
        a file
    """
    if n <= 0:
        return 0
    available_characters = 1
    pending_characters = n - 1
    copied_characters = 0
    ops = 0

    while (pending_characters):
        if copied_characters and pending_characters % available_characters:
            pending_characters -= copied_characters
            available_characters += copied_characters
            ops += 1
            continue
        if available_characters <= pending_characters:
            copied_characters = available_characters
        else:
            copied_characters = pending_characters
        pending_characters -= copied_characters
        available_characters += copied_characters
        ops = ops + 2

    if available_characters == n:
        return ops
    return 0
