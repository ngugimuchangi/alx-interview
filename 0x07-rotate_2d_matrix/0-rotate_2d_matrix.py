#!/usr/bin/python3
""" 2D Matrix rotation challenge
"""


def rotate_2d_matrix(matrix: list[list]):
    """ Rotates 2D matrix 90 decrease clockwise
        in place
        Args:
            - matrix - 2D matrix
    """
    inward_cycles = int(len(matrix) // 2)
    last_idx = len(matrix) - 1
    for i in range(inward_cycles):
        for j in range(i, len(matrix) - 1 - i):
            matrix[i][j], matrix[j][last_idx - i] = \
                matrix[j][last_idx - i], matrix[i][j]
            matrix[i][j], matrix[last_idx - j][i] = \
                matrix[last_idx - j][i], matrix[i][j]
            matrix[last_idx - j][i], matrix[last_idx - i][last_idx - j] = \
                matrix[last_idx - i][last_idx - j], matrix[last_idx - j][i]
