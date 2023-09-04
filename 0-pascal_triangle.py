#!/usr/bin/python3
from typing import List


def pascal_triangle(n: int) -> List:
    """
        Function that returns a list of integers representing
        the pascals triangle
        :param n: int
        :return: List
    """
    if n <= 0:
        return []
    else:
        triangle = [[1]]

        for i in range(1, n):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(1, i):
                new_element = prev_row[j - 1] + prev_row[j]
                new_row.append(new_element)

            new_row.append(1)
            triangle.append(new_row)

        return triangle
