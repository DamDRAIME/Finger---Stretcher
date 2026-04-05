# https://leetcode.com/problems/next-permutation

# Given an array of integers nums, find the next lexicographically greater permutation of nums.


def nextPermutation(nums: list[int]) -> None:
    n = len(nums)
    for i in range(n - 1, 0, -1):
        if (pivot := nums[i - 1]) < nums[i]:
            for j in range(n - 1, i - 1, -1):
                if nums[j] > pivot:
                    nums[i - 1], nums[j] = nums[j], pivot
                    break
            k = n - 1
            while i < k:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k -= 1
            return
    nums.reverse()
