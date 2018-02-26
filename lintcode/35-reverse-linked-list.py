"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """

    def reverse(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        new_head = head
        cur = head.next
        new_head.next = None

        while cur is not None:
            nxt = cur.next
            cur.next = new_head
            new_head = cur
            cur = nxt

        return new_head
