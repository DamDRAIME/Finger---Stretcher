# https://leetcode.com/problems/substring-with-concatenation-of-all-words

# You are given a string s and an array of strings words. All the strings of words are of the same length.


PERMUTATIONS = set()


def findSubstring(s: str, words: list[str]) -> list[int]:
    get_permutations(words)
    perm_len = len(next(iter(PERMUTATIONS)))
    n = len(s)
    idx = []
    i = 0
    while i <= n - perm_len:
        if s[i : i + perm_len] in PERMUTATIONS:
            idx.append(i)
        i += 1
    return idx


def get_permutations(words: list[str]) -> None:
    for word in words:
        generate_permutations(word)
    PERMUTATIONS = set("".join(p) for p in PERMUTATIONS)


def generate_permutations(word: str) -> None:
    if len(PERMUTATIONS) == 0:
        PERMUTATIONS = {(word,)}
        return
    perms = set()
    for permutation in PERMUTATIONS:
        for i in range(len(permutation) + 1):
            perms.add(permutation[:i] + (word,) + permutation[i:])
    PERMUTATIONS = perms
