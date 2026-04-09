# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value. If target is not found in the array, return [-1, -1].


def searchRange(nums: list[int], target: int) -> list[int]:
    not_found = [-1, -1]
    n = len(nums) - 1
    if n == -1:
        return not_found
    if n == 0:
        if nums[0] == target:
            return [0, 0]
        return not_found

    eps = 0.1

    l = proxy_binary_search(nums, target - eps)
    l = look_at_neighbors(nums, target, l)
    if l == -1:
        return not_found

    r = proxy_binary_search(nums, target + eps)
    r = look_at_neighbors(nums, target, r)

    return [l, r]


def look_at_neighbors(nums: list[int], target: int, idx: int) -> int:
    x = nums[idx]
    if x != target:
        idx += -1 if x > target else 1
        if not (len(nums) > idx >= 0) or nums[idx] != target:
            return -1
    return idx


def proxy_binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    m = None
    while l <= r and m != (m := (l + r) // 2):
        if nums[m] > target:
            r = m
        else:
            l = m
    return r
