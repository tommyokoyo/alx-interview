#!/usr/bin/python3
"""
    Minimum Operators
"""


def minOperations(n):
    """
        Calculates the number of operations
        :param n:
        :return:
    """
    if n <= 2:
        return 0
    else:
        min_op = [0] * (n + 1)

        for i in range(2, n + 1):
            min_op[i] = float('inf')

            for j in range(1, i):
                if i % j == 0:
                    min_op[i] = min(min_op[i], min_op[j] + (i // j))

        return min_op[n]
