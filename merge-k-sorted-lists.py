# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import Optional


def mergeKLists(lists: list[Optional["ListNode"]]) -> Optional["ListNode"]:
    lists = [ln for ln in lists if ln]
    if not lists or not lists[0]:
        return None
    head = None
    pointer = None
    while lists:
        j = 0
        min_node = lists[j]
        for i, x in enumerate(lists[1:], 1):
            if x.val < min_node.val:
                min_node = x
                j = i
        if not head:
            head = ListNode(min_node.val)
            pointer = head
        else:
            pointer.next = ListNode(min_node.val)
            pointer = pointer.next
        lists.pop(j)
        if min_node.next is not None:
            lists.append(min_node.next)

    return head
