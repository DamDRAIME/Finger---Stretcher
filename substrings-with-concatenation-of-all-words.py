# https://leetcode.com/problems/substring-with-concatenation-of-all-words

# You are given a string s and an array of strings words. All the strings of words are of the same length.


from copy import deepcopy


def findSubstring(s: str, words: list[str]) -> list[int]:
    word_len = len(words[0])
    perm_len = word_len * len(words)
    words = get_words_freq(words)
    n = len(s)
    idx = []

    for j in range(word_len):
        i = j
        seen_words = deepcopy(words)
        counter = 0
        while i <= n - perm_len:
            while (w := s[i + counter : i + counter + word_len]) in words and counter < perm_len:
                if seen_words[w] == 0:
                    offset = 0
                    while (pop := s[i + offset : i + offset + word_len]) != w:
                        seen_words[pop] += 1
                        offset += word_len
                    i += offset + word_len
                    counter -= offset
                    continue
                seen_words[w] -= 1
                counter += word_len
            if counter == perm_len:
                idx.append(i)
                seen_words[s[i : i + word_len]] += 1
                counter -= word_len
                i += word_len
            else:
                i += word_len + counter
                seen_words = deepcopy(words)
                counter = 0

    return idx


def get_words_freq(words: list[str]) -> dict[str, int]:
    w = {}
    for word in words:
        if word in w:
            w[word] += 1
        else:
            w[word] = 1
    return w
