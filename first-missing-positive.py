# https://leetcode.com/problems/first-missing-positive

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


def firstMissingPositive(nums: list[int]) -> int:
    n_pos = 0
    n = len(nums)
    for i, x in enumerate(nums):
        if x > 0 and x <= n:
            n_pos += 1
        elif x == -1:
            nums[i] = 0

    for i, x in enumerate(nums):
        if x == -1:
            continue
        nums[i] = 0
        while True:
            if x > 0 and x <= n_pos:
                temp = nums[x - 1]
                nums[x - 1] = -1
                if x <= i:
                    break
                else:
                    x = temp
            else:
                break

    for i, x in enumerate(nums, 1):
        if x == 0:
            return i

    return n_pos + 1
