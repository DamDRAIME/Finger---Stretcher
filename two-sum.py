# https://leetcode.com/problems/two-sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    mapping = {}
    for idx, num in enumerate(nums):
        if num in mapping:
            mapping[num].append(idx)
        else:
            mapping[num] = [idx]
    for idx, num in enumerate(nums):
        inv_t = target - num
        if inv_t in mapping and (len(mapping[num]) > 1 if num == inv_t else True):
            inv_idxs = mapping[inv_t]
            for inv_idx in inv_idxs:
                if inv_idx != idx:
                    return [idx, inv_idx]
