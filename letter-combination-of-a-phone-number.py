# https://leetcode.com/problems/letter-combinations-of-a-phone-number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.


def letterCombinations(digits: str) -> list[str]:
    map = {
        "2": list("abc"),
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz"),
    }
    res = map[digits[0]]
    for d in digits[1:]:
        new_res = []
        for r in res:
            for n in map[d]:
                new_res.append(r + n)
        res = new_res
    return res
