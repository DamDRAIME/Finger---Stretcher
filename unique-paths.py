# https://leetcode.com/problems/unique-paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
# down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
# bottom-right corner.

from collections import deque


class Solution:
    def uniquePaths(m: int, n: int) -> int:
        n_paths = 0
        queue = deque([(0, 0)])
        while queue:
            pos = queue.pop()
            y, x = pos
            if y == m - 1 and x == n - 1:
                n_paths += 1
                continue
            if y < m - 1:
                queue.append((y + 1, x))
            if x < n - 1:
                queue.append((y, x + 1))
        return n_paths
