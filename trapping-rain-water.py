# https://leetcode.com/problems/trapping-rain-water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
# water it can trap after raining.


def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    while l < r and height[l] == 0:
        l += 1
    while l < r and height[r] == 0:
        r -= 1
    h = min(height[l], height[r])
    w = 0
    while l < r:
        if height[l] <= h:
            l += 1
            if (v := h - height[l]) > 0:
                w += v
            else:
                h = min(height[l], height[r])
        else:
            r -= 1
            if (v := h - height[r]) > 0:
                w += v
            else:
                h = min(height[l], height[r])
    return w
