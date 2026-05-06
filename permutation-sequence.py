# https://leetcode.com/problems/permutation-sequence

# Given n and k, return the kth permutation sequence.


def getPermutation(n: int, k: int) -> str:
    perm, n_iter = smart_init(n, k)
    for _ in range(n_iter):
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


def smart_init(n: int, k: int) -> tuple[list[int], int]:
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    n_1_fact = factorial(n - 1)
    start_num = (k // n_1_fact) + int(bool(k % n_1_fact))
    perm = [start_num] + [x for x in range(1, n + 1) if x != start_num]
    return perm, k - ((start_num - 1) * n_1_fact) - 1
