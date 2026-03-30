# https://leetcode.com/problems/integer-to-roman

# Given an integer, convert it to a Roman numeral.


def intToRoman(num: int) -> str:
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    integers = [1, 5, 10, 50, 100, 500, 1000, 9999]
    if num == 0:
        return ""
    num_l = list(str(num))
    pow = len(num_l) - 1
    num_f = int(num_l[0])
    for idx, i in enumerate(integers):
        if num < i:
            if num_f == 4:
                return f"{romans[idx-1]}{romans[idx]}" + intToRoman(num - 4 * 10**pow)
            if num_f == 9:
                return f"{romans[idx-2]}{romans[idx]}" + intToRoman(num - 9 * 10**pow)
            return romans[idx - 1] + intToRoman(num - integers[idx - 1])
