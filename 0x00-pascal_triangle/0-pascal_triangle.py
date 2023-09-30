#!/usr/bin/python3
"""
 0-pascal_triangle.py
"""


def pascal_triangle(n):
    """ function that returns a list of lists of integers representing the
    Pascals triangle of n:

    Args:
        n: number of integers
    """

    if n < 0:
        return []

    while (n >= 0):
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1, 1]]
        else:
            new_list = [[1], [1, 1]]
            for i in range(2, n):
                new_list.append([1])
                for j in range(1, i):
                    new_list[i].append(new_list[i - 1][j - 1] +
                                       new_list[i - 1][j])
                new_list[i].append(1)
            return new_list
