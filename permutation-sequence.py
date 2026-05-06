# https://leetcode.com/problems/permutation-sequence

# Given n and k, return the kth permutation sequence.


def getPermutation(n: int, k: int) -> str:
    perm = list(range(1, n + 1))
    for _ in range(k - 1):
        next_permutation(perm, n)
    return "".join(map(str, perm))


def next_permutation(perm: list[int], n: int):
    for r in range(n - 1, 0, -1):
        if (pivot := perm[r - 1]) < perm[r]:
            for i in range(n - 1, r - 1, -1):
                if perm[i] > pivot:
                    perm[i], perm[r - 1] = pivot, perm[i]
                    break
            k = n - 1
            while r < k:
                perm[r], perm[k] = perm[k], perm[r]
                r += 1
                k -= 1
            return
    perm.reverse()
