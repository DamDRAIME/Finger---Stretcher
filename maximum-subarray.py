# https://leetcode.com/problems/maximum-subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.


def maxSubArray(nums: list[int]) -> int:
    best = nums[0]
    for i in range(len(nums)):
        curr_best = 0
        for x in nums[i:]:
            curr_best += x
            if curr_best > best:
                best = curr_best
    return best
