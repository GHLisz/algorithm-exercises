"""
206. Reverse Linked List
Easy


Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def iterative(head):
            pre = None
            while head:
                cur = head
                head = head.next
                cur.next = pre
                pre = cur
            return pre

        def recursive(head):
            if head is None or head.next is None:
                return head
            new_head = recursive(head.next)
            head.next.next = head
            head.next = None
            return new_head

        return recursive(head)
