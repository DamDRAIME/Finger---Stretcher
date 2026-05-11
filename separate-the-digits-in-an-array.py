# https://leetcode.com/problems/separate-the-digits-in-an-array

# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in
# nums after separating them in the same order they appear in nums.


def separateDigits(nums: list[int]) -> list[int]:
    digits = []
    for num in nums:
        for digit in str(num):
            digits.append(int(digit))
    return digits
