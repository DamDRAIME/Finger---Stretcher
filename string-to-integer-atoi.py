# https://leetcode.com/problems/string-to-integer-atoi

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.


def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
    sign = s[0] == "-"
    if s[0] in ("-", "+"):
        s = s[1:]
    n = len(s)
    digits = ""
    i = 0
    while i < n and s[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        if not digits and s[i] == "0":
            i += 1
        else:
            digits += s[i]
            i += 1
    if not digits:
        return 0
    res = int(digits)
    bound = 2**31
    if res >= 2**31:
        res = bound - (1 if not sign else 0)
    return res * (-1 if sign else 1)
