#!/usr/bin/python3
""" Prime Game Problem
    Topic: Eratosthenes algorithm
"""
from typing import List


def isWinner(x: int, nums: List[int]) -> str:
    """
    Determines the winner in the prime game using
    Eratosthenes prime sieving algorithm
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        if nums[round] == 1:
            Ben += 1
            continue
        playing_numbers = [num for num in range(2, nums[round] + 1)]
        index = 0

        while (index < len(playing_numbers)):
            current_prime = playing_numbers[index]
            sieve_index = index + current_prime
            while(sieve_index < len(playing_numbers)):
                playing_numbers.pop(sieve_index)
                sieve_index += current_prime - 1
            index += 1
        prime_count = (len(playing_numbers))
        if prime_count % 2:
            Maria += 1
        else:
            Ben += 1

    return 'Ben' if Ben > Maria else 'Maria'
