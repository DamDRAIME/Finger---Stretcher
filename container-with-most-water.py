# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.


def maxArea(height: list[int]) -> int:
    i = 0
    j = len(height) - 1
    best = 0
    while i < j:
        h = min(height[i], height[j])
        if (curr := h * (j - i)) > best:
            best = curr
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return best
