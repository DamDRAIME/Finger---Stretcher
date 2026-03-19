# https://leetcode.com/problems/add-two-numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

from typing import Optional


def addTwoNumbers(l1: Optional["ListNode"], l2: Optional["ListNode"]) -> Optional["ListNode"]:
    if not l1 and not l2:
        return None
    return addTwoNumbers_(l1, l2)


def addTwoNumbers_(l1: Optional["ListNode"], l2: Optional["ListNode"], carry: int = 0) -> "ListNode":
    res = carry
    if not l1 and not l2:
        return ListNode(res) if res else None
    if l1:
        res += l1.val
        l1 = l1.next
    if l2:
        res += l2.val
        l2 = l2.next
    carry = res // 10
    return ListNode(res % 10, addTwoNumbers_(l1, l2, carry))
