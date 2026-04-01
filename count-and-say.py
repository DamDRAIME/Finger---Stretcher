# https://leetcode.com/problems/count-and-say

# Given a positive integer n, return the nth element of the count-and-say sequence.


def countAndSay(n: int) -> str:
    acc = [1]
    for _ in range(n - 1):
        acc = rle(acc)
    return "".join(map(str, acc))


def rle(x: list[int]) -> list[int]:
    i = 0
    num = x[0]
    ans = []
    n = len(x)
    for j in range(1, n):
        if (y := x[j]) != num:
            ans.append(j - i)
            ans.append(num)
            num = y
            i = j
    ans.append(n - i)
    ans.append(num)
    return ans
