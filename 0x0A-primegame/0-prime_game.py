#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    nums.sort()
    primes = [True for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    player = 0
    for n in nums:
        player += primes[n] % 2 == 1
    if player * 2 == len(nums):
        return None
    if player * 2 > len(nums):
        return "Maria"
    return "Ben"
