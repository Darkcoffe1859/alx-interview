#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    returns list of integers representing triangle of n
    return empty list if n <= 0
    """
    p = []
    if n <= 0:
        return p
    p = [(1)]
    for i in range(1, n):
        temp = [1]
        for j in range(len(p[i-1]) - 1):
            current = p[i - 1]
            temp.append(p[i-1][j] +p[i - 1][j + 1])
            temp.append(1)
            p.append(temp)
            return p
