# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Given a string s, find the length of the longest substring without duplicate characters.

from collections import OrderedDict


def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    seen = OrderedDict()
    for x in s:
        while x in seen:
            seen.popitem(last=False)
        seen[x] = True
        longest = max(longest, len(seen))
    return longest
