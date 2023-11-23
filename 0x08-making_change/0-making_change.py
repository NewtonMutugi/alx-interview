#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:
            change += total // coin
            total = total % coin
    if total != 0:
        return -1
    return change
