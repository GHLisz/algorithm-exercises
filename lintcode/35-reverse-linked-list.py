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
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        cur = head

        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp

        return dummy.next

    # solution 2
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head

        p = head
        head = self.reverse(p.next)
        p.next.next = p
        p.next = None
        return head
