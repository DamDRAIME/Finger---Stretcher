# https://leetcode.com/problems/regular-expression-matching

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# - '.' Matches any single character.​​​​
# - '*' Matches zero or more of the preceding element.
# Return a boolean indicating whether the matching covers the entire input string (not partial).


def isMatch(s: str, p: str) -> bool:
    if p == ".*":
        return True
    if not p and s:
        return False
    if not p and not s:
        return True
    if len(p) == 1:
        return (p == "." and len(s) == 1) or p == s
    if p[1] != "*":
        return len(s) > 0 and (p[0] == "." or p[0] == s[0]) and isMatch(s[1:], p[1:])
    # ?* case
    # Not used
    if isMatch(s, p[2:]):
        return True
    # Exhausted
    for i in range(1, len(s) + 1):
        if not (s[i - 1] == p[0] or p[0] == "."):
            return False
        if isMatch(s[i:], p[2:]):
            return True
    return False
