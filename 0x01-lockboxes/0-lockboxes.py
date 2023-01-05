#!/usr/bin/python
def canUnlockAll(boxes):
    opened = [0]

    for box in opened:
        keys = boxes[box]
        for key in keys:
            if key not in opened and key < len(boxes):
                opened.append(key)

    return len(opened) == len(boxes)
