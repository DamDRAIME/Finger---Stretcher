# https://leetcode.com/problems/multiply-strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
# represented as a string.


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    mult = [0] * (len(num1) + len(num2))
    offset = 0
    for x in num1[::-1]:
        carry_over = 0
        x = int(x)
        for i, y in enumerate(num2[::-1], offset):
            m = (x * int(y)) + carry_over
            s = mult[i] + (m % 10)
            carry_over = m // 10 + int(s >= 10)
            mult[i] = (s) % 10
        mult[i + 1] += carry_over
        offset += 1
    return "".join(map(str, mult[::-1])).removeprefix("0")
