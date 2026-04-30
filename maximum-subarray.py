# https://leetcode.com/problems/maximum-subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.


def maxSubArray(nums: list[int]) -> int:
    best = nums[0]
    prev = nums[0]
    for x in nums[1:]:
        prev = max(x, prev + x)
        best = max(best, prev)
    return best
