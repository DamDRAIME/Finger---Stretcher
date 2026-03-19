# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.


def longestPalindrome(s: str) -> str:
    n = len(s)
    longest = 0
    res = ""
    i = 1
    while i < n - (longest // 2):
        x = s[i]
        j, k = i - 1, i + 1
        while j >= 0 and s[j] == x:
            if (curr_len := i - j) > longest:
                longest = curr_len
                res = s[j : i + 1]
            j -= 1
        j = max(0, j)
        while k < n and s[k] == x:
            if (curr_len := k - j + int(s[j] == x)) > longest:
                longest = curr_len
                res = s[j + int(s[j] != x) : k + 1]
            k += 1
        k = min(n - 1, k)
        while j >= 0 and k < n:
            if s[j] == s[k]:
                if (curr_len := k - j + 1) > longest:
                    longest = curr_len
                    res = s[j : j + curr_len]
                j -= 1
                k += 1
            else:
                break
        i += 1
    return res if res else s[0]
