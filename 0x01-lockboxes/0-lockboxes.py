#!/usr/bin/python3
"""
    Lock boxes
"""
from collections import deque


def canUnlockAll(boxes):
    if not boxes:
        return False
    else:
        n = len(boxes)
        visited = [False] * n
        visited[0] = True

        queue = deque([0])

        while queue:
            current_box = queue.popleft()

            for key in boxes[current_box]:
                if 0 <= key < n and not visited[key]:
                    visited[key] = True
                    queue.append(key)

    return all(visited)
