# https://leetcode.com/problems/search-insert-position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.


def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    t = target - 0.01
    m = None
    while l < r and m != (m := ((l + r) // 2)):
        if nums[m] > t:
            r = m
        else:
            l = m
    if nums[r] < target:
        return r + 1
    return r
