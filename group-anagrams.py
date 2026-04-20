# https://leetcode.com/problems/group-anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = []
    group__representatives = []
    for x in strs:
        x_s = sorted(x)

        for i, g_repr in enumerate(group__representatives):
            if are_anagrams(x_s, g_repr):
                groups[i].append(x)
                break
        else:
            groups.append([x])
            group__representatives.append(x_s)

    return groups


def are_anagrams(a: list[str], b: list[str]) -> bool:
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x != y:
            return False
    return True
