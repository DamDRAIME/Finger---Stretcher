# https://leetcode.com/problems/spiral-matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    res = []
    m = len(matrix)
    n = len(matrix[0])
    l, r, u, b = 0, n, 0, m
    d = "right"
    prev_l = None
    while prev_l != (prev_l := len(res)):
        if d == "right":
            res.extend(matrix[u][l:r])
            u += 1
            d = "down"
        elif d == "down":
            res.extend([x[r - 1] for x in matrix[u:b]])
            r -= 1
            d = "left"
        elif d == "left":
            res.extend(matrix[b - 1][l:r][::-1])
            b -= 1
            d = "up"
        elif d == "up":
            res.extend([x[l] for x in matrix[u:b]][::-1])
            l += 1
            d = "right"
    return res
