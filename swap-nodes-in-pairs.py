# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
# the values in the list's nodes (i.e., only nodes themselves may be changed.)

from typing import Optional


def swapPairs(head: Optional["ListNode"]) -> Optional["ListNode"]:
    if head is None or head.next is None:
        return head
    pointer = ListNode()
    new_head = pointer
    while head is not None:
        temp = head.next
        pointer.next = swap(head)
        if not temp:
            break
        pointer = pointer.next.next
        head = temp.next
    return new_head.next


def swap(node: Optional["ListNode"]) -> Optional["ListNode"]:
    if node.next is None:
        return node
    return ListNode(node.next.val, ListNode(node.val))
