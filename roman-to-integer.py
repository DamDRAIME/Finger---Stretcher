# https://leetcode.com/problems/roman-to-integer

# Given a roman numeral, convert it to an integer.


def romanToInt(s: str) -> int:
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    res = 0
    max_idx = len(s) - 1
    s = list(s)
    for idx, x in enumerate(s):
        x_v = mapping[x]
        if idx < max_idx and mapping[s[idx + 1]] > x_v:
            res -= x_v
        else:
            res += x_v
    return res
