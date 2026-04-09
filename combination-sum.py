# https://leetcode.com/problems/combination-sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
# of candidates where the chosen numbers sum to target. You may return the combinations in any order.

combinations = []


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    combination_sum(sorted(candidates), [], 0, target)
    return combinations


def combination_sum(candidates: list[int], curr_selection: list[int], curr_sum: int, target: int):
    if not candidates:
        return
    for i, x in enumerate(candidates):
        new_sum = x + curr_sum
        if new_sum == target:
            combinations.append(curr_selection + [x])
        elif new_sum < target:
            combination_sum(candidates[i:], curr_selection + [x], new_sum, target)
        else:
            return
