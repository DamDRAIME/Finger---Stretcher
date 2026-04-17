# https://leetcode.com/problems/jump-game-ii

# Return the minimum number of jumps to reach index n - 1

min_n_jumps = None


def jump(nums: list[int]) -> int:
    jump_count(nums)
    return min_n_jumps


def jump_count(nums: list[int], n_jumps: int = 0) -> None:
    global min_n_jumps
    if len(nums) <= 1:
        min_n_jumps = n_jumps if min_n_jumps is None else min(min_n_jumps, n_jumps)
        return

    x = nums[0]
    if x == 0:
        return

    for j in range(1, x + 1):
        jump_count(nums[j:], n_jumps + 1)
