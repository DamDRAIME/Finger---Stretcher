# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional


def removeNthFromEnd(head: Optional["ListNode"], n: int) -> Optional["ListNode"]:
    q = [head]
    i = 1
    x = head
    while x.next is not None:
        q.append(x.next)
        if len(q) > (n + 1):
            q.pop(0)
        i += 1
        x = x.next
    if n == i:
        q.pop(0)
        return q[0] if q else None
    q[0].next = q[2] if n > 1 else None
    return head
