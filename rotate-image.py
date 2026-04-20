# https://leetcode.com/problems/rotate-image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise), in-place.


def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix[0]) - 1
    for y, row in enumerate(matrix[: (n + 1) // 2]):
        for x, cell in enumerate(row[y : -y - 1], start=y):
            prev = cell
            for _ in range(4):
                x, y = n - y, x
                matrix[y][x], prev = prev, matrix[y][x]
