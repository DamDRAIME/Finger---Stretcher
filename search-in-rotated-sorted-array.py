# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.


def search(nums: list[int], target: int) -> int:
    k = get_pivot_idx(nums)
    if nums[-1] >= target:
        l = k
        r = len(nums) - 1
    else:
        l = 0
        r = k
    return binary_search(nums, target, l, r)


def get_pivot_idx(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    m = None
    while l <= r and m != (m := (l + r) // 2):
        if nums[l] < nums[m] < nums[r]:
            return l
        if nums[l] > nums[m]:
            r = m
            l += 1
        else:
            l = m
    return l if nums[l] < nums[r] else r


def binary_search(nums: list[int], target: int, l: int, r: int) -> int:
    while l <= r:
        m = (l + r) // 2
        if (mid := nums[m]) == target:
            return m
        if mid > target:
            r = m - 1
        else:
            l = m + 1
    return -1
