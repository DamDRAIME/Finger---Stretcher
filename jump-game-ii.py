# https://leetcode.com/problems/jump-game-ii

# Return the minimum number of jumps to reach index n - 1

from collections import defaultdict


def jump(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    memory_jumps = defaultdict(lambda: 10**4)
    memory_jumps[n - 1] = 0
    for i in range(n - 2, -1, -1):
        if (x := nums[i]) == 0:
            continue
        next_n_jumps = min(memory_jumps[i + j] for j in range(1, x + 1))
        memory_jumps[i] = next_n_jumps + 1
    return memory_jumps[0]
