# https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such
# that the sum is closest to target. Returns the sum of the three integers


def threeSumClosest(nums: list[int], target: int) -> int:
    closest = None
    diff = None
    nums.sort()
    for i, x in enumerate(nums[:-2]):
        for j, y in enumerate(nums[i + 1 : -1], start=i + 1):
            array = nums[j + 1 :]
            value = target - (x + y)
            z = binarySearchClosest(array, value)
            s = x + y + z
            d = abs(s - target)
            if closest is None:
                closest = s
                diff = d
                continue
            if d < diff:
                closest = s
                diff = d
    return closest


def binarySearchClosest(array: list[int], value: int) -> int:
    n = len(array)
    if n == 1:
        return array[0]
    if n == 2:
        x, y = array
        return y if abs(x - value) > abs(y - value) else x
    l = 0
    r = n - 1
    mid = n // 2
    while r - l > 1:
        x = array[mid]
        if x == value:
            return value
        if x > value:
            r = mid
            mid -= (r - l) // 2
        else:
            l = mid
            mid += (r - l) // 2
    x, y = array[l], array[r]
    if abs(x - value) > abs(y - value):
        return y
    return x
