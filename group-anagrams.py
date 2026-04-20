# https://leetcode.com/problems/group-anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = []
    fds = []
    for x in strs:
        x_fd = get_freq_dict(x)

        for i, group_fd in enumerate(fds):
            if are_anagrams(x_fd, group_fd):
                groups[i].append(x)
                break
        else:
            groups.append([x])
            fds.append(x_fd)

    return groups


def get_freq_dict(x: str) -> dict[str, int]:
    fd = {}
    for s in x:
        if s in fd:
            fd[s] += 1
        else:
            fd[s] = 1
    return fd


def are_anagrams(a_fd: dict[str, int], b_fd: dict[str, int]) -> bool:
    if len(a_fd) != len(b_fd):
        return False
    for k, v in a_fd.items():
        if b_fd.get(k, None) != v:
            return False
    return True
