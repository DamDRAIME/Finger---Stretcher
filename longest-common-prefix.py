# https://leetcode.com/problems/longest-common-prefix

# Write a function to find the longest common prefix string amongst an array of strings.


def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    prefix = ""
    for xs in zip(*strs):
        i = xs[0]
        for j in xs[1:]:
            if j != i:
                return prefix
        else:
            prefix += i
    return prefix
