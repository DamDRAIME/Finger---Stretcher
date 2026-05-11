# https://leetcode.com/problems/rotate-list

# Given the head of a linked list, rotate the list to the right by k places.

from typing import Optional


def rotateRight(head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
    if k == 0 or not head:
        return head
    n = 1
    cursor = head
    while next := cursor.next:
        n += 1
        cursor = next
    if n == 1:
        return head
    k = k % n
    if k == 0:
        return head
    n_k = n - k - 1
    cutoff = head
    for _ in range(n_k):
        cutoff = cutoff.next
    new_head = cutoff.next
    cutoff.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    return new_head
