#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the
other boxes."""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""
    n = len(boxes)
    keys = boxes[0]
    unlocked = [False] * n
    unlocked[0] = True

    while True:
        added_keys = False
        for key in keys:
            if not unlocked[key]:
                unlocked[key] = True
                keys += boxes[key]
                added_keys = True
        if not added_keys:
            break

    return all(unlocked)
