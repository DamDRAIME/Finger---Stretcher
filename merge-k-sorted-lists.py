# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import Optional


def mergeKLists(lists: list[Optional["ListNode"]]) -> Optional["ListNode"]:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        temp_lists = []
        while len(lists) > 1:
            temp_lists.append(merge_two_sorted_lists(lists.pop(), lists.pop()))
        if lists:
            temp_lists.append(merge_two_sorted_lists(lists.pop(), temp_lists.pop()))
        lists = temp_lists

    return lists[0]


def merge_two_sorted_lists(l1: Optional["ListNode"], l2: Optional["ListNode"]) -> Optional["ListNode"]:
    if not l1:
        return l2
    if not l2:
        return l1

    pointer = ListNode()
    head = pointer
    while l1 and l2:
        if l1.val < l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next
        pointer = pointer.next

    if l1:
        pointer.next = l1
    elif l2:
        pointer.next = l2

    return head.next
