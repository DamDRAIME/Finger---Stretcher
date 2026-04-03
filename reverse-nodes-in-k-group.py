# https://leetcode.com/problems/reverse-nodes-in-k-group

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.


from typing import Optional


def reverseKGroup(head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
    if not head:
        return None
    if k == 1:
        return head
    prev_link = ListNode(next=head)
    new_head = None
    counter = 0

    while head:
        if counter == k - 1:
            h, t = reverse_linked_list(prev_link.next, head, k)
            prev_link.next = h
            prev_link = t
            head = t
            counter = -1
            if new_head is None:
                new_head = h
        counter += 1
        head = head.next

    return new_head


def reverse_linked_list(head: "ListNode", tail: "ListNode", length: int) -> tuple["ListNode", "ListNode"]:
    if length == 2:
        temp = tail.next
        tail.next = head
        head.next = temp
        return tail, head
    if length == 3:
        temp = tail.next
        tail.next = head.next
        tail.next.next = head
        head.next = temp
        return tail, head
    inner_tail = head.next
    j = 0
    while j < length - 3:
        inner_tail = inner_tail.next
        j += 1
    inner_head, inner_tail = reverse_linked_list(head.next, inner_tail, length - 2)
    temp = tail.next
    tail.next = inner_head
    inner_tail.next = head
    head.next = temp
    return tail, head
