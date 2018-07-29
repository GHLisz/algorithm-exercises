"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        def iterative(head):
            if not head: return head
            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev

        def recursive(head):
            if head is None or head.next is None: return head
            new_head = recursive(head.next)
            head.next.next = head
            head.next = None
            return new_head

        return iterative(head)
