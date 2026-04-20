# https://leetcode.com/problems/permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any
# order.

permutations = []


def permute(nums: list[int]) -> list[list[int]]:
    permute_(nums, [])
    return permutations


def permute_(nums: list[int], acc: list[int]) -> None:
    global permutations
    if not nums:
        permutations.append(acc)
        return

    for _ in range(len(nums)):
        x = nums.pop(0)
        permute_(nums, acc + [x])
        nums.append(x)
