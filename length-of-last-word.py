# https://leetcode.com/problems/length-of-last-word

# Given a string s consisting of words and spaces, return the length of the last word in the string.


def lengthOfLastWord(s: str) -> int:
    lowl = 0
    reset = False
    for x in s:
        if x == " ":
            reset = True
            continue
        if reset:
            lowl = 1
            reset = False
            continue
        lowl += 1
    return lowl
