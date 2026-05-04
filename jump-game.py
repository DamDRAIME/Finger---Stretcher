# https://leetcode.com/problems/jump-game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in
# the array represents your maximum jump length at that position. Return true if you can reach the last index, or
# false otherwise.


def canJump(nums: list[int]) -> bool:
    n = len(nums)
    to_check = [0] * n
    to_check[0] = 1
    for idx, (check, jumps) in enumerate(zip(to_check, nums)):
        if not check:
            continue
        if to_check[-1] == 1 or idx == n - 1:
            return True
        for jump in range(1, jumps + 1):
            if (jump_idx := idx + jump) >= n:
                return True
            to_check[jump_idx] = 1
    return False
