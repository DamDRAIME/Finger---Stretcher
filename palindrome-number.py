# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is a palindrome, and false otherwise.


def isPalindrome(x: int) -> bool:
    return isPalindrome_(list(str(x)))


def isPalindrome_(x: list[str]) -> bool:
    if not x or len(x) == 1:
        return True
    if x[0] == x[-1]:
        return isPalindrome_(x[1:-1])
    return False
