# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def generateParenthesis(n: int) -> list[str]:
    return generate("(", (n - 1, n))


def generate(x: str, para_count: tuple[int, int]) -> list[str]:
    opening, closing = para_count
    if opening == 0 and closing == 0:
        return [x]
    if opening > 0 and closing > opening:
        return generate(x + "(", (opening - 1, closing)) + generate(x + ")", (opening, closing - 1))
    elif opening > 0:
        return generate(x + "(", (opening - 1, closing))
    elif closing > opening:
        return generate(x + ")", (opening, closing - 1))
