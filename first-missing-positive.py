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
        if x > 0 and x <= n_pos:
            if x < i:
                nums[x - 1] = -1
            else:
                while True:
                    y = nums[x - 1]
                    nums[x - 1] = -1
                    if y > 0 and y <= n_pos:
                        if y <= i:
                            nums[y - 1] = -1
                            break
                        else:
                            x, y = y, nums[y - 1]
                    else:
                        break

    for i, x in enumerate(nums, 1):
        if x == 0:
            return i

    return n_pos + 1
