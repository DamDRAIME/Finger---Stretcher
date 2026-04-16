# https://leetcode.com/problems/combination-sum-ii

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
# candidates where the candidate numbers sum to target.

combinations = set()


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    prev_x = None
    for i, x in enumerate(candidates):
        if x == prev_x:
            continue
        if x > target:
            break
        find_combinations(candidates[i + 1 :], target, x, [x])
        prev_x = x
    return list(map(list, combinations))


def find_combinations(candidates: list[int], target: int, curr_sum: int = 0, curr_comb=[]) -> None:
    if curr_sum == target:
        combinations.add(tuple(curr_comb))
        return
    prev_x = None
    for i, x in enumerate(candidates):
        if x == prev_x:
            continue
        if (temp_sum := x + curr_sum) > target:
            return
        find_combinations(candidates[i + 1 :], target, temp_sum, curr_comb + [x])
        prev_x = x
