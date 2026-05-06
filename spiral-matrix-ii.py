# https://leetcode.com/problems/spiral-matrix-ii

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


def generateMatrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    y, x = 0, 0
    l, r, b, u = 0, 0, 0, 0
    direction = "right"
    for z in range(1, (n * n) + 1):
        matrix[y][x] = z
        if direction == "right":
            if x < n - r - 1:
                x += 1
                continue
            direction = "down"
            y += 1
            u += 1
        elif direction == "down":
            if y < n - b - 1:
                y += 1
                continue
            direction = "left"
            x -= 1
            r += 1
        elif direction == "left":
            if x > l:
                x -= 1
                continue
            direction = "up"
            y -= 1
            b += 1
        elif direction == "up":
            if y > u:
                y -= 1
                continue
            direction = "right"
            x += 1
            l += 1
    return matrix
