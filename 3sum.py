# https://leetcode.com/problems/3sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    i = 0
    n = len(nums)

    while i < n - 2:

        if i > 0 and nums[i] == nums[i - 1]:
            i += 1
            continue

        j = i + 1
        k = n - 1

        x = nums[i]
        while j < k:
            tot = x + nums[j] + nums[k]
            if tot == 0:
                res.append([x, nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

            elif tot > 0:
                k -= 1
            else:
                j += 1

        i += 1

    return res
