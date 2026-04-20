# https://leetcode.com/problems/group-anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for x in strs:
        key = "".join(sorted(x))
        groups[key].append(x)

    return list(groups.values())
