# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)). --> Note satisfied


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    counter = (n1 + n2) // 2
    m1, m2 = 0, 0
    i, j = 0, 0

    while counter >= 0:
        counter -= 1
        m1 = m2
        if i == n1:
            m2 = nums2[j]
            j += 1
        elif j == n2:
            m2 = nums1[i]
            i += 1
        elif nums1[i] < nums2[j]:
            m2 = nums1[i]
            i += 1
        else:
            m2 = nums2[j]
            j += 1

    return float(m2) if n % 2 else (m1 + m2) / 2
