#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """minOperations"""
    if n <= 1:
        return 0
    else:
        i = 2
        result = 0
        while i <= n:
            if n % i == 0:
                result += i
                n = n / i
            else:
                i += 1
        return result
